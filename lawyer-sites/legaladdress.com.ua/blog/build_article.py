#!/usr/bin/env python3
"""Сторінка статті legaladdress.com.ua з експорту Google Docs (HTML). Використання:
python3 build_article.py <№ статті> <doc.html>   -> out/article-<№>.html
python3 build_article.py <№> <doc.html> --post [parent_id]   -> створює/оновлює ЧЕРНЕТКУ (дочірня сторінка хабу)"""
import sys, os, json, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, '..', '..', '_blog-kit'))
import article_kit as K
from articles import ARTICLES
n = int(sys.argv[1]); doc = open(sys.argv[2], encoding='utf-8').read()
a = [x for x in ARTICLES if x[0] == n][0]
art = K.convert(doc)
hub = open(os.path.join(H, 'out/blog-hub.html'), encoding='utf-8').read()
d, mo, y = a[1].split('.')
meta = dict(site_url='https://legaladdress.com.ua', slug=a[2], date_iso=f'{y}-{mo}-{d}T09:00:00', topic=a[3], author_name='Бойчук Артем Валерійович',
            author_id='https://legaladdress.com.ua/#boychuk', tg='https://t.me/artem_adwokat',
            cta_title='Потрібна допомога з кредитом?', cta_text='Опишіть ситуацію в Telegram: розберемо договір, підкажемо, що робити, і складемо план дій.', announce=a[5])
page = K.build_page(hub, art, meta)
os.makedirs(os.path.join(H, 'out'), exist_ok=True)
open(os.path.join(H, f'out/article-{n}.html'), 'w', encoding='utf-8').write(page)
print('built', n, len(page), 'bytes; H1:', art['title'][:70], '| FAQ:', len(K.faq(art['body'])))
if '--post' in sys.argv:
    parent = int(sys.argv[sys.argv.index('--post') + 1]) if len(sys.argv) > sys.argv.index('--post') + 1 else 94
    payload = dict(title=art['title'], slug=a[2], status='draft', template='page-blank', parent=parent, content=page, excerpt=a[5])
    json.dump(payload, open('/tmp/_art.json', 'w', encoding='utf-8'), ensure_ascii=False)
    pid = sys.argv[sys.argv.index('--update') + 1] if '--update' in sys.argv else ''
    r = subprocess.run(['curl', '-sS', '-m', '120', '-X', 'POST', f'https://legaladdress.com.ua/wp-json/wp/v2/pages' + (f'/{pid}' if pid else ''), '-H', 'Content-Type: application/json', '--data-binary', '@/tmp/_art.json'], capture_output=True, text=True)
    try:
        j = json.loads(r.stdout); print({k: j.get(k) for k in ('id', 'status', 'slug', 'parent', 'link', 'template', 'code', 'message')})
    except Exception: print(r.stdout[:300])
