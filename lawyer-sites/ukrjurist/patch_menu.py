"""Додає мобільне меню (бургер) у шапку сторінки WP: python3 patch_menu.py in.html out.html home|results"""
import re, sys
src, dst, kind = sys.argv[1:4]
c = open(src, encoding="utf-8").read()
L = {"home": ["#about", "#services", "/rezultaty-roboty/", "#reviews", "#contacts"],
     "results": ["/#about", "/#services", "#results", "/#reviews", "#contacts"]}[kind]
names = ["Про мене", "Послуги", "Результати", "Відгуки", "Контакти"]
close = "this.closest('details').removeAttribute('open')"
links = "".join(f'<a href="{h}" onclick="{close}">{n}</a>' for h, n in zip(L, names))
menu = ('<details class="m-menu"><summary aria-label="Меню">'
        '<svg class="ic-bars" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
        '<svg class="ic-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></summary>'
        f'<div class="m-panel">{links}<a class="btn" href="https://t.me/Viktoriia_yrist">Написати в Telegram</a></div></details>')
assert 'class="m-menu"' not in c and c.count("</nav>") == 1
c = c.replace("</nav>", "  " + menu + "\n  </nav>", 1)
css = open("code/mobile-menu.css", encoding="utf-8").read()
k = c.index("</style>"); c = c[:k] + css + c[k:]
open(dst, "w", encoding="utf-8").write(c)
print("ok", len(c))
