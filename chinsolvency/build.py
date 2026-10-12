"""Build WordPress-ready pages: inject shared brand.css and split around the form shortcode.

Usage: python3 build.py <page.src.html> <out_dir>
Writes <name>.html (full page, form placeholder for local preview) and <name>.wp.txt (block markup for WP).
"""
import sys, pathlib

FORM = '[sureforms id="1762"]'

src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
brand = (src.parent / 'brand.css').read_text(encoding='utf-8')
article = (src.parent / 'article.css').read_text(encoding='utf-8')
html = src.read_text(encoding='utf-8').replace('/*BRAND_CSS*/', brand).replace('/*ARTICLE_CSS*/', article)
name = src.name.replace('.src.html', '')

before, after = html.split('<!-- FORM_SLOT -->')
(out / f'{name}.wp.txt').write_text(
    f'<!-- wp:html -->\n{before}\n<!-- /wp:html -->\n\n'
    f'<!-- wp:shortcode -->\n{FORM}\n<!-- /wp:shortcode -->\n\n'
    f'<!-- wp:html -->\n{after}\n<!-- /wp:html -->', encoding='utf-8')
stub = '<div style="height:260px;border:1px dashed #ccc;border-radius:12px;display:grid;place-items:center;color:#999">[SureForms]</div>'
(out / f'{name}.html').write_text(
    '<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    '<style>body{margin:0}</style></head><body>' + before + stub + after + '</body></html>', encoding='utf-8')
print('built', name)
