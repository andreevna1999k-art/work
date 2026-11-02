# _blog-kit: спільний будівельник макета блогу для сайтів на Elementor
1. Зняти стиль сайту (скриншот, кольори, шрифти) і записати в `lawyer-sites/<сайт>/STYLE.md`.
2. Створити дві чернетки через REST (`blog` і `blok-moi-statti-maket`, шаблон `elementor_canvas`), взяти їхні id.
3. Скопіювати `bankruptcyukraine.com/blog/config.py` і `run.py`, виправити кольори, шрифти, контакти, id.
4. `python3 blog/run.py` (хаб і превʼю), `python3 blog/run.py home` (копія Elementor-головної з шапкою і блоком).
5. Перевірити локально: `node _blog-kit/shot.js <blog-каталог> <hub_id> <preview_id> <каталог-png>`.
Сайт повинен мати доступ на запис у REST (секрет у налаштуваннях середовища).
