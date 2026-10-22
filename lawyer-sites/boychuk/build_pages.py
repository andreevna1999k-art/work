#!/usr/bin/env python3
"""Бойчук (legaladdress.com.ua): сторінки «Контакти» і «Політика конфіденційності» у стилі S1 Mahogany.
Оболонка (CSS, меню, футер) береться з уже опублікованої сторінки результатів (page48-published.html) + pages.css.
  python3 build_pages.py                 -> kontakty.wp.html, polityka.wp.html
  python3 build_pages.py --publish       -> створює/оновлює ЧЕРНЕТКИ в WP (авторизацію додає проксі)
"""
import json, re, subprocess, sys, pathlib, urllib.parse

R = pathlib.Path(__file__).parent
SITE = "https://legaladdress.com.ua"
NAME = "Бойчук Артем Валерійович"
EMAIL = "artem-yrist@legaladdress.com.ua"
EMAIL_HTML = EMAIL.replace("@", "<wbr>@")
PHONE_TEL, PHONE = "+380754921980", "+38 075 492 19 80"
TG, TG_NICK = "https://t.me/artem_adwokat", "@artem_adwokat"
FB = "https://www.facebook.com/profile.php?id=100088336967953"
ADDR = "02055, вул. Княжий Затон, 2/30, Київ"
ADDR_Q = urllib.parse.quote(ADDR)
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + ADDR_Q
MAP_EMBED = "https://www.google.com/maps?q=" + ADDR_Q + "&hl=uk&output=embed"
URL_CONTACTS, URL_POLICY, URL_RESULTS = "/kontakty/", "/polityka-konfidentsiinosti/", "/rezultaty-roboty/"
POLICY_TITLE = "Політика конфіденційності та обробки персональних даних"
DATE_HUMAN, DATE_ISO = "22 жовтня 2026 року", "2026-10-22"

# ---------- оболонка з опублікованої сторінки ----------
src = (R / "page48-published.html").read_text(encoding="utf-8")
a = src.index("<style>") + 7
BASE_CSS = src[a: src.index("</style>", a)]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Forum&family=Source+Sans+3:wght@400;600&display=swap">')
CSS = BASE_CSS + "\n" + (R / "pages.css").read_text(encoding="utf-8")
FULL = ".bz{width:100%;margin:0;min-height:100vh}html,body{margin:0!important;padding:0!important;background:#F5EEE4!important}html{scroll-behavior:smooth}"

ICO_TG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.5 4.3 2.9 11.5c-1.3.5-1.3 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.8.8.8.5 0 .8-.2 1.1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.2-.5-1.8-1.5-1.4zM8.5 13.6l9.6-6c.5-.3.9-.1.5.2l-7.8 7-.3 3.2z"/></svg>'
ICO_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.5-3.2h-3.2V7.7c0-.9.3-1.6 1.7-1.6h1.6V3.2c-.3 0-1.3-.1-2.4-.1-2.5 0-4.1 1.5-4.1 4.2v2.5H7.5V13h2.8v8z"/></svg>'

NAV = f'''<div class="nav"><input type="checkbox" id="bzm" class="menu-cb" aria-hidden="true" tabindex="-1">
    <a class="logo" href="/">Бойчук А. В.</a>
    <ul><li><a href="/#about">Про мене</a></li><li><a href="/#services">Послуги</a></li><li><a href="{URL_RESULTS}"%CUR_R%>Результати</a></li><li><a href="/#reviews">Відгуки</a></li><li><a href="{URL_CONTACTS}"%CUR_C%>Контакти</a></li></ul>
    <a class="btn sm" href="{TG}" target="_blank" rel="noopener">Telegram</a><label for="bzm" class="burger" aria-label="Меню"><i></i></label>
  </div>'''

BURGER_JS = '<script>(function(){var r=document.getElementById("top");if(!r)return;var cb=r.querySelector("#bzm");if(!cb)return;r.querySelectorAll(".nav ul a").forEach(function(a){a.addEventListener("click",function(){cb.checked=false})});document.addEventListener("keydown",function(e){if(e.key==="Escape")cb.checked=false})})();</script>'

def nav(cur_contacts=False, cur_results=False, cur_policy=False):
    return NAV.replace("%CUR_C%", ' class="cur"' if cur_contacts else "").replace("%CUR_R%", ' class="cur"' if cur_results else "").replace("%CUR_P%", ' class="cur"' if cur_policy else "")

def social_block(dark=True):
    return f'''<section id="socials"><div class="wrap">
<div class="panel on-brown pad">
  <div class="soc-head"><div><span class="rule"></span><h2>Мої соцмережі</h2></div><p>Пишіть у зручний месенджер або стежте за мною в соцмережах.</p></div>
  <div class="soc-grid">
    <a class="soc" href="{TG}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_TG}</span><span><small>Telegram</small><b>{TG_NICK}</b></span></a>
    <a class="soc" href="{FB}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_FB}</span><span><small>Facebook</small><b>Профіль у Facebook</b></span></a>
  </div>
</div>
</div></section>'''

def footer():
    return f'''<!-- ФУТЕР · КОНТАКТИ -->
<section id="contacts"><div class="wrap">
<div class="panel footer-panel">
  <div class="info">
    <span class="rule"></span>
    <h2 style="color:var(--cream)">Контакти</h2>
    <div class="links">
      <a href="tel:{PHONE_TEL}"><small>Телефон</small><b>{PHONE}</b></a>
      <a href="mailto:{EMAIL}"><small>Email</small><b>{EMAIL_HTML}</b></a>
      <a href="{TG}" target="_blank" rel="noopener"><small>Telegram</small><b>{TG_NICK}</b></a>
      <a href="{FB}" target="_blank" rel="noopener me"><small>Facebook</small><b>Профіль у Facebook</b></a>
      <a href="{MAPS_LINK}" target="_blank" rel="noopener"><small>Адреса</small><b>{ADDR}</b></a>
      <a href="{URL_POLICY}"><small>Документи</small><b>Політика конфіденційності</b></a>
    </div>
    <div class="hours"><b>Години роботи:</b> пн–пт з 09:00 до 18:00, на вихідних — за домовленістю.</div>
    <nav class="fnav" aria-label="Меню"><a href="/#about">Про мене</a><a href="/#services">Послуги</a><a href="{URL_RESULTS}">Результати</a><a href="/#reviews">Відгуки</a><a href="{URL_CONTACTS}">Контакти</a><a href="{URL_POLICY}">Політика</a></nav>
  </div>
  <div class="map"><iframe title="Мапа: {ADDR}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div>
<div class="foot"><span>© {NAME}</span><span class="legal-links"><a href="{URL_POLICY}">{POLICY_TITLE}</a><a href="{URL_CONTACTS}">Контакти</a></span></div>
</div></section>'''

def hero(h1_html, lead, badge, cls=""):
    return f'''<section class="hero"><div class="wrap">
<div class="panel rp-hero">
  {nav(cur_contacts=(cls=="contacts"), cur_policy=(cls=="legal"))}
  <div class="rp-head{' legal-h' if cls=='legal' else ''}"><span class="res-badge">{badge}</span>
    <h1>{h1_html}</h1>
    <p class="lead">{lead}</p>
  </div>
</div>
</div></section>'''

def wrap_page(title, desc, ld, body):
    ldj = json.dumps(ld, ensure_ascii=False)
    return (f'<!-- wp:html -->\n<meta name="description" content="{desc}">\n<script type="application/ld+json">{ldj}</script>\n'
            f'{FONTS}\n<style>\n{CSS}\n</style>\n<style>{FULL}</style>\n<div class="bz" lang="uk" id="top">\n\n{body}\n\n</div>\n{BURGER_JS}\n<!-- /wp:html -->\n')

# ---------- Контакти ----------
C_DESC = ("Контакти юриста по кредитам Бойчука Артема Валерійовича: телефон, email, Telegram, Facebook, адреса офісу в Києві та години роботи.")
assert len(C_DESC) <= 160, len(C_DESC)
C_TITLE = "Контакти"
ORG = {
    "@context": "https://schema.org",
    "@type": ["Organization", "LegalService"],
    "@id": SITE + "/#organization",
    "name": f"{NAME} — юрист по кредитам",
    "legalName": NAME,
    "description": "Юридична допомога позичальникам: аналіз кредитних договорів, переговори з банками, захист від колекторів, представництво в суді.",
    "url": SITE + "/",
    "email": EMAIL,
    "telephone": PHONE_TEL,
    "image": SITE + "/wp-content/uploads/2026/10/boychuk-portrait-office.jpg",
    "founder": {"@id": SITE + "/#boychuk"},
    "address": {"@type": "PostalAddress", "streetAddress": "вул. Княжий Затон, 2/30", "postalCode": "02055",
                "addressLocality": "Київ", "addressCountry": "UA"},
    "areaServed": {"@type": "Country", "name": "Україна"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}],
    "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": PHONE_TEL, "email": EMAIL,
                      "availableLanguage": ["uk"]}],
    "sameAs": [TG, FB],
}
C_LD = {"@context": "https://schema.org", "@graph": [
    {"@type": "ContactPage", "@id": SITE + URL_CONTACTS + "#page", "url": SITE + URL_CONTACTS, "name": C_TITLE,
     "description": C_DESC, "inLanguage": "uk", "about": {"@id": SITE + "/#organization"},
     "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}},
    {k: v for k, v in ORG.items() if k != "@context"}]}

def contacts_body():
    cards = f'''<div class="ct-grid">
  <a class="ct-card" href="tel:{PHONE_TEL}"><small>Телефон</small><b>{PHONE}</b><p>Дзвінки й повідомлення в робочий час.</p></a>
  <a class="ct-card" href="mailto:{EMAIL}"><small>Email</small><b>{EMAIL_HTML}</b><p>Для звернень і скарг. Відповідаємо протягом 30 днів.</p></a>
  <a class="ct-card" href="{TG}" target="_blank" rel="noopener"><small>Telegram</small><b>{TG_NICK}</b><p>Найшвидший спосіб зв’язку.</p></a>
  <a class="ct-card" href="{FB}" target="_blank" rel="noopener me"><small>Facebook</small><b>Профіль у Facebook</b><p>Повідомлення в месенджері.</p></a>
  <a class="ct-card" href="{MAPS_LINK}" target="_blank" rel="noopener"><small>Адреса</small><b>{ADDR}</b><p>Зустріч за попередньою домовленістю.</p></a>
  <div class="ct-card"><small>Години роботи</small><b>Пн–пт, 09:00–18:00</b><p>На вихідних — за домовленістю.</p></div>
</div>'''
    return f'''{hero("Контакти", "Зверніться до мене зручним способом: напишіть у Telegram, зателефонуйте або надішліть лист. Розберемо вашу ситуацію з кредитом.", "Зв’язок", "contacts")}

<section class="sec-gap"><div class="wrap"><div class="panel on-white pad">
{cards}
<div class="center" style="text-align:center;margin-top:34px"><a class="btn" href="{TG}" target="_blank" rel="noopener">Написати в Telegram</a></div>
</div></div></section>

<section><div class="wrap"><div class="panel map-panel"><iframe title="Мапа: {ADDR}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></div></section>

{social_block()}

{footer()}'''

# ---------- Політика ----------
P_DESC = ("Політика конфіденційності та обробки персональних даних сайту юриста Бойчука Артема Валерійовича: які дані збираємо, навіщо, права відвідувачів, скарги.")
assert len(P_DESC) <= 160, len(P_DESC)
P_TITLE = POLICY_TITLE
P_LD = {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + URL_POLICY + "#page", "url": SITE + URL_POLICY,
        "name": POLICY_TITLE, "description": P_DESC, "inLanguage": "uk", "dateModified": DATE_ISO,
        "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}, "about": {"@id": SITE + "/#organization"}}

SECTIONS = [
 ("s1", "1. Хто відповідає за ваші дані", f'''<p>Ця Політика пояснює, як сайт <b>legaladdress.com.ua</b> збирає, використовує та захищає персональні дані. Вона складена відповідно до Закону України «Про захист персональних даних» та вимог Регламенту (ЄС) 2016/679 (GDPR).</p>
<p><b>Володілець персональних даних (контролер)</b> — це той, хто вирішує, навіщо й як обробляються ваші дані, і відповідає за їх захист. На цьому сайті це {NAME}, юрист, {ADDR}.</p>
<p>Email для звернень, запитів і скарг щодо персональних даних: <a href="mailto:{EMAIL}">{EMAIL}</a>. Телефон: <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>'''),
 ("s2", "2. Які дані ми збираємо", '''<p>Ми збираємо лише ті дані, які потрібні для зв’язку з вами та роботи сайту:</p>
<ul>
<li><b>Дані, які ви надаєте самі:</b> ім’я, номер телефону, нік у Telegram або Facebook, зміст повідомлення чи запиту, а також документи, які ви надсилаєте для консультації.</li>
<li><b>Дані форми відгуку:</b> ім’я, оцінка, текст відгуку, за бажанням посилання на соцмережу. Форма записує в браузер ідентифікатор відвідувача (cookie), щоб ви бачили свій відгук до його перевірки.</li>
<li><b>Технічні дані:</b> IP-адреса, тип браузера й пристрою, дата і час відвідування, відвідані сторінки. Їх фіксують сервери сайту та засоби захисту.</li>
</ul>
<p>Ми не збираємо особливі категорії даних (здоров’я, політичні погляди тощо) через сайт і не просимо вас їх вказувати. Якщо вони потрібні для вирішення вашої справи, ви передаєте їх добровільно у зверненні.</p>'''),
 ("s3", "3. Навіщо та на якій підставі", '''<ul>
<li><b>Відповідь на ваш запит і надання консультації</b> — ваша згода (ст. 6(1)(a) GDPR) та вжиття заходів на ваш запит до укладення договору (ст. 6(1)(b)).</li>
<li><b>Публікація відгуку</b> — ваша згода. Ви можете її відкликати й попросити видалити відгук.</li>
<li><b>Безпека й стабільна робота сайту</b> (захист від атак, спаму) — законний інтерес (ст. 6(1)(f)).</li>
<li><b>Виконання вимог законодавства</b> — юридичний обов’язок (ст. 6(1)(c)).</li>
</ul>
<p>Ми не продаємо ваші дані й не використовуємо їх для автоматизованого прийняття рішень чи профілювання.</p>'''),
 ("s4", "4. Скільки зберігаємо", '''<ul>
<li>Листування й звернення — до трьох років з моменту завершення спілкування (загальний строк позовної давності), якщо закон не вимагає більшого.</li>
<li>Відгуки — доти, доки ви не попросите їх видалити.</li>
<li>Технічні журнали сервера й захисту — до 12 місяців.</li>
</ul>
<p>Після спливу строку дані видаляються або знеособлюються.</p>'''),
 ("s5", "5. Кому ми можемо передавати дані", '''<p>Доступ до даних мають лише власник сайту та постачальники послуг, без яких сайт не працює:</p>
<ul>
<li><b>Хостинг-провайдер</b> — розміщення сайту й резервні копії.</li>
<li><b>Cloudflare</b> — мережа доставки контенту (CDN), DNS і захист сайту від атак.</li>
<li><b>Google</b> — карта Google Maps і шрифти Google Fonts на сторінках (Google може отримувати вашу IP-адресу).</li>
<li><b>Telegram та Meta (Facebook)</b> — коли ви самі переходите за посиланнями на ці сервіси; їхні політики діють окремо.</li>
</ul>
<p>Частина цих сервісів може обробляти дані за межами України та ЄС. У такому разі передача відбувається на підставі стандартних договірних положень або інших гарантій, передбачених GDPR. Державним органам дані надаються лише за законною вимогою.</p>'''),
 ("s6", "6. Файли cookie", '''<p>Сайт використовує мінімум файлів cookie:</p>
<ul>
<li><b>технічні файли cookie</b> — потрібні для роботи й безпеки сайту (захист від зламів, підтримка сесії адміністратора);</li>
<li><b>файл cookie форми відгуку</b> — ідентифікатор, щоб ви бачили свій відгук до його перевірки;</li>
<li><b>файли cookie сторонніх сервісів</b> — можуть встановлювати карта Google Maps і Cloudflare.</li>
</ul>
<p>Рекламні й аналітичні файли cookie ми не застосовуємо. Ви можете видалити файли cookie або заборонити їх у налаштуваннях браузера, але деякі функції (наприклад, форма відгуку) можуть працювати гірше.</p>'''),
 ("s7", "7. Ваші права", f'''<p>Ви маєте право:</p>
<ul>
<li>отримати підтвердження, чи обробляємо ми ваші дані, і копію цих даних (доступ);</li>
<li>виправити неточні або неповні дані;</li>
<li>вимагати видалення даних («право бути забутим»);</li>
<li>обмежити обробку або заперечити проти неї;</li>
<li>отримати свої дані у зручному форматі та передати іншому володільцеві (переносимість);</li>
<li>відкликати згоду в будь-який момент — це не вплине на законність обробки до відкликання;</li>
<li>подати скаргу до наглядового органу.</li>
</ul>
<p>Щоб скористатися правами, напишіть на <a href="mailto:{EMAIL}">{EMAIL}</a>. Ми відповімо протягом 30 днів. Іноді нам потрібно буде перевірити, що запит надійшов саме від вас.</p>'''),
 ("s8", "8. Скарги та звернення", f'''<p>Скарги, звернення й запити щодо обробки персональних даних приймаються на email <a href="mailto:{EMAIL}">{EMAIL}</a>. Вкажіть ваше ім’я, контакт для відповіді й суть питання.</p>
<p>Якщо ви вважаєте, що ми порушили ваші права, ви можете звернутися до наглядового органу: в Україні — Уповноваженого Верховної Ради України з прав людини (<a href="https://ombudsman.gov.ua" target="_blank" rel="noopener">ombudsman.gov.ua</a>), у країнах ЄС — до органу із захисту даних за місцем проживання.</p>'''),
 ("s9", "9. Безпека", '''<p>Ми захищаємо дані технічними й організаційними заходами: шифроване з’єднання (HTTPS), обмежений доступ до адміністрування сайту, захист від підбору паролів і атак, резервне копіювання. Жоден спосіб передачі через інтернет не буває абсолютно безпечним, тому не надсилайте через форми й месенджери зайвих даних (наприклад, повних реквізитів карток).</p>'''),
 ("s10", "10. Діти", '''<p>Сайт не призначений для осіб віком до 16 років, і ми свідомо не збираємо їхні дані. Якщо ви вважаєте, що дитина надіслала нам свої дані, напишіть нам, і ми їх видалимо.</p>'''),
 ("s11", "11. Зміни до Політики", f'''<p>Ми можемо оновлювати цю Політику. Актуальна редакція завжди доступна на цій сторінці. Поточна редакція діє від {DATE_HUMAN}.</p>'''),
]

def policy_body():
    toc = "".join(f'<a href="#{i}">{t}</a>' for i, t, _ in SECTIONS)
    secs = "".join(f'<h2 id="{i}">{t}</h2>\n{b}\n' for i, t, b in SECTIONS)
    return f'''{hero(POLICY_TITLE, "Пояснюємо простою мовою, які персональні дані збирає сайт, навіщо, як довго їх зберігаємо і як ви можете скористатися своїми правами.", "Конфіденційність", "legal")}

<section class="sec-gap"><div class="wrap"><div class="panel on-white pad">
<div class="legal-wrap">
  <nav class="toc" aria-label="Зміст"><b>Зміст</b>{toc}</nav>
  <div class="legal"><span class="upd">Редакція від {DATE_HUMAN}</span>
{secs}</div>
</div>
</div></div></section>

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
        html = wrap_page(p["title"], p["desc"], p["ld"], p["body"]())
        (R / p["file"]).write_text(html, encoding="utf-8")
        print(p["file"], len(html))
        if "--publish" in sys.argv:
            found = call("GET", f"{SITE}/wp-json/wp/v2/pages?slug={slug}&status=any&context=edit&_fields=id,status")
            payload = {"title": p["title"], "slug": slug, "template": "page-blank", "content": html}
            if not found:
                payload["status"] = "draft"
            if found:
                if found[0]["status"] != "draft" and "--update" not in sys.argv:
                    sys.exit(f"{slug}: уже опублікована, не чіпаю")
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages/{found[0]['id']}", payload)
            else:
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages", payload)
            print(" ->", d.get("id"), d.get("status"), d.get("link"), d.get("code"), d.get("message"))
