#!/usr/bin/env python3
"""jurist-online.info (Мельник М. М.): статті блогу 1-4 (заплановані), хаб «Мої статті» (чернетка id 2675), головна (чернетка id 2679).
  python3 build_site.py            -> payload/, preview/ (нічого не відправляє)
  python3 build_site.py --media    -> завантажує картинки в медіатеку (ids у media-ids.json)
  python3 build_site.py --push     -> створює/оновлює статті (status=future), оновлює ЧЕРНЕТКИ хабу і головної
Хаб і головна лишаються ЧЕРНЕТКАМИ: публікація тільки за командою.
"""
import json, re, sys, pathlib, subprocess, html, os
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import convert
R = pathlib.Path(__file__).parent
SITE = "https://jurist-online.info"
HUB_ID, HOME_ID = 2675, 2679
AUTHOR = "Мельник Марія Миколаївна"
TG = "https://t.me/maria_yrist"
PH = SITE + "/wp-content/uploads/2025/07/melnyk-mariia-mykolaivna-yuryst-po-kredytam.jpg"
PH2 = SITE + "/wp-content/uploads/2025/07/melnyk-mariia-mykolaivna-kredytnyi-yuryst.jpg"
ART = [
 (1, "01-yak-diznatysia-chy-vziato-na-mene-mikrozaim", "yak-diznatysia-chy-vziato-na-mene-mikrozaim", "2026-11-12", "Перевірка боргів", "Жінка перевіряє інформацію про кредити на телефоні й ноутбуці за робочим столом"),
 (2, "02-shcho-robyty-iakshcho-na-tebe-oformyly-mikrozaim", "shcho-robyty-iakshcho-na-tebe-oformyly-mikrozaim", "2026-11-13", "Шахрайські кредити", "Чоловік уважно вивчає кредитні документи за столом"),
 (3, "03-chy-mozhut-oformyty-kredyt-bez-moho-vidoma", "chy-mozhut-oformyty-kredyt-bez-moho-vidoma", "2026-11-16", "Шахрайські кредити", "Чоловік розмовляє по телефону й робить нотатки біля вікна"),
 (4, "04-yak-zakhystytysia-vid-kredytnykh-shakhraiv", "yak-zakhystytysia-vid-kredytnykh-shakhraiv", "2026-11-18", "Захист від шахраїв", "Юрист за ноутбуком у кабінеті з книжковими шафами"),
]
CSS_HUB = (R / "hub-css.html").read_text(encoding="utf-8")
HDR = (R / "hub-header.html").read_text(encoding="utf-8")
FTR = (R / "hub-footer.html").read_text(encoding="utf-8")
CSS_ART = """<style>
.kv .ahero{background:linear-gradient(90deg,#FCE8CF 0 50%,#FFF6EA 50% 100%);padding:130px 0 80px;color:#2E1700}
.kv .ahero .crumbs{font:700 12px/1 'DM Sans',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8A5A25}
.kv .ahero .crumbs a{color:#2E1700;border-bottom:1px solid rgba(46,23,0,.4)}
.kv .ahero h1{font-size:clamp(28px,4vw,46px);margin-top:20px;max-width:1000px;color:#2E1700}
.kv .art-sec{background:#FBF5F1;padding:0 0 80px}
.kv .art-card{position:relative;max-width:900px;margin:-30px auto 0;background:#fff;border-radius:16px;padding:44px 52px 48px;color:#4A3523;box-shadow:0 14px 40px rgba(102,51,0,.14)}
.kv .art-meta{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-bottom:26px;font:700 13px/1 'DM Sans',sans-serif;letter-spacing:.06em;color:#8A5A25}
.kv .art-tag{padding:6px 14px;background:#FFA500;color:#2E1700;font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.kv .art-meta time{color:#B56A00}
.kv .art-body{font-size:18px;line-height:1.7;color:#4A3523}
.kv .art-body p{margin:0 0 16px}
.kv .art-body h2{font-size:clamp(23px,2.8vw,30px);color:#2E1700;margin:40px 0 14px;scroll-margin-top:90px}
.kv .art-body h3{font-size:clamp(19px,2.2vw,22px);color:#2E1700;margin:28px 0 10px}
.kv .art-body ul,.kv .art-body ol{margin:0 0 18px;padding-left:24px}
.kv .art-body ul{list-style:disc}.kv .art-body ol{list-style:decimal}
.kv .art-body li{margin:0 0 8px;padding-left:4px}
.kv .art-body a{color:#663300;border-bottom:1px solid currentColor}
.kv .art-body blockquote{margin:20px 0;padding:18px 24px;background:#FBF5F1;border-left:4px solid #FFA500;border-radius:0 12px 12px 0}
.kv .art-body blockquote p{margin:0 0 8px}.kv .art-body blockquote p:last-child{margin:0}
.kv .art-toc{margin:0 0 30px;padding:20px 26px;background:#FBF5F1;border-radius:12px}
.kv .art-toc b{display:block;margin-bottom:10px;font:700 14px/1 'DM Sans',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#2E1700}
.kv .art-toc ol{margin:0;padding-left:22px;font-size:16px}.kv .art-toc li{margin:0 0 6px}
.kv .art-toc a{border:0;color:#663300}.kv .art-toc a:hover{color:#B56A00}
.kv .art-table{overflow-x:auto;margin:22px 0;border-radius:12px;border:1px solid #EADCCB}
.kv .art-body table{width:100%;border-collapse:collapse;font-size:16px;min-width:560px}
.kv .art-body th{background:#663300;color:#fff;text-align:left;padding:12px 14px;font-weight:700}
.kv .art-body td{padding:12px 14px;border-top:1px solid #F0E4D4;vertical-align:top;color:#4A3523}
.kv .art-body tr:nth-child(even) td{background:#FBF5F1}
.kv .art-fig{margin:30px 0}.kv .art-fig img{width:100%;height:auto;display:block;border-radius:12px}
.kv .art-back{margin-top:34px;padding-top:22px;border-top:1px solid #EADCCB;font:700 13px/1 'DM Sans',sans-serif;letter-spacing:.1em;text-transform:uppercase}
.kv .art-back a{color:#2E1700}.kv .art-back a:hover{color:#B56A00}
.kv .cta-band{background:#663300;padding:64px 0;text-align:center;color:#fff}
.kv .cta-band h2{font-size:clamp(24px,3.2vw,38px);color:#fff}
.kv .cta-band p{max-width:620px;margin:16px auto 0;color:rgba(255,255,255,.9)}
.kv .cta-band .btn{margin-top:28px;background:#FFA500;color:#2E1700}.kv .cta-band .btn:hover{background:#fff}
@media(max-width:900px){.kv .ahero{background:#FCE8CF}}
@media(max-width:700px){.kv .art-card{padding:30px 20px 34px;margin-top:-20px}.kv .ahero{padding:110px 0 56px}.kv .art-body{font-size:17px}}
</style>"""
CSS_SITE = """<style>
.kv .hero .soc{margin-top:26px;display:flex;gap:18px;font:700 13px/1 'DM Sans',sans-serif;letter-spacing:.1em;text-transform:uppercase}
.kv .hero .soc a{color:#663300;border-bottom:1px solid #663300;padding-bottom:3px}
.kv section[id]{scroll-margin-top:68px}
.kv .sec.about{background:#fff}.kv .sec.about .lead2{max-width:760px}.kv .sec.about h3.k{font-size:clamp(22px,2.6vw,32px);text-align:center;margin-top:14px;color:#2E1700}
.kv .exp .g{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:44px;align-items:stretch}
.kv .exp .g img{width:100%;height:100%;object-fit:cover;border-radius:16px;display:block;min-height:320px}
.kv .exp .cc{display:grid;gap:18px}
.kv .exp .c{background:#EDE6E1;border-radius:16px;padding:24px 26px}
.kv .exp .c h4{font:600 20px/1.25 Jost,sans-serif;color:#2E1700;margin:0 0 10px}
.kv .exp .c p{margin:0;font-size:16px;color:#5A4634}
.kv .exp .c a{color:#663300;border-bottom:1px solid currentColor}
.kv .cen{text-align:center;margin-top:40px}
.kv .sec.res{background:#FBF5F1}
.kv .res-g{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px;margin-top:40px}
.kv .res-g a{background:#fff;padding:6px;border-radius:6px;display:block;box-shadow:0 8px 24px rgba(102,51,0,.1)}.kv .res-g img{display:block;width:100%;height:auto}
.kv .sec.rev{background:#F3E5CE}.kv .rev-box{max-width:760px;margin:36px auto 0}
.kv .bl-empty{grid-column:1/-1;text-align:center;color:#6B5848;padding:30px 10px;font-size:18px}
@media(max-width:1000px){.kv .res-g{grid-template-columns:repeat(3,minmax(0,1fr))}.kv .exp .g{grid-template-columns:1fr}}
@media(max-width:620px){.kv .res-g{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}
</style>"""
def ui(d): y, m, dd = d.split("-"); return f"{dd}.{m}.{y}"
import base64, io
from PIL import Image
def b64(folder, w, h, q):
    im = Image.open(R / "img" / (folder + ".webp")).convert("RGB").resize((w, h)); b = io.BytesIO(); im.save(b, "WEBP", quality=q, method=6)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()
MEDIA = {}
for _n, _f, _s, *_ in ART:
    MEDIA[_s] = {"url": b64(_f, 1200, 800, 78), "card": b64(_f, 640, 427, 70)}
IDS = json.load(open(R / "draft-ids.json")) if (R / "draft-ids.json").exists() else {}

def call(method, url, data=None, raw=None, headers=()):
    cmd = ["curl", "-s", "-m", "180", "-X", method, url]
    for h in headers: cmd += ["-H", h]
    if data is not None: cmd += ["-H", "Content-Type: application/json", "--data-binary", "@-"]; inp = json.dumps(data, ensure_ascii=False).encode()
    elif raw is not None: cmd += ["--data-binary", "@-"]; inp = raw
    else: inp = None
    r = subprocess.run(cmd, input=inp, capture_output=True)
    try: return json.loads(r.stdout.decode())
    except Exception: return {"raw": r.stdout.decode()[:300]}

def article(n, folder, slug, date, tag, alt):
    txt = (R / folder / "text-fixed.txt").read_text(encoding="utf-8")
    meta, h1, toc, blocks = convert.parse(txt, n)
    body = convert.render(blocks)
    h2s = re.findall(r'<h2 id="(s\d+)">(.*?)</h2>', body)
    tocl = '<nav class="art-toc" aria-label="Зміст"><b>Зміст</b><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in h2s) + "</ol></nav>"
    m = MEDIA.get(slug)
    fig = ""
    if m: fig = f'<figure class="art-fig"><img src="{m["url"]}" alt="{html.escape(alt, quote=True)}" width="1200" height="800" loading="lazy" decoding="async"></figure>'
    first = body.find('<h2 id="s1">')
    body = body[:first] + fig + tocl + "\n" + body[first:]
    faq = []
    fm = re.search(r'<h2 id="s\d+">FAQ</h2>(.*?)(?=<h2|\Z)', body, re.S)
    if fm: faq = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", fm.group(1), re.S)
    plain = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s))
    ps = [plain(x) for x in re.findall(r"<p>(.*?)</p>", body, re.S)]
    exc = ""
    for x in re.split(r"(?<=[.!?])\s+", ps[0] + " " + ps[1]):
        exc = (exc + " " + x).strip()
        if len(exc) >= 120: break
    if len(exc) > 230: exc = exc[:227].rsplit(" ", 1)[0] + "…"
    url = f"{SITE}/blog/{slug}/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": h1, "description": meta["desc"], "inLanguage": "uk", "datePublished": date + "T09:00:00+02:00", "dateModified": date + "T09:00:00+02:00",
         "mainEntityOfPage": url, "author": {"@type": "Person", "name": AUTHOR, "url": SITE + "/"}, "publisher": {"@type": "Person", "name": AUTHOR}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Головна", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Блог", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": h1, "item": url}]}]}
    if faq: ld["@graph"].append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faq]})
    content = ("<!-- wp:html -->\n" + CSS_HUB + "\n" + CSS_ART + "\n" + HDR +
        '<div class="kv"><header class="ahero"><div class="w"><p class="crumbs"><a href="/">Головна</a> / <a href="/blog/">Блог</a></p>'
        f'<h1>{h1}</h1><span class="bar"></span></div></header>'
        f'<section class="art-sec"><div class="w"><article class="art-card"><div class="art-meta"><span class="art-tag">{tag}</span><time datetime="{date}">{ui(date)}</time><span>{AUTHOR}</span></div>'
        f'<div class="art-body">{body}</div><p class="art-back"><a href="/blog/">← Усі статті блогу</a></p></article></div></section>'
        '<section class="cta-band"><div class="w"><h2>Потрібна консультація юриста?</h2><p>Опишіть ситуацію в Telegram: перегляну договір чи кредитну історію та підкажу перший крок.</p>'
        f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div></section>'
        + FTR + "</div>\n" + '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>\n<!-- /wp:html -->")
    payload = {"title": h1, "slug": slug, "status": "future", "date": date + "T09:00:00", "parent": HUB_ID, "template": "elementor_canvas",
               "content": content, "excerpt": exc, "meta": {"_yoast_wpseo_title": meta["title"], "_yoast_wpseo_metadesc": meta["desc"]}}
    return payload, dict(h1=h1, exc=exc, title=meta["title"], desc=meta["desc"], faq=len(faq), words=len(plain(body).split()))

JS = r'''(function(){var A=String.fromCharCode(38);var g=document.getElementById("%(gid)s");if(!g)return;var M=%(M)s;var LIM=%(lim)d,PID=%(hub)d;var PV=location.search.indexOf("preview=true")>-1;
function T(s){var d=document.createElement("div");d.innerHTML=s;return(d.textContent||"").replace(/\s+/g," ").trim()}
function D(s){var p=String(s).slice(0,10).split("-");return p[2]+"."+p[1]+"."+p[0]}
function E(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
function card(u,slug,ti,dt,ex){var m=M[slug]||{t:"Стаття"};var art=E("article","bl-card"),cv=E("a","bl-cover");cv.href=u;cv.tabIndex=-1;
if(m.i){var im=new Image();im.src=m.i;im.alt=ti;im.width=640;im.height=427;im.loading="lazy";cv.appendChild(im)}
cv.appendChild(E("span","bl-tag",m.t));art.appendChild(cv);var b=E("div","bl-body"),tm=E("time",null,D(dt));tm.setAttribute("datetime",String(dt).slice(0,10));b.appendChild(tm);
var h=E("h3"),l=E("a",null,ti);l.href=u;l.style.color="inherit";h.appendChild(l);b.appendChild(h);b.appendChild(E("p",null,ex));var mr=E("a","bl-more","Читати статтю");mr.href=u;b.appendChild(mr);art.appendChild(b);g.appendChild(art)}
function fallback(){if(!PV){g.appendChild(E("p","bl-empty","Перші статті з’являться найближчим часом."));return}Object.keys(M).sort(function(a,b){return M[b].d.localeCompare(M[a].d)}).slice(0,LIM).forEach(function(s){card("/blog/"+s+"/",s,M[s].h,M[s].d,M[s].e)})}
fetch("/wp-json/wp/v2/pages?parent="+PID+A+"per_page=100"+A+"orderby=date"+A+"order=desc"+A+"_fields=id,date,link,slug,title,excerpt",{credentials:"omit"}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(a){
if(!a.length){fallback();return}a.slice(0,LIM).forEach(function(x){card(new URL(x.link,location.href).pathname,x.slug,T(x.title.rendered),x.date,T((x.excerpt?x.excerpt.rendered:"")||""))})}).catch(fallback)})();'''
def blog_js(gid, lim, infos):
    M = {}
    for n, folder, slug, date, tag, alt in ART:
        m = MEDIA.get(slug, {})
        M[slug] = {"t": tag, "i": m.get("card", m.get("url", "")), "h": infos[n]["h1"], "d": date, "e": infos[n]["exc"]}
    Mj = json.dumps(M, ensure_ascii=False, separators=(",", ":")).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    return "<script>" + JS % dict(gid=gid, M=Mj, hub=HUB_ID, lim=lim) + "</script>"

def hub_html(infos):
    inner = ('<header class="hero"><div class="w"><div><h1>Мої статті</h1><span class="bar"></span><p class="sub">Юрист з питань<br>захисту прав споживачів</p>'
             '<p class="lead">Пояснюю питання захисту прав споживачів кредитних послуг, дій МФО та шахрайських кредитів простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>'
             f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></div>'
             f'<div class="ph"><img src="{PH}" alt="Мельник Марія Миколаївна" width="640" height="640"></div></div></header>'
             '<section class="sec" id="articles"><div class="w"><div class="bl-g" id="blogGrid"></div>' + blog_js("blogGrid", 100, infos) + '</div></section>')
    return "<!-- wp:html -->\n" + CSS_HUB + "\n" + CSS_SITE + "\n" + HDR + '<div class="kv">' + inner + FTR + "</div>\n<!-- /wp:html -->"

def home_html(infos):
    hdr = HDR.replace(' class="cur"', "")
    docs = "".join(f'<a href="{SITE}/wp-content/uploads/2025/07/doc{i}-scaled.webp" target="_blank" rel="noopener"><img src="{SITE}/wp-content/uploads/2025/07/doc{i}-{w}x300.webp" alt="Результат роботи — документ {i}" loading="lazy"></a>'
                   for i, w in zip(range(1, 10), (191, 212, 210, 240, 214, 224, 216, 226, 220)))
    inner = (
     f'<header class="hero" id="top"><div class="w"><div><h1>{AUTHOR}</h1><span class="bar"></span><p class="sub">Юрист з питань захисту прав споживачів.</p>'
     f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a>'
     '<p class="soc"><a href="https://www.facebook.com/profile.php?id=100087573902068" target="_blank" rel="noopener">Facebook</a><a href="https://www.instagram.com/maria_yrist/" target="_blank" rel="noopener">Instagram</a></p></div>'
     f'<div class="ph"><img src="{PH}" alt="Мельник Марія Миколаївна - юрист по кредитам" width="640" height="640"></div></div></header>'
     '<section class="sec about pre" id="about"><div class="w"><h2>Про мене</h2><span class="bar"></span><h3 class="k">Юрист з питань захисту прав споживачів.</h3>'
     '<p class="lead2">Закінчила Одеську юридичну академію у 2016 році. Має досвід супроводу спорів із мікрофінансовими організаціями, захисту прав споживачів кредитних послуг. У ЛА Консалтинг працює з 2022 року. Її особливість — вміння розмовляти з клієнтами простою мовою та захищати їхні інтереси у судах першої та апеляційної інстанцій.</p></div></section>'
     '<section class="sec exp" id="experience"><div class="w"><h2>Досвід роботи</h2><span class="bar"></span><div class="g">'
     f'<img src="{PH2}" alt="Мельник Марія Миколаївна - юрист по кредитам" width="640" height="640" loading="lazy"><div class="cc">'
     '<div class="c"><h4>2016–2018 — Юрисконсульт, МФО «CreditPlus»</h4><p>Працювала з договорами, розглядала скарги клієнтів, готувала відповіді на запити ДСФМУ.</p></div>'
     '<div class="c"><h4>2018–2021 — Старший юрист, ТОВ «Фінансовий Стандарт»</h4><p>Захист прав споживачів у кредитних спорах, участь у судових процесах.</p></div>'
     '<div class="c"><h4>З 2022 — Юрист,<br><a href="https://la.co.ua" target="_blank" rel="noopener noreferrer">ТОВ "ЛА Консалтинг - юридична фірма"</a></h4></div></div></div></div></section>'
     f'<section class="sec res" id="results"><div class="w"><h2>Результати роботи</h2><span class="bar"></span><div class="res-g">{docs}</div>'
     f'<p class="cen"><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></p></div></section>'
     '<section class="sec arts" id="articles"><div class="w"><h2>Мої статті</h2><span class="bar"></span>'
     '<p class="lead2">Пояснюю питання захисту прав споживачів кредитних послуг, дій МФО та шахрайських кредитів простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.</p>'
     '<div class="bl-g" id="homeBlog"></div>' + blog_js("homeBlog", 3, infos) + '<p class="cen"><a class="btn" href="/blog/">Усі статті</a></p></div></section>'
     '<section class="sec rev" id="reviews"><div class="w"><h2>Відгуки</h2><span class="bar"></span><div class="rev-box">[react_reviews_1]</div>'
     f'<p class="cen"><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></p></div></section>')
    return "<!-- wp:html -->\n" + CSS_HUB + "\n" + CSS_SITE + "\n" + hdr + '<div class="kv">' + inner + FTR + "</div>\n<!-- /wp:html -->"

if __name__ == "__main__":
    (R / "payload").mkdir(exist_ok=True); (R / "preview").mkdir(exist_ok=True)
    infos = {}
    for n, folder, slug, date, tag, alt in ART:
        p, info = article(n, folder, slug, date, tag, alt); infos[n] = info
        (R / "payload" / f"{n:02d}-{slug}.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        (R / "preview" / f"{n:02d}-{slug}.html").write_text(p["content"], encoding="utf-8")
        print(n, slug, "words", info["words"], "faq", info["faq"], "|", info["title"][:50], "|", len(info["desc"]), "|", info["exc"][:80])
        if "--push" in sys.argv:
            if slug not in IDS:
                r = call("POST", SITE + "/wp-json/wp/v2/pages", p)
                if "id" not in r: print("   ERR", str(r)[:300]); continue
                IDS[slug] = r["id"]; json.dump(IDS, open(R / "draft-ids.json", "w"), ensure_ascii=False, indent=1)
            else:
                r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{IDS[slug]}", p)
            print("   ->", r.get("id"), r.get("status"), r.get("date"), r.get("parent"), r.get("template"), r.get("link"), str(r.get("code", ""))[:60])
    hub, home = hub_html(infos), home_html(infos)
    (R / "preview" / "hub.html").write_text(hub, encoding="utf-8"); (R / "preview" / "home.html").write_text(home, encoding="utf-8")
    if "--push" in sys.argv:
        r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{HUB_ID}", {"content": hub, "status": "draft", "template": "elementor_canvas"}); print("hub ->", r.get("id"), r.get("status"), str(r.get("code", ""))[:60])
        r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{HOME_ID}", {"content": home, "status": "draft", "template": "elementor_canvas"}); print("home ->", r.get("id"), r.get("status"), r.get("template"), str(r.get("code", ""))[:60])
