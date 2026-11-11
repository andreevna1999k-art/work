#!/usr/bin/env python3
"""bankruptcyukraine.com (Бондар О. О.): ЧЕРНЕТКИ статей блогу 1-12 + хаб «Мої статті» (id 1397) у стилі сайту (navy #02176D / жовтий #FFE16A / блакитний #E4F7FC, Montserrat + Roboto Condensed).
  python3 build_drafts.py            -> payload/, preview/ (нічого не публікує)
  python3 build_drafts.py --create   -> створює/оновлює ЧЕРНЕТКИ (status=draft, parent=1397, template elementor_canvas); ids у draft-ids.json
Статті 1-4 мають повний текст; 5-12 -- заглушки з робочою назвою (текст з'явиться пізніше). Публікація лише за командою.
"""
import json, re, sys, pathlib, subprocess, html, base64, io
R = pathlib.Path(__file__).parent
SITE = "https://bankruptcyukraine.com"
HUB_ID = 1397
AUTHOR = "Бондар Олег Олексійович"
TG = "https://t.me/Oleg_adwokat"
DATES = ["2026-11-11","2026-11-12","2026-11-13","2026-11-16","2026-11-18","2026-11-20","2026-11-23","2026-11-25","2026-11-27","2026-11-30","2026-12-02","2026-12-04"]
TAGS = ["Кредитні картки","Списання боргів","Списання боргів","МФО","МФО","Пенсіонери","Списання боргів","МФО","Кредитні борги","Мікрозайми","Списання боргів","Списання боргів"]
STUB = {5,6,7,8,9,10,11,12}
CSS_HUB = (R / "hub-css.html").read_text(encoding="utf-8")
HDR = (R / "hub-header.html").read_text(encoding="utf-8")
FTR = (R / "hub-footer.html").read_text(encoding="utf-8")
CSS_ART = """<style>
.kv .ahero{background:#02176D;padding:140px 0 70px;color:#fff}
.kv .ahero .crumbs{font:700 12px/1 'Roboto Condensed',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.75)}
.kv .ahero .crumbs a{color:#fff;border-bottom:1px solid rgba(255,255,255,.45)}
.kv .ahero h1{font-size:clamp(28px,4vw,46px);margin-top:20px;max-width:1000px;color:#fff}
.kv .ahero .bar{background:#FFE16A}
.kv .art-sec{background:#E4F7FC;padding:0 0 80px}
.kv .art-card{position:relative;max-width:900px;margin:-30px auto 0;background:#fff;border-radius:6px;padding:44px 52px 48px;color:#2A2E38;box-shadow:0 14px 40px rgba(2,23,109,.14)}
.kv .art-meta{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-bottom:26px;font:700 13px/1 'Roboto Condensed',sans-serif;letter-spacing:.06em;color:#4B4F58}
.kv .art-tag{padding:6px 14px;background:#FFE16A;color:#02176D;font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.kv .art-meta time{color:#02176D}
.kv .art-body{font-size:18px;line-height:1.7;color:#2A2E38}
.kv .art-body p{margin:0 0 16px}
.kv .art-body h2{font-size:clamp(23px,2.8vw,30px);color:#02176D;margin:40px 0 14px}
.kv .art-body h3{font-size:clamp(19px,2.2vw,22px);color:#222;margin:28px 0 10px}
.kv .art-body ul,.kv .art-body ol{margin:0 0 18px;padding-left:24px}
.kv .art-body ul{list-style:disc}.kv .art-body ol{list-style:decimal}
.kv .art-body li{margin:0 0 8px;padding-left:4px}
.kv .art-body a{color:#02176D;border-bottom:1px solid currentColor}
.kv .art-table{overflow-x:auto;margin:22px 0;border-radius:6px;border:1px solid #D3E6EE}
.kv .art-body table{width:100%;border-collapse:collapse;font-size:16px;min-width:560px}
.kv .art-body th{background:#02176D;color:#fff;text-align:left;padding:12px 14px;font-weight:700}
.kv .art-body td{padding:12px 14px;border-top:1px solid #E1EEF3;vertical-align:top;color:#3A3F4A}
.kv .art-body tr:nth-child(even) td{background:#F3FBFE}
.kv .art-fig{margin:30px 0}.kv .art-fig img{width:100%;height:auto;display:block;border-radius:6px}
.kv .art-back{margin-top:34px;padding-top:22px;border-top:1px solid #D3E6EE;font:700 13px/1 'Roboto Condensed',sans-serif;letter-spacing:.1em;text-transform:uppercase}
.kv .art-back a{color:#222}.kv .art-back a:hover{color:#02176D}
.kv .cta-band{background:#02176D;padding:64px 0;text-align:center;color:#fff}
.kv .cta-band h2{font-size:clamp(24px,3.2vw,38px);color:#fff}
.kv .cta-band p{max-width:620px;margin:16px auto 0;color:rgba(255,255,255,.9)}
.kv .cta-band .btn{margin-top:28px}
@media(max-width:700px){.kv .art-card{padding:30px 20px 34px;margin-top:-20px}.kv .ahero{padding:110px 0 56px}.kv .art-body{font-size:17px}}
</style>"""
ALTS = json.load(open(R / "image-alts.json")) if (R / "image-alts.json").exists() else {}
IMAGES = {}
for _n, _alt in ALTS.items():
    _p = R / "img" / f"{_n}.webp"
    if _p.exists(): IMAGES[int(_n)] = {"src": "data:image/webp;base64," + base64.b64encode(_p.read_bytes()).decode(), "alt": _alt}

def ui(d): y, m, dd = d.split("-"); return f"{dd}.{m}.{y}"
def clean(body, date):
    body = body.replace("[ДАТА]", ui(date))
    body = re.sub(r'</?(strong|b)>', '', body)
    body = re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', lambda m: m.group(0) if m.group(1).startswith("http") else m.group(2), body, flags=re.S)
    body = re.sub(r'<table[^>]*>', '<table>', body)
    body = re.sub(r'<table>.*?</table>', lambda m: '<div class="art-table">' + re.sub(r'\s*\n\s*', '', m.group(0)) + '</div>', body, flags=re.S)
    n = [0]
    def idr(m): n[0] += 1; return f'<{m.group(1)} id="s{n[0]}">'
    return re.sub(r'<(h2|h3)>', idr, body)

def pidcss(pid):
    if not pid: return ""
    return (f"<style>body.page-id-{pid} .entry-header,body.page-id-{pid} .ast-breadcrumbs-wrapper,body.page-id-{pid} .entry-title,body.page-id-{pid} .site-footer{{display:none!important}}"
            f"body.page-id-{pid} .ast-container,body.page-id-{pid} #primary,body.page-id-{pid} .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}body.page-id-{pid}{{background:#E4F7FC}}</style>")

def page_html(i, url, pid, date, tag, h1, desc, body, ld):
    return ("<!-- wp:html -->\n" + f'<meta name="description" content="{html.escape(desc, quote=True)}">\n' + CSS_HUB + "\n" + CSS_ART + "\n" + pidcss(pid) + "\n" + HDR +
        '<div class="kv"><header class="ahero"><div class="w"><p class="crumbs"><a href="/">Головна</a> / <a href="/blog/">Блог</a></p>'
        f'<h1>{h1}</h1><span class="bar"></span></div></header>'
        f'<section class="art-sec"><div class="w"><article class="art-card"><div class="art-meta"><span class="art-tag">{tag}</span><time datetime="{date}">{ui(date)}</time><span>{AUTHOR}</span></div>'
        f'<div class="art-body">{body}</div><p class="art-back"><a href="/blog/">← Усі статті блогу</a></p></article></div></section>'
        '<section class="cta-band"><div class="w"><h2>Потрібна консультація юриста?</h2><p>Опишіть ситуацію в Telegram: підкажу перші кроки та скажу, чи потрібне представництво.</p>'
        f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div></section>'
        + FTR + "</div>\n" + '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>\n<!-- /wp:html -->")

def build(i, url, pid):
    date, tag = DATES[i - 1], TAGS[i - 1]
    src = (R / "src" / f"{i:02d}-{url}.html").read_text(encoding="utf-8")
    m = re.search(r'<b>Title:</b>\s*(.*?)<br><b>Description:</b>\s*(.*?)</p>', src, re.S)
    title, desc = m.group(1).strip(), m.group(2).strip()
    h1 = re.search(r'<h1>(.*?)</h1>', src).group(1).strip()
    body = clean(src[src.index('</h1>') + 5:].strip(), date)
    fm = re.search(r'<h2[^>]*>(?:FAQ|Питання та відповіді|Питання й відповіді|Поширені запитання|Часті запитання|Часті питання)</h2>(.*?)(?=<h2|\Z)', body, re.S)
    faq = re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>', fm.group(1), re.S) if fm else []
    if i in STUB:
        exc = "Стаття готується до публікації."
    else:
        p1 = next(re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<p>(.*?)</p>', body, re.S) if not x.startswith('Автор'))
        sents = re.split(r'(?<=[.!?])(?<!ст\.)(?<!ч\.)(?<!п\.)\s+', p1)
        exc = ""
        for x in sents:
            exc = (exc + " " + x).strip()
            if len(exc) >= 120: break
        if len(exc) > 230: exc = exc[:227].rsplit(" ", 1)[0] + "…"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": h1, "description": desc, "inLanguage": "uk", "datePublished": date + "T09:00:00+02:00",
         "mainEntityOfPage": f"{SITE}/blog/{url}/", "author": {"@type": "Person", "name": AUTHOR}, "isPartOf": {"@type": "Blog", "url": SITE + "/blog/"}}]}
    if faq:
        ld["@graph"].append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub(r'<[^>]+>', '', q),
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}} for q, a in faq]})
    fig = IMAGES.get(i)
    if fig:
        f = (f'<figure class="art-fig"><img src="{fig["src"]}" alt="{html.escape(fig["alt"], quote=True)}" width="1200" height="800" loading="lazy" decoding="async"></figure>')
        body = body.replace('<h2 id="s1">', f + '\n<h2 id="s1">', 1) if '<h2 id="s1">' in body else f + body
    content = page_html(i, url, pid, date, tag, h1, desc, body, ld)
    payload = {"title": h1, "slug": url, "status": "draft", "parent": HUB_ID, "template": "elementor_canvas",
               "content": content, "excerpt": exc, "date": date + "T09:00:00"}
    return payload, dict(title=title, desc=desc, words=len(re.sub(r'<[^>]+>', ' ', body).split()), faq=len(faq), h1=h1, exc=exc)

# ---------- хаб (динамічний + запасний список для чернетки) ----------
JS = r'''(function(){var A=String.fromCharCode(38);var g=document.getElementById("blogGrid");if(!g)return;var M=%(M)s;var LIM=%(lim)d,PID=%(hub)d,FB=%(fb)d;
function T(s){var d=document.createElement("div");d.innerHTML=s;return(d.textContent||"").replace(/\s+/g," ").trim()}
function D(s){var p=String(s).slice(0,10).split("-");return p[2]+"."+p[1]+"."+p[0]}
function E(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
function card(u,slug,ti,dt,ex){var m=M[slug]||{t:"Стаття"};var art=E("article","bl-card"),cv=E("a","bl-cover");cv.href=u;cv.tabIndex=-1;
if(m.i){var im=new Image();im.src=m.i;im.alt=ti;im.width=640;im.height=427;im.loading="lazy";cv.appendChild(im)}
cv.appendChild(E("span","bl-tag",m.t));art.appendChild(cv);var b=E("div","bl-body"),tm=E("time",null,D(dt));tm.setAttribute("datetime",String(dt).slice(0,10));b.appendChild(tm);
var h=E("h3"),l=E("a",null,ti);l.href=u;l.style.color="inherit";h.appendChild(l);b.appendChild(h);b.appendChild(E("p",null,ex));var mr=E("a","bl-more","Читати статтю");mr.href=u;b.appendChild(mr);art.appendChild(b);g.appendChild(art)}
function fallback(){if(!FB){g.appendChild(E("p","bl-empty","Перші статті з’являться найближчим часом."));return}Object.keys(M).sort(function(a,b){return M[b].d.localeCompare(M[a].d)}).slice(0,LIM).forEach(function(s){card("/blog/"+s+"/",s,M[s].h,M[s].d,M[s].e)})}
fetch("/wp-json/wp/v2/pages?parent="+PID+A+"per_page=100"+A+"orderby=date"+A+"order=desc"+A+"_fields=id,date,link,slug,title,excerpt",{credentials:"omit"}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(a){
if(!a.length){fallback();return}a.slice(0,LIM).forEach(function(x){card(new URL(x.link,location.href).pathname,x.slug,T(x.title.rendered),x.date,T((x.excerpt?x.excerpt.rendered:"")||""))})}).catch(fallback)})();'''
def thumb(n):
    from PIL import Image
    p = R / "img" / f"{n:02d}.webp"
    if not p.exists(): return ""
    im = Image.open(p).convert("RGB").resize((640, 427)); b = io.BytesIO(); im.save(b, "WEBP", quality=70, method=6)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()
FALLBACK = False   # True -- показувати запасний список із 12 карток, поки статті в чернетках (лише для перегляду макета)
def blog_js(gid, lim, infos):
    M = {}
    for i, url, _ in json.load(open(R / "src/index.json")):
        inf = infos[i]; M[url] = {"t": TAGS[i-1], "i": thumb(i), "h": inf["h1"], "d": DATES[i-1], "e": inf["exc"]}
    Mj = json.dumps(M, ensure_ascii=False, separators=(",", ":")).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    return "<script>" + JS.replace('getElementById("blogGrid")', 'getElementById("%s")' % gid) % dict(M=Mj, hub=HUB_ID, lim=lim, fb=int(FALLBACK)) + "</script>"
def hub_html(infos):
    js = blog_js("blogGrid", 100, infos)
    css = (f"<style>body.page-id-{HUB_ID} .entry-header,body.page-id-{HUB_ID} .ast-breadcrumbs-wrapper,body.page-id-{HUB_ID} .entry-title,body.page-id-{HUB_ID} .site-footer{{display:none!important}}"
           f"body.page-id-{HUB_ID} .ast-container,body.page-id-{HUB_ID} #primary,body.page-id-{HUB_ID} .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}body.page-id-{HUB_ID}{{background:#E4F7FC}}</style>")
    inner = ('<header class="hero"><div class="w"><div><h1>Мої статті</h1><span class="bar"></span><p class="sub">Адвокат зі скасування судових наказів<br>та колекторських дій</p>'
             '<p class="lead">Пояснюю питання списання кредитних боргів, дій МФО і колекторів простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>'
             f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div>'
             '<div class="ph"><img src="https://bankruptcyukraine.com/wp-content/uploads/2025/07/bondar-oleh-oleksiiovych-yuryst-po-kredytam.jpg" alt="Бондар Олег Олексійович" width="640" height="640"></div></div></header>'
             '<section class="sec" id="articles"><div class="w"><div class="bl-g" id="blogGrid"></div>' + js + '</div></section>')
    return "<!-- wp:html -->\n" + CSS_HUB + "\n" + css + "\n" + HDR + '<div class="kv">' + inner + FTR + "</div>\n<!-- /wp:html -->"

def call(method, url, data=None):
    cmd = ["curl", "-s", "-m", "120", "-X", method, "-H", "Content-Type: application/json", url]
    if data is not None: cmd += ["--data-binary", "@-"]
    r = subprocess.run(cmd, input=(json.dumps(data, ensure_ascii=False).encode() if data is not None else None), capture_output=True)
    return json.loads(r.stdout.decode())

if __name__ == "__main__":
    (R / "payload").mkdir(exist_ok=True); (R / "preview").mkdir(exist_ok=True)
    idf = R / "draft-ids.json"; ids = json.load(open(idf)) if idf.exists() else {}
    idx = json.load(open(R / "src/index.json")); infos = {}
    for i, url, _ in idx:
        p, info = build(i, url, ids.get(url)); infos[i] = info
        (R / "payload" / f"{i:02d}-{url}.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        (R / "preview" / f"{i:02d}-{url}.html").write_text(p["content"], encoding="utf-8")
        print(i, url, info["words"], "faq", info["faq"], "|", info["title"][:60], "|", len(info["desc"]))
        if "--create" in sys.argv:
            if url not in ids:
                r = call("POST", f"{SITE}/wp-json/wp/v2/pages", p)
                if "id" not in r: print("   ERR", str(r)[:300]); continue
                ids[url] = r["id"]; json.dump(ids, open(idf, "w"), ensure_ascii=False, indent=1)
                p, _ = build(i, url, ids[url])
            r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{ids[url]}", p)
            print("   ->", r.get("id"), r.get("status"), r.get("date"), r.get("parent"), r.get("template"), str(r.get("code", ""))[:60])
    hub = hub_html(infos)
    (R / "preview" / "hub.html").write_text(hub, encoding="utf-8")
    if "--create" in sys.argv:
        r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{HUB_ID}", {"content": hub, "title": "Мої статті"})
        print("hub ->", r.get("id"), r.get("status"), str(r.get("code", ""))[:60])
