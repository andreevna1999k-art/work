#!/usr/bin/env python3
"""Додає гіперпосилання на закони (zakon.rada.gov.ua) і постанови (reyestr.court.gov.ua) у текст статті на сайті.
Посилання беруться з Google-документів юристів (структура посилань однакова в усіх статтях).
Не чіпає статус/дату публікації, лише поле content. Блок FAQ і зміст не посилаються (як у документах).
  python3 add_law_links.py <домен> <page_id> [--apply] [--default 9=1404-19,21=1734-19]
    [--only-cases] [--headings-cases] [--odb] [--force] [--custom "текст|url"]
  --odb: номери справ ведуть на court.opendatabot.ua (як у документах legaladdress), --headings-cases: лише в заголовках
"""
import sys, re, json, subprocess, pathlib, html
CODES = {"ЦК": "435-15", "ЦПК": "1618-15", "КУзПБ": "2597-19", "КК": "2341-14", "КЗпП": "322-08"}
ACTS = {"Про споживче кредитування": "1734-19", "Про виконавче провадження": "1404-19", "Про доступ до судових рішень": "3262-15",
        "Про організацію формування та обігу кредитних історій": "2704-15", "Про електронну комерцію": "675-19", "Про іпотеку": "898-15", "Про захист прав споживачів": "1023-12"}
CASES = {"444/9519/12": 74838904, "310/11534/13-ц": 75287282, "442/5498/16-ц": 86903580, "639/858/21": 108766199, "909/1028/20": 98812420,
         "342/180/17": 82998244, "331/3045/21": 114928833, "757/19339/21-ц": 111613920, "174/968/23": 124143546, "679/1103/23": 125540068,
         "310/11024/15-ц": 82703516, "361/4481/19": 110111441, "523/10225/15-ц": 81691871,
         "756/8815/20": 104728588, "910/2629/20": 91786468, "903/806/20": 105458809, "916/2372/20": 106774351}
CCU = "https://ccu.gov.ua/dokument/3-rii2023"
law = lambda i: f"https://zakon.rada.gov.ua/laws/show/{i}#Text"
LOCAL = len(sys.argv) > 2 and sys.argv[1] == "--local"   # --local <payload.json>: лінкує поле content у файлі, без сайту
site, pid = ("local", sys.argv[2]) if LOCAL else (sys.argv[1], sys.argv[2])
APPLY = "--apply" in sys.argv
ONLY_CASES = "--only-cases" in sys.argv; HEAD = "--headings-cases" in sys.argv; ODB = "--odb" in sys.argv; FORCE = "--force" in sys.argv
CUSTOM = [a.split("|") for a in sys.argv if "|" in a and a.count("|") == 1 and not a.startswith("--")]
import urllib.parse
in_head = {"v": 0}
DEF = {}
if "--default" in sys.argv:
    for kv in sys.argv[sys.argv.index("--default") + 1].split(","):
        k, v = kv.split("="); DEF[k] = v
ART = r'(?:[Чч]\. ?\d+ )?(?:[Сс]т\.|[Сс]татт(?:я|і|ею|ях)) ?\d+(?:-\d+)?(?:, ?\d+)*(?: [Чч]\. ?\d+)?(?: (?:і|та) \d+)?'
MASTER = re.compile(
    rf'(?P<code>{ART} (?P<c>ЦК|ЦПК|КУзПБ|КК|КЗпП)(?: України)?)'
    rf'|(?P<actart>{ART} Закон(?:у|ом)? «(?P<an>Про [^»]+)»)'
    rf'|(?P<act>Закон(?:у|ом)? «(?P<an2>Про [^»]+)»)'
    rf'|(?P<zak>{ART} Закону)'
    rf'|(?P<ccu>№ 3-р\(II\)/2023)'
    rf'|(?P<case>№ (?P<cn>\d+/\d+/\d+(?:-ц)?))'
    rf'|(?P<bare>{ART})(?![\w])')
cnt = {"n": 0}
def a(url, text): cnt["n"] += 1; return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
def sub(m):
    t = m.group(0)
    if ONLY_CASES and not m.group("case") and not m.group("ccu"): return t
    if m.group("code"): return a(law(CODES[m.group("c")]), t)
    if m.group("actart"):
        i = ACTS.get(m.group("an")); return a(law(i), t) if i else t
    if m.group("act"):
        i = ACTS.get(m.group("an2")); return a(law(i), t) if i else t
    if m.group("zak"):
        num = re.search(r'\d+', t).group(0); i = DEF.get(num); return a(law(i), t) if i else t
    if m.group("ccu"): return a(CCU, t)
    if ONLY_CASES and not m.group("case"): return t
    if m.group("case"):
        if HEAD and not in_head["v"]: return t
        cn = m.group("cn")
        if ODB: return a("https://court.opendatabot.ua/cause/" + urllib.parse.quote(cn.replace("-ц", ""), safe=""), t)
        i = CASES.get(cn); return a(f"https://reyestr.court.gov.ua/Review/{i}", t) if i else t
    if m.group("bare"):
        num = re.search(r'\d+', t).group(0); i = DEF.get(num); return a(law(i), t) if i else t
    return t
def curl(path, data=None):
    cmd = ["curl", "-s", "-m", "120", f"https://{site}/wp-json/wp/v2/pages/{pid}{path}"]
    if data is not None: cmd += ["-X", "POST", "-H", "Content-Type: application/json", "--data-binary", "@-"]
    r = subprocess.run(cmd, input=json.dumps(data, ensure_ascii=False).encode() if data is not None else None, capture_output=True)
    t = r.stdout.decode(); return json.loads(t[t.find("{"):])
if LOCAL:
    _pl = json.loads(pathlib.Path(pid).read_text(encoding="utf-8")); raw = _pl["content"]; d = {"status": "local", "date": "-"}
else:
    d = curl("?context=edit&_fields=id,status,date,content")
    raw = d["content"]["raw"]
    pathlib.Path(f"/tmp/claude-0/linkbak/{site}-{pid}.html").write_text(raw, encoding="utf-8")
if not FORCE and ("zakon.rada.gov.ua/laws/show" in raw.split('<script type="application/ld+json">')[0].split('<div class="art-body">')[-1]):
    print(site, pid, "вже має посилання, пропускаю"); sys.exit()
bs = raw.find('<div class="art-body">') + len('<div class="art-body">')
nv = raw.find("</nav>", bs)
s = nv + 6 if 0 <= nv - bs < 4000 else bs
fm = re.search(r'<h2[^>]*>(?:FAQ|Питання та відповіді|Питання і відповіді|Часті питання|Часті запитання)</h2>', raw[bs:])
e = bs + fm.start() if fm else raw.find('<p class="art-back">', bs)
if e < 0: e = raw.find('</article>', bs)
seg = raw[s:e]
parts = re.split(r'(<[^>]+>)', seg); out = []; skip = 0
for p in parts:
    if p.startswith("<"):
        if re.match(r'<h[23]\b', p): in_head["v"] = 1
        elif re.match(r'</h[23]>', p): in_head["v"] = 0
        if re.match(r'<(a|script|style)\b', p): skip += 1
        elif re.match(r'</(a|script|style)>', p): skip = max(0, skip - 1)
        out.append(p)
    else:
        if not skip:
            p = MASTER.sub(sub, p)
            for an, url in CUSTOM:
                if an in p and "<a " not in p: p = p.replace(an, a(url, an))
        out.append(p)
new = raw[:s] + "".join(out) + raw[e:]
print(site, pid, d["status"], d["date"], "посилань:", cnt["n"], "| FAQ виключено:", bool(fm))
if APPLY and LOCAL:
    _pl["content"] = new; pathlib.Path(pid).write_text(json.dumps(_pl, ensure_ascii=False), encoding="utf-8")
elif APPLY:
    r = curl("", {"content": new}); print("  ->", r.get("id"), r.get("status"), r.get("date"))
else:
    ex = re.findall(r'<a href="[^"]+" target="_blank" rel="noopener">[^<]+</a>', new)
    for x in ex[:4]: print("   ", x)
