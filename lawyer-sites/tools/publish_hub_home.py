#!/usr/bin/env python3
"""Публікує хаб `blog` і нову головну (з блоком «Мої статті») для сайту юриста, у якого вже є чернетки-макети.
  python3 publish_hub_home.py <домен> <hub_id> <home_draft_id> <live_front_id> [--apply]
Без --apply нічого не змінює (лише перевірки і prepared/ у scratch). Кроки з --apply:
 1) бекап: жива головна, чернетка головної, чернетка хабу -> <домен>/site-drafts/backup-live/
 2) у макетах хабу і головної заглушки-картки замінюються на динамічний блок (REST /pages?parent=<hub>, лише опубліковані дочірні сторінки)
 3) хаб -> publish; чернетка головної -> publish (slug golovna), page_on_front = чернетка, стара головна -> draft
"""
import json, re, sys, subprocess, pathlib, datetime
SITE_DIR = pathlib.Path(__file__).resolve().parent.parent
site, HUB, HOMED, FRONT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
APPLY = "--apply" in sys.argv
PATCH = "--patch-scripts" in sys.argv
import os
INC_ENV = os.environ.get("LEGACY_IDS", "")
BASE = f"https://{site}"
def call(method, path, data=None):
    cmd = ["curl", "-s", "-m", "150", "-X", method, f"{BASE}/wp-json/wp/v2/{path}"]
    if data is not None: cmd += ["-H", "Content-Type: application/json", "--data-binary", "@-"]
    r = subprocess.run(cmd, input=json.dumps(data, ensure_ascii=False).encode() if data is not None else None, capture_output=True)
    try: return json.loads(r.stdout.decode())
    except Exception: return {"raw": r.stdout.decode()[:200]}

JS = r'''(function(){var A=String.fromCharCode(38);var g=document.getElementById("%(gid)s");if(!g)return;var LIM=%(lim)d,PID=%(hub)d,INC="%(inc)s";
function T(s){var d=document.createElement("div");d.innerHTML=s;return(d.textContent||"").replace(/\s+/g," ").trim()}
function D(s){var p=String(s).slice(0,10).split("-");return p[2]+"."+p[1]+"."+p[0]}
function E(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
function card(x){var u=new URL(x.link,location.href).pathname,ti=T(x.title.rendered),ex=T((x.excerpt?x.excerpt.rendered:"")||"");if(ex.indexOf(ti)===0)ex=ex.slice(ti.length).trim();ex=ex.replace(/\s*\[…\]\s*$/,"");if(ex.length>230){ex=ex.slice(0,227).replace(/\s+\S*$/,"")+"…"}var art=E("article","bl-card"),cv=E("a","bl-cover");cv.href=u;cv.tabIndex=-1;
var fm=x._embedded&&x._embedded["wp:featuredmedia"]&&x._embedded["wp:featuredmedia"][0];if(fm&&fm.source_url){var im=new Image();im.src=fm.source_url;im.alt=ti;im.width=640;im.height=427;im.loading="lazy";cv.appendChild(im)}
cv.appendChild(E("span","bl-tag","Стаття"));art.appendChild(cv);var b=E("div","bl-body"),tm=E("time",null,D(x.date));tm.setAttribute("datetime",String(x.date).slice(0,10));b.appendChild(tm);
var h=E("h3"),l=E("a",null,ti);l.href=u;l.style.color="inherit";h.appendChild(l);b.appendChild(h);b.appendChild(E("p",null,ex));var mr=E("a","bl-more","Читати статтю");mr.href=u;b.appendChild(mr);art.appendChild(b);g.appendChild(art)}
function empty(){g.appendChild(E("p","bl-empty","Перші статті з’являться найближчим часом."))}
var F="_embed=wp:featuredmedia"+A+"_fields=id,date,link,slug,title,excerpt,_embedded";
function J(u){return fetch(u,{credentials:"omit"}).then(function(r){if(!r.ok)throw 0;return r.json()})}
Promise.all([J("/wp-json/wp/v2/pages?parent="+PID+A+"per_page=100"+A+F),INC?J("/wp-json/wp/v2/pages?include="+INC+A+"per_page=100"+A+F).catch(function(){return[]}):Promise.resolve([])]).then(function(r){var m={},a=[];r[0].concat(r[1]).forEach(function(x){if(!m[x.id]){m[x.id]=1;a.push(x)}});
if(!a.length){empty();return}a.sort(function(p,q){return String(q.date).localeCompare(String(p.date))});a.slice(0,LIM).forEach(card)}).catch(empty)})();'''
GRID = re.compile(r'<div class="bl-g">(?:<article.*?</article>)+</div>', re.S)
EMPTY_CSS = ".kv .bl-empty{grid-column:1/-1;text-align:center;opacity:.8;padding:30px 10px;font-size:18px}"
INC = INC_ENV
def dyn(html, gid, lim):
    if ".kv .bl-empty" not in html: html = html.replace("</style>", EMPTY_CSS + "\n</style>", 1)
    js = "<script>" + JS % dict(gid=gid, lim=lim, hub=HUB, inc=INC) + "</script>"
    n = len(GRID.findall(html))
    assert n == 1, f"очікувалась 1 сітка карток, знайдено {n}"
    html = GRID.sub(lambda m: f'<div class="bl-g" id="{gid}"></div>' + js, html, count=1)
    return html
def find(nodes, i):
    for e in nodes:
        if e.get("id") == i: return e
        r = find(e.get("elements", []), i)
        if r: return r

live = call("GET", f"pages/{FRONT}?context=edit"); hubd = call("GET", f"pages/{HUB}?context=edit"); homed = call("GET", f"pages/{HOMED}?context=edit")
for n, d in (("live", live), ("hub", hubd), ("homedraft", homed)):
    assert "id" in d, (n, d)
print("live:", live["id"], live["status"], live["slug"][:30], "|", live["title"]["raw"]); print("hub:", hubd["id"], hubd["status"], hubd["slug"], hubd["template"], len(hubd["content"]["raw"])); print("home draft:", homed["id"], homed["status"], homed["template"])
# перевірка: чернетка головної = жива головна + додані контейнери
ed_live = json.loads(live["meta"]["_elementor_data"]); ed_dr = json.loads(homed["meta"]["_elementor_data"])
ADDED = {"kvhdr01", "kvblk01", "kvanc01"}
def strip_ids(nodes):
    for e in nodes:
        if e.get("settings") == []: e["settings"] = {}
        if isinstance(e.get("settings"), dict): e["settings"].pop("_element_id", None)
        strip_ids(e.get("elements", []))
    return nodes
base_dr = strip_ids(json.loads(json.dumps([e for e in ed_dr if e.get("id") not in ADDED])))
same = json.dumps(base_dr, sort_keys=True) == json.dumps(strip_ids(json.loads(json.dumps(ed_live))), sort_keys=True)
print("чернетка = жива + додані (header/block/anchors):", same, "| контейнерів live/draft:", len(ed_live), len(ed_dr))
blk = find(ed_dr, "kvblk01w") or find(ed_dr, "kvblk02w"); assert blk or PATCH, "немає kvblk01w"
SCRIPT_RE = re.compile(r'<script>\(function\(\)\{var A=String.fromCharCode\(38\);var g=document.getElementById\("(blogGrid|homeBlog)"\).*?\}\)\(\);</script>', re.S)
def repl_scripts(html):
    def f(m):
        gid = m.group(1); return "<script>" + JS % dict(gid=gid, lim=(100 if gid == "blogGrid" else 3), hub=HUB, inc=INC) + "</script>"
    new, n = SCRIPT_RE.subn(f, html); return new, n
if PATCH:
    h, n1 = repl_scripts(hubd["content"]["raw"]); assert n1 == 1, n1
    r = call("POST", f"pages/{HUB}", {"content": h}); print("hub script ->", r.get("id"), r.get("status"))
    cur = json.loads(homed["meta"]["_elementor_data"]); cnt = [0]
    def walk(nodes):
        for e in nodes:
            st = e.get("settings")
            if isinstance(st, dict) and st.get("html") and "homeBlog" in st["html"]:
                st["html"], n = repl_scripts(st["html"]); cnt[0] += n
            walk(e.get("elements", []))
    walk(cur); assert cnt[0] == 1, cnt
    r = call("POST", f"pages/{HOMED}", {"meta": {"_elementor_data": json.dumps(cur, ensure_ascii=True, separators=(",", ":"))}}); print("home script ->", r.get("id"), str(r.get("code", ""))[:60])
    print("elementor cache ->", subprocess.run(["curl", "-s", "-X", "DELETE", f"{BASE}/wp-json/elementor/v1/cache"], capture_output=True).stdout.decode()[:60]); sys.exit()
if not APPLY:
    html = dyn(blk["settings"]["html"], "homeBlog", 3); print("dyn home OK", len(html))
    dyn(hubd["content"]["raw"], "blogGrid", 100); print("dyn hub OK"); sys.exit()
assert same, "жива головна відрізняється від основи чернетки -- зупиняюсь"
bk = SITE_DIR / site / "site-drafts" / "backup-live"; bk.mkdir(parents=True, exist_ok=True)
for n, d in (("live-home", live), ("home-draft", homed), ("hub-draft", hubd)):
    (bk / f"{n}-{d['id']}.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
# хаб
if 'id="blogGrid"' in hubd["content"]["raw"] and hubd["status"] == "publish": print("hub already done")
else:
  hub_html = dyn(hubd["content"]["raw"], "blogGrid", 100)
  name = re.sub(r"^Блог — |\s*\(хаб.*$", "", hubd["title"]["raw"]).strip()
  r = call("POST", f"pages/{HUB}", {"content": hub_html, "title": "Мої статті", "status": "publish"})
  print("hub ->", r.get("id"), r.get("status"), r.get("link"), str(r.get("code", ""))[:60])
  for k, v in (("_yoast_wpseo_title", f"Блог — {name}: статті"), ("_yoast_wpseo_metadesc", f"Статті юриста {name}: пояснення простою мовою, що каже закон і що робити.")):
    call("POST", f"pages/{HUB}", {"meta": {k: v}})
# головна (якщо жива головна вже має slug golovna/home -- звільняємо slug)
if live["slug"] in ("golovna", "home"):
    r = call("POST", f"pages/{FRONT}", {"slug": live["slug"] + "-old", "status": "draft"}); print("old slug ->", r.get("slug"), r.get("status"))
blk["settings"]["html"] = dyn(blk["settings"]["html"], "homeBlog", 3)
ed_new = json.dumps(ed_dr, ensure_ascii=True, separators=(",", ":"))
r = call("POST", f"pages/{HOMED}", {"title": live["title"]["raw"], "slug": "golovna", "status": "publish"}); print("home page ->", r.get("id"), r.get("status"), r.get("link"), str(r.get("code", ""))[:80])
r = call("POST", f"pages/{HOMED}", {"meta": {"_elementor_data": ed_new}}); print("home data ->", r.get("id"), str(r.get("code", ""))[:80])
chk = call("GET", f"pages/{HOMED}?context=edit")
assert "homeBlog" in chk["meta"].get("_elementor_data", ""), "дані головної НЕ оновились -- зупиняюсь, фронт-сторінку не міняю"
for k in ("_yoast_wpseo_title", "_yoast_wpseo_metadesc"):
    if live["meta"].get(k): call("POST", f"pages/{HOMED}", {"meta": {k: live["meta"][k]}})
r = call("POST", "settings", {"page_on_front": HOMED, "show_on_front": "page"}); print("front ->", r.get("page_on_front"))
r = call("POST", f"pages/{FRONT}", {"status": "draft"}); print("old home ->", r.get("id"), r.get("status"))
# Elementor кешує відрендерений вміст: без цього сторінка показує старі заглушки
r = subprocess.run(["curl", "-s", "-X", "DELETE", f"{BASE}/wp-json/elementor/v1/cache"], capture_output=True); print("elementor cache ->", r.stdout.decode()[:80])
