#!/usr/bin/env python3
"""advokato.in.ua: ЧЕРНЕТКИ головної (id 1824), хабу «Мої статті» (id 1818) та копій 3 опублікованих сторінок із шапкою .kvh.
Нічого не публікує і не чіпає живі сторінки.
  python3 build_site.py            -> payload/, preview/
  python3 build_site.py --push     -> оновлює чернетки 1824, 1818 та створює/оновлює копії (ids у ids.json)
"""
import json, re, sys, pathlib, subprocess, html, base64, io
from PIL import Image
R = pathlib.Path(__file__).parent
B = R.parent / "blog-drafts"
SITE = "https://advokato.in.ua"; HUB = 1818
HOME = (json.load(open(pathlib.Path(__file__).parent / "ids.json")).get("home") if (pathlib.Path(__file__).parent / "ids.json").exists() else None) or 1824
sys.path.insert(0, str(B))
import build_drafts as bd

CSS_ART = bd.CSS_ART
CSS = bd.CSS_HUB
HDR_T = bd.HDR
def hdr(cur=None):
    h = HDR_T.replace(' class="cur"', '')
    # меню: усі пункти ведуть на головну/сторінки; «Блог» -> /blog/
    h = h.replace('<a href="/#about">Освіта</a><a href="/#experience">Досвід</a><a href="/#results">Результати</a><a href="/#reviews">Відгуки</a><a href="/blog/">Блог</a><a href="/#contacts">Контакти</a>',
                  '<a href="/#about">Освіта</a><a href="/#experience">Досвід</a><a href="/#results">Результати</a><a href="/#articles">Статті</a><a href="/#reviews">Відгуки</a><a href="/#contacts">Контакти</a>')
    if cur == "blog": h = h.replace('<a href="/#articles">Статті</a>', '<a href="/blog/" class="cur">Блог</a>')
    elif cur == "home": pass
    else: h = h.replace('<a href="/#articles">Статті</a>', '<a href="/blog/">Блог</a>')
    return h
FTR = bd.FTR

CSS_SITE = """<style>
.kv .hero{padding:140px 0 90px}.kv .hero .sub{font-size:19px}
.kv .sec h2{margin-bottom:0}
.kv .sec.edu{background:var(--slate)}.kv .sec.edu p{max-width:900px;margin:30px auto 0;text-align:center;font-size:15.5px}
.kv .sec.exp{background:var(--slate2)}
.kv .exp .w{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.kv .exp h2{text-align:left}.kv .exp .bar{margin-left:0}
.kv .exp .box{margin-top:30px;background:var(--rose);padding:34px 36px;color:#fff;font-size:15.5px}
.kv .exp .box p{margin:0 0 14px}.kv .exp .box strong{color:#fff}.kv .exp .box a{color:#fff;border-bottom:1px solid #fff}
.kv .exp .btn{margin-top:26px}
.kv .exp .ph img{width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;display:block;box-shadow:0 24px 50px rgba(0,0,0,.35)}
.kv .sec.res{background:var(--slate)}
.kv .res-row{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;padding:34px 4px 18px;margin-top:10px}
.kv .res-row a{flex:0 0 auto;scroll-snap-align:start;background:#fff;padding:8px;border-radius:6px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
.kv .res-row img{display:block;height:340px;width:auto}
.kv .res-row::-webkit-scrollbar{height:8px}.kv .res-row::-webkit-scrollbar-thumb{background:rgba(255,255,255,.4);border-radius:4px}
.kv .cen{text-align:center;margin-top:34px}
.kv .sec.arts{background:var(--slate2)}
.kv .bl-empty{grid-column:1/-1;text-align:center;color:#fff;padding:30px 10px;font-size:18px}
.kv .sec.rev{background:var(--slate)}.kv .rev-box{max-width:760px;margin:36px auto 0}
.kv .hero + .sec,.kv .hero{scroll-margin-top:80px}
.kv section[id]{scroll-margin-top:68px}
@media(max-width:900px){.kv .exp .w{grid-template-columns:1fr;gap:34px}.kv .res-row img{height:280px}}
</style>"""

def pidcss(pid):
    return (f"<style>body.page-id-{pid} .entry-header,body.page-id-{pid} .ast-breadcrumbs-wrapper,body.page-id-{pid} .entry-title,body.page-id-{pid} .site-footer,body.page-id-{pid} #masthead,body.page-id-{pid} .ast-above-header-wrap,body.page-id-{pid} .site-header{{display:none!important}}"
            f"body.page-id-{pid} .ast-container,body.page-id-{pid} #primary,body.page-id-{pid} .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}body.page-id-{pid}{{background:#615C68}}</style>")

# ---------- дані статей (для fallback у чернетці) ----------
idx = json.load(open(B / "src/index.json"))
ids_art = json.load(open(B / "draft-ids.json"))
def thumb(n):
    im = Image.open(B / "img" / f"{n:02d}.webp").convert("RGB").resize((640, 427))
    b = io.BytesIO(); im.save(b, "WEBP", quality=70, method=6)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()
def art_meta():
    M = {}
    for i, url, _ in idx:
        p = json.load(open(B / "payload" / f"{i:02d}-{url}.json"))
        M[url] = {"t": bd.TAGS[i-1], "i": thumb(i), "h": p["title"], "d": bd.DATES[i-1], "e": p["excerpt"]}
    return M

JS = r'''(function(){var A=String.fromCharCode(38);var g=document.getElementById("%(gid)s");if(!g)return;var M=%(M)s;var LIM=%(lim)d,PID=%(hub)d;
function T(s){var d=document.createElement("div");d.innerHTML=s;return(d.textContent||"").replace(/\s+/g," ").trim()}
function D(s){var p=String(s).slice(0,10).split("-");return p[2]+"."+p[1]+"."+p[0]}
function E(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
function card(u,slug,ti,dt,ex){var m=M[slug]||{t:"Стаття"};var art=E("article","bl-card"),cv=E("a","bl-cover");cv.href=u;cv.tabIndex=-1;
if(m.i){var im=new Image();im.src=m.i;im.alt=ti;im.width=640;im.height=427;im.loading="lazy";cv.appendChild(im)}
cv.appendChild(E("span","bl-tag",m.t));art.appendChild(cv);var b=E("div","bl-body"),tm=E("time",null,D(dt));tm.setAttribute("datetime",String(dt).slice(0,10));b.appendChild(tm);
var h=E("h3"),l=E("a",null,ti);l.href=u;l.style.color="inherit";h.appendChild(l);b.appendChild(h);b.appendChild(E("p",null,ex));var mr=E("a","bl-more","Читати статтю");mr.href=u;b.appendChild(mr);art.appendChild(b);g.appendChild(art)}
function fallback(){Object.keys(M).sort(function(a,b){return M[b].d.localeCompare(M[a].d)}).slice(0,LIM).forEach(function(s){card("/blog/"+s+"/",s,M[s].h,M[s].d,M[s].e)})}
fetch("/wp-json/wp/v2/pages?parent="+PID+A+"per_page=100"+A+"orderby=date"+A+"order=desc"+A+"_fields=id,date,link,slug,title,excerpt",{credentials:"omit"}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(a){
if(!a.length){fallback();return}a.slice(0,LIM).forEach(function(x){card(new URL(x.link,location.href).pathname,x.slug,T(x.title.rendered),x.date,T((x.excerpt?x.excerpt.rendered:"")||""))})}).catch(fallback)})();'''
def blog_js(gid, lim, M):
    return "<script>" + JS % dict(gid=gid, M=json.dumps(M, ensure_ascii=False, separators=(",", ":")).replace("&","\\u0026").replace("<","\\u003c").replace(">","\\u003e"), lim=lim, hub=HUB) + "</script>"

def wrap(pid, cur, inner, extra=""):
    return ("<!-- wp:html -->\n" + CSS + "\n" + CSS_ART + "\n" + CSS_SITE + "\n" + pidcss(pid) + "\n" + extra + hdr(cur) + '<div class="kv">' + inner + FTR + "</div>\n<!-- /wp:html -->")

# ---------- хаб ----------
def hub_page(M):
    inner = ('<section class="sec pre" id="articles"><div class="w"><h2>Мої статті</h2><span class="bar"></span>'
             '<p class="lead2">Пояснюю питання банкрутства фізичних осіб, боргів і захисту від колекторів простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>'
             '<div class="bl-g" id="blogGrid"></div>' + blog_js("blogGrid", 100, M) + '</div></section>')
    return wrap(HUB, "blog", inner)

# ---------- головна ----------
src = json.load(open(R / "adv_1824.json"))
raw = src["content"]["raw"]
def between(a, b): i = raw.index(a) + len(a); return raw[i:raw.index(b, i)]
EDU = re.search(r'<h2>Освіта</h2>\s*(<p>.*?</p>)', raw, re.S).group(1)
EXP = re.search(r'<h3>Досвід роботи</h3>\s*(.*?)\s*<a href="https://t.me', raw, re.S).group(1)
EXP = re.sub(r'\s+', ' ', EXP)
DOCS = re.findall(r'href="(https://advokato\.in\.ua/wp-content/uploads/2025/07/doc[^"]+)"><figure><img src="([^"]+)"', raw)
PH1 = "https://advokato.in.ua/wp-content/uploads/2025/07/kovalenko-nataliia-oleksandrivna-yuryst-po-kredytam.jpg"
PH2 = "https://advokato.in.ua/wp-content/uploads/2025/07/kovalenko-nataliia-kredytnyi-yuryst.jpg"
TG = "https://t.me/yrist_kovalenko"

def home_page(M):
    res = "".join(f'<a href="{a}" target="_blank" rel="noopener"><img src="{b}" alt="Результат роботи — документ" loading="lazy"></a>' for a, b in DOCS)
    inner = (
     '<header class="hero" id="top"><div class="w"><div><h1>Коваленко Наталія Олександрівна</h1><p class="sub">Юрист з питань<br>банкрутства фізичних осіб</p>'
     f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div>'
     f'<div class="ph"><img src="{PH1}" alt="Коваленко Наталія Олександрівна - юрист по кредитам" width="640" height="640"></div></div></header>'
     f'<section class="sec edu pre" id="about"><div class="w"><h2>Освіта</h2><span class="bar"></span>{EDU}</div></section>'
     f'<section class="sec exp" id="experience"><div class="w"><div><h2>Досвід роботи</h2><span class="bar"></span><div class="box">{EXP}</div>'
     f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div>'
     f'<div class="ph"><img src="{PH2}" alt="Коваленко Наталія Олександрівна - юрист по кредитам" width="640" height="640" loading="lazy"></div></div></section>'
     f'<section class="sec res" id="results"><div class="w"><h2>Результати роботи</h2><span class="bar"></span><div class="res-row">{res}</div>'
     f'<p class="cen"><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></p></div></section>'
     '<section class="sec arts" id="articles"><div class="w"><h2>Мої статті</h2><span class="bar"></span>'
     '<p class="lead2">Пояснюю питання банкрутства фізичних осіб, боргів і захисту від колекторів простою мовою: що каже закон і що варто зробити в першу чергу.</p>'
     '<div class="bl-g" id="homeBlog"></div>' + blog_js("homeBlog", 3, M) +
     '<p class="cen"><a class="btn" href="/blog/">Усі статті</a></p></div></section>'
     '<section class="sec rev" id="reviews"><div class="w"><h2>Відгуки</h2><span class="bar"></span><div class="rev-box">[react_reviews_1]</div></div></section>')
    return wrap(HOME, "home", inner)

# ---------- копії опублікованих сторінок ----------
def convert(n):
    d = json.load(open(R / f"p{n}.json")); c = d["content"]["rendered"]
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', c, re.S); h1 = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else d["title"]["rendered"]
    c = re.sub(r'<h1[^>]*>.*?</h1>', '', c, flags=re.S)
    c = re.sub(r'<(script|style)\b.*?</\1>', '', c, flags=re.S)
    c = re.sub(r'<h4[^>]*>.*?</h4>', '', c, flags=re.S)          # підзаголовок «Юрист з питань…» у hero
    c = re.sub(r'<a\b[^>]*href="https://t\.me/[^"]*"[^>]*>\s*(?:<span[^>]*>.*?</span>\s*)*Безкоштовна консультація\s*</a>', '', c, flags=re.S)
    c = re.sub(r'</?div\b[^>]*>', '', c)
    c = re.sub(r'<(/?)(h[2-6]|p|ul|ol|li|table|thead|tbody|tr|th|td|strong|em|b|i|br|blockquote)\b[^>]*>', lambda m: f'<{m.group(1)}{m.group(2)}>', c)
    c = re.sub(r'<a\b([^>]*)>', lambda m: '<a href="%s">' % (re.search(r'href="([^"]*)"', m.group(1)).group(1) if 'href=' in m.group(1) else '#'), c)
    c = re.sub(r'<img\b[^>]*?src="([^"]+)"[^>]*?(?:alt="([^"]*)")?[^>]*>', lambda m: f'<figure class="art-fig"><img src="{m.group(1)}" alt="{m.group(2) or ""}" loading="lazy"></figure>', c)
    c = re.sub(r'<a href="[^"]*">\s*Безкоштовна консультація\s*</a>', '', c)
    c = re.sub(r'<p>\s*</p>', '', c); c = re.sub(r'\n\s*\n+', '\n', c).strip()
    c = re.sub(r'<table>.*?</table>', lambda m: '<div class="art-table">' + m.group(0) + '</div>', c, flags=re.S)
    return d, h1, c

def copy_page(n, pid):
    d, h1, body = convert(n)
    inner = ('<header class="ahero"><div class="w"><p class="crumbs"><a href="/">Головна</a> / ' + re.sub(r'<[^>]+>', '', h1)[:60] + '</p>'
             f'<h1>{h1}</h1><span class="bar"></span></div></header>'
             f'<section class="art-sec"><div class="w"><article class="art-card"><div class="art-body">{body}</div><p class="art-back"><a href="/">← На головну</a></p></article></div></section>'
             '<section class="cta-band"><div class="w"><h2>Потрібна консультація юриста?</h2><p>Опишіть ситуацію в Telegram: підкажу перші кроки та скажу, чи потрібне представництво.</p>'
             f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div></section>')
    return {"title": d["title"]["rendered"] + " (копія з шапкою)", "slug": d["slug"] + "-shapka", "status": "draft", "template": "elementor_canvas",
            "content": wrap(pid, None, inner)}, h1

def call(method, url, data=None):
    cmd = ["curl", "-s", "-m", "120", "-X", method, "-H", "Content-Type: application/json", url]
    if data is not None: cmd += ["--data-binary", "@-"]
    r = subprocess.run(cmd, input=(json.dumps(data, ensure_ascii=False).encode() if data is not None else None), capture_output=True)
    return json.loads(r.stdout.decode())

if __name__ == "__main__":
    (R / "payload").mkdir(exist_ok=True); (R / "preview").mkdir(exist_ok=True)
    M = art_meta()
    idf = R / "ids.json"; ids = json.load(open(idf)) if idf.exists() else {}
    jobs = {"home": (HOME, {"title": "Головна (макет з шапкою і блоком Мої статті)", "status": "draft", "template": "elementor_canvas", "content": home_page(M)}),
            "hub": (HUB, {"title": "Мої статті", "status": "draft", "template": "elementor_canvas", "content": hub_page(M)})}
    for n in (1222, 1710, 1735):
        pid = ids.get(f"copy{n}")
        p, h1 = copy_page(n, pid or 0); jobs[f"copy{n}"] = (pid, p)
    for k, (pid, p) in jobs.items():
        (R / "payload" / f"{k}.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        (R / "preview" / f"{k}.html").write_text(p["content"], encoding="utf-8")
        print(k, pid, len(p["content"]))
        if "--push" in sys.argv:
            if k.startswith("copy") and not pid:
                r = call("POST", f"{SITE}/wp-json/wp/v2/pages", p)
                if "id" not in r: print("  ERR", str(r)[:300]); continue
                ids[k] = pid = r["id"]; json.dump(ids, open(idf, "w"), indent=1)
                n = int(k[4:]); p, _ = copy_page(n, pid)
            r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", {"content": p["content"]})
            print("  ->", r.get("id"), r.get("status"), r.get("link"), str(r.get("code", ""))[:60])
