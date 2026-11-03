#!/usr/bin/env python3
"""Сторінка статті ukrjurist.com.ua з експорту Google Docs (HTML).
python3 build_article.py <№> <doc.html>                      -> out/article-<№>.html
python3 build_article.py <№> <doc.html> --post [--update id] -> створює/оновлює ЧЕРНЕТКУ (дочірня сторінка хабу 57)"""
import sys, os, re, json, html, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, '..', '..', '_blog-kit'))
import article_kit as K
from articles import ARTICLES
HUB = 57; SITE = 'https://ukrjurist.com.ua'; AUTHOR = 'Гончарук Вікторія Анатолієвна'
CSS = """
.gv .hero .art-crumbs{margin:0 0 14px;font-size:14px;letter-spacing:.16em;text-transform:uppercase;font-weight:500;color:var(--olive-t)}
.gv .hero .art-crumbs a{color:var(--olive-t);text-decoration:underline;text-underline-offset:3px}
.gv .hero h1.art-h1{font-size:clamp(26px,3.6vw,50px);line-height:1.15}
.gv .art-wrap{max-width:860px;margin:0 auto}
.gv .art-meta{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin:0 0 26px;font-size:15px;color:var(--ink-soft)}
.gv .art-meta .art-tag{display:inline-block;padding:7px 16px;border-radius:999px;background:var(--olive);color:var(--ink);font:600 12px/1 var(--f-body);letter-spacing:.14em;text-transform:uppercase}
.gv .art-body{font-size:18px;line-height:1.75;color:var(--ink)}
.gv .art-body h2{font-family:var(--f-head);font-weight:500;font-size:clamp(24px,3vw,34px);margin:46px 0 16px;color:var(--ink);line-height:1.2}
.gv .art-body h3{font-family:var(--f-head);font-weight:500;font-size:clamp(19px,2.2vw,24px);margin:30px 0 12px;color:var(--olive-t);line-height:1.25}
.gv .art-body p{margin:0 0 16px}
.gv .art-body ul,.gv .art-body ol{margin:0 0 20px;padding-left:1.4em}
.gv .art-body ul{list-style:disc}.gv .art-body ol{list-style:decimal}
.gv .art-body li{margin:0 0 8px}
.gv .art-body a{color:var(--olive-t);text-decoration:underline;text-underline-offset:3px}
.gv .art-table{overflow-x:auto;margin:22px 0 26px;border:1px solid var(--line);border-radius:18px;background:#fff}
.gv .art-body table{border-collapse:collapse;width:100%;min-width:560px;font-size:16px;line-height:1.5}
.gv .art-body th{background:var(--ink);color:var(--cream);text-align:left;padding:12px 14px;font-weight:600}
.gv .art-body td{padding:12px 14px;border-top:1px solid var(--line);vertical-align:top}
.gv .art-body tbody tr:nth-child(even) td{background:rgba(245,240,227,.7)}
.gv .art-back{margin-top:36px;padding-top:24px;border-top:1px solid var(--line)}
.gv .art-back a{font-weight:600;color:var(--olive-t)}
@media(max-width:620px){.gv .art-body{font-size:17px}.gv .art-body h2{margin-top:36px}}
"""
def build(n, doc_html):
    a = [x for x in ARTICLES if x[0] == n][0]
    art = K.convert(doc_html); d, mo, y = a[1].split('.')
    for ph in ('[ДАТА ОНОВЛЕННЯ СТАТТІ]', '[ДАТА ПУБЛІКАЦІЇ ТА ОНОВЛЕННЯ]', '[ДАТА ОНОВЛЕННЯ]', '[ДАТА ПУБЛІКАЦІЇ]'):
        art['body'] = art['body'].replace(ph, a[1])
    s = open(os.path.join(H, 'out/blog-hub.html'), encoding='utf-8').read()
    url = f'{SITE}/blog/{a[2]}/'; desc = art['seo_description'] or a[5]; title = art['title']
    s = re.sub(r'<div class="hero-copy">.*?</div>\s*</div>\s*<svg class="wave"', lambda m: f'<div class="hero-copy"><p class="art-crumbs"><a href="/">Головна</a> / <a href="/blog/">Блог</a></p><h1 class="art-h1">{html.escape(title)}</h1></div>\n  </div>\n  <svg class="wave"', s, count=1, flags=re.S)
    sec = ('<section class="band on-cream" id="article"><div class="wrap"><article class="art-wrap">'
           f'<div class="art-meta"><span class="art-tag">{html.escape(a[3])}</span><time datetime="{y}-{mo}-{d}">{a[1]}</time><span>{html.escape(AUTHOR)}</span></div>'
           f'<div class="art-body">{art["body"]}</div><p class="art-back"><a href="/blog/">← Усі статті блогу</a></p></article></div></section>\n\n')
    i = s.index('<section class="band on-cream" id="articles">'); j = s.index('<section class="band on-cream" id="cta">')
    s = s[:i] + sec + s[j:]
    s = s.replace('<!-- Title: Блог — Гончарук Вікторія Анатолієвна, юрист по кредитам -->', f'<!-- Title: {html.escape(art["seo_title"] or title)} -->')
    s = re.sub(r'<!-- Description: .*? -->', f'<!-- Description: {html.escape(desc)} -->', s, count=1)
    fq = K.faq(art['body'])
    graph = [{"@type": "Article", "headline": title, "description": desc, "inLanguage": "uk", "datePublished": f'{y}-{mo}-{d}T09:00:00+02:00',
              "mainEntityOfPage": url, "author": {"@type": "Person", "@id": f"{SITE}/#person", "name": AUTHOR, "url": SITE + '/'}, "isPartOf": {"@type": "Blog", "url": f'{SITE}/blog/'}}]
    if fq: graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": t}} for q, t in fq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    s = re.sub(r'(<script type="application/ld\+json">).*?(</script>)', lambda m: m.group(1) + ld + m.group(2), s, count=1, flags=re.S)
    i = s.index('</style>'); s = s[:i] + CSS + s[i:]
    return s, art, a
if __name__ == '__main__':
    n = int(sys.argv[1]); page, art, a = build(n, open(sys.argv[2], encoding='utf-8').read())
    os.makedirs(os.path.join(H, 'out'), exist_ok=True); open(os.path.join(H, f'out/article-{n}.html'), 'w', encoding='utf-8').write(page)
    print('built', n, len(page), 'bytes | H1:', art['title'][:60], '| FAQ:', len(K.faq(art['body'])), '| desc:', bool(art['seo_description']))
    if '--post' in sys.argv:
        payload = dict(title=art['title'], slug=a[2], status='draft', template='page-blank', parent=HUB, content=page, excerpt=a[5])
        json.dump(payload, open('/tmp/_art.json', 'w', encoding='utf-8'), ensure_ascii=False)
        pid = sys.argv[sys.argv.index('--update') + 1] if '--update' in sys.argv else ''
        r = subprocess.run(['curl', '-sS', '-m', '120', '-X', 'POST', f'{SITE}/wp-json/wp/v2/pages' + (f'/{pid}' if pid else ''), '-H', 'Content-Type: application/json', '--data-binary', '@/tmp/_art.json'], capture_output=True, text=True)
        try: j = json.loads(r.stdout); print({k: j.get(k) for k in ('id', 'status', 'slug', 'parent', 'template', 'link', 'code', 'message')})
        except Exception: print(r.stdout[:300])
