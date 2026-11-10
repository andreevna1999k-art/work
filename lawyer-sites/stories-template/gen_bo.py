CSS = """
@import url(fonts/all.css);
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
:root{--ink:#0D1017;--kh:#7A6D3C;--khl:#D2C48F;--panel:#F5F3EC;--mid:#A9A89F;--tx:#262626}
body{font-variant-ligatures:none;font-feature-settings:'liga' 0,'dlig' 0,'clig' 0,'calt' 0;position:relative;font-family:'Noto Sans',sans-serif;font-weight:600;color:var(--panel);background:#0D1017;-webkit-font-smoothing:antialiased}
.abs{position:absolute}.pf{font-family:'Playfair Display',serif}
.full{left:0;top:0;width:1080px;height:1920px}
.grain{left:0;top:0;width:1080px;height:1920px;opacity:.22;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 1.4 -.15'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.gbox{left:72px;width:640px;top:290px;height:262px;display:flex;align-items:flex-end}
.giant{font-family:'Playfair Display',serif;font-weight:900;line-height:.72;white-space:nowrap;display:inline-block;color:rgba(169,168,159,.62)}
.tagb{display:inline-block;background:var(--panel);color:var(--ink);font-weight:800;font-size:20px;letter-spacing:2.5px;padding:5px 12px;text-transform:uppercase}
.rc{left:700px;width:308px;top:256px;text-align:right}
.rc .a{font-family:'Playfair Display',serif;font-weight:900;font-size:43px;line-height:1.02;text-transform:uppercase;color:#fff;margin-top:16px}
.rc .as{font-family:'Playfair Display',serif;font-weight:900;font-size:25px;line-height:1.12;text-transform:uppercase;color:var(--khl);margin-top:8px}
.rc .r{width:110px;height:6px;background:#fff;margin:22px 0 22px auto}
.rc .b{font-family:'Playfair Display',serif;font-weight:700;font-size:35px;line-height:1.04;text-transform:uppercase;color:#fff}
.rc .bs{font-family:'Playfair Display',serif;font-weight:900;font-size:23px;line-height:1.12;text-transform:uppercase;color:var(--khl);margin-top:8px}
.lc{left:72px;top:640px;width:300px}
.lc .a{font-family:'Playfair Display',serif;font-weight:900;font-size:44px;line-height:1.0;text-transform:uppercase;color:#fff;margin-top:14px}
.lc .as{font-family:'Playfair Display',serif;font-weight:900;font-size:30px;line-height:1.08;text-transform:uppercase;color:var(--khl);margin-top:10px}
.vg{left:0;top:0;width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 38%,rgba(0,0,0,0) 38%,rgba(5,7,10,.62) 100%)}
.scrim{left:0;top:1040px;width:1080px;height:880px;background:linear-gradient(to bottom,rgba(13,16,23,0),rgba(13,16,23,.82) 14%,rgba(13,16,23,.93) 40%,rgba(10,12,17,.98) 100%)}
.eb{left:72px;top:1118px;font-weight:700;font-size:23px;letter-spacing:12px;text-transform:uppercase;color:var(--khl)}
.hl{left:72px;width:936px;top:1160px}
.hl .ln{display:table;font-family:'Playfair Display',serif;font-weight:900;text-transform:uppercase;line-height:.98;white-space:nowrap;color:#fff;letter-spacing:-.5px}
.hl .ln .dim{color:rgba(169,168,159,.8);font-weight:700}
.sb{left:72px;top:1476px;font-weight:700;font-size:23px;letter-spacing:3px;text-transform:uppercase;color:var(--panel);width:936px}
.plate{left:72px;top:1556px;height:84px;padding:0 32px;background:var(--khl);color:var(--ink);font-size:46px;font-weight:600;display:flex;align-items:center;white-space:nowrap}
.foot{left:72px;width:936px;top:1716px;border-top:2px solid rgba(210,196,143,.3);padding-top:18px;text-align:center;font-weight:600;font-size:22px;letter-spacing:5px;color:var(--mid)}
"""
SCRIPT = """<script>document.fonts.ready.then(()=>{
const gs=document.getElementById('g');gs.style.fontSize='100px';const k=640/gs.getBoundingClientRect().width;gs.style.fontSize=Math.min(%d,100*k)+'px';
const lns=[...document.querySelectorAll('.hl .ln')];lns.forEach(e=>e.style.fontSize='100px');
const mw=Math.max(...lns.map(e=>e.getBoundingClientRect().width));const fs=Math.min(%d,100*936/mw,300/(lns.length*.98));lns.forEach(e=>e.style.fontSize=fs+'px');
})</script>"""
FILT={'warm':'grayscale(1) sepia(.5) contrast(1.18) brightness(.95)','neutral':'grayscale(1) contrast(1.22) brightness(.98)','cool':'grayscale(1) sepia(.35) hue-rotate(165deg) saturate(1.5) contrast(1.18) brightness(.98)'}
GLOW={'warm':'rgba(122,109,60,.55)','neutral':'rgba(70,78,92,.60)','cool':'rgba(40,78,96,.62)'}
FX,HY=900,48
def page(c):
    k=c['k']; tone=c['tone']
    left=540+c.get('shift',0)-FX*k; top=c.get('hair',566)-HY*k
    ra=c['ra']; lc=c['lc']
    return f"""<!doctype html><html lang="uk"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="abs full" style="background:linear-gradient(180deg,#141A24 0%,#0D1017 55%,#080A0F 100%)"></div>
<div class="abs" style="left:{c.get('gx',90)}px;top:300px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,{GLOW[tone]},rgba(13,16,23,0) 66%)"></div>
<div class="abs gbox"><span id="g" class="giant">{c['giant']}</span></div>
<img class="abs" src="bo_hero.png" style="left:{left}px;top:{top}px;width:{1920*k}px;height:{1920*k}px;filter:{FILT[tone]} drop-shadow(0 0 26px rgba(0,0,0,.6))">
<div class="abs vg"></div>
<div class="abs rc"><span class="tagb">{ra[0]}</span><div class="a">{ra[1]}</div><div class="as">{ra[2]}</div><div class="r"></div><div class="b">{ra[3]}</div><div class="bs">{ra[4]}</div></div>
<div class="abs lc"><span class="tagb">{lc[0]}</span><div class="a">{lc[1]}</div><div class="as">{lc[2]}</div></div>
<div class="abs scrim"></div>
<div class="abs eb">{c['eb']}</div>
<div class="abs hl">{''.join(f'<span class="ln">{t}</span>' for t in c['lines'])}</div>
<div class="abs sb">{c['sub']}</div>
<div class="abs plate">Читайте мою нову статтю</div>
<div class="abs foot">uchet.com.ua</div>
<div class="abs grain"></div>
{SCRIPT % (c.get('gmax',300), c.get('hmax',168))}</body></html>"""
covers={
'b1':dict(tone='warm',k=.66,giant='РЕЄСТР',
 ra=('Виїзд за кордон','Єдиний реєстр боржників','і система виконавчих проваджень','Обмеження виїзду','онлайн-сервіс ДПСУ'),
 lc=('Важливо','Потрібна ухвала суду','сам по собі борг виїзд не закриває'),
 eb='Покрокова інструкція',lines=['Як перевірити,','<span class="dim">чи є</span> борги','для виїзду за кордон?'],sub='Пояснює юрист Максим Борисов'),
'b2':dict(tone='neutral',k=.66,shift=-20,gx=60,giant='ПОРІГ',
 ra=('Кредити й картки','Фіксованого порогу немає','закон його не встановлює','Обмежує лише суд','рішення, провадження, ухилення'),
 lc=('Перед поїздкою','Перевірте реєстр','боржників до купівлі квитків'),
 eb='Відповідь юриста',lines=['З якою сумою','<span class="dim">не</span> випускають','за кордон?'],sub='Розмір боргу не має значення'),
'b3':dict(tone='cool',k=.78,hair=540,giant='3 РОКИ',
 ra=('Ст. 256, 257 ЦК','Загальний строк','позовної давності','Не від договору','рахують по кожному платежу'),
 lc=('Заявіть','Давність працює лише за заявою','до ухвалення рішення'),
 eb='Перевірте самостійно',lines=['Строк позовної','давності по кредиту:','<span class="dim">як</span> перевірити?'],sub='Давність не списує борг'),
'b4':dict(tone='warm',k=.66,shift=50,gx=150,giant='КАРТКА',
 ra=('Прострочка','Сама по собі','виїзд не забороняє','Банк не може','самостійно заборонити виїзд'),
 lc=('Три умови','Рішення суду','відкрите провадження й ухилення від виконання'),
 eb='Відповідь юриста',lines=['Чи випустять','за кордон з боргом','по кредитній картці?'],sub='Обмежити виїзд може лише суд'),
'b5':dict(tone='neutral',k=.72,giant='КОРДОН',
 ra=('Колектори','Не мають права','забороняти виїзд','Три умови','рішення суду, примусове виконання, ухилення'),
 lc=('За 10 хвилин','Перевірте свій статус','у реєстрі боржників'),
 eb='Пояснює юрист',lines=['Чи можна виїхати','з України,','<span class="dim">якщо є</span> кредит?'],sub='Кредит сам по собі кордон не закриває'),
}
for n,c in covers.items(): open(n+'.html','w').write(page(c))
print('ok')
