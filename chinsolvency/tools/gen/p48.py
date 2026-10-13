import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'formula-durata-de-recuperare':('Indicator financiar','Durata medie de recuperare (DSO)',
   '<div class="row">'+'<div class="card" style="flex:1"><div class="k">Creanțe de încasat</div><div class="v">120.000 lei</div><div class="s">Soldul clienților la sfârșitul perioadei</div></div><div class="v" style="align-self:center;color:#8c1d24;font-size:40px">÷</div><div class="card" style="flex:1"><div class="k">Vânzări pe perioadă</div><div class="v">600.000 lei</div><div class="s">Cifra de afaceri, pe 365 de zile</div></div><div class="v" style="align-self:center;color:#8c1d24;font-size:40px">×</div><div class="card" style="flex:.6"><div class="k">Zile</div><div class="v">365</div><div class="s">în perioadă</div></div></div>'
   '<div class="card dark" style="margin-top:20px;display:flex;align-items:center;gap:24px"><div class="v" style="font-size:44px;margin:0;white-space:nowrap">73 zile</div><div class="s" style="font-size:18px;margin:0">durata medie de încasare; dacă termenul din contract este de 30 de zile, întârzierea medie este de 43 de zile</div></div>',
   'Formulă: creanțe ÷ vânzări × numărul de zile. Exemplu orientativ.','Formula duratei medii de recuperare a creanțelor: creanțe împărțite la vânzări, înmulțite cu zilele din perioadă, exemplu 73 de zile','Formula duratei de recuperare (DSO)'),
 'etapele-si-termenele-recuperarii':('Amiabil → executare','Termene în recuperarea juridică',
   steps([('Somația','Cu dovadă','Termen de plată stabilit de tine'),('Titlul','Hotărâre sau ordonanță','Dacă nu ai un titlu executoriu'),('Încuviințarea','3 zile','Executorul decide fără citare (art. 666)'),('Poprirea','5 zile','Terțul consemnează suma (art. 787)'),('Prescripția','3 ani','Dreptul de a cere executarea (art. 706)')],
   'Perimarea: <b>6 luni</b> de inactivitate din culpa creditorului, la cererea scrisă a executorului (art. 697).'),
   'Cod procedură civilă. Orientativ.','Etapele și termenele recuperării juridice: somație, titlu, încuviințare în 3 zile, poprire în 5 zile, prescripție 3 ani','Etapele și termenele recuperării'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
fields='''          <div class="grp">Datele firmei</div>
          <div class="field"><label for="f-v">Creanțe de încasat, sold (lei)</label><div class="inp"><input id="f-v" inputmode="numeric" placeholder="120000"></div></div>
          <div class="field"><label for="f-d">Vânzări în perioadă (lei)</label><div class="inp"><input id="f-d" inputmode="numeric" placeholder="600000"></div></div>
          <div class="field"><label for="f-s">Perioada</label><div class="inp"><select id="f-s"><option value="365">12 luni (365 de zile)</option><option value="90">Trimestru (90 de zile)</option><option value="30">Lună (30 de zile)</option></select></div></div>
          <div class="field"><label for="f-t">Termenul de plată din contract (zile)</label><div class="inp"><input id="f-t" inputmode="numeric" placeholder="30"></div></div>'''
outs='''            <div class="opt full" id="c-t"><span class="k">Durata medie de recuperare</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Introdu creanțele și vânzările.</span></div>
            <div class="opt" id="c-m"><span class="k">Întârziere medie</span><span class="v" id="o-m">—</span><span class="s" id="o-ms">Față de termenul din contract.</span></div>
            <div class="opt" id="c-r"><span class="k">Creanțe ca % din vânzări</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Sold ÷ vânzări.</span></div>'''
calc=calcs._shell('Durata medie de recuperare <span class="accent">a creanțelor (DSO)</span>','Calculează în câte zile încasezi, în medie, facturile emise, și cât depășești termenul din contract. Formula este un indicator financiar, nu un termen din lege.',fields,'Exemplu: 120.000 lei / 600.000 lei / 12 luni',outs,'Indicator orientativ: creanțe ÷ vânzări × zile. Termenele legale de recuperare (somație, executare, prescripție) sunt separate și le găsești în ghid.')
calc=calc.replace('<div class="row-btns">','<div class="row-btns">',1)
# add button row content is already in shell
js=r'''  function num(id){var v=($(id).value||'').replace(/[\s.]/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function calc(){
    var c=num('f-v'),v=num('f-d'),z=parseInt($('f-s').value,10),t=num('f-t');
    if(!(c>=0)||!(v>0)){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Introdu creanțele și vânzările.';$('o-m').textContent='—';$('o-r').textContent='—';return}
    var d=Math.round(c/v*z);
    $('o-t').textContent=d+' zile';cls('c-t','alert');$('o-ts').textContent='Creanțe ÷ vânzări × '+z+' de zile.';
    $('o-r').textContent=(Math.round(c/v*1000)/10).toString().replace('.',',')+'%';
    if(t>0){var i=d-t;$('o-m').textContent=(i>0?i+' zile':'0 zile');cls('c-m',i>0?'alert':'ok');$('o-ms').textContent=i>0?'Încasezi, în medie, peste termenul din contract.':'Încasezi în medie în termen.'}
    else{$('o-m').textContent='—';$('o-ms').textContent='Introdu termenul de plată din contract.'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-s','f-v','f-d','f-t'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-v').value='120000';$('f-d').value='600000';$('f-s').value='365';$('f-t').value='30';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Durata de recuperare a creanțelor: răspuns rapid</h2>
        <p>„Durata de recuperare” are două sensuri. Primul este un indicator financiar: în câte zile încasezi, în medie, facturile emise (DSO). Al doilea este durata procedurii de recuperare, care nu are o limită totală în lege, ci termene pe etape: executorul încuviințează executarea în 3 zile (art. 666 CPC), terțul poprit consemnează în 5 zile (art. 787), contestația se face în general în 15 zile (art. 715), iar dreptul de a cere executarea se prescrie în 3 ani (art. 706).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Creanțe de încasat de 120.000 lei, vânzări de 600.000 lei pe an. Durata medie de recuperare este 120.000 ÷ 600.000 × 365 = 73 de zile. Dacă termenul din contract este de 30 de zile, întârzierea medie este de 43 de zile.</p>
          <span class="formula">120.000 ÷ 600.000 × 365 = 73 de zile</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Indicator</span>
        <h2>Cum se calculează durata medie de recuperare</h2>
        <p>Formula obișnuită este: creanțe de încasat ÷ vânzări în perioadă × numărul de zile din perioadă. Rezultatul îți arată câte zile de vânzări ai blocate la clienți. Compară-l cu termenul de plată din contract: diferența este întârzierea medie.</p>
'''+F('formula-durata-de-recuperare')+'''
        <h3>Cum interpretezi rezultatul</h3>
        <ul class="chk">
          <li>O durată apropiată de termenul din contract înseamnă că încasezi, în medie, în termen.</li>
          <li>O durată mult mai mare înseamnă lichiditate blocată: clienți rău-platnici sau facturare întârziată.</li>
          <li>Urmărește indicatorul lunar, nu doar anual: mediile anuale ascund vârfurile.</li>
        </ul>
        <p>Valoarea „bună” depinde de domeniu și de termenele contractuale; nu există un prag legal.</p>'''
S3='''        <span class="eyebrow">Factori</span>
        <h2>Factorii care influențează recuperarea creanțelor</h2>
        <ul class="chk">
          <li><b>Clienții:</b> istoricul de plată și solvabilitatea.</li>
          <li><b>Contractele:</b> termene clare de plată, dobânzi pentru întârziere, un titlu executoriu acolo unde legea îl permite.</li>
          <li><b>Procedurile interne:</b> facturare la timp, urmărirea scadențelor, o somație imediat după scadență.</li>
          <li><b>Prescripția:</b> dreptul de a cere executarea se stinge în 3 ani, dacă debitorul o invocă (art. 706–707 CPC).</li>
        </ul>'''
S4='''        <span class="eyebrow">Amiabil</span>
        <h2>Recuperarea amiabilă a creanțelor</h2>
        <p>Amiabil înseamnă somație cu dovadă de primire, negociere și, dacă e nevoie, un plan de plată în scris. Este cea mai rapidă și mai ieftină cale, dar nu are forță coercitivă. Plata voluntară sau recunoașterea datoriei de către debitor întrerupe prescripția (art. 709 alin. 1 pct. 1 CPC). Externalizarea către o firmă de recuperare presupune cesiunea creanței sau un mandat; verifică autorizarea firmei. Vezi <a href="/societati-recuperare-creante/">societățile de recuperare creanțe</a>.</p>'''
S5='''        <span class="eyebrow">Juridic</span>
        <h2>Recuperarea juridică: termene și costuri</h2>
        <p>Dacă nu ai titlu executoriu, ai nevoie de o hotărâre sau de o ordonanță de plată (art. 1013 CPC), care cere o somație prealabilă. Cu titlu în mână, depui cererea la executor, care o încuviințează în 3 zile (art. 666). Poprirea produce efecte din ziua în care banca primește adresa, iar terțul consemnează în 5 zile (art. 787). Vânzarea unui imobil poate dura luni sau ani. Cheltuielile de executare sunt, de regulă, în sarcina debitorului (art. 670), dar le avansezi tu.</p>
'''+F('etapele-si-termenele-recuperarii')+'''
        <p>Perimarea: dacă lași 6 luni fără un act cerut în scris de executor, executarea se perimă (art. 697). Vezi <a href="/perimarea-executarii-silite/">perimarea executării silite</a> și <a href="/lege-recuperare-creante/">legea recuperării creanțelor</a>.</p>'''
S6='''        <span class="eyebrow">Reducere</span>
        <h2>Cum reduci durata de recuperare</h2>
        <ul class="chk">
          <li>Verifică clientul înainte de contract: istoric, garanții, avans.</li>
          <li>Pune în contract termene clare de plată și consecințele întârzierii.</li>
          <li>Trimite somația imediat după scadență, cu dovadă de primire.</li>
          <li>Urmărește scadențarul lunar și acționează înainte de prescripție.</li>
          <li>Când ai titlu executoriu, cere executarea fără întârziere.</li>
        </ul>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente în recuperarea creanțelor</h2>
        <ul class="chk">
          <li>Lipsa unui contract clar sau a dovezii livrării.</li>
          <li>Amânarea acțiunii până se apropie prescripția.</li>
          <li>Dependența de câțiva clienți rău-platnici.</li>
          <li>Executare începută, apoi lăsată fără acte 6 luni: riscul perimării.</li>
        </ul>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>'''
S8='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Calculează durata medie de recuperare și întârzierea față de contract.</li>
          <li>Listează facturile scadente peste 60 de zile și trimite somații cu dovadă de primire.</li>
          <li>Trimite-ne dosarul în chat; îți spunem în aceeași zi ce cale se potrivește.</li>
        </ol>
        <!--@author practice="recuperare creanțe" -->'''
faq=[("Ce este durata de recuperare a creanțelor?","Un indicator financiar (DSO): în câte zile încasezi, în medie, facturile emise. Se calculează ca creanțe ÷ vânzări × zile."),
("Cum se calculează perioada de încasare?","Împarți soldul creanțelor la vânzările din perioadă și înmulțești cu numărul de zile din perioadă."),
("Care este durata optimă de recuperare?","Nu există un prag legal. Compară-o cu termenul de plată din contract: o diferență mare indică întârzieri."),
("Ce înseamnă recuperarea amiabilă?","Somație, negociere și plan de plată în scris, fără proces. Este rapidă, dar nu are forță coercitivă."),
("Când este necesară executarea silită?","Când debitorul nu plătește după somație și ai un titlu executoriu; fără titlu, ai nevoie întâi de o hotărâre sau de o ordonanță de plată."),
("Cum pot reduce riscul de neplată?","Verifici clientul, ceri avans sau garanții, ai contracte clare și acționezi imediat după scadență."),
("Ce documente sunt necesare?","Contractul, facturile, dovada livrării sau a prestării, corespondența și dovada primirii somației."),
("Care sunt costurile recuperării juridice?","Taxe de timbru, onorariul executorului și al avocatului. Cheltuielile de executare sunt, de regulă, în sarcina debitorului, dar le avansezi tu (art. 670 CPC).")]
P=dict(slug='durata-de-recuperare-a-creantelor',crumb='Durata de recuperare a creanțelor',
 title='Durata de recuperare a creanțelor: calcul, termene legale',
 desc='Cum calculezi durata medie de recuperare a creanțelor (DSO), ce termene legale au etapele de recuperare (3 zile, 5 zile, 15 zile, 3 ani) și cum reduci întârzierile la încasare.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#calcul|Formula;#juridic|Termene legale;#reducere|Reducere;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='DSO · termen de încasare · termene legale',
  h1='Durata de recuperare a creanțelor: <span class="accent">calcul și termene de încasare</span>',
  lead=['Facturile sunt emise, banii nu vin, iar „în câte zile încasez” rămâne o presupunere. Aceeași expresie înseamnă două lucruri: un indicator al firmei și durata procedurii legale, iar amândouă merită calculate separat.',
        'Aici ai formula indicatorului, un calculator pentru întârzierea medie și termenele legale de la somație la executare, ca să știi în ce fază pierzi timp.'],
  meta2='Formula: creanțe ÷ vânzări × zile',cta='Calculează durata',
  answer='Durata medie de recuperare (DSO) se calculează ca creanțe de încasat ÷ vânzări în perioadă × numărul de zile. În procedura legală nu există o durată totală, ci termene pe etape: încuviințarea executării în 3 zile (art. 666 CPC), consemnarea de către terțul poprit în 5 zile (art. 787), contestația în general în 15 zile (art. 715) și prescripția executării în 3 ani (art. 706).',
  opts=[('DSO','creanțe ÷ vânzări × zile'),('Încuviințare','3 zile'),('Prescripție','3 ani')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('calcul','Cum se calculează',S2),('factori','Factori',S3),('amiabil','Amiabil',S4),('juridic','Recuperare juridică',S5),('reducere','Cum reduci durata',S6),('greseli','Greșeli',S7),('azi','Ce faci azi',S8)],
 faq=faq,faq_h2='Întrebări frecvente despre durata de recuperare a creanțelor',
 contact=dict(h2='Ai facturi neîncasate?',lead='Trimite-ne facturile scadente, contractul și datele clientului. Îți spunem în aceeași zi ce cale se potrivește și ce termene curg. Consultația nu te obligă la nimic.',nav='/|Acasă;/lege-recuperare-creante/|Legea recuperării;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum calculezi durata medie de recuperare',steps=[('Soldul creanțelor','Suma facturilor neîncasate la sfârșitul perioadei.'),('Vânzările din perioadă','Cifra de afaceri pe aceeași perioadă.'),('Aplici formula','Creanțe ÷ vânzări × zile.'),('Compari cu contractul','Diferența este întârzierea medie.'),('Acționezi','Somație imediată după scadență, apoi executare dacă ai titlu.')]),
 knows=['Recuperare creanțe','DSO','Executare silită','Prescripție'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/durata-de-recuperare-a-creantelor.src.html','w',encoding='utf-8').write(build(P))
