import re,sys,importlib,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import json
PNG={k:v[1] for k,v in json.load(open('/tmp/pngmap.json')).items()} if os.path.exists('/tmp/pngmap.json') else {}
def doc(P,words=None):
    h=P['hero']; plain=lambda s:re.sub(r'<[^>]+>','',s)
    o=['<html><body>',f'<p><b>Title (≤60):</b> {P["title"]}</p>',f'<p><b>Meta description:</b> {P["desc"]}</p>',f'<p><b>URL:</b> /{P["slug"]}/</p>','<p><b>Schema:</b> Article + HowTo + FAQPage</p>','<p><b>Autor:</b> [DE COMPLETAT: nume avocat, titlu, barou, nr. legitimație, practică]</p>','<p><b>Actualizat:</b> 13 octombrie 2026</p>','<hr>',f'<h1>{plain(h["h1"])}</h1>']
    o+= [f'<p>{x}</p>' for x in h['lead']]
    o.append(f'<h2>Răspuns rapid</h2><p><b>{h["answer"]}</b></p>')
    imgs=iter(P['images']); 
    for i,l,body in P['sections']:
        b=re.sub(r'<span class="eyebrow">.*?</span>\s*','',body)
        b=re.sub(r'<!--@author.*?-->','',b)
        b=re.sub(r'<button.*?</button>','',b,flags=re.S)
        def fg(m):
            alt=re.search(r'alt="([^"]*)"',m.group(0)).group(1); src=re.search(r'/([^/"]+\.webp)',m.group(0)).group(1)
            if src in PNG: return f'<p><img src="{PNG[src]}" width="620" alt="{alt}"></p><p><i>{alt}</i></p>'
            return f'<p><b>[Infografic]</b> <i>{src}</i>. Alt: „{alt}”.</p>'
        b=re.sub(r'<figure>.*?</figure>',fg,b,flags=re.S)
        o.append(b)
    o.append('<h2>CTA</h2><p><a href="http://chat.la.co.ua/o1r0iw">Scrie-ne în chat</a></p>')
    o.append(f'<h2>{P["faq_h2"]}</h2>')
    for q,a in P['faq']: o.append(f'<h3>{q}</h3><p>{a}</p>')
    o.append('</body></html>'); return '\n'.join(o).replace('href="/','href="https://chinsolvency.ro/')
if __name__=='__main__':
    for n in sys.argv[1:]:
        P=importlib.import_module('p'+n).P
        s=doc(P); open(f'/tmp/doc{n}.html','w').write(s)
        print(n,len(s),len(re.sub(r'<[^>]+>',' ',s).split()))
