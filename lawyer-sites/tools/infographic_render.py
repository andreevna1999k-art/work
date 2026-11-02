import os, sys, json, subprocess, html
QUAL=int(os.environ.get('Q','55'))
THEMES = {
 'khaki':  dict(bg='#F5F3EC', head='#0D1017', accent='#7E7038', accent2='#A89B6B', card='#FFFFFF', line='#E3DDC7', headtxt='#FFFFFF', eyebrow='#C9BC8A', muted='#5E5A48', dark='#0D1017'),
 'mahogany': dict(bg='#F5EEE4', head='#2B1711', accent='#6E1423', accent2='#D4B27A', card='#FFFFFF', line='#E6D6BE', headtxt='#F4E6D0', eyebrow='#D4B27A', muted='#6A5646', dark='#2B1711'),
 'navy':   dict(bg='#F1F1F5', head='#181A31', accent='#8A6128', accent2='#C9A06A', card='#FFFFFF', line='#DEDFE8', headtxt='#FFFFFF', eyebrow='#C9A06A', muted='#5C5E76', dark='#181A31'),
 'olive':  dict(bg='#F5F0E3', head='#1C2430', accent='#6B5F26', accent2='#CDC28F', card='#FFFFFF', line='#E4DDC4', headtxt='#F5F0E3', eyebrow='#CDC28F', muted='#58554A', dark='#1C2430'),
 'blue':   dict(bg='#EEF3FB', head='#12305F', accent='#1F5FBF', accent2='#7FA8E8', card='#FFFFFF', line='#D5E0F2', headtxt='#FFFFFF', eyebrow='#9DBDF0', muted='#51607A', dark='#12305F'),
}
def esc(x): return html.escape(x)
def body_steps(items, t):
    n=len(items); o='<div class="row">'
    for i,(k,s) in enumerate(items,1):
        o+=f'<div class="card" style="flex:1"><div class="n">{i}</div><div class="k">{esc(k)}</div><div class="s">{esc(s)}</div></div>'
    return o+'</div>'
def body_compare(cols, rows, t):
    # cols: [left title, right title]; rows: [(label,left,right)]
    o='<div class="cmp"><div class="ch" style="background:transparent"></div><div class="ch l">'+esc(cols[0])+'</div><div class="ch r">'+esc(cols[1])+'</div>'
    for lab,a,b in rows:
        o+=f'<div class="lab">{esc(lab)}</div><div class="cell">{esc(a)}</div><div class="cell">{esc(b)}</div>'
    return o+'</div>'
def body_timeline(items, t):
    n=len(items); o='<div class="tl"><div class="tline"></div>'
    for i,(k,s) in enumerate(items,1):
        o+=f'<div class="tp"><div class="dot">{i}</div><div class="tcard"><div class="k">{esc(k)}</div><div class="s">{esc(s)}</div></div></div>'
    return o+'</div>'
def page(spec, t, foot):
    kind=spec['kind']
    body={'steps':lambda:body_steps(spec['items'],t),'compare':lambda:body_compare(spec['cols'],spec['rows'],t),'timeline':lambda:body_timeline(spec['items'],t)}[kind]()
    css=f'''*{{box-sizing:border-box;margin:0;padding:0}}body{{width:1200px;height:675px;background:{t['bg']};font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;color:{t['dark']};position:relative;overflow:hidden}}
.hd{{background:{t['head']};height:176px;padding:30px 52px 0;position:relative}}.ey{{color:{t['eyebrow']};letter-spacing:.12em;font-size:15px;font-weight:700;text-transform:uppercase}}
.hd h1{{color:{t['headtxt']};font-size:33px;font-weight:700;margin-top:10px;line-height:1.2;max-width:1090px}}.bar{{position:absolute;left:52px;top:172px;width:130px;height:5px;background:{t['accent2']}}}
.main{{position:absolute;left:52px;right:52px;top:208px;bottom:70px}}.note{{position:absolute;left:52px;right:52px;bottom:62px;background:{t['accent']};color:#fff;border-radius:14px;padding:14px 22px;font-size:19px;font-weight:700}}.ft{{position:absolute;left:52px;right:52px;bottom:24px;font-size:14px;color:{t['muted']}}}
.row{{display:flex;gap:14px;height:100%}}.card{{background:{t['card']};border:1px solid {t['line']};border-radius:16px;padding:20px 18px}}
.n{{display:flex;width:38px;height:38px;border-radius:50%;background:{t['accent']};color:#fff;font-weight:700;align-items:center;justify-content:center;font-size:19px;margin-bottom:14px}}
.k{{font-size:21px;font-weight:700;line-height:1.2;color:{t['dark']}}}.s{{font-size:16px;color:{t['muted']};margin-top:10px;line-height:1.4}}
.cmp{{display:grid;grid-template-columns:190px 1fr 1fr;gap:12px 12px;height:100%;align-content:start}}.ch{{font-weight:700;font-size:21px;padding:12px 16px;border-radius:12px;color:#fff;background:{t['accent']}}}.ch.r{{background:{t['head']}}}.ch.l{{background:{t['accent']}}}
.lab{{font-size:15px;font-weight:700;color:{t['muted']};padding:0 4px;display:flex;align-items:center;text-transform:uppercase;letter-spacing:.04em}}.cell{{background:{t['card']};border:1px solid {t['line']};border-radius:12px;padding:12px 18px;font-size:20px;line-height:1.25;min-height:70px;display:flex;align-items:center}}
.tl{{position:relative;display:flex;gap:10px;height:100%;align-items:flex-start;padding-top:10px}}.tline{{position:absolute;left:30px;right:30px;top:40px;height:4px;background:{t['accent2']}}}
.tp{{flex:1;position:relative;padding-top:0}}.dot{{width:60px;height:60px;border-radius:50%;background:{t['accent']};color:#fff;font-weight:700;font-size:26px;display:flex;align-items:center;justify-content:center;border:5px solid {t['bg']};position:relative}}
.tp .k{{margin-top:0;font-size:23px}}.tp .s{{font-size:19px}}.tcard{{background:{t['card']};border:1px solid {t['line']};border-radius:16px;padding:18px 16px;margin-top:16px;height:250px}}'''
    return f'<html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="hd"><div class="ey">{esc(spec["eyebrow"])}</div><h1>{esc(spec["title"])}</h1></div><div class="bar"></div><div class="main">{body}</div>{('<div class="note">'+esc(spec['note'])+'</div>') if spec.get('note') else ''}<div class="ft">{esc(foot)}</div></body></html>'
def render(specs, theme, outdir, foot):
    t=THEMES[theme]; os.makedirs(outdir,exist_ok=True)
    for name,spec in specs.items():
        open(f'{outdir}/{name}.html','w').write(page(spec,t,spec.get('foot',foot)))
    shot=f'''import pw from '/opt/node22/lib/node_modules/playwright/index.js';import fs from 'fs';
const b=await pw.chromium.launch({{executablePath:'/opt/pw-browsers/chromium'}});const p=await b.newPage({{viewport:{{width:1200,height:675}}}});
for(const f of fs.readdirSync('{outdir}').filter(x=>x.endsWith('.html'))){{await p.goto('file://{os.path.abspath(outdir)}/'+f);await p.screenshot({{path:'{outdir}/'+f.replace('.html','.png')}});}}
await b.close();'''
    open(f'{outdir}/shot.mjs','w').write(shot); subprocess.run(['node',f'{outdir}/shot.mjs'],check=True)
    from PIL import Image
    for name in specs:
        im=Image.open(f'{outdir}/{name}.png').convert('RGB'); im.quantize(colors=16,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).convert('RGB').save(f'{outdir}/{name}.webp',lossless=True,method=6)
        print(name, os.path.getsize(f'{outdir}/{name}.webp'))
if __name__=='__main__':
    spec=json.load(open(sys.argv[1])); render(spec['specs'],spec['theme'],sys.argv[2],spec['foot'])
