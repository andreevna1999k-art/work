"""Replaces «Результати» and «Відгуки» sections in index.html with the 8-document grid + 12 demo reviews.
usage: python3 build_blocks.py index.html out.html"""
import sys,re,html,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from results_data import R,RV
src,out=sys.argv[1],sys.argv[2]
WP='https://uchet.com.ua/wp-content/uploads/2026/10/borysov-rezultat-'
e=html.escape
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
cards=''.join(f'''  <article class="res"><button class="res-photo" type="button" data-full="{WP}{s}.webp" data-alt="{e(alt)}" aria-label="Збільшити: {e(h)}"><img src="{WP}{s}.webp" alt="{e(alt)}" width="1000" height="1414" loading="lazy"></button><div class="res-tx"><h3>{e(h)}</h3><p>{e(t)}</p></div><div class="bar">Результат клієнта</div></article>
''' for s,_,h,t,alt in R)
RES=f'''<section id="results"><div class="w">
 <span class="eyebrow">Результати</span>
 <h2>Результати <em>роботи</em></h2>
 <p class="lead">Документи з реальних справ: гарантійні листи та листи про врегулювання заборгованості. Персональні дані клієнтів закрито. Натисніть на документ, щоб збільшити.</p>
 <div class="res-grid">
{cards} </div>
</div></section>
<div class="lb" id="lb" hidden><button class="lb-x" type="button" aria-label="Закрити">×</button><img id="lb-img" alt=""></div>
<script>
(function(){{var lb=document.getElementById('lb'),im=document.getElementById('lb-img');if(!lb)return;
function close(){{lb.hidden=true;im.removeAttribute('src');document.body.style.overflow=''}}
document.querySelectorAll('.res-photo').forEach(function(b){{b.addEventListener('click',function(){{im.src=b.getAttribute('data-full');im.alt=b.getAttribute('data-alt');lb.hidden=false;document.body.style.overflow='hidden'}})}});
lb.addEventListener('click',close);document.addEventListener('keydown',function(ev){{if(ev.key==='Escape')close()}});}})();
</script>'''
stars=lambda n:'★'*n+'☆'*(5-n)
rv=''.join(f'''  <figure class="rv"><div class="rv-top"><span class="rv-st" aria-label="Оцінка {n} з 5">{stars(n)}</span><span class="rv-date">{d}</span></div><blockquote>{e(t)}</blockquote><figcaption><b>{e(nm)}</b><span>{e(pl)}</span></figcaption></figure>
''' for nm,pl,d,n,t in RV)
REV=f'''<section style="padding-top:0"><div class="rev">
 <span class="eyebrow">Відгуки</span>
 <h2>Відгуки <em>клієнтів</em></h2>
 <!-- ДЕМО: вигадані відгуки для перегляду макета. Замінити реальними або плагіном перед публікацією. Review/AggregateRating у JSON-LD НЕ додавати. -->
 <div class="rv-grid">
{rv} </div>
 <p class="demo-note">Демо-відгуки для перегляду макета. Перед публікацією замінити реальними відгуками або плагіном.</p>
 <div class="center" style="margin-top:28px"><a class="btn" style="background:var(--kh-l);color:var(--dark)" href="https://t.me/yrist_maxim" target="_blank" rel="noopener">Написати юристу <i style="background:var(--dark);color:var(--kh-l)">{ARROW}</i></a></div>
</div></section>'''
CSS='''/* results (grid 4/2/1) */
.uc .res-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;margin-top:34px}
.uc .res{display:flex;flex-direction:column;min-width:0;background:var(--panel);border-radius:28px;overflow:hidden}
.uc .res-photo{display:block;width:100%;aspect-ratio:3/4;padding:0;margin:0;border:0;background:#fff;cursor:zoom-in;position:relative;overflow:hidden}
.uc .res-photo img{width:100%;height:100%;object-fit:cover;object-position:50% 0;transition:transform .35s}
.uc .res-photo:hover img{transform:scale(1.03)}
.uc .res-photo::after{content:"";position:absolute;left:0;right:0;bottom:0;height:46px;background:linear-gradient(0deg,rgba(245,243,236,.95),rgba(245,243,236,0))}
.uc .res-tx{padding:18px 20px 20px;flex:1}
.uc .res-tx h3{font-size:16.5px;line-height:1.3;margin:0 0 8px;color:var(--dark)}
.uc .res-tx p{margin:0;font-size:14px;line-height:1.55;color:var(--tx2)}
.uc .res .bar{background:var(--dark);color:var(--kh-l);padding:14px 20px;font-weight:600;font-size:13.5px}
.uc .lead{color:var(--tx2);max-width:640px;margin:14px 0 0}
@media(max-width:1100px){.uc .res-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){.uc .res-grid{grid-template-columns:minmax(0,1fr);gap:16px}.uc .res-photo{aspect-ratio:4/5}.uc .res-tx h3{font-size:18px}.uc .res-tx p{font-size:15px}}
.uc .lb{position:fixed;inset:0;z-index:99999;background:rgba(13,16,23,.9);display:flex;align-items:center;justify-content:center;padding:24px;overflow:auto}
.uc .lb[hidden]{display:none}
.uc .lb img{max-width:min(920px,100%);max-height:100%;width:auto;height:auto;border-radius:12px;background:#fff}
.uc .lb-x{position:fixed;top:14px;right:18px;width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.4);background:rgba(0,0,0,.45);color:#fff;font-size:28px;line-height:1;cursor:pointer}
/* reviews (masonry columns) */
.uc .rv-grid{column-count:3;column-gap:18px;margin-top:32px}
.uc .rv{break-inside:avoid;margin:0 0 18px;padding:24px 24px 20px;border:1px solid rgba(210,196,143,.22);border-radius:28px;background:rgba(255,255,255,.05)}
.uc .rv-top{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:12px}
.uc .rv-st{color:var(--kh-l);letter-spacing:.12em;font-size:17px}
.uc .rv-date{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#A9A89F}
.uc .rv blockquote{margin:0 0 16px;font-size:15.5px;line-height:1.6;color:#ECEBE4}
.uc .rv figcaption{display:flex;flex-direction:column;gap:2px;border-top:1px solid rgba(210,196,143,.2);padding-top:12px}
.uc .rv figcaption b{font-size:15.5px;color:#fff}
.uc .rv figcaption span{font-size:13px;color:#A9A89F}
.uc .demo-note{margin-top:20px;padding:12px 16px;border:1px dashed rgba(210,196,143,.5);border-radius:18px;font-size:13px;color:#C9C8C0;text-align:center}
@media(max-width:1000px){.uc .rv-grid{column-count:2}}
@media(max-width:640px){.uc .rv-grid{column-count:1}.uc .rv{padding:20px 18px 16px}}
'''
s=open(src,encoding='utf-8').read()
a=s.index('<section><div class="w">\n <span class="eyebrow">Результати</span>')
c=s.index('<footer class="page-end"')
s=s[:a]+RES+'\n\n'+REV+'\n\n'+s[c:]
# drop old cases/reviews css, add new
b1=s.index('/* cases */'); b2=s.index('/* reviews */')
s=s[:b1]+CSS+s[b2:]
open(out,'w',encoding='utf-8').write(s)
print('ok',len(s))
