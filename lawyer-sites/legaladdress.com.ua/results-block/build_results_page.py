"""Builds the standalone page «Результати роботи» (draft) from the final home page content (page13_final.html).
usage: python3 build_results_page.py home_final.html out.html [--local DIR]"""
import sys,re,json,html,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from results_data import R
home,out=sys.argv[1],sys.argv[2]
local=sys.argv[sys.argv.index('--local')+1] if '--local' in sys.argv else None
WP='https://legaladdress.com.ua/wp-content/uploads/2026/10/boychuk-rezultat-'
def src(slug): return f'{local}/boychuk-rezultat-{slug}.webp' if local else f'{WP}{slug}.webp'
s=open(home,encoding='utf-8').read()
style=s[s.index('<link rel="preconnect"'):s.index('</style>')+8]   # fonts + css (incl. results/reviews css)
DESC='Результати роботи юриста Бойчука Артема Валерійовича: гарантійні листи та угоди про врегулювання заборгованості за кредитами. Персональні дані клієнтів закрито.'
SCHEMA={"@context":"https://schema.org","@type":"CollectionPage","name":"Результати роботи — Бойчук Артем Валерійович","description":DESC,
 "url":"https://legaladdress.com.ua/rezultaty-roboty/","about":{"@id":"https://legaladdress.com.ua/#boychuk"},
 "isPartOf":{"@type":"WebSite","name":"Бойчук Артем Валерійович","url":"https://legaladdress.com.ua/"}}
head=f'<meta name="description" content="{DESC}">\n<script type="application/ld+json">{json.dumps(SCHEMA,ensure_ascii=False)}</script>'
nav=s[s.index('<div class="nav">'):s.index('</div>',s.index('Telegram</a>',s.index('<div class="nav">')))+6]
nav=nav.replace('href="#top"','href="/"').replace('href="#about"','href="/#about"').replace('href="#services"','href="/#services"').replace('<li><a href="#results">Результати</a></li>','<li><a href="#results" class="cur">Результати</a></li>').replace('href="#reviews"','href="/#reviews"').replace('href="#contacts"','href="#contacts"')
footer=s[s.index('<!-- ФУТЕР'):s.rindex('</div>')]   # footer section (up to closing of .bz)
cards=''.join(f'''    <article class="res"><button class="res-photo" type="button" data-full="{src(sl)}" data-alt="{html.escape(alt)}" aria-label="Збільшити: {html.escape(h)}"><img src="{src(sl)}" alt="{html.escape(alt)}" width="1000" height="1414" loading="lazy"></button><h2>{html.escape(h)}</h2><p>{html.escape(t)}</p></article>
''' for sl,h,t,alt in R)
CSS='''
/* results page */
.bz .rp-hero{background:var(--brown-dark);color:var(--cream)}
.bz .rp-hero .nav ul a.cur{color:var(--gold)}
.bz .rp-head{position:relative;text-align:center;padding:76px 28px 84px;max-width:860px;margin:0 auto}
.bz .rp-head .res-badge{background:var(--gold);color:var(--brown-dark)}
.bz .rp-head h1{font-size:clamp(34px,5.4vw,64px);line-height:1.1;margin:0 0 20px;color:var(--cream)}
.bz .rp-head h1 span{color:var(--gold)}
.bz .rp-head h1::after{content:"";display:block;width:110px;height:3px;margin:22px auto 0;border-radius:3px;background:var(--gold)}
.bz .rp-head .lead{color:var(--cream-soft);margin:0 auto 12px;max-width:680px}
.bz .rp-count{display:inline-flex;gap:10px;align-items:center;margin-top:10px;padding:8px 18px;border:1px solid var(--line-d);border-radius:999px;font-size:13.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--cream-soft)}
.bz .rp-count b{font-family:var(--f-head);font-weight:400;font-size:22px;color:var(--gold);letter-spacing:0}
.bz .rp-list{box-shadow:0 18px 44px -22px rgba(43,23,17,.35);border:1px solid rgba(212,178,122,.55)}
.bz .rp-list .res-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:18px}
.bz .rp-list .res{flex:0 0 calc(25% - 13.5px)}
.bz .res h2{font-size:16.5px;line-height:1.25;margin:0 6px 8px;text-transform:uppercase;letter-spacing:.03em}
@media(max-width:1100px){.bz .rp-list .res{flex-basis:calc(50% - 9px)}}
@media(max-width:620px){.bz .rp-list .res{flex-basis:100%}.bz .res h2{font-size:18px}.bz .rp-head{padding:54px 8px 60px}}
.bz .rp-cta{background:var(--brown);color:var(--cream);text-align:center}
.bz .rp-cta h2{color:var(--cream);margin-bottom:14px}
.bz .rp-cta .lead{margin:0 auto 28px;color:var(--cream-soft)}
'''
i=style.rindex('</style>'); style=style[:i]+CSS+style[i:]
body=f'''<div class="bz" lang="uk" id="top">

<section class="hero"><div class="wrap">
<div class="panel rp-hero">
  {nav}
  <div class="rp-head"><span class="res-badge">Реальні документи</span>
    <h1>Результати <span>роботи</span></h1>
    <p class="lead">Гарантійні листи й угоди про врегулювання заборгованості за кредитами. Персональні дані клієнтів закрито, у документах залишилися лише реквізити кредиторів, суми та строки.</p>
    <span class="rp-count"><b>{len(R)}</b> документів</span>
  </div>
</div>
</div></section>

<section id="results"><div class="wrap">
<div class="panel on-white pad res-panel rp-list">
  <div class="res-grid">
{cards}  </div>
</div>
</div></section>

<section><div class="wrap">
<div class="panel pad rp-cta">
  <span class="rule" style="margin-left:auto;margin-right:auto"></span>
  <h2>Хочете такий самий результат?</h2>
  <p class="lead">Опишіть ситуацію в Telegram: розберемо договір, підкажемо, що робити, і складемо план дій.</p>
  <a class="btn" href="https://t.me/artem_adwokat" target="_blank" rel="noopener">Безкоштовна консультація</a>
</div>
</div></section>

<div class="lb" id="lb" hidden><button class="lb-x" type="button" aria-label="Закрити">×</button><img id="lb-img" alt=""></div>
<script>
(function(){{var lb=document.getElementById('lb');var im=document.getElementById('lb-img');if(!lb){{return}}
function close(){{lb.hidden=true;im.removeAttribute('src');document.body.style.overflow=''}}
document.querySelectorAll('.res-photo').forEach(function(b){{b.addEventListener('click',function(){{im.src=b.getAttribute('data-full');im.alt=b.getAttribute('data-alt');lb.hidden=false;document.body.style.overflow='hidden'}})}});
lb.addEventListener('click',close);document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{close()}}}});}})();
</script>

{footer}
</div>
'''
res=f'<!-- wp:html -->\n{head}\n{style}\n<style>.bz{{width:100%;margin:0;min-height:100vh}}html,body{{margin:0!important;padding:0!important;background:#F5EEE4!important}}html{{scroll-behavior:smooth}}</style>\n{body}\n<!-- /wp:html -->\n'
open(out,'w',encoding='utf-8').write(res)
print('ok',len(res),'&&:',res.count('&&'),'cards:',res.count('class="res"'),'h1:',res.count('<h1'))
