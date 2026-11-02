#!/usr/bin/env python3
"""МАКЕТ блогу advokato.in.ua (стиль див. ../STYLE.md). Головна сайту в Elementor, тому макет самодостатній:
 out/blog-hub.html           сторінка-хаб (WP id 1818, чернетка)
 out/block-preview.html      блок «Мої статті» в контексті сайту (WP id 1819, чернетка)
 out/home-block-snippet.html той самий блок окремо, для вставки в HTML-віджет Elementor на головній
Живі сторінки не чіпає."""
import os, html, base64, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from articles import ARTICLES, PLACEHOLDERS
e = html.escape
HUB_ID, PREVIEW_ID = 1818, 1819
TG = 'https://t.me/yrist_kovalenko'
PORTRAIT = 'https://advokato.in.ua/wp-content/uploads/2025/07/kovalenko-nataliia-oleksandrivna-yuryst-po-kredytam.jpg'
LEAD = 'Пояснюю питання банкрутства фізичних осіб, боргів і дій колекторів простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.'

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Noto+Serif:wght@700&display=swap');
.kv{--rose:#B5838C;--peach:#FFCDB2;--slate:#615C68;--slate2:#6E6876;--char:#424242;--ink:#2F2B36;--white:#fff;
 font-family:Lato,sans-serif;font-size:16px;line-height:1.6;color:rgba(255,255,255,.85);background:var(--slate);
 position:relative;left:50%;margin-left:-50vw;width:100vw;overflow:hidden;-webkit-font-smoothing:antialiased}
.kv *{box-sizing:border-box}.kv h1,.kv h2,.kv h3,.kv p,.kv ul,.kv li{margin:0;padding:0}.kv ul{list-style:none}
.kv a{color:inherit;text-decoration:none;border:0;box-shadow:none}
.kv h1,.kv h2,.kv h3{font-family:'Noto Serif',serif;font-weight:700;color:#fff;line-height:1.2;text-transform:none;letter-spacing:0}
.kv .w{max-width:1180px;margin:0 auto;padding:0 24px}
.kv .bar{display:block;width:60px;height:3px;background:#fff;margin:18px 0 0}
.kv .btn{display:inline-block;padding:15px 30px;border:1px solid #fff;color:#fff;font:400 14px/1 Lato,sans-serif;letter-spacing:.08em;text-transform:uppercase;background:transparent;transition:.2s}
.kv .btn:hover{background:#fff;color:var(--slate)}
/* верхня смуга з меню (на сайті меню немає, тут мінімальне) */
.kv .top{position:absolute;z-index:5;left:0;right:0;top:0;padding:22px 0}
.kv .top .w{display:flex;align-items:center;justify-content:space-between;gap:20px}
.kv .logo{font:700 20px/1 'Noto Serif',serif;color:#fff}
.kv .menu{display:flex;gap:30px;font-size:13px;letter-spacing:.1em;text-transform:uppercase}
.kv .menu a{padding:6px 0;border-bottom:1px solid transparent}.kv .menu a:hover,.kv .menu a.cur{border-bottom-color:#fff}
.kv .menu-cb{position:absolute;opacity:0;pointer-events:none;width:0;height:0}
.kv .burger{display:none;width:42px;height:42px;border:1px solid #fff;cursor:pointer;position:relative}
.kv .burger i,.kv .burger i::before,.kv .burger i::after{content:"";position:absolute;left:10px;width:20px;height:2px;background:#fff}
.kv .burger i{top:20px}.kv .burger i::before{left:0;top:-7px}.kv .burger i::after{left:0;top:7px}
.kv .menu-cb:checked ~ .burger i{background:transparent}.kv .menu-cb:checked ~ .burger i::before{top:0;transform:rotate(45deg)}.kv .menu-cb:checked ~ .burger i::after{top:0;transform:rotate(-45deg)}
/* hero: дві половини, як на головній сайту */
.kv .hero{position:relative;background:linear-gradient(90deg,var(--rose) 0 50%,var(--char) 50% 100%);padding:130px 0 80px}
.kv .hero .w{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.kv .hero h1{font-size:clamp(38px,5vw,60px)}
.kv .hero .sub{margin-top:22px;font:700 17px/1.4 Lato,sans-serif;color:#fff}
.kv .hero .lead{margin-top:14px;max-width:460px;color:rgba(255,255,255,.9)}
.kv .hero .btn{margin-top:30px}
.kv .hero .ph{justify-self:end;width:min(100%,430px)}
.kv .hero .ph img{width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;border-radius:28px;display:block;box-shadow:0 24px 50px rgba(0,0,0,.35)}
/* секція з картками */
.kv .sec{padding:80px 0 90px;background:var(--slate)}
.kv .sec.pre{padding-top:120px}
.kv .sec h2{font-size:clamp(30px,4vw,50px);text-align:center}
.kv .sec .bar{margin:18px auto 0}
.kv .sec .lead2{max-width:640px;margin:20px auto 0;text-align:center}
.kv .bl-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:44px}
.kv .bl-card{display:flex;flex-direction:column;min-width:0;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 14px 40px rgba(0,0,0,.18);transition:transform .2s}
.kv .bl-card:hover{transform:translateY(-4px)}
.kv .bl-cover{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:linear-gradient(135deg,var(--slate2),var(--char))}
.kv .bl-cover img{width:100%;height:100%;object-fit:cover;display:block}
.kv .bl-tag{position:absolute;top:14px;left:14px;padding:6px 14px;background:var(--rose);color:#fff;font:700 11px/1.2 Lato,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.kv .bl-body{display:flex;flex-direction:column;flex:1;padding:22px 24px 26px}
.kv .bl-card time{display:block;margin-bottom:10px;font:700 13px/1 Lato,sans-serif;letter-spacing:.06em;color:var(--rose)}
.kv .bl-card h3{font-size:20px;line-height:1.3;margin:0 0 12px;color:var(--ink)}
.kv .bl-card p{margin:0 0 20px;font-size:15px;color:#5E5A66}
.kv .bl-more{margin-top:auto;font:700 13px/1 Lato,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
.kv .bl-more::after{content:" \\2192"}.kv .bl-more:hover{color:var(--rose)}
.kv .all{text-align:center;margin-top:44px}
/* футер: три колонки, як на головній сайту */
.kv .ft{background:var(--slate);padding:0 0 60px}
.kv .ft .w{border-top:1px solid rgba(255,255,255,.3);padding-top:56px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px}
.kv .ft h3{font-size:20px;margin-bottom:18px}
.kv .ft p,.kv .ft li{font-size:15px;margin-bottom:8px}
.kv .ft a{color:var(--rose)}.kv .ft a:hover{color:#fff}
@media(max-width:900px){.kv .hero{background:linear-gradient(180deg,var(--rose) 0 62%,var(--char) 62% 100%)}.kv .hero .w{grid-template-columns:1fr}.kv .hero .ph{justify-self:start;width:min(100%,360px)}.kv .bl-g{grid-template-columns:repeat(2,minmax(0,1fr))}.kv .ft .w{grid-template-columns:1fr;gap:28px}
 .kv .burger{display:block}.kv .menu{display:none}.kv .menu-cb:checked ~ .menu{display:flex;flex-direction:column;gap:0;position:absolute;top:70px;left:16px;right:16px;background:var(--char);padding:10px;border:1px solid rgba(255,255,255,.25)}.kv .menu-cb:checked ~ .menu a{padding:14px 12px}}
@media(max-width:620px){.kv .bl-g{grid-template-columns:minmax(0,1fr);gap:16px}.kv .sec{padding:60px 0 70px}.kv .bl-body{padding:18px 18px 22px}}
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

def top(cur):
    return ('<div class="top"><div class="w"><a class="logo" href="/">Коваленко Н. О.</a><input type="checkbox" id="kvm" class="menu-cb" aria-hidden="true" tabindex="-1">'
            f'<nav class="menu" aria-label="Меню"><a href="/">Головна</a><a href="/blog/"{" class=\"cur\"" if cur=="blog" else ""}>Блог</a><a href="#contacts">Контакти</a></nav>'
            '<label for="kvm" class="burger" aria-label="Меню"><i></i></label></div></div>')

FOOT = ('<footer class="ft" id="contacts"><div class="w"><div><h3>Контакти</h3><p><a href="tel:+380508202176">+38 (050) 820-21-76</a></p>'
        f'<p><a href="{TG}" target="_blank" rel="noopener">Telegram</a> · <a href="https://www.facebook.com/profile.php?id=100087439299448" target="_blank" rel="noopener">Facebook</a></p></div>'
        '<div><h3>Графік роботи</h3><p>Пн–Пт<br>9:00 — 18:00</p></div>'
        '<div><h3>Корисні статті</h3><ul><li><a href="/blog/">Блог: усі статті</a></li><li><a href="/poniattia-bankrutstva/">Поняття банкрутства: юридичне визначення та ознаки</a></li>'
        '<li><a href="/primokolect-kolektorska-kompaniia-borhy-ta-pravovyi-zakhyst/">Прімоколект: колекторська компанія, борги та правовий захист</a></li></ul></div></div></footer>')

def hide(pid):
    return (f'body.page-id-{pid} .entry-header,body.page-id-{pid} .ast-breadcrumbs-wrapper,body.page-id-{pid} .entry-title,body.page-id-{pid} .site-footer{{display:none!important}}'
            f'body.page-id-{pid} .ast-container,body.page-id-{pid} #primary,body.page-id-{pid} .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}'
            f'body.page-id-{pid}{{background:#615C68}}')

def section(heading=True, n=3, pre=False):
    return ('<section class="sec%s" id="articles"><div class="w">' % (' pre' if pre else '') +
            ('<h2>Мої статті</h2><span class="bar"></span><p class="lead2">' + LEAD + '</p>' if heading else '') +
            '<div class="bl-g">' + ''.join(card(a) for a in items()[:n]) + '</div>' +
            ('<div class="all"><a class="btn" href="/blog/">Усі статті</a></div>' if heading else '') + '</div></section>')

def hub():
    hero = ('<header class="hero"><div class="w"><div><h1>Мої статті</h1><span class="bar"></span><p class="sub">Юрист з питань<br>банкрутства фізичних осіб</p>'
            f'<p class="lead">{LEAD}</p><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div>'
            f'<div class="ph"><img src="{PORTRAIT}" alt="Коваленко Наталія Олександрівна, юрист з питань банкрутства фізичних осіб" width="640" height="640"></div></div></header>')
    return f'<!-- wp:html -->\n<style>{CSS}{hide(HUB_ID)}</style>\n<div class="kv">{top("blog")}{hero}{section(False, 99)}{FOOT}</div>\n<!-- /wp:html -->'

def preview():
    return f'<!-- wp:html -->\n<style>{CSS}{hide(PREVIEW_ID)}</style>\n<div class="kv">{top("")}{section(True, 3, True)}{FOOT}</div>\n<!-- /wp:html -->'

def snippet():
    return f'<style>{CSS}</style>\n<div class="kv">{section(True, 3)}</div>'

if __name__ == '__main__':
    os.makedirs(os.path.join(H, 'out'), exist_ok=True)
    for n, f in [('blog-hub.html', hub), ('block-preview.html', preview), ('home-block-snippet.html', snippet)]:
        open(os.path.join(H, 'out', n), 'w', encoding='utf-8').write(f())
    print('ok')
