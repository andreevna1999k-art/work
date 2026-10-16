#!/usr/bin/env python3
"""Збірка чернетки головної ukrjurist.com.ua (Гончарук В. А.), стиль S4 «Olive Arch».
python3 build.py          -> home.wp.html
python3 build.py --publish -> POST draft у WordPress (авторизацію додає проксі середовища)
"""
import json, sys, urllib.parse, urllib.request, pathlib

HERE = pathlib.Path(__file__).parent
SITE = "https://ukrjurist.com.ua"
WP = SITE + "/wp-content/uploads/2026/10/goncharuk-"
TG = "https://t.me/Viktoriia_yrist"
FB = "https://www.facebook.com/profile.php?id=100087531533171"
PHONE_TEL = "+380753916186"
PHONE = "+38 075 391 61 86"
ADDR = "01001, Київ, вул. Михайлівська, 24а"
MAP = "https://www.google.com/maps?q=" + urllib.parse.quote("01001 Київ вул. Михайлівська 24а") + "&hl=uk&output=embed"
H1 = "Гончарук Вікторія Анатолієвна - юрист по кредитам"
DESC = ("Гончарук Вікторія Анатолієвна — юрист по кредитам у Києві: захист позичальників, "
        "реструктуризація боргів, банкрутство фізичних осіб. 15+ років у банках.")
assert len(DESC) <= 160, len(DESC)

SCHEMA = {
    "@context": "https://schema.org", "@type": "Person",
    "name": "Гончарук Вікторія Анатолієвна",
    "jobTitle": "Юристка по кредитам",
    "description": DESC,
    "url": SITE + "/",
    "image": WP + "hero.jpg",
    "telephone": PHONE_TEL,
    "sameAs": [TG, FB],
    "knowsAbout": ["Кредитне право", "Реструктуризація боргів", "Банкрутство фізичних осіб",
                   "Захист прав позичальників", "Переговори з банками та колекторами"],
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Донецький національний університет імені Василя Стуса"},
    "address": {"@type": "PostalAddress", "streetAddress": "вул. Михайлівська, 24а",
                "addressLocality": "Київ", "postalCode": "01001", "addressCountry": "UA"},
}

ICON = {
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><circle cx="11" cy="14" r="2.6"/><path d="m13 16 2.4 2.4"/></svg>',
 "restr": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 13.7-5.6L20 8.5"/><path d="M20 4v4.5h-4.5"/><path d="M20 12a8 8 0 0 1-13.7 5.6L4 15.5"/><path d="M4 20v-4.5h4.5"/></svg>',
 "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v16M8 20h8M5 7h14"/><path d="m5 7-3 7a3.2 3.2 0 0 0 6 0zM19 7l-3 7a3.2 3.2 0 0 0 6 0z"/></svg>',
 "talk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/><path d="M19 10h1a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-1v3l-3-3h-5"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 5 6v5c0 4.4 3 8 7 10 4-2 7-5.6 7-10V6z"/><path d="m9 12 2.2 2.2L15.5 10"/></svg>',
}

SERVICES = [
 ("doc", "Аналіз кредитних договорів", "Перевірка умов договору та нарахувань, виявлення порушень з боку банків."),
 ("restr", "Реструктуризація та рефінансування", "Пошук законних способів зменшити навантаження та впорядкувати борги."),
 ("scale", "Банкрутство фізичних осіб", "Супровід процедури банкрутства фізичних осіб на кожному етапі."),
 ("talk", "Переговори з банками та колекторами", "Діалог із кредиторами та колекторськими компаніями від вашого імені."),
 ("shield", "Захист прав позичальників у суді", "Представництво інтересів позичальників у судових спорах."),
]

# ЗАГЛУШКИ: за ТЗ потрібно 12–20 відгуків із різними датами. Замінити реальними (плагін відгуків) до публікації.
REVIEWS = [
 ("Олена К.", "2026-02-12", "12 лютого 2026", "Пояснила все простою мовою і розклала по кроках, що робити з кредитним договором. Стало зрозуміло, з чого починати."),
 ("Андрій М.", "2026-03-04", "4 березня 2026", "Швидко зорієнтувалась у моїх документах. Спілкування чемне, без зайвих обіцянок."),
 ("Ірина П.", "2026-03-27", "27 березня 2026", "Дуже допомогла порада щодо розмови з банком. Тепер знаю свої права як позичальниця."),
 ("Сергій Т.", "2026-04-15", "15 квітня 2026", "Відчувається, що людина знає систему зсередини. Консультація була предметною."),
 ("Наталія Б.", "2026-05-06", "6 травня 2026", "Відповідала на всі запитання, нічого не лишилось незрозумілим. Дякую за терпіння."),
 ("Володимир Л.", "2026-05-29", "29 травня 2026", "Допомогла розібратися з нарахуваннями та підготуватись до розмови з колекторами."),
 ("Тетяна Г.", "2026-06-18", "18 червня 2026", "Спокійний і професійний підхід. Одразу побачила, де є проблеми в договорі."),
 ("Максим Ш.", "2026-07-09", "9 липня 2026", "Консультація по суті, без води. Отримав чіткий план дій."),
 ("Оксана Р.", "2026-07-30", "30 липня 2026", "Вдячна за підтримку в складний час. Все пояснено доступно."),
 ("Дмитро Ф.", "2026-08-21", "21 серпня 2026", "Допомогла розібратися, як діяти далі з боргом. Рекомендую звернутися за консультацією."),
 ("Юлія С.", "2026-09-10", "10 вересня 2026", "Зручно, що можна швидко написати в Telegram. Відповіла того ж дня."),
 ("Роман Д.", "2026-10-02", "2 жовтня 2026", "Чітко, зрозуміло і по справі. Дізнався, які в мене є варіанти."),
]

def reviews_html():
    out = []
    for name, iso, human, text in REVIEWS:
        out.append(f'<article class="rev"><span class="qm">“</span><p>{text}</p>'
                   f'<footer><b>{name}</b><time datetime="{iso}">{human}</time></footer></article>')
    return "\n".join(out)

def services_html():
    return "\n".join(f'<div class="svc"><div class="ico">{ICON[i]}</div><h3>{t}</h3><p>{d}</p></div>'
                     for i, t, d in SERVICES)

BODY = f"""
<div class="gv" id="top">
<header class="hero">
  <nav class="nav" aria-label="Меню">
    <a class="logo" href="#top">Гончарук В. А.</a>
    <ul>
      <li><a href="#about">Про мене</a></li><li><a href="#services">Послуги</a></li>
      <li><a href="#results">Результати</a></li><li><a href="#reviews">Відгуки</a></li><li><a href="#contacts">Контакти</a></li>
    </ul>
    <a class="btn sm" href="{TG}">Telegram</a>
  </nav>
  <div class="hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">Кредитне право · Банкрутство фізичних осіб</span>
      <h1>{H1}</h1>
      <p class="slogan">«15+ років всередині банківської системи — тепер я граю на вашому боці»</p>
      <p class="lead">Знаю кредитну систему зсередини: від оцінки позичальника до процедури стягнення. Допомагаю знайти законні шляхи виходу з боргової скрути.</p>
      <div class="tags"><span class="tag">Реструктуризація боргів</span><span class="tag">Банкрутство фізичних осіб</span><span class="tag">Захист позичальників</span></div>
      <a class="btn" href="{TG}">Написати в Telegram</a>
    </div>
    <div class="hero-photo"><div class="arch"><img src="{WP}hero.jpg" width="900" height="1236" alt="Гончарук Вікторія Анатолієвна, юрист по кредитам"></div></div>
  </div>
  <svg class="wave" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true"><path d="M0,140 C320,20 1120,20 1440,140 L1440,141 L0,141 Z"/></svg>
</header>

<section class="band on-cream about" id="about">
  <div class="wrap about-grid">
    <div class="arch"><img src="{WP}about.jpg" width="900" height="1106" loading="lazy" alt="Вікторія Гончарук — незалежний консультант з кредитних питань та банкрутства"></div>
    <div>
      <span class="eyebrow">Про мене</span>
      <h2>Знаю банки зсередини</h2>
      <p class="txt">Вікторія — одна з небагатьох консультантів, хто знає кредитну систему зсередини: від оцінки позичальника до процедури стягнення. Працювала в трьох державних банках України, бачила тисячі кредитних справ по обидва боки столу.</p>
      <p class="txt">Закінчила юридичний факультет Донецького національного університету імені Василя Стуса у 2003 році. Пройшла шлях від кредитного спеціаліста до керівника відділу проблемної заборгованості в Ощадбанку, Укрексімбанку та Укргазбанку.</p>
      <blockquote>«Я бачила, як банки приймають рішення, як формуються відмови, як працюють колектори зсередини. І зрозуміла: людям по той бік потрібен хтось, хто знає всі ці механізми.»</blockquote>
      <p class="txt">Сьогодні — незалежний консультант з кредитних питань та банкрутства: допомагаю розібратися з боргами, домовитися з банками та повернути фінансовий спокій.</p>
      <div class="facts">
        <div class="fact"><b>20+</b><span>років у фінансово-правовій сфері</span></div>
        <div class="fact"><b>3</b><span>державні банки за плечима</span></div>
        <div class="fact"><b>2 000+</b><span>розглянутих кредитних справ</span></div>
        <div class="fact"><b>500+</b><span>успішних консультацій з реструктуризації</span></div>
      </div>
    </div>
  </div>
</section>

<section class="band on-ink" id="services">
  <div class="wrap">
    <div class="head"><span class="eyebrow" style="color:var(--gold)">Послуги</span><h2>Чим можу допомогти</h2>
      <p class="lead">Спеціалізація: кредитне право, реструктуризація боргів, банкрутство фізичних осіб.</p></div>
    <div class="svc-grid">
{services_html()}
    </div>
    <div class="center"><a class="btn" href="{TG}">Обговорити мою ситуацію</a></div>
  </div>
</section>

<section class="band on-cream" id="results">
  <div class="wrap">
    <div class="head"><span class="eyebrow" style="color:var(--olive-t)">Результати</span><h2>Результати роботи</h2>
      <p class="lead">Тут з’являться реальні результати для клієнтів: фото документа та короткий опис.</p></div>
    <!-- ПОРОЖНІ ЗАГЛУШКИ: замінити фото + H3 + описом реальних результатів (до 10). -->
    <div class="res-grid">
      <div class="res"><div class="res-photo">Фото результату</div><h3>Результат скоро буде додано</h3><p>Опис результату для клієнта.</p></div>
      <div class="res"><div class="res-photo">Фото результату</div><h3>Результат скоро буде додано</h3><p>Опис результату для клієнта.</p></div>
      <div class="res"><div class="res-photo">Фото результату</div><h3>Результат скоро буде додано</h3><p>Опис результату для клієнта.</p></div>
    </div>
  </div>
</section>

<section class="band on-olive" id="reviews">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Відгуки</span><h2>Відгуки клієнтів</h2></div>
    <!-- МІСЦЕ ПІД ПЛАГІН ВІДГУКІВ: вставити шорткод плагіна замість цього блоку. -->
    <div class="rev-slot">Тут буде плагін відгуків</div>
    <!-- ЗАГЛУШКИ: 12 відгуків за ТЗ (12–20, різні дати). Вигадані, замінити реальними перед публікацією. У Schema не потрапляють. -->
    <div class="rev-track">
{reviews_html()}
    </div>
    <p class="hint">Гортайте вбік →</p>
  </div>
</section>

<section class="band on-cream" id="cta">
  <div class="wrap cta">
    <div>
      <span class="eyebrow" style="color:var(--olive-t)">Консультація</span>
      <h2>Розкажіть про вашу ситуацію</h2>
      <p>Напишіть у Telegram — розберемо кредитний договір, борг і можливі шляхи вирішення.</p>
      <a class="btn" href="{TG}">Написати в Telegram</a>
    </div>
    <div class="photo"><img src="{WP}hall.jpg" width="1100" height="1225" loading="lazy" alt="Вікторія Гончарук із документами у залі"></div>
  </div>
</section>

<footer class="band on-ink foot-band" id="contacts">
  <div class="wrap">
    <div class="contacts">
      <div class="info">
        <span class="eyebrow" style="color:var(--gold)">Контакти</span>
        <h2>Зв’яжіться зі мною</h2>
        <div class="links">
          <a href="tel:{PHONE_TEL}"><small>Телефон</small><b>{PHONE}</b></a>
          <a href="{TG}"><small>Telegram</small><b>@Viktoriia_yrist</b></a>
          <a href="{FB}"><small>Facebook</small><b>Вікторія Гончарук</b></a>
          <div><small>Адреса</small><b>{ADDR}</b></div>
        </div>
        <p class="hours"><b>Години роботи:</b> пн–пт 09:00–18:00, вихідні за домовленістю</p>
      </div>
      <div class="map"><iframe src="{MAP}" title="Карта: {ADDR}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    </div>
    <div class="copy"><span>© Гончарук Вікторія Анатолієвна</span><a href="#top">Нагору ↑</a></div>
  </div>
</footer>
</div>
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Noto+Serif+Display:wght@400;500&display=swap&subset=cyrillic">')

def build():
    css = (HERE / "gv.css").read_text(encoding="utf-8")
    ld = json.dumps(SCHEMA, ensure_ascii=False, indent=1)
    return (f"<!-- Title/H1: {H1} -->\n<!-- Description: {DESC} -->\n{FONTS}\n<style>{css}</style>\n{BODY}\n"
            f'<script type="application/ld+json">{ld}</script>\n')

if __name__ == "__main__":
    html = build()
    (HERE / "home.wp.html").write_text(html, encoding="utf-8")
    print("home.wp.html", len(html))
    if "--publish" in sys.argv:
        pid = sys.argv[sys.argv.index("--publish") + 1] if len(sys.argv) > sys.argv.index("--publish") + 1 else None
        payload = {"title": H1, "status": "draft", "slug": "golovna", "template": "page-blank",
                   "content": "<!-- wp:html -->\n" + html + "\n<!-- /wp:html -->"}
        url = SITE + "/wp-json/wp/v2/pages" + (f"/{pid}" if pid else "")
        import subprocess
        out = subprocess.run(["curl", "-sS", "-m", "90", "-X", "POST", url, "-H", "Content-Type: application/json",
                              "--data-binary", "@-"], input=json.dumps(payload).encode(), capture_output=True).stdout
        d = json.loads(out)
        if "id" not in d:
            sys.exit(str(d))
        print(d["id"], d["status"], d["link"], d.get("template"))
