#!/usr/bin/env python3
"""МАКЕТ блогу urists.com.ua (WP id хабу 48, головної-чернетки 49).
Вхід: backup-page9-live-*.gz, backup-page30-live-*.gz. Вихід: out/*.html. Живі сторінки не чіпає.
Якщо ARTICLES порожній, показує картки-заглушки; коли додати статті в articles.py і фото в photos/<slug>.webp, збірка заповнить реальні дані."""
import os, re, sys, gzip, html, base64
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from articles import ARTICLES, PLACEHOLDERS
e = html.escape
rd = lambda n: gzip.open(os.path.join(H, n), 'rt', encoding='utf-8').read()
LEAD = 'Пояснюю питання кредитів, боргів і захисту позичальника простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.'

CSS = """
.yk .bl-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:34px}
.yk .bl-card{display:flex;flex-direction:column;min-width:0;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 14px 40px rgba(24,26,49,.08);transition:.25s}
.yk .bl-card:hover{transform:translateY(-4px);box-shadow:0 22px 50px rgba(24,26,49,.14)}
.yk .bl-cover{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:radial-gradient(420px 240px at 80% -10%,#23264A 0,transparent 65%),linear-gradient(160deg,#23264A,#181A31)}
.yk .bl-cover img{width:100%;height:100%;object-fit:cover;display:block}
.yk .bl-tag{position:absolute;top:14px;left:14px;display:inline-block;padding:7px 15px;border-radius:999px;background:var(--gold);color:var(--navy);font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.yk .bl-body{display:flex;flex-direction:column;flex:1;padding:22px 24px 26px}
.yk .bl-card time{display:block;margin-bottom:10px;font-size:13.5px;font-weight:700;letter-spacing:.04em;color:var(--gold-d)}
.yk .bl-card h3{font-family:var(--f-head);font-weight:400;font-size:21px;line-height:1.25;margin:0 0 12px;color:var(--navy)}
.yk .bl-card h3 a{color:inherit;text-decoration:none}
.yk .bl-card p{margin:0 0 20px;color:var(--mute);font-size:15.5px}
.yk .bl-more{margin-top:auto;font-weight:800;font-size:13.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--navy);text-decoration:none}
.yk .bl-more::after{content:" \\2192"}
.yk .bl-all{display:flex;justify-content:center;margin-top:38px}
@media(max-width:1000px){.yk .bl-g{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){.yk .bl-g{grid-template-columns:minmax(0,1fr);gap:16px}.yk .bl-body{padding:18px 18px 22px}.yk .bl-card h3{font-size:19px}}
"""

def items():
    if ARTICLES: return ARTICLES
    return [(i, 'ДД.ММ.РРРР', '', 'Тема статті', 'Назва статті, яка займе один-два рядки', 'Короткий анонс статті на дві-три речення. Текст з’явиться, коли стаття буде готова.') for i in range(1, PLACEHOLDERS + 1)]

def card(a):
    n, d, slug, topic, title, ann = a
    u = f'/blog/{slug}/' if slug else '/blog/'
    p = os.path.join(H, 'photos', slug + '.webp') if slug else ''
    img = ''
    if p and os.path.exists(p):
        img = f'<img src="data:image/webp;base64,{base64.b64encode(open(p,"rb").read()).decode()}" alt="{e(title)}" width="760" height="507" loading="lazy" decoding="async">'
    dt = f'<time datetime="{d[6:]}-{d[3:5]}-{d[:2]}">{d}</time>' if slug else f'<time>{d}</time>'
    return (f'<article class="bl-card"><a class="bl-cover" href="{u}" tabindex="-1">{img}<span class="bl-tag">{e(topic)}</span></a>'
            f'<div class="bl-body">{dt}<h3><a href="{u}">{e(title)}</a></h3><p>{e(ann)}</p><a class="bl-more" href="{u}">Читати статтю</a></div></article>')

ARROW = '<i><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i>'

def nav(s, want):
    s = s.replace('<a href="/rezultaty-roboty/">Результати</a>', '<a href="/rezultaty-roboty/">Результати</a><a href="/blog/">Блог</a>')
    assert s.count('>Блог<') == want, s.count('>Блог<')
    return s

def addcss(s, extra=''):
    i = s.index('</style>'); return s[:i] + CSS + extra + s[i:]

def home():
    s = nav(rd('backup-page9-live-20261102.html.gz'), 2)
    sec = ('<section class="results" id="articles"><div class="in"><div class="head"><span class="eyebrow">Блог юриста</span><h2 class="t">Мої статті</h2>'
           f'<p>{LEAD}</p></div><div class="bl-g">' + ''.join(card(a) for a in items()[:3]) + '</div>'
           f'<div class="bl-all"><a class="btn" href="/blog/">Усі статті{ARROW}</a></div></div></section>\n\n')
    m = '<!-- 5. ВІДГУКИ -->'; assert s.count(m) == 1
    return addcss(s.replace(m, sec + m))

def hub():
    s = nav(rd('backup-page30-live-20261102.html.gz'), 2)
    s = s.replace('<span class="eyebrow">Результати · Яковенко Дмитро</span>', '<span class="eyebrow">Блог · Яковенко Дмитро</span>', 1)
    s = s.replace('<h1>Результати роботи</h1>', '<h1>Мої статті</h1>', 1)
    s = re.sub(r'<p class="lead">Документи з реальних справ[^<]*</p>', f'<p class="lead">{LEAD}</p>', s, count=1)
    a = s.index('<section class="results page" id="results">'); b = s.index('<!-- CTA -->')
    sec = ('<section class="results page" id="articles"><div class="in"><div class="bl-g">' + '\n'.join(card(x) for x in items()) + '</div></div></section>\n\n')
    s = s[:a] + sec + s[b:]
    ld = ('{"@context":"https://schema.org","@type":"Blog","name":"Блог — Яковенко Дмитро","url":"https://urists.com.ua/blog/","inLanguage":"uk",'
          '"author":{"@id":"https://urists.com.ua/#person"},"isPartOf":{"@type":"WebSite","name":"Юристи України","url":"https://urists.com.ua/"}}')
    s = re.sub(r'(<script type="application/ld\+json">\s*)\{.*?"@type": "CollectionPage".*?\n\}(\s*</script>)', lambda m: m.group(1) + ld + m.group(2), s, count=1, flags=re.S)
    # на живій сторінці «Результати» немає мобільного меню й стилів футер-меню: беремо з головної (menu_patch.css)
    return addcss(s, open(os.path.join(H, 'menu_patch.css'), encoding='utf-8').read())

if __name__ == '__main__':
    os.makedirs(os.path.join(H, 'out'), exist_ok=True)
    open(os.path.join(H, 'out/home-with-articles.html'), 'w', encoding='utf-8').write(home())
    open(os.path.join(H, 'out/blog-hub.html'), 'w', encoding='utf-8').write(hub())
    print('ok')
