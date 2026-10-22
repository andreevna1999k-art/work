#!/usr/bin/env python3
"""Оновлює ЖИВІ сторінки Бойчука (id 13 головна, id 48 результати): меню «Результати»/«Контакти» ведуть на окремі сторінки,
новий футер (email, кнопки «Політика» і «Контакти»), блок «Мої соцмережі» на головній. Спочатку завантажує поточний вміст із WP і зберігає копію."""
import json, re, subprocess, sys, datetime, pathlib
sys.argv = [sys.argv[0]]
import build_pages as B
R = pathlib.Path(__file__).parent
SITE = B.SITE

def call(method, url, data=None):
    cmd = ["curl", "-sS", "-m", "90", "-X", method, url, "-H", "Content-Type: application/json"]
    if data is not None: cmd += ["--data-binary", "@-"]
    out = subprocess.run(cmd, input=json.dumps(data).encode() if data is not None else None, capture_output=True).stdout
    return json.loads(out)

def patch(pid, with_socials):
    d = call("GET", f"{SITE}/wp-json/wp/v2/pages/{pid}?context=edit")
    raw = d["content"]["raw"]
    (R / f"backup-page{pid}-{datetime.date.today():%Y%m%d}-before-footer.html").write_text(raw, encoding="utf-8")
    new = raw
    # CSS: додати стилі футера/соцблоку перед першим </style>
    if "legal-links" not in new:
        new = new.replace("</style>", "\n" + (R / "pages.css").read_text(encoding="utf-8") + "\n</style>", 1)
    # меню
    new, n1 = re.subn(r'href="#results"', f'href="{B.URL_RESULTS}"', new, count=1)
    new, n2 = re.subn(r"(<ul>\s*<li>.*?)href=\"#contacts\"", lambda m: m.group(1) + f"href=\"{B.URL_CONTACTS}\"", new, count=1, flags=re.S)
    # футер
    a = new.index("<!-- ФУТЕР · КОНТАКТИ -->")
    b = new.index("</section>", new.index('id="contacts"', a)) + len("</section>")
    block = (B.social_block() + "\n\n" if with_socials else "") + B.footer()
    new = new[:a] + block + new[b:]
    assert new.count("<h1") == raw.count("<h1")
    r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", {"content": new})
    print(pid, r.get("status"), "menu:", n1, n2, "| політика у футері:", r.get("content", {}).get("raw", "").count(B.URL_POLICY) if "content" in r else r)

if __name__ == "__main__":
    patch(13, True)
    patch(48, False)
