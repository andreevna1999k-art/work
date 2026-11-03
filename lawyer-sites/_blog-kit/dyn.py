#!/usr/bin/env python3
"""Автообновлювані картки блогу: JS бере з публічного REST WordPress лише ОПУБЛІКОВАНІ дочірні сторінки хабу
(анонімний запит повертає тільки статус publish, тож заплановані статті з'являються самі в день виходу).
Дані карток: заголовок, дата, анонс (excerpt) і посилання беруться з сайту; тема й фото — з вбудованої мапи slug -> {t, i}."""
import json, os, base64, html

def photo_map(items, photos_dir):
    m = {}
    for a in items:
        n, d, slug, topic, title, ann = a
        p = os.path.join(photos_dir, slug + '.webp')
        m[slug] = {'t': topic}
        if os.path.exists(p):
            m[slug]['i'] = 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
    return m

def script(parent_id, limit, items, photos_dir, count_id='blogCount', grid_id='blogGrid'):
    data = json.dumps(photo_map(items, photos_dir), ensure_ascii=False)
    return ('<script>(function(){var g=document.getElementById("' + grid_id + '");if(!g)return;var M=' + data + ';var LIM=' + str(limit) + ';'
            'function T(s){var d=document.createElement("div");d.innerHTML=s;return(d.textContent||"").replace(/\\s+/g," ").trim()}'
            'function D(s){var p=String(s).slice(0,10).split("-");return p[2]+"."+p[1]+"."+p[0]}'
            'function E(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}'
            'fetch("/wp-json/wp/v2/pages?parent=' + str(parent_id) + '&per_page=100&orderby=date&order=desc&_fields=id,date,link,slug,title,excerpt",{credentials:"omit"})'
            '.then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(a){'
            'var c=document.getElementById("' + count_id + '");if(c){c.textContent=a.length;var lb=document.getElementById("' + count_id + 'Label"),n=a.length%100,k=a.length%10;if(lb)lb.textContent=(n>10&&n<15)||k==0||k>4?"статей":(k==1?"стаття":"статті")}'
            'if(!a.length){g.appendChild(E("p","bl-empty","Перші статті з’являться найближчим часом."));return}'
            'a.slice(0,LIM).forEach(function(x){var u=new URL(x.link,location.href).pathname,m=M[x.slug]||{t:"Стаття"},ti=T(x.title.rendered);'
            'var art=E("article","bl-card"),cv=E("a","bl-cover");cv.href=u;cv.tabIndex=-1;'
            'if(m.i){var im=new Image();im.src=m.i;im.alt=ti;im.width=760;im.height=507;im.loading="lazy";cv.appendChild(im)}'
            'cv.appendChild(E("span","bl-tag",m.t));art.appendChild(cv);'
            'var b=E("div","bl-body"),mt=E("div","bl-meta"),tm=E("time",null,D(x.date));tm.setAttribute("datetime",String(x.date).slice(0,10));mt.appendChild(tm);b.appendChild(mt);'
            'var h=E("h3"),l=E("a",null,ti);l.href=u;h.appendChild(l);b.appendChild(h);b.appendChild(E("p",null,T(x.excerpt&&x.excerpt.rendered||"")));'
            'var mr=E("a","bl-more","Читати статтю");mr.href=u;b.appendChild(mr);art.appendChild(b);g.appendChild(art)})})'
            '.catch(function(){g.appendChild(E("p","bl-empty","Не вдалося завантажити статті. Спробуйте оновити сторінку."))})})();</script>')

EXTRA_CSS = ".bz .bl-empty{grid-column:1/-1;text-align:center;color:var(--ink-soft);padding:30px 10px;font-size:18px}"
