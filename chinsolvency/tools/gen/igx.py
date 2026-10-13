# Image spec renderer: python3 igx.py spec.py  (spec defines IMGS = {filename: (kind, eyebrow, title, data, foot)})
import base64,sys,os,subprocess
H=os.path.dirname(os.path.abspath(__file__))
logo=base64.b64encode(open('/tmp/claude-0/-home-user-work/057d374e-6f74-511c-a2f4-1bfe9640b1d5/scratchpad/g3/logo.png','rb').read()).decode()
CSS='''*{box-sizing:border-box;margin:0;padding:0}body{width:1200px;height:675px;background:#FFFBF4;font-family:Inter,'Helvetica Neue',Arial,sans-serif;color:#3a0b0b;position:relative;overflow:hidden}
.hd{background:#380404;height:150px;padding:34px 48px 0}.ey{color:#d9a9a9;letter-spacing:.14em;font-size:15px;font-weight:600;text-transform:uppercase}
.hd h1{color:#fff;font-size:41px;font-weight:700;margin-top:10px;letter-spacing:-.01em}.logo{position:absolute;right:42px;top:24px;width:102px;height:102px;background:url(data:image/png;base64,LOGO)}
.bar{position:absolute;left:48px;top:146px;width:120px;height:4px;background:#c0262b}
.ft{position:absolute;left:48px;right:48px;bottom:22px;display:flex;justify-content:space-between;font-size:15px;color:#5e5348}.ft b{color:#8c1d24;font-size:16px}
.main{position:absolute;left:48px;right:48px;top:182px;bottom:64px}
.row{display:flex;gap:16px}.card{background:#fff;border:1px solid #eadfd2;border-radius:16px;padding:18px 18px}
.k{font-size:14px;color:#6b5f55;font-weight:600}.v{font-size:30px;font-weight:800;color:#8c1d24;margin-top:6px;line-height:1.1}.s{font-size:14px;color:#5e5348;margin-top:8px;line-height:1.35}
.dark{background:#380404;color:#fff;border-color:#380404}.dark .k{color:#e5b8b8}.dark .v{color:#fff}.dark .s{color:#f0d6d6}
.n{display:inline-flex;width:34px;height:34px;border-radius:50%;background:#8c1d24;color:#fff;font-weight:700;align-items:center;justify-content:center;font-size:17px;margin-bottom:10px}
table{border-collapse:collapse;width:100%}td,th{padding:13px 16px;text-align:left;font-size:18px;border-bottom:1px solid #eadfd2}th{font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:#6b5f55}td.r{font-weight:800;color:#8c1d24}
'''.replace('LOGO',logo)
def page(ey,title,body,foot): return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="hd"><div class="ey">{ey}</div><h1>{title}</h1></div><div class="logo"></div><div class="bar"></div><div class="main">{body}</div><div class="ft"><span>{foot}</span><b>consultarius</b></div></body></html>'
def steps(items,banner=None):
    o='<div class="row">'
    for i,(k,v,s) in enumerate(items,1): o+=f'<div class="card" style="flex:1"><div class="n">{i}</div><div class="k" style="font-size:19px;color:#380404;font-weight:700">{k}</div><div class="v" style="font-size:22px">{v}</div><div class="s">{s}</div></div>'
    o+='</div>'
    if banner: o+=f'<div class="card dark" style="margin-top:22px"><div class="s" style="font-size:18px;margin:0">{banner}</div></div>'
    return o
def cards(items,per=3):
    o=''
    for i in range(0,len(items),per):
        o+='<div class="row" style="margin-top:%dpx">'%(0 if i==0 else 16)
        for k,v,s,d in items[i:i+per]: o+=f'<div class="card{" dark" if d else ""}" style="flex:1"><div class="k">{k}</div><div class="v">{v}</div><div class="s">{s}</div></div>'
        o+='</div>'
    return o
def table(head,rows):
    o='<table><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr>'
    for r in rows: o+='<tr>'+''.join(f'<td class="r">{c}</td>' if j>0 else f'<td>{c}</td>' for j,c in enumerate(r))+'</tr>'
    return o+'</table>'
def render(spec_file,outdir):
    ns={}; exec(open(spec_file).read(),{'steps':steps,'cards':cards,'table':table},ns)
    return render_d(ns['IMGS'],outdir)
def render_d(IMGS,outdir):
    ns={'IMGS':IMGS}
    os.makedirs(outdir,exist_ok=True)
    for name,(ey,title,body,foot) in ns['IMGS'].items(): open(f'{outdir}/{name}.html','w').write(page(ey,title,body,foot))
    shot=f'''import pw from '/opt/node22/lib/node_modules/playwright/index.js';import fs from 'fs';
const b=await pw.chromium.launch({{executablePath:'/opt/pw-browsers/chromium'}});const p=await b.newPage({{viewport:{{width:1200,height:675}}}});
for(const f of fs.readdirSync('{outdir}').filter(x=>x.endsWith('.html'))){{await p.goto('file://{os.path.abspath(outdir)}/'+f);await p.screenshot({{path:'{outdir}/'+f.replace('.html','.png')}});}}
await b.close();'''
    open(f'{outdir}/shot.mjs','w').write(shot); subprocess.run(['node',f'{outdir}/shot.mjs'],check=True)
    from PIL import Image
    for name in ns['IMGS']: Image.open(f'{outdir}/{name}.png').convert('RGB').save(f'{outdir}/{name}.webp',quality=85)
    print('ok',len(ns['IMGS']))
if __name__=='__main__': render(sys.argv[1],sys.argv[2])
