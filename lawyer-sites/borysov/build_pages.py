#!/usr/bin/env python3
"""Борисов Максим Юрійович (uchet.com.ua), стиль S2 «Khaki Light»: сторінки «Контакти» і «Політика конфіденційності».
CSS-оболонка береться з живої сторінки результатів (page33-live.html) + pages.css.
  python3 build_pages.py                 -> kontakty.wp.html, polityka.wp.html
  python3 build_pages.py --publish       -> створює/оновлює ЧЕРНЕТКИ у WP (авторизацію додає проксі)
  python3 build_pages.py --publish --live -> те саме, але статус publish (лише за командою «публікуй»)
"""
import json, subprocess, sys, pathlib, urllib.parse

R = pathlib.Path(__file__).parent
SITE = "https://uchet.com.ua"
NAME = "Борисов Максим Юрійович"
EMAIL = "maksym-yrist@uchet.com.ua"
EMAIL_HTML = EMAIL.replace("@", "<wbr>@")
PHONE_TEL, PHONE = "+380505100661", "+380 50 510 06 61"
TG, TG_NICK = "https://t.me/yrist_maxim", "@yrist_maxim"
FB = "https://www.facebook.com/profile.php?id=100087490643353"
ADDR = "03134, вул. Івана Дзюби (Сім'ї Сосніних), 3, приміщення 1, Київ"
ADDR_SHORT = "вул. Івана Дзюби, 3, Київ"
ADDR_Q = urllib.parse.quote("03134, Київ, вул. Івана Дзюби, 3")
MAP_EMBED = "https://www.google.com/maps?q=" + ADDR_Q + "&hl=uk&output=embed"
URL_CONTACTS, URL_POLICY, URL_RESULTS = "/kontakty/", "/polityka-konfidentsiinosti/", "/rezultaty-roboty/"
POLICY_TITLE = "Політика конфіденційності та обробки персональних даних"
DATE_HUMAN, DATE_ISO = "22 жовтня 2026 року", "2026-10-22"

# База: CSS живої головної (меню, бургер, футер) + правила внутрішньої сторінки з «Результатів» (hero.sub, crumbs)
src = (R / "page9-live-20261022.html").read_text(encoding="utf-8")
a = src.index("<style>") + 7
BASE_CSS = src[a: src.index("</style>", a)]
CSS = BASE_CSS + "\n" + (R / "base-extra.css").read_text(encoding="utf-8") + "\n" + (R / "pages.css").read_text(encoding="utf-8")

ARROW = '<i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></i>'
IC = {
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "tg": '<path d="M21 4L3 11l6 2 2 6 3-4 5 4z"/>',
 "pin": '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "doc": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/>',
}
def row(kind, label, val, href=None, ext=False):
    svg = f'<i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{IC[kind]}</svg></i>'
    inner = f'{svg}<span><small>{label}</small>{val}</span>'
    if href:
        t = ' target="_blank" rel="noopener"' if ext else ""
        return f'<a class="row" href="{href}"{t}>{inner}</a>'
    return f'<div class="row">{inner}</div>'

ICO_TG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.5 4.3 2.9 11.5c-1.3.5-1.3 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.8.8.8.5 0 .8-.2 1.1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.2-.5-1.8-1.5-1.4zM8.5 13.6l9.6-6c.5-.3.9-.1.5.2l-7.8 7-.3 3.2z"/></svg>'
ICO_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.5-3.2h-3.2V7.7c0-.9.3-1.6 1.7-1.6h1.6V3.2c-.3 0-1.3-.1-2.4-.1-2.5 0-4.1 1.5-4.1 4.2v2.5H7.5V13h2.8v8z"/></svg>'

LOGO = '<a class="logo" href="/">БОРИСОВ <b>·</b> ЮРИСТ</a>'
def header(h1, lead, crumb, cta=True):
    menu = (f'<nav class="menu"><a href="/#about">Про мене</a><a href="/#services">Послуги</a><a href="{URL_RESULTS}">Результати</a>'
            f'<a href="/#reviews">Відгуки</a><a href="{URL_CONTACTS}">Контакти</a></nav>')
    btn = f'<a class="btn" href="{TG}" target="_blank" rel="noopener">Написати в Telegram {ARROW}</a>' if cta else ""
    return f'''<header class="hero sub"><div class="w nav-w">
 <div class="nav"><input type="checkbox" id="ucm" class="menu-cb" aria-hidden="true" tabindex="-1">{LOGO}{menu}<a class="tg" href="{TG}" target="_blank" rel="noopener">{TG_NICK}</a><label for="ucm" class="burger" aria-label="Меню"><i></i></label></div>
</div>
<div class="w">
 <div class="hero-g" id="top"><div class="hero-t">
  <div class="crumbs"><a href="/">Головна</a> / {crumb}</div>
  <h1>{h1}</h1>
  <p>{lead}</p>
  {btn}
 </div></div>
</div></header>'''

def footer():
    rows = "\n   ".join([
        row("pin", "Адреса", ADDR),
        row("clock", "Години роботи", "Пн-Пт 09:00-18:00, вихідні за домовленістю"),
        row("phone", "Телефон", PHONE, f"tel:{PHONE_TEL}"),
        row("mail", "Email", EMAIL_HTML, f"mailto:{EMAIL}"),
        row("tg", "Telegram", TG_NICK, TG, True),
        row("doc", "Документи", "Політика конфіденційності", URL_POLICY),
        row("doc", "Компанія", "ЛА Консалтінг (LA Consulting)"),
    ])
    return f'''<footer class="page-end" id="contacts"><div class="w">
 <div class="ct">
  <div class="ct-l">
   <span class="eyebrow">Контакти</span>
   <h2>Зв'яжіться <em>зі мною</em></h2>
   <p>Напишіть у Telegram або приходьте в офіс у Києві. Вихідні за домовленістю.</p>
   {rows}
  </div>
  <div class="map"><iframe title="Мапа: {ADDR_SHORT}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}"></iframe></div>
 </div>
 <nav class="fnav" aria-label="Меню"><a href="/#about">Про мене</a><a href="/#services">Послуги</a><a href="{URL_RESULTS}">Результати</a><a href="/#reviews">Відгуки</a><a href="{URL_CONTACTS}">Контакти</a><a href="{URL_POLICY}">Політика</a></nav>
 <div class="end-bar"><span>© {NAME}. Юрист по кредитам, Київ.</span><span class="legal-links"><a href="{URL_POLICY}">{POLICY_TITLE}</a><a href="{URL_CONTACTS}">Контакти</a></span></div>
</div></footer>'''

BURGER_JS = '<script>(function(){var r=document.querySelector(".uc");if(!r)return;var cb=r.querySelector("#ucm");if(!cb)return;r.querySelectorAll(".nav .menu a").forEach(function(a){a.addEventListener("click",function(){cb.checked=false})});document.addEventListener("keydown",function(e){if(e.key==="Escape")cb.checked=false})})();</script>'

def wrap(desc, ld, body):
    ldj = json.dumps(ld, ensure_ascii=False)
    return (f'<!-- wp:html -->\n<div class="uc">\n<style>\n{CSS}\n</style>\n<meta name="description" content="{desc}">\n\n{body}\n\n'
            f'<script type="application/ld+json">{ldj}</script>\n</div>\n{BURGER_JS}\n<!-- /wp:html -->\n')

# ---------- Контакти ----------
C_TITLE = f"Контакти — {NAME}"
C_DESC = "Контакти юриста по кредитам Борисова Максима Юрійовича: телефон, email, Telegram, Facebook, адреса офісу в Києві та години роботи."
assert len(C_DESC) <= 160
ORG = {"@type": ["Organization", "LegalService"], "@id": SITE + "/#organization",
       "name": "ЛА Консалтінг (LA Consulting)", "alternateName": f"{NAME} — юрист по кредитам",
       "url": SITE + "/", "email": EMAIL, "telephone": PHONE_TEL,
       "employee": {"@id": SITE + "/#person"},
       "address": {"@type": "PostalAddress", "streetAddress": "вул. Івана Дзюби (Сім'ї Сосніних), 3, приміщення 1",
                   "postalCode": "03134", "addressLocality": "Київ", "addressCountry": "UA"},
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
   <a class="cc" href="https://www.google.com/maps/search/?api=1&query={ADDR_Q}" target="_blank" rel="noopener"><small>Адреса</small><b>{ADDR}</b><p>Компанія «ЛА Консалтінг».</p></a>
   <div class="cc"><small>Години роботи</small><b>Пн-Пт, 09:00-18:00</b><p>Вихідні за домовленістю.</p></div>
  </div>'''
    return f'''{header("Контакти <em>юриста</em>", "Напишіть у Telegram, зателефонуйте або надішліть лист. Розберемо вашу ситуацію з кредитом і підкажемо, з чого почати.", "Контакти")}
<section><div class="w">
 <div class="panel">
  <span class="eyebrow">Звʼязок</span>
  <h2>Як зі мною <em>звʼязатися</em></h2>
  <div style="height:26px"></div>
  {cards}
  <div class="map-box"><iframe title="Мапа: {ADDR_SHORT}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
 </div>
</div></section>
<section style="padding-top:0"><div class="w">
 <div class="panel" id="socials">
  <span class="eyebrow">Соцмережі</span>
  <h2>Мої <em>соцмережі</em></h2>
  <div class="soc-grid">
   <a class="soc" href="{TG}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_TG}</span><span><small>Telegram</small><b>{TG_NICK}</b></span></a>
   <a class="soc" href="{FB}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_FB}</span><span><small>Facebook</small><b>Профіль у Facebook</b></span></a>
  </div>
 </div>
</div></section>
{footer()}'''

# ---------- Політика (власний текст у першій особі; відрізняється від інших сайтів) ----------
P_DESC = "Політика конфіденційності та обробки персональних даних сайту юриста Борисова Максима Юрійовича: які дані збираю, навіщо, права відвідувачів, звернення."
assert len(P_DESC) <= 160
P_TITLE = f"{POLICY_TITLE} — {NAME}"
P_LD = {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + URL_POLICY + "#page", "url": SITE + URL_POLICY,
        "name": POLICY_TITLE, "description": P_DESC, "inLanguage": "uk", "dateModified": DATE_ISO,
        "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}, "about": {"@id": SITE + "/#organization"}}

SECTIONS = [
 ("p1", "1. Загальні положення", f'''<p>Цей документ описує, як на сайті <b>uchet.com.ua</b> обробляються персональні дані відвідувачів. Він підготовлений відповідно до Закону України «Про захист персональних даних» і Регламенту (ЄС) 2016/679 (GDPR).</p>
<p><b>Володілець персональних даних (контролер)</b> — особа, яка визначає мету й способи обробки даних і відповідає за їхній захист. На цьому сайті це я, {NAME}, юрист, {ADDR}.</p>
<p>З будь-яких питань про персональні дані пишіть на <a href="mailto:{EMAIL}">{EMAIL}</a> або телефонуйте <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>'''),
 ("p2", "2. Які дані я отримую", '''<p>Я отримую лише те, що потрібно, щоб відповісти вам і підтримувати роботу сайту:</p>
<ul>
<li><b>Те, що ви повідомляєте самі:</b> імʼя, номер телефону, нік у Telegram чи Facebook, текст звернення та документи, які ви надсилаєте для оцінки вашої ситуації.</li>
<li><b>Відгук на сайті:</b> імʼя, оцінка, текст і (за бажанням) посилання на вашу сторінку в соцмережі. У браузері зберігається технічний ідентифікатор, щоб ви могли бачити свій відгук до того, як його перевірено.</li>
<li><b>Технічні відомості:</b> IP-адреса, браузер, пристрій, час візиту та сторінки, які ви відкривали. Їх фіксують сервер і засоби захисту сайту.</li>
</ul>
<p>Особливі категорії даних (здоров’я, політичні чи релігійні погляди тощо) я через сайт не збираю. Якщо вони потрібні у справі, ви передаєте їх добровільно в особистому зверненні.</p>'''),
 ("p3", "3. Для чого й на яких підставах", '''<ul>
<li><b>Відповісти на звернення, провести первинну консультацію</b> — ваша згода (ст. 6(1)(a) GDPR) і заходи на ваше прохання до укладення договору (ст. 6(1)(b)).</li>
<li><b>Показати відгук на сайті</b> — ваша згода; ви можете відкликати її й попросити видалити відгук.</li>
<li><b>Захистити сайт від зламів, спаму й збоїв</b> — законний інтерес (ст. 6(1)(f)).</li>
<li><b>Виконати вимоги закону</b> — юридичний обов’язок (ст. 6(1)(c)).</li>
</ul>
<p>Я не продаю дані, не веду рекламного профілювання й не ухвалюю щодо вас автоматизованих рішень.</p>'''),
 ("p4", "4. Як довго я зберігаю дані", '''<ul>
<li>Листування й документи за зверненням — до трьох років після завершення спілкування (загальна позовна давність), а якщо закон вимагає, довше.</li>
<li>Відгуки — до вашого прохання їх видалити.</li>
<li>Технічні журнали сервера й засобів захисту — до шести місяців.</li>
</ul>
<p>Коли строк минає, дані видаляються або знеособлюються.</p>'''),
 ("p5", "5. Хто ще може мати доступ", '''<p>Окрім мене, з даними можуть працювати лише ті, без кого сайт не функціонує:</p>
<ul>
<li><b>хостинг-провайдер</b> — розміщує сайт і зберігає резервні копії;</li>
<li><b>Cloudflare</b> — мережа доставки контенту, DNS і захист від атак;</li>
<li><b>Google</b> — відображає карту Google Maps і шрифти Google Fonts (Google може побачити вашу IP-адресу);</li>
<li><b>Telegram і Meta (Facebook)</b> — коли ви самі переходите на ці сервіси за посиланнями.</li>
</ul>
<p>Деякі сервіси розташовані за межами України та ЄС. Тоді передача даних відбувається на підставі стандартних договірних положень або інших гарантій за GDPR. Державним органам дані передаються лише на законну вимогу.</p>'''),
 ("p6", "6. Файли cookie", '''<p>Сайт обходиться мінімальним набором файлів cookie:</p>
<ul>
<li><b>технічні</b>, потрібні для безпеки й роботи сайту;</li>
<li><b>cookie форми відгуку</b> — щоб ви бачили свій відгук до його перевірки;</li>
<li><b>cookie сторонніх сервісів</b>, які можуть встановлювати Google Maps і Cloudflare.</li>
</ul>
<p>Реклами й аналітики на сайті немає. Cookie можна видалити або заборонити в налаштуваннях браузера, але форма відгуку тоді може працювати некоректно.</p>'''),
 ("p7", "7. Ваші права", f'''<p>Ви можете:</p>
<ul>
<li>дізнатися, чи обробляю я ваші дані, і отримати їх копію;</li>
<li>вимагати виправити неточні чи неповні дані;</li>
<li>вимагати видалити дані;</li>
<li>обмежити обробку або заперечити проти неї;</li>
<li>отримати свої дані у зручному форматі й передати їх іншій особі;</li>
<li>відкликати згоду будь-коли (це не вплине на законність обробки до відкликання);</li>
<li>поскаржитися наглядовому органові.</li>
</ul>
<p>Для цього напишіть на <a href="mailto:{EMAIL}">{EMAIL}</a>. Відповідь надам протягом 30 днів; щоб захистити ваші дані, я можу попросити підтвердити особу.</p>'''),
 ("p8", "8. Звернення та скарги", f'''<p>Звернення, запити й скарги щодо персональних даних приймаю за адресою <a href="mailto:{EMAIL}">{EMAIL}</a>. Вкажіть, будь ласка, як до вас звертатися, куди надіслати відповідь і в чому суть питання.</p>
<p>Якщо ви вважаєте, що ваші права порушено, ви можете звернутися до Уповноваженого Верховної Ради України з прав людини (<a href="https://ombudsman.gov.ua" target="_blank" rel="noopener">ombudsman.gov.ua</a>) або, якщо ви перебуваєте в ЄС, до органу із захисту даних вашої країни.</p>'''),
 ("p9", "9. Захист даних", '''<p>Дані захищено шифрованим з’єднанням (HTTPS), обмеженим доступом до адміністрування сайту, захистом від підбору паролів і регулярними резервними копіями. Жоден канал в інтернеті не буває цілком безпечним, тож не надсилайте через форми й месенджери зайвого, наприклад, повні реквізити банківських карток.</p>'''),
 ("p10", "10. Неповнолітні", '''<p>Сайт розрахований на дорослих. Я свідомо не збираю дані осіб молодших за 16 років; якщо така інформація потрапила до мене, видалю її після звернення.</p>'''),
 ("p11", "11. Оновлення політики", f'''<p>Політику можна оновлювати. Остання редакція завжди розміщена на цій сторінці та діє від {DATE_HUMAN}.</p>'''),
]

def policy_body():
    toc = "".join(f'<a href="#{i}">{t}</a>' for i, t, _ in SECTIONS)
    secs = "".join(f'<h2 id="{i}">{t}</h2>\n{b}\n' for i, t, b in SECTIONS)
    return f'''{header("Політика <em>конфіденційності</em>", "Пояснюю простими словами, які персональні дані збирає цей сайт, навіщо, як довго я їх зберігаю та як ви можете скористатися своїми правами.", "Політика конфіденційності", cta=False)}
<section><div class="w">
 <div class="panel">
  <div class="legal-wrap">
   <nav class="toc" aria-label="Зміст"><b>Зміст</b>{toc}</nav>
   <div class="legal"><span class="upd">Редакція від {DATE_HUMAN}</span>
{secs}</div>
  </div>
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
            payload = {"title": p["title"], "slug": slug, "template": "page-landing", "content": html,
                       "status": "publish" if "--live" in sys.argv else "draft"}
            if found:
                if found[0]["status"] == "publish" and "--live" not in sys.argv:
                    payload.pop("status")
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages/{found[0]['id']}", payload)
            else:
                d = call("POST", f"{SITE}/wp-json/wp/v2/pages", payload)
            print(" ->", d.get("id"), d.get("status"), d.get("link"), d.get("code"), d.get("message"))
