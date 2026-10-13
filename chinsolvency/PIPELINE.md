# Конвейер страниц Румыния (chinsolvency.ro) — состояние и следующие шаги

Обновлено: 13.10.2026. Продолжать с этого файла в новой сессии (после подключения Google Sheets и Google Docs).

## Где что лежит
- Основная папка Drive: https://drive.google.com/drive/folders/1FDoj6H01W8i_Ku6Na7ou6L1I6xc-uV-2
- Исходная таблица заказчика «Сторінки Румунія»: https://docs.google.com/spreadsheets/d/1svK--mhKf-kySA6zlME1Zb1O0MKmQeORd919slLLHh0 (колонки: Розділ, Фокусне слово, ТЗ, Текст старий, Текст новий, Зображення ×2)
- Наша таблица «Конвеєр сторінок Румунія»: https://docs.google.com/spreadsheets/d/1Ln8N7-6KksbWdcJdFHD0bzWOoj9ir_4IyFagNZR5Rd8 (колонка D = номер строки в исходной таблице)
- Инструкция: https://docs.google.com/document/d/1z4xbg70OV1bNDHjbZmHeOoGbmYodo_9Bx0NKrlDrTmI
- Папки разделов: Calculator 1QodD40JQ4-z5hfUMDLiOi8hJgnmOzZhA · Restructurare 1kYLmeRbFQHwaboOQf6SgLNlokv42OexQ · Recuperare 1L2o-SrWz-11UAZOi-30Zp7ElXdWHLaeH · Istoric/Biroul 14pwbcbLEcE1-46fJpwHzxUHLfz1T3M1_ · Avocat litigii bancare 1F_y6U45C2TrQQxv5un9vNt999ZqifAk2 · Executare silită 1jOSJBVISDElkFB_GKzJ0089hPnIyIvWn · Insolvență și faliment 16BdvEpq85C4qUFiOvN5HZe3aG0AXOC2_ (создана 13.10)
- В папке каждой страницы: «<H1> — text», «Аудит головреда — …», 2 картинки .webp 1200×675.

## Решения заказчика
- Вариант A: тексты и картинки делает Claude (без ChatGPT).
- Структура страниц — как у 22 сверстанных.
- CTA: все кнопки → http://chat.la.co.ua/o1r0iw (target=_blank). Формы нет. СДЕЛАНО на 22 черновиках 13.10 (build.py без FORM_SLOT собирает одну wp:html секцию).

## Правки таблиц — СДЕЛАНО 13.10 в обеих таблицах
Удалено 10 строк в «Сторінки Румунія» (теперь 58 ключей) и в «Конвеєр» (58 строк, вкладка «Конвеєр», колонка D пересчитана под новые номера строк, примечания в J). Номера ниже — СТАРЫЕ строки исходной таблицы (до удаления).

Удалить строки (дубли/каннибализация/компании):
| Строка | Ключ | Причина | Куда влить |
|---|---|---|---|
| 68 | insolventa iasi | полный дубль строки 66 (та же семантика, те же ТОП-10) | — |
| 48 | suspendarea executarii silite | ТЗ = копия кластера строки 42 (ТОП-10 совпадают 10/10) | 42 (страница про amânare + suspendare) |
| 76 | plan de reorganizare insolventa | тот же интент, что 65; пересекается с 11 | 65 |
| 51 | avocat executari silite | 4 общих URL в ТОП-10 со строкой 35 | 35 |
| 61 | intrarea in insolventa | 3 общих URL с 62, тот же смысл; H1 дублирует 60 | 62 |
| 63 | procedura simplificata insolventa | 4 общих URL с 71 | 71 (раздел «procedura simplificată») |
| 67 | somes sa dej insolventa | фирма в банкротстве с 2013, кластер про «compania de apa somes» | — |
| 73 | flamingo faliment | Flamingo International — банкротство 2009–2010, фирма ликвидирована | — |
| 74 | insolventa romaero | новость о конкретной госкомпании; используем как пример в 65 | 65 (пример: план реорганизации Romaero 2026) |
| 75 | amt servicii insolventa | фирма ликвидирована в 2015; ТЗ фактически про «administrator judiciar» | 70 |

Оставить с пометкой:
- 22 model cerere stergere biroul de credit (WP 1843) — ТОП-10 совпадают 10/10 со строкой 20 (WP 1837). Не публиковать отдельно: перенести генератор моделей в 1837, 1843 оставить черновиком (удалять только с согласия).
- 41 и 43 (CPC / termen contestatie) — 3 общих URL; тексты уже готовы, развести акценты при вёрстке (41 — статьи 712–720 CPC, 43 — расчёт 15 дней).
- 64 insolventa sau faliment — ТЗ скопировано со строки 63 (procedura simplificata) → нужно новое ТЗ (Claude может составить из семантики «faliment 12100 / insolvență 5400»).
- 52 executari focsani — семантика про Constanța/ANAF, H1 про Vrancea → чистить семантику.
- 69 insolventa bacau — в семантике мусор (запросы о сериале) → чистить.
- 38 lege recuperare creante — семантика смешана с ANPC; развести с 15 (legea împotriva recuperatorilor).
- 46 rabon credit solutions — делать: «Ai primit scrisoare de la Rabon?» права должника, без оценок компании.
- 70 consultant insolventa sprl — общая страница; не выдавать Consultarius за практика UNPIR.
- 66 insolventa iasi, 69 bacau — локальные страницы (компетентный Tribunal, BPI).

Итог: 68 → 58 страниц. Генерировать 38 − 10 = 28. Готовы к вёрстке 8 (строки 29, 30, 31, 34, 36, 39, 41, 43).

## Факты о компаниях
См. research-companies.md (источники, непроверенные пункты помечены).

## Примітки выполнены (13.10)
- 1843 → 1837: генератор (#generator) и 3 модели (#model) перенесены в cerere-de-stergere-din-biroul-de-credit.src.html (второй калькулятор: кнопка примера #b-ex2). 6 внутренних ссылок /model-cerere-stergere-biroul-de-credit/ → /cerere-de-stergere-din-biroul-de-credit/#model (gdpr, firme-care, bucuresti, avocat, cat-dureaza). Черновики 1837, 1846, 1849, 1852, 1855, 1858 обновлены и проверены. 1843 перемещена в корзину WP 13.10 (по согласию пользователя; восстановима ~30 дней).
- В 11 ТЗ-таблиц добавлена вкладка «Claude — доповнення» (чистая семантика, H1, H2, разграничение, [DE VERIFICAT]); для №52 insolventa sau faliment — полное новое ТЗ во вкладке «ТЗ (нове, Claude)». Оригинальные вкладки не трогались. При генерации текста брать сначала эти вкладки.
- Конвеєр, колонка «Примітки»: статусы ✅/⏳ и ссылки на вкладки.
- Открыто: №34/№36 — акценты при вёрстке; №8 (1813) — ссылка на №53 после его публикации.

## Проверка [DE VERIFICAT] (13.10) — выполнена на 21 сверстанной странице
Метод: WebSearch по официальным источникам и вторичным (прямой доступ к legislatie.just.ro, brd.ro из песочницы закрыт). На сайте пометок [DE VERIFICAT] не осталось: подтверждённое — вписано, неподтверждённое — общая формулировка без цифр.
Ключевые исправления:
- Регламент BNR 2/2012 утратил силу, заменён Регламентом BNR 4/2025 (с 01.12.2025).
- Полосы FICO «651–750 = bun» не имеют источника: заменено на «Biroul de Credit nu stabilește praguri; fiecare bancă are al ei» (+ калькулятор, FAQ, JSON-LD).
- Позитивные данные в Biroul de Credit обрабатываются по законному интересу, не по согласию: на странице GDPR «retragerea consimțământului» заменено на opoziție (art. 21).
- Контакты BdC: ул. Sfânta Vineri 29 (без «et. 4»), телефоны робота 021 311 02 67 / 021 310 42 60, GDPR-запросы — rpd@birouldecredit.ro. Приложение называется CredIT.
- Legea 243/2024: Lombard BNR 7,50% → потолок DAE 34,5% (потреб.) / 15,5% (ипотека); для договоров до 11.11.2024 — только по запросу потребителя, просрочка ≤ 60 дней (art. 8).
- reorganizare judiciara: срок плана 30 дней от публикации таблицы (+30 по уважительным причинам), 3 года (4 для юрлиц, art. 133 alin. 3^1), модификация до 5 лет (art. 139 alin. 5); голосование — art. 138–139; «12 luni observație» и «excepții 5 ani» убраны как неподтверждённые.
- ANAF: art. 162 CPF + OPANAF 558/2016; lista albă — Ordinul 1.923/2022; eșalonare 5 лет + fideiusiune, simplificată 12 мес. (из 2026).
Не подтверждено полностью (проверять по первоисточнику перед публикацией): тексты Legea 243/2024 art. 2 и 8; пороги art. 138; RIL 10/2015; сумма eșalonare simplificată 400.000 lei.
Romaero — ВНИМАНИЕ: цифры расходятся (785,5 млн = масса требований с правом голоса, не выплаты за 36 мес.; бюджетные долги ~467 vs ~550 млн). В ТЗ №53 помечено; на странице использовать только подтверждённое.
Не проверено: названия секций Tribunalul Iași/Bacău, URL реестра publicitatevanzari, компетентный суд по Legea 151/2015 (нужно для №43, 54, 55 при генерации).

## Сверка по первоисточникам (13.10, вечер) — доступ открыт частично
Доступны: lege5.ro (тексты в редакции Monitorul Oficial, без поздних изменений), unbr.ro. Закрыты/пустой ответ: legislatie.just.ro, birouldecredit.ro, anaf.ro, bnr.ro, bpi.ro, brd.ro, avocatnet.ro.
ПОДТВЕРЖДЕНО по тексту закона:
- Legea 85/2014: art. 132(1) 30 дней от публикации таблицы, 20% кредиторов, (2) продление до 30 дней, (4) ИСКЛЮЧЕНИЯ: 5 лет с прошлой процедуры + осуждённые администраторы/участники (мой ранний «фикс» их убрал — восстановлено), (5) утрата права на план → faliment; art. 133(3) 3 года (оригинал; «4 года для юрлиц» из поздних правок не подтверждено — смягчено); art. 139(1) пороги: 3 из 5 / 2 из 3 / половина при 2 или 4 категориях + одна defavorizată + 30% массы; art. 75(1) приостановка «de drept»; art. 66(1) 30 дней; art. 145(1) случаи faliment; art. 169 ответственность.
- Legea 243/2024: art. 4 (+8 п.п.), art. 5 (+27 п.п.), art. 8 (30 дней на предложение; отказ или задержка >45 дней → adaptare judiciară), art. 10 (действует для договоров, активных на 11.11.2024, в просрочке ≤ 60 дней; потолок — только к остатку основного долга на дату заявления).
- CPC art. 714: contestația — instanța de executare, 15 дней от узнавания об акте; art. 719: кауцион 10% до 10.000 lei, 1.000 + 5%, 5.500 + 1% свыше 100.000, 14.500 + 0,1% свыше 1 млн; неоценимое — 1.000 lei; RIL 2/2021 — приостановка до решения первой инстанции. (Номера alin. зависят от редакции.)
- Legea 151/2015 art. 10: компетентна judecătoria по месту жительства ≥ 6 мес. (НЕ tribunalul); tribunalul — апелляция.
- Romaero: 785,5 млн = масса с правом голоса; 467 млн бюджетных долгов AAAS → акции (подтверждено 2 источниками; 550 млн — нет); 94,33% голосов; решение 4474 от 04.08.2026; срок плана «36 мес.» не подтверждён.
- RIL по art. 348 CP: номер «10/2015» не подтверждён (возможно 15/2015) — на странице теперь без номера.
НЕ подтверждено (доступ закрыт): ANAF (приказы 558/2016, 1.923/2022, eșalonare simplificată 400.000), BdC/BNR/BRD (тарифы, контакты), названия секций tribunal Iași/Bacău, URL реестра публичных продаж.

## Вёрстка 8 готовых страниц — СДЕЛАНО 13.10 (черновики WP)
| № | Страница | WP ID |
|---|---|---|
| 23 | /avocat-specializat-credite-bancare/ | 1913 |
| 24 | /avocati-care-au-castigat-procese-cu-bancile/ | 1916 |
| 25 | /avocat-clauze-abuzive/ | 1919 |
| 27 | /avocat-contestatie-executare-silita/ | 1922 |
| 29 | /contestatie-la-executare/ | 1925 |
| 32 | /unde-se-depune-contestatia-la-executare/ | 1928 |
| 34 | /contestatia-la-executare-cod-procedura-civila/ | 1934 |
| 36 | /termen-contestatie-la-executare/ | 1937 |
Всё: CTA → чат, без формы, калькулятор на каждой, Drive-картинки загружены в WP (медиа 1911–1936), JSON-LD, проверено (errchk, мобильная ширина). Страницы 34/36 разведены по акцентам (34 — статьи CPC и кауцион art. 719; 36 — календарь с праздниками, дата + 16 дней).
Генератор: tools/gen/mk.py (шаблон страницы) + tools/gen/pNN.py (данные каждой страницы); запуск: `python3 tools/gen/pNN.py`, затем build.py → WP. go.sh.example — цепочка build → WP → проверка (нужны пути scratchpad).
Сверка по тексту CPC (lege5, art. 712–720, 651): art. 715(2) — 15 дней (НЕ 5) для нефинальных încheieri executor; art. 720(3) amendă 1.000–7.000 lei; art. 651(4) apel 10 zile; art. 714(2)/(3); art. 719 грид кауциона. RIL 20/2021 (много должников → judecătoria care a încuviințat) подтверждён по вторичным источникам.
Что убрано как неподтверждённое: «100 lei при неоценимом объекте» (taxa), art. 13 Legea 193/2000 (освобождение от кауциона), Decizia Tribunalul Iași 714/2016, ÎCCJ 10/2020, Legea 414/2023 (номер), art. 31 Legea 51/1995.
Ссылки на страницы, которых ещё нет (404 до их появления): /procedura-executare-silita-etape/ (№30), /amanare-executare-silita/ (№35), /poprire-cont/ (№40). Проверить при публикации.
Также исправлено на 5 страницах Biroul de Credit: «данные позитивные передаются с согласия» → законный интерес (opoziție, art. 21).

## Дальше
1. Шаг 2: генерация 28 страниц партиями по 5–10 (потом верстка тем же генератором tools/gen).
2. Публикация — решение начальника; перед публикацией открыть ссылки на ещё не созданные страницы.


## Генерація (крок 2): №30, №35, №40 — 13.10.2026
Тексти (HTML) у `texts/`, інфографіки (1200×675 WebP) у `img/`. Drive-папки в «Executare silită»: №30 `1oKz1FtkeaI7Nt9D836fFyD7JEAq26AWI`, №35 `1D67hudU-vLX4b4P41LMXsBn3-h6rUHZo`, №40 `1qvbBY0lPdsAWQcTqdhS8ZQNcMn4S12Bo` (текст + аудит; картинки у Drive не завантажені). Статус у Конвеєрі: 3. Далі — верстка (tools/gen) лише за запитом.

Верстка №30/35/40 (13.10): WP-чернетки 1949 (/procedura-executare-silita-etape/), 1950 (/amanare-executare-silita/), 1951 (/poprire-cont/); медіа 1943–1948. Калькулятори: №30 — утримання з доходу (art. 729), №35 — cauțiune (art. 719), №40 — останній день оскарження зі святами. Генератор: tools/gen/p30.py, p35.py, p40.py. Правило користувача: наступні сторінки робити одразу повним циклом (текст → картинки → верстка-чернетка) без питань.

Батч №31/33/37 (13.10): WP-чернетки 1958 (/lege-recuperare-creante/), 1959 (/executare-silita-definitie/), 1960 (/darea-in-plata-in-procedura-insolventei/); медіа 1952–1957. Drive-папки створені в «Executare silită». Генератор: tools/gen/p31.py, p33.py, p37.py; текст-док для Drive збирається з P скриптом tools/gen/mkdoc.py. №37: у ТЗ «darea în plată specială» нема в Legea 85/2014 — показати босу.

Батч 12 сторінок (13.10): WP-чернетки №26→1963, №28→1966, №38→1969, №41→1972, №42→1976, №48→1982, №49→1979, №50→1985, №51→1988, №52→1991, №53→1994, №57→1997 (медіа 1961–1996). Генератор: tools/gen/p26…p57.py + calcs.py (калькулятори), igx.py/imgs.py (інфографіки), mkdoc.py/audits.py (Drive-документи). ⚠ №52: у ТЗ-таблиці для ключа «insolventa sau faliment» лежить ТЗ про «procedura simplificata» — сторінка написана під ключ з Конвеєра + розділ про simplificată; показати босу. Не зроблено (потрібне зовнішнє дослідження): №39 Rabon, №43–47 executări по містах, №54–56 insolvență Iași/Bacău/consultant SPRL, №58 cum să scapi de datorii.
