#!/usr/bin/env python3
"""Вставка розділу з посиланнями на lawagency.kiev.ua у 10 проіндексованих статей (за завданням керівника).
  python3 insert_links.py            -> dry-run (diff у /tmp, нічого не пишеться на сайти)
  python3 insert_links.py --apply    -> бекап + POST content у WP, перевірка після запису"""
import json, re, sys, subprocess, pathlib, csv, html as H
R = pathlib.Path(__file__).parent
LA = "https://lawagency.kiev.ua/"
U = {"44": "https://www.44.ua/catalog/index/1448513/la-konsalting-la-consulting-vidguki-pro-uridicnu-firmu",
     "meget": "https://meget.kiev.ua/yuristi/1777-la-consulting/otzivi",
     "cons": "https://consultant.kiev.ua/uk/la-konsalting-forum/",
     "jl": "https://jurliga.ligazakon.net/ru/catalog/12850",
     "fb": "https://facebook.com/groups/1787856888697144"}
A = ["тов ла консалтинг юридична фірма має відгуки на різних платформах", "ла консалтинг відгуки від клієнтів",
     "ла консалтинг отзывы от клиентов юридической фирмы", "la consulting отзывы я оставил тут",
     "ла консалтинг предпреждает про мошенничества", "la.co.ua отзывы", "ла консалтинг номер телефона",
     "сайт где я оставил отзыв про юридическую фирму ЛА Консалтинг", "юридическая фирма ла консалтинг предупреждает про мошенничества"]
def a(i): return f'<a href="{LA}" target="_blank" rel="noopener">{A[i]}</a>'
def b(k): return f'<a href="{U[k]}" target="_blank" rel="noopener">{U[k]}</a>'
# domain: (page id, marker h2 text start, H2 title or None, html body, anchor idx, bare key, why)
S = {
 "advokat-kharkov.org.ua": (1160, "Питання та відповіді", "Як перевірити юриста, якщо борги накопичуються",
   f"<p>Коли борги накопичуються, легко потрапити до тих, хто обіцяє «списати все за тиждень». Тому перед зверненням перевірте, що про юридичну фірму пишуть клієнти. Наприклад, {a(0)}, і їх можна порівняти між собою. Добірку сторінок із відгуками можна переглянути тут: {b('44')}.</p>", 0, "44"),
 "advokato.in.ua": (1873, "Висновок юриста", "Як вибрати юриста для спору з колекторською компанією",
   f"<p>Спір з колекторською компанією, зокрема з Прімоколект, краще вести з юристом, який працює з такими справами. Дізнайтеся, що про фірму пишуть клієнти: {a(1)} опубліковані на кількох майданчиках, і їх варто прочитати самостійно. Ще одна сторінка з відгуками: {b('meget')}.</p>", 1, "meget"),
 "argument-consulting.com.ua": (1464, "Часті питання щодо", "Куди звернутися, якщо колектори порушують вашу приватність",
   f"<p>Якщо колектори телефонують родичам чи знайомим, це привід звернутися до юриста. Обираючи фірму, подивіться, що про неї пишуть: дехто шукає відгуки й російською, наприклад за запитом «{a(2)}»; результати варто порівнювати між собою. Також є форум, де обговорюють фірму: {b('cons')}.</p>", 2, "cons"),
 "bankruptcyukraine.com": (1330, "Питання та відповіді", "Як перевірити юридичний супровід у спорі з приватним кредитором",
   f"<p>Перш ніж довіряти юридичний супровід у спорі з приватним кредитором, вивчіть відгуки про фірму. Шукаючи їх, люди часто натрапляють на фрази на кшталт «{a(3)}»; такі сторінки корисно відкривати й читати разом з іншими джерелами. Добірка відгуків: {b('jl')}.</p>", 3, "jl"),
 "jurist-po-ipotechnum-kreditam.kiev.ua": (973, "Висновок", None, None, 4, "cons"),
 "lawmsb.com.ua": (3731, "Юридичні поради та практичні кейси", "Як вибрати юриста для судової справи з фінансовою компанією",
   f"<p>Судові справи проти фінансових компаній потребують досвіду, тому юриста варто обирати свідомо. Окрім сайту фірми, подивіться на незалежні сторінки: є й сторінка за запитом «{a(5)}», яку також можна переглянути. Ще одна добірка відгуків: {b('fb')}.</p>", 5, "fb"),
 "legaladdress.com.ua": (107, "Висновок юриста", "Коли варто звернутися до юриста",
   f"<p>Якщо вам уже надійшло рішення суду чи постанова виконавця, не чекайте: зв’яжіться з юристом. Контактні дані фірми, зокрема {a(6)}, вказані на її офіційному сайті. Обговорення про фірму ведуться й в інтернеті: {b('44')}.</p>", 6, "44"),
 "uchet.com.ua": (68, "Висновок юриста", "Як перевірити фірму перед консультацією",
   f"<p>Перед виїздом за кордон з боргом краще проконсультуватися з юристом. Шукаючи відгуки про фірму, люди натрапляють і на такі формулювання: «{a(7)}»; звертайте увагу на джерело й дату відгуку. Ще одна сторінка з відгуками: {b('meget')}.</p>", 7, "meget"),
 "urists.com.ua": (54, "Питання та відповіді", "Як не потрапити на шахраїв, якщо є прострочка",
   f"<p>Прострочка по кредиту — зручний момент для шахраїв: вони пишуть у соцмережах і месенджерах від імені юристів. Про це попереджають і самі фірми: «{a(8)}». Звіряйте контакти з офіційним сайтом і не передавайте кошти чи коди з банківських застосунків. Добірка відгуків: {b('jl')}.</p>", 8, "jl"),
 "yuristy.in.ua": (25472, "Питання та відпповіді", "Як вибрати фірму для супроводу у справах з МФО",
   f"<p>Боргові питання з МФО, зокрема з Таліон Плюс, краще вирішувати з юристом, який знає такі справи. Перед зверненням перегляньте, що пишуть клієнти: {a(0)}. Ще одна добірка відгуків: {b('fb')}.</p>", 0, "fb"),
}
def get(d, i):
    r = subprocess.run(["curl", "-s", "-m", "90", "-A", "curl/8.5.0", f"https://{d}/wp-json/wp/v2/pages/{i}?context=edit"], capture_output=True, text=True).stdout
    return json.loads(r)
def build(d, raw):
    pid, marker, h2, body, ai, bk = S[d]
    if d.startswith("jurist-po"):
        # додаємо в наявний розділ про відгуки; існуюче посилання на форум робимо безанкорним
        old = re.search(r'<a href="https://consultant\.kiev\.ua/uk/la-konsalting-forum/"[^>]*>де прочитати відгуки про ла консалтінг</a> можна дізнатися на тематичному форумі боржників\.', raw)
        assert old, "jurist-po: не знайдено наявне посилання"
        new_sent = f'Обговорення про фірму є на тематичному форумі боржників: {b("cons")}.'
        raw2 = raw.replace(old.group(0), new_sent)
        add = f' Окремо остерігайтеся шахраїв у соцмережах: «{a(4)}». Перш ніж писати комусь у месенджері, звіряйте контакти з офіційним сайтом.'
        m = re.search(r"(Порівнюйте їх з іншими джерелами й перевіряйте самі, що саме пишуть: конкретні факти чи загальні емоції\.)(</p>)", raw2)
        assert m
        return raw2[:m.end(1)] + add + raw2[m.end(1):]
    block = f"<h2>{h2}</h2>\n{body}\n"
    ms = [m for m in re.finditer(r"<h2[^>]*>(?:\s*<b>)?\s*" + re.escape(marker), raw)]
    assert len(ms) >= 1, (d, "marker")
    pos = ms[0].start()
    return raw[:pos] + block + raw[pos:]
def verify(d, i, anchor, bare):
    j = get(d, i); raw = j["content"]["raw"]
    ok = LA in raw and anchor in raw and bare in raw
    # рендер
    rr = subprocess.run(["curl", "-s", "-m", "60", "-A", "curl/8.5.0", f"https://{d}/wp-json/wp/v2/pages/{i}"], capture_output=True, text=True).stdout
    rend = json.loads(rr)["content"]["rendered"]
    return ok, (LA in rend and anchor in rend and bare in rend), j["status"], raw.count(LA)
def main():
    apply = "--apply" in sys.argv
    rows = []
    for d, (pid, marker, h2, body, ai, bk) in S.items():
        j = get(d, pid); raw = j["content"]["raw"]
        assert j["status"] == "publish", d
        assert LA not in raw, (d, "вже є lawagency")
        new = build(d, raw)
        (R / "backups" / f"{d}-{pid}.html").write_text(raw, encoding="utf-8")
        print(d, pid, "+", len(new) - len(raw), "символів")
        if apply:
            req = subprocess.run(["curl", "-s", "-m", "120", "-A", "curl/8.5.0", "-X", "POST", f"https://{d}/wp-json/wp/v2/pages/{pid}", "-H", "Content-Type: application/json", "--data-binary", "@-"], input=json.dumps({"content": new}, ensure_ascii=False), capture_output=True, text=True).stdout
            r = json.loads(req); print("   POST", r.get("status"), r.get("code"), r.get("message"))
            print("   verify", verify(d, pid, A[ai], U[bk]))

if __name__ == "__main__":
    main()
