#!/usr/bin/env python3
"""yuristy.in.ua (Хмельницький М. В.): стаття 1 (запланована на 12.11), хаб `blog` id 25521 і головна 25525 уже опубліковані.
  python3 build_site.py            -> payload/, preview/ (нічого не відправляє)
  python3 build_site.py --media    -> завантажує картинки в медіатеку (ids у media-ids.json)
  python3 build_site.py --push     -> створює/оновлює статті (status=future), оновлює ЧЕРНЕТКИ хабу і головної
Хаб і головну цей скрипт не чіпає (блок «Мої статті» оновлюється через tools/publish_hub_home.py --patch-scripts).
"""
import json, re, sys, pathlib, subprocess, html, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent / "jurist-online.info" / "blog-drafts"))
import convert
R = pathlib.Path(__file__).parent
SITE = "https://yuristy.in.ua"
HUB_ID, HOME_ID = 25521, 25525
AUTHOR = "Хмельницький Максим Валерійович"
TG = "https://t.me/max_yrist"
PH = SITE + "/wp-content/uploads/2025/07/khmelnytskyi-maksym-valeriiovych-yuryst-po-kredytam.jpg"
ART = [
 (1, "01-yak-skasuvaty-rishennia-sudu-za-kredytom", "yak-skasuvaty-rishennia-sudu-za-kredytom", "2026-11-12", "Рішення суду", "Жінка в чорному піджаку читає судові документи за столом в офісі"),
 (2, "02-apeliatsiia-na-rishennia-sudu-za-kredytom", "apeliatsiia-na-rishennia-sudu-za-kredytom", "2026-11-13", "Апеляція", "Чоловік у темно-синій сорочці уважно читає судове рішення за столом в офісі"),
 (3, "03-shcho-take-strok-pozovnoi-davnosti-za-kredytom", "shcho-take-strok-pozovnoi-davnosti-za-kredytom", "2026-11-16", "Позовна давність", "Жінка у темно-синьому кардигані замислено дивиться на документ, поруч календар і калькулятор"),
 (4, "04-yak-borotysia-z-pryvatbankom", "yak-borotysia-z-pryvatbankom", "2026-11-18", "Кредитні спори", "Жінка в сірому піджаку уважно читає кредитний договір за столом в офісі, поруч закритий ноутбук і склянка води"),
]
PARSE_CFG = {
 4: dict(tables=[("Спосіб", 5, 7), ("Складник", 3, 7)], extra_h3=('Ситуація 1. Борг за кредиткою, а договору немає — лише анкета-заява', 'Ситуація 2. Банк нараховує проценти роками після вимоги повернути весь борг', 'Ситуація 3. Як розірвати договір по кредитці і що буде з боргом', 'Розбір рішення: справа № 342/180/17', 'Проценти після спливу строку і ст. 625 ЦК', 'Документи, які потрібні', 'Строки, які не можна пропустити')),
 3: dict(tables=[("Платіж за графіком", 3, 5), ("Переривають (ваші активні дії)", 2, 5)], extra_h3=("Щомісячні платежі: строк окремо за кожним", "Коли строк кредитування закінчився або банк вимагав усю суму", "Приклад із розрахунком", "Що каже закон", "Як вирішив суд", "Моя позиція")),
 2: dict(tables=[("Критерій", 3, 6), ("Показник", 2, 5)], extra_h3=("Висновок автора", "Ситуація 1: рішення не вручили", "Ситуація 2: банк списував гроші з картки", "Умовний розрахунок")),
 1: dict(tables=[("Спосіб", 6, 4), ("Стаття розрахунку", 3, 5)], extra_h3=("Задача 1. Строк і повний текст рішення", "Задача 2. Позовна давність після заочного рішення", "Задача 3. Банк списував кошти з картки", "Розбір постанови Великої Палати № 444/9519/12", "Розрахунок на прикладі", "Документи для заяви", "Що зробити сьогодні: чекліст")),
}
CSS_HUB = (R / "hub-css.html").read_text(encoding="utf-8")
HDR = (R / "hub-header.html").read_text(encoding="utf-8")
FTR = (R / "hub-footer.html").read_text(encoding="utf-8")
CSS_ART = """<style>
.kv .ahero{background:linear-gradient(90deg,#3E4E8A 0 50%,#3E4E8A 50% 100%);padding:130px 0 80px;color:#fff}
.kv .ahero .crumbs{font:700 12px/1 'Open Sans',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#fff}
.kv .ahero .crumbs a{color:#fff;border-bottom:1px solid rgba(255,255,255,.5)}
.kv .ahero h1{font-size:clamp(28px,4vw,46px);margin-top:20px;max-width:1000px;color:#fff}
.kv .art-sec{background:#EEF0F8;padding:0 0 80px}
.kv .art-card{position:relative;max-width:900px;margin:-30px auto 0;background:#fff;border-radius:16px;padding:44px 52px 48px;color:#3B4452;box-shadow:0 14px 40px rgba(36,42,54,.12)}
.kv .art-meta{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-bottom:26px;font:700 13px/1 'Open Sans',sans-serif;letter-spacing:.06em;color:#3B4452}
.kv .art-tag{padding:6px 14px;background:#1A5CE0;color:#fff;font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.kv .art-meta time{color:#1346B5}
.kv .art-body{font-size:18px;line-height:1.7;color:#3B4452}
.kv .art-body p{margin:0 0 16px}
.kv .art-body h2{font-size:clamp(23px,2.8vw,30px);color:#242A36;margin:40px 0 14px;scroll-margin-top:90px}
.kv .art-body h3{font-size:clamp(19px,2.2vw,22px);color:#242A36;margin:28px 0 10px}
.kv .art-body ul,.kv .art-body ol{margin:0 0 18px;padding-left:24px}
.kv .art-body ul{list-style:disc}.kv .art-body ol{list-style:decimal}
.kv .art-body li{margin:0 0 8px;padding-left:4px}
.kv .art-body a{color:#242A36;border-bottom:1px solid currentColor}
.kv .art-body blockquote{margin:20px 0;padding:18px 24px;background:#EEF0F8;border-left:4px solid #1A5CE0;border-radius:0 12px 12px 0}
.kv .art-body blockquote p{margin:0 0 8px}.kv .art-body blockquote p:last-child{margin:0}
.kv .art-toc{margin:0 0 30px;padding:20px 26px;background:#EEF0F8;border-radius:12px}
.kv .art-toc b{display:block;margin-bottom:10px;font:700 14px/1 'Open Sans',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#242A36}
.kv .art-toc ol{margin:0;padding-left:22px;font-size:16px}.kv .art-toc li{margin:0 0 6px}
.kv .art-toc a{border:0;color:#242A36}.kv .art-toc a:hover{color:#1346B5}
.kv .art-table{overflow-x:auto;margin:22px 0;border-radius:12px;border:1px solid #CDD2E6}
.kv .art-body table{width:100%;border-collapse:collapse;font-size:16px;min-width:560px}
.kv .art-body th{background:#242A36;color:#fff;text-align:left;padding:12px 14px;font-weight:700}
.kv .art-body td{padding:12px 14px;border-top:1px solid #DDE1F0;vertical-align:top;color:#3B4452}
.kv .art-body tr:nth-child(even) td{background:#EEF0F8}
.kv .art-fig{margin:30px 0}.kv .art-fig img{width:100%;height:auto;display:block;border-radius:12px}
.kv .art-back{margin-top:34px;padding-top:22px;border-top:1px solid #CDD2E6;font:700 13px/1 'Open Sans',sans-serif;letter-spacing:.1em;text-transform:uppercase}
.kv .art-back a{color:#242A36}.kv .art-back a:hover{color:#1346B5}
.kv .cta-band{background:#242A36;padding:64px 0;text-align:center;color:#fff}
.kv .cta-band h2{font-size:clamp(24px,3.2vw,38px);color:#fff}
.kv .cta-band p{max-width:620px;margin:16px auto 0;color:rgba(255,255,255,.9)}
.kv .cta-band .btn{margin-top:28px;background:#1A5CE0;color:#fff}.kv .cta-band .btn:hover{background:#fff;color:#242A36}.kv .cta-band .btn:hover{background:#fff}
@media(max-width:900px){.kv .ahero{background:#3E4E8A}}
@media(max-width:700px){.kv .art-card{padding:30px 20px 34px;margin-top:-20px}.kv .ahero{padding:110px 0 56px}.kv .art-body{font-size:17px}}
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
    meta, h1, toc, blocks = convert.parse(txt, **PARSE_CFG[n])
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
    content = ("<!-- wp:html -->\n" + CSS_HUB + "\n" + CSS_ART + "\n" + 
        HDR +
        '<div class="kv"><header class="ahero"><div class="w"><p class="crumbs"><a href="/">Головна</a> / <a href="/blog/">Блог</a></p>'
        f'<h1>{h1}</h1><span class="bar"></span></div></header>'
        f'<section class="art-sec"><div class="w"><article class="art-card"><div class="art-meta"><span class="art-tag">{tag}</span><time datetime="{date}">{ui(date)}</time><span>{AUTHOR}</span></div>'
        f'<div class="art-body">{body}</div><p class="art-back"><a href="/blog/">← Усі статті блогу</a></p></article></div></section>'
        '<section class="cta-band"><div class="w"><h2>Потрібна консультація юриста?</h2><p>Опишіть ситуацію в Telegram: перевірю строки та розрахунок банку.</p>'
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

if __name__ == "__main__":
    (R / "payload").mkdir(exist_ok=True); (R / "preview").mkdir(exist_ok=True)
    infos = {}
    for n, folder, slug, date, tag, alt in ART:
        p, info = article(n, folder, slug, date, tag, alt); infos[n] = info
        # посилання на закони й справи вставляємо ДО публікації: на сайт сторінка потрапляє одразу з ними (tools/add_law_links.py --local)
        _f = R / "payload" / "_links_tmp.json"; _f.write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        subprocess.run([sys.executable, str(R.parent.parent / "tools" / "add_law_links.py"), "--local", str(_f), "--apply"], check=True)
        p = json.loads(_f.read_text(encoding="utf-8")); _f.unlink()
        (R / "payload" / f"{n:02d}-{slug}.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        (R / "preview" / f"{n:02d}-{slug}.html").write_text(p["content"], encoding="utf-8")
        print(n, slug, "words", info["words"], "faq", info["faq"], "|", info["title"][:50], "|", len(info["desc"]), "|", info["exc"][:80])
        if "--push" in sys.argv and "--only" not in sys.argv:
            sys.exit("Захист: --push лише з --only N (щоб не перезаписувати вже опубліковані статті і не губити посилання на закони)")
        if "--push" in sys.argv and str(n) == sys.argv[sys.argv.index("--only") + 1]:
            if slug not in IDS:
                r = call("POST", SITE + "/wp-json/wp/v2/pages", p)
                if "id" not in r: print("   ERR", str(r)[:300]); continue
                IDS[slug] = r["id"]; json.dump(IDS, open(R / "draft-ids.json", "w"), ensure_ascii=False, indent=1)
            else:
                r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{IDS[slug]}", p)
            print("   ->", r.get("id"), r.get("status"), r.get("date"), r.get("parent"), r.get("template"), r.get("link"), str(r.get("code", ""))[:60])
    # мапа карток для блоку «Мої статті» (картинка 640x427 + тег) -- підхоплює tools/publish_hub_home.py --patch-scripts (CARD_MAP=card-map.json)
    cm = {slug: {"t": tag, "i": MEDIA[slug]["card"]} for n, folder, slug, date, tag, alt in ART}
    (R / "card-map.json").write_text(json.dumps(cm, ensure_ascii=False, separators=(",", ":")).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e"), encoding="utf-8")
