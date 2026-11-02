#!/usr/bin/env python3
"""Кравченко Максим Віталійович (rada-advokat.uz.ua): сторінки «Контакти» і «Політика конфіденційності» у стилі живого сайту
(Unbounded + Manrope, синя палітра, шаблон Elementor Canvas). CSS береться з сторінки результатів (base.css) + pages.css.
  python3 build_pages.py                  -> kontakty.wp.html, polityka.wp.html (для id=0)
  python3 build_pages.py --publish        -> створює/оновлює ЧЕРНЕТКИ (двопрохідно: id потрібен для CSS приховування шапки теми)
  python3 build_pages.py --publish --live -> статус publish (лише за командою «публікуй»)
"""
import json, subprocess, sys, pathlib, urllib.parse

R = pathlib.Path(__file__).parent
SITE = "https://rada-advokat.uz.ua"
NAME = "Кравченко Максим Віталійович"
EMAIL = "maksym-yrist@rada-advokat.uz.ua"
EMAIL_HTML = EMAIL.replace("@", "<wbr>@")
PHONE_TEL, PHONE = "+380914811951", "+380914811951"
# Telegram підтверджено замовницею 22.10: @maxim_yrist (раніше на сайті помилково стояв @evgen_yrist)
TG_NICK = "@maxim_yrist"
TG = "https://t.me/maxim_yrist"
IG, IG_NICK = "https://www.instagram.com/yuryst_kravchenko/", "@yuryst_kravchenko"
FB = "https://www.facebook.com/profile.php?id=100077932089127"
ADDR = "04108, м. Київ, пр-т Європейського Союзу (Правди), 31а"
ADDR_Q = urllib.parse.quote("пр-т Європейського Союзу 31а, Київ, 04108")
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + ADDR_Q
MAP_EMBED = "https://www.google.com/maps?q=" + ADDR_Q + "&hl=uk&z=16&output=embed"
U_CONTACTS, U_POLICY, U_RESULTS = SITE + "/kontakty/", SITE + "/polityka-konfidentsiinosti/", SITE + "/rezultaty-roboty/"
POLICY_TITLE = "Політика конфіденційності та обробки персональних даних"
DATE_HUMAN, DATE_ISO = "22 жовтня 2026 року", "2026-10-22"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@500;600;700&display=swap&subset=cyrillic" rel="stylesheet">')
ICO_TG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.5 4.3 2.9 11.5c-1.3.5-1.3 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.8.8.8.5 0 .8-.2 1.1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.2-.5-1.8-1.5-1.4zM8.5 13.6l9.6-6c.5-.3.9-.1.5.2l-7.8 7-.3 3.2z"/></svg>'
ICO_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.5-3.2h-3.2V7.7c0-.9.3-1.6 1.7-1.6h1.6V3.2c-.3 0-1.3-.1-2.4-.1-2.5 0-4.1 1.5-4.1 4.2v2.5H7.5V13h2.8v8z"/></svg>'
ICO_IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zM17.2 6.1a1.1 1.1 0 1 0 0 2.2 1.1 1.1 0 0 0 0-2.2zM12 3c-2.4 0-2.7 0-3.7.1-3.2.1-4.8 1.7-4.9 4.9C3.3 9 3.3 9.3 3.3 12s0 3 .1 4c.1 3.2 1.7 4.8 4.9 4.9 1 .1 1.3.1 3.7.1s2.7 0 3.7-.1c3.2-.1 4.8-1.7 4.9-4.9.1-1 .1-1.3.1-4s0-3-.1-4c-.1-3.2-1.7-4.8-4.9-4.9C14.7 3 14.4 3 12 3zm0 1.8c2.4 0 2.7 0 3.6.1 2.3.1 3.2 1 3.3 3.3.1.9.1 1.2.1 3.6s0 2.7-.1 3.6c-.1 2.3-1 3.2-3.3 3.3-.9.1-1.2.1-3.6.1s-2.7 0-3.6-.1c-2.3-.1-3.2-1-3.3-3.3-.1-.9-.1-1.2-.1-3.6s0-2.7.1-3.6c.1-2.3 1-3.2 3.3-3.3.9-.1 1.2-.1 3.6-.1z"/></svg>'

MENU = [(SITE + "/#help", "Кому допоможу"), (SITE + "/#about", "Про мене"), (SITE + "/#services", "Послуги"),
        (SITE + "/#experience", "Досвід"), (U_RESULTS, "Результати"), (SITE + "/#reviews", "Відгуки"), (U_CONTACTS, "Контакти")]
def menu_ul():
    return "<ul>" + "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in MENU) + "</ul>"

def header(h1_plain, h1_lime, lead):
    return (f'<header class="box hero dk rp-hero" id="top"><div class="nav"><a class="logo" href="{SITE}/">Кравченко М. В.</a>'
            f'<input type="checkbox" id="krm" class="menu-cb" aria-hidden="true" tabindex="-1"><a class="btn sm" href="{TG}" target="_blank" rel="noopener">Консультація</a>'
            f'<label for="krm" class="burger" aria-label="Меню"><i></i></label>{menu_ul()}</div>'
            f'<div class="rp-in"><h1>{h1_plain} <span class="lime">{h1_lime}</span></h1><p class="lead">{lead}</p></div></header>')

def social_block():
    return f'''<section class="box sec dk" id="socials"><div class="in">
<div class="sh"><h2>Мої <span class="lime">соцмережі</span></h2></div>
<div class="soc-grid">
<a class="soc" href="{TG}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_TG}</span><span><small>Telegram</small><b>{TG_NICK}</b></span></a>
<a class="soc" href="{IG}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_IG}</span><span><small>Instagram</small><b>{IG_NICK}</b></span></a>
<a class="soc" href="{FB}" target="_blank" rel="me noopener"><span class="soc-ico">{ICO_FB}</span><span><small>Facebook</small><b>Профіль у Facebook</b></span></a>
</div></div></section>'''

def footer():
    return f'''<footer class="box sec dk" id="contacts"><div class="in"><div class="cta"><h2>Потрібна допомога з кредитом або боргом? <span class="lime">Напишіть юристу</span></h2><div class="btns"><a class="btn" href="{TG}" target="_blank" rel="noopener">Безкоштовна консультація</a><a class="btn ghost" href="tel:{PHONE_TEL}">{PHONE}</a></div></div><div class="ct-g"><div class="ct"><h3>Контакти</h3><div class="row"><small>Телефон</small><a href="tel:{PHONE_TEL}">{PHONE}</a></div><div class="row"><small>Email</small><a href="mailto:{EMAIL}">{EMAIL_HTML}</a></div><div class="row"><small>Telegram</small><a href="{TG}" target="_blank" rel="noopener">{TG_NICK}</a></div><div class="row"><small>Instagram</small><a href="{IG}" target="_blank" rel="noopener">{IG_NICK}</a></div><div class="row"><small>Facebook</small><a href="{FB}" target="_blank" rel="noopener">Профіль у Facebook</a></div><div class="row"><small>Адреса</small>{ADDR}</div><div class="row"><small>Години роботи</small>пн–пт з 09:00 до 18:00, на вихідних за домовленістю</div><div class="row"><small>Документи</small><a href="{U_POLICY}">Політика конфіденційності</a></div></div><div class="map"><iframe title="Карта: пр-т Європейського Союзу (Правди), 31а, Київ" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></div><nav class="fnav" aria-label="Меню">{"".join(f'<a href="{h}">{t}</a>' for h, t in MENU)}<a href="{U_POLICY}">Політика</a></nav><div class="copy"><span>© {NAME}, rada-advokat.uz.ua</span><span class="legal-links"><a href="{U_POLICY}">{POLICY_TITLE}</a><a href="{U_CONTACTS}">Контакти</a></span></div></div></footer>'''

MENU_JS = ("<script>\n(function(){var r=document.getElementById('kr');if(!r){return}var cb=r.querySelector('#krm');if(!cb){return}\n"
           "r.querySelectorAll('.nav ul a').forEach(function(a){a.addEventListener('click',function(){cb.checked=false})});\n"
           "document.addEventListener('keydown',function(e){if(e.key==='Escape'){cb.checked=false}})})();\n</script>")

def wrap(pid, ld, body):
    css = (R / "base.css").read_text(encoding="utf-8").replace("page-id-1916", f"page-id-{pid}") + "\n" + (R / "pages.css").read_text(encoding="utf-8")
    ldj = json.dumps(ld, ensure_ascii=False)
    return (f'<!-- wp:html -->\n{FONTS}\n<script type="application/ld+json">{ldj}</script>\n<style>\n{css}\n</style>\n'
            f'<div id="kr">\n<div class="kr-wrap">{body}{MENU_JS}</div>\n</div>\n<!-- /wp:html -->\n')

# ---------- Контакти ----------
C_TITLE = f"Контакти — {NAME}"
C_DESC = "Контакти юриста по кредитам Кравченка Максима Віталійовича: телефон, email, Telegram, Instagram, Facebook, адреса в Києві та години роботи."
assert len(C_DESC) <= 170
ORG = {"@type": ["Organization", "LegalService"], "@id": SITE + "/#organization",
       "name": f"{NAME} — юрист по кредитам", "legalName": NAME, "url": SITE + "/", "email": EMAIL, "telephone": PHONE_TEL,
       "founder": {"@id": SITE + "/#person"},
       "address": {"@type": "PostalAddress", "streetAddress": "пр-т Європейського Союзу (Правди), 31а", "postalCode": "04108",
                   "addressLocality": "Київ", "addressCountry": "UA"},
       "areaServed": {"@type": "Country", "name": "Україна"},
       "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}],
       "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": PHONE_TEL, "email": EMAIL,
                         "availableLanguage": ["uk"]}],
       "sameAs": [TG, IG, FB]}
C_LD = {"@context": "https://schema.org", "@graph": [
    {"@type": "ContactPage", "@id": U_CONTACTS + "#page", "url": U_CONTACTS, "name": C_TITLE, "description": C_DESC,
     "inLanguage": "uk", "about": {"@id": SITE + "/#organization"}, "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}}, ORG]}

def contacts_body():
    cards = f'''<div class="ccg">
<a class="cc" href="tel:{PHONE_TEL}"><small>Телефон</small><b>{PHONE}</b><p>Дзвінки й повідомлення в робочий час.</p></a>
<a class="cc" href="mailto:{EMAIL}"><small>Email</small><b>{EMAIL_HTML}</b><p>Для звернень і скарг. Відповідь протягом 30 днів.</p></a>
<a class="cc" href="{TG}" target="_blank" rel="noopener"><small>Telegram</small><b>{TG_NICK}</b><p>Найшвидший спосіб зв’язатися.</p></a>
<a class="cc" href="{IG}" target="_blank" rel="noopener me"><small>Instagram</small><b>{IG_NICK}</b><p>Повідомлення в Direct.</p></a>
<a class="cc" href="{FB}" target="_blank" rel="noopener me"><small>Facebook</small><b>Профіль у Facebook</b><p>Повідомлення в месенджері.</p></a>
<a class="cc" href="{MAPS_LINK}" target="_blank" rel="noopener"><small>Адреса</small><b>{ADDR}</b><p>Зустріч за попередньою домовленістю.</p></a>
</div>'''
    return (header("Контакти", "юриста", "Напишіть у Telegram, зателефонуйте або надішліть лист. Розберемо вашу ситуацію з кредитом чи боргом і підкажемо, з чого почати.")
        + f'''<main><section class="sec pg" id="ways"><div class="in"><h2 class="sec-t">Оберіть зручний <span class="hl">спосіб</span></h2>{cards}
<div class="map-box"><iframe title="Карта: {ADDR}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
<p class="car-note">Години роботи: пн–пт з 09:00 до 18:00, на вихідних за домовленістю.</p></div></section>{social_block()}</main>''' + footer())

# ---------- Політика: блок «Коротко» + нумеровані розділи з кружечками (відрізняється від інших сайтів) ----------
P_DESC = "Політика конфіденційності та обробки персональних даних сайту юриста Кравченка Максима Віталійовича: мета, підстави, строки, права, звернення і скарги."
assert len(P_DESC) <= 170
P_TITLE = f"{POLICY_TITLE} — {NAME}"
P_LD = {"@context": "https://schema.org", "@type": "WebPage", "@id": U_POLICY + "#page", "url": U_POLICY, "name": POLICY_TITLE,
        "description": P_DESC, "inLanguage": "uk", "dateModified": DATE_ISO,
        "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE + "/"}, "about": {"@id": SITE + "/#organization"}}

SHORT = [("Хто обробляє", f"{NAME}, {ADDR}."),
         ("Що збирається", "Контактні дані, текст звернення, відгук, технічні дані (IP, браузер)."),
         ("Навіщо", "Відповісти на запит, показати відгук, захистити сайт, виконати закон."),
         ("Ваші права", f"Доступ, виправлення, видалення, скарга: {EMAIL}.")]
SECTIONS = [
 ("k1", "Загальні положення", f'''<p>Ця Політика описує, як сайт <b>rada-advokat.uz.ua</b> обробляє персональні дані відвідувачів, відповідно до Закону України «Про захист персональних даних» і Регламенту (ЄС) 2016/679 (GDPR).</p>
<p><b>Володілець персональних даних (контролер)</b> — особа, яка визначає мету й засоби обробки та відповідає за захист даних. Це {NAME}, {ADDR}. Зв’язок із володільцем: <a href="mailto:{EMAIL}">{EMAIL}</a>, <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>'''),
 ("k2", "Які дані обробляються", '''<ul>
<li><b>Надані вами:</b> імʼя, номер телефону, нік у Telegram, Instagram чи Facebook, текст звернення, документи, надіслані для оцінки ситуації.</li>
<li><b>Відгук:</b> імʼя, оцінка, текст, за бажанням посилання на сторінку в соцмережі, ідентифікатор браузера (cookie) для показу вашого відгуку до модерації.</li>
<li><b>Технічні:</b> IP-адреса, браузер і пристрій, дата й час візиту, відкриті сторінки (журнали сервера й засобів захисту).</li>
</ul>
<p>Особливі категорії даних через сайт не збираються. Якщо вони потрібні у справі, ви передаєте їх добровільно в особистому зверненні.</p>'''),
 ("k3", "Мета й підстави обробки", '''<ul>
<li>Відповідь на звернення й первинна консультація — ваша згода (ст. 6(1)(a) GDPR) і заходи на ваш запит до укладення договору (ст. 6(1)(b)).</li>
<li>Публікація відгуку — ваша згода, яку можна відкликати.</li>
<li>Безпека й справна робота сайту — законний інтерес (ст. 6(1)(f)).</li>
<li>Виконання вимог закону — юридичний обов’язок (ст. 6(1)(c)).</li>
</ul>
<p>Дані не продаються, не використовуються для реклами та автоматизованого прийняття рішень.</p>'''),
 ("k4", "Строки зберігання", '''<ul>
<li>Листування й документи за зверненням — до трьох років після завершення спілкування (загальна позовна давність), а коли закон вимагає, довше.</li>
<li>Відгуки — до вашого запиту на видалення.</li>
<li>Технічні журнали — до 90 днів.</li>
</ul>
<p>Після спливу строку дані видаляються або знеособлюються.</p>'''),
 ("k5", "Одержувачі та передача", '''<p>Доступ мають володілець і постачальники, потрібні для роботи сайту: хостинг-провайдер, Cloudflare (CDN, DNS, захист від атак), Google (Google Maps, Google Fonts). Telegram, Instagram і Facebook (Meta) отримують дані, лише коли ви самі переходите на ці сервіси.</p>
<p>Частина постачальників може бути за межами України та ЄС; передача відбувається на підставі стандартних договірних положень або інших гарантій за GDPR. Державним органам дані надаються лише на законну вимогу.</p>'''),
 ("k6", "Файли cookie", '''<p>Використовуються технічні cookie (безпека, робота сайту), cookie форми відгуку та cookie сторонніх сервісів (Google Maps, Cloudflare). Сайт також використовує плагін для керування cookie. Рекламні й аналітичні cookie не застосовуються. Cookie можна видалити або заборонити в налаштуваннях браузера; форма відгуку тоді може працювати некоректно.</p>'''),
 ("k7", "Права суб'єкта даних", f'''<ul>
<li>отримати підтвердження обробки й копію своїх даних;</li>
<li>вимагати виправлення неточних або неповних даних;</li>
<li>вимагати видалення даних;</li>
<li>обмежити обробку або заперечити проти неї;</li>
<li>перенести дані в зручному форматі;</li>
<li>відкликати згоду в будь-який час (це не вплине на законність обробки до відкликання);</li>
<li>звернутися зі скаргою до наглядового органу.</li>
</ul>
<p>Запит надсилайте на <a href="mailto:{EMAIL}">{EMAIL}</a>. Відповідь надається протягом 30 днів; для захисту даних може бути запитане підтвердження особи.</p>'''),
 ("k8", "Звернення та скарги", f'''<p>Звернення, запити й скарги щодо персональних даних приймаються на <a href="mailto:{EMAIL}">{EMAIL}</a>. Вкажіть імʼя, контакт для відповіді й суть питання.</p>
<p>Якщо ви вважаєте, що права порушено, можна звернутися до Уповноваженого Верховної Ради України з прав людини (<a href="https://ombudsman.gov.ua" target="_blank" rel="noopener">ombudsman.gov.ua</a>) або в орган із захисту даних вашої країни в ЄС.</p>'''),
 ("k9", "Безпека", '''<p>Застосовуються шифроване з’єднання (HTTPS), обмежений доступ до адміністрування, захист від підбору паролів і атак, резервне копіювання. Не надсилайте через форми й месенджери зайвих даних, наприклад повних реквізитів банківських карток.</p>'''),
 ("k10", "Неповнолітні", '''<p>Сайт розрахований на дорослих. Дані осіб до 16 років не збираються; якщо такі дані потрапили до володільця, вони будуть видалені після звернення.</p>'''),
 ("k11", "Зміни до Політики", f'''<p>Політика може оновлюватися. Чинна редакція розміщена на цій сторінці й діє від {DATE_HUMAN}.</p>'''),
]

def policy_body():
    short = "".join(f'<div class="mini"><h3>{t}</h3><p>{d}</p></div>' for t, d in SHORT)
    secs = "".join(f'<h2 id="{i}"><span class="no">{n}</span>{t}</h2>\n{b}\n' for n, (i, t, b) in enumerate(SECTIONS, 1))
    return (header("Політика", "конфіденційності", "Як цей сайт обробляє персональні дані: що збирається, навіщо, як довго зберігається і як ви можете скористатися своїми правами.")
        + f'''<main><section class="sec pg"><div class="in"><div class="short">{short}</div>
<div class="doc"><span class="upd">Редакція від {DATE_HUMAN}</span>
{secs}</div></div></section></main>''' + footer())

PAGES = {
    "kontakty": dict(title=C_TITLE, ld=C_LD, body=contacts_body, file="kontakty.wp.html"),
    "polityka-konfidentsiinosti": dict(title=P_TITLE, ld=P_LD, body=policy_body, file="polityka.wp.html"),
}

def call(method, url, data=None):
    cmd = ["curl", "-sS", "-m", "120", "-X", method, url, "-H", "Content-Type: application/json"]
    if data is not None:
        cmd += ["--data-binary", "@-"]
    out = subprocess.run(cmd, input=json.dumps(data).encode() if data is not None else None, capture_output=True).stdout
    return json.loads(out)

if __name__ == "__main__":
    for slug, p in PAGES.items():
        if "--publish" not in sys.argv:
            (R / p["file"]).write_text(wrap(0, p["ld"], p["body"]()), encoding="utf-8")
            print(p["file"]); continue
        found = call("GET", f"{SITE}/wp-json/wp/v2/pages?slug={slug}&status=any&context=edit&_fields=id,status")
        if found:
            pid = found[0]["id"]; status0 = found[0]["status"]
        else:  # перший прохід: порожня чернетка, щоб отримати id
            d = call("POST", f"{SITE}/wp-json/wp/v2/pages", {"title": p["title"], "slug": slug, "status": "draft", "template": "elementor_canvas"})
            pid = d["id"]; status0 = "draft"
        html = wrap(pid, p["ld"], p["body"]())
        (R / p["file"]).write_text(html, encoding="utf-8")
        payload = {"title": p["title"], "slug": slug, "template": "elementor_canvas", "content": html}
        payload["status"] = "publish" if "--live" in sys.argv else status0
        d = call("POST", f"{SITE}/wp-json/wp/v2/pages/{pid}", payload)
        print(slug, "->", d.get("id"), d.get("status"), d.get("link"), d.get("code"), d.get("message"))
