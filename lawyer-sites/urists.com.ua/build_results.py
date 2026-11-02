"""Сторінка «Результати роботи» (urists.com.ua): той самий стиль S3, що й головна.
Usage: python3 build_results.py [RES_BASE_URL]  → results.html (прев'ю), results.wp.txt (wp:html)
"""
import sys, os, re, html, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from results_data import R, R2
res_base = sys.argv[1] if len(sys.argv) > 1 else 'img/results/yakovenko-rezultat-'
HOME = sys.argv[2] if len(sys.argv) > 2 else '/'
TG = 'https://t.me/yakovenko_lawyer'

src = open(os.path.join(HERE, 'home.src.html'), encoding='utf-8').read()
head = src[:src.index('<div class="yk" id="top">')]
head = re.sub(r'<meta name="description" content="[^"]*">',
  '<meta name="description" content="Документи з реальних справ юриста Дмитра Яковенка: гарантійні листи та листи про врегулювання заборгованості перед МФО. Персональні дані клієнтів закрито.">', head, 1)
cta_footer = src[src.index('<!-- CTA -->'):src.index('</div>\n\n<script type="application/ld+json">')]
cta_footer = cta_footer.replace('<section class="panel cta dark">', '<section class="panel cta dark">', 1)

def nb(x):
    x = re.sub(r'(\d) (?=\d{3}\b)', '\\1\u00a0', x)
    return re.sub(r' (грн|заміст)', '\u00a0\\1', x)
ZOOM = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5M11 8v6M8 11h6"/></svg>'
ARROW = '<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
cards = '\n'.join(
  f'      <article class="res"><button class="res-ph" type="button" data-full="{res_base}{n:02d}.webp" data-alt="{html.escape(alt)}" aria-label="Збільшити: {html.escape(h)}">'
  f'<img src="{res_base}{n:02d}.webp" alt="{html.escape(alt)}" width="1000" height="1414" loading="lazy"><i>{ZOOM}</i></button>'
  f'<div class="res-tx"><h3>{html.escape(nb(h))}</h3><p>{html.escape(nb(t))}</p></div><div class="bar">Результат клієнта</div></article>'
  for n, h, t, alt in R + R2)

extra_css = '''<style>
.yk .hero.sub{min-height:0}
.yk .sub-body{position:relative;z-index:2;padding:clamp(34px,5vw,80px) clamp(22px,5vw,88px) clamp(46px,6vw,90px);max-width:1320px;margin:0 auto;width:100%}
.yk .sub-body h1{font-size:clamp(40px,5.6vw,84px);margin:18px 0 20px}
.yk .sub-body h1 em{font-style:normal;color:var(--gold)}
.yk .sub-body .lead{max-width:640px;color:#CBCDE0;font-size:clamp(16px,1.3vw,19px)}
.yk .sub-body .acts{display:flex;flex-wrap:wrap;gap:14px;margin-top:30px}
.yk .sub-ring{position:absolute;right:-160px;top:-120px;width:560px;height:560px;border-radius:50%;border:70px solid rgba(201,160,106,.10);z-index:1}
.yk .results.page{padding-top:clamp(40px,5vw,70px)}
@media(max-width:860px){.yk .sub-ring{width:340px;height:340px;border-width:44px;right:-120px;top:-90px}}
</style>
'''

page = f'''{head}{extra_css}
<div class="yk" id="top">

<section class="panel hero sub dark">
  <div class="sub-ring"></div>
  <div class="nav">
    <a class="logo" href="{HOME}"><b>Яковенко Дмитро</b><span>Юрист</span></a>
    <nav>
      <a href="{HOME}#about">Про мене</a>
      <a href="{HOME}#services">Послуги</a>
      <a href="#results">Результати</a>
      <a href="{HOME}#reviews">Відгуки</a>
      <a href="#contacts">Контакти</a>
    </nav>
    <a class="btn sm" href="{TG}" target="_blank" rel="noopener"><span class="lg">Написати в Telegram</span><span class="sh">Telegram</span><i>{ARROW}</i></a>
  </div>
  <div class="sub-body">
    <span class="eyebrow">Результати · Яковенко Дмитро</span>
    <h1>Результати роботи</h1>
    <p class="lead">Документи з реальних справ: гарантійні листи та листи про врегулювання заборгованості. Персональні дані клієнтів закрито. Натисніть на документ, щоб збільшити.</p>
    <div class="acts">
      <a class="btn" href="{TG}" target="_blank" rel="noopener">Отримати консультацію<i>{ARROW}</i></a>
      <a class="btn line" href="{HOME}">На головну<i>{ARROW}</i></a>
    </div>
  </div>
</section>

<section class="results page" id="results">
  <div class="in">
    <div class="res-g">
{cards}
    </div>
  </div>
</section>
<div class="lb" id="lb" hidden><button class="lb-x" type="button" aria-label="Закрити">×</button><img id="lb-img" alt=""></div>
<script>
(function(){{var lb=document.getElementById('lb'),im=document.getElementById('lb-img');if(!lb)return;
function close(){{lb.hidden=true;im.removeAttribute('src');document.body.style.overflow=''}}
document.querySelectorAll('.res-ph').forEach(function(b){{b.addEventListener('click',function(){{im.src=b.getAttribute('data-full');im.alt=b.getAttribute('data-alt');lb.hidden=false;document.body.style.overflow='hidden'}})}});
lb.addEventListener('click',close);document.addEventListener('keydown',function(ev){{if(ev.key==='Escape')close()}});}})();
</script>

{cta_footer}
</div>

<script type="application/ld+json">
{json.dumps({
 "@context": "https://schema.org", "@type": "CollectionPage",
 "name": "Результати роботи", "url": "https://urists.com.ua/rezultaty-roboty/", "inLanguage": "uk",
 "description": "Документи з реальних справ юриста Дмитра Яковенка: гарантійні листи та листи про врегулювання заборгованості.",
 "about": {"@id": "https://urists.com.ua/#person"},
 "isPartOf": {"@type": "WebSite", "name": "Юристи України", "url": "https://urists.com.ua/"}
}, ensure_ascii=False, indent=2)}
</script>
'''
open(os.path.join(HERE, 'results.html'), 'w', encoding='utf-8').write(
  '<!doctype html><html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Результати роботи — Яковенко Дмитро</title></head><body style="margin:0">' + page + '</body></html>')
open(os.path.join(HERE, 'results.wp.txt'), 'w', encoding='utf-8').write('<!-- wp:html -->\n' + page + '\n<!-- /wp:html -->')
print('ok', len(page))
