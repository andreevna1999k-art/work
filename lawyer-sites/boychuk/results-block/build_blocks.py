"""Builds the results + reviews blocks for page 13 (legaladdress.com.ua) from live page content.
usage: python3 build_blocks.py live13.html out.html [--local DIR]   (--local: images from DIR for preview)"""
import sys,re,json,html
live,out=sys.argv[1],sys.argv[2]
local=sys.argv[sys.argv.index('--local')+1] if '--local' in sys.argv else None
WP='https://legaladdress.com.ua/wp-content/uploads/2026/10/boychuk-rezultat-'
R=[ # slug, H3, text, alt
('tekhnofinans','ФК «Технофінанс»: графік погашення та довідка','Гарантійний лист від 06.08.2026: заборгованість 9 000 грн погашається двома платежами по 4 500 грн (до 06.08 і до 08.09.2026). Після повної сплати компанія гарантує довідку про відсутність заборгованості.','Гарантійний лист ФК «Технофінанс» про графік погашення 9 000 грн і довідку про відсутність заборгованості'),
('fintarhet','«Фінтаргет»: гарантійний лист із графіком платежів','Гарантійний лист від 19.08.2026: погашення двома платежами по 1 375 грн (до 25.08 і до 25.09.2026). Умови зафіксовано письмово, з реквізитами для оплати.','Гарантійний лист «Фінтаргет» від 19.08.2026 про два платежі по 1 375 грн'),
('sos-kredyt','«СОС Кредит»: заборгованість розбито на три платежі','Гарантійний лист від 13.08.2026: 10 562,75 грн можна погасити трьома платежами по 3 520,92 грн (14.08, 04.09 та 25.09.2026). У листі вказано строки та реквізити.','Гарантійний лист «СОС Кредит» від 13.08.2026 про погашення 10 562,75 грн трьома платежами'),
('na-hrup','ФК «Н.А. ГРУП» (CreditBox): строк погашення','Гарантійний лист: фінансова компанія зафіксувала пропозицію погашення заборгованості зі сплатою не пізніше 09.08.2026 та надала реквізити для платежу.','Гарантійний лист ФК «Н.А. ГРУП» (CreditBox) про строк погашення заборгованості до 09.08.2026'),
('eko-fin','«Еко Фін»: угода про розмір зобов’язання','Угода від 21.08.2026: за сплати 5 500 грн до 22.08.2026 стягувач припиняє подальше стягнення. В угоді зазначено прощення 5 400 грн відсотків і 92,60 грн штрафів.','Угода «Еко Фін» від 21.08.2026 про розмір зобов’язання та порядок його виконання'),
('slon-kredyt','«Слон Кредит»: індивідуальні умови погашення','Лист від 13.08.2026: заборгованість становила 23 443,75 грн (тіло 5 500, відсотки 7 218,75, штрафи 10 725 грн). Компанія запропонувала індивідуальні умови погашення.','Лист «Слон Кредит» від 13.08.2026 з розрахунком заборгованості та індивідуальною пропозицією'),
('maks-kredyt','Гарантійний лист: відсотки й неустойка підлягають прощенню','Гарантійний лист від 04.08.2026 про врегулювання заборгованості. Серед складових: відсотки 2 209 грн і неустойка 2 000 грн, які за умовами листа підлягають прощенню.','Гарантійний лист від 04.08.2026 про врегулювання заборгованості, прощення відсотків і неустойки'),
('kredyt-kapital','«Кредит-Капітал»: відмова від заходів стягнення','Гарантійний лист від 22.06.2026: за виконання умов до 30.06.2026 компанія відмовляється від запланованих заходів стягнення та надає довідку про відсутність претензій.','Гарантійний лист ФК «Кредит-Капітал» від 22.06.2026 про відмову від заходів стягнення'),
]
def src(slug): return (f'{local}/boychuk-rezultat-{slug}.webp' if local else f'{WP}{slug}.webp')
cards=''.join(f'''    <article class="res"><button class="res-photo" type="button" data-full="{src(s)}" data-alt="{html.escape(alt)}" aria-label="Збільшити: {html.escape(h)}"><img src="{src(s)}" alt="{html.escape(alt)}" width="1000" height="1414" loading="lazy"></button><h3>{html.escape(h)}</h3><p>{html.escape(t)}</p></article>
''' for s,h,t,alt in R)
RES=f'''<!-- 4 · РЕЗУЛЬТАТИ (8 карток, вертикальна сітка 4/2/1 без горизонтального скролу) -->
<section id="results"><div class="wrap">
<div class="pad" style="padding-left:12px;padding-right:12px">
  <div class="head"><span class="rule" style="background:var(--maroon)"></span><h2>Результати для клієнтів</h2>
  <p class="lead">Документи з реальних справ: гарантійні листи та угоди про врегулювання заборгованості. Персональні дані клієнтів закрито. Натисніть на документ, щоб збільшити.</p></div>
  <div class="res-grid">
{cards}  </div>
</div>
</div></section>
<div class="lb" id="lb" hidden><button class="lb-x" type="button" aria-label="Закрити">×</button><img id="lb-img" alt=""></div>
<script>
(function(){{var lb=document.getElementById('lb');var im=document.getElementById('lb-img');if(!lb){{return}}
function close(){{lb.hidden=true;im.removeAttribute('src');document.body.style.overflow=''}}
document.querySelectorAll('.res-photo').forEach(function(b){{b.addEventListener('click',function(){{im.src=b.getAttribute('data-full');im.alt=b.getAttribute('data-alt');lb.hidden=false;document.body.style.overflow='hidden'}})}});
lb.addEventListener('click',close);document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{close()}}}});}})();
</script>
'''
RV=[ # name, place/topic, date, stars, text
('Олена К.','Київ','жовтень 2026',5,'Банк підняв ціну за кредитом, а я не розуміла, що з цим робити. Артем Валерійович за одну консультацію розклав усе по пунктах: що в договорі, які в мене права і які кроки зробити першими. Було спокійніше вже після розмови.'),
('Андрій М.','Житомир','вересень 2026',5,'Телефонували колектори, і я боявся навіть брати слухавку. Підказали, що можна вимагати і як писати відповіді. Дзвінки припинилися, а я нарешті виспався.'),
('Ірина П.','Львів','серпень 2026',5,'Дуже чітко і без води. Одразу сказали, що реально, а чого не варто очікувати. Саме цього мені бракувало від інших юристів, які тільки обіцяють.'),
('Максим Т.','Дніпро','липень 2026',4,'Допоміг розібратися з виконавчим провадженням. Все пояснив простою мовою, відповідав у Telegram навіть увечері. Єдине, хотілося б швидше отримувати документи, але справа рухалася.'),
('Наталія С.','Харків','червень 2026',5,'Мені потрібна була консультація щодо реструктуризації кредиту. Отримала план дій, шаблон звернення до банку та терміни. Банк пішов на зустріч.'),
('Олександр В.','Одеса','травень 2026',5,'Було три МФО й суцільний стрес. Юрист допоміг зрозуміти, що по кожному кредиту законно, а що ні, і скласти спокійну стратегію. Дякую за людське ставлення.'),
('Тетяна Б.','Полтава','квітень 2026',5,'Звернулася щодо іпотечного кредиту. Мені пояснили, що таке звернення стягнення на предмет застави і які в мене варіанти. Нарешті стало зрозуміло, з чого починати.'),
('Володимир Г.','Київ','березень 2026',5,'Коротко: професіонал. Відповів на всі питання по договору, показав слабкі місця в нарахуваннях. Рекомендую всім, хто сумнівається, чи правильно банк рахує борг.'),
('Світлана Р.','Вінниця','лютий 2026',4,'Підтримали психологічно і юридично. Багато чого з документів була не в курсі, тепер знаю, на що звертати увагу. Зв’язок завжди був стабільний.'),
('Дмитро Л.','Запоріжжя','січень 2026',5,'Колектори писали рідним і колегам. Артем Валерійович пояснив, як на це реагувати за законом, і допоміг скласти звернення. Тиск зменшився.'),
('Юлія Н.','Черкаси','грудень 2025',5,'Консультація була конкретною: що робити сьогодні, що завтра, які документи зібрати. Без складних термінів, з прикладами. Дуже зручно, що все в месенджері.'),
('Богдан Ш.','Київ','листопад 2025',5,'Раніше вважав, що борг уже не вирішити. Після розмови зрозумів, що варіантів більше, ніж здавалося. Дякую за чесність і терпіння.'),
]
def stars(n): return '★'*n+'☆'*(5-n)
rv=''.join(f'''    <figure class="rv"><div class="rv-top"><span class="rv-st" aria-label="Оцінка {n} з 5">{stars(n)}</span><span class="rv-date">{d}</span></div><blockquote>{html.escape(t)}</blockquote><figcaption><b>{html.escape(nm)}</b><span>{html.escape(pl)}</span></figcaption></figure>
''' for nm,pl,d,n,t in RV)
REV=f'''<!-- 5 · ВІДГУКИ (ДЕМО: вигадані тексти для перегляду макета; ЗАМІНИТИ реальними або плагіном перед публікацією) -->
<section id="reviews"><div class="wrap">
<div class="panel on-brown pad">
  <div class="head"><span class="quote-mark">“</span><h2>Відгуки клієнтів</h2></div>
  <div class="rv-grid">
{rv}  </div>
  <p class="demo-note">Демо-відгуки для перегляду макета. Перед публікацією замінити реальними відгуками або плагіном.</p>
</div>
</div></section>
'''
CSS='''
/* results v2: vertical grid, no horizontal scroll */
.bz .res-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.bz .res{display:flex;flex-direction:column;min-width:0;padding:12px 12px 22px}
.bz .res-photo{display:block;width:100%;aspect-ratio:3/4;padding:0;margin:0 0 16px;border:1px solid var(--line);border-radius:var(--r-md);overflow:hidden;background:#fff;cursor:zoom-in;position:relative}
.bz .res-photo img{width:100%;height:100%;object-fit:cover;object-position:50% 0;transition:transform .35s}
.bz .res-photo:hover img{transform:scale(1.03)}
.bz .res-photo::after{content:"";position:absolute;left:0;right:0;bottom:0;height:46px;background:linear-gradient(0deg,rgba(255,255,255,.9),rgba(255,255,255,0))}
.bz .res h3{font-size:16.5px;line-height:1.25;margin:0 6px 8px}
.bz .res p{font-size:14.5px;line-height:1.55;margin:0 6px;color:var(--ink-soft)}
@media(max-width:1100px){.bz .res-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){.bz .res-grid{grid-template-columns:minmax(0,1fr);gap:16px}.bz .res-photo{aspect-ratio:4/5}.bz .res h3{font-size:18px}.bz .res p{font-size:15.5px}}
.lb{position:fixed;inset:0;z-index:99999;background:rgba(20,10,6,.88);display:flex;align-items:center;justify-content:center;padding:24px;overflow:auto}
.lb[hidden]{display:none}
.lb img{max-width:min(920px,100%);max-height:100%;width:auto;height:auto;border-radius:12px;background:#fff;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.lb-x{position:fixed;top:14px;right:18px;width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.4);background:rgba(0,0,0,.4);color:#fff;font-size:28px;line-height:1;cursor:pointer}
/* reviews v2: vertical masonry columns */
.bz .rv-grid{column-count:3;column-gap:18px}
.bz .rv{break-inside:avoid;margin:0 0 18px;padding:24px 24px 20px;border:1px solid var(--line-d);border-radius:var(--r-card);background:rgba(244,230,208,.07)}
.bz .rv-top{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:12px}
.bz .rv-st{color:var(--gold);letter-spacing:.12em;font-size:17px}
.bz .rv-date{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:rgba(244,230,208,.6)}
.bz .rv blockquote{margin:0 0 16px;font-size:16.5px;line-height:1.6;color:var(--cream)}
.bz .rv figcaption{display:flex;flex-direction:column;gap:2px;border-top:1px solid var(--line-d);padding-top:12px}
.bz .rv figcaption b{font-family:var(--f-head);font-weight:400;font-size:18px;letter-spacing:.04em;color:var(--cream)}
.bz .rv figcaption span{font-size:13.5px;color:rgba(244,230,208,.65)}
.bz .demo-note{margin-top:22px;padding:12px 16px;border:1px dashed var(--gold);border-radius:14px;font-size:13.5px;color:var(--cream-soft);text-align:center}
@media(max-width:1000px){.bz .rv-grid{column-count:2}}
@media(max-width:640px){.bz .rv-grid{column-count:1}.bz .rv{padding:20px 18px 16px}}
'''
s=open(live,encoding='utf-8').read()
# results section
a=s.index('<!-- 4 · РЕЗУЛЬТАТИ'); b=s.index('<!-- 5 · ВІДГУКИ')
c=s.index('<!-- ФУТЕР · КОНТАКТИ')
s=s[:a]+RES+'\n'+REV+'\n'+s[c:]
# css: insert before the closing </style> (first)
i=s.index('</style>'); s=s[:i]+CSS+s[i:]
open(out,'w',encoding='utf-8').write(s)
print('ok',len(s),'&& count:',s.count('&&'),'wp tail:',s.rstrip()[-30:])
json.dump([dict(slug=a,h=b,t=c) for a,b,c,d in R],open(out+'.meta.json','w'),ensure_ascii=False)
