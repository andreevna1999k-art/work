#!/usr/bin/env python3
"""Додає гіперпосилання на закони (zakon.rada.gov.ua) і постанови (reyestr.court.gov.ua) у текст статті на сайті.
Посилання беруться з Google-документів юристів (структура посилань однакова в усіх статтях).
Не чіпає статус/дату публікації, лише поле content. Блок FAQ і зміст не посилаються (як у документах).
  python3 add_law_links.py <домен> <page_id> [--apply] [--default 9=1404-19,21=1734-19]
"""
import sys, re, json, subprocess, pathlib, html
CODES = {"ЦК": "435-15", "ЦПК": "1618-15", "КУзПБ": "2597-19", "КК": "2341-14"}
ACTS = {"Про споживче кредитування": "1734-19", "Про виконавче провадження": "1404-19", "Про доступ до судових рішень": "3262-15",
        "Про організацію формування та обігу кредитних історій": "2704-15", "Про електронну комерцію": "675-19", "Про іпотеку": "898-15"}
CASES = {"444/9519/12": 74838904, "310/11534/13-ц": 75287282, "442/5498/16-ц": 86903580, "639/858/21": 108766199, "909/1028/20": 98812420,
         "342/180/17": 82998244, "331/3045/21": 114928833, "757/19339/21-ц": 111613920, "174/968/23": 124143546,
         "310/11024/15-ц": 82703516, "361/4481/19": 110111441, "523/10225/15-ц": 81691871}
law = lambda i: f"https://zakon.rada.gov.ua/laws/show/{i}#Text"
site, pid = sys.argv[1], sys.argv[2]
APPLY = "--apply" in sys.argv
DEF = {}
if "--default" in sys.argv:
    for kv in sys.argv[sys.argv.index("--default") + 1].split(","):
        k, v = kv.split("="); DEF[k] = v
ART = r'(?:ч\. ?\d+ )?(?:[Сс]т\.|[Сс]татт(?:я|і|ею|ях)) ?\d+(?:-\d+)?(?: ч\. ?\d+)?(?: (?:і|та) \d+)?'
MASTER = re.compile(
    rf'(?P<code>{ART} (?P<c>ЦК|ЦПК|КУзПБ|КК)(?: України)?)'
    rf'|(?P<actart>{ART} Закон(?:у|ом)? «(?P<an>Про [^»]+)»)'
    rf'|(?P<act>Закон(?:у|ом)? «(?P<an2>Про [^»]+)»)'
    rf'|(?P<zak>{ART} Закону)'
    rf'|(?P<case>№ (?P<cn>\d+/\d+/\d+(?:-ц)?))'
    rf'|(?P<bare>{ART})(?![\w])')
cnt = {"n": 0}
def a(url, text): cnt["n"] += 1; return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
def sub(m):
    t = m.group(0)
    if m.group("code"): return a(law(CODES[m.group("c")]), t)
    if m.group("actart"):
        i = ACTS.get(m.group("an")); return a(law(i), t) if i else t
    if m.group("act"):
        i = ACTS.get(m.group("an2")); return a(law(i), t) if i else t
    if m.group("zak"):
        num = re.search(r'\d+', t).group(0); i = DEF.get(num); return a(law(i), t) if i else t
    if m.group("case"):
        i = CASES.get(m.group("cn")); return a(f"https://reyestr.court.gov.ua/Review/{i}", t) if i else t
    if m.group("bare"):
        num = re.search(r'\d+', t).group(0); i = DEF.get(num); return a(law(i), t) if i else t
    return t
def curl(path, data=None):
    cmd = ["curl", "-s", "-m", "120", f"https://{site}/wp-json/wp/v2/pages/{pid}{path}"]
    if data is not None: cmd += ["-X", "POST", "-H", "Content-Type: application/json", "--data-binary", "@-"]
    r = subprocess.run(cmd, input=json.dumps(data, ensure_ascii=False).encode() if data is not None else None, capture_output=True)
    t = r.stdout.decode(); return json.loads(t[t.find("{"):])
d = curl("?context=edit&_fields=id,status,date,content")
raw = d["content"]["raw"]
pathlib.Path(f"/tmp/claude-0/linkbak/{site}-{pid}.html").write_text(raw, encoding="utf-8")
if 'rel="noopener">№' in raw or "zakon.rada.gov.ua/laws/show" in raw.split('<script type="application/ld+json">')[0].split('<div class="art-body">')[-1]:
    print(site, pid, "вже має посилання, пропускаю"); sys.exit()
bs = raw.find('<div class="art-body">'); s = raw.find("</nav>", bs) + 6
fm = re.search(r'<h2 id="s\d+">FAQ</h2>', raw); e = fm.start() if fm else raw.find('<p class="art-back">')
seg = raw[s:e]
parts = re.split(r'(<[^>]+>)', seg); out = []; skip = 0
for p in parts:
    if p.startswith("<"):
        if re.match(r'<(a|script|style)\b', p): skip += 1
        elif re.match(r'</(a|script|style)>', p): skip -= 1
        out.append(p)
    else:
        out.append(p if skip else MASTER.sub(sub, p))
new = raw[:s] + "".join(out) + raw[e:]
print(site, pid, d["status"], d["date"], "посилань:", cnt["n"], "| FAQ виключено:", bool(fm))
if APPLY:
    r = curl("", {"content": new}); print("  ->", r.get("id"), r.get("status"), r.get("date"))
else:
    ex = re.findall(r'<a href="[^"]+" target="_blank" rel="noopener">[^<]+</a>', new)
    for x in ex[:4]: print("   ", x)
