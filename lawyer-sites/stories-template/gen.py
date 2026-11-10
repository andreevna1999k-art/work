import html
CSS = """
@import url(fonts/all.css);
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
:root{--acc:#C9A262;--acc2:#E0C38F;--ink:#F3EBDD;--soft:#C9BFAC;--mute:#9A8F7B;--dk:#17130E}
body{position:relative;font-family:'Noto Sans',sans-serif;font-weight:600;color:var(--ink);background:#17130E;-webkit-font-smoothing:antialiased}
.abs{position:absolute}.serif{font-family:'Noto Serif',serif;font-weight:900}.sans{font-family:'Noto Sans',sans-serif;font-weight:600}
.full{left:0;top:0;width:1080px;height:1920px}
.bg{background:linear-gradient(180deg,#231D14 0%,#17130E 52%,#0D0A07 100%)}
.bk{position:absolute;border-radius:50%;filter:blur(34px)}
.grain{left:0;top:0;width:1080px;height:1920px;opacity:.2;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 1.4 -.15'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.top{left:72px;width:936px;top:258px;display:flex;justify-content:space-between;align-items:flex-end;font-size:25px;letter-spacing:3px;text-transform:uppercase;line-height:1}
.top span{padding-bottom:12px}.top .k{border-bottom:3px solid var(--acc)}.top .d{color:var(--soft);border-bottom:3px solid #3A3122}
.giant{left:72px;width:936px;text-align:center;line-height:.8;white-space:nowrap;color:var(--ink);top:322px}
.pt{width:1160px;height:1160px;background:url(cut2x.png) 0 0/1160px 1160px no-repeat;filter:drop-shadow(0 0 24px rgba(0,0,0,.5)) contrast(1.05) sepia(.12) saturate(.95)}
.fade{left:0;top:1048px;width:1080px;height:700px;background:linear-gradient(to bottom,rgba(15,12,8,0),rgba(15,12,8,.93) 14%,rgba(15,12,8,.985) 42%,rgba(15,12,8,.99) 100%)}
.co{position:absolute;width:262px}
.co::before{content:'';display:block;width:60px;border-top:5px solid var(--acc);margin-bottom:16px}
.co b{display:block;font-weight:600;color:var(--acc2);font-size:28px;letter-spacing:1.5px;line-height:1.12;text-transform:uppercase;margin-bottom:9px}
.co p{font-size:25px;line-height:1.27;color:var(--ink)}
.h{left:72px;top:1088px;letter-spacing:-.5px;color:var(--ink)}
.h mark{background:var(--acc);color:var(--dk);padding:0 16px;margin-left:-2px;display:inline-block;line-height:1.02}
.h em{font-style:normal;color:var(--acc)}
.sub{left:72px;font-size:29px;letter-spacing:2px;text-transform:uppercase;color:var(--acc2);white-space:nowrap}
.byline{left:72px;top:1500px;font-size:23px;letter-spacing:2px;text-transform:uppercase;white-space:nowrap;color:var(--soft)}
.byline i{font-style:normal;color:var(--acc)}
.plate{left:72px;top:1552px;height:84px;padding:0 30px;background:var(--acc);color:var(--dk);font-size:46px;display:flex;align-items:center;white-space:nowrap}
.foot{left:72px;width:936px;top:1716px;border-top:2px solid #3A3122;padding-top:18px;text-align:center;font-size:22px;letter-spacing:4px;color:var(--mute);text-transform:lowercase}
.glowb{left:0;top:1560px;width:1080px;height:520px;background:radial-gradient(ellipse at 50% 85%,rgba(201,162,98,.30),rgba(201,162,98,0) 65%)}
"""
def page(c):
    co=''.join(f'<div class="co" style="left:{x}px;top:{y}px;width:{w}px"><b>{b}</b><p>{p}</p></div>' for (x,y,w,b,p) in c['co'])
    hl=c['headline']
    sub=f'<div class="abs sub sans" style="top:{c.get("subtop",1390)}px">{c["sub"]}</div>' if c.get('sub') else ''
    return f"""<!doctype html><html lang="uk"><head><meta charset="utf-8"><style>{CSS}{c.get('css','')}</style></head><body>
<div class="abs full bg"></div>
{c.get('bokeh','')}
<div class="abs" style="left:{c['gl'][0]}px;top:{c['gl'][1]}px;width:820px;height:820px;background:radial-gradient(circle,rgba(201,162,98,.34),rgba(201,162,98,.09) 45%,rgba(23,19,14,0) 70%)"></div>
<div class="abs top sans"><span class="k">{c['kicker']}</span><span class="d">{c['date']}</span></div>
<div class="abs giant serif"><span id="g" data-w="936" style="display:inline-block;font-size:100px">{c['giant']}</span></div>
{c.get('obj','')}
<div class="abs pt" style="left:{c['pl']}px;top:{c['pt']}px"></div>
{co}
<div class="abs fade"></div>
<div class="abs glowb"></div>
<div class="abs h serif" id="h" style="font-size:{c['hs']}px;line-height:{c.get('lh',1.03)}">{hl}</div>
{sub}
<div class="abs byline sans">Бойчук Артем Валерійович <i>·</i> юрист по кредитах</div>
<div class="abs plate sans">Читайте мою нову статтю</div>
<div class="abs foot sans">legaladdress.com.ua</div>
<div class="abs grain"></div>
<script>document.fonts.ready.then(()=>{{const e=document.getElementById('g');const k=936/e.getBoundingClientRect().width;e.style.fontSize=(100*k)+'px';}})</script></body></html>"""

BOKEH1='<div class="bk" style="left:-50px;top:640px;width:230px;height:230px;background:rgba(201,162,98,.28)"></div><div class="bk" style="left:850px;top:430px;width:200px;height:200px;background:rgba(255,236,200,.14)"></div>'
BOKEH2='<div class="bk" style="left:860px;top:600px;width:210px;height:210px;background:rgba(201,162,98,.24)"></div><div class="bk" style="left:30px;top:420px;width:180px;height:180px;background:rgba(255,236,200,.12)"></div>'

DOC='''<div class="abs" style="left:770px;top:560px;width:290px;height:420px;background:#F3EBDD;transform:rotate(8deg);box-shadow:-14px 20px 40px rgba(0,0,0,.6);padding:34px 28px">
<i style="display:block;height:14px;width:56%;background:#17130E;margin-bottom:28px"></i>
'''+''.join('<i style="display:block;height:10px;background:#CFC4AE;margin-bottom:18px;border-radius:2px;width:%s"></i>'%w for w in ['94%','92%','76%'])+'''
<i style="display:block;height:10px;background:#E4D9C6;outline:4px solid #C9A262;outline-offset:7px;margin:26px 0;width:100%"></i>
'''+''.join('<i style="display:block;height:10px;background:#CFC4AE;margin-bottom:18px;border-radius:2px;width:%s"></i>'%w for w in ['94%','76%','94%'])+'</div>'

CHAT='''<div class="abs" style="left:790px;top:560px;width:218px;height:130px;background:#F3EBDD;border-radius:22px 22px 22px 4px;transform:rotate(-3deg);box-shadow:-10px 16px 30px rgba(0,0,0,.5);padding:26px 24px"><i style="display:block;height:11px;width:88%;background:#CFC4AE;border-radius:3px;margin-bottom:16px"></i><i style="display:block;height:11px;width:60%;background:#CFC4AE;border-radius:3px"></i></div>
<div class="abs" style="left:812px;top:730px;width:196px;height:110px;background:#C9A262;border-radius:22px 22px 4px 22px;transform:rotate(2deg);box-shadow:-10px 16px 30px rgba(0,0,0,.5);padding:24px 22px"><i style="display:block;height:11px;width:84%;background:#17130E;opacity:.55;border-radius:3px;margin-bottom:16px"></i><i style="display:block;height:11px;width:50%;background:#17130E;opacity:.55;border-radius:3px"></i></div>'''

BADGE='''<div class="abs serif" style="left:768px;top:548px;width:236px;height:236px;border-radius:50%;background:#C9A262;color:#17130E;font-size:130px;line-height:236px;text-align:center;box-shadow:-12px 18px 36px rgba(0,0,0,.55);border:6px solid #E0C38F;outline:3px solid #C9A262;outline-offset:8px">НІ</div>'''

covers={
'g1':dict(kicker='Правовий розбір · колектори',date='09.11.2026',giant='КОЛЕКТОРИ',pl=-18,pt=386,gl=(130,360),hs=116,lh=1.0,bokeh=BOKEH1,
 headline='Банк передав<br>справу:<br><mark>що робити?</mark>',
 co=[(72,596,236,'Не платіть за дзвінком','і нічого не підписуйте'),(72,846,236,'Перевірте колектора','у реєстрі Національного банку України'),
     (776,596,232,'Борг не зникає','і від передачі справи не збільшується'),(776,846,232,'Дві ситуації','колектор від імені банку або новий кредитор')]),
'g2':dict(kicker='Правовий розбір · кредитний договір',date='06.11.2026',giant='ДОГОВІР',pl=82,pt=420,gl=(250,380),hs=118,bokeh=BOKEH1,obj=DOC,
 headline='Як оскаржити<br>його в суді?',sub='<span style="color:#C9A262">—</span> Покрокова інструкція юриста',
 co=[(72,596,236,'Аналіз договору','і власний розрахунок боргу'),(72,846,214,'Претензія','кредитодавцю, за потреби — позов')]),
'g3':dict(kicker='Правовий розбір · мікрозайми',date='05.11.2026',giant='ФОРУМ',pl=-70,pt=420,gl=(60,380),hs=140,lh=.98,bokeh=BOKEH2,obj=CHAT,
 headline='Користь<br><em>чи ризик?</em>',sub='Форум боржників по МФО: як не нашкодити собі',subtop=1372,
 co=[(72,596,196,'Користь','типові ситуації та підтримка'),(72,846,196,'Ризик','неперевірені поради, розголос даних')]),
'g4':dict(kicker='Правовий розбір · наслідки боргу',date='04.11.2026',giant='БОРГИ',pl=-55,pt=420,gl=(40,380),hs=140,lh=.98,bokeh=BOKEH2,obj=BADGE,
 headline='Чи можуть<br><mark>посадити?</mark>',sub='За борги в Україні · пояснення юриста',subtop=1372,
 co=[(72,596,226,'Борг — не злочин','лише цивільна відповідальність'),(72,846,214,'Наслідки','позов, арешт майна, обмеження виїзду'),(776,826,232,'За сам борг','позбавлення волі закон не передбачає')]),
'g5':dict(kicker='Правовий розбір · наслідки боргу',date='02.11.2026',giant='КРЕДИТ',pl=40,pt=472,gl=(300,380),hs=104,lh=1.04,bokeh=BOKEH1,
 headline='Що буде за<br><mark>прострочення?</mark>',sub='Наслідки за законом і дії позичальника',subtop=1340,
 co=[(72,596,236,'Неустойка','пеня або штраф за договором'),(72,846,236,'Інфляція + 3%','індекс інфляції та річні за ст. 625 ЦК'),
     (822,640,186,'Весь залишок','банк може вимагати повернути його'),(822,886,186,'Суд','позов і виконавче провадження')]),
}
for k,c in covers.items(): open(k+'.html','w').write(page(c))
print('ok')
