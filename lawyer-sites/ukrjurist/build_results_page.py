"""Окрема сторінка «Результати роботи» (стиль головної page 14): code/results-page.html. Дані: results_data.py (R = 8 з головної, R2 = ще 5)."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from results_data import R, R2
D = pathlib.Path(__file__).parent / "code"
home = (D / "page14.new.html").read_text(encoding="utf-8")
WP = "https://ukrjurist.com.ua/wp-content/uploads/2026/10/goncharuk-rezultat-"
TITLE = "Результати роботи — Гончарук Вікторія Анатолієвна"
DESC = "Результати роботи юриста по кредитам Гончарук Вікторії Анатолієвни: довідки кредиторів про закриття договорів і відсутність заборгованості."
assert len(DESC) <= 160, len(DESC)
fonts = re.search(r'<link rel="preconnect".*?display=swap&subset=cyrillic">', home, re.S).group(0)
css = home[home.index("<style"):home.index("</style>") + 8]
extra = """<style>
.gv .hero.sub{min-height:0}
.gv .hero.sub .hero-grid{grid-template-columns:1fr;padding:64px 28px 170px;text-align:center}
.gv .hero.sub .hero-copy{max-width:820px;margin:0 auto}
.gv .hero.sub h1{margin-bottom:20px}
.gv .hero.sub .lead{margin:0 auto 0;max-width:640px}
.gv .res-grid.flexed{display:flex;flex-wrap:wrap;justify-content:center;gap:22px;align-items:stretch}
.gv .res-grid.flexed .res{flex:0 0 calc((100% - 66px)/4)}
@media(max-width:1000px){.gv .res-grid.flexed .res{flex-basis:calc((100% - 22px)/2)}}
@media(max-width:620px){.gv .res-grid.flexed{gap:14px}.gv .res-grid.flexed .res{flex-basis:100%}.gv .hero.sub .hero-grid{padding:36px 16px 120px}}
</style>"""
cards = []
for i, (_, t, d, alt) in enumerate(R + R2, 1):
    src = f"{WP}{i:02d}.webp"
    cards.append(f'      <div class="res"><a class="res-shot" href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{alt}" loading="lazy" decoding="async"></a><h3>{t}</h3><p>{d}</p></div>')
nav = '''  <nav class="nav" aria-label="Меню">
    <a class="logo" href="/">Гончарук В. А.</a>
    <ul>
      <li><a href="/#about">Про мене</a></li><li><a href="/#services">Послуги</a></li>
      <li><a href="#results">Результати</a></li><li><a href="/#reviews">Відгуки</a></li><li><a href="#contacts">Контакти</a></li>
    </ul>
    <a class="btn sm" href="https://t.me/Viktoriia_yrist">Telegram</a>
  </nav>'''
hero = f'''<header class="hero sub">
{nav}
  <div class="hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">Гончарук Вікторія Анатолієвна · юрист по кредитам</span>
      <h1>Результати роботи</h1>
      <p class="lead">Довідки кредиторів про виконання зобов’язань і відсутність заборгованості. Персональні дані клієнтів закрито.</p>
    </div>
  </div>
  <svg class="wave" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true"><path d="M0,140 C320,20 1120,20 1440,140 L1440,141 L0,141 Z"/></svg>
</header>'''
results = f'''<section class="band on-cream" id="results">
  <div class="wrap">
    <div class="res-grid flexed">
{chr(10).join(cards)}
    </div>
  </div>
</section>'''
tail = home[home.index('<section class="band on-cream" id="cta">'):home.index('<script type="application/ld+json">')]
schema = {"@context": "https://schema.org", "@type": "CollectionPage", "name": TITLE, "description": DESC,
          "url": "https://ukrjurist.com.ua/rezultaty-roboty/",
          "about": {"@type": "Person", "name": "Гончарук Вікторія Анатолієвна", "jobTitle": "Юристка по кредитам", "url": "https://ukrjurist.com.ua/"}}
page = f'''<!-- wp:html -->
<!-- Title: {TITLE} -->
<!-- H1: Результати роботи -->
<!-- Description: {DESC} -->
{fonts}
{css}
{extra}

<div class="gv" id="top">
{hero}

{results}

{tail}<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>

<!-- /wp:html -->
'''
(D / "results-page.html").write_text(page, encoding="utf-8")
(D / "results-meta-description.txt").write_text(f"Title: {TITLE}\nH1: Результати роботи\nDescription: {DESC}\n", encoding="utf-8")
print("ok", len(page), page.count('class="res"'), page.count("<h1"), len(DESC))
