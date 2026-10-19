"""Builds the standalone page «Результати роботи» (14 documents = 8 from home + 6 new) in the same S2 style.
usage: python3 build_results_page.py ../index.html out.html"""
import sys,html,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from results_data import R,R2
src,out=sys.argv[1],sys.argv[2]
e=html.escape
WP='https://uchet.com.ua/wp-content/uploads/2026/10/borysov-rezultat-'
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
s=open(src,encoding='utf-8').read()
head=s[:s.index('<header class="hero">')]
foot=s[s.index('<footer class="page-end"'):]
foot=foot[:foot.index('<script type="application/ld+json">')]  # keep footer + fab, drop Person schema
head=head.replace('</style>','''.uc .hero.sub{padding-bottom:0}
.uc .hero.sub .hero-g{min-height:0;display:block}
.uc .hero.sub .hero-t{width:auto;max-width:760px;padding:30px 0 clamp(70px,9vw,110px)}
.uc .crumbs{font-size:13px;color:#A9A89F;margin-bottom:18px}.uc .crumbs a{color:var(--kh-l)}
.uc .hero.sub h1{font-size:clamp(34px,5.4vw,64px)}
.uc .hero.sub h1 em{display:inline}
.uc .res-intro{padding-bottom:0}
.uc .res-cta{display:flex;justify-content:center;margin-top:40px}
</style>''',1)
hdr=f'''<header class="hero sub"><div class="w nav-w">
 <div class="nav"><a class="logo" href="/">БОРИСОВ <b>·</b> ЮРИСТ</a><a class="tg" href="https://t.me/yrist_maxim" target="_blank" rel="noopener">@yrist_maxim</a></div>
</div>
<div class="w">
 <div class="hero-g" id="top"><div class="hero-t">
  <div class="crumbs"><a href="/">Головна</a> / Результати роботи</div>
  <h1>Результати <em>роботи</em></h1>
  <p>Документи з реальних справ: гарантійні листи й листи про врегулювання заборгованості. Персональні дані клієнтів закрито.</p>
  <a class="btn" href="https://t.me/yrist_maxim" target="_blank" rel="noopener">Обговорити вашу справу <i>{ARROW}</i></a>
 </div></div>
</div></header>
'''
def cards(L): return ''.join(f'''  <article class="res"><button class="res-photo" type="button" data-full="{WP}{sl}.webp" data-alt="{e(alt)}" aria-label="Збільшити: {e(h)}"><img src="{WP}{sl}.webp" alt="{e(alt)}" width="1000" height="1414" loading="lazy"></button><div class="res-tx"><h3>{e(h)}</h3><p>{e(t)}</p></div><div class="bar">Результат клієнта</div></article>
''' for sl,_,h,t,alt in L)
body=f'''<section id="results"><div class="w">
 <span class="eyebrow">Всі результати</span>
 <h2>Документи <em>наших клієнтів</em></h2>
 <p class="lead">Усього {len(R)+len(R2)} документів. Натисніть на документ, щоб переглянути його збільшеним.</p>
 <div class="res-grid">
{cards(R)}{cards(R2)} </div>
 <div class="res-cta"><a class="btn wide" href="https://t.me/yrist_maxim" target="_blank" rel="noopener">Отримати консультацію в Telegram <i>{ARROW}</i></a></div>
</div></section>
<div class="lb" id="lb" hidden><button class="lb-x" type="button" aria-label="Закрити">×</button><img id="lb-img" alt=""></div>
<script>
(function(){{var lb=document.getElementById('lb'),im=document.getElementById('lb-img');if(!lb)return;
function close(){{lb.hidden=true;im.removeAttribute('src');document.body.style.overflow=''}}
document.querySelectorAll('.res-photo').forEach(function(b){{b.addEventListener('click',function(){{im.src=b.getAttribute('data-full');im.alt=b.getAttribute('data-alt');lb.hidden=false;document.body.style.overflow='hidden'}})}});
lb.addEventListener('click',close);document.addEventListener('keydown',function(ev){{if(ev.key==='Escape')close()}});}})();
</script>
'''
ld='''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"CollectionPage","name":"Результати роботи","url":"https://uchet.com.ua/rezultaty-roboty/","inLanguage":"uk","about":{"@type":"Person","@id":"https://uchet.com.ua/#person","name":"Максим Юрійович Борисов"}}
</script>
</div>
<!-- /wp:html -->
'''
res=head+hdr+body+foot+ld
open(out,'w',encoding='utf-8').write(res); print('ok',len(res),res.count('class="res"'))
