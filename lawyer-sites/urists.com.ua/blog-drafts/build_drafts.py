#!/usr/bin/env python3
"""urists.com.ua: чернетки статей блогу (ключі 1-12) за шаблоном живої сторінки 54.
  python3 build_drafts.py            -> payload/NN-slug.json + preview/NN-slug.html (нічого не публікує)
  python3 build_drafts.py --create   -> створює ЧЕРНЕТКИ у WP (status=draft, parent=48); повторний запуск оновлює за збереженими id
Дати: з нового графіку (10.11 ... 04.12.2026, 09:00 Київ = 07:00 UTC). Статус publish ставиться лише за командою «публікуй».
"""
import json, re, sys, pathlib, subprocess, html
R = pathlib.Path(__file__).parent
SITE = "https://urists.com.ua"
BLOG_ID = 48
AUTHOR = "Яковенко Дмитро"
DATES = ["2026-11-10","2026-11-12","2026-11-13","2026-11-16","2026-11-18","2026-11-20","2026-11-23","2026-11-25","2026-11-27","2026-11-30","2026-12-02","2026-12-04"]
TAGS = ["Робота і борги","Права водія","Батьківські права","Колектори","Подружжя","Права боржника","Закон і суд","Особистий бюджет","Втрата роботи","Наслідки несплати","Кредит за кордоном","Позовна давність"]
TPL = (R / "template-page54.html").read_text(encoding="utf-8")
idx = json.load(open(R / "src/index.json"))

def ui(d): y,m,dd = d.split("-"); return f"{dd}.{m}.{y}"

def clean_links(body):
    # посилання на власний сайт прибираємо (лишаємо текст), зовнішні держресурси лишаємо
    def rep(m):
        href, txt = m.group(1), m.group(2)
        return m.group(0) if href.startswith("http") else txt
    return re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', rep, body, flags=re.S)

def build(i, url, h1_unused, src_file):
    k = i - 1
    date, tag = DATES[k], TAGS[k]
    src = (R / "src" / f"{i:02d}-{url}.html").read_text(encoding="utf-8")
    m = re.search(r'<b>Title:</b>\s*(.*?)<br><b>Description:</b>\s*(.*?)</p>', src, re.S)
    title, desc = m.group(1).strip(), m.group(2).strip()
    h1 = re.search(r'<h1>(.*?)</h1>', src).group(1).strip()
    body = src[src.index('</h1>') + 5:].strip().replace("[ДАТА]", ui(date))
    body = clean_links(body)
    fm = re.search(r'<h2>(?:FAQ|Питання та відповіді|Питання й відповіді|Поширені запитання|Часті запитання|Часті питання)</h2>(.*?)(?=<h2>|\Z)', body, re.S)
    faq = re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', fm.group(1), re.S) if fm else []
    body = re.sub(r'<table[^>]*>', '<table>', body)
    body = re.sub(r'<table>.*?</table>', lambda mm: '<div class="art-table">' + mm.group(0) + '</div>', body, flags=re.S)
    n = [0]
    def idrep(mm): n[0] += 1; return f'<{mm.group(1)} id="s{n[0]}">'
    body = re.sub(r'<(h2|h3)>', idrep, body)
    # excerpt: перші речення першого абзацу
    p1 = next(re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<p>(.*?)</p>', body, re.S) if not x.startswith('Автор'))
    sents = re.split(r'(?<=[.!?])(?<!ст\.)(?<!ч\.)(?<!п\.)\s+', p1)
    exc = ""
    for x in sents:
        exc = (exc + " " + x).strip()
        if len(exc) >= 120: break
    if len(exc) > 230: exc = exc[:227].rsplit(" ", 1)[0] + "…"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": h1, "description": desc, "inLanguage": "uk", "datePublished": date + "T09:00:00+02:00",
         "mainEntityOfPage": f"{SITE}/blog/{url}/", "author": {"@id": SITE + "/#person"}, "isPartOf": {"@type": "Blog", "url": SITE + "/blog/"}}]}
    if faq:
        ld["@graph"].append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub(r'<[^>]+>', '', q),
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}} for q, a in faq]})
    out = TPL
    out = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % html.escape(desc, quote=True), out, count=1)
    out = re.sub(r'(<div class="sub-body art">.*?<h1>).*?(</h1>)', lambda mm: mm.group(1) + h1 + mm.group(2), out, count=1, flags=re.S)
    out = re.sub(r'<div class="art-meta">.*?</div>', f'<div class="art-meta"><span class="art-tag">{tag}</span><time datetime="{date}">{ui(date)}</time><span>{AUTHOR}</span></div>', out, count=1, flags=re.S)
    a = out.index('<div class="art-body">'); b = out.index('</div><p class="art-back">')
    out = out[:a] + '<div class="art-body">' + body + out[b:]
    mm = re.search(r'<script type="application/ld\+json">.*?</script>', out, re.S)
    out = out[:mm.start()] + '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>' + out[mm.end():]
    assert out.count('<h1') == 1 and out.count('<p class="art-back">') == 1 and out.count('<article') == 1
    payload = {"title": h1, "slug": url, "status": "draft", "parent": BLOG_ID, "template": "page-landing",
               "content": out, "excerpt": exc, "date": date + "T07:00:00", "date_gmt": date + "T07:00:00"}
    return payload, dict(title=title, desc=desc, words=len(re.sub(r'<[^>]+>', ' ', body).split()), faq=len(faq), exc=exc)

def call(method, url, data=None):
    cmd = ["curl", "-s", "-m", "120", "-X", method, "-H", "Content-Type: application/json", url]
    if data is not None: cmd += ["--data-binary", "@-"]
    r = subprocess.run(cmd, input=(json.dumps(data, ensure_ascii=False).encode() if data is not None else None), capture_output=True)
    return json.loads(r.stdout.decode())

if __name__ == "__main__":
    (R / "payload").mkdir(exist_ok=True); (R / "preview").mkdir(exist_ok=True)
    ids_file = R / "draft-ids.json"; ids = json.load(open(ids_file)) if ids_file.exists() else {}
    for rec in idx:
        i, url = rec[0], rec[1]
        p, info = build(i, url, None, None)
        (R / "payload" / f"{i:02d}-{url}.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        (R / "preview" / f"{i:02d}-{url}.html").write_text(p["content"], encoding="utf-8")
        print(i, url, info["words"], "faq", info["faq"], "|", info["title"], "|", len(info["desc"]))
        if "--create" in sys.argv:
            if url in ids: r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{ids[url]}", p)
            else: r = call("POST", f"{SITE}/wp-json/wp/v2/pages", p)
            if "id" in r:
                ids[url] = r["id"]; print("   ->", r["id"], r["status"], r["date"], r["link"])
            else: print("   ERR", str(r)[:300])
            json.dump(ids, open(ids_file, "w"), ensure_ascii=False, indent=1)
