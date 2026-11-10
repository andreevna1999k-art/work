import json, html
STYLE = ("Editorial flat-vector infographic illustration for a Ukrainian credit-law blog, premium legal-consultancy look. "
 "STRICT palette: deep navy #181A31 (dark panels, outlines), warm gold #C9A06A and darker gold #8A6128 (accents, numbers, icons), "
 "pale lilac-grey background #F1F1F5, pure white cards #FFFFFF, cream #F3E8D6, muted slate #5C5E76 for secondary text. "
 "No other colours: no red, no green, no bright blue, no gradients except very subtle navy shading. "
 "Soft rounded cards (about 24 px radius), thin gold outlines, one large pale-gold ring as corner decoration, generous white space, safe margins 6%. "
 "People: stylized semi-flat adult characters with realistic proportions, diverse Ukrainian look, modest business-casual clothes, calm and confident expressions, "
 "no caricature, no real-person likeness. Typography (only where text is requested): elegant high-contrast serif for the title (Prata style), clean rounded sans (Nunito style) for labels. "
 "All text must be in correct Ukrainian Cyrillic, spelled exactly as given letter by letter, nothing added. No logos, no bank or company brand names, no watermarks, no phone numbers. "
 "Aspect ratio 3:2, 1536x1024 px.")
FOOT = "Довідкова інформація. Не є індивідуальною юридичною консультацією."
A = [
("01","chy-mozhut-zvilnyty-za-borhy-po-kredytakh","Чи можуть звільнити за борги по кредитах","після вступу (перші 2 абзаци)","після H2 «Що законно, а що ні: порівняння дій роботодавця і кредитора»",
 "Office scene. A calm employee at a desk hands a signed paper to an HR manager across the table; a smartphone lies face-down on the desk, a thin gold line from it ends at a crossed-out door icon. Behind the employee floats a large navy shield with a gold check mark. No text on the image.",
 "Compare infographic with two people icons. Title (serif): «Борг не є підставою для звільнення». Left white card with an employer icon, label «Що може роботодавець», text «Виконати постанову виконавця про утримання із зарплати». Right navy card with a crossed-out door icon, label «Чого не може», text «Звільнити за кредитний борг». Bottom gold strip: «Перелік підстав — у ст. 40 КЗпП». Small footer: «%s»",
 "Працівник і керівниця за столом: борг перед банком не є підставою для звільнення","Що може і чого не може роботодавець щодо боргу працівника"),
("02","chy-mozhut-zabraty-prava-za-nesplatu-kredytu","Чи можуть забрати права за несплату кредиту","після вступу","після H2 «Арешт автомобіля — це не позбавлення прав»",
 "A man sits calmly behind the wheel of a car, car keys in his hand; outside the window a faceless phone-caller silhouette made of navy shapes with a speech bubble containing only an empty gold steering-wheel icon crossed by a thin line. Warm gold light, quiet mood. No text.",
 "Two-column compare infographic with a driver icon on each side. Title (serif): «Права водія і кредит». Left white card, label «Кредит у банку чи МФО», text «Права не забирають». Right navy card, label «Борг за аліментами», text «Виконавець може обмежити право керування». Bottom gold strip: «Норма: ч. 9 ст. 71 Закону «Про виконавче провадження»». Small footer: «%s»",
 "Водій спокійно сидить за кермом: за кредит водійські права не забирають","Різниця між кредитним боргом і боргом за аліментами для права керування"),
("03","chy-mozhut-pozbavyty-batkivskykh-prav-za-nesplatu-kredytu","Чи можуть позбавити батьківських прав за несплату кредиту","після вступу","після H2 «Кредитний борг, аліменти й ухилення від виховання: порівняння»",
 "A father and a small daughter play with building blocks on a living-room floor; on the far side a separate semi-transparent navy bank-building icon is divided from them by a thin gold vertical line, symbolising two different worlds. Soft warm light. No text.",
 "Two-column infographic with a bank-building icon on the left and a parent-with-child icon on the right. Title (serif): «Кредит і діти: різні справи». Left white card, label «Кредит», text «Майновий борг: стягнення, виконавче провадження». Right navy card, label «Батьківські права», text «Оцінюють поведінку щодо дитини. Рішення ухвалює суд». Bottom gold strip: «Банк, МФО і колектор — не сторона такого спору». Small footer: «%s»",
 "Батько з донькою граються вдома: борг перед банком не впливає на батьківські права","Чим кредитний борг відрізняється від питання батьківських прав"),
("04","chy-mozhut-kredytory-pryikhaty-dodomu","Чи можуть кредитори приїхати додому","після вступу","після H2 «Хто може прийти: кредитор, колектор чи виконавець»",
 "Inside an apartment hallway: a woman stands calmly at the front door with the safety chain on, looking through the peephole; in the stairwell outside, a man in a dark coat with a folder is seen as a navy silhouette. Calm, protected mood, gold light from the apartment. No text.",
 "Three numbered cards in a row, each with a small person icon at a door. Title (serif): «Візит додому: три умови». Card 1: «Ваша згода на зустріч». Card 2: «Час візиту: з 9 до 19 години». Card 3: «Назвав себе, підставу та суму боргу». Bottom gold strip: «Без вашої згоди двері відчиняти не потрібно». Small footer: «%s»",
 "Жінка за дверима з ланцюжком: без вашої згоди зустріч не обов'язкова","Три умови, за яких допустима особиста зустріч із боржником"),
("05","druzhyna-nabrala-kredytiv-shcho-robyty","Дружина набрала кредитів: що робити","після вступу","після H2 «Що каже закон про борги одного з подружжя»",
 "A married couple sit at a kitchen table with a laptop, papers and a bank card; the husband listens attentively while the wife explains, calm and cooperative mood, warm lamp light. No text.",
 "Three-condition infographic with a couple icon in the header. Title (serif): «Чи платить чоловік за кредит дружини». Three white cards with gold numbers 1-3: «Договір укладено в інтересах сім'ї», «Гроші пішли на потреби сім'ї», «Це встановив суд». Bottom gold strip: «Колектор чи менеджер банку цього не встановлюють». Small footer: «%s»",
 "Подружжя за кухонним столом розбирає кредитні документи","Три умови, за яких борг дружини стає спільним"),
("06","yak-skhovatysia-vid-kredytoriv","Як сховатися від кредиторів","після вступу","після H2 «Порівняння варіантів: сховатися чи діяти законно»",
 "Split composition, left and right halves. Left half dim and navy: a man hides behind a curtain, a phone rings, envelopes pile up at the door. Right half bright with gold light: the same man sits at a table with a lawyer, documents between them, calm. A thin gold vertical divider. No text.",
 "Left-vs-right infographic with people icons. Title (serif): «Ховатися чи діяти законно». Left dark navy card, label «Ховатися»: «Проценти й штрафи ростуть», «Позов і виконавче провадження». Right three white cards with gold numbers: «Реструктуризація», «Банкрутство фізичної особи», «Захист у виконавчому провадженні». Small footer: «%s»",
 "Дві дороги: ховатися від кредиторів чи діяти законно разом з юристом","Порівняння: що буде, якщо ховатися, і які законні шляхи є"),
("07","shcho-roblyat-z-borzhnykamy-po-kredytakh","Що роблять з боржниками по кредитах","після вступу","після H2 «Що відбувається за законом після рішення суду»",
 "A debtor stands at the bottom of a winding path made of five stepping stones leading up to a calm horizon; on the path small gold icons: a bell, a phone, a gavel, a folder, a lock. A person with a briefcase (lawyer) walks beside him. No text.",
 "Horizontal timeline infographic with five numbered circles connected by a gold line and a small person icon above the first. Title (serif): «Що роблять з боржником: етапи». Steps: «Нагадування і неустойка», «Колектори або продаж боргу», «Позов до суду», «Виконавче провадження», «Арешт, утримання з доходів». Bottom gold strip: «Примусові заходи — після рішення суду або виконавчого документа». Small footer: «%s»",
 "Шлях боржника: від нагадування до виконавчого провадження","П'ять етапів стягнення боргу за кредитом"),
("08","shcho-robyty-yakshcho-zarplaty-ne-vystachaye-na-kredyty","Що робити, якщо зарплати не вистачає на кредити","після вступу","після H2 «Реструктуризація за згодою сторін»",
 "A woman at a home desk with a calculator, a payslip and several loan statements, writing a letter by hand; a coffee mug, evening lamp light; on the wall a small calendar. Focused, determined mood. No text.",
 "Four-step infographic with a woman-at-desk icon in the corner. Title (serif): «Зарплати не вистачає: перші кроки». Steps in four white cards with gold numbers: «Скласти перелік кредитів і платежів», «Написати кожному кредитору заяву про зміну графіка», «Додати докази зниження доходу», «Перечитати кредитний договір». Bottom gold strip: «Письмово, а не по телефону». Small footer: «%s»",
 "Жінка складає заяву кредиторам про зміну графіка платежів","Чотири перші кроки, якщо зарплати не вистачає на кредити"),
("09","yakshcho-vtratyv-robotu-yak-platyty-kredyt","Якщо втратив роботу: як платити кредит","після вступу","після H2 «Реструктуризація: тільки за згодою сторін»",
 "Two small scenes joined by a gold arrow. Left: a man leaves an office building carrying a cardboard box. Right: the same man at home at a laptop writing a letter, a lamp on, calm resolve. Navy and gold only. No text.",
 "Three-card infographic with a man icon. Title (serif): «Втратив роботу: що робити з кредитом». Cards: «Договір діє, поки його не змінили», «Заява кредитору письмово, не дзвінок», «Банкрутство — крайній шлях, лише за заявою боржника». Small footer: «%s»",
 "Чоловік після втрати роботи складає письмову заяву кредитору","Що робити з кредитом після втрати роботи: три принципи"),
("10","yakshcho-ne-vyplachuvaty-kredyt","Якщо не виплачувати кредит","після вступу","після H2 «Що нараховують після прострочення: закон і межі»",
 "A person stands at the top of a descending staircase of five steps; on each step a small gold icon: a percent sign, a phone, an envelope, a gavel, a folder. A calm lawyer stands beside him pointing to the first step. No text.",
 "Staircase infographic with a person icon at the top. Title (serif): «Після прострочення: сходинки». Five descending steps: «Нарахування неустойки», «Дзвінки й листи», «Вимога повернути залишок», «Позов і рішення суду», «Виконавче провадження». Bottom gold strip: «Строки залежать від вашого договору». Small footer: «%s»",
 "Сходинки після прострочення кредиту: від неустойки до виконавчого провадження","П'ять етапів після прострочення кредиту"),
("11","chy-mozhna-splachuvaty-kredyt-z-za-kordonu","Чи можна сплачувати кредит з-за кордону","після вступу","після H2 «Порівняння способів оплати кредиту з-за кордону»",
 "A woman in a European city café pays a loan through a banking app on her phone; a thin gold dotted arc leads from her phone over a stylized map outline to a small bank-building icon labelled by shape only. Calm, modern. No text.",
 "Three-condition infographic with a person-with-phone icon. Title (serif): «Платіж з-за кордону: три умови». Cards: «Сума надійшла повністю», «Не пізніше дати за графіком», «У призначенні платежу — номер договору». Bottom gold strip: «Рахується дата зарахування, а не дата відправлення». Small footer: «%s»",
 "Жінка за кордоном сплачує кредит через мобільний застосунок","Три умови належного платежу за кредитом з-за кордону"),
("12","chy-mozhe-bank-zabuty-pro-kredyt","Чи може банк забути про кредит","після вступу","після H2 «Обмеження права банку діє за трьох умов»",
 "A man sits at a table looking thoughtfully at a closed envelope from a bank; behind him a large calendar and an hourglass in navy and gold; quiet, reflective mood. No text.",
 "Three-card infographic with a man-and-calendar icon. Title (serif): «Банк мовчить: що з боргом». Cards: «Борг не зникає сам», «Позовна давність — три роки», «Визнання боргу може поновити строк». Small footer: «%s»",
 "Чоловік розглядає лист від банку: давність не списує борг автоматично","Що відбувається з боргом, коли банк довго мовчить"),
]
md=["# urists.com.ua: промпти для картинок до 12 статей (ChatGPT / GPT Image)","",
"Для кожної статті 2 картинки: **A** — сюжетна ілюстрація з людьми (без тексту, вставити після вступу), **B** — інфографіка з людьми й українським текстом (вставити після вказаного H2).",
"Формат 3:2 (1536×1024). Назви файлів: `<slug>-a.png`, `<slug>-b.png`. Я переведу у webp 1200×800 і вставлю в чернетки.","",
"**Як користуватися:** кожен раз вставляйте спочатку ЗАГАЛЬНИЙ БЛОК СТИЛЮ, потім промпт картинки. Якщо в B помилки в кирилиці, не перегенеровуйте без кінця: надішліть мені картинку з чистим фоном, я накладу текст сам.","",
"## ЗАГАЛЬНИЙ БЛОК СТИЛЮ (вставляти перед кожним промптом)","","```",STYLE,"```",""]
h=["<h1>urists.com.ua: промпти для картинок до 12 статей (ChatGPT / GPT Image)</h1>",
"<p>Для кожної статті 2 картинки: <b>A</b> — сюжетна ілюстрація з людьми (без тексту, після вступу), <b>B</b> — інфографіка з людьми й українським текстом (після вказаного H2). Формат 3:2 (1536×1024). Назви файлів: &lt;slug&gt;-a.png, &lt;slug&gt;-b.png. Я переведу у webp 1200×800 і вставлю в чернетки.</p>",
"<p><b>Як користуватися:</b> кожен раз вставляйте спочатку ЗАГАЛЬНИЙ БЛОК СТИЛЮ, потім промпт картинки. Якщо в B помилки в кирилиці, не перегенеровуйте без кінця: надішліть мені картинку з чистим фоном, я накладу текст сам.</p>",
"<h2>ЗАГАЛЬНИЙ БЛОК СТИЛЮ (вставляти перед кожним промптом)</h2><p>"+html.escape(STYLE)+"</p>"]
for n,slug,t,placeA,placeB,pa,pb,altA,altB in A:
    pb=pb%FOOT
    md+= [f"## Стаття {int(n)}. {t}","",f"URL: `/blog/{slug}/`. Чернетка WP: див. нижче.",
          f"- **A** ({slug}-a): {placeA}. Alt: «{altA}»",f"- **B** ({slug}-b): {placeB}. Alt: «{altB}»","",
          "**Промпт A:**","```",pa,"```","","**Промпт B:**","```",pb,"```",""]
    h+= [f"<h2>Стаття {int(n)}. {html.escape(t)}</h2><p>URL: /blog/{slug}/</p>",
         f"<p><b>A</b> ({slug}-a): {placeA}. Alt: «{html.escape(altA)}»<br><b>B</b> ({slug}-b): {placeB}. Alt: «{html.escape(altB)}»</p>",
         f"<p><b>Промпт A:</b><br>{html.escape(pa)}</p>",f"<p><b>Промпт B:</b><br>{html.escape(pb)}</p>"]
open('IMAGE-PROMPTS.md','w',encoding='utf-8').write('\n'.join(md))
open('IMAGE-PROMPTS.html','w',encoding='utf-8').write('\n'.join(h))
print(len('\n'.join(md)))
