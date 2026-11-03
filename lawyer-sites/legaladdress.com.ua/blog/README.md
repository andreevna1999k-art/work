# Блог legaladdress.com.ua — чернетки (02.11.2026)
- Чернетка хабу: WP page id 94 (slug `blog`). Чернетка головної з блоком «Мої статті»: page id 95. Жива головна (id 13) не змінена.
- `articles.py` — 12 статей (з таблиці), `build_blog.py` — збірка в `out/`. Бекапи живих сторінок 13 і 48 — `backup-*-live-20261102.html`.
- Обкладинки: фото з ChatGPT у `photos-src/NN-*.webp` (NN = № статті), `make_photos.py` стискає до `photos/`, `build_blog.py` вбудовує їх у картки як data-URI (медіатека WP закрита правами на `uploads/2026/11`). Векторні сцени `covers_*.py` лишились як запасний варіант.
- Посилання у картках ведуть на `/blog/<slug>/` — сторінок статей ще немає (404 до їх створення).
- Після схвалення: бекап id 13 → оновити id 13 вмістом `out/home-with-articles.html`, id 94 опублікувати, додати «Блог» у меню на id 48/59/60 (шапка і футер).

## Сторінки статей (03.11.2026)
- `build_article.py <№> <doc.html> [--post 94 [--update <id>]]` збирає сторінку статті з експорту Google Docs (HTML) в стилі сайту: H1, мета-рядок, чистий текст, таблиці, FAQ, JSON-LD (Article + FAQPage), блок CTA. Конвертер: `../../_blog-kit/article_kit.py`.
- Експорт документа: Google Drive `download_file_content` з `exportMimeType=text/html` (base64; при великому розмірі зберігається у файл).
- Пробна стаття №1: WP page id 105, чернетка, дочірня сторінка хабу (id 94), адреса після публікації хабу: `/blog/shcho-bude-za-prostrochennia-kredytu/`.
- Розклад: статус `future` і дата з таблиці; sitemap — вбудований `/wp-sitemap.xml` (додає сторінки сам після виходу).
