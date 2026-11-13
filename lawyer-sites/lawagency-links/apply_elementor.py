#!/usr/bin/env python3
"""Те саме для сторінок на Elementor (рендер із _elementor_data): вставка widget-ів heading + text-editor перед FAQ-заголовком.
  python3 apply_elementor.py [--apply]"""
import json, re, sys, subprocess, random, copy, pathlib
from insert_links import S, get, a, b, A, U, R
APPLY = "--apply" in sys.argv
def call(m, url, data=None):
    cmd = ["curl", "-s", "-m", "180", "-A", "curl/8.5.0", "-X", m, url]; inp = None
    if data is not None: cmd += ["-H", "Content-Type: application/json", "--data-binary", "@-"]; inp = json.dumps(data, ensure_ascii=False)
    r = subprocess.run(cmd, input=inp, capture_output=True, text=True)
    try: return json.loads(r.stdout)
    except Exception: return {"raw": r.stdout[:200]}
def nid(): return "".join(random.choice("0123456789abcdef") for _ in range(7))
def find_parent(els, marker):
    for k, e in enumerate(els):
        if isinstance(e, dict) and e.get("widgetType") == "heading" and str(e.get("settings", {}).get("title", "")).strip().startswith(marker):
            return els, k
    for e in els:
        if isinstance(e, dict):
            r = find_parent(e.get("elements", []), marker)
            if r: return r
    return None
def sub_editor(n, f):
    cnt = 0
    if isinstance(n, list):
        for x in n: cnt += sub_editor(x, f)
    elif isinstance(n, dict):
        ed = n.get("settings", {}).get("editor")
        if isinstance(ed, str):
            new = f(ed)
            if new != ed: n["settings"]["editor"] = new; cnt += 1
        cnt += sub_editor(n.get("elements", []), f)
    return cnt
ELEM = ["advokat-kharkov.org.ua", "argument-consulting.com.ua", "bankruptcyukraine.com", "jurist-po-ipotechnum-kreditam.kiev.ua", "lawmsb.com.ua", "yuristy.in.ua"]
for d in ELEM:
    pid, marker, h2, body, ai, bk = S[d]
    base = f"https://{d}/wp-json/wp/v2/pages/{pid}"
    j = call("GET", base + "?context=edit&_fields=meta,status")
    assert j["status"] == "publish"
    raw_ed = j["meta"]["_elementor_data"]
    (R / "backups" / f"{d}-{pid}-elementor_data.json").write_text(raw_ed, encoding="utf-8")
    ed = json.loads(raw_ed)
    if "lawagency.kiev.ua" in raw_ed: print(d, "вже є — пропуск"); continue
    if d.startswith("jurist-po"):
        old = 'де прочитати відгуки про ла консалтінг'
        def f(t):
            m = re.search(r'<a href="https://consultant\.kiev\.ua/uk/la-konsalting-forum/"[^>]*>' + old + r'</a> можна дізнатися на тематичному форумі боржників\.', t)
            if not m: return t
            t = t.replace(m.group(0), f'Обговорення про фірму є на тематичному форумі боржників: {b("cons")}.')
            mm = re.search(r"Порівнюйте їх з іншими джерелами й перевіряйте самі, що саме пишуть: конкретні факти чи загальні емоції\.", t)
            add = f' Окремо остерігайтеся шахраїв у соцмережах: «{a(4)}». Перш ніж писати комусь у месенджері, звіряйте контакти з офіційним сайтом.'
            return t[:mm.end()] + add + t[mm.end():]
        n = sub_editor(ed, f); assert n == 1, (d, n)
    else:
        fp = find_parent(ed, marker); assert fp, (d, "heading")
        els, k = fp
        h = copy.deepcopy(els[k]); h["id"] = nid(); h["settings"]["title"] = h2
        te = {"id": nid(), "elType": "widget", "settings": {"editor": body}, "elements": [], "widgetType": "text-editor"}
        els[k:k] = [h, te]
    new = json.dumps(ed, ensure_ascii=True, separators=(",", ":"))
    print(d, pid, "elementor_data", len(raw_ed), "->", len(new))
    if APPLY:
        r = call("POST", base, {"meta": {"_elementor_data": new}}); print("   POST", r.get("id"), r.get("status"), r.get("code"))
        print("   cache", subprocess.run(["curl", "-s", "-m", "60", "-A", "curl/8.5.0", "-X", "DELETE", f"https://{d}/wp-json/elementor/v1/cache"], capture_output=True, text=True).stdout[:60])
        rend = call("GET", base)["content"]["rendered"]
        print("   rendered:", "lawagency.kiev.ua" in rend, A[ai] in rend, U[bk] in rend, rend.count("lawagency.kiev.ua"))
