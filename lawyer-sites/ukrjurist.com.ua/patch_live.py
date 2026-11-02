#!/usr/bin/env python3
"""Гончарук: оновлює ЖИВІ сторінки (14 головна, 31 результати): меню «Результати»/«Контакти» на окремі сторінки, новий футер,
@id у Schema Person. Запускати після публікації «Контактів» і «Політики» (за командою «публікуй»)."""
import json, re, subprocess, sys, datetime, pathlib
sys.argv = [sys.argv[0]]
import build_pages as B
R = pathlib.Path(__file__).parent
SITE = B.SITE

def call(method, url, data=None):
    cmd = ["curl", "-sS", "-m", "90", "-X", method, url, "-H", "Content-Type: application/json"]
    if data is not None: cmd += ["--data-binary", "@-"]
    return json.loads(subprocess.run(cmd, input=json.dumps(data).encode() if data is not None else None, capture_output=True).stdout)

def patch(pid, with_socials):
    d = call("GET", f"{SITE}/wp-json/wp/v2/pages/{pid}?context=edit")
    raw = d["content"]["raw"]
    (R / f"backup-page{pid}-{datetime.datetime.now():%Y%m%d-%H%M}-before-footer.html").write_text(raw, encoding="utf-8")
    new = raw
    if "legal-links" not in new:
        new = new.replace("</style>", "\n" + (R / "pages.css").read_text(encoding="utf-8") + "\n</style>", 1)
    # меню (ul і мобільна панель) у шапці: до <details>…</details> включно
    i = new.index('<nav class="nav"'); j = new.index("</nav>", i)
    head = new[i:j]
    head = head.replace('href="/rezultaty-roboty/"', 'href="/rezultaty-roboty/"')
    head = head.replace('href="#results"', f'href="{B.URL_RESULTS}"').replace('href="#contacts"', f'href="{B.URL_CONTACTS}"')
    new = new[:i] + head + new[j:]
    a = new.index('<footer class="band on-ink foot-band"'); b = new.index("</footer>", a) + len("</footer>")
    block = (B.social_block() + "\n\n" if with_socials and 'id="socials"' not in new else "") + B.footer()
    new = new[:a] + block + new[b:]
    # Schema Person: додати @id
    if '"@id": "https://ukrjurist.com.ua/#person"' not in new:
        new = new.replace('"@type": "Person",', '"@type": "Person",\n "@id": "https://ukrjurist.com.ua/#person",', 1)
    assert new.count("<h1") == raw.count("<h1")
    r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", {"content": new})
    print(pid, r.get("status"), "| політика у футері:", r["content"]["raw"].count(B.URL_POLICY) if "content" in r else r)

if __name__ == "__main__":
    patch(14, True)
    patch(31, False)
    print(call("POST", f"{SITE}/wp-json/wp/v2/settings", {"title": B.NAME}).get("title"))
