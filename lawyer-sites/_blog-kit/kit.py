#!/usr/bin/env python3
"""Спільний будівельник макета блогу для сайтів на Elementor (шапка-навігація, хаб, блок «Мої статті», копія головної).
Кожен сайт описується словником cfg (кольори ролями, шрифти, контакти). Приклад: ../bankruptcyukraine.com/blog/config.py
Нічого не публікує на живих сторінках: усе йде в нові чернетки."""
import os, json, html, base64, subprocess
e = html.escape
LEAD_DEFAULT = 'Пояснюю питання кредитів, боргів і захисту боржників простою мовою: що каже закон, як діє суд і що варто зробити в першу чергу.'

def items(cfg):
    A = cfg.get('articles') or []
    if A: return A
    return [(i, 'ДД.ММ.РРРР', '', 'Тема статті', 'Назва статті, яка займе один-два рядки',
             'Короткий анонс статті на дві-три речення. Текст з’явиться, коли стаття буде готова.') for i in range(1, cfg.get('placeholders', 6) + 1)]

def card(cfg, a):
    n, d, slug, topic, title, ann = a
    u = f'/blog/{slug}/' if slug else '/blog/'
    p = os.path.join(cfg['dir'], 'photos', slug + '.webp') if slug else ''
    img = ''
    if p and os.path.exists(p):
        img = f'<img src="data:image/webp;base64,{base64.b64encode(open(p,"rb").read()).decode()}" alt="{e(title)}" width="760" height="507" loading="lazy" decoding="async">'
    dt = f'<time datetime="{d[6:]}-{d[3:5]}-{d[:2]}">{d}</time>' if slug else f'<time>{d}</time>'
    return (f'<article class="bl-card"><a class="bl-cover" href="{u}" tabindex="-1">{img}<span class="bl-tag">{e(topic)}</span></a>'
            f'<div class="bl-body">{dt}<h3><a href="{u}">{e(title)}</a></h3><p>{e(ann)}</p><a class="bl-more" href="{u}">Читати статтю</a></div></article>')

def css(cfg):
    c, f = cfg['colors'], cfg['fonts']
    btn_solid = f".kv .btn{{display:inline-block;padding:15px 30px;background:{c['btn_bg']};color:{c['btn_fg']};font:700 13px/1 {f['body']};letter-spacing:.08em;text-transform:uppercase;border:0;transition:.2s}}.kv .btn:hover{{background:{c['btn_hover']};color:{c['btn_fg']}}}"
    btn_out = f".kv .btn{{display:inline-block;padding:15px 30px;border:1px solid {c['btn_bg']};color:{c['btn_bg']};font:400 14px/1 {f['body']};letter-spacing:.08em;text-transform:uppercase;background:transparent;transition:.2s}}.kv .btn:hover{{background:{c['btn_bg']};color:{c['btn_fg']}}}"
    btn = btn_solid if cfg.get('btn_style', 'solid') == 'solid' else btn_out
    cta_h = (f"background:{c['btn_bg']};color:{c['btn_fg']};border:0;font-weight:700;" if cfg.get('btn_style', 'solid') == 'solid' else f"border:1px solid {c['btn_bg']};")
    return f"""
@import url('{f['import']}');
.kv{{font-family:{f['body']};font-size:16px;line-height:1.6;color:{c['sec_text']};background:{c['sec_bg']};position:relative;width:100%;margin:0;overflow:hidden;-webkit-font-smoothing:antialiased}}
.kv *{{box-sizing:border-box}}.kv h1,.kv h2,.kv h3,.kv p,.kv ul,.kv li{{margin:0;padding:0}}.kv ul{{list-style:none}}
.kv a{{color:inherit;text-decoration:none;border:0;box-shadow:none}}
.kv h1,.kv h2,.kv h3{{font-family:{f['head']};font-weight:{f['head_weight']};line-height:1.2;text-transform:none;letter-spacing:0}}
.kv .w{{max-width:1180px;margin:0 auto;padding:0 24px}}
.kv .bar{{display:block;width:60px;height:3px;background:{c['hero_text']};margin:18px 0 0}}
{btn}
.kv .hero{{position:relative;background:linear-gradient(90deg,{c['hero_left']} 0 50%,{c['hero_right']} 50% 100%);padding:150px 0 90px;color:{c['hero_text']}}}
.kv .hero h1{{color:{c['hero_text']};font-size:clamp(34px,4.6vw,56px)}}
.kv .hero .w{{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;position:relative}}
.kv .hero .sub{{margin-top:22px;font:700 18px/1.4 {f['body']};color:{c['hero_text']}}}
.kv .hero .lead{{margin-top:14px;max-width:470px;opacity:.92}}
.kv .hero .btn{{margin-top:30px}}
.kv .hero .ph{{justify-self:end;width:min(100%,430px)}}
.kv .hero .ph img{{width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;object-position:50% 20%;border-radius:{cfg.get('photo_radius','28px')};display:block;box-shadow:0 24px 50px rgba(0,0,0,.3)}}
.kv .sec{{padding:80px 0 90px;background:{c['sec_bg']}}}
.kv .sec.pre{{padding-top:140px}}
.kv .sec h2{{font-size:clamp(28px,3.6vw,44px);text-align:center;color:{c['sec_title']}}}
.kv .sec .bar{{margin:18px auto 0;background:{c['sec_title']}}}
.kv .sec .lead2{{max-width:660px;margin:20px auto 0;text-align:center}}
.kv .bl-g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:44px}}
.kv .bl-card{{display:flex;flex-direction:column;min-width:0;background:{c['card_bg']};border-radius:{cfg.get('card_radius','6px')};overflow:hidden;box-shadow:0 14px 40px rgba(2,23,109,.12);transition:transform .2s}}
.kv .bl-card:hover{{transform:translateY(-4px)}}
.kv .bl-cover{{position:relative;display:block;aspect-ratio:3/2;overflow:hidden;background:linear-gradient(135deg,{c['cover_a']},{c['cover_b']})}}
.kv .bl-cover img{{width:100%;height:100%;object-fit:cover;display:block}}
.kv .bl-tag{{position:absolute;top:14px;left:14px;padding:6px 14px;background:{c['tag_bg']};color:{c['tag_fg']};font:700 11px/1.2 {f['body']};letter-spacing:.12em;text-transform:uppercase}}
.kv .bl-body{{display:flex;flex-direction:column;flex:1;padding:22px 24px 26px}}
.kv .bl-card time{{display:block;margin-bottom:10px;font:700 13px/1 {f['body']};letter-spacing:.06em;color:{c['card_meta']}}}
.kv .bl-card h3{{font-size:19px;line-height:1.3;margin:0 0 12px;color:{c['card_title']}}}
.kv .bl-card h3 a:hover{{color:{c['card_meta']}}}
.kv .bl-card p{{margin:0 0 20px;font-size:16px;color:{c['card_text']}}}
.kv .bl-more{{margin-top:auto;font:700 13px/1 {f['body']};letter-spacing:.1em;text-transform:uppercase;color:{c['card_title']}}}
.kv .bl-more::after{{content:" \\2192"}}.kv .bl-more:hover{{color:{c['card_meta']}}}
.kv .all{{text-align:center;margin-top:44px}}
.kv .ft{{background:{c['footer_bg']};color:{c['footer_text']};padding:70px 0 60px}}
.kv .ft .w{{display:grid;grid-template-columns:repeat(3,1fr);gap:40px}}
.kv .ft h3{{font-size:20px;margin-bottom:18px;color:{c['footer_title']}}}
.kv .ft p,.kv .ft li{{font-size:16px;margin-bottom:10px}}
.kv .ft a{{color:{c['footer_link']}}}.kv .ft a:hover{{color:#fff}}
.kv .ft .copy{{max-width:1180px;margin:44px auto 0;padding:24px 24px 0;border-top:1px solid rgba(255,255,255,.2);font-size:14px;opacity:.8}}
@media(max-width:900px){{.kv .hero{{background:linear-gradient(180deg,{c['hero_left']} 0 64%,{c['hero_right']} 64% 100%)}}.kv .hero .w{{grid-template-columns:1fr}}.kv .hero .ph{{justify-self:start;width:min(100%,360px)}}.kv .bl-g{{grid-template-columns:repeat(2,minmax(0,1fr))}}.kv .ft .w{{grid-template-columns:1fr;gap:28px}}}}
@media(max-width:620px){{.kv .bl-g{{grid-template-columns:minmax(0,1fr);gap:16px}}.kv .sec{{padding:60px 0 70px}}.kv .bl-body{{padding:18px 18px 22px}}}}
"""

def hdr_css(cfg):
    c, f = cfg['colors'], cfg['fonts']
    cta = (f"background:{c['btn_bg']};color:{c['btn_fg']};border:0;font-weight:700;" if cfg.get('btn_style', 'solid') == 'solid' else f"border:1px solid {c['header_text']};")
    return f"""
html{{scroll-padding-top:90px;scroll-behavior:smooth}}
.kvh{{position:fixed;top:0;left:0;right:0;z-index:99999;background:{c['header_bg']};border-bottom:1px solid rgba(255,255,255,.18);font-family:{f['body']}}}
body.admin-bar .kvh{{top:32px}}@media(max-width:782px){{body.admin-bar .kvh{{top:46px}}}}
.kvh *{{box-sizing:border-box}}.kvh a{{color:{c['header_text']};text-decoration:none;border:0;box-shadow:none}}
.kvh .in{{max-width:1280px;margin:0 auto;padding:0 24px;height:68px;display:flex;align-items:center;justify-content:space-between;gap:24px}}
.kvh .logo{{font:{f['head_weight']} 20px/1 {f['head']};white-space:nowrap}}
.kvh .menu{{display:flex;gap:26px;font-size:13px;letter-spacing:.1em;text-transform:uppercase;margin-left:auto;font-weight:700}}
.kvh .menu a{{padding:6px 0;border-bottom:2px solid transparent;white-space:nowrap}}.kvh .menu a:hover,.kvh .menu a.cur{{border-bottom-color:{c['accent']}}}
.kvh .cta{{padding:11px 20px;{cta}font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap;transition:.2s}}.kvh .cta:hover{{background:#fff;color:{c['header_bg']}}}
.kvh .cb{{position:absolute;opacity:0;pointer-events:none;width:0;height:0}}
.kvh .burger{{display:none;width:42px;height:42px;border:1px solid {c['header_text']};cursor:pointer;position:relative;flex:none}}
.kvh .burger i,.kvh .burger i::before,.kvh .burger i::after{{content:"";position:absolute;left:10px;width:20px;height:2px;background:{c['header_text']}}}
.kvh .burger i{{top:20px}}.kvh .burger i::before{{left:0;top:-7px}}.kvh .burger i::after{{left:0;top:7px}}
.kvh .cb:checked ~ .burger i{{background:transparent}}.kvh .cb:checked ~ .burger i::before{{top:0;transform:rotate(45deg)}}.kvh .cb:checked ~ .burger i::after{{top:0;transform:rotate(-45deg)}}
@media(max-width:1060px){{.kvh .cta{{display:none}}.kvh .menu{{gap:18px}}}}
@media(max-width:860px){{.kvh .in{{height:60px}}.kvh .burger{{display:block;margin-left:auto}}.kvh .menu{{display:none;margin:0}}
 .kvh .cb:checked ~ .menu{{display:flex;flex-direction:column;gap:0;position:absolute;top:60px;left:0;right:0;background:{c['header_bg']};padding:8px 16px 16px;border-top:1px solid rgba(255,255,255,.18)}}
 .kvh .cb:checked ~ .menu a{{padding:15px 4px;border-bottom:1px solid rgba(255,255,255,.12);font-size:14px}}.kvh .cb:checked ~ .menu a:last-child{{border-bottom:0}}}}
"""

def header(cfg, prefix='/', cur=''):
    nav = cfg['nav']  # [(текст, якір)], якір None = /blog/
    def a(text, anchor):
        href = '/blog/' if anchor == 'blog' else prefix + '#' + anchor
        return f'<a href="{href}"' + (' class="cur"' if cur == anchor else '') + f'>{text}</a>'
    return (f'<div class="kvh"><div class="in"><a class="logo" href="/">{e(cfg["logo"])}</a><input type="checkbox" id="kvhm" class="cb" aria-hidden="true" tabindex="-1">'
            '<nav class="menu" aria-label="Меню">' + ''.join(a(t, k) for t, k in nav) + '</nav>'
            f'<a class="cta" href="{cfg["tg"]}" target="_blank" rel="noopener">Консультація</a><label for="kvhm" class="burger" aria-label="Меню"><i></i></label></div></div>')

def footer(cfg):
    soc = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in cfg['socials'])
    art = ''.join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in [('Блог: усі статті', '/blog/')] + cfg['useful'])
    return (f'<footer class="ft" id="contacts"><div class="w"><div><h3>Контакти</h3><p><a href="tel:{cfg["tel"]}">{cfg["phone"]}</a></p><p>{soc}</p></div>'
            f'<div><h3>Графік роботи</h3><p>{cfg["hours"]}</p></div><div><h3>Корисні статті</h3><ul>{art}</ul></div></div>'
            f'<div class="copy">© {e(cfg["full_name"])}</div></footer>')

def hide(cfg, pid):
    return (f'body.page-id-{pid} .entry-header,body.page-id-{pid} .ast-breadcrumbs-wrapper,body.page-id-{pid} .entry-title,body.page-id-{pid} .site-footer{{display:none!important}}'
            f'body.page-id-{pid} .ast-container,body.page-id-{pid} #primary,body.page-id-{pid} .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}')

def section(cfg, heading=True, n=3, pre=False):
    lead = cfg.get('lead', LEAD_DEFAULT)
    return ('<section class="sec%s" id="articles"><div class="w">' % (' pre' if pre else '') +
            (f'<h2>Мої статті</h2><span class="bar"></span><p class="lead2">{lead}</p>' if heading else '') +
            '<div class="bl-g">' + ''.join(card(cfg, a) for a in items(cfg)[:n]) + '</div>' +
            ('<div class="all"><a class="btn" href="/blog/">Усі статті</a></div>' if heading else '') + '</div></section>')

def hub(cfg):
    lead = cfg.get('lead', LEAD_DEFAULT)
    hero = ('<header class="hero"><div class="w"><div><h1>Мої статті</h1><span class="bar"></span>' + f'<p class="sub">{cfg["role"]}</p>'
            f'<p class="lead">{lead}</p><a class="btn" href="{cfg["tg"]}" target="_blank" rel="noopener">Безкоштовна консультація</a></div>'
            f'<div class="ph"><img src="{cfg["portrait"]}" alt="{e(cfg["full_name"])}" width="640" height="640"></div></div></header>')
    return (f'<!-- wp:html -->\n<style>{css(cfg)}{hdr_css(cfg)}{hide(cfg, cfg["hub_id"])}</style>\n{header(cfg, "/", "blog")}<div class="kv">{hero}{section(cfg, False, 99)}{footer(cfg)}</div>\n<!-- /wp:html -->')

def preview(cfg):
    return (f'<!-- wp:html -->\n<style>{css(cfg)}{hdr_css(cfg)}{hide(cfg, cfg["preview_id"])}</style>\n{header(cfg, "/")}<div class="kv">{section(cfg, True, 3, True)}{footer(cfg)}</div>\n<!-- /wp:html -->')

def snippet(cfg):
    return f'<style>{css(cfg)}</style>\n<div class="kv">{section(cfg, True, 3)}</div>'

# ---------- REST ----------
def post(site, path, payload):
    open('/tmp/_kit.json', 'w', encoding='utf-8').write(json.dumps(payload, ensure_ascii=False))
    r = subprocess.run(['curl', '-sS', '-m', '120', '-X', 'POST', f'https://{site}/wp-json/wp/v2/{path}', '-H', 'Content-Type: application/json', '--data-binary', '@/tmp/_kit.json'], capture_output=True, text=True)
    try: return json.loads(r.stdout)
    except Exception: return {'raw': r.stdout[:300]}

def get(site, path):
    r = subprocess.run(['curl', '-sS', '-m', '90', f'https://{site}/wp-json/wp/v2/{path}'], capture_output=True, text=True)
    return json.loads(r.stdout)

def build_pages(cfg):
    out = os.path.join(cfg['dir'], 'out'); os.makedirs(out, exist_ok=True)
    for n, fn in [('blog-hub.html', hub), ('block-preview.html', preview), ('home-block-snippet.html', snippet)]:
        open(os.path.join(out, n), 'w', encoding='utf-8').write(fn(cfg))

def upload_pages(cfg):
    res = {}
    for pid, n in [(cfg['hub_id'], 'blog-hub.html'), (cfg['preview_id'], 'block-preview.html')]:
        j = post(cfg['site'], f'pages/{pid}', {'content': open(os.path.join(cfg['dir'], 'out', n), encoding='utf-8').read(), 'template': 'elementor_canvas'})
        res[pid] = {k: j.get(k) for k in ('id', 'status', 'template', 'code', 'message')}
    return res

KEYS = [('Освіта', 'about'), ('Досвід', 'experience'), ('Результат', 'results'), ('Відгук', 'reviews')]
def _texts(el, acc):
    s = el.get('settings', {})
    if not isinstance(s, dict): s = {}
    for k in ('title', 'editor', 'text'):
        if isinstance(s.get(k), str): acc.append(s[k])
    for c in el.get('elements', []): _texts(c, acc)
    return acc

def home_draft(cfg, live, draft_id=None):
    """live: JSON головної (context=edit: meta, content). Повертає (відповідь REST, список якорів)."""
    meta = live['meta']; data = json.loads(meta['_elementor_data'])
    anchors = ['top'] + [None] * (len(data) - 1)
    for i, el in enumerate(data[1:], 1):
        t = ' '.join(_texts(el, []))
        for key, anc in KEYS:
            if key.lower() in t.lower() and anc not in anchors:
                anchors[i] = anc; break
    for el, an in zip(data, anchors):
        if not isinstance(el.get('settings'), dict): el['settings'] = {}   # у PHP порожні налаштування приходять як []
        if an: el['settings']['_element_id'] = an
    zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
    def wrap(eid, h):
        return {"id": eid, "elType": "container", "settings": {"content_width": "full", "padding": zero, "margin": zero, "flex_gap": {"size": "0", "unit": "px", "column": "0", "row": "0", "isLinked": True}, "flex_direction": "column"},
                "elements": [{"id": eid + "w", "elType": "widget", "widgetType": "html", "settings": {"html": h, "_margin": zero}, "elements": [], "isInner": False}], "isInner": False}
    ri = anchors.index('results') if 'results' in anchors else (anchors.index('reviews') - 1 if 'reviews' in anchors else len(data) - 1)
    out = [wrap('kvhdr01', f'<style>{hdr_css(cfg)}</style>' + header(cfg, '', ''))] + data[:ri + 1] + \
          [wrap('kvblk01', f'<style>{css(cfg)}</style><div class="kv">{section(cfg, True, 3)}</div>')] + data[ri + 1:] + \
          [wrap('kvanc01', '<span id="contacts" style="display:block;height:0"></span>')]
    payload = {"title": "ЧЕРНЕТКА: Головна з шапкою і блоком «Мої статті» (макет)", "slug": "golovna-chernetka-shapka-blog", "status": "draft",
               "content": live['content']['raw'], "meta": {k: v for k, v in meta.items() if v not in ('', None, [], {}, False, 0) and not k.startswith('_yoast')}}
    payload["meta"]["_elementor_data"] = json.dumps(out, ensure_ascii=False)
    return post(cfg['site'], 'pages' + (f'/{draft_id}' if draft_id else ''), payload), anchors
