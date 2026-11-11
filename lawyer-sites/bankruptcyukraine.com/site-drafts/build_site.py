#!/usr/bin/env python3
"""bankruptcyukraine.com: головна з шапкою .kvh і блоком «Мої статті» (нова сторінка замість Elementor-головної) + публікація хабу 1397.
  python3 build_site.py          -> payload/home.json, preview/home.html
  python3 build_site.py --push   -> створює/оновлює сторінку головної (id у ids.json) і оновлює хаб 1397 (контент)
Статус/слаг/front page виставляються окремо (див. команду публікації).
"""
import json, re, sys, pathlib
R = pathlib.Path(__file__).parent
sys.path.insert(0, str(R.parent / "blog-drafts"))
import build_drafts as bd
SITE = bd.SITE; TG = bd.TG
c = json.load(open(R / "bu_1401.json"))["content"]["raw"]
EDU = [re.sub(r'\s+', ' ', x).strip() for x in re.findall(r'<h6>\s*(.*?)\s*</h6>', c, re.S)]
EXP = re.findall(r'<h4>\s*(.*?)\s*</h4>\s*<p>\s*(.*?)\s*</p>', c, re.S)
DOCS = re.findall(r"href='(https://bankruptcyukraine\.com/wp-content/uploads/[^']+)'><img width=\"\d+\" height=\"\d+\" src=\"([^\"]+)\"", c)
PH = "https://bankruptcyukraine.com/wp-content/uploads/2025/07/bondar-oleh-oleksiiovych-yuryst-po-kredytam.jpg"
FB = re.search(r'href="(https://www\.facebook\.com[^"]+)"', c).group(1); IG = "https://www.instagram.com/oleg_adwokat/"
CSS_SITE = """<style>
.kv .hero{padding:140px 0 90px}.kv .hero .soc{margin-top:26px;display:flex;gap:18px;font:700 13px/1 'Roboto Condensed',sans-serif;letter-spacing:.1em;text-transform:uppercase}
.kv .hero .soc a{color:#FFE16A;border-bottom:1px solid #FFE16A;padding-bottom:3px}
.kv section[id]{scroll-margin-top:68px}
.kv .sec.edu{background:#fff}.kv .edu .list{max-width:860px;margin:36px auto 0;display:grid;gap:18px}
.kv .edu .it{display:flex;gap:16px;align-items:flex-start;font:700 18px/1.5 Montserrat,sans-serif;color:#222}
.kv .edu .it i{flex:none;width:26px;height:26px;border-radius:50%;background:#FFE16A;position:relative;margin-top:3px}
.kv .edu .it i::after{content:"";position:absolute;left:8px;top:4px;width:6px;height:12px;border:solid #02176D;border-width:0 3px 3px 0;transform:rotate(45deg)}
.kv .exp .grid4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px;margin-top:44px}
.kv .exp .c{background:#fff;border-radius:6px;padding:26px 24px;box-shadow:0 14px 40px rgba(2,23,109,.1)}
.kv .exp .c h4{font:800 22px/1.2 Montserrat,sans-serif;color:#02176D;margin:0 0 12px}
.kv .exp .c p{margin:0;font-size:16px;color:#4B4F58}.kv .exp .c p b{color:#222}
.kv .exp .c a{color:#02176D;border-bottom:1px solid currentColor}
.kv .cen{text-align:center;margin-top:40px}
.kv .sec.res{background:#02176D;color:#fff}.kv .sec.res h2{color:#fff}.kv .sec.res .bar{background:#FFE16A}
.kv .res-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:40px}
.kv .res-g a{background:#fff;padding:6px;border-radius:3px;display:block}.kv .res-g img{display:block;width:100%;height:auto}
.kv .sec.rev{background:#fff}.kv .rev-box{max-width:760px;margin:36px auto 0}
.kv .bl-empty{grid-column:1/-1;text-align:center;color:#4B4F58;padding:30px 10px;font-size:18px}
@media(max-width:1000px){.kv .exp .grid4{grid-template-columns:repeat(2,minmax(0,1fr))}.kv .res-g{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media(max-width:620px){.kv .exp .grid4{grid-template-columns:minmax(0,1fr)}.kv .res-g{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.kv .edu .it{font-size:16px}}
</style>"""
def pidcss(pid):
    return (f"<style>body.page-id-{pid} .entry-header,body.page-id-{pid} .ast-breadcrumbs-wrapper,body.page-id-{pid} .entry-title,body.page-id-{pid} .site-footer,body.page-id-{pid} #masthead,body.page-id-{pid} .site-header{{display:none!important}}"
            f"body.page-id-{pid} .ast-container,body.page-id-{pid} #primary,body.page-id-{pid} .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}body.page-id-{pid}{{background:#E4F7FC}}</style>")
def hdr():
    h = bd.HDR.replace(' class="cur"', '')
    return h.replace('<a href="/#reviews">Відгуки</a><a href="/blog/">Блог</a>', '<a href="/#articles">Статті</a><a href="/#reviews">Відгуки</a>')
def infos():
    out = {}
    for i, url, _ in json.load(open(bd.R / "src/index.json")):
        p, inf = bd.build(i, url, None); out[i] = inf
    return out
def home_html(pid, inf):
    edu = "".join(f'<div class="it"><i></i><span>{t}</span></div>' for t in EDU)
    exp = "".join(f'<div class="c"><h4>{a}</h4><p>{b}</p></div>' for a, b in EXP)
    res = "".join(f'<a href="{a}" target="_blank" rel="noopener"><img src="{b}" alt="Результат роботи — документ" loading="lazy"></a>' for a, b in DOCS)
    inner = (
     '<header class="hero" id="top"><div class="w"><div><h1>Бондар Олег Олексійович</h1><span class="bar"></span><p class="sub">Адвокат зі скасування судових наказів<br>та колекторських дій</p>'
     f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a>'
     f'<p class="soc"><a href="{FB}" target="_blank" rel="noopener">Facebook</a><a href="{IG}" target="_blank" rel="noopener">Instagram</a></p></div>'
     f'<div class="ph"><img src="{PH}" alt="Бондар Олег Олексійович - юрист по кредитам" width="640" height="640"></div></div></header>'
     f'<section class="sec edu pre" id="about"><div class="w"><h2>Освіта</h2><span class="bar"></span><div class="list">{edu}</div></div></section>'
     f'<section class="sec exp" id="experience"><div class="w"><h2>Досвід роботи</h2><span class="bar"></span><div class="grid4">{exp}</div>'
     f'<p class="cen"><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></p></div></section>'
     f'<section class="sec res" id="results"><div class="w"><h2>Результати роботи</h2><span class="bar"></span><div class="res-g">{res}</div></div></section>'
     '<section class="sec arts" id="articles"><div class="w"><h2>Мої статті</h2><span class="bar"></span>'
     '<p class="lead2">Пояснюю питання списання кредитних боргів, дій МФО і колекторів простою мовою: що каже закон і що варто зробити в першу чергу.</p>'
     '<div class="bl-g" id="homeBlog"></div>' + bd.blog_js("homeBlog", 3, inf) +
     '<p class="cen"><a class="btn" href="/blog/">Усі статті</a></p></div></section>'
     '<section class="sec rev" id="reviews"><div class="w"><h2>Відгуки</h2><span class="bar"></span><div class="rev-box">[react_reviews_1]</div>'
     f'<p class="cen"><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></p></div></section>')
    return "<!-- wp:html -->\n" + bd.CSS_HUB + "\n" + CSS_SITE + "\n" + pidcss(pid) + "\n" + hdr() + '<div class="kv">' + inner + bd.FTR + "</div>\n<!-- /wp:html -->"
if __name__ == "__main__":
    (R / "payload").mkdir(exist_ok=True); (R / "preview").mkdir(exist_ok=True)
    idf = R / "ids.json"; ids = json.load(open(idf)) if idf.exists() else {}
    inf = infos(); pid = ids.get("home") or 0
    (R / "preview" / "home.html").write_text(home_html(pid, inf), encoding="utf-8")
    print("edu", len(EDU), "exp", len(EXP), "docs", len(DOCS), "home id", pid)
    if "--push" in sys.argv:
        if not pid:
            r = bd.call("POST", f"{SITE}/wp-json/wp/v2/pages", {"title": "Бондар Олег Олексійович", "slug": "golovna-new", "status": "draft", "template": "elementor_canvas", "content": home_html(0, inf)})
            pid = r["id"]; ids["home"] = pid; json.dump(ids, open(idf, "w"), indent=1)
        r = bd.call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", {"content": home_html(pid, inf)})
        print("home ->", r.get("id"), r.get("status"), r.get("link"))
