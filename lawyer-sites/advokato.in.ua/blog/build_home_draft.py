#!/usr/bin/env python3
"""Створює/оновлює ЧЕРНЕТКУ-копію головної advokato.in.ua (Elementor) із шапкою-навігацією, якорями і блоком «Мої статті».
Живу головну (id 516) не змінює: бере її з backup-page516-live-*.json (знято через REST) і публікує як нову сторінку-чернетку.
Запуск: python3 build_home_draft.py [id_чернетки]   (без id створює нову; id друкується)"""
import json, os, sys, subprocess, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import build_blog as B

live = json.load(open(os.path.join(H, 'backup-page516-live-20261102.json'), encoding='utf-8'))
meta = live['meta']
data = json.loads(meta['_elementor_data'])
ids = ['top', 'about', 'experience', 'results', 'reviews']          # п'ять контейнерів верхнього рівня: hero, Освіта, Досвід, Результати, Відгуки
assert len(data) == 5
for el, anchor in zip(data, ids):
    el['settings']['_element_id'] = anchor

zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
def wrap(eid, html, bg=None):
    c = {"id": eid, "elType": "container", "settings": {"content_width": "full", "padding": zero, "margin": zero, "flex_gap": {"size": "0", "unit": "px", "column": "0", "row": "0", "isLinked": True}, "flex_direction": "column"},
         "elements": [{"id": eid + "w", "elType": "widget", "widgetType": "html", "settings": {"html": html, "_margin": zero}, "elements": [], "isInner": False}], "isInner": False}
    return c

header_html = f'<style>{B.HDR_CSS}</style>' + B.header('', '')
block_html = f'<style>{B.CSS}</style><div class="kv">{B.section(True, 3)}</div>'
anchor_html = '<span id="contacts" style="display:block;height:0"></span>'
out = [wrap('kvhdr01', header_html)] + data[:4] + [wrap('kvblk01', block_html)] + data[4:] + [wrap('kvanc01', anchor_html)]

payload = {
    "title": "ЧЕРНЕТКА: Головна з шапкою і блоком «Мої статті» (макет)",
    "slug": "golovna-chernetka-shapka-blog",
    "status": "draft",
    "content": live['content']['raw'],
    "meta": {k: v for k, v in meta.items() if v not in ('', None, [], {}, False, 0) and not k.startswith('_yoast')},
}
payload["meta"]["_elementor_data"] = json.dumps(out, ensure_ascii=False)
json.dump(payload, open('/tmp/home_draft.json', 'w', encoding='utf-8'), ensure_ascii=False)
pid = sys.argv[1] if len(sys.argv) > 1 else ''
url = 'https://advokato.in.ua/wp-json/wp/v2/pages' + (f'/{pid}' if pid else '')
r = subprocess.run(['curl', '-sS', '-m', '90', '-X', 'POST', url, '-H', 'Content-Type: application/json', '--data-binary', '@/tmp/home_draft.json'], capture_output=True, text=True)
try:
    j = json.loads(r.stdout); print({k: j.get(k) for k in ('id', 'status', 'slug', 'template', 'link', 'code', 'message')})
except Exception:
    print(r.stdout[:400])
