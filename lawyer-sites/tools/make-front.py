#!/usr/bin/env python3
"""Робить головну сторінку сайту головною за доменом (сайт.юа/, а не сайт.юа/головна).
Використання:
  python3 make-front.py legaladdress.com.ua 13          # лише перевірка, нічого не змінює
  python3 make-front.py legaladdress.com.ua 13 --go     # ПУБЛІКУЄ сторінку й ставить її головною
Тільки після моєї команди «публікуй». Що робить --go:
  1) статус сторінки -> publish; 2) Settings -> Reading: show_on_front=page, page_on_front=ID.
Старе посилання /slug/ після цього перенаправляє на корінь домену.
"""
import json, subprocess, sys

def call(method, url, data=None):
    cmd = ["curl", "-sS", "-m", "60", "-X", method, url, "-H", "Content-Type: application/json"]
    if data is not None:
        cmd += ["--data-binary", json.dumps(data)]
    return json.loads(subprocess.run(cmd, capture_output=True).stdout)

host, pid = sys.argv[1], int(sys.argv[2])
base = f"https://{host}/wp-json/wp/v2"
page = call("GET", f"{base}/pages/{pid}?context=edit&_fields=id,slug,status,template,title")
st = call("GET", f"{base}/settings")
print("сторінка:", page.get("id"), page.get("status"), page.get("slug") or "(slug порожній)", page.get("template"))
print("зараз: show_on_front =", st.get("show_on_front"), "page_on_front =", st.get("page_on_front"))
if "--go" not in sys.argv:
    print("Режим перевірки. Для застосування додай --go"); sys.exit(0)
r = call("POST", f"{base}/pages/{pid}", {"status": "publish"})
print("публікація:", r.get("status"), r.get("link"))
r = call("POST", f"{base}/settings", {"show_on_front": "page", "page_on_front": pid})
print("головна:", r.get("show_on_front"), r.get("page_on_front"))
