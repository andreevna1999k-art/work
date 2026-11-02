#!/usr/bin/env python3
"""Борисов: оновлює ЖИВІ сторінки (9 головна, 33 результати): меню «Результати»/«Контакти» ведуть на окремі сторінки,
новий футер (email, Політика, кнопки). Запускати ЛИШЕ після публікації «Контактів» і «Політики» (за командою «публікуй»).
Спочатку завантажує поточний вміст з WP і зберігає копію."""
import json, re, subprocess, sys, datetime, pathlib
sys.argv = [sys.argv[0]]
import build_pages as B
R = pathlib.Path(__file__).parent
SITE = B.SITE

def call(method, url, data=None):
    cmd = ["curl", "-sS", "-m", "90", "-X", method, url, "-H", "Content-Type: application/json"]
    if data is not None: cmd += ["--data-binary", "@-"]
    return json.loads(subprocess.run(cmd, input=json.dumps(data).encode() if data is not None else None, capture_output=True).stdout)

def patch(pid):
    d = call("GET", f"{SITE}/wp-json/wp/v2/pages/{pid}?context=edit")
    raw = d["content"]["raw"]
    (R / f"backup-page{pid}-{datetime.datetime.now():%Y%m%d-%H%M}-before-footer.html").write_text(raw, encoding="utf-8")
    new = raw
    if "legal-links" not in new:
        new = new.replace("</style>", "\n" + (R / "pages.css").read_text(encoding="utf-8") + "\n</style>", 1)
    # меню: Результати і Контакти на окремі сторінки (у <nav class="menu">)
    m = re.search(r'<nav class="menu">.*?</nav>', new, re.S)
    if m:
        menu = m.group(0).replace('href="#results"', f'href="{B.URL_RESULTS}"').replace('href="#contacts"', f'href="{B.URL_CONTACTS}"')
        new = new.replace(m.group(0), menu, 1)
    # футер: замінити <footer ...>...</footer> новим
    a = new.index('<footer class="page-end"'); b = new.index("</footer>", a) + len("</footer>")
    new = new[:a] + B.footer() + new[b:]
    assert new.count("<h1") == raw.count("<h1")
    r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", {"content": new})
    print(pid, r.get("status"), "| посилань на політику:", r.get("content", {}).get("raw", "").count(B.URL_POLICY) if "content" in r else r)

if __name__ == "__main__":
    patch(9)
    patch(33)
