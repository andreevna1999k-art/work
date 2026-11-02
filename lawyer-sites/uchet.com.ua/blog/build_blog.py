#!/usr/bin/env python3
"""Чернетки uchet.com.ua: хаб блогу (WP id 58) і головна з блоком «Мої статті» (WP id 59).
Вхід: backup-page9-live-*.gz (головна), backup-page33-live-*.gz (каркас хабу). Вихід: out/*.html. Живі сторінки не чіпає."""
import os, re, sys, gzip, html, base64
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from articles import ARTICLES
e = html.escape
rd = lambda n: gzip.open(os.path.join(H, n), 'rt', encoding='utf-8').read()

CSS = """
.uc .bl-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:34px}
.uc .bl-card{display:flex;flex-direction:column;min-width:0;background:var(--panel);border-radius:28px;overflow:hidden;transition:transform .2s}
.uc .bl-card:hover{transform:translateY(-3px)}
.uc .bl-cover{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:var(--dark)}
.uc .bl-cover img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s}
.uc .bl-card:hover .bl-cover img{transform:scale(1.03)}
.uc .bl-tag{position:absolute;top:14px;left:14px;display:inline-block;padding:7px 14px;border-radius:999px;background:var(--kh-l);color:var(--dark);font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
.uc .bl-body{display:flex;flex-direction:column;flex:1;padding:20px 22px 24px}
.uc .bl-card time{display:block;margin-bottom:10px;font-size:13px;font-weight:600;letter-spacing:.04em;color:var(--kh-t)}
.uc .bl-card h3{font-size:18px;line-height:1.3;margin:0 0 10px;color:var(--dark)}
.uc .bl-card h3 a{color:inherit;text-decoration:none}
.uc .bl-card h3 a:hover{color:var(--kh-t)}
.uc .bl-more,.uc .bl-cover{text-decoration:none}
.uc .bl-card p{margin:0 0 18px;font-size:14.5px;line-height:1.55;color:var(--tx2)}
.uc .bl-more{margin-top:auto;font-weight:700;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--dark)}
.uc .bl-more::after{content:" \\2192"}
.uc .bl-more:hover{color:var(--kh-t)}
@media(max-width:1000px){.uc .bl-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){.uc .bl-grid{grid-template-columns:minmax(0,1fr);gap:16px}.uc .bl-body{padding:18px 18px 22px}.uc .bl-card h3{font-size:17px}}
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

def nav(s, want):
    s = s.replace('<a href="/rezultaty-roboty/">Результати</a><a href="#reviews">', '<a href="/rezultaty-roboty/">Результати</a><a href="/blog/">Блог</a><a href="#reviews">')
    s = s.replace('<a href="/rezultaty-roboty/">Результати</a><a href="/#reviews">', '<a href="/rezultaty-roboty/">Результати</a><a href="/blog/">Блог</a><a href="/#reviews">')
    assert s.count('>Блог<') == want, s.count('>Блог<')
    return s

FNAV = """
.uc .fnav{display:flex;flex-wrap:wrap;gap:8px 26px;margin:clamp(22px,3vw,34px) 0 0;padding:20px 0 0;border-top:1px solid rgba(255,255,255,.14);font-size:14px;font-weight:600}
.uc .fnav a{color:var(--kh-l);text-decoration:none}
.uc .fnav a:hover{color:#fff}
@media(max-width:620px){.uc .fnav{flex-direction:column;gap:2px}.uc .fnav a{display:block;padding:11px 0}}
"""

def addcss(s, extra=''):
    i = s.index('</style>'); return s[:i] + CSS + extra + s[i:]

def home():
    s = nav(rd('backup-page9-live-20261102.html.gz'), 2)
    sec = ('<section id="articles"><div class="w"><span class="eyebrow">Блог юриста</span><h2>Мої <em>статті</em></h2>'
           '<p class="lead">Пояснюю питання кредитів, боргів і виїзду за кордон простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>'
           '<div class="bl-grid">' + ''.join(card(a) for a in ARTICLES[:3]) + '</div>'
           '<div class="res-cta"><a class="btn" href="/blog/">Усі статті <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i></a></div></div></section>\n\n')
    m = '<section style="padding-top:0" id="reviews">'; assert s.count(m) == 1
    return addcss(s.replace(m, sec + m))

def hub():
    s = nav(rd('backup-page33-live-20261102.html.gz'), 1)
    s = s.replace('<div class="crumbs"><a href="/">Головна</a> / Результати роботи</div>', '<div class="crumbs"><a href="/">Головна</a> / Блог</div>', 1)
    s = s.replace('<h1>Результати <em>роботи</em></h1>', '<h1>Мої <em>статті</em></h1>', 1)
    s = s.replace('<p>Документи з реальних справ: гарантійні листи й листи про врегулювання заборгованості. Персональні дані клієнтів закрито.</p>',
                  '<p>Пояснюю питання кредитів, боргів і виїзду за кордон простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>', 1)
    s = s.replace('Обговорити вашу справу', 'Обговорити вашу ситуацію', 1)
    a = s.index('<section id="results">'); b = s.index('</section>', a) + len('</section>')
    sec = ('<section id="articles"><div class="w"><span class="eyebrow">Блог юриста</span><h2>Усі <em>статті</em></h2>'
           f'<p class="lead">Усього {len(ARTICLES)} статей. Матеріали мають інформаційний характер і не замінюють індивідуальну консультацію.</p>'
           '<div class="bl-grid">' + '\n'.join(card(x) for x in ARTICLES) + '</div></div></section>')
    s = s[:a] + sec + s[b:]
    s = re.sub(r'<script>\s*\(function\(\)\{var lb=document.getElementById\(.lb.\).*?</script>', '', s, count=1, flags=re.S)
    s = re.sub(r'<div id="lb" class="lb"[^>]*>.*?</div>\n?', '', s, count=1, flags=re.S)
    ld = '{"@context":"https://schema.org","@type":"Blog","name":"Блог — Борисов Максим Юрійович","url":"https://uchet.com.ua/blog/","inLanguage":"uk","author":{"@type":"Person","@id":"https://uchet.com.ua/#person","name":"Максим Юрійович Борисов"}}'
    s = re.sub(r'(<script type="application/ld\+json">\s*)\{"@context":"https://schema.org","@type":"CollectionPage".*?\}\s*(</script>)', lambda m: m.group(1) + ld + '\n' + m.group(2), s, count=1, flags=re.S)
    return addcss(s, FNAV)

if __name__ == '__main__':
    os.makedirs(os.path.join(H, 'out'), exist_ok=True)
    open(os.path.join(H, 'out/home-with-articles.html'), 'w', encoding='utf-8').write(home())
    open(os.path.join(H, 'out/blog-hub.html'), 'w', encoding='utf-8').write(hub())
    print('ok')
