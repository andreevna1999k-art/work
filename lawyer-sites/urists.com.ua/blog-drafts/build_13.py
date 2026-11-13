#!/usr/bin/env python3
"""Стаття 13 (окрема, про фейкові профілі юрфірм) за тим самим шаблоном, що й build_drafts.py.
  python3 build_13.py [--create]   -> payload/13-*.json, preview, ЧЕРНЕТКА у WP (draft)"""
import json, sys, base64, subprocess, pathlib
import build_drafts as B
SLUG = "yak-vidriznyty-feikovyi-profil-yurydychnoi-firmy"
DATE = "2026-12-07"
B.DATES.append(DATE); B.TAGS.append("Шахрайство")
B.IMAGES[SLUG] = {"src": "data:image/webp;base64," + base64.b64encode((B.R / "img/13.webp").read_bytes()).decode(),
                  "alt": "Жінка в телефоні перевіряє профіль юридичної фірми та порівнює його з реєстром на ноутбуці"}
p, info = B.build(13, SLUG, None, None)
pf = B.R / "payload" / f"13-{SLUG}.json"
pf.write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
print(info)
# посилання на закони (КК, ЦК) локально
print(subprocess.run(["python3", str(B.R.parent.parent / "tools/add_law_links.py"), "--local", str(pf), "--apply"], capture_output=True, text=True).stdout)
p = json.loads(pf.read_text(encoding="utf-8"))
(B.R / "preview" / f"13-{SLUG}.html").write_text(p["content"], encoding="utf-8")
p["content"] = p["content"].replace('<a href="https://jurliga.ligazakon.net/ru/catalog/12850" target="_blank" rel="noopener">', '<a href="https://jurliga.ligazakon.net/ru/catalog/12850" target="_blank" rel="noopener" style="word-break:break-all">')
pf.write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
(B.R / "preview" / f"13-{SLUG}.html").write_text(p["content"], encoding="utf-8")
c = p["content"]; print("lawagency:", c.count("lawagency.kiev.ua"), "jurliga:", c.count('href="https://jurliga'), "zakon:", c.count("zakon.rada.gov.ua"), "img:", c.count("data:image/webp"))
if "--create" in sys.argv:
    ids = json.load(open(B.R / "draft-ids.json"))
    assert p["status"] == "draft"
    r = B.call("POST", f"{B.SITE}/wp-json/wp/v2/pages/{ids[SLUG]}" if SLUG in ids else f"{B.SITE}/wp-json/wp/v2/pages", p)
    print(r.get("id"), r.get("status"), r.get("date"), r.get("link"), str(r.get("message", ""))[:200])
    if "id" in r:
        ids[SLUG] = r["id"]; json.dump(ids, open(B.R / "draft-ids.json", "w"), ensure_ascii=False, indent=1)
