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
- 1843 → 1837: генератор (#generator) и 3 модели (#model) перенесены в cerere-de-stergere-din-biroul-de-credit.src.html (второй калькулятор: кнопка примера #b-ex2). 6 внутренних ссылок /model-cerere-stergere-biroul-de-credit/ → /cerere-de-stergere-din-biroul-de-credit/#model (gdpr, firme-care, bucuresti, avocat, cat-dureaza). Черновики 1837, 1846, 1849, 1852, 1855, 1858 обновлены и проверены. 1843 — черновик, не публиковать, не удалять без согласия.
- В 11 ТЗ-таблиц добавлена вкладка «Claude — доповнення» (чистая семантика, H1, H2, разграничение, [DE VERIFICAT]); для №52 insolventa sau faliment — полное новое ТЗ во вкладке «ТЗ (нове, Claude)». Оригинальные вкладки не трогались. При генерации текста брать сначала эти вкладки.
- Конвеєр, колонка «Примітки»: статусы ✅/⏳ и ссылки на вкладки.
- Открыто: №34/№36 — акценты при вёрстке; №8 (1813) — ссылка на №53 после его публикации.

## Дальше
1. Шаг 3: сверстать 8 готовых страниц (CTA → чат, без формы), черновиками WP.
2. Шаг 2: генерация 28 страниц партиями по 5–10.
