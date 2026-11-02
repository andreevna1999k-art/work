#!/usr/bin/env python3
"""Генерує 12 обложок 1200x750 (PNG→WebP) у стилі сайту: темно-коричневий фон, золоті лінійні піктограми."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import ARTICLES
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, 'covers')
# піктограми в рамці 100x100 (лінійні)
ICONS = {
 1: '<circle cx="50" cy="50" r="34"/><path d="M50 26v26l17 10"/>',                                   # годинник
 2: '<rect x="26" y="44" width="48" height="36" rx="5"/><path d="M34 44V32a16 16 0 0 1 32 0v12"/><path d="M50 58v10"/>',  # замок
 3: '<path d="M30 14h30l16 16v56H30z"/><path d="M60 14v16h16"/><path d="M40 58l8 8 14-16"/>',        # документ з галочкою
 4: '<path d="M30 20h14l6 16-9 6a42 42 0 0 0 17 17l6-9 16 6v14a8 8 0 0 1-8 8C45 78 22 55 22 28a8 8 0 0 1 8-8z"/>', # телефон
 5: '<rect x="14" y="26" width="72" height="48" rx="7"/><path d="M14 42h72"/><path d="M24 62h18"/>',   # картка
 6: '<path d="M22 28l22 22 14-14 22 24"/><path d="M62 60h18V42"/>',                                    # стрілка вниз
 7: '<path d="M30 16h40M30 84h40"/><path d="M34 16c0 22 32 22 32 34S34 62 34 84M66 16c0 22-32 22-32 34s32 12 32 34"/>', # пісочний годинник
 8: '<path d="M50 18v62M30 80h40"/><path d="M22 30h56"/><path d="M22 30l-10 22a12 8 0 0 0 20 0zM78 30l-10 22a12 8 0 0 0 20 0z"/>', # терези
 9: '<ellipse cx="42" cy="34" rx="26" ry="10"/><path d="M16 34v14c0 6 12 10 26 10s26-4 26-10V34"/><path d="M16 48v14c0 6 12 10 26 10"/><ellipse cx="68" cy="62" rx="18" ry="8"/><path d="M50 62v10c0 5 8 8 18 8s18-3 18-8V62"/>', # монети
 10: '<path d="M50 12l32 12v24c0 20-14 34-32 40-18-6-32-20-32-40V24z"/><path d="M36 50l10 10 18-20"/>', # щит
 11: '<circle cx="34" cy="32" r="12"/><circle cx="68" cy="36" r="10"/><path d="M12 80c0-16 10-26 22-26s22 10 22 26"/><path d="M56 80c0-12 6-20 14-20s14 8 14 20"/>', # люди
 12: '<path d="M12 48L50 16l38 32"/><path d="M22 42v42h56V42"/><path d="M42 84V60h16v24"/>',           # будинок
}
def svg(n):
    ic = ICONS[n]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="750" viewBox="0 0 1200 750">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5C2B1D"/><stop offset="1" stop-color="#2B1711"/></linearGradient>
<radialGradient id="r" cx=".78" cy=".42" r=".55"><stop offset="0" stop-color="#D4B27A" stop-opacity=".30"/><stop offset="1" stop-color="#D4B27A" stop-opacity="0"/></radialGradient></defs>
<rect width="1200" height="750" fill="url(#g)"/><rect width="1200" height="750" fill="url(#r)"/>
<g fill="none" stroke="#D4B27A" stroke-opacity=".16" stroke-width="2"><circle cx="880" cy="330" r="330"/><circle cx="880" cy="330" r="250"/><circle cx="880" cy="330" r="170"/></g>
<g transform="translate(880 330) scale(3.4) translate(-50 -50)" fill="none" stroke="#D4B27A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{ic}</g>
<rect x="80" y="610" width="130" height="5" rx="2.5" fill="#D4B27A"/>
</svg>'''
html = lambda n: f'<!doctype html><body style="margin:0;background:#000">{svg(n)}</body>'
if __name__ == '__main__':
    # 1) SVG -> covers/*.svg ; 2) node/playwright render -> png ; 3) PIL -> webp
    import json
    os.makedirs(OUT, exist_ok=True)
    for a in ARTICLES: open(os.path.join(OUT, a[2]+'.svg'), 'w', encoding='utf-8').write(svg(a[0]))
    js = """const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:750}});
for(const f of fs.readdirSync(process.argv[2]).filter(x=>x.endsWith('.svg'))){await p.setContent('<body style="margin:0">'+fs.readFileSync(process.argv[2]+'/'+f,'utf8')+'</body>');await p.screenshot({path:process.argv[2]+'/'+f.replace('.svg','.png')});}
await b.close()})();"""
    jsf = os.path.join(os.environ.get('TMPDIR','/tmp'), 'render_covers.js'); open(jsf,'w').write(js)
    root = subprocess.check_output(['npm','root','-g']).decode().strip()
    subprocess.check_call(['node', jsf, OUT], env=dict(os.environ, NODE_PATH=root))
    from PIL import Image
    for a in ARTICLES:
        png = os.path.join(OUT, a[2]+'.png')
        Image.open(png).convert('RGB').save(os.path.join(OUT, a[2]+'.webp'), quality=82); os.remove(png)
    print('covers:', len([x for x in os.listdir(OUT) if x.endswith('.webp')]))
