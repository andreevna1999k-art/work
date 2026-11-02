#!/usr/bin/env python3
"""Збирає чернетки: хаб блогу (/blog/) і головну з блоком «Мої статті» + пункт меню «Блог».
Вхід: backup-page13-live-*.html (головна), backup-page48-live-*.html (каркас хабу). Вихід: out/*.html
Живі сторінки НЕ чіпає."""
import re, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES
import base64
from make_covers import svg as cover_svg
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda n: open(os.path.join(H, n), encoding='utf-8').read()
e = html.escape

CSS = """<style>
.bz .bl-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.bz .bl-card{display:flex;flex-direction:column;min-width:0;background:var(--white);border:1px solid var(--line);border-radius:var(--r-card);padding:0 0 24px;box-shadow:var(--sh);transition:transform .2s,box-shadow .2s;overflow:hidden}
.bz .bl-cover{position:relative;display:block;aspect-ratio:8/5;background:var(--brown-dark)}
.bz .bl-cover img{width:100%;height:100%;object-fit:cover}
.bz .bl-cover .bl-tag{position:absolute;top:14px;left:14px;background:rgba(43,23,17,.82);color:var(--cream);backdrop-filter:blur(2px)}
.bz .bl-body{display:flex;flex-direction:column;flex:1;padding:20px 24px 0}
.bz .bl-card:hover{transform:translateY(-3px)}
.bz .bl-meta{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-bottom:12px;font-size:13.5px;color:var(--ink-soft)}
.bz .bl-tag{display:inline-block;padding:5px 14px;border-radius:999px;background:rgba(212,178,122,.28);color:var(--brown);font-size:12px;letter-spacing:.1em;text-transform:uppercase;font-weight:600}
.bz .bl-card h3{font-size:21px;line-height:1.25;margin:0 0 12px;color:var(--brown);letter-spacing:.02em}
.bz .bl-card h3 a:hover{color:var(--maroon)}
.bz .bl-card p{font-size:16px;color:var(--ink-soft);margin:0 0 20px}
.bz .bl-card .bl-more{margin-top:auto;font-weight:600;font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:var(--maroon)}
.bz .bl-card .bl-more::after{content:" \\2192"}
.bz .bl-card .bl-more:hover{color:var(--maroon-600)}
.bz .bl-more-row{text-align:center;margin-top:38px}
@media(max-width:1100px){.bz .bl-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){.bz .bl-grid{grid-template-columns:minmax(0,1fr);gap:16px}.bz .bl-body{padding:18px 20px 0}.bz .bl-card h3{font-size:19px}}
</style>
"""

def card(a, tag='h3'):
    n, d, slug, topic, title, ann = a
    u = f"/blog/{slug}/"
    src = 'data:image/svg+xml;base64,' + base64.b64encode(cover_svg(n).encode()).decode()
    return (f'<article class="bl-card"><a class="bl-cover" href="{u}" tabindex="-1" aria-hidden="true">'
            f'<img src="{src}" alt="" width="1200" height="750" loading="lazy"><span class="bl-tag">{e(topic)}</span></a>'
            f'<div class="bl-body"><div class="bl-meta"><time datetime="{d[6:]}-{d[3:5]}-{d[:2]}">{d}</time></div>'
            f'<{tag}><a href="{u}">{e(title)}</a></{tag}><p>{e(ann)}</p>'
            f'<a class="bl-more" href="{u}">Читати статтю</a></div></article>')

def add_nav(src, cur=False):
    # пункт меню «Блог» після «Результати» (шапка) і у футері
    li = '<li><a href="/blog/"%s>Блог</a></li>' % (' class="cur"' if cur else '')
    src = re.sub(r'(<li><a href="/rezultaty-roboty/"[^>]*>Результати</a></li>)', r'\1' + li, src, count=1)
    src = src.replace('<a href="/rezultaty-roboty/">Результати</a><a href="/#reviews">',
                      '<a href="/rezultaty-roboty/">Результати</a><a href="/blog/">Блог</a><a href="/#reviews">', 1)
    src = src.replace('<a href="/rezultaty-roboty/" class="cur">Результати</a>', '<a href="/rezultaty-roboty/">Результати</a>')
    return src

def home():
    s = rd('backup-page13-live-20261102.html')
    s = add_nav(s)
    blk = ('<!-- 4б · МОЇ СТАТТІ -->\n<section id="articles"><div class="wrap">\n<div class="panel on-white pad">\n'
           '<div class="head res-head"><span class="res-badge">Блог юриста</span>\n<h2 class="res-title">Мої статті</h2>\n'
           '<p class="lead">Пояснюю кредитні питання простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p></div>\n'
           '<div class="bl-grid">' + ''.join(card(a) for a in ARTICLES[:3]) + '</div>\n'
           '<div class="bl-more-row"><a class="btn ghost dark" href="/blog/">Усі статті</a></div>\n</div>\n</div></section>\n')
    # блок — після «Результати», перед lightbox
    m = '<div id="lb" class="lb" hidden="">'
    assert s.count(m) == 1
    s = s.replace(m, blk + m)
    # CSS — перед закриттям першого <style>
    assert '</style></p>' in s
    s = s.replace('</style></p>', CSS.replace('<style>\n','').replace('</style>\n','') + '</style></p>', 1)
    return s

def hub():
    s = rd('backup-page48-live-20261102.html')
    s = add_nav(s, cur=True)
    # SEO-мета та JSON-LD
    desc = 'Статті юриста Бойчука Артема Валерійовича про кредити, борги, колекторів і суд: що каже закон і що робити позичальнику.'
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, 1)
    ld = ('{"@context": "https://schema.org", "@type": "Blog", "name": "Блог — Бойчук Артем Валерійович", "description": "%s", '
          '"url": "https://legaladdress.com.ua/blog/", "author": {"@id": "https://legaladdress.com.ua/#boychuk"}, '
          '"isPartOf": {"@type": "WebSite", "name": "Бойчук Артем Валерійович", "url": "https://legaladdress.com.ua/"}}') % desc
    s = re.sub(r'(<script type="application/ld\+json">)\{"@context": "https://schema.org", "@type": "CollectionPage".*?(</script>)', lambda m: m.group(1)+ld+m.group(2), s, 1, flags=re.S)
    # шапка сторінки
    a = s.index('<div class="rp-head">'); b = s.index('</div>\n</div>\n</div></section>', a)
    head = ('<div class="rp-head"><span class="res-badge">Блог юриста</span>\n    <h1>Мої <span>статті</span></h1>\n'
            '    <p class="lead">Пояснюю кредитні питання простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>\n'
            f'    <span class="rp-count"><b>{len(ARTICLES)}</b> статей</span>\n  ')
    s = s[:a] + head + s[b:]
    # список
    a = s.index('<section id="results">'); b = s.index('<section><div class="wrap">\n<div class="panel pad rp-cta">')
    lst = ('<section id="articles"><div class="wrap">\n<div class="panel on-white pad res-panel rp-list">\n<div class="bl-grid">\n'
           + '\n'.join(card(x) for x in ARTICLES) + '\n</div>\n</div></div></section>\n\n')
    s = s[:a] + lst + s[b:]
    # CTA
    s = s.replace('Хочете такий самий результат?', 'Потрібна допомога з кредитом?')
    # lightbox не потрібен
    s = re.sub(r'<div class="lb" id="lb" hidden>.*?</script>\n', '', s, 1, flags=re.S)
    s = s.replace('</style>\n<style>.bz{width:100%', CSS.replace('<style>\n','').replace('</style>\n','') + '</style>\n<style>.bz{width:100%', 1)
    assert 'bl-grid{' in s
    return s

if __name__ == '__main__':
    os.makedirs(os.path.join(H, 'out'), exist_ok=True)
    open(os.path.join(H, 'out/home-with-articles.html'), 'w', encoding='utf-8').write(home())
    open(os.path.join(H, 'out/blog-hub.html'), 'w', encoding='utf-8').write(hub())
    print('ok')
