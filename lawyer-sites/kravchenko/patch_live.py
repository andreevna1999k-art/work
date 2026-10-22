#!/usr/bin/env python3
"""Кравченко: оновлює ЖИВІ сторінки (1901 головна, 1916 результати): меню (додає «Результати», «Контакти» на сторінки),
новий футер (email, Facebook, Політика, кнопки), блок «Мої соцмережі» на головній, sameAs Facebook у Schema Person.
Запускати ЛИШЕ після публікації «Контактів» і «Політики» (за командою «публікуй»). Копії сторінок кладе в BACKUP_DIR (не в репозиторій: сторінки ~1,8 МБ)."""
import json, re, subprocess, sys, datetime, pathlib
sys.argv = [sys.argv[0]]
import build_pages as B
R = pathlib.Path(__file__).parent
BACKUP_DIR = pathlib.Path("/tmp/claude-0/-home-user-work/bd2e8cc1-3024-54de-bcd5-7f29eaa7db16/scratchpad/kra-backups")
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
SITE = B.SITE

def call(method, url, data=None):
    cmd = ["curl", "-sS", "-m", "180", "-X", method, url, "-H", "Content-Type: application/json"]
    if data is not None: cmd += ["--data-binary", "@-"]
    return json.loads(subprocess.run(cmd, input=json.dumps(data).encode() if data is not None else None, capture_output=True).stdout)

def patch(pid, with_socials):
    d = call("GET", f"{SITE}/wp-json/wp/v2/pages/{pid}?context=edit")
    raw = d["content"]["raw"]
    (BACKUP_DIR / f"backup-page{pid}-{datetime.datetime.now():%Y%m%d-%H%M}-before-footer.html").write_text(raw, encoding="utf-8")
    new = raw
    if "legal-links" not in new:  # стилі футера/соцблоку: беремо pages.css, замінюючи лише при першому проході
        new = new.replace("</style>", "\n" + (R / "pages.css").read_text(encoding="utf-8") + "\n</style>", 1)
    # меню: ul у шапці
    i = new.index('<div class="nav">'); j = new.index("</ul>", i) + 5
    new = new[:i] + new[i:j].split("<ul>")[0] + B.menu_ul() + new[j:]
    # футер
    a = new.index('<footer class="box sec dk" id="contacts">'); b = new.index("</footer>", a) + len("</footer>")
    block = (B.social_block() + "\n" if with_socials and 'id="socials"' not in new else "") + B.footer()
    new = new[:a] + block + new[b:]
    # sameAs: додати Facebook
    if B.FB not in new.split("</script>")[0]:
        new = new.replace('"https://www.instagram.com/yuryst_kravchenko/"]', '"https://www.instagram.com/yuryst_kravchenko/", "' + B.FB + '"]', 1)
    assert new.count("<h1") == raw.count("<h1")
    r = call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", {"content": new})
    print(pid, r.get("status"), "| політика у футері:", r["content"]["raw"].count("/polityka-konfidentsiinosti/") if "content" in r else r)

if __name__ == "__main__":
    patch(1901, True)
    patch(1916, False)
