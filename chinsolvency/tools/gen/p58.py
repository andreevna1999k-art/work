import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'snowball-sau-avalanche':('Metode de plată','Snowball sau Avalanche?',
   table(['','Snowball','Avalanche'],[['Ordinea plății','Întâi datoria cu soldul cel mai mic','Întâi datoria cu dobânda cea mai mare'],['Avantaj','Câștiguri rapide, motivație','Costuri totale de dobândă mai mici'],['Dezavantaj','Poți plăti mai multă dobândă în total','Prima datorie poate dura mult'],['Se potrivește când','Ai multe datorii mici și ai nevoie de motivație','Ai dobânzi foarte diferite între datorii']]),
   'Metode generale de gestionare a datoriilor; nu sunt sfat financiar personalizat.','Metoda Snowball și metoda Avalanche pentru plata datoriilor: ordinea plății, avantaj, dezavantaj și când se potrivesc','Snowball sau Avalanche'),
 'pasii-pentru-a-scapa-de-datorii':('Plan în 6 pași','Pașii ca să scapi de datorii',
   steps([('Listează','Toate datoriile','Sold, dobândă anuală, rată, scadență'),('Buget','Venituri − cheltuieli','Cât poți plăti real, lunar'),('Alege metoda','Snowball sau Avalanche','Ordinea în care plătești'),('Negociază','Cu creditorii','Eșalonare, reducere de dobândă, în scris'),('Verifică drepturile','Executare, prescripție','Contestație în 15 zile (art. 715 CPC)'),('Soluții juridice','Dacă nu mai ajunge','Insolvență pentru persoane fizice (Legea 151/2015)')],
   'Dacă primești acte de executare, termenul de contestație curge din ziua primirii: nu aștepta.'),
   'Orientativ; nu înlocuiește consultanța juridică sau financiară.','Pașii pentru a scăpa de datorii: listă, buget, metodă, negociere, verificarea drepturilor, soluții juridice','Pașii ca să scapi de datorii'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
rows=''.join(f'''          <div class="field"><label for="d{i}b">Datoria {i}: sold (lei)</label><div class="inp"><input id="d{i}b" inputmode="numeric" placeholder="{v[0]}"></div></div>
          <div class="field"><label for="d{i}r">Dobândă anuală (%)</label><div class="inp"><input id="d{i}r" inputmode="decimal" placeholder="{v[1]}"></div></div>
          <div class="field"><label for="d{i}m">Rată minimă lunară (lei)</label><div class="inp"><input id="d{i}m" inputmode="numeric" placeholder="{v[2]}"></div></div>
''' for i,v in [(1,(3000,25,150)),(2,(10000,18,400)),(3,(25000,9,700))])
fields='          <div class="grp">Datoriile tale</div>\n'+rows+'''          <div class="grp">Bugetul</div>
          <div class="field full"><label for="f-x">Sumă suplimentară pe lună, peste ratele minime (lei)</label><div class="inp"><input id="f-x" inputmode="numeric" placeholder="300"></div></div>'''
outs='''            <div class="opt full" id="c-t"><span class="k">Metoda Avalanche (dobânda cea mai mare întâi)</span><span class="v" id="o-t" style="font-size:19px">—</span><span class="s" id="o-ts">Introdu cel puțin o datorie.</span></div>
            <div class="opt" id="c-m"><span class="k">Metoda Snowball (soldul cel mai mic întâi)</span><span class="v" id="o-m" style="font-size:17px">—</span><span class="s" id="o-ms"> </span></div>
            <div class="opt" id="c-r"><span class="k">Diferență de dobândă</span><span class="v" id="o-r" style="font-size:17px">—</span><span class="s" id="o-rs">Avalanche față de Snowball.</span></div>'''
calc=calcs._shell('Cât durează să plătești datoriile: <span class="accent">Snowball sau Avalanche</span>','Introdu până la trei datorii (sold, dobândă anuală și rată minimă) și o sumă suplimentară lunară. Simulăm lună cu lună ambele metode și îți arătăm durata și dobânda totală.',fields,'Exemplu: 3 datorii și 300 lei în plus pe lună',outs,'Simulare orientativă: dobânda se calculează lunar (dobândă anuală ÷ 12), iar rata minimă și suma suplimentară se plătesc după calcularea dobânzii. Nu include comisioane, penalități sau modificări de dobândă. Nu este sfat financiar personalizat.')
js=r'''  function lei(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/\s/g,'').replace(',','.');return v===''?0:parseFloat(v)}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function sim(ds,extra,mode){
    var b=ds.map(function(d){return d.b}),r=ds.map(function(d){return d.r/1200}),m=ds.map(function(d){return d.m});
    var tot=0,ti=0,mo=0,n=ds.length,i;
    for(i=0;i<n;i++){tot+=b[i]}
    while(tot>0.5){
      mo++;if(mo>600){return null}
      var pool=extra;
      for(i=0;i<n;i++){if(b[i]>0){var it=b[i]*r[i];b[i]+=it;ti+=it}}
      for(i=0;i<n;i++){if(b[i]>0){var p=Math.min(m[i],b[i]);b[i]-=p}else{pool+=m[i]}}
      while(pool>0.01){
        var k=-1;
        for(i=0;i<n;i++){if(b[i]>0.005){
          if(k<0){k=i}
          else if(mode==='a'){if(r[i]>r[k]){k=i}}
          else{if(b[k]>b[i]){k=i}}
        }}
        if(k<0){break}
        var q=Math.min(pool,b[k]);b[k]-=q;pool-=q;
      }
      tot=0;for(i=0;i<n;i++){tot+=Math.max(b[i],0)}
    }
    return {mo:mo,int:ti};
  }
  function calc(){
    var ds=[],i;
    for(i=1;i<=3;i++){var b=num('d'+i+'b');if(b>0){ds.push({b:b,r:num('d'+i+'r'),m:num('d'+i+'m')})}}
    var x=num('f-x');
    if(ds.length===0){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Introdu cel puțin o datorie.';$('o-m').textContent='—';$('o-r').textContent='—';return}
    var bad=false;if(0>=x){bad=ds.some(function(d){return 0>=d.m})}
    if(bad){$('o-t').textContent='Completează rata minimă sau suma suplimentară';cls('c-t','alert');$('o-m').textContent='—';$('o-r').textContent='—';return}
    var A=sim(ds,x,'a'),S=sim(ds,x,'s');
    if(!A||!S){$('o-t').textContent='Peste 50 de ani: ratele nu acoperă dobânda';cls('c-t','alert');$('o-ts').textContent='Mărește suma lunară sau negociază dobânda.';$('o-m').textContent='—';$('o-r').textContent='—';return}
    $('o-t').textContent=A.mo+' luni, dobândă totală '+lei(A.int);cls('c-t','ok');$('o-ts').textContent='Dobânda cea mai mare se plătește prima.';
    $('o-m').textContent=S.mo+' luni, dobândă '+lei(S.int);$('o-ms').textContent='Soldul cel mai mic se plătește primul.';
    var dif=S.int-A.int;$('o-r').textContent=(dif>0?lei(dif)+' mai puțin cu Avalanche':'Fără diferență semnificativă');cls('c-r',dif>0?'ok':'');
  }
  $('b-calc').addEventListener('click',calc);
  ['d1b','d1r','d1m','d2b','d2r','d2m','d3b','d3r','d3m','f-x'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){var v={d1b:3000,d1r:25,d1m:150,d2b:10000,d2r:18,d2m:400,d3b:25000,d3r:9,d3m:700,'f-x':300};Object.keys(v).forEach(function(k){$(k).value=v[k]});calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Cum scapi de datorii: răspuns rapid</h2>
        <p>Ca să scapi de datorii ai nevoie de patru lucruri, în ordine: o listă completă a datoriilor (sold, dobândă, rată), un buget realist, o metodă de plată (Snowball sau Avalanche) și, dacă nu mai ajungi, soluții juridice: negociere cu creditorii, contestarea unei executări nelegale sau insolvența persoanei fizice (Legea nr. 151/2015). Nu aștepta actele de executare: contestația se face, în general, în 15 zile (art. 715 CPC).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Ai trei datorii: 3.000 lei la 25% pe an, 10.000 lei la 18% și 25.000 lei la 9%, cu rate minime de 150, 400 și 700 lei, plus 300 lei în plus pe lună. Simularea din calculator arată în câte luni le stingi cu fiecare metodă și cât plătești în dobânzi. Dacă ordinea contează, diferența dintre cele două metode este exact dobânda totală.</p>
          <span class="formula">rate minime + 300 lei = suma lunară totală pentru datorii</span>
          <button type="button" class="btn btn-line" data-ex="1">Vezi în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Cauze</span>
        <h2>De ce apar datoriile și cum le recunoști</h2>
        <p>Datoriile apar din venituri care scad, cheltuieli neprevăzute, credite luate pentru a plăti alte credite și din dobânzi care se adună. Cele mai frecvente tipuri sunt creditele bancare, cardurile de credit, împrumuturile de la IFN-uri, datoriile fiscale și facturile neplătite.</p>
        <h3>Semne că situația devine periculoasă</h3>
        <ul class="chk">
          <li>Întârzieri repetate la plată și penalități care cresc.</li>
          <li>Refinanțări repetate fără strategie.</li>
          <li>Folosești cardul de credit pentru nevoi curente.</li>
          <li>Ai primit somație sau acte de la executor.</li>
        </ul>'''
S3='''        <span class="eyebrow">Plan</span>
        <h2>Cum scapi de datorii, pas cu pas</h2>
'''+F('pasii-pentru-a-scapa-de-datorii')+'''
        <ol class="num">
          <li><b>Listează toate datoriile:</b> creditor, sold, dobândă anuală, rată, scadență.</li>
          <li><b>Fă un buget realist:</b> venituri minus cheltuieli esențiale. O regulă generală este 50/30/20: 50% nevoi, 30% dorințe, 20% economii și plata datoriilor; adaptează-o, nu o aplica orbește.</li>
          <li><b>Alege metoda:</b> Snowball sau Avalanche (vezi mai jos).</li>
          <li><b>Negociază cu creditorii:</b> reducerea ratei, restructurare, eșalonare; acordul trebuie să fie în scris. Vezi <a href="/restructurare-credit-vs-refinantare/">restructurare sau refinanțare</a>.</li>
          <li><b>Verifică-ți drepturile:</b> dacă ai acte de executare, vezi mai jos.</li>
        </ol>'''
S4='''        <span class="eyebrow">Metode</span>
        <h2>Snowball sau Avalanche: care e mai bună</h2>
'''+F('snowball-sau-avalanche')+'''
        <p>Snowball plătește întâi datoria cu soldul cel mai mic, ceea ce dă rezultate rapide și motivație. Avalanche plătește întâi datoria cu dobânda cea mai mare, ceea ce reduce, de regulă, costul total. Calculatorul de mai sus arată diferența pe cifrele tale. Refinanțarea sau consolidarea creditelor poate scădea rata, dar verifică costul total și comisioanele.</p>'''
S5='''        <span class="eyebrow">Buget</span>
        <h2>Cum reduci cheltuielile și îți crești veniturile</h2>
        <ul class="chk">
          <li><b>Elimină ce nu e esențial:</b> abonamente nefolosite, cumpărături impulsive.</li>
          <li><b>Renegociază facturile:</b> telefonie, internet, asigurări.</li>
          <li><b>Venituri suplimentare:</b> activități pe cont propriu, vânzarea bunurilor nefolosite, program extra.</li>
          <li><b>Automatizează:</b> plata ratelor și un transfer lunar către economii, imediat după salariu.</li>
        </ul>'''
S6='''        <span class="eyebrow">Juridic</span>
        <h2>Soluții juridice pentru datorii mari</h2>
        <h3>Executarea silită și drepturile tale</h3>
        <p>Executarea silită se face numai pe baza unui titlu executoriu (art. 632 CPC). Salariul și pensia pot fi urmărite până la o treime din venitul net la datorii obișnuite, iar la mai multe urmăriri până la jumătate (art. 729); alocațiile de stat și indemnizațiile pentru copii nu pot fi urmărite (art. 729 alin. 7). Poți contesta executarea, în general în 15 zile (art. 712, 715), poți cere suspendarea cu cauțiune (art. 719) sau poți opri măsurile consemnând toată datoria (art. 721). Dreptul de a cere executarea se prescrie în 3 ani, dar prescripția trebuie invocată (art. 706–707). Detalii: <a href="/procedura-executare-silita-etape/">procedura executării silite</a>, <a href="/contestatie-la-executare/">contestația la executare</a>, <a href="/poprire-cont/">poprirea pe cont</a>.</p>
        <h3>Insolvența persoanei fizice</h3>
        <p>Persoanele fizice neprofesioniste au o procedură separată, Legea nr. 151/2015, depusă la judecătorie (art. 10), cu posibilitatea eliberării de datoriile reziduale. Condițiile exacte nu sunt reproduse aici și trebuie verificate în textul consolidat și cu un specialist. Pentru firme și profesioniști se aplică Legea nr. 85/2014: vezi <a href="/insolventa/">insolvența explicată simplu</a>.</p>
        <h3>Drepturile consumatorului</h3>
        <p>Clauzele abuzive din contractul de credit pot fi contestate în instanță; vezi <a href="/avocat-clauze-abuzive/">avocat clauze abuzive</a>. Dacă ești contactat de recuperatori, vezi <a href="/legea-impotriva-recuperatorilor-de-credite/">legea împotriva recuperatorilor</a>.</p>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli care te mențin în datorii</h2>
        <ul class="chk">
          <li>Folosești cardul de credit pentru cheltuieli curente.</li>
          <li>Refinanțezi continuu, fără strategie și fără să calculezi costul total.</li>
          <li>Nu ai un fond de urgență, așa că orice cheltuială neprevăzută devine datorie nouă.</li>
          <li>Ignori actele de executare sau depășești termenul de contestație.</li>
        </ul>'''
S8='''        <span class="eyebrow">După datorii</span>
        <h2>Cum ajungi la libertate financiară</h2>
        <p>După ce achiți datoriile, mută rata în economii: construiește un fond de siguranță (de regulă 3–6 luni de cheltuieli, ca regulă generală, nu ca obligație legală), apoi economisește și investește treptat. Păstrează bugetul lunar și un plafon pentru cheltuieli pe card. Informațiile financiare de aici sunt generale și nu constituie sfat de investiții.</p>
        <!--@author practice="datorii persoane fizice" -->'''
faq=[("Cum pot scăpa rapid de datorii?","Listezi toate datoriile, faci un buget, alegi o metodă (Snowball sau Avalanche), negociezi cu creditorii și, dacă nu ajunge, verifici soluțiile juridice."),
("Care este cea mai eficientă metodă pentru plata datoriilor?","Nu există una singură. Avalanche reduce, de regulă, dobânda totală; Snowball oferă rezultate rapide și motivație. Calculatorul îți arată diferența pe cifrele tale."),
("Ce este metoda Snowball?","Plătești rata minimă la toate datoriile și restul banilor merg la datoria cu soldul cel mai mic; apoi treci la următoarea."),
("Ce este metoda Avalanche?","Plătești rata minimă la toate și restul banilor merg la datoria cu dobânda cea mai mare."),
("Cum negociez cu creditorii?","Ceri în scris reducerea ratei, restructurarea sau eșalonarea, cu dovada veniturilor și un plan realist; orice acord se face în scris."),
("Ce se întâmplă dacă nu mai pot plăti ratele?","Creditorul poate trimite somație și, dacă are titlu executoriu, poate cere executarea silită. Ai drept de contestație, în general în 15 zile (art. 715 CPC)."),
("Pot intra în insolvență ca persoană fizică?","Persoanele fizice neprofesioniste pot folosi Legea nr. 151/2015, cu condiții pe care trebuie să le verifici în textul consolidat și cu un specialist."),
("Cum evit să mă îndatorez din nou?","Un buget lunar, un fond de siguranță, un plafon pentru card și un calcul al costului total înainte de orice credit nou.")]
P=dict(slug='cum-sa-scapi-de-datorii',crumb='Cum să scapi de datorii',
 title='Cum să scapi de datorii: metode, buget și soluții juridice',
 desc='Cum scapi de datorii: lista datoriilor, buget, metoda Snowball sau Avalanche (cu calculator), negociere cu creditorii și soluții juridice: executare silită, contestație, insolvență.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#plan|Plan;#metode|Metode;#juridic|Soluții juridice;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Datorii · Snowball · Avalanche · soluții juridice',
  h1='Cum să scapi de datorii și să ajungi la <span class="accent">libertate financiară</span>',
  lead=['Ratele s-au adunat, dobânzile cresc și nu mai știi pe ce să plătești întâi. Cea mai mare greșeală este să aștepți: fiecare lună de întârziere adaugă dobânzi, iar actele de executare vin cu termene scurte.',
        'Aici ai planul, două metode de plată cu un calculator care le compară pe cifrele tale și soluțiile juridice, de la negociere la contestarea executării și insolvență.'],
  meta2='Contestație la executare: 15 zile',cta='Compară metodele',
  answer='Ca să scapi de datorii, listezi toate datoriile (sold, dobândă, rată), faci un buget realist, alegi o metodă de plată (Snowball: întâi soldul mic; Avalanche: întâi dobânda mare), negociezi cu creditorii în scris și, dacă nu mai ajungi, verifici soluțiile juridice. Dacă primești acte de executare, contestația se face, în general, în 15 zile (art. 715 CPC).',
  opts=[('Snowball','soldul mic întâi'),('Avalanche','dobânda mare întâi'),('Executare','contestație în 15 zile')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('cauze','Cauze',S2),('plan','Plan',S3),('metode','Metode',S4),('buget','Buget',S5),('juridic','Soluții juridice',S6),('greseli','Greșeli',S7),('dupa','După datorii',S8)],
 faq=faq,faq_h2='Întrebări frecvente despre scăparea de datorii',
 contact=dict(h2='Ai datorii pe care nu le mai poți plăti?',lead='Trimite-ne lista datoriilor și actele primite de la creditori sau de la executor. Îți spunem în aceeași zi ce termene curg și ce soluții ai. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat creditorilor, executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum scapi de datorii',steps=[('Listezi datoriile','Sold, dobândă anuală, rată, scadență.'),('Faci bugetul','Venituri minus cheltuieli esențiale.'),('Alegi metoda','Snowball sau Avalanche.'),('Negociezi','Cu creditorii, în scris.'),('Verifici drepturile','Contestație la executare în 15 zile; soluții juridice dacă nu mai ajungi.')]),
 knows=['Datorii','Snowball','Avalanche','Executare silită','Insolvență persoane fizice'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/cum-sa-scapi-de-datorii.src.html','w',encoding='utf-8').write(build(P))
