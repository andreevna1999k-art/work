#!/usr/bin/env python3
"""jurist-online.info: збірка 4 статей (Мельник Марія Миколаївна) у стилі хаба (кав'ярня/бежевий).
  python3 build_articles.py            -> preview/NN-slug.html (нічого не відправляє)
  python3 build_articles.py --push     -> створює/оновлює сторінки в WP (parent = хаб 2675, status future, дата 09:00 Київ)
Тексти: NN-slug/text-fixed.txt. Зображення: img/NN-slug.webp (завантажуються у медіатеку).
"""
import re, json, sys, html, pathlib, subprocess
R = pathlib.Path(__file__).parent
SITE = "https://jurist-online.info"
HUB = 2675
AUTHOR = "Мельник Марія Миколаївна"
TG = "https://t.me/maria_yrist"
ART = [
 dict(n=1, slug="yak-diznatysia-chy-vziato-na-mene-mikrozaim", date="2026-11-12", tag="Перевірка боргів",
      alt="Жінка перевіряє на телефоні й ноутбуці, чи оформлено на неї мікрозайм",
      h3=["Справа № 331/3045/21: чужі договори визнано недійсними","Справа № 757/19339/21-ц: чому споживач програв","Що зробити сьогодні"],
      tables=[("Спосіб",5,"Висновок автора:")]),
 dict(n=2, slug="shcho-robyty-iakshcho-na-tebe-oformyly-mikrozaim", date="2026-11-13", tag="Шахрайські кредити",
      alt="Чоловік уважно вивчає документи про мікрозайм за домашнім столом",
      h3=["Правова позиція: справа № 331/3045/21","Правова позиція: справа № 174/968/23"],
      tables=[("Куди",4,"Висновок юриста:")]),
 dict(n=3, slug="chy-mozhut-oformyty-kredyt-bez-moho-vidoma", date="2026-11-16", tag="Кредит без відома",
      alt="Чоловік розмовляє телефоном і робить нотатки біля вікна з вечірнім містом",
      h3=["Що каже закон","Справа, яку виграли: № 331/3045/21","Справа, яку програли: № 174/968/23","Зразок документа","Що зробити сьогодні:"],
      tables=[("Ситуація",4,"Висновок автора."),("Критерій",3,"У моїй практиці я бачила різницю")]),
 dict(n=4, slug="yak-zakhystytysia-vid-kredytnykh-shakhraiv", date="2026-11-18", tag="Захист від шахраїв",
      alt="Юрист у кабінеті з ноутбуком обмірковує захист від кредитних шахраїв",
      h3=["Копія паспорта і фото з документом","Втрачені або викрадені документи","Дзвінки «служби безпеки банку» і SMS-коди","Фейкові «помічники» з оформлення кредиту","Алгоритм дій","Які документи підготувати","Зразок заяви кредитодавцю","Чи можуть Вас притягнути за несплату такого кредиту","Якщо Ви самі ввели код із SMS","Справа № 331/3045/21: договори, укладені шахраями, визнано недійсними","Справа № 174/968/23: електронний підпис одноразовим ідентифікатором"],
      tables=[("Спосіб",5,"Висновок автора:")]),
]
for a in ART:
    nn = f"{a['n']:02d}"
    a["dir"] = next(R.glob(f"{nn}-*"))
    a["img"] = R / "img" / f"{a['dir'].name}.webp"

E = lambda s: html.escape(s, quote=False)

# ---- розбиття «склеєних» рядків (джерело: Word, де списки склеєно в абзац)
CUTS = {  # (стаття, початок рядка) -> маркери розрізу
 (1, "Суд може визнати недійсним"): ["Умовний приклад зростання боргу.", "| Період", "Розрахунок: умовна ставка"],
 (2, "Ви отримали дзвінок із вимогою"): ["Якщо кредитодавець не надає їх", "Не ведіть усних розмов", "Це не просто теорія"],
 (2, "Чим довше Ви мовчите"): ["Формула розрахунку"],
 (2, "Головна пастка"): ["У моїй практиці, коли я працювала"],
 (3, "Головна помилка — ігнорувати"): ["Як захиститися від мікрозаймів?"],
}
def explode(art_n, line):
    s = line.strip()
    for (n, st), marks in CUTS.items():
        if n == art_n and s.startswith(st):
            chunks = [s]
            for m in marks:
                nc = []
                for c in chunks:
                    if m in c and not c.startswith(m):
                        i = c.index(m); nc += [c[:i].strip(), c[i:].strip()]
                    else: nc.append(c)
                chunks = nc
            out = []
            for c in chunks:
                if c.startswith("| Період"):
                    toks = [x.strip() for x in c.split("|") if x.strip() and not x.strip().startswith(":---")]
                    rows = [toks[i:i+4] for i in range(0, len(toks), 4)]
                    out.append(("table", rows))
                elif " * " in c:
                    parts = c.split(" * ")
                    out.append(("p", parts[0].strip()))
                    out += [("li", p.strip()) for p in parts[1:]]
                else:
                    out.append(("p", c))
            return out
    return None

def steps_art1(line):
    s = line.strip()
    m = re.match(r'(.*?)\s*1\. (Крок 1\..*)', s)
    head, rest = m.group(1), m.group(2)
    parts = re.split(r'\s(?=\d\. Крок \d\.)', rest)
    steps = [re.sub(r'^\d\. ', '', p).strip() for p in parts]
    tail = ""
    i = steps[-1].find("У моїй практиці")
    if i > 0: tail = steps[-1][i:].strip(); steps[-1] = steps[-1][:i].strip()
    quote = ""
    q = re.search(r'Зразок вимоги: («Кому:.*?\[Підпис\]»)', steps[2])
    if q:
        quote = q.group(1); steps[2] = steps[2][:q.start()].strip()
    return head, steps, quote, tail

def parse(a):
    raw = (a["dir"] / "text-fixed.txt").read_text(encoding="utf-8").replace(" ", " ")
    lines = raw.split("\n")
    # перейменувати дубль заголовка
    toc = []
    i = next(k for k, l in enumerate(lines) if l.strip() == "Зміст")
    j = i + 1
    while re.match(r'^\s+\d+\.\s', lines[j]):
        toc.append(re.sub(r'^\s+\d+\.\s+', '', lines[j]).strip()); j += 1
    title = lines[0].split(":", 1)[1].strip(); desc = lines[1].split(":", 1)[1].strip()
    h1 = lines[2].strip()
    intro = [l.strip() for l in lines[3:i] if l.strip()]
    body = lines[j:]
    # дубль «Висновок…» → останній стає «Підсумок»
    names = set(toc)
    idxs = [k for k, l in enumerate(body) if l.strip() in names]
    seen = {}
    for k in idxs:
        seen.setdefault(body[k].strip(), []).append(k)
    for nm, ks in seen.items():
        if len(ks) > 1 and "Підсумок" in names: body[ks[-1]] = "Підсумок"
    blocks = []   # (kind, data)
    h2set = set(toc) | {"Підсумок"}
    h3set = set(a["h3"])
    in_faq = False; in_quote = False
    tabs = list(a["tables"])
    k = 0
    while k < len(body):
        l = body[k]; s = l.strip()
        if not s: k += 1; continue
        if s in h2set:
            in_faq = (s == "FAQ"); in_quote = False
            blocks.append(("h2", s)); k += 1; continue
        # таблиця
        hit = next((t for t in tabs if s == t[0] and k + 1 < len(body)), None)
        if hit:
            first, nc, end = hit
            cells = []; k2 = k
            while k2 < len(body) and not body[k2].strip().startswith(end):
                if body[k2].strip(): cells.append(body[k2].strip())
                k2 += 1
            rows = [cells[x:x+nc] for x in range(0, len(cells), nc)]
            blocks.append(("table", rows)); tabs.remove(hit); k = k2; continue
        if s in h3set:
            in_quote = (s == "Зразок заяви кредитодавцю")
            blocks.append(("h3", s.rstrip(":"))); k += 1; continue
        if a["n"] == 2 and re.match(r'^Крок \d\.', s) and not l.startswith(" "):
            blocks.append(("h3", s)); k += 1; continue
        if in_faq and s.endswith("?") and len(s) < 140:
            blocks.append(("h3", s)); k += 1; continue
        ex = explode(a["n"], l)
        if ex:
            for kind, d in ex: blocks.append((kind, d))
            k += 1; continue
        if a["n"] == 1 and s.startswith("Щоб дізнатися, чи взято на мене мікрозайм, дійте за п"):
            head, steps, quote, tail = steps_art1(l)
            blocks.append(("p", head)); blocks.append(("ol", steps[:3]))
            if quote: blocks.append(("quote", [quote]))
            blocks.append(("ol4", steps[3:]))
            if tail: blocks.append(("p", tail))
            k += 1; continue
        m = re.match(r'^\s+[•◦]\s+(.*)$', l)
        if m: blocks.append(("li", m.group(1).strip())); k += 1; continue
        m = re.match(r'^\s+(\d+)\.\s+(.*)$', l)
        if m: blocks.append(("oli", m.group(2).strip())); k += 1; continue
        if in_quote: blocks.append(("qline", s)); k += 1; continue
        blocks.append(("p", s)); k += 1
    return dict(title=title, desc=desc, h1=h1, intro=intro, toc=toc, blocks=blocks)

def render(a, P, img_url=None, pid=None):
    slug = a["slug"]; out = []; sid = 0
    ids = {}
    def close_list():
        pass
    out_blocks = []
    cur = None
    for kind, d in P["blocks"]:
        if kind in ("li", "oli"):
            tag = "ul" if kind == "li" else "ol"
            if cur and cur[0] == tag: cur[1].append(d)
            else:
                if cur: out_blocks.append(cur)
                cur = [tag, [d]]
            continue
        if cur: out_blocks.append(cur); cur = None
        out_blocks.append([kind, d])
    if cur: out_blocks.append(cur)
    h2n = 0
    faq = []; lastq = None
    for kind, d in out_blocks:
        if kind == "h2":
            h2n += 1; ids[d] = f"s{h2n}"; out.append(f'<h2 id="s{h2n}">{E(d)}</h2>')
        elif kind == "h3": out.append(f"<h3>{E(d)}</h3>")
        elif kind == "p": out.append(f"<p>{E(d)}</p>")
        elif kind == "ul": out.append("<ul>" + "".join(f"<li>{E(x)}</li>" for x in d) + "</ul>")
        elif kind == "ol":
            cls = ' class="st"' if all(x.startswith("Крок") for x in d) else ""
            out.append(f"<ol{cls}>" + "".join(f"<li>{E(x)}</li>" for x in d) + "</ol>")
        elif kind == "ol4": out.append('<ol class="st" start="4">' + "".join(f"<li>{E(x)}</li>" for x in d) + "</ol>")
        elif kind == "quote": out.append('<blockquote><p>' + "<br>".join(E(x) for x in d) + "</p></blockquote>")
        elif kind == "qline": out.append(f'<p class="ql">{E(d)}</p>')
        elif kind == "table":
            rows = d
            t = "<div class='tw'><table><thead><tr>" + "".join(f"<th>{E(c)}</th>" for c in rows[0]) + "</tr></thead><tbody>"
            for r in rows[1:]: t += "<tr>" + "".join(f"<td>{E(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table></div>")
    body = "\n".join(out)
    # qline-и в одну цитату
    body = re.sub(r'((?:<p class="ql">.*?</p>\n?)+)', lambda m: '<blockquote>' + m.group(1).replace(' class="ql"', '') + '</blockquote>\n', body, flags=re.S)
    # FAQ з блоків
    faq = []
    inf = False
    for kind, d in out_blocks:
        if kind == "h2": inf = (d == "FAQ"); continue
        if inf and kind == "h3": lastq = d
        elif inf and kind == "p" and lastq: faq.append((lastq, d)); lastq = None
    toc = "".join(f'<li><a href="#{ids[t]}">{E(t)}</a></li>' for t in P["toc"] if t in ids)
    intro = "".join(f"<p>{E(x)}</p>" for x in P["intro"])
    fig = ""
    if img_url:
        fig = f'<figure class="fig"><img src="{img_url}" alt="{html.escape(a["alt"], quote=True)}" width="1200" height="800" loading="lazy" decoding="async"></figure>'
    ui = a["date"][8:] + "." + a["date"][5:7] + "." + a["date"][:4]
    url = f"{SITE}/blog/{slug}/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": P["h1"], "description": P["desc"], "inLanguage": "uk", "datePublished": a["date"] + "T09:00:00+02:00",
         "mainEntityOfPage": url, "author": {"@type": "Person", "name": AUTHOR, "url": SITE + "/"}, **({"image": img_url} if img_url else {})},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Головна", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Блог", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": P["h1"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in faq]}]}
    ldj = json.dumps(ld, ensure_ascii=False).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    css = CSS.replace("__PID__", str(pid or 0))
    page = f"""<!-- wp:html -->
<meta name="description" content="{html.escape(P['desc'], quote=True)}">
<style>
{css}
</style>
{HEADER}
<div class="kv"><header class="ah"><div class="w"><p class="crumbs"><a href="/">Головна</a> · <a href="/blog/">Блог</a></p><h1>{E(P['h1'])}</h1><span class="bar"></span><p class="meta"><span class="tag">{E(a['tag'])}</span><time datetime="{a['date']}">{ui}</time><span>{AUTHOR}</span></p></div></header>
<main class="art"><div class="w"><article>
<div class="intro">{intro}</div>
{fig}
<nav class="toc" aria-label="Зміст"><p class="toc-t">Зміст</p><ol>{toc}</ol></nav>
{body}
<p class="cta-box"><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a></p>
<p class="back"><a href="/blog/">← Усі статті блогу</a></p>
</article></div></main>
{FOOTER}</div>
<script type="application/ld+json">{ldj}</script>
<!-- /wp:html -->"""
    return page, dict(words=len(re.sub(r"<[^>]+>", " ", body).split()), faq=len(faq))

hub = (R.parent / "site-drafts" / "hub-2675.html").read_text(encoding="utf-8")
CSS_HUB = hub[hub.index("<style>") + 7: hub.index("</style>")]
CSS_HUB = CSS_HUB.replace("page-id-2675", "page-id-__PID__")
HEADER = hub[hub.index('<div class="kvh">'): hub.index('<div class="kv">')]
FOOTER = hub[hub.index('<footer class="ft"'): hub.index("</footer>") + 9]
ART_CSS = """
.kv .ah{background:linear-gradient(90deg,#FCE8CF 0 50%,#FFF6EA 50% 100%);padding:130px 0 50px;color:#2E1700}
.kv .ah .w{max-width:900px}
.kv .ah h1{font-size:clamp(28px,4vw,44px);color:#2E1700;margin-top:10px}
.kv .crumbs{font:700 13px/1.4 'DM Sans',sans-serif;letter-spacing:.04em;color:#8A5A2B}.kv .crumbs a:hover{color:#B56A00}
.kv .ah .meta{margin-top:20px;display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;font:700 13px/1 'DM Sans',sans-serif;color:#8A5A2B}
.kv .ah .meta .tag{padding:6px 12px;background:#FFA500;color:#2E1700;letter-spacing:.1em;text-transform:uppercase;font-size:11px}
.kv .art{background:#FBF5F1;padding:48px 0 90px}
.kv .art .w{max-width:820px}
.kv .art p{margin:0 0 16px;color:#4A3322;font-size:17px;line-height:1.7}
.kv .art h2{font-size:clamp(24px,3vw,32px);margin:46px 0 16px;color:#2E1700;text-align:left}
.kv .art h3{font-size:21px;margin:30px 0 12px;color:#2E1700}
.kv .art ul,.kv .art ol{margin:0 0 20px 24px;padding:0}.kv .art ul{list-style:disc}.kv .art ol{list-style:decimal}
.kv .art ol.st{list-style:none;margin-left:0}
.kv .art li{margin:0 0 9px;color:#4A3322;font-size:17px;line-height:1.65}
.kv .art .toc{background:#fff;border-radius:16px;padding:22px 26px 10px;margin:26px 0 34px;box-shadow:0 10px 30px rgba(102,51,0,.1)}
.kv .art .toc-t{font:600 20px/1.2 Jost,sans-serif;color:#2E1700;margin:0 0 12px}
.kv .art .toc ol{margin:0 0 12px 22px}.kv .art .toc a{color:#663300;border-bottom:1px solid rgba(102,51,0,.3)}.kv .art .toc a:hover{color:#B56A00}
.kv .art .fig{margin:28px 0}.kv .art .fig img{display:block;width:100%;height:auto;border-radius:20px;box-shadow:0 14px 40px rgba(102,51,0,.16)}
.kv .art .tw{overflow-x:auto;margin:0 0 22px}
.kv .art table{border-collapse:collapse;width:100%;min-width:560px;background:#fff;font-size:15px;line-height:1.5}
.kv .art th,.kv .art td{border:1px solid #E6D6C4;padding:10px 12px;text-align:left;vertical-align:top;color:#4A3322}
.kv .art th{background:#FCE8CF;color:#2E1700;font-weight:700}
.kv .art blockquote{margin:0 0 20px;padding:16px 22px;background:#fff;border-left:4px solid #FFA500;border-radius:8px}
.kv .art blockquote p{margin:0 0 6px;font-size:16px}
.kv .art .cta-box{text-align:center;margin:40px 0 20px}
.kv .art .cta-box .btn{color:#fff}
.kv .art .back a{font:700 13px/1 'DM Sans',sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#663300}
@media(max-width:900px){.kv .ah{background:linear-gradient(180deg,#FCE8CF 0 64%,#FFF6EA 64% 100%);padding:110px 0 36px}}
@media(max-width:620px){.kv .art p,.kv .art li{font-size:16px}}
"""
CSS = CSS_HUB + ART_CSS

def main():
    push = "--push" in sys.argv
    (R / "preview").mkdir(exist_ok=True)
    meta = json.load(open(R / "wp-ids.json")) if (R / "wp-ids.json").exists() else {}
    for a in ART:
        P = parse(a)
        key = a["slug"]
        info = meta.get(key, {})
        page, st = render(a, P, img_url=info.get("img_url"), pid=info.get("id"))
        (R / "preview" / f"{a['n']:02d}-{a['slug']}.html").write_text(page, encoding="utf-8")
        print(a["n"], a["slug"], "words", st["words"], "faq", st["faq"], "img", bool(info.get("img_url")), "id", info.get("id"))
        a["_page"] = page; a["_P"] = P
    if push:
        sys.path.insert(0, str(R))
        import wp_push
        wp_push.run(ART, meta, render, R)

if __name__ == "__main__":
    main()
