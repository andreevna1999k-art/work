#!/usr/bin/env python3
"""Прибирає «Юрист пояснює…» (зворотний порядок, пропущений у fix_poyasniuie.py) з title/content/excerpt/_elementor_data.
  python3 fix_yurist_poiasniuie.py [--apply]"""
import json, re, subprocess, sys, pathlib
APPLY = "--apply" in sys.argv
B = pathlib.Path(__file__).parent / "backup-yurist-poiasniuie"
T = {"jurist-online.info": [2685], "legaladdress.com.ua": [117, 113, 107, 105], "uchet.com.ua": [70], "ukrjurist.com.ua": [74, 69]}
RX = re.compile(r"([Юю])рист пояснює,?\s+(\S)")
def fx(s):
    return RX.sub(lambda m: m.group(2).upper() if m.group(1) == "Ю" else m.group(2), s) if isinstance(s, str) else s
def call(m, u, data=None):
    cmd = ["curl", "-s", "-m", "180", "-X", m, u]; inp = None
    if data is not None: cmd += ["-H", "Content-Type: application/json", "--data-binary", "@-"]; inp = json.dumps(data, ensure_ascii=False)
    return json.loads(subprocess.run(cmd, input=inp, capture_output=True, text=True).stdout)
for d, ids in T.items():
    for i in ids:
        u = f"https://{d}/wp-json/wp/v2/pages/{i}"
        p = call("GET", u + "?context=edit&_fields=id,status,title,content,excerpt,meta")
        upd = {}
        for k in ("title", "content", "excerpt"):
            v = p[k]["raw"]
            if RX.search(v): upd[k] = fx(v)
        ed = (p.get("meta") or {}).get("_elementor_data")
        if isinstance(ed, str) and RX.search(ed): upd["meta"] = {"_elementor_data": fx(ed)}
        for k, v in upd.items():
            src = p[k]["raw"] if k != "meta" else ed; dst = v if k != "meta" else v["_elementor_data"]
            for m in RX.finditer(src): print(d, i, p["status"], k, "|", src[max(0, m.start()-40):m.end()+25].replace("\n", " "))
        if APPLY and upd:
            (B / f"{d}-{i}.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
            r = call("POST", u, upd); print("   ->", r.get("id"), r.get("status"), r.get("code"))
            chk = call("GET", u + "?context=edit&_fields=title,content,excerpt,meta")
            left = sum(1 for k in ("title", "content", "excerpt") if RX.search(chk[k]["raw"])) + (1 if RX.search((chk.get("meta") or {}).get("_elementor_data") or "") else 0)
            print("   left:", left)
