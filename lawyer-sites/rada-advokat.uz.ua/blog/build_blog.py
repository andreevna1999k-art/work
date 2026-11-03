#!/usr/bin/env python3
"""Чернетки rada-advokat.uz.ua: хаб блогу (WP id 1942) і головна з блоком «Мої статті» (WP id 1943).
Вхід: backup-page1901-live-*.gz (головна), backup-page1916-live-*.gz (каркас хабу). Вихід: out/*.html. Живі сторінки не чіпає."""
import os, re, sys, gzip, html, base64
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from articles import ARTICLES
sys.path.insert(0, os.path.join(H, '..', '..', '_blog-kit'))
import dyn
PHOTOS = os.path.join(H, 'photos')
PARENT = 1942   # id хабу (батьківська сторінка статей)
e = html.escape
HUB_ID, HOME_ID = 1942, 1943
B = 'https://rada-advokat.uz.ua'
rd = lambda n: gzip.open(os.path.join(H, n), 'rt', encoding='utf-8').read()

CSS = """
#kr .bgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--gap);align-items:stretch}
#kr .bc{display:flex;flex-direction:column;min-width:0;background:#fff;border-radius:var(--r2);overflow:hidden;transition:transform .2s}
#kr .bc:hover{transform:translateY(-3px)}
#kr .bc .bp{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:radial-gradient(520px 300px at 78% -10%,#004671 0,transparent 62%),linear-gradient(160deg,#06344f,#042a41 60%,#031f31)}
#kr .bc .bp img{width:100%;height:100%;object-fit:cover;display:block}
#kr .bc .bt{position:absolute;top:14px;left:14px;display:inline-block;padding:6px 14px;border-radius:999px;background:var(--sky);color:var(--navy);font-size:11px;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
#kr .bc .bx{display:flex;flex-direction:column;flex:1;padding:clamp(18px,1.8vw,26px)}
#kr .bc time{display:block;margin-bottom:10px;font-size:12.5px;font-weight:700;letter-spacing:.04em;color:var(--steel)}
#kr .bc h3{font-size:clamp(15px,1.15vw,19px);line-height:1.25;margin-bottom:10px;letter-spacing:-.01em;color:var(--ink)}
#kr .bc h3 a:hover{color:var(--lime)}
#kr .bc p{color:var(--muted);font-size:.94em;margin-bottom:18px}
#kr .bc .bl{margin-top:auto;font-weight:800;font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--lime)}
#kr .bc .bl::after{content:" \\2192"}
#kr .bwrap{margin-top:0}
#kr .bc-empty{grid-column:1/-1;text-align:center;color:var(--muted);padding:30px 10px;font-size:18px}
@media(max-width:1100px){#kr .bgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){#kr .bgrid{grid-template-columns:minmax(0,1fr)}}
"""

def card(a):
    n, d, slug, topic, title, ann = a
    u = f'{B}/blog/{slug}/'
    p = os.path.join(H, 'photos', slug + '.webp')
    img = ''
    if os.path.exists(p):
        img = f'<img src="data:image/webp;base64,{base64.b64encode(open(p,"rb").read()).decode()}" alt="{e(title)}" width="760" height="507" loading="lazy">'
    return (f'<article class="bc"><a class="bp" href="{u}" tabindex="-1">{img}<span class="bt">{e(topic)}</span></a>'
            f'<div class="bx"><time datetime="{d[6:]}-{d[3:5]}-{d[:2]}">{d}</time><h3><a href="{u}">{e(title)}</a></h3><p>{e(ann)}</p>'
            f'<a class="bl" href="{u}">Читати статтю</a></div></article>')

def nav(s):
    s = s.replace(f'<li><a href="{B}/rezultaty-roboty/">Результати</a></li>', f'<li><a href="{B}/rezultaty-roboty/">Результати</a></li><li><a href="{B}/blog/">Блог</a></li>', 1)
    s = s.replace(f'<a href="{B}/rezultaty-roboty/">Результати</a><a href="{B}/#reviews">', f'<a href="{B}/rezultaty-roboty/">Результати</a><a href="{B}/blog/">Блог</a><a href="{B}/#reviews">', 1)
    assert s.count('/blog/">Блог<') >= 1
    return s

def addcss(s):
    i = s.index('</style>'); return s[:i] + CSS + s[i:]

def home():
    s = rd('backup-page1901-live-20261102.html.gz').replace('page-id-1901', f'page-id-{HOME_ID}')
    s = nav(s)
    sec = ('<section class="sec art" id="articles"><div class="in"><div class="sh c"><span class="eb">Блог юриста</span><h2>Мої <span class="hl">статті</span></h2></div>'
           '<div class="bgrid" id="blogGrid"></div>' + dyn.script(PARENT, 3, ARTICLES, PHOTOS, cls=dyn.RADA) +
           f'<div class="rmore"><a class="btn" href="{B}/blog/">Усі статті</a></div></div></section>')
    m = '<section class="sec rev" id="reviews">'; assert s.count(m) == 1
    return addcss(s.replace(m, sec + m))

def hub():
    s = rd('backup-page1916-live-20261102.html.gz').replace('page-id-1916', f'page-id-{HUB_ID}')
    s = nav(s)
    a = s.index('<div class="rp-in">'); b = s.index('</header><main>')
    s = s[:a] + ('<div class="rp-in"><h1>Мої <span class="lime">статті</span></h1><p class="lead">Пояснюю питання кредитів, боргів і виконавчого провадження простою мовою: що каже закон, як діє виконавець і що варто зробити в першу чергу.</p>'
                 f'<p class="rp-note"><span><b><span id="blogCount">0</span> <span id="blogCountLabel">статей</span>.</b> Матеріали мають інформаційний характер і не замінюють індивідуальну консультацію.</span></p></div>') + s[b:]
    a = s.index('<main>'); b = s.index('</main>') + len('</main>')
    main = ('<main><section class="sec res rp-res" id="articles"><div class="in"><div class="bgrid" id="blogGrid"></div>' + dyn.script(PARENT, 100, ARTICLES, PHOTOS, cls=dyn.RADA) + '</div></section></main>')
    s = s[:a] + main + s[b:]
    s = re.sub(r'<script>\s*\(function\(\)\{var root=document\.getElementById\(\'kr\'\).*?</script>', '', s, count=1, flags=re.S)
    s = s.replace('Результати <span', 'Результати <span')  # no-op guard
    # прибрати cur-підсвітку «Результати» якщо є — у цьому шаблоні її немає
    t = re.search(r'<title>.*?</title>', s)
    return addcss(s)

if __name__ == '__main__':
    os.makedirs(os.path.join(H, 'out'), exist_ok=True)
    open(os.path.join(H, 'out/home-with-articles.html'), 'w', encoding='utf-8').write(home())
    open(os.path.join(H, 'out/blog-hub.html'), 'w', encoding='utf-8').write(hub())
    print('ok')
