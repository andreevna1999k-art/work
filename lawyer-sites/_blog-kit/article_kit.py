#!/usr/bin/env python3
"""Конвертер статті з експорту Google Docs (HTML) у чисту розмітку і збірка сторінки статті в стилі сайту.
Використання: див. lawyer-sites/<сайт>/blog/build_article.py. Нічого не публікує на живих сторінках."""
import re, json, html, urllib.parse
from html.parser import HTMLParser

PLACEHOLDER = re.compile(r'\[(?:ІЗОБРАЖЕННЯ|ЗОБРАЖЕННЯ|ФОТО|ИЗОБРАЖЕНИЕ)[^\]]*\]', re.I)

def _clean_href(h):
    if not h: return ''
    if h.startswith('https://www.google.com/url?'):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(h).query).get('q')
        if q: h = q[0]
    return h

class _Conv(HTMLParser):
    """Google Docs HTML -> чисті h1/h2/h3/p/ul/ol/li/table/a/strong."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []; self.meta = {}; self.title = ''
        self.stack = []; self.buf = None; self.started = False
        self.in_h = 0; self.bold = 0; self.a_stack = []; self.skip_list = False; self.after_zmist = False
        self.skip_depth = 0; self.table_depth = 0; self.row = 0; self.in_thead = False; self.list_depth = 0; self.li_depth = 0; self.cell = None
    # -- допоміжне
    def w(self, s):
        (self.buf if self.buf is not None else self.out).append(s)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); st = a.get('style', '')
        if tag == 'h1': self.begin('h1'); return
        if tag in ('h2', 'h3'): self.begin(tag); return
        if tag == 'p':
            if self.li_depth or self.cell is not None:   # p в li/td -> inline, але з пробілом між абзацами
                self.w(' '); return
            self.begin('p'); return
        if tag in ('span', 'a') and self.skip_depth:
            self.stack.append(None); return
        if tag == 'span':
            if 'font-weight:700' in st and not self.in_h:
                self.w('<strong>'); self.bold += 1; self.stack.append('strong')
            else: self.stack.append(None)
            return
        if tag == 'a':
            href = _clean_href(a.get('href', ''))
            if href.startswith('#') or not href: self.stack.append(None); return
            ext = href.startswith('http')
            self.w(f'<a href="{html.escape(href, quote=True)}"' + (' target="_blank" rel="noopener"' if ext else '') + '>'); self.stack.append('a'); return
        if tag in ('ul', 'ol'):
            if self.skip_list or self.skip_depth:
                self.skip_list = False; self.skip_depth += 1; return
            self.list_depth += 1; self.w(f'<{tag}>'); self.stack.append(tag); return
        if tag == 'li':
            if self.skip_depth: return
            self.li_depth += 1; self.w('<li>'); self.stack.append('li'); return
        if tag == 'table':
            self.table_depth += 1; self.row = 0; self.w('<div class="art-table"><table>'); self.stack.append('table'); return
        if tag in ('thead', 'tbody'): return          # Google Docs віддає зламані thead/tbody: будуємо свої
        if tag == 'tr':
            self.row += 1
            self.w('<thead><tr>' if self.row == 1 else ('<tr>' if self.row > 1 else '<tr>')); return
        if tag in ('td', 'th'):
            self.cell = 'th' if self.row == 1 else 'td'; self.w(f'<{self.cell}>'); return
        if tag == 'br': self.w(' ')
    def begin(self, tag):
        self.buf = []; self.cur = tag
        if tag in ('h2', 'h3', 'h1'): self.in_h = 1
        self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in ('h1', 'h2', 'h3', 'p') and self.buf is not None and self.stack and self.stack[-1] == tag:
            self.stack.pop(); inner = ''.join(self.buf); self.buf = None; self.in_h = 0
            self.finish(tag, inner); return
        if tag == 'span' and self.stack:
            t = self.stack.pop()
            if t == 'strong': self.w('</strong>'); self.bold -= 1
            return
        if tag == 'a' and self.stack:
            t = self.stack.pop()
            if t == 'a': self.w('</a>')
            return
        if tag in ('ul', 'ol') and self.skip_depth:
            self.skip_depth -= 1; return
        if tag in ('ul', 'ol') and self.stack:
            t = self.stack.pop()
            self.list_depth -= 1; self.w(f'</{tag}>'); return
        if tag == 'li' and self.skip_depth: return
        if tag == 'li' and self.stack:
            t = self.stack.pop()
            if t == 'li': self.li_depth -= 1; self.w('</li>')
            return
        if tag in ('td', 'th'):
            if self.cell: self.w(f'</{self.cell}>'); self.cell = None
            return
        if tag == 'tr':
            self.w('</tr></thead><tbody>' if self.row == 1 else '</tr>'); return
        if tag in ('thead', 'tbody'): return
        if tag == 'table' and self.stack:
            self.stack.pop(); self.table_depth -= 1; self.w('</tbody></table></div>' if self.row > 1 else '</table></div>'); return
    def handle_data(self, data):
        d = data.replace('\xa0', ' ')
        if not d.strip() and (self.buf is None): return
        if self.buf is None and self.cell is None and not self.li_depth: return
        self.w(html.escape(d, quote=False))
    def finish(self, tag, inner):
        text = re.sub(r'<[^>]+>', '', inner).strip()
        text = html.unescape(text)
        if tag == 'p':
            m = re.match(r'(Title|Description)\s*:\s*(.*)$', text, re.S | re.I)
            if m and not self.started:
                self.meta[m.group(1).lower()] = m.group(2).strip(); return
            if not self.started: return
            inner = PLACEHOLDER.sub('', inner).strip(); text = PLACEHOLDER.sub('', text).strip()
            if not text: return
            if text.lower() == 'зміст': self.skip_list = True; return
            if re.match(r'^Автор:\s', text) and False: return
            self.out.append(f'<p>{inner}</p>'); return
        if tag == 'h1':
            self.started = True; self.title = text; return
        if not self.started: return
        if not text: return
        self.out.append(f'<{tag}>{html.escape(text, quote=False)}</{tag}>')

def convert(doc_html):
    body = re.search(r'<body[^>]*>(.*)</body>', doc_html, re.S).group(1)
    c = _Conv(); c.feed(body)
    out = '\n'.join(c.out)
    # id для h2/h3
    n = [0]
    def add_id(m):
        n[0] += 1; return f'<{m.group(1)} id="s{n[0]}">'
    out = re.sub(r'<(h[23])>', add_id, out)
    return dict(title=c.title, seo_title=c.meta.get('title', ''), seo_description=c.meta.get('description', ''), body=out)

def faq(body):
    """Пари (питання, відповідь) із розділу «Часті запитання»: h3 після h2 з таким заголовком."""
    m = re.search(r'<h2[^>]*>[^<]*(?:Часті запитання|Часті питання|Поширені запитання|Поширені питання|Питання та відповіді|Питання й відповіді|FAQ)[^<]*</h2>(.*?)(?=<h2|$)', body, re.S | re.I)
    if not m: return []
    pairs = []
    for q, a in re.findall(r'<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|$)', m.group(1), re.S):
        ans = re.sub(r'<[^>]+>', ' ', a); ans = html.unescape(re.sub(r'\s+', ' ', ans)).strip()
        qq = html.unescape(re.sub(r'<[^>]+>', '', q)).strip()
        if ans and qq.endswith('?'): pairs.append((html.unescape(re.sub(r'<[^>]+>', '', q)).strip(), ans))
    return pairs

ART_CSS = """
.bz .art-wrap{max-width:860px;margin:0 auto}
.bz .art-meta{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin:0 0 26px;font-size:15px;color:var(--ink-soft)}
.bz .art-meta .art-tag{display:inline-block;padding:6px 16px;border-radius:999px;background:rgba(212,178,122,.3);color:var(--brown);font-size:12px;letter-spacing:.1em;text-transform:uppercase;font-weight:600}
.bz .art-body{font-size:18px;line-height:1.75;color:var(--ink)}
.bz .art-body h2{font-size:clamp(24px,3vw,34px);margin:46px 0 16px;color:var(--brown);text-transform:none;letter-spacing:.01em}
.bz .art-body h3{font-size:clamp(19px,2.2vw,24px);margin:30px 0 12px;color:var(--brown-2);text-transform:none;letter-spacing:.01em}
.bz .art-body p{margin:0 0 16px}
.bz .art-body ul,.bz .art-body ol{margin:0 0 20px;padding-left:1.4em}
.bz .art-body li{margin:0 0 8px}
.bz .art-body a{color:var(--maroon);text-decoration:underline;text-underline-offset:3px}
.bz .art-body a:hover{color:var(--maroon-600)}
.bz .art-table{overflow-x:auto;margin:22px 0 26px;border:1px solid var(--line);border-radius:18px;background:#fff}
.bz .art-body table{border-collapse:collapse;width:100%;min-width:560px;font-size:16px;line-height:1.5}
.bz .art-body th{background:var(--brown);color:var(--cream);text-align:left;padding:12px 14px;font-weight:600}
.bz .art-body td{padding:12px 14px;border-top:1px solid var(--line);vertical-align:top}
.bz .art-body tbody tr:nth-child(even) td{background:rgba(244,230,208,.35)}
.bz .art-back{margin-top:36px;padding-top:24px;border-top:1px solid var(--line)}
.bz .art-back a{font-weight:600;color:var(--maroon)}
.bz .rp-head .art-crumbs{margin:0 0 14px;font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold)}
.bz .rp-head .art-crumbs a{color:var(--gold)}
.bz .rp-head h1.art-h1{font-size:clamp(26px,4vw,46px);text-transform:none;letter-spacing:.01em;line-height:1.18}
.bz .rp-head h1.art-h1::after{margin-top:20px}
@media(max-width:620px){.bz .art-body{font-size:17px}.bz .art-body h2{margin-top:36px}}
"""

# ---------- збірка сторінки статті ----------
def build_page(hub_html, art, meta):
    """hub_html: готовий html хабу сайту (каркас: шапка, футер, стилі). art: результат convert(). meta: dict(
        site_url, slug, date_iso, topic, author_name, author_id, tg, cta_title, cta_text, announce)."""
    s = hub_html
    title = art['title']; url = f"{meta['site_url']}/blog/{meta['slug']}/"
    desc = art['seo_description'] or meta.get('announce', '')
    # 1) шапка сторінки (rp-head)
    a = s.index('<div class="rp-head">'); b = s.index('</div>', s.index('rp-count', a)) + len('</div>')
    head = (f'<div class="rp-head"><p class="art-crumbs"><a href="/">Головна</a> / <a href="/blog/">Блог</a></p>'
            f'<h1 class="art-h1">{html.escape(title)}</h1></div>')
    s = s[:a] + head + s[b:]
    # 2) основний блок замість сітки карток
    a = s.index('<section id="articles">'); b = s.index('<section><div class="wrap">\n<div class="panel pad rp-cta">')
    date_txt = '.'.join(reversed(meta['date_iso'][:10].split('-')))
    art_sec = ('<section id="article"><div class="wrap"><div class="panel on-white pad res-panel"><article class="art-wrap">'
               f'<div class="art-meta"><span class="art-tag">{html.escape(meta["topic"])}</span><time datetime="{meta["date_iso"][:10]}">{date_txt}</time><span>{html.escape(meta["author_name"])}</span></div>'
               f'<div class="art-body">{art["body"]}</div>'
               '<p class="art-back"><a href="/blog/">← Усі статті блогу</a></p></article></div></div></section>\n\n')
    s = s[:a] + art_sec + s[b:]
    # 3) CTA
    s = re.sub(r'<h2>Потрібна допомога з кредитом\?</h2>\s*<p class="lead">.*?</p>', f'<h2>{html.escape(meta["cta_title"])}</h2>\n  <p class="lead">{html.escape(meta["cta_text"])}</p>', s, count=1, flags=re.S)
    # 4) meta + JSON-LD
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(desc, quote=True)}">', s, count=1)
    fq = faq(art['body'])
    graph = [{"@type": "Article", "headline": title, "description": desc, "inLanguage": "uk", "datePublished": meta['date_iso'],
              "mainEntityOfPage": url, "author": {"@id": meta['author_id']}, "isPartOf": {"@type": "Blog", "url": f"{meta['site_url']}/blog/"}}]
    if fq:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a_}} for q, a_ in fq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    s = re.sub(r'(<script type="application/ld\+json">).*?(</script>)', lambda m: m.group(1) + ld + m.group(2), s, count=1, flags=re.S)
    # 5) стилі
    i = s.index('</style>'); s = s[:i] + ART_CSS + s[i:]
    # 6) прибрати нав'язану підсвітку пункту «Блог» не потрібно: лишаємо, бо це розділ блогу
    return s
