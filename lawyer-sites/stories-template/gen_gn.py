import math
CSS = """
@import url(fonts/all.css);
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
:root{--ink:#1C2430;--ink2:#273142;--soft:#4A5260;--cream:#F5F0E3;--cream2:#EBE4D0;--gold:#D3C283;--olive:#CDC28F;--olivet:#6B5F26}
body{position:relative;font-family:'Roboto Condensed',sans-serif;font-weight:600;color:var(--ink);background:#F5F0E3;-webkit-font-smoothing:antialiased}
.abs{position:absolute}.serif{font-family:'Noto Serif',serif;font-weight:900}.cn{font-family:'Roboto Condensed',sans-serif}
.full{left:0;top:0;width:1080px;height:1920px}
.bg{background:linear-gradient(180deg,#FBF8EE 0%,#F5F0E3 40%,#EBE4D0 72%,#DDD4B8 100%)}
.grain{left:0;top:0;width:1080px;height:1920px;opacity:.16;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 1.4 -.15'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.top{left:72px;width:936px;top:252px;height:40px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:23px;letter-spacing:3px;text-transform:uppercase}
.top .d{border-bottom:3px solid var(--gold);padding-bottom:6px}
.top .k{color:var(--soft)}
.gbox{left:72px;width:936px;top:284px;height:230px;display:flex;align-items:flex-end;justify-content:center}
.giant{line-height:.74;white-space:nowrap;display:inline-block;color:var(--ink)}
.colm{display:flex;flex-direction:column;gap:26px}
.co{position:relative;width:262px}
.co::before{content:'';display:block;width:54px;border-top:5px solid var(--gold);margin-bottom:12px}
.co b{display:block;font-weight:900;font-size:40px;line-height:.98;text-transform:uppercase;color:var(--ink);margin-bottom:9px;letter-spacing:.3px}
.co p{font-weight:600;font-size:24px;line-height:1.22;color:var(--soft)}
.scrim{left:0;top:1090px;width:1080px;height:830px;background:linear-gradient(to bottom,rgba(28,36,48,0),rgba(28,36,48,.55) 16%,rgba(28,36,48,.90) 38%,rgba(22,29,39,.97) 100%)}
.hl{left:72px;width:936px;top:1182px;display:flex;flex-direction:column;align-items:center}
.hl .ln{display:table;font-weight:900;text-transform:uppercase;line-height:.98;white-space:nowrap;color:#fff;text-shadow:0 3px 18px rgba(0,0,0,.35);margin:0 auto}
.hl .ln mark{background:var(--gold);color:var(--ink);padding:0 16px;text-shadow:none;display:inline-block;line-height:.98}
.sub{left:72px;width:936px;text-align:center;top:1500px;font-weight:700;font-size:25px;letter-spacing:3px;text-transform:uppercase;color:var(--olive)}
.plate{left:72px;width:936px;top:1556px;height:84px;background:var(--gold);color:var(--ink);font-size:46px;font-weight:700;letter-spacing:1px;display:flex;align-items:center;justify-content:center;text-transform:none}
.foot{left:72px;width:936px;top:1716px;border-top:2px solid rgba(211,194,131,.35);padding-top:18px;text-align:center;font-weight:600;font-size:23px;letter-spacing:5px;color:rgba(245,240,227,.55)}
"""
CITY = '''<svg class="abs" style="left:0;top:520px" width="1080" height="700" viewBox="0 0 1080 700">
<defs><linearGradient id="cg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#273142" stop-opacity=".07"/><stop offset="1" stop-color="#273142" stop-opacity=".01"/></linearGradient></defs>
<g fill="url(#cg)">
<rect x="-10" y="260" width="90" height="440"/><rect x="90" y="170" width="70" height="530"/><rect x="170" y="310" width="100" height="390"/><rect x="280" y="230" width="60" height="470"/>
<rect x="760" y="250" width="70" height="450"/><rect x="840" y="120" width="60" height="580"/><rect x="852" y="60" width="36" height="60"/><rect x="866" y="10" width="8" height="52"/><rect x="910" y="220" width="80" height="480"/><rect x="1000" y="300" width="90" height="400"/>
</g>
<g stroke="#D3C283" stroke-width="2" fill="none" opacity=".75">
<polyline points="30,120 130,200 90,330 220,380"/><polyline points="130,200 260,110 330,190"/><polyline points="1040,140 940,230 980,340 860,390"/><polyline points="940,230 830,150 760,230"/>
</g>
<g fill="#D3C283" opacity=".95"><circle cx="30" cy="120" r="7"/><circle cx="130" cy="200" r="9"/><circle cx="90" cy="330" r="6"/><circle cx="220" cy="380" r="7"/><circle cx="260" cy="110" r="6"/><circle cx="330" cy="190" r="7"/>
<circle cx="1040" cy="140" r="7"/><circle cx="940" cy="230" r="9"/><circle cx="980" cy="340" r="6"/><circle cx="860" cy="390" r="7"/><circle cx="830" cy="150" r="6"/><circle cx="760" cy="230" r="7"/></g>
</svg>'''
ROAD = '<svg class="abs" style="left:0;top:1180px" width="1080" height="740" viewBox="0 0 1080 740"><g stroke="#D3C283" stroke-width="2" opacity=".28" fill="none">' + ''.join(f'<line x1="540" y1="0" x2="{x}" y2="740"/>' for x in range(-900,2000,120)) + ''.join(f'<line x1="0" y1="{y}" x2="1080" y2="{y}"/>' for y in (160,300,470,680)) + '</g></svg>'
SCRIPT = """<script>document.fonts.ready.then(()=>{
const gs=document.getElementById('g');gs.style.fontSize='100px';const k=936/gs.getBoundingClientRect().width;gs.style.fontSize=Math.min(%d,100*k)+'px';
const lns=[...document.querySelectorAll('.hl .ln')];lns.forEach(e=>e.style.fontSize='100px');
const mw=Math.max(...lns.map(e=>e.getBoundingClientRect().width));const fs=Math.min(%d,100*936/mw,300/(lns.length*.98));lns.forEach(e=>e.style.fontSize=fs+'px');
})</script>"""
PH={'about':dict(fx=1034,hy=19,w=1800,h=2212),'hero':dict(fx=920,hy=362,w=1800,h=2472),'hall':dict(fx=1142,hy=205,w=2200,h=2450)}
def page(c):
    ph=PH[c['photo']]; k=c['k']
    left=540+c.get('shift',0)-ph['fx']*k; top=c.get('hair',476)-ph['hy']*k
    def col(x):
        items=[t for t in c['co'] if t[0]==x]
        w=max((t[4] if len(t)>4 else 262) for t in items)
        inner=''.join(f'<div class="co" style="width:{(t[4] if len(t)>4 else 262)}px"><b>{t[2]}</b><p>{t[3]}</p></div>' for t in items)
        return f'<div class="abs colm" style="left:{x}px;top:590px;width:{w}px">{inner}</div>'
    cos=col(72)+col(746)
    lines=''.join(f'<span class="ln">{t}</span>' for t in c['lines'])
    return f"""<!doctype html><html lang="uk"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="abs full bg"></div>
<div class="abs" style="left:{c.get('gx',140)}px;top:330px;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95),rgba(255,255,255,0) 68%)"></div>
{CITY}
<div class="abs top"><span class="k">Кредитна історія • Бюро • Прострочення</span><span class="d">{c['date']}</span></div>
<div class="abs gbox"><span id="g" class="giant serif">{c['giant']}</span></div>
<img class="abs" src="gn_{c['photo']}.png" style="left:{left}px;top:{top}px;width:{ph['w']*k}px;height:{ph['h']*k}px;filter:drop-shadow(0 6px 22px rgba(28,36,48,.30))">
{cos}
<div class="abs scrim"></div>
{ROAD}
<div class="abs hl cn">{lines}</div>
<div class="abs sub cn">{c['sub']}</div>
<div class="abs plate cn">Читайте мою нову статтю</div>
<div class="abs foot cn">ukrjurist.com.ua</div>
<div class="abs grain"></div>
{SCRIPT % (c.get('gmax',270), c.get('hmax',122))}</body></html>"""
HL=lambda *a:list(a)
covers={
'g1':dict(photo='about',k=.72,date='09.11.2026',giant='10 РОКІВ',
 co=[(72,596,'Звіт безоплатно','отримайте звіт і перевірте дати закриття кредитів',236),(72,770,'Що рахують','строк від припинення правочину, а не від прострочки',236),(746,596,'Ст. 10 Закону','строк зберігання: десять років (частина 3)'),(746,770,'Оскарження','недостовірні дані оскаржують за ст. 13 Закону')],
 lines=['Скільки зберігається','<mark>кредитна історія</mark>','в Україні?'],sub='Вікторія Гончарук · юрист по кредитах'),
'g2':dict(photo='hall',k=.62,date='06.11.2026',giant='СУД',gx=100,
 co=[(72,596,'Суд не пише','кредитну історію до бюро'),(72,770,'Дані передає','кредитор: банк або фінансова компанія'),(746,596,'Прострочення','з’являється задовго до рішення суду'),(746,770,'Борг не за кредитом','як правило, у бюро не передається')],
 lines=['Чи впливає','судова заборгованість','<mark>на кредитну історію?</mark>'],sub='Відповідь юриста · Вікторія Гончарук'),
'g3':dict(photo='hero',k=.72,shift=40,date='05.11.2026',giant='ВІДМОВА',
 co=[(72,596,'Що пропонують','менша сума, вища ціна, коротший строк',215),(72,770,'Реальний ризик','потрапити до шахраїв',215),(746,596,'Звіт до заявки','перевірте безоплатно свою історію'),(746,770,'Рішення','ухвалює кредитор, а не бюро')],
 lines=['Кредит з поганою','кредитною історією:','як не потрапити','<mark>в пастку?</mark>'],sub='Вікторія Гончарук · юрист по кредитах'),
'g4':dict(photo='about',k=.72,shift=0,date='04.11.2026',giant='1 ДЕНЬ',
 co=[(72,596,'Може потрапити','а може й ні: усе залежить від договору',236),(72,770,'Важливо','чи передав кредитор дані до бюро і коли',236),(746,596,'Погасіть до звіту','до того, як кредитор сформує звіт'),(746,770,'Без паніки','але й без легковажності')],
 lines=['Чи впливає','прострочення','<mark>на кредитну історію?</mark>'],sub='Відповідь юриста · Вікторія Гончарук'),
'g5':dict(photo='hall',k=.66,shift=0,date='02.11.2026',giant='ЗАПИС',gx=60,hair=480,
 co=[(72,596,'Правдивий запис','не видалити: його закривають погашенням'),(72,770,'Помилковий запис','вилучають заявою до бюро або через суд'),(746,596,'Довідка','про відсутність заборгованості'),(746,770,'Нова історія','вчасні платежі перекривають стару')],
 lines=['Як виправити','кредитну історію,','якщо були','<mark>прострочення?</mark>'],sub='Пояснення юриста · Вікторія Гончарук'),
}
for n,c in covers.items(): open(n+'.html','w').write(page(c))
print('ok')
