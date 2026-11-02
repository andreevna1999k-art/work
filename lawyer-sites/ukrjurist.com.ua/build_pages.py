#!/usr/bin/env python3
"""Гончарук Вікторія Анатолієвна (ukrjurist.com.ua), стиль S4 «Olive Arch»: сторінки «Контакти» і «Політика конфіденційності».
CSS береться з живої головної та сторінки результатів (base.css) + pages.css.
  python3 build_pages.py                  -> kontakty.wp.html, polityka.wp.html
  python3 build_pages.py --publish        -> ЧЕРНЕТКИ у WP
  python3 build_pages.py --publish --live -> статус publish (лише за командою «публікуй»)
"""
import json, subprocess, sys, pathlib, urllib.parse

R = pathlib.Path(__file__).parent
SITE = "https://ukrjurist.com.ua"
NAME = "Гончарук Вікторія Анатолієвна"
EMAIL = "viktoriia-yrist@ukrjurist.com.ua"
EMAIL_HTML = EMAIL.replace("@", "<wbr>@")
PHONE_TEL, PHONE = "+380753916186", "+38 075 391 61 86"
TG, TG_NICK = "https://t.me/Viktoriia_yrist", "@Viktoriia_yrist"
FB = "https://www.facebook.com/profile.php?id=100087531533171"
ADDR = "01001, Київ, вул. Михайлівська, 24а"
ADDR_Q = urllib.parse.quote("01001 Київ вул. Михайлівська 24а")
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + ADDR_Q
MAP_EMBED = "https://www.google.com/maps?q=" + ADDR_Q + "&hl=uk&output=embed"
URL_CONTACTS, URL_POLICY, URL_RESULTS = "/kontakty/", "/polityka-konfidentsiinosti/", "/rezultaty-roboty/"
POLICY_TITLE = "Політика конфіденційності та обробки персональних даних"
DATE_HUMAN, DATE_ISO = "22 жовтня 2026 року", "2026-10-22"
CSS = (R / "base.css").read_text(encoding="utf-8") + "\n" + (R / "pages.css").read_text(encoding="utf-8")

ICO_TG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.5 4.3 2.9 11.5c-1.3.5-1.3 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.8.8.8.5 0 .8-.2 1.1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.2-.5-1.8-1.5-1.4zM8.5 13.6l9.6-6c.5-.3.9-.1.5.2l-7.8 7-.3 3.2z"/></svg>'
ICO_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.5-3.2h-3.2V7.7c0-.9.3-1.6 1.7-1.6h1.6V3.2c-.3 0-1.3-.1-2.4-.1-2.5 0-4.1 1.5-4.1 4.2v2.5H7.5V13h2.8v8z"/></svg>'
CLOSE = "onclick=\"this.closest('details').removeAttribute('open')\""

def header(h1, lead, eyebrow):
    links = [("/#about", "Про мене"), ("/#services", "Послуги"), (URL_RESULTS, "Результати"), ("/#reviews", "Відгуки"), (URL_CONTACTS, "Контакти")]
    ul = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in links)
    panel = "".join(f'<a href="{h}" {CLOSE}>{t}</a>' for h, t in links)
    return f'''<header class="hero sub">
  <nav class="nav" aria-label="Меню">
    <a class="logo" href="/">Гончарук В. А.</a>
    <ul>{ul}</ul>
    <a class="btn sm" href="{TG}">Telegram</a>
    <details class="m-menu"><summary aria-label="Меню"><svg class="ic-bars" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg><svg class="ic-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></summary><div class="m-panel">{panel}<a class="btn" href="{TG}">Написати в Telegram</a></div></details>
  </nav>
  <div class="hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
    </div>
  </div>
  <svg class="wave" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true"><path d="M0,140 C320,20 1120,20 1440,140 L1440,141 L0,141 Z"/></svg>
</header>'''

def footer():
    return f'''<footer class="band on-ink foot-band" id="contacts">
  <div class="wrap">
    <div class="contacts">
      <div class="info">
        <span class="eyebrow" style="color:var(--gold)">Контакти</span>
        <h2>Зв’яжіться зі мною</h2>
        <div class="links">
          <a href="tel:{PHONE_TEL}"><small>Телефон</small><b>{PHONE}</b></a>
          <a href="mailto:{EMAIL}"><small>Email</small><b>{EMAIL_HTML}</b></a>
          <a href="{TG}"><small>Telegram</small><b>{TG_NICK}</b></a>
          <a href="{FB}"><small>Facebook</small><b>Вікторія Гончарук</b></a>
          <a href="{MAPS_LINK}"><small>Адреса</small><b>{ADDR}</b></a>
          <a href="{URL_POLICY}"><small>Документи</small><b>Політика конфіденційності</b></a>
        </div>
        <p class="hours"><b>Години роботи:</b> пн–пт 09:00–18:00, вихідні за домовленістю</p>
        <nav class="fnav" aria-label="Меню"><a href="/#about">Про мене</a><a href="/#services">Послуги</a><a href="{URL_RESULTS}">Результати</a><a href="/#reviews">Відгуки</a><a href="{URL_CONTACTS}">Контакти</a><a href="{URL_POLICY}">Політика</a></nav>
      </div>
      <div class="map"><iframe src="{MAP_EMBED}" title="Карта: {ADDR}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    </div>
    <div class="copy"><span>© {NAME}</span><span class="legal-links"><a href="{URL_POLICY}">{POLICY_TITLE}</a><a href="{URL_CONTACTS}">Контакти</a></span></div>
  </div>
</footer>'''

def social_block():
    return f'''<section class="band on-ink" id="socials" style="padding:72px 0 80px">
  <div class="wrap">
    <div class="soc-head"><span class="eyebrow" style="color:var(--gold)">Соцмережі</span><h2>Мої соцмережі</h2></div>
    <div class="soc-grid">
      <a class="soc" href="{TG}" rel="me noopener"><span class="soc-ico">{ICO_TG}</span><span><small>Telegram</small><b>{TG_NICK}</b></span></a>
      <a class="soc" href="{FB}" rel="me noopener"><span class="soc-ico">{ICO_FB}</span><span><small>Facebook</small><b>Вікторія Гончарук</b></span></a>
    </div>
  </div>
</section>'''

def wrap(desc, ld, body):
    ldj = json.dumps(ld, ensure_ascii=False)
    return (f'<!-- wp:html -->\n<meta name="description" content="{desc}">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Noto+Serif+Display:wght@400;500&display=swap">\n'
            f'<style>\n{CSS}\n</style>\n<div class="gv" id="top">\n\n{body}\n\n</div>\n'
            f'<script type="application/ld+json">{ldj}</script>\n<!-- /wp:html -->\n')

# ---------- Контакти ----------
C_TITLE = f"Контакти — {NAME}"
C_DESC = "Контакти юриста по кредитам Гончарук Вікторії Анатолієвни: телефон, email, Telegram, Facebook, адреса в Києві та години роботи."
assert len(C_DESC) <= 160
ORG = {"@type": ["Organization", "LegalService"], "@id": SITE + "/#organization",
       "name": f"{NAME} — юрист по кредитам", "legalName": NAME, "url": SITE + "/", "email": EMAIL, "telephone": PHONE_TEL,
       "founder": {"@id": SITE + "/#person"},
       "address": {"@type": "PostalAddress", "streetAddress": "вул. Михайлівська, 24а", "postalCode": "01001",
                   "addressLocality": "Київ", "addressCountry": "UA"},
       "areaServed": {"@type": "Country", "name": "Україна"},
       "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}],
       "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": PHONE_TEL,
                         "email": EMAIL, "availableLanguage": ["uk"]}],
       "sameAs": [TG, FB]}
C_LD = {"@context": "https://schema.org", "@graph": [
    {"@type": "ContactPage", "@id": SITE + URL_CONTACTS + "#page", "url": SITE + URL_CONTACTS, "name": C_TITLE,
     "description": C_DESC, "inLanguage": "uk", "about": {"@id": SITE + "/#organization"},
     "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}}, ORG]}

def contacts_body():
    cards = f'''<div class="ct-grid">
      <a class="ct-card" href="tel:{PHONE_TEL}"><small>Телефон</small><b>{PHONE}</b><p>Дзвінки й повідомлення в робочий час.</p></a>
      <a class="ct-card" href="mailto:{EMAIL}"><small>Email</small><b>{EMAIL_HTML}</b><p>Для звернень і скарг. Відповідь протягом 30 днів.</p></a>
      <a class="ct-card" href="{TG}"><small>Telegram</small><b>{TG_NICK}</b><p>Найшвидший спосіб зв’язатися.</p></a>
      <a class="ct-card" href="{FB}" rel="me"><small>Facebook</small><b>Вікторія Гончарук</b><p>Повідомлення в месенджері.</p></a>
      <a class="ct-card" href="{MAPS_LINK}"><small>Адреса</small><b>{ADDR}</b><p>Зустріч за попередньою домовленістю.</p></a>
      <div class="ct-card"><small>Години роботи</small><b>Пн–пт, 09:00–18:00</b><p>Вихідні за домовленістю.</p></div>
    </div>'''
    return f'''{header("Контакти", "Напишіть у Telegram, зателефонуйте або надішліть лист. Розберемо вашу ситуацію з кредитом і підкажемо, з чого почати.", "Зв’язок · юрист по кредитам")}

<section class="band on-cream pg"><div class="wrap">
  <span class="eyebrow" style="color:var(--olive-t)">Як зв’язатися</span>
  <h2 class="sec">Оберіть зручний спосіб</h2>
  {cards}
  <div class="map-panel"><iframe title="Карта: {ADDR}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>

{social_block()}

{footer()}'''

# ---------- Політика: розмовний формат у формі запитань, від першої особи (жін.) ----------
P_DESC = "Політика конфіденційності та обробки персональних даних сайту юристки Гончарук Вікторії Анатолієвни: які дані збираю, навіщо, права відвідувачів, звернення."
assert len(P_DESC) <= 160
P_TITLE = f"{POLICY_TITLE} — {NAME}"
P_LD = {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + URL_POLICY + "#page", "url": SITE + URL_POLICY,
        "name": POLICY_TITLE, "description": P_DESC, "inLanguage": "uk", "dateModified": DATE_ISO,
        "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}, "about": {"@id": SITE + "/#organization"}}

SECTIONS = [
 ("g1", "Хто відповідає за ваші дані?", f'''<p>Цей документ пояснює, як на сайті <b>ukrjurist.com.ua</b> обробляються персональні дані. Він складений відповідно до Закону України «Про захист персональних даних» і Регламенту (ЄС) 2016/679 (GDPR).</p>
<p><b>Володілець персональних даних (контролер)</b> — це особа, яка вирішує, навіщо й як обробляти дані, і відповідає за їх захист. На цьому сайті це я, {NAME}, юристка, {ADDR}.</p>
<p>Питання про персональні дані можна поставити на <a href="mailto:{EMAIL}">{EMAIL}</a> або за телефоном <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>'''),
 ("g2", "Які дані я збираю?", '''<ul>
<li><b>Те, що ви пишете самі:</b> імʼя, телефон, нік у Telegram чи Facebook, суть звернення та документи, які ви надсилаєте, щоб я оцінила вашу ситуацію.</li>
<li><b>Відгук на сайті:</b> імʼя, оцінка, текст, за бажанням — посилання на вашу сторінку в соцмережі. У браузері зберігається ідентифікатор, щоб ви бачили власний відгук до перевірки.</li>
<li><b>Технічні дані:</b> IP-адреса, браузер, пристрій, час візиту, відкриті сторінки. Їх записують сервер і засоби захисту сайту.</li>
</ul>
<p>Особливих категорій даних (здоров’я, політичних і релігійних поглядів тощо) через сайт я не збираю й не прошу вказувати. Якщо вони потрібні у справі, ви передаєте їх добровільно в особистому зверненні.</p>'''),
 ("g3", "Навіщо мені ці дані і на якій підставі?", '''<ul>
<li><b>Щоб відповісти вам і провести первинну консультацію</b> — ваша згода (ст. 6(1)(a) GDPR) та заходи на ваше прохання до укладення договору (ст. 6(1)(b)).</li>
<li><b>Щоб показати ваш відгук</b> — ваша згода; її можна відкликати й попросити видалити відгук.</li>
<li><b>Щоб захистити сайт</b> від атак, спаму й збоїв — законний інтерес (ст. 6(1)(f)).</li>
<li><b>Щоб виконати вимоги закону</b> — юридичний обов’язок (ст. 6(1)(c)).</li>
</ul>
<p>Я не продаю дані, не використовую їх для реклами й не ухвалюю щодо вас автоматизованих рішень.</p>'''),
 ("g4", "Як довго я зберігаю дані?", '''<ul>
<li>Листування та документи за зверненням — до трьох років після завершення спілкування (загальний строк позовної давності), а коли закон вимагає, довше.</li>
<li>Відгуки — доки ви не попросите їх прибрати.</li>
<li>Технічні журнали — до 60 днів.</li>
</ul>
<p>Після цього дані видаляються або знеособлюються.</p>'''),
 ("g5", "Кому ще доступні дані?", '''<p>Окрім мене — лише тим, без кого сайт не працює:</p>
<ul>
<li><b>хостинг-провайдеру</b> — він розміщує сайт і робить резервні копії;</li>
<li><b>Cloudflare</b> — мережа доставки контенту, DNS і захист від атак;</li>
<li><b>Google</b> — карта Google Maps і шрифти Google Fonts (Google може побачити вашу IP-адресу);</li>
<li><b>Telegram і Meta (Facebook)</b> — коли ви самі переходите на ці сервіси.</li>
</ul>
<p>Частина сервісів розташована поза Україною та ЄС. Тоді передача даних відбувається на підставі стандартних договірних положень або інших гарантій за GDPR. Державним органам дані передаються лише на законну вимогу.</p>'''),
 ("g6", "Які cookie використовує сайт?", '''<p>Мінімум: технічні файли cookie для безпеки й роботи сайту, cookie форми відгуку (щоб ви бачили свій відгук до перевірки) і cookie сторонніх сервісів, які можуть встановлювати Google Maps та Cloudflare.</p>
<p>Реклами й аналітики на сайті немає. Cookie можна видалити або заборонити в налаштуваннях браузера, але форма відгуку тоді може працювати гірше.</p>'''),
 ("g7", "Які у вас права?", f'''<ul>
<li>дізнатися, чи обробляю я ваші дані, і отримати їх копію;</li>
<li>вимагати виправити неточні чи неповні дані;</li>
<li>вимагати видалити дані;</li>
<li>обмежити обробку або заперечити проти неї;</li>
<li>отримати свої дані у зручному форматі й передати іншій особі;</li>
<li>відкликати згоду в будь-який час (це не вплине на законність обробки до відкликання);</li>
<li>поскаржитися наглядовому органу.</li>
</ul>
<p>Щоб скористатися правами, напишіть на <a href="mailto:{EMAIL}">{EMAIL}</a>. Я відповім протягом 30 днів і, можливо, попрошу підтвердити особу, щоб не передати дані стороннім.</p>'''),
 ("g8", "Як подати звернення чи скаргу?", f'''<p>Звернення, запити й скарги щодо персональних даних приймаю на <a href="mailto:{EMAIL}">{EMAIL}</a>. Напишіть, як до вас звертатися, куди надіслати відповідь і в чому питання.</p>
<p>Якщо вважаєте, що ваші права порушено, можна звернутися до Уповноваженого Верховної Ради України з прав людини (<a href="https://ombudsman.gov.ua" target="_blank" rel="noopener">ombudsman.gov.ua</a>), а в країнах ЄС — до органу із захисту даних за місцем проживання.</p>'''),
 ("g9", "Як захищені дані?", '''<p>Сайт працює через шифроване з’єднання (HTTPS), доступ до адміністрування обмежений і захищений від підбору паролів, робляться резервні копії. Жоден канал в інтернеті не безпечний повністю, тож не надсилайте через форми й месенджери зайвого, наприклад реквізитів банківських карток.</p>'''),
 ("g10", "А якщо відвідувач неповнолітній?", '''<p>Сайт розрахований на дорослих. Дані осіб до 16 років я свідомо не збираю; якщо така інформація до мене потрапила, видалю її після вашого звернення.</p>'''),
 ("g11", "Як змінюється політика?", f'''<p>Я можу її оновлювати. Остання редакція завжди на цій сторінці й діє від {DATE_HUMAN}.</p>'''),
]

def policy_body():
    toc = "".join(f'<a href="#{i}">{t}</a>' for i, t, _ in SECTIONS)
    secs = "".join(f'<h2 id="{i}">{t}</h2>\n{b}\n' for i, t, b in SECTIONS)
    return f'''{header("Політика конфіденційності", "Пояснюю простою мовою, які персональні дані збирає цей сайт, навіщо, як довго я їх зберігаю і як ви можете скористатися своїми правами.", "Конфіденційність · юристка по кредитам")}

<section class="band on-cream pg"><div class="wrap">
  <div class="legal-wrap">
    <nav class="toc" aria-label="Зміст"><b>Зміст</b>{toc}</nav>
    <div class="legal"><span class="upd">Редакція від {DATE_HUMAN}</span>
{secs}</div>
  </div>
</div></section>

{footer()}'''

PAGES = {
    "kontakty": dict(title=C_TITLE, desc=C_DESC, ld=C_LD, body=contacts_body, file="kontakty.wp.html"),
    "polityka-konfidentsiinosti": dict(title=P_TITLE, desc=P_DESC, ld=P_LD, body=policy_body, file="polityka.wp.html"),
}

def call(method, url, data=None):
    cmd = ["curl", "-sS", "-m", "90", "-X", method, url, "-H", "Content-Type: application/json"]
    if data is not None:
        cmd += ["--data-binary", "@-"]
    out = subprocess.run(cmd, input=json.dumps(data).encode() if data is not None else None, capture_output=True).stdout
    return json.loads(out)

if __name__ == "__main__":
    for slug, p in PAGES.items():
        html = wrap(p["desc"], p["ld"], p["body"]())
        (R / p["file"]).write_text(html, encoding="utf-8")
        print(p["file"], len(html))
        if "--publish" in sys.argv:
            found = call("GET", f"{SITE}/wp-json/wp/v2/pages?slug={slug}&status=any&context=edit&_fields=id,status")
            payload = {"title": p["title"], "slug": slug, "template": "page-blank", "content": html,
                       "status": "publish" if "--live" in sys.argv else "draft"}
            if found:
                if found[0]["status"] == "publish" and "--live" not in sys.argv:
                    payload.pop("status")
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages/{found[0]['id']}", payload)
            else:
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages", payload)
            print(" ->", d.get("id"), d.get("status"), d.get("link"), d.get("code"), d.get("message"))
