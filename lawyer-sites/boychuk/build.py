"""Builds WordPress homepage fragment and the design-system page from src/ + bz.css."""
import pathlib
R = pathlib.Path(__file__).parent
CSS = (R / "bz.css").read_text(encoding="utf-8")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Playfair+Display:ital,wght@0,500;1,500&display=swap">')
WP = "https://legaladdress.com.ua/wp-content/uploads/2026/10/boychuk-"
IMGS = {"__IMG_OFFICE__": "portrait-office", "__IMG_OFFICE2__": "portrait-office-2", "__IMG_CAR__": "portrait-car"}

TITLE = "Бойчук Артем Валерійович — юрист по кредитам"
DESC = "Юрист по кредитам у Києві: аналіз кредитного договору, переговори з банком, захист від колекторів і представництво в суді. Консультація в Telegram."
import json
SCHEMA = {"@context": "https://schema.org", "@type": "Person",
 "@id": "https://legaladdress.com.ua/#boychuk",
 "name": "Бойчук Артем Валерійович", "givenName": "Артем", "familyName": "Бойчук", "additionalName": "Валерійович",
 "jobTitle": "Юрист по кредитам", "description": DESC,
 "url": "https://legaladdress.com.ua/", "image": WP+"portrait-office.jpg",
 "telephone": "+380754921980", "sameAs": ["https://t.me/artem_adwokat"],
 "knowsAbout": ["Кредитні спори", "Реструктуризація боргів", "Захист від колекторів", "Виконавче провадження", "Іпотека"],
 "knowsLanguage": ["uk"],
 "address": {"@type": "PostalAddress", "streetAddress": "вул. Княжий Затон, 2/30", "postalCode": "02055", "addressLocality": "Київ", "addressCountry": "UA"},
 "workLocation": {"@type": "Place", "name": "Офіс", "address": {"@type": "PostalAddress", "streetAddress": "вул. Княжий Затон, 2/30", "postalCode": "02055", "addressLocality": "Київ", "addressCountry": "UA"}}}
HEAD = ('<meta name="description" content="%s">\n<script type="application/ld+json">%s</script>' % (DESC, json.dumps(SCHEMA, ensure_ascii=False)))
FULL = "width:100%;margin:0;min-height:100vh"

def sub(html, local):
    for k, v in IMGS.items():
        html = html.replace(k, (f"img/{v}.jpg" if local else f"{WP}{v}.jpg"))
    return html

body = (R / "src/home.body.html").read_text(encoding="utf-8")
(R / "home.wp.html").write_text(f"{HEAD}\n{FONTS}\n<style>\n{CSS}\n.bz{{{FULL}}}\nhtml,body{{margin:0!important;padding:0!important;background:#FBF7F1!important}}\nhtml{{scroll-behavior:smooth}}\n</style>\n{sub(body, False)}", encoding="utf-8")
ds = (R / "src/ds.body.html").read_text(encoding="utf-8")
(R / "design-system.html").write_text(
    f'<!doctype html>\n<html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    f'<title>Бойчук — дизайн-система</title>\n{FONTS}\n<style>body{{margin:0;background:#FBF7F1}}\n{CSS}</style></head><body>\n{sub(ds, True)}\n</body></html>', encoding="utf-8")
print("ok")
