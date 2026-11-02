#!/usr/bin/env python3
"""Чернетки ukrjurist.com.ua: хаб блогу (WP id 57) і головна з блоком «Мої статті» (WP id 58).
Вхід: backup-page14-live-*.gz (головна), backup-page31-live-*.gz (каркас хабу). Вихід: out/*.html. Живі сторінки не чіпає."""
import os, re, sys, gzip, html, base64
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from articles import ARTICLES
e = html.escape
rd = lambda n: gzip.open(os.path.join(H, n), 'rt', encoding='utf-8').read()

CSS = """
.gv .bl-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;align-items:stretch}
.gv .bl-card{display:flex;flex-direction:column;min-width:0;background:var(--white);border:1px solid var(--line);border-radius:var(--r-card);overflow:hidden;box-shadow:var(--sh);transition:transform .2s}
.gv .bl-card:hover{transform:translateY(-3px)}
.gv .bl-cover{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:linear-gradient(135deg,var(--ink-2),var(--ink))}
.gv .bl-cover img{width:100%;height:100%;object-fit:cover;display:block}
.gv .bl-tag{position:absolute;top:14px;left:14px;display:inline-block;padding:7px 15px;border-radius:999px;background:var(--olive);color:var(--ink);font:600 12px/1 var(--f-body);letter-spacing:.14em;text-transform:uppercase}
.gv .bl-body{display:flex;flex-direction:column;flex:1;padding:22px 24px 26px}
.gv .bl-card time{display:block;margin-bottom:10px;font-size:14px;font-weight:500;letter-spacing:.06em;color:var(--olive-t)}
.gv .bl-card h3{font-family:var(--f-head);font-weight:500;font-size:21px;line-height:1.25;margin:0 0 12px;color:var(--ink)}
.gv .bl-card h3 a:hover{color:var(--olive-t)}
.gv .bl-card p{margin:0 0 20px;color:var(--ink-soft);font-size:16px}
.gv .bl-more{margin-top:auto;font:600 13px/1 var(--f-body);letter-spacing:.14em;text-transform:uppercase;color:var(--ink)}
.gv .bl-more::after{content:" \\2197"}
.gv .bl-more:hover{color:var(--olive-t)}
.gv .bl-all{text-align:center;margin-top:38px}
@media(max-width:1000px){.gv .bl-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){.gv .bl-grid{grid-template-columns:minmax(0,1fr);gap:16px}.gv .bl-body{padding:18px 18px 22px}.gv .bl-card h3{font-size:19px}}
"""

def card(a):
    n, d, slug, topic, title, ann = a
    u = f'/blog/{slug}/'
    p = os.path.join(H, 'photos', slug + '.webp')
    img = ''
    if os.path.exists(p):
        img = f'<img src="data:image/webp;base64,{base64.b64encode(open(p,"rb").read()).decode()}" alt="{e(title)}" width="760" height="507" loading="lazy" decoding="async">'
    return (f'<article class="bl-card"><a class="bl-cover" href="{u}" tabindex="-1">{img}<span class="bl-tag">{e(topic)}</span></a>'
            f'<div class="bl-body"><time datetime="{d[6:]}-{d[3:5]}-{d[:2]}">{d}</time><h3><a href="{u}">{e(title)}</a></h3><p>{e(ann)}</p>'
            f'<a class="bl-more" href="{u}">Читати статтю</a></div></article>')

def nav(s):
    pre = '(?:/)?'
    s = s.replace('<li><a href="/rezultaty-roboty/">Результати</a></li>', '<li><a href="/rezultaty-roboty/">Результати</a></li><li><a href="/blog/">Блог</a></li>')
    s = s.replace('''<a href="/rezultaty-roboty/" onclick="this.closest('details').removeAttribute('open')">Результати</a>''',
                  '''<a href="/rezultaty-roboty/" onclick="this.closest('details').removeAttribute('open')">Результати</a><a href="/blog/" onclick="this.closest('details').removeAttribute('open')">Блог</a>''')
    s = s.replace('<a href="/rezultaty-roboty/">Результати</a><a href="/#reviews">', '<a href="/rezultaty-roboty/">Результати</a><a href="/blog/">Блог</a><a href="/#reviews">')
    assert s.count('>Блог<') == 3, s.count('>Блог<')
    return s

def addcss(s):
    i = s.index('</style>'); return s[:i] + CSS + s[i:]

def home():
    s = rd('backup-page14-live-20261102.html.gz'); s = nav(s)
    sec = ('<section class="band on-cream" id="articles"><div class="wrap"><div class="head"><span class="eyebrow" style="color:var(--olive-t)">Блог юристки</span><h2>Мої статті</h2>'
           '<p class="lead">Пояснюю питання кредитів, боргів і кредитної історії простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p></div>'
           '<div class="bl-grid">' + ''.join(card(a) for a in ARTICLES[:3]) + '</div>'
           '<div class="bl-all"><a class="btn" href="/blog/">Усі статті</a></div></div></section>\n\n')
    m = '<section class="band on-olive" id="reviews">'; assert s.count(m) == 1
    return addcss(s.replace(m, sec + m))

def hub():
    s = rd('backup-page31-live-20261102.html.gz'); s = nav(s)
    s = s.replace('<!-- Title: Результати роботи — Гончарук Вікторія Анатолієвна -->', '<!-- Title: Блог — Гончарук Вікторія Анатолієвна, юрист по кредитам -->')
    s = s.replace('<!-- H1: Результати роботи -->', '<!-- H1: Мої статті -->')
    desc = 'Статті юристки по кредитам Гончарук Вікторії Анатолієвни: кредитна історія, прострочення, права позичальника, банки та суд простою мовою.'
    s = re.sub(r'<!-- Description: .*? -->', f'<!-- Description: {desc} -->', s, 1)
    s = s.replace('<h1>Результати роботи</h1>', '<h1>Мої статті</h1>', 1)
    s = s.replace('<p class="lead">Довідки кредиторів про виконання зобов’язань і відсутність заборгованості. Персональні дані клієнтів закрито.</p>',
                  '<p class="lead">Пояснюю питання кредитів, боргів і кредитної історії простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>', 1)
    a = s.index('<section class="band on-cream" id="results">'); b = s.index('<section class="band on-cream" id="cta">')
    sec = ('<section class="band on-cream" id="articles">\n  <div class="wrap">\n    <div class="bl-grid">' + '\n'.join(card(x) for x in ARTICLES) + '</div>\n  </div>\n</section>\n\n')
    s = s[:a] + sec + s[b:]
    ld = ('{"@context": "https://schema.org", "@type": "Blog", "name": "Блог — Гончарук Вікторія Анатолієвна", "description": "%s", "url": "https://ukrjurist.com.ua/blog/", '
          '"author": {"@type": "Person", "@id": "https://ukrjurist.com.ua/#person", "name": "Гончарук Вікторія Анатолієвна", "jobTitle": "Юристка по кредитам", "url": "https://ukrjurist.com.ua/"}}') % desc
    s = re.sub(r'(<script type="application/ld\+json">)\{"@context": "https://schema.org", "@type": "CollectionPage".*?(</script>)', lambda m: m.group(1) + ld + m.group(2), s, 1, flags=re.S)
    return addcss(s)

if __name__ == '__main__':
    os.makedirs(os.path.join(H, 'out'), exist_ok=True)
    open(os.path.join(H, 'out/home-with-articles.html'), 'w', encoding='utf-8').write(home())
    open(os.path.join(H, 'out/blog-hub.html'), 'w', encoding='utf-8').write(hub())
    print('ok')
