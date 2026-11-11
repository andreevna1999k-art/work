#!/usr/bin/env python3
"""advokato.in.ua (Коваленко Н. О.): чернетки статей блогу 1-12 у стилі сайту (rose/peach/slate, Lato + Noto Serif) за макетом хабу (id 1818).
  python3 build_drafts.py            -> payload/, preview/ (нічого не публікує)
  python3 build_drafts.py --create   -> створює ЧЕРНЕТКИ (status=draft, parent=1818, template elementor_canvas); повторний запуск оновлює за draft-ids.json
Публікація (status publish/future) -- лише за командою «публікуй». Авторизацію додає проксі середовища.
"""
import json, re, sys, pathlib, subprocess, html
R = pathlib.Path(__file__).parent
SITE = "https://advokato.in.ua"
HUB_ID = 1818
AUTHOR = "Коваленко Наталія Олександрівна"
DATES = ["2026-11-11","2026-11-12","2026-11-13","2026-11-16","2026-11-18","2026-11-20","2026-11-23","2026-11-25","2026-11-27","2026-11-30","2026-12-02","2026-12-04"]
TAGS = ["Банкрутство","Банкрутство","Банкрутство","Колектори","Колектори","Колектори","Колектори","Колектори","Борг","Чужий кредит","Антиколектор","Колектори"]
CSS_HUB = (R / "hub-css.html").read_text(encoding="utf-8")
CSS_HUB = re.sub(r'body\.page-id-1818[^}]*\}[^}]*\}[^<]*', '', CSS_HUB) if False else CSS_HUB
# прибираємо правила, прив'язані до id хабу
CSS_HUB = re.sub(r'body\.page-id-1818[^{]*\{[^}]*\}', '', CSS_HUB)
HDR = (R / "hub-header.html").read_text(encoding="utf-8").replace('<a href="/blog/" class="cur">', '<a href="/blog/" class="cur">')
FTR = (R / "hub-footer.html").read_text(encoding="utf-8")
CSS_ART = """<style>
.kv .ahero{background:var(--char);padding:140px 0 70px}
.kv .ahero .crumbs{font:700 12px/1 Lato,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.7)}
.kv .ahero .crumbs a{color:#fff;border-bottom:1px solid rgba(255,255,255,.4)}
.kv .ahero h1{font-size:clamp(30px,4.4vw,52px);margin-top:20px;max-width:980px}
.kv .art-sec{background:var(--slate);padding:0 0 80px}
.kv .art-card{position:relative;max-width:900px;margin:-30px auto 0;background:#fff;border-radius:22px;padding:44px 52px 48px;color:#3A3640;box-shadow:0 14px 40px rgba(0,0,0,.18)}
.kv .art-meta{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-bottom:26px;font:700 13px/1 Lato,sans-serif;letter-spacing:.06em;color:#6E6876}
.kv .art-tag{padding:6px 14px;background:var(--rose);color:#fff;font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.kv .art-meta time{color:var(--rose)}
.kv .art-body{font-size:17px;line-height:1.7;color:#3A3640}
.kv .art-body p{margin:0 0 16px}
.kv .art-body h2{font-size:clamp(25px,3vw,32px);color:var(--ink);margin:40px 0 14px}
.kv .art-body h3{font-size:clamp(20px,2.4vw,23px);color:var(--ink);margin:28px 0 10px}
.kv .art-body ul,.kv .art-body ol{margin:0 0 18px;padding-left:24px}
.kv .art-body ul{list-style:disc}.kv .art-body ol{list-style:decimal}
.kv .art-body li{margin:0 0 8px;padding-left:4px}
.kv .art-body a{color:var(--rose);border-bottom:1px solid currentColor}
.kv .art-table{overflow-x:auto;margin:22px 0;border-radius:14px;border:1px solid #E7DFE0}
.kv .art-body table{width:100%;border-collapse:collapse;font-size:15px;min-width:560px}
.kv .art-body th{background:var(--rose);color:#fff;text-align:left;padding:12px 14px;font-weight:700}
.kv .art-body td{padding:12px 14px;border-top:1px solid #EEE6E7;vertical-align:top;color:#4A4650}
.kv .art-body tr:nth-child(even) td{background:#FBF6F3}
.kv .art-fig{margin:30px 0}.kv .art-fig img{width:100%;height:auto;display:block;border-radius:18px}
.kv .art-back{margin-top:34px;padding-top:22px;border-top:1px solid #E7DFE0;font:700 13px/1 Lato,sans-serif;letter-spacing:.1em;text-transform:uppercase}
.kv .art-back a{color:var(--ink)}.kv .art-back a:hover{color:var(--rose)}
.kv .cta-band{background:var(--rose);padding:64px 0;text-align:center}
.kv .cta-band h2{font-size:clamp(26px,3.4vw,40px)}
.kv .cta-band p{max-width:620px;margin:16px auto 0;color:#fff}
.kv .cta-band .btn{margin-top:28px}
@media(max-width:700px){.kv .art-card{padding:30px 20px 34px;margin-top:-20px;border-radius:18px}.kv .ahero{padding:110px 0 56px}.kv .art-body{font-size:16px}}
</style>"""

import base64
ALTS = json.load(open(R / "image-alts.json")) if (R / "image-alts.json").exists() else {}
IMAGES = {}
for _n, _alt in ALTS.items():
    _p = R / "img" / f"{_n}.webp"
    if _p.exists(): IMAGES[int(_n)] = {"src": "data:image/webp;base64," + base64.b64encode(_p.read_bytes()).decode(), "alt": _alt}

def ui(d): y, m, dd = d.split("-"); return f"{dd}.{m}.{y}"

def clean(body, date):
    body = body.replace("[ДАТА]", ui(date))
    body = re.sub(r'</?(strong|b)>', '', body)               # ТЗ: без жирного
    body = re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', lambda m: m.group(0) if m.group(1).startswith("http") else m.group(2), body, flags=re.S)
    body = re.sub(r'<table[^>]*>', '<table>', body)
    body = re.sub(r'<table>.*?</table>', lambda m: '<div class="art-table">' + re.sub(r'\s*\n\s*', '', m.group(0)) + '</div>', body, flags=re.S)
    n = [0]
    def idr(m): n[0] += 1; return f'<{m.group(1)} id="s{n[0]}">'
    return re.sub(r'<(h2|h3)>', idr, body)

def page_html(i, url, pid, date, tag, h1, desc, body, ld):
    pidcss = (f"<style>body.page-id-{pid} .entry-header,body.page-id-{pid} .ast-breadcrumbs-wrapper,body.page-id-{pid} .entry-title,body.page-id-{pid} .site-footer{{display:none!important}}"
              f"body.page-id-{pid} .ast-container,body.page-id-{pid} #primary,body.page-id-{pid} .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}body.page-id-{pid}{{background:#615C68}}</style>") if pid else ""
    return ("<!-- wp:html -->\n" + f'<meta name="description" content="{html.escape(desc, quote=True)}">\n' + CSS_HUB + "\n" + CSS_ART + "\n" + pidcss + "\n" + HDR +
        '<div class="kv"><header class="ahero"><div class="w"><p class="crumbs"><a href="/">Головна</a> / <a href="/blog/">Блог</a></p>'
        f'<h1>{h1}</h1><span class="bar"></span></div></header>'
        f'<section class="art-sec"><div class="w"><article class="art-card"><div class="art-meta"><span class="art-tag">{tag}</span><time datetime="{date}">{ui(date)}</time><span>{AUTHOR}</span></div>'
        f'<div class="art-body">{body}</div><p class="art-back"><a href="/blog/">← Усі статті блогу</a></p></article></div></section>'
        '<section class="cta-band"><div class="w"><h2>Потрібна консультація юриста?</h2><p>Опишіть ситуацію в Telegram: підкажу перші кроки та скажу, чи потрібне представництво.</p>'
        '<a class="btn" href="https://t.me/yrist_kovalenko" target="_blank" rel="noopener">Безкоштовна консультація</a></div></section>'
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
        body = body.replace('<h2 id="s1">', f + '\n<h2 id="s1">', 1)
    content = page_html(i, url, pid, date, tag, h1, desc, body, ld)
    payload = {"title": h1, "slug": url, "status": "draft", "parent": HUB_ID, "template": "elementor_canvas",
               "content": content, "excerpt": exc, "date": date + "T09:00:00"}
    return payload, dict(title=title, desc=desc, words=len(re.sub(r'<[^>]+>', ' ', body).split()), faq=len(faq))

def call(method, url, data=None):
    cmd = ["curl", "-s", "-m", "120", "-X", method, "-H", "Content-Type: application/json", url]
    if data is not None: cmd += ["--data-binary", "@-"]
    r = subprocess.run(cmd, input=(json.dumps(data, ensure_ascii=False).encode() if data is not None else None), capture_output=True)
    return json.loads(r.stdout.decode())

if __name__ == "__main__":
    (R / "payload").mkdir(exist_ok=True); (R / "preview").mkdir(exist_ok=True)
    idf = R / "draft-ids.json"; ids = json.load(open(idf)) if idf.exists() else {}
    idx = json.load(open(R / "src/index.json"))
    for i, url, _ in idx:
        p, info = build(i, url, ids.get(url))
        (R / "payload" / f"{i:02d}-{url}.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        (R / "preview" / f"{i:02d}-{url}.html").write_text(p["content"], encoding="utf-8")
        print(i, url, info["words"], "faq", info["faq"], "|", info["title"][:60], "|", len(info["desc"]))
        if "--create" in sys.argv:
            if url not in ids:
                r = call("POST", f"{SITE}/wp-json/wp/v2/pages", p)
                if "id" not in r: print("   ERR", str(r)[:300]); continue
                ids[url] = r["id"]; json.dump(ids, open(idf, "w"), ensure_ascii=False, indent=1)
                p, _ = build(i, url, ids[url])   # вдруге вже з page-id для CSS
            r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{ids[url]}", p)
            print("   ->", r.get("id"), r.get("status"), r.get("date"), r.get("parent"), r.get("template"), str(r.get("code", ""))[:60])
