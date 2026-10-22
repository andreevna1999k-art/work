#!/usr/bin/env python3
"""Яковенко: оновлює ЖИВІ сторінки (9 головна, 30 результати): меню на окремі сторінки, новий футер,
бургер-меню на сторінці результатів, sameAs (Facebook) у Schema Person. Запускати після публікації «Контактів» і «Політики»."""
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
    # меню
    if 'class="menu-cb"' not in new:  # сторінка результатів: у шапки немає бургера, ставимо повну
        m = re.search(r'<div class="nav">.*?</div>', new, re.S)
        full = re.search(r'<div class="nav">.*?</div>', B.header("x", "x", "x"), re.S).group(0)
        new = new.replace(m.group(0), full, 1)
    else:
        m = re.search(r'<nav>.*?</nav>', new, re.S)
        menu = m.group(0).replace('href="#results"', f'href="{B.URL_RESULTS}"').replace('href="#contacts"', f'href="{B.URL_CONTACTS}"')
        new = new.replace(m.group(0), menu, 1)
    # футер
    a = new.index('<footer class="contacts dark"'); b = new.index("</footer>", a) + len("</footer>")
    new = new[:a] + B.footer() + new[b:]
    if 'id="ykm"' not in new[b:] and "getElementById" not in new[a:] and '#ykm' not in new:
        new = new.replace("<!-- /wp:html -->", B.BURGER_JS + "\n<!-- /wp:html -->", 1)
    # sameAs: додати Facebook
    if B.FB not in new:
        new = re.sub(r'("sameAs":\s*\[\s*"https://t\.me/yakovenko_lawyer")', r'\1,\n    "' + B.FB + '"', new, count=1)
    assert new.count("<h1") == raw.count("<h1")
    r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", {"content": new})
    print(pid, r.get("status"), "| політика у футері:", r["content"]["raw"].count(B.URL_POLICY) if "content" in r else r, "| FB у sameAs:", B.FB in r.get("content", {}).get("raw", ""))

if __name__ == "__main__":
    patch(9)
    patch(30)
