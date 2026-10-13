import json,html,re
def esc(s): return html.escape(s,quote=False)
def plain(s): return re.sub(r'<[^>]+>','',s)
CAL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
CLK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>'
ARW='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5l8 7-8 7z"/></svg>'
CHAT='http://chat.la.co.ua/o1r0iw'
def build(p):
    o=[]
    o.append(f'<!-- Consultarius — /{p["slug"]}/ (draft). Built by build.py (partials + CSS injection). -->')
    o.append('<!--@head -->')
    if p.get('css'): o.append('<style>\n'+p['css']+'\n</style>')
    o.append('<div class="cbx">\n')
    o.append(f'<!--@header nav="{p["nav"]}" -->\n')
    h=p['hero']
    o.append(f'''<!-- HERO -->
<section class="hero a-hero">
  <div class="wrap">
    <div class="hero-box">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Acasă</a><span>/</span><span>{p["crumb"]}</span></nav>
      <div class="a-hero-grid">
        <div>
          <span class="eyebrow">{h["eyebrow"]}</span>
          <h1>{h["h1"]}</h1>
          <div class="lead">
{chr(10).join("            <p>"+x+"</p>" for x in h["lead"])}
          </div>
          <div class="meta">
            <span>{CAL}Actualizat: {p.get("date","13 octombrie 2026")}</span>
            <span>{CLK}{h["meta2"]}</span>
          </div>
          <div class="hero-cta">
            <a href="#calculator" class="btn btn-primary">{h["cta"]}</a>
            <a href="{CHAT}" target="_blank" rel="noopener" class="btn btn-ghost">Consultație gratuită {ARW}</a>
          </div>
        </div>
        <aside class="answer">
          <h2>Răspuns rapid</h2>
          <p>{h["answer"]}</p>
          <div class="opts">
{chr(10).join("            <div><b>"+a+"</b>"+b+"</div>" for a,b in h["opts"])}
          </div>
        </aside>
      </div>
    </div>
  </div>
</section>
''')
    o.append('<!-- CALCULATOR -->\n'+p['calc_html']+'\n')
    toc='\n'.join(f'      <a href="#{i}">{l}</a>' for i,l,_ in p['sections'])+'\n      <a href="#intrebari">Întrebări frecvente</a>'
    o.append(f'''<!-- ARTICLE -->
<section style="padding-top:32px">
  <div class="wrap article">
    <nav class="toc" aria-label="Cuprins">
      <b>Cuprins</b>
{toc}
    </nav>

    <div class="prose">
''')
    for i,l,body in p['sections']:
        o.append(f'      <section id="{i}">\n{body}\n      </section>\n')
    faq=p['faq']
    items='\n'.join(f'          <details{" open" if k==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for k,(q,a) in enumerate(faq))
    o.append(f'''      <section id="intrebari" class="faq-wide" style="padding-bottom:0">
        <span class="eyebrow">Întrebări frecvente</span>
        <h2>{p["faq_h2"]}</h2>
        <div class="faq">
{items}
        </div>
      </section>

    </div>
  </div>
</section>
''')
    c=p['contact']
    o.append(f'<!--@contact h2="{c["h2"]}" lead="{c["lead"]}" nav="{c["nav"]}" note="{c["note"]}" -->\n')
    o.append('</div>\n')
    o.append('<script>\n(function(){\n  var $=function(id){return document.getElementById(id)};\n  var root=document.querySelector(\'.cbx\'); if(!root) return;\n'+p['js']+'\n})();\n</script>\n')
    url=f'https://chinsolvency.ro/{p["slug"]}/'
    g=[{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Acasă","item":"https://chinsolvency.ro/"},{"@type":"ListItem","position":2,"name":p["crumb"],"item":url}]},
       {"@type":"Article","headline":p["title"],"description":p["desc"],"inLanguage":"ro","dateModified":p.get("date_iso","2026-10-13"),"mainEntityOfPage":url,"image":["https://chinsolvency.ro/wp-content/uploads/2026/10/"+x for x in p["images"]],"author":{"@type":"Organization","name":"Consultarius"},"publisher":{"@type":"Organization","name":"Consultarius"}}]
    if p.get('howto'):
        t=p['howto']; g.append({"@type":"HowTo","name":t["name"],"inLanguage":"ro","step":[{"@type":"HowToStep","position":k+1,"name":a,"text":b} for k,(a,b) in enumerate(t["steps"])]})
    g.append({"@type":"LegalService","name":"Consultarius","url":"https://chinsolvency.ro/","areaServed":"RO","knowsAbout":p["knows"]})
    g.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":plain(q),"acceptedAnswer":{"@type":"Answer","text":plain(a)}} for q,a in faq]})
    ld=json.dumps({"@context":"https://schema.org","@graph":g},ensure_ascii=False)
    o.append('<script type="application/ld+json">\n'+ld+'\n</script>\n')
    return '\n'.join(o)
def fig(img,alt,cap): return f'''        <figure>
          <img src="https://chinsolvency.ro/wp-content/uploads/2026/10/{img}" width="1200" height="675" alt="{alt}" loading="lazy">
          <figcaption>{cap}</figcaption>
        </figure>'''
