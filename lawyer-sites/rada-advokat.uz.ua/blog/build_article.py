#!/usr/bin/env python3
"""Сторінка статті rada-advokat.uz.ua з експорту Google Docs (HTML).
python3 build_article.py <№> <doc.html>                       -> out/article-<№>.html
python3 build_article.py <№> <doc.html> --post [--update id]  -> створює/оновлює ЧЕРНЕТКУ (дочірня сторінка хабу 1942)"""
import sys, os, re, json, html, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, '..', '..', '_blog-kit'))
import article_kit as K
from articles import ARTICLES
HUB = 1942; SITE = 'https://rada-advokat.uz.ua'
AUTHOR = 'Кравченко Максим Віталійович'
CSS = """
#kr .rp-hero .art-crumbs{margin:0 0 14px;font-size:13px;letter-spacing:.09em;text-transform:uppercase;font-weight:700;color:var(--sky)}
#kr .rp-hero .art-crumbs a{color:var(--sky)}
#kr .rp-hero .art-h1{font-size:clamp(22px,3.3vw,44px);line-height:1.18;max-width:980px}
#kr .art-card{background:#fff;border-radius:var(--r1);padding:clamp(22px,3.4vw,56px);max-width:940px;margin:0 auto}
#kr .art-meta{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin-bottom:26px;font-size:14px;color:var(--muted);font-weight:600}
#kr .art-meta .art-tag{display:inline-block;padding:7px 16px;border-radius:999px;background:var(--sky);color:var(--navy);font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:800}
#kr .art-body{font-size:clamp(16px,1.15vw,18px);line-height:1.75;color:var(--ink)}
#kr .art-body h2{font-size:clamp(19px,1.9vw,28px);margin:40px 0 14px;color:var(--ink)}
#kr .art-body h3{font-size:clamp(16px,1.4vw,20px);margin:28px 0 10px;color:var(--blue)}
#kr .art-body p{margin:0 0 14px;color:var(--muted);font-weight:500}
#kr .art-body ul,#kr .art-body ol{margin:0 0 18px;padding-left:1.4em;list-style:revert}
#kr .art-body ul{list-style:disc}#kr .art-body ol{list-style:decimal}
#kr .art-body li{margin:0 0 7px;color:var(--muted);font-weight:500;list-style:inherit}
#kr .art-body a{color:var(--lime);border-bottom:1px solid rgba(0,70,113,.35)}
#kr .art-table{overflow-x:auto;margin:22px 0 26px;border:1px solid var(--line);border-radius:18px;background:#fff}
#kr .art-body table{border-collapse:collapse;width:100%;min-width:560px;font-size:15px;line-height:1.5}
#kr .art-body th{background:var(--navy);color:#fff;text-align:left;padding:12px 14px;font-weight:700}
#kr .art-body td{padding:12px 14px;border-top:1px solid var(--line);vertical-align:top;color:var(--muted);font-weight:500}
#kr .art-body tbody tr:nth-child(even) td{background:var(--grey)}
#kr .art-back{margin-top:34px;padding-top:22px;border-top:1px solid var(--line)}
#kr .art-back a{font-weight:800;color:var(--lime);border:0}
"""

def build(n, doc_html):
    a = [x for x in ARTICLES if x[0] == n][0]
    art = K.convert(doc_html)
    d, mo, y = a[1].split('.')
    art['body'] = art['body'].replace('[ДАТА ПУБЛІКАЦІЇ ТА ОНОВЛЕННЯ]', a[1]).replace('[ДАТА ОНОВЛЕННЯ]', a[1])
    shell = open(os.path.join(H, 'out/blog-hub.html'), encoding='utf-8').read()
    s = shell.replace(f'page-id-{HUB}', 'elementor-template-canvas')
    url = f'{SITE}/blog/{a[2]}/'; desc = art['seo_description'] or a[5]; title = art['title']
    date_txt = a[1]
    # шапка: хлібні крихти + H1
    s = re.sub(r'<div class="rp-in">.*?</div></header>', lambda m: f'<div class="rp-in"><p class="art-crumbs"><a href="{SITE}/">Головна</a> / <a href="{SITE}/blog/">Блог</a></p><h1 class="art-h1">{html.escape(title)}</h1></div></header>', s, count=1, flags=re.S)
    # основний вміст замість карток (разом зі скриптом хабу)
    main = ('<main><section class="sec" id="article"><div class="in"><article class="art-card">'
            f'<div class="art-meta"><span class="art-tag">{html.escape(a[3])}</span><time datetime="{y}-{mo}-{d}">{date_txt}</time><span>{html.escape(AUTHOR)}</span></div>'
            f'<div class="art-body">{art["body"]}</div>'
            f'<p class="art-back"><a href="{SITE}/blog/">← Усі статті блогу</a></p></article></div></section></main>')
    s = re.sub(r'<main>.*?</main>', lambda m: main, s, count=1, flags=re.S)
    # meta + JSON-LD
    fq = K.faq(art['body'])
    graph = [{"@type": "Article", "headline": title, "description": desc, "inLanguage": "uk", "datePublished": f'{y}-{mo}-{d}T09:00:00+02:00',
              "mainEntityOfPage": url, "author": {"@type": "Person", "name": AUTHOR, "url": SITE + '/'}, "isPartOf": {"@type": "Blog", "url": f'{SITE}/blog/'}}]
    if fq: graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": t}} for q, t in fq]})
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + '</script>'
    i = s.rindex('</div>\n<!-- /wp:html -->') if '</div>\n<!-- /wp:html -->' in s else None
    s = s.replace('<!-- /wp:html -->', ld + '\n<!-- /wp:html -->', 1)
    i = s.index('</style>'); s = s[:i] + CSS + s[i:]
    return s, art, a

if __name__ == '__main__':
    n = int(sys.argv[1]); doc = open(sys.argv[2], encoding='utf-8').read()
    page, art, a = build(n, doc)
    os.makedirs(os.path.join(H, 'out'), exist_ok=True)
    open(os.path.join(H, f'out/article-{n}.html'), 'w', encoding='utf-8').write(page)
    print('built', n, len(page), 'bytes | H1:', art['title'][:60], '| FAQ:', len(K.faq(art['body'])), '| desc:', bool(art['seo_description']))
    if '--post' in sys.argv:
        d, mo, y = a[1].split('.')
        payload = dict(title=art['title'], slug=a[2], status='draft', template='elementor_canvas', parent=HUB, content=page, excerpt=a[5],
                       meta={'_yoast_wpseo_title': art['seo_title'] or art['title'], '_yoast_wpseo_metadesc': art['seo_description'] or a[5]})
        json.dump(payload, open('/tmp/_art.json', 'w', encoding='utf-8'), ensure_ascii=False)
        pid = sys.argv[sys.argv.index('--update') + 1] if '--update' in sys.argv else ''
        r = subprocess.run(['curl', '-sS', '-m', '120', '-X', 'POST', f'{SITE}/wp-json/wp/v2/pages' + (f'/{pid}' if pid else ''), '-H', 'Content-Type: application/json', '--data-binary', '@/tmp/_art.json'], capture_output=True, text=True)
        try: j = json.loads(r.stdout); print({k: j.get(k) for k in ('id', 'status', 'slug', 'parent', 'template', 'link', 'code', 'message')})
        except Exception: print(r.stdout[:300])
