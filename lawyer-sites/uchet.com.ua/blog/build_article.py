#!/usr/bin/env python3
"""Сторінка статті uchet.com.ua з експорту Google Docs (HTML).
python3 build_article.py <№> <doc.html>                      -> out/article-<№>.html
python3 build_article.py <№> <doc.html> --post [--update id] -> створює/оновлює ЧЕРНЕТКУ (дочірня сторінка хабу 58)"""
import sys, os, re, json, html, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, '..', '..', '_blog-kit'))
import article_kit as K
from articles import ARTICLES
HUB = 58; SITE = 'https://uchet.com.ua'; AUTHOR = 'Борисов Максим Юрійович'
CSS = """
.uc .hero .crumbs{margin-bottom:14px}
.uc .hero h1.art-h1{font-size:clamp(26px,3.6vw,46px);line-height:1.18;max-width:900px}
.uc .art-wrap{max-width:860px;margin:0 auto}
.uc .art-meta{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin:0 0 26px;font-size:14.5px;color:var(--tx2)}
.uc .art-meta .art-tag{display:inline-block;padding:7px 14px;border-radius:999px;background:var(--kh-l);color:var(--dark);font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
.uc .art-body{font-size:17.5px;line-height:1.75;color:var(--tx)}
.uc .art-body h2{font-size:clamp(23px,2.6vw,32px);margin:44px 0 14px;color:var(--dark);line-height:1.2}
.uc .art-body h3{font-size:clamp(18px,1.9vw,22px);margin:28px 0 10px;color:var(--kh-t);line-height:1.3}
.uc .art-body p{margin:0 0 15px}
.uc .art-body ul,.uc .art-body ol{margin:0 0 20px;padding-left:1.4em}
.uc .art-body ul{list-style:disc}.uc .art-body ol{list-style:decimal}
.uc .art-body li{margin:0 0 8px}
.uc .art-body a{color:var(--kh-t);text-decoration:underline;text-underline-offset:3px}
.uc .art-table{overflow-x:auto;margin:22px 0 26px;border:1px solid rgba(13,16,23,.12);border-radius:18px;background:#fff}
.uc .art-body table{border-collapse:collapse;width:100%;min-width:560px;font-size:15.5px;line-height:1.5}
.uc .art-body th{background:var(--dark);color:var(--kh-l);text-align:left;padding:12px 14px;font-weight:600}
.uc .art-body td{padding:12px 14px;border-top:1px solid rgba(13,16,23,.1);vertical-align:top}
.uc .art-body tbody tr:nth-child(even) td{background:var(--panel)}
.uc .art-back{margin-top:34px;padding-top:22px;border-top:1px solid rgba(13,16,23,.12)}
.uc .art-back a{font-weight:700;color:var(--kh-t)}
@media(max-width:620px){.uc .art-body{font-size:16.5px}.uc .art-body h2{margin-top:34px}}
"""
def build(n, doc_html):
    a = [x for x in ARTICLES if x[0] == n][0]
    art = K.convert(doc_html); d, mo, y = a[1].split('.')
    for ph in ('[ДАТА ОНОВЛЕННЯ СТАТТІ]', '[ДАТА ПУБЛІКАЦІЇ ТА ОНОВЛЕННЯ]', '[ДАТА ОНОВЛЕННЯ]', '[ДАТА ПУБЛІКАЦІЇ]'):
        art['body'] = art['body'].replace(ph, a[1])
    s = open(os.path.join(H, 'out/blog-hub.html'), encoding='utf-8').read()
    url = f'{SITE}/blog/{a[2]}/'; desc = art['seo_description'] or a[5]; title = art['title']
    s = re.sub(r'<div class="crumbs">.*?</div>\s*<h1>.*?</h1>\s*<p>.*?</p>\s*<a class="btn"', lambda m: f'<div class="crumbs"><a href="/">Головна</a> / <a href="/blog/">Блог</a></div>\n  <h1 class="art-h1">{html.escape(title)}</h1>\n  <a class="btn"', s, count=1, flags=re.S)
    s = s.replace('Обговорити вашу ситуацію', 'Обговорити вашу ситуацію', 1)
    sec = ('<section id="article"><div class="w"><article class="art-wrap">'
           f'<div class="art-meta"><span class="art-tag">{html.escape(a[3])}</span><time datetime="{y}-{mo}-{d}">{a[1]}</time><span>{html.escape(AUTHOR)}</span></div>'
           f'<div class="art-body">{art["body"]}</div><p class="art-back"><a href="/blog/">← Усі статті блогу</a></p></article></div></section>')
    i = s.index('<section id="articles">'); j = s.index('</section>', i) + len('</section>')
    s = s[:i] + sec + s[j:]
    fq = K.faq(art['body'])
    graph = [{"@type": "Article", "headline": title, "description": desc, "inLanguage": "uk", "datePublished": f'{y}-{mo}-{d}T09:00:00+02:00',
              "mainEntityOfPage": url, "author": {"@type": "Person", "@id": f"{SITE}/#person", "name": AUTHOR, "url": SITE + '/'}, "isPartOf": {"@type": "Blog", "url": f'{SITE}/blog/'}}]
    if fq: graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": t}} for q, t in fq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    s = re.sub(r'(<script type="application/ld\+json">).*?(</script>)', lambda m: m.group(1) + '\n' + ld + '\n' + m.group(2), s, count=1, flags=re.S)
    i = s.index('</style>'); s = s[:i] + CSS + s[i:]
    return s, art, a
if __name__ == '__main__':
    n = int(sys.argv[1]); page, art, a = build(n, open(sys.argv[2], encoding='utf-8').read())
    os.makedirs(os.path.join(H, 'out'), exist_ok=True); open(os.path.join(H, f'out/article-{n}.html'), 'w', encoding='utf-8').write(page)
    print('built', n, len(page), 'bytes | H1:', art['title'][:60], '| FAQ:', len(K.faq(art['body'])), '| desc:', bool(art['seo_description']))
    if '--post' in sys.argv:
        payload = dict(title=art['title'], slug=a[2], status='draft', template='page-landing', parent=HUB, content=page, excerpt=a[5])
        json.dump(payload, open('/tmp/_art.json', 'w', encoding='utf-8'), ensure_ascii=False)
        pid = sys.argv[sys.argv.index('--update') + 1] if '--update' in sys.argv else ''
        r = subprocess.run(['curl', '-sS', '-m', '120', '-X', 'POST', f'{SITE}/wp-json/wp/v2/pages' + (f'/{pid}' if pid else ''), '-H', 'Content-Type: application/json', '--data-binary', '@/tmp/_art.json'], capture_output=True, text=True)
        try: j = json.loads(r.stdout); print({k: j.get(k) for k in ('id', 'status', 'slug', 'parent', 'template', 'link', 'code', 'message')})
        except Exception: print(r.stdout[:300])
