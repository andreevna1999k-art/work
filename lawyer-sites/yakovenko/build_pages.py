#!/usr/bin/env python3
"""Яковенко Дмитро (urists.com.ua), стиль S3 «Navy Gold»: сторінки «Контакти» і «Політика конфіденційності».
CSS береться з живої головної та сторінки результатів (base.css) + pages.css.
  python3 build_pages.py                  -> kontakty.wp.html, polityka.wp.html
  python3 build_pages.py --publish        -> ЧЕРНЕТКИ у WP (авторизацію додає проксі)
  python3 build_pages.py --publish --live -> статус publish (лише за командою «публікуй»)
"""
import json, subprocess, sys, pathlib, urllib.parse

R = pathlib.Path(__file__).parent
SITE = "https://urists.com.ua"
NAME = "Яковенко Дмитро"
EMAIL = "dmytro-yrist@urists.com.ua"
EMAIL_HTML = EMAIL.replace("@", "<wbr>@")
PHONE_TEL, PHONE = "+380751462697", "+38 075 146 26 97"
TG, TG_NICK = "https://t.me/yakovenko_lawyer", "@yakovenko_lawyer"
FB = "https://www.facebook.com/profile.php?id=100087644206123"
ADDR = "01024, вул. Басейна, 9, к.3, Київ"
ADDR_Q = urllib.parse.quote("вул. Басейна, 9, Київ, 01024")
MAP_EMBED = "https://www.google.com/maps?q=" + ADDR_Q + "&hl=uk&z=16&output=embed"
URL_CONTACTS, URL_POLICY, URL_RESULTS = "/kontakty/", "/polityka-konfidentsiinosti/", "/rezultaty-roboty/"
POLICY_TITLE = "Політика конфіденційності та обробки персональних даних"
DATE_HUMAN, DATE_ISO = "22 жовтня 2026 року", "2026-10-22"
CSS = (R / "base.css").read_text(encoding="utf-8") + "\n" + (R / "pages.css").read_text(encoding="utf-8")

ARR = '<i><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i>'
ICO_TG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.5 4.3 2.9 11.5c-1.3.5-1.3 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.8.8.8.5 0 .8-.2 1.1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.2-.5-1.8-1.5-1.4zM8.5 13.6l9.6-6c.5-.3.9-.1.5.2l-7.8 7-.3 3.2z"/></svg>'
ICO_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.5-3.2h-3.2V7.7c0-.9.3-1.6 1.7-1.6h1.6V3.2c-.3 0-1.3-.1-2.4-.1-2.5 0-4.1 1.5-4.1 4.2v2.5H7.5V13h2.8v8z"/></svg>'

def ct(svg_path, label, val_html, em=None):
    e = f"<em>{em}</em>" if em else ""
    return (f'<div class="ct"><svg viewBox="0 0 48 48">{svg_path}</svg><div><small>{label}</small>{val_html}{e}</div></div>')

P_PIN = '<path d="M24 44s14-12.5 14-24a14 14 0 0 0-28 0c0 11.5 14 24 14 24z"/><circle cx="24" cy="20" r="5"/>'
P_PHONE = '<path d="M12 6h8l4 10-5 3a22 22 0 0 0 10 10l3-5 10 4v8a4 4 0 0 1-4 4C22 40 8 26 8 10a4 4 0 0 1 4-4z"/>'
P_CLOCK = '<circle cx="24" cy="24" r="16"/><path d="M24 14v10l7 4"/>'
P_TG = '<path d="M42 8L6 22l10 4 4 12 6-7 9 7z"/><path d="M16 26L42 8"/>'
P_MAIL = '<rect x="6" y="10" width="36" height="28" rx="4"/><path d="m6 14 18 13 18-13"/>'
P_DOC = '<rect x="10" y="6" width="28" height="36" rx="3"/><path d="M17 16h14M17 23h14M17 30h8"/>'
P_FB = '<circle cx="24" cy="24" r="16"/><path d="M26 38V25h4l1-5h-5v-3c0-1.5.6-2 2-2h3v-4.5c-.6 0-2-.2-3.6-.2-3.6 0-5.4 2-5.4 5.6V20h-4v5h4v13z"/>'

def header(h1, lead, eyebrow, cta=True):
    acts = (f'<div class="acts"><a class="btn" href="{TG}" target="_blank" rel="noopener">Написати в Telegram{ARR}</a>'
            f'<a class="btn line" href="/">На головну{ARR}</a></div>') if cta else f'<div class="acts"><a class="btn line" href="/">На головну{ARR}</a></div>'
    return f'''<section class="panel hero sub dark">
  <div class="sub-ring"></div>
  <div class="nav"><input type="checkbox" id="ykm" class="menu-cb" aria-hidden="true" tabindex="-1">
    <a class="logo" href="/"><b>Яковенко Дмитро</b><span>Юрист</span></a>
    <nav>
      <a href="/#about">Про мене</a>
      <a href="/#services">Послуги</a>
      <a href="{URL_RESULTS}">Результати</a>
      <a href="/#reviews">Відгуки</a>
      <a href="{URL_CONTACTS}">Контакти</a>
    </nav>
    <a class="btn sm" href="{TG}" target="_blank" rel="noopener"><span class="lg">Написати в Telegram</span><span class="sh">Telegram</span>{ARR}</a><label for="ykm" class="burger" aria-label="Меню"><i></i></label>
  </div>
  <div class="sub-body">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {acts}
  </div>
</section>'''

def footer():
    items = "\n        ".join([
        ct(P_PIN, "Адреса", '<span class="v">01024, вул. Басейна, 9, к.3</span>', "Київ"),
        ct(P_PHONE, "Телефон", f'<a href="tel:{PHONE_TEL}">{PHONE}</a>'),
        ct(P_MAIL, "Email", f'<a href="mailto:{EMAIL}">{EMAIL_HTML}</a>'),
        ct(P_CLOCK, "Години роботи", '<span class="v">Пн-пт: 09:00-18:00</span>', "У вихідні за домовленістю"),
        ct(P_TG, "Telegram", f'<a href="{TG}" target="_blank" rel="noopener">{TG_NICK}</a>'),
        ct(P_DOC, "Документи", f'<a href="{URL_POLICY}">Політика конфіденційності</a>'),
    ])
    return f'''<footer class="contacts dark" id="contacts">
  <div class="in">
    <span class="eyebrow">Контакти</span>
    <h2 class="t">Зв'яжіться зі мною</h2>
    <div class="ct-g">
      <div class="ct-list">
        {items}
        <div style="margin-top:6px"><a class="btn" href="{TG}" target="_blank" rel="noopener">Написати в Telegram{ARR}</a></div>
      </div>
      <div class="map"><iframe title="Мапа: вул. Басейна, 9, Київ" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    </div>
    <nav class="fnav" aria-label="Меню"><a href="/#about">Про мене</a><a href="/#services">Послуги</a><a href="{URL_RESULTS}">Результати</a><a href="/#reviews">Відгуки</a><a href="{URL_CONTACTS}">Контакти</a><a href="{URL_POLICY}">Політика</a></nav>
    <div class="bottom"><span>© 2026 Яковенко Дмитро &#45; юрист по кредитам</span><span>Інформація на сайті має ознайомчий характер і не є юридичною консультацією.</span><span class="legal-links"><a href="{URL_POLICY}">{POLICY_TITLE}</a><a href="{URL_CONTACTS}">Контакти</a></span></div>
  </div>
</footer>'''

BURGER_JS = '<script>(function(){var r=document.querySelector(".yk");if(!r)return;var cb=r.querySelector("#ykm");if(!cb)return;r.querySelectorAll(".nav nav a").forEach(function(a){a.addEventListener("click",function(){cb.checked=false})});document.addEventListener("keydown",function(e){if(e.key==="Escape")cb.checked=false})})();</script>'

def wrap(desc, ld, body):
    ldj = json.dumps(ld, ensure_ascii=False)
    return (f'<!-- wp:html -->\n<meta name="description" content="{desc}">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Prata&display=swap">\n'
            f'<style>\n{CSS}\n</style>\n\n<div class="yk" id="top">\n\n{body}\n\n</div>\n\n'
            f'<script type="application/ld+json">{ldj}</script>\n{BURGER_JS}\n<!-- /wp:html -->\n')

# ---------- Контакти ----------
C_TITLE = f"Контакти — {NAME}"
C_DESC = "Контакти юриста по кредитам Яковенка Дмитра: телефон, email, Telegram, Facebook, адреса офісу в Києві та години роботи."
assert len(C_DESC) <= 160
ORG = {"@type": ["Organization", "LegalService"], "@id": SITE + "/#organization",
       "name": f"{NAME} — юрист по кредитам", "legalName": NAME,
       "url": SITE + "/", "email": EMAIL, "telephone": PHONE_TEL,
       "founder": {"@id": SITE + "/#person"},
       "address": {"@type": "PostalAddress", "streetAddress": "вул. Басейна, 9, к.3", "postalCode": "01024",
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
    cards = f'''<div class="cc-grid">
      <a class="cc" href="tel:{PHONE_TEL}"><small>Телефон</small><b>{PHONE}</b><p>Дзвінки й повідомлення в робочий час.</p></a>
      <a class="cc" href="mailto:{EMAIL}"><small>Email</small><b>{EMAIL_HTML}</b><p>Для звернень і скарг. Відповідь протягом 30 днів.</p></a>
      <a class="cc" href="{TG}" target="_blank" rel="noopener"><small>Telegram</small><b>{TG_NICK}</b><p>Найшвидший спосіб звʼязатися.</p></a>
      <a class="cc" href="{FB}" target="_blank" rel="noopener me"><small>Facebook</small><b>Профіль у Facebook</b><p>Повідомлення в месенджері.</p></a>
      <a class="cc" href="https://www.google.com/maps/search/?api=1&query={ADDR_Q}" target="_blank" rel="noopener"><small>Адреса</small><b>{ADDR}</b><p>Зустріч за попередньою домовленістю.</p></a>
      <div class="cc"><small>Години роботи</small><b>Пн-пт, 09:00-18:00</b><p>У вихідні за домовленістю.</p></div>
    </div>'''
    return f'''{header("Контакти", "Напишіть у Telegram, зателефонуйте або надішліть лист. Розберемо вашу ситуацію з кредитом і підкажемо, з чого почати.", "Звʼязок · Яковенко Дмитро")}

<section class="pg"><div class="in">
  <span class="eyebrow">Як звʼязатися</span>
  <h2 class="t">Оберіть зручний спосіб</h2>
  {cards}
  <div class="map-box"><iframe title="Мапа: вул. Басейна, 9, Київ" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>

<section><div class="in"><div class="soc-panel" id="socials">
  <span class="eyebrow">Соцмережі</span>
  <h2 class="t">Мої соцмережі</h2>
  <div class="soc-grid">
    <a class="soc" href="{TG}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_TG}</span><span><small>Telegram</small><b>{TG_NICK}</b></span></a>
    <a class="soc" href="{FB}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_FB}</span><span><small>Facebook</small><b>Профіль у Facebook</b></span></a>
  </div>
</div></div></section>

{footer()}'''

# ---------- Політика: офіційний нумерований формат (відрізняється від інших сайтів) ----------
P_DESC = "Політика конфіденційності та обробки персональних даних сайту юриста Яковенка Дмитра: мета, підстави, строки, права суб'єктів, порядок подання звернень."
assert len(P_DESC) <= 160
P_TITLE = f"{POLICY_TITLE} — {NAME}"
P_LD = {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + URL_POLICY + "#page", "url": SITE + URL_POLICY,
        "name": POLICY_TITLE, "description": P_DESC, "inLanguage": "uk", "dateModified": DATE_ISO,
        "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}, "about": {"@id": SITE + "/#organization"}}

def cl(items):
    return "".join(f'<p><span class="n">{n}</span>{t}</p>' for n, t in items)

SECTIONS = [
 ("d1", "1. Загальні положення", cl([
  ("1.1.", "Ця Політика визначає порядок обробки персональних даних відвідувачів сайту <b>urists.com.ua</b> (далі — Сайт) і складена відповідно до Закону України «Про захист персональних даних» та Регламенту (ЄС) 2016/679 (GDPR)."),
  ("1.2.", f"<b>Володілець персональних даних (контролер)</b> — особа, яка визначає мету та засоби обробки персональних даних. Володільцем є {NAME}, юрист, {ADDR} (далі — Юрист)."),
  ("1.3.", f"Контакти для звернень: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>, <a href=\"tel:{PHONE_TEL}\">{PHONE}</a>."),
  ("1.4.", "Користуючись Сайтом і надсилаючи Юристу повідомлення, ви підтверджуєте, що ознайомилися з цією Політикою.")])),
 ("d2", "2. Категорії персональних даних", cl([
  ("2.1.", "Дані, які надає сам відвідувач: імʼя, номер телефону, нік у Telegram або Facebook, зміст звернення, документи, надіслані для попередньої оцінки ситуації."),
  ("2.2.", "Дані відгуку: імʼя, оцінка, текст відгуку, за бажанням посилання на сторінку в соцмережі, а також ідентифікатор браузера (cookie) для відображення власного відгуку до його модерації."),
  ("2.3.", "Технічні дані: IP-адреса, тип браузера та пристрою, дата й час запитів, відвідані сторінки (журнали сервера й засобів захисту)."),
  ("2.4.", "Особливі категорії даних (стан здоровʼя, політичні, релігійні погляди тощо) Юрист через Сайт не збирає. Якщо такі дані потрібні для справи, їх передає сам суб'єкт у зверненні.")])),
 ("d3", "3. Мета та правові підстави обробки", cl([
  ("3.1.", "Розгляд звернень і надання попередньої консультації — згода суб'єкта (п. (a) ч. 1 ст. 6 GDPR) та заходи до укладення договору на прохання суб'єкта (п. (b))."),
  ("3.2.", "Публікація відгуку — згода суб'єкта, яку можна відкликати."),
  ("3.3.", "Забезпечення безпеки й справної роботи Сайту — законний інтерес (п. (f))."),
  ("3.4.", "Виконання вимог законодавства — юридичний обовʼязок (п. (c)). Автоматизованого прийняття рішень і профілювання не здійснюється, дані не продаються.")])),
 ("d4", "4. Строки зберігання", cl([
  ("4.1.", "Листування та документи за зверненням зберігаються до трьох років після завершення спілкування (загальний строк позовної давності), якщо закон не встановлює довший строк."),
  ("4.2.", "Відгуки зберігаються до запиту про їх видалення."),
  ("4.3.", "Технічні журнали зберігаються до 90 днів."),
  ("4.4.", "Після спливу строку дані видаляються або знеособлюються.")])),
 ("d5", "5. Одержувачі та передача даних", cl([
  ("5.1.", "Доступ до даних мають Юрист і постачальники послуг, необхідних для роботи Сайту: хостинг-провайдер; Cloudflare (мережа доставки контенту, DNS, захист від атак); Google (Google Maps, Google Fonts)."),
  ("5.2.", "Telegram і Meta (Facebook) отримують дані лише тоді, коли суб'єкт сам переходить на ці сервіси, і діють за власними політиками."),
  ("5.3.", "Частина постачальників може розташовуватися поза Україною та ЄС. Передача здійснюється на підставі стандартних договірних положень або інших гарантій, передбачених GDPR."),
  ("5.4.", "Державним органам дані надаються лише за законною вимогою.")])),
 ("d6", "6. Файли cookie", cl([
  ("6.1.", "Сайт використовує технічні файли cookie (безпека й робота Сайту), cookie форми відгуку та файли cookie сторонніх сервісів (Google Maps, Cloudflare)."),
  ("6.2.", "Рекламні й аналітичні cookie не застосовуються."),
  ("6.3.", "Суб'єкт може видалити cookie або заборонити їх у налаштуваннях браузера; частина функцій Сайту (зокрема форма відгуку) тоді може працювати некоректно.")])),
 ("d7", "7. Права суб'єкта персональних даних", cl([
  ("7.1.", "Суб'єкт має право: знати про обробку своїх даних і отримати їх копію; вимагати виправлення неточних даних; вимагати видалення; обмежити обробку або заперечити проти неї; на переносимість даних; відкликати згоду в будь-який час (це не впливає на законність обробки до відкликання)."),
  ("7.2.", f"Запит надсилається на <a href=\"mailto:{EMAIL}\">{EMAIL}</a>. Відповідь надається протягом 30 днів. Для захисту даних може бути запитане підтвердження особи.")])),
 ("d8", "8. Подання звернень і скарг", cl([
  ("8.1.", f"Звернення, запити та скарги щодо обробки персональних даних приймаються на <a href=\"mailto:{EMAIL}\">{EMAIL}</a>. У зверненні слід вказати імʼя, контакт для відповіді та суть питання."),
  ("8.2.", "Якщо суб'єкт вважає, що його права порушено, він може звернутися до Уповноваженого Верховної Ради України з прав людини (<a href=\"https://ombudsman.gov.ua\" target=\"_blank\" rel=\"noopener\">ombudsman.gov.ua</a>) або, у країнах ЄС, до органу із захисту даних за місцем проживання.")])),
 ("d9", "9. Захист даних", cl([
  ("9.1.", "Застосовуються шифроване зʼєднання (HTTPS), обмежений доступ до адміністрування Сайту, захист від підбору паролів і атак, резервне копіювання."),
  ("9.2.", "Не надсилайте через форми й месенджери зайвих даних, зокрема повних реквізитів банківських карток.")])),
 ("d10", "10. Неповнолітні", cl([
  ("10.1.", "Сайт не призначений для осіб віком до 16 років. Дані таких осіб свідомо не збираються й за надходження звернення будуть видалені.")])),
 ("d11", "11. Зміни до Політики", cl([
  ("11.1.", f"Юрист може змінювати Політику. Чинна редакція розміщується на цій сторінці та діє від {DATE_HUMAN}.")])),
]

def policy_body():
    toc = "".join(f'<a href="#{i}">{t}</a>' for i, t, _ in SECTIONS)
    secs = "".join(f'<h2 id="{i}">{t}</h2>\n{b}\n' for i, t, b in SECTIONS)
    return f'''{header("Політика конфіденційності", "Порядок обробки персональних даних відвідувачів сайту: мета, підстави, строки зберігання, права та звернення.", "Конфіденційність · Яковенко Дмитро", cta=False)}

<section class="pg"><div class="in"><div class="legal-card">
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
        html = wrap(p["desc"], p["ld"], p["body"]())
        (R / p["file"]).write_text(html, encoding="utf-8")
        print(p["file"], len(html))
        if "--publish" in sys.argv:
            found = call("GET", f"{SITE}/wp-json/wp/v2/pages?slug={slug}&status=any&context=edit&_fields=id,status")
            payload = {"title": p["title"], "slug": slug, "template": "page-landing", "content": html,
                       "status": "publish" if "--live" in sys.argv else "draft"}
            if found:
                if found[0]["status"] == "publish" and "--live" not in sys.argv:
                    payload.pop("status")
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages/{found[0]['id']}", payload)
            else:
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages", payload)
            print(" ->", d.get("id"), d.get("status"), d.get("link"), d.get("code"), d.get("message"))
