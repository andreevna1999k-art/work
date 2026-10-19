"""Builds code/home.wp.html (WP block) and code/home.local.html (preview) from src/ + hz.css.
Photos: photos/hz-hero.jpg, hz-about.jpg, hz-chair.jpg (processed copies of photos/originals/). Missing photo -> placeholder."""
import json, pathlib, re, sys
R = pathlib.Path(__file__).parent
LOCAL = "--local" in sys.argv
WP = "https://ukrjurist.com.ua/wp-content/uploads/2026/10/goncharuk-"
SCANS = pathlib.Path("/tmp/claude-0/-home-user-work/1b462dfe-7007-59f9-af84-0f520b5507b3/scratchpad/out")  # лише для локального прев'ю
from results_data import R as RES
TITLE = "Гончарук Вікторія Анатолієвна - юрист по кредитам"
DESC = "Юрист по кредитам у Києві: 15+ років у банках, реструктуризація боргів, банкрутство фізосіб, захист позичальників. Консультація в Telegram."
assert len(DESC) <= 160, len(DESC)
(R / "code/meta-description.txt").write_text(f"Title: {TITLE}\nDescription: {DESC}\nПотрібен SEO-плагін (Yoast/Rank Math), щоб description потрапив у <head>.\n", encoding="utf-8")
ADDR = {"@type": "PostalAddress", "streetAddress": "вул. Михайлівська, 24а", "addressLocality": "Київ", "postalCode": "01001", "addressCountry": "UA"}
SCHEMA = {"@context": "https://schema.org", "@type": "Person", "@id": "https://ukrjurist.com.ua/#person",
 "name": "Гончарук Вікторія Анатолієвна", "jobTitle": "юристка по кредитам", "description": DESC,
 "url": "https://ukrjurist.com.ua/", "image": WP + "hero.jpg", "telephone": "+380753916186",
 "sameAs": ["https://t.me/Viktoriia_yrist", "https://www.facebook.com/profile.php?id=100087531533171"],
 "knowsAbout": ["Кредитне право", "Реструктуризація боргів", "Банкрутство фізичних осіб", "Захист прав позичальників"],
 "alumniOf": {"@type": "CollegeOrUniversity", "name": "Донецький національний університет імені Василя Стуса"},
 "address": ADDR}
def img(m):
    key, alt, w, h, lazy = m.group(1).split("|")
    f = R / f"photos/hz-{key}.jpg"
    if LOCAL and not f.exists():
        return f'<div class="ph">Фото ({key}) буде додано</div>'
    src = f"../photos/hz-{key}.jpg" if LOCAL else f"{WP}{key}.jpg"
    return f'<img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="{lazy}">'
def card(i, mid, t, d, alt):
    n = f"{i:02d}"
    src = f"file://{SCANS}/res-{n}.webp" if LOCAL else f"{WP}rezultat-{n}.webp"
    return (f'<article class="res-card"><a class="shot" href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{alt}" loading="lazy"></a>'
            f'<h3>{t}</h3><p>{d}</p></article>')
res = "\n".join(card(i, *r) for i, r in enumerate(RES, 1))
REV = [("Ірина К.","12.03.2026"),("Олег М.","28.03.2026"),("Наталія С.","14.04.2026"),("Андрій Т.","02.05.2026"),("Світлана Л.","19.05.2026"),("Максим Д.","07.06.2026"),
       ("Оксана Б.","25.06.2026"),("Віктор Р.","11.07.2026"),("Тетяна Г.","30.07.2026"),("Сергій П.","16.08.2026"),("Людмила Ш.","03.09.2026"),("Роман Ф.","21.09.2026")]
rev = "\n".join(f'<!-- ЗАГЛУШКА: замінити реальними -->\n<article class="rev-card"><div class="stars">★★★★★</div><p>Текст відгуку-заглушка. Тут буде справжній відгук клієнта.</p><div class="who"><b>{n}</b><span>{d}</span></div></article>' for n, d in REV)
body = (R / "src/home.body.html").read_text(encoding="utf-8").replace("<!--RES-->", res).replace("<!--REV-->", rev)
body = re.sub(r"<!--IMG:([^>]*?)-->", img, body)
css = (R / "hz.css").read_text(encoding="utf-8")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Manrope:wght@400;600;700&display=swap&subset=cyrillic">')
page = (f'<script type="application/ld+json">{json.dumps(SCHEMA, ensure_ascii=False)}</script>\n{FONTS}\n<style>\n{css}\n.hz{{width:100%;margin:0;min-height:100vh}}\n'
        f'html,body{{margin:0!important;padding:0!important;background:#F5EFE3!important}}html{{scroll-behavior:smooth}}\n</style>\n{body}')
if LOCAL:
    page = f'<!doctype html><html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE}</title><meta name="description" content="{DESC}"></head><body>{page}</body></html>'
(R / ("code/home.local.html" if LOCAL else "code/home.wp.html")).write_text(page, encoding="utf-8")
print("ok", "local" if LOCAL else "wp", len(DESC))
