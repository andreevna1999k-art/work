CSS = """
@import url(fonts/all.css);
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
:root{--navy:#181A31;--navy2:#23264A;--gold:#C9A06A;--goldl:#F3E8D6;--bg:#F1F1F5;--mute:#5C5E76;--lav:#B9BBD2}
body{font-variant-ligatures:none;font-feature-settings:'liga' 0,'dlig' 0,'clig' 0,'calt' 0;position:relative;font-family:'Noto Sans',sans-serif;font-weight:600;color:#fff;background:#181A31;-webkit-font-smoothing:antialiased}
.abs{position:absolute}.pf{font-family:'Playfair Display',serif}
.full{left:0;top:0;width:1080px;height:1920px}
.bg{background:linear-gradient(165deg,#D2D4E6 0%,#AEB2D2 38%,#7D82AE 70%,#3B3F6E 100%)}
.grain{left:0;top:0;width:1080px;height:1920px;opacity:.2;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 1.4 -.15'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.mast{left:72px;top:262px;width:640px;height:250px;display:flex;align-items:flex-end}
.mast span{font-family:'Playfair Display',serif;font-weight:400;color:#181A31;line-height:.72;white-space:nowrap;display:inline-block}
.tagline{left:76px;top:526px;font-size:19px;letter-spacing:4px;text-transform:uppercase;color:#181A31;font-weight:700}
.vg{left:0;top:0;width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 32%,rgba(0,0,0,0) 40%,rgba(24,26,49,.45) 100%)}
.scrim{left:0;top:1040px;width:1080px;height:880px;background:linear-gradient(to bottom,rgba(24,26,49,0),rgba(24,26,49,.80) 12%,rgba(24,26,49,.96) 26%,rgba(20,22,41,.99) 100%)}
.tagb{display:inline-block;background:#fff;color:#181A31;font-weight:800;font-size:19px;letter-spacing:2.5px;padding:5px 12px;text-transform:uppercase}
.lb{left:72px;top:610px;width:290px}
.lb .i{font-weight:800;font-size:27px;line-height:1.06;text-transform:uppercase;color:#181A31;margin-top:13px}
.lb .r{width:130px;height:6px;background:#fff;margin-top:20px}
.hexw{left:722px;top:258px;width:290px;text-align:center}
.hexw .n{font-family:'Playfair Display',serif;font-weight:400;font-size:150px;line-height:.9;color:#181A31;margin-top:6px}
.hexw .l{font-weight:800;font-size:28px;letter-spacing:4px;text-transform:uppercase;color:#181A31;margin-top:6px}
.hexw .d{font-weight:600;font-size:22px;line-height:1.2;text-transform:uppercase;color:#181A31;margin-top:10px}
.rb{left:716px;top:770px;width:292px;text-align:center}
.rb .t{font-family:'Playfair Display',serif;font-weight:700;font-size:35px;line-height:1.05;text-transform:uppercase;color:#181A31}
.rb .p{font-size:22px;line-height:1.25;color:#181A31;margin-top:10px;text-transform:uppercase;font-weight:700;letter-spacing:.5px}
.bar{left:1062px;top:770px;width:18px;height:92px;background:#181A31}
.eb{left:72px;width:936px;top:1124px;text-align:center;font-family:'Playfair Display',serif;font-weight:400;font-size:46px;letter-spacing:11px;text-transform:uppercase;color:#fff}
.big{left:72px;width:936px;top:1186px;text-align:center}
.big span{font-family:'Playfair Display',serif;font-weight:400;text-transform:uppercase;color:#fff;line-height:.82;white-space:nowrap;display:inline-block;letter-spacing:-1px}
.sub{left:72px;width:936px;top:1396px;text-align:center;font-family:'Playfair Display',serif;font-weight:700;font-size:34px;letter-spacing:5px;text-transform:uppercase;color:#fff}
.sub2{left:72px;width:936px;top:1458px;text-align:center;font-size:23px;letter-spacing:3px;text-transform:uppercase;color:#C9A06A;font-weight:700}
.plate{left:72px;width:936px;top:1556px;height:84px;background:#C9A06A;color:#181A31;font-size:46px;font-weight:600;display:flex;align-items:center;justify-content:center}
.foot{left:72px;width:936px;top:1716px;border-top:2px solid rgba(201,160,106,.35);padding-top:18px;text-align:center;font-weight:600;font-size:22px;letter-spacing:5px;color:#B9BBD2}
"""
SCRIPT = """<script>document.fonts.ready.then(()=>{
const m=document.getElementById('m');m.style.fontSize='100px';const k=640/m.getBoundingClientRect().width;m.style.fontSize=Math.min(300,100*k)+'px';
const b=document.getElementById('b');b.style.fontSize='100px';const k2=936/b.getBoundingClientRect().width;b.style.fontSize=Math.min(230,100*k2)+'px';
})</script>"""
# portrait: image 1760x1080 (2x crop 880x540), face center x≈570, hair top y≈230 (in 1760 scale)
FX,HY=570,230
HEX='''<svg class="abs" style="left:730px;top:250px" width="278" height="240" viewBox="0 0 278 240"><polygon points="70,6 208,6 274,120 208,234 70,234 4,120" fill="#181A31" stroke="#C9A06A" stroke-width="3"/></svg>
<div class="abs pf" style="left:730px;top:250px;width:278px;height:240px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;text-transform:uppercase;color:#fff;font-weight:400;font-size:32px;line-height:1.1;letter-spacing:1px">Прострочка<br><span style="font-size:24px;letter-spacing:5px;color:#C9A06A;font-weight:400">по кредиту</span></div>'''
def page(c):
    k=c['k']; left=540+c.get('shift',0)-FX*k; top=c.get('hair',480)-HY*k
    return f"""<!doctype html><html lang="uk"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="abs full bg"></div>
<div class="abs" style="left:60px;top:300px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.55),rgba(255,255,255,0) 66%)"></div>
<div class="abs mast"><span id="m">{c['mast']}</span></div>
<div class="abs tagline">{c['tagline']}</div>
<img class="abs" src="ya_cut.png" style="left:{left}px;top:{top}px;width:{1760*k}px;height:{1080*k}px;filter:drop-shadow(0 8px 26px rgba(24,26,49,.35)) contrast(1.04)">
<div class="abs vg"></div>
{HEX}
<div class="abs hexw" style="top:500px"><div class="n">{c['num']}</div><div class="l">{c['numl']}</div><div class="d">{c['numd']}</div></div>
<div class="abs lb"><span class="tagb">{c['ltag']}</span>{''.join(f'<div class="i">{t}</div>' for t in c['litems'])}<div class="r"></div></div>
<div class="abs scrim"></div>
<div class="abs eb">{c['eb']}</div>
<div class="abs big"><span id="b">{c['big']}</span></div>
<div class="abs sub">{c['sub']}</div>
<div class="abs sub2">{c['sub2']}</div>
<div class="abs plate">Читайте мою нову статтю</div>
<div class="abs foot">urists.com.ua</div>
<div class="abs grain"></div>
{SCRIPT}</body></html>"""
covers={'y1':dict(k=.90,mast='КРЕДИТ',tagline='Київ · кредитні спори',
 num='5',numl='етапів',numd='від SMS до виконавчого провадження',
 ltag='Важливо',litems=['Не ховайтеся від кредитора','Зверніться письмово до банку чи МФО','Попросіть розрахунок боргу'],
 rt='Закон ставить межі нарахувань',rp='ст. 625 ч. 2 Цивільного кодексу',
 eb='Прострочка по кредиту:',big='Що робити?',sub='Поради юриста Дмитра Яковенка',sub2='Розрахунок боргу · письмова заява · ст. 625 ЦК')}
for n,c in covers.items(): open(n+'.html','w').write(page(c))
print('ok')
