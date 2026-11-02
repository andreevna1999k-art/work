#!/usr/bin/env python3
"""Генерує 12 обложок 1200x750 (PNG→WebP) у стилі сайту: темно-коричневий фон, золоті лінійні піктограми."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import ARTICLES
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, 'covers')
from covers_scenes import svg
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
