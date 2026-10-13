import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='cum-functioneaza-poprirea-bancara.webp'; IMG2='cum-contesti-poprirea-pe-cont.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Până când contești poprirea, <span class="accent">cu sărbători legale</span></h2></div>
      <p>Alege tipul popririi și data la care ai primit înștiințarea (sau la care s-a făcut prima reținere din venit). Calculatorul numără 15 zile libere, ca în art. 181 CPC, și mută termenul peste weekend și sărbători legale.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Poprirea ta</div>
          <div class="field full"><label for="f-s">Tipul popririi</label><div class="inp"><select id="f-s">
            <option value="0">Poprire pe cont bancar (am primit înștiințarea)</option>
            <option value="1">Poprire pe venituri periodice (salariu, pensie): prima reținere</option>
          </select></div></div>
          <div class="field full"><label for="f-d">Data primirii înștiințării sau a primei rețineri</label><div class="inp"><input type="date" id="f-d"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: 12 octombrie 2026</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Ultima zi utilă pentru contestație</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Completează data.</span></div>
            <div class="opt" id="c-c"><span class="k">Data + 16 zile</span><span class="v" id="o-c">—</span><span class="s" id="o-cs">Înainte de prelungire.</span></div>
            <div class="opt" id="c-r"><span class="k">Zile rămase</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Până la ultima zi utilă.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne adresa de poprire</a>
          <span class="disc">Calcul orientativ după art. 715 și art. 181 CPC. La poprirea pe venituri periodice, termenul începe cel mai târziu la prima reținere. Pentru poprirea ANAF se aplică Codul de procedură fiscală, cu termene proprii. Depune cu cel puțin o zi înainte.</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  var ZI=['duminică','luni','marți','miercuri','joi','vineri','sâmbătă'];
  function dt(s){var p=s.split('-');return new Date(Date.UTC(+p[0],+p[1]-1,+p[2]))}
  function fmt(d){return ('0'+d.getUTCDate()).slice(-2)+'.'+('0'+(d.getUTCMonth()+1)).slice(-2)+'.'+d.getUTCFullYear()}
  function key(d){return d.getUTCFullYear()+'-'+(d.getUTCMonth()+1)+'-'+d.getUTCDate()}
  function addD(d,n){var x=new Date(d.getTime());x.setUTCDate(x.getUTCDate()+n);return x}
  function easter(y){var a=y%4,b=y%7,c=y%19,d=(19*c+15)%30,e=(2*a+4*b-d+34)%7,m=Math.floor((d+e+114)/31),day=((d+e+114)%31)+1;return addD(new Date(Date.UTC(y,m-1,day)),13)}
  function hol(y){var s={},add=function(m,d){s[y+'-'+m+'-'+d]=1},E=easter(y);
    [[1,1],[1,2],[1,6],[1,7],[1,24],[5,1],[6,1],[8,15],[11,30],[12,1],[12,25],[12,26]].forEach(function(x){add(x[0],x[1])});
    [-2,0,1,49,50].forEach(function(n){s[key(addD(E,n))]=1});return s}
  function off(d){var w=d.getUTCDay();if(w===0||w===6)return true;return !!hol(d.getUTCFullYear())[key(d)]}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function calc(){
    var v=$('f-d').value;
    if(!v){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Completează data.';$('o-c').textContent='—';$('o-r').textContent='—';$('o-rs').textContent='Până la ultima zi utilă.';return}
    var s=dt(v),e=addD(s,16),raw=e,moved=[];
    while(off(e)){moved.push(fmt(e));e=addD(e,1)}
    $('o-c').textContent=fmt(raw)+' ('+ZI[raw.getUTCDay()]+')';
    $('o-cs').textContent=moved.length?'Zi nelucrătoare: termenul se prelungește.':'Zi lucrătoare: fără prelungire.';
    $('o-t').textContent=fmt(e)+' ('+ZI[e.getUTCDay()]+')';cls('c-t','alert');
    $('o-ts').textContent=moved.length?'Prelungit peste: '+moved.join(', ')+'.':'15 zile libere după '+fmt(s)+'.';
    var t=new Date();var today=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate()));
    var left=Math.round((e.getTime()-today.getTime())/864e5);
    if(0>left){$('o-r').textContent='Termen trecut';cls('c-r','alert');$('o-rs').textContent='Verifică dovada comunicării sau un act nou.'}
    else{$('o-r').textContent=left+' zile';cls('c-r',left<=3?'alert':'ok');$('o-rs').textContent=left<=3?'Depune cât mai repede.':'Până la ultima zi utilă.'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-s','f-d'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-s').value='0';$('f-d').value='2026-10-12';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Poprirea pe cont: răspuns rapid</h2>
        <p>Poprirea bancară este măsura prin care executorul judecătoresc indisponibilizează sumele din conturile debitorului: soldul existent și încasările viitoare. Se înființează fără somație, produce efecte din ziua în care banca primește adresa, iar debitorul are, de regulă, 15 zile să o conteste la instanța de executare.</p>
        <ul class="chk">
          <li><b>Când se blochează conturile:</b> din momentul comunicării adresei către bancă (art. 784 alin. 1 CPC).</li>
          <li><b>Cum se anulează:</b> prin contestație admisă, prin plata sau consemnarea integrală a datoriei ori prin renunțarea creditorului.</li>
        </ul>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Datorie de 20.000 lei, venit net de 4.000 lei. Plafonul de o treime este 1.333 lei pe lună, deci 20.000 ÷ 1.333 ≈ 15 luni. Dacă mai ai o poprire, totalul nu depășește jumătate din venit: 2.000 lei pe lună.</p>
          <span class="formula">20.000 ÷ (4.000 × 1/3) ≈ 15 luni</span>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este poprirea bancară și cine o poate înființa</h2>
        <p>Poprirea este o formă de executare silită prin care sunt urmărite sumele pe care o terță persoană (banca, angajatorul, un chiriaș) le datorează debitorului (art. 781 alin. 1 CPC). La conturi, pot fi poprite atât soldul creditor, cât și încasările viitoare, cu respectarea limitelor din art. 729 acolo unde se aplică (art. 781 alin. 2).</p>
        <h3>Creditorul și executorul judecătoresc</h3>
        <p>Poprirea se înființează la cererea creditorului, de un executor din circumscripția curții de apel unde ai domiciliul sau sediul ori unde banca are sediul principal sau secundar (art. 782). Dacă ai mai multe conturi, orice executor din locurile unde sunt deschise poate înființa poprirea pe toate. Condiția de bază este un titlu executoriu (art. 632).</p>
        <h3>ANAF și creditorii publici</h3>
        <p>Datoriile către bugetul de stat se execută prin organele fiscale, după Codul de procedură fiscală, nu prin executor judecătoresc. Termenele și căile de contestare diferă; nu aplica automat cele 15 zile din CPC. Dacă poprirea vine de la ANAF, verifică actul pe care se întemeiază și cere sfatul unui avocat înainte să depui ceva.</p>
        <h4>Exemple practice</h4>
        <div class="roles">
          <div><b>Bancă</b>Contract de credit scadent: executor din raza curții de apel, poprire pe toate conturile.</div>
          <div><b>Creditor cu hotărâre</b>Poprire pe salariu și pe contul în care îl primești.</div>
          <div><b>Pensie de întreținere</b>Terțul plătește direct creditorului suma reținută (art. 787 alin. 1 pct. 2).</div>
        </div>'''
S3='''        <span class="eyebrow">Etape</span>
        <h2>Cum se înființează poprirea, etapă cu etapă</h2>
        <ol class="num">
          <li><b>Încuviințarea executării</b> de către executor, în 3 zile, fără citare (art. 666).</li>
          <li><b>Adresa de înființare a popririi</b> către bancă, împreună cu încheierea de încuviințare; fără somație (art. 783 alin. 1).</li>
          <li><b>Indisponibilizarea:</b> sumele sunt blocate din momentul comunicării; banca nu poate face plăți care diminuează bunurile poprite (art. 784 alin. 1).</li>
          <li><b>Înștiințarea ta:</b> primești copia adresei, cu încheierea și titlul dacă nu ți-au fost comunicate (art. 783 alin. 1).</li>
          <li><b>Consemnarea:</b> banca consemnează suma în 5 zile de la comunicare (art. 787 alin. 1 pct. 1).</li>
          <li><b>Distribuirea:</b> executorul eliberează sau distribuie suma (art. 788, 864 și urm.).</li>
        </ol>
'''+fig(IMG1,'cum funcționează poprirea bancară: cerere, încuviințare în 3 zile, adresă către bancă, blocaj, consemnare în 5 zile','Cum funcționează poprirea bancară')+'''
        <h3>Rolul băncii</h3>
        <p>Banca este terț poprit. Trebuie să blocheze, să consemneze și să informeze executorul despre toate conturile. Dacă adresa a ajuns la o singură unitate, poprirea acoperă conturile de acolo, iar banca informează despre conturile de la alte unități (art. 783 alin. 5). Banca nu poate contesta poprirea; își formulează apărările în instanța de validare (art. 787 alin. 5). Sumele în valută pot fi convertite în lei, fără consimțământul tău, la cursul BNR (art. 784 alin. 7).</p>'''
S4='''        <span class="eyebrow">Comparație</span>
        <h2>Poprirea pe cont și pe salariu: diferențe</h2>
        <div class="tbl wide"><table>
          <thead><tr><th></th><th>Poprire pe cont</th><th>Poprire pe salariu</th><th>Urmărire imobiliară</th></tr></thead>
          <tbody>
            <tr><td>Procedura</td><td>Adresă către bancă</td><td>Adresă către angajator</td><td>Notare în cartea funciară, licitație</td></tr>
            <tr><td>Limite legale</td><td>Sold și încasări, cu limitele art. 729 unde se aplică</td><td>1/3 din venitul net; 1/2 la mai multe urmăriri</td><td>Valoarea nu poate fi vădit excesivă (art. 702)</td></tr>
            <tr><td>Contestare</td><td>15 zile (art. 715)</td><td>15 zile, cel târziu de la prima reținere</td><td>15 zile și, uneori, la judecătoria imobilului</td></tr>
            <tr><td>Avantaj creditor</td><td>Rapidă, fără somație</td><td>Reținere lunară sigură</td><td>Recuperează sume mari</td></tr>
            <tr><td>Risc debitor</td><td>Blocaj imediat</td><td>Venit redus ani de zile</td><td>Pierderea locuinței</td></tr>
          </tbody>
        </table></div>
        <p>Poprirea rămâne în ființă dacă îți schimbi locul de muncă sau ieși la pensie: noul plătitor primește actele (art. 786).</p>'''
S5='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile debitorului când ai contul poprit</h2>
        <h3>Sumele care nu pot fi poprite</h3>
        <ul class="chk">
          <li>Alocațiile de stat, indemnizațiile pentru copii, ajutoarele pentru îngrijirea copilului bolnav, ajutoarele de maternitate și de deces, bursele de studii și diurnele nu pot fi urmărite pentru niciun fel de datorii (art. 729 alin. 7).</li>
          <li>Ajutoarele pentru incapacitate temporară de muncă, compensațiile la desfacerea contractului și sumele cuvenite șomerilor se urmăresc doar pentru întreținere sau despăgubiri pentru daune corporale, și doar până la jumătate (art. 729 alin. 4–5).</li>
          <li>Veniturile sub salariul minim net se pot urmări doar peste jumătate din acest nivel (art. 729 alin. 3).</li>
        </ul>
        <p>Renunțarea la aceste protecții și orice urmărire care le încalcă sunt nule de drept (art. 730). Dacă banca a blocat și sume protejate, depune contestație și arată originea lor: extras de cont, decizie de plată, adeverință de la plătitor.</p>
        <h3>Verificarea legalității executării</h3>
        <p>Verifică: există titlu executoriu; creanța este certă, lichidă și exigibilă (art. 663); ți s-au comunicat încheierea și titlul; executorul este competent (art. 782); suma poprită nu depășește ce se datorează, cu accesoriile. Poprirea se face „în măsura necesară” realizării creanței (art. 783 alin. 2).</p>
        <h3>Prescripția executării</h3>
        <p>Dreptul de a cere executarea se prescrie în 3 ani, dacă legea nu prevede altfel (art. 706). Prescripția nu operează de drept: o invoci tu (art. 707 alin. 1). O poprire valabilă întrerupe prescripția pentru creanța poprită și pentru cea pentru care a fost înființată (art. 784 alin. 5). Perimarea, după 6 luni de inactivitate din vina creditorului, este un alt mod de a stinge executarea (art. 697).</p>'''
S6='''        <span class="eyebrow">Contestație</span>
        <h2>Contestația la executare: cum anulezi poprirea</h2>
        <h3>Când poate fi contestată poprirea</h3>
        <ul class="chk">
          <li>Titlul nu este executoriu sau creanța nu e certă, lichidă, exigibilă.</li>
          <li>Dreptul de a cere executarea s-a prescris.</li>
          <li>Executorul nu era competent sau actele nu ți-au fost comunicate (nulitate: art. 667 alin. 2, art. 704).</li>
          <li>Se poprește un venit sau o sumă nepopribilă (art. 729).</li>
          <li>Suma poprită depășește datoria.</li>
        </ul>
        <p>Nu poți invoca în contestație motive pe care le puteai ridica în procesul care a dus la hotărârea executată (art. 713 alin. 1).</p>
        <h3>Termenul</h3>
        <p>15 zile de la comunicarea sau înștiințarea privind înființarea popririi. La poprirea pe venituri periodice, termenul începe cel mai târziu la prima reținere (art. 715 alin. 1 pct. 2). Calculul se face pe zile libere: ultima zi este data primirii plus 16 zile, mutată în prima zi lucrătoare dacă cade în weekend sau sărbătoare (art. 181 CPC). Vezi și <a href="/termen-contestatie-la-executare/">termenul contestației la executare</a>.</p>
        <h3>Actele necesare</h3>
        <p>Contestația, încheierea de încuviințare, adresa de poprire, extrasele de cont, dovada sumelor protejate, procura avocatului și taxa de timbru (cel mult 1.000 lei). O depui la instanța de executare (<a href="/unde-se-depune-contestatia-la-executare/">unde se depune</a>).</p>
        <h3>Suspendarea executării</h3>
        <p>Poți cere instanței suspendarea, cu cauțiune (art. 719): 10% până la 10.000 lei, apoi 1.000 lei + 5% din ce depășește 10.000 lei. Suspendarea simplă nu ridică singură poprirea (art. 701 alin. 3); cere expres ridicarea blocajului. Detalii în <a href="/amanare-executare-silita/">amânarea și suspendarea executării</a>.</p>
'''+fig(IMG2,'cum contești poprirea pe cont: 15 zile, contestație la instanța de executare, suspendare cu cauțiune, consemnare pentru ridicare','Cum contești poprirea pe cont')
S7='''        <span class="eyebrow">Ridicare</span>
        <h2>Cum ridici poprirea fără contestație</h2>
        <ul class="chk">
          <li><b>Consemnezi toată datoria</b> la dispoziția executorului: creanța, accesoriile și cheltuielile (art. 721 și art. 784 alin. 6). Depui recipisa la executor, care înștiințează banca de îndată.</li>
          <li><b>Lipsa titlului executoriu:</b> dacă titlul e desființat sau nu e executoriu, ceri anularea executării.</li>
          <li><b>Datorie prescrisă:</b> invoci prescripția printr-o contestație (art. 707).</li>
          <li><b>Eroarea executorului:</b> suma, contul sau persoana greșită se corectează printr-o contestație la actul respectiv.</li>
          <li><b>Înțelegere cu creditorul:</b> creditorul poate renunța la executare, iar executarea încetează (art. 703 alin. 1 pct. 3).</li>
        </ul>
        <p>Dacă contestația se admite, instanța anulează actul sau executarea (art. 720 alin. 1), iar sumele se restituie prin întoarcerea executării (art. 723).</p>
        <h3>Validarea popririi, când terțul nu își face datoria</h3>
        <p>Dacă banca sau angajatorul nu consemnează suma, creditorul, debitorul sau executorul poate sesiza instanța de executare pentru validarea popririi, în cel mult o lună de la data când terțul trebuia să consemneze (art. 790 alin. 1). Hotărârea se atacă doar cu apel, în 5 zile de la comunicare (art. 791).</p>'''
S8='''        <span class="eyebrow">ANAF</span>
        <h2>Poprirea ANAF versus poprirea clasică</h2>
        <p>La ANAF, creditorul public are propriul titlu (de pildă decizia de impunere) și nu are nevoie de executor judecătoresc, iar contestarea urmează Codul de procedură fiscală. În poprirea clasică, executorul acționează după CPC. Diferențele de termen sunt frecvente, deci verifică separat la ce procedură te încadrezi.</p>'''
S9='''        <span class="eyebrow">Practică</span>
        <h2>Greșeli frecvente când ai contul blocat</h2>
        <ul class="chk">
          <li><b>Ignori actele:</b> primești adresa și aștepți; cele 15 zile trec.</li>
          <li><b>Plătești fără calcul:</b> achiți ce ți se cere fără să verifici dobânzile și cheltuielile.</li>
          <li><b>Muți banii în alt cont:</b> nu ajută; creditorul poate cere poprirea pe toate conturile (art. 782 alin. 2), iar plata sau cesiunea creanței poprite nu îi este opozabilă (art. 784 alin. 4).</li>
          <li><b>Contești prea târziu:</b> contestația se respinge ca tardivă.</li>
          <li><b>Nu arăți originea sumelor</b> din cont: banca nu poate ghici ce e nepopribil.</li>
        </ul>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată. Când în cont sunt amestecate salariul și alte încasări, banca și executorul nu pot ști ce e protejat; de aceea dovada originii sumelor cântărește mult.</p>'''
S10='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi dacă ai contul blocat</h2>
        <ol class="num">
          <li>Cere băncii și executorului copia adresei de poprire și notează data primirii.</li>
          <li>Strânge extrasul de cont și dovezile pentru sumele nepopribile (salariu, alocații, indemnizații).</li>
          <li>Trimite-ne totul în chat; îți spunem în aceeași zi dacă să contești, să ceri suspendarea sau să consemnezi.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Ce este poprirea bancară?","Măsura prin care executorul indisponibilizează sumele din conturile debitorului, soldul și încasările viitoare (art. 781 alin. 2 CPC)."),
("Cine poate pune poprire pe cont?","Un executor judecătoresc, la cererea creditorului care are un titlu executoriu, sau organele fiscale pentru datoriile către buget."),
("Cât din salariu poate fi poprit?","Maximum o treime din venitul net pentru datorii obișnuite, maximum jumătate dacă sunt mai multe urmăriri (art. 729 alin. 1–2)."),
("Cum contest poprirea bancară?","Prin contestație la executare, la instanța de executare, în 15 zile de la comunicarea sau înștiințarea despre poprire (art. 712, 715)."),
("Pot suspenda executarea silită?","Da, instanța o poate suspenda pentru motive temeinice, în schimbul unei cauțiuni (art. 719)."),
("Când poate fi anulată poprirea?","Când titlul nu e executoriu, datoria e prescrisă, executorul e necompetent, actele nu ți-au fost comunicate sau se poprește peste limita legii."),
("Ce venituri nu pot fi poprite?","Alocațiile de stat, indemnizațiile pentru copii, ajutoarele de maternitate și de deces, bursele și diurnele (art. 729 alin. 7)."),
("Cum verific dacă executarea este legală?","Cere dosarul de executare și verifică titlul, comunicarea actelor, competența executorului, calculul sumei și respectarea plafoanelor.")]
P=dict(slug='poprire-cont',crumb='Poprire cont bancar',
 title='Poprire cont bancar: contestație, anulare, ridicare',
 desc='Ce este poprirea pe cont, cine o poate înființa, cât se poate reține din salariu, ce sume sunt nepopribile și cum o contești în 15 zile sau o ridici prin consemnare.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#etape|Etape;#contestatie|Contestație;#ridicare|Ridicare;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Poprire cont · art. 781–790 CPC · contestație în 15 zile',
  h1='Poprirea pe cont bancar și <span class="accent">contestația la executare silită</span>',
  lead=['Încerci să plătești la magazin și cardul e respins. În aplicație vezi „cont indisponibilizat”, iar în cutia poștală nu e nicio somație. Nu e o eroare: poprirea se înființează fără somație. De aici încep 15 zile în care poți încă schimba rezultatul.',
        'Aici afli ce poate bloca executorul, ce nu poate, cum contești și cum ridici poprirea, plus un calculator pentru ultima zi de contestație.'],
  meta2='Ultima zi = data + 16 zile',cta='Calculează ultima zi',
  answer='Poprirea bancară este măsura prin care executorul indisponibilizează sumele din conturile debitorului: soldul existent și încasările viitoare. Se înființează fără somație, produce efecte din ziua în care banca primește adresa, iar debitorul are, de regulă, 15 zile să o conteste la instanța de executare (art. 715 CPC).',
  opts=[('Blocaj','din comunicare'),('Contestație','15 zile libere'),('Ridicare','consemnare (art. 721)')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('etape','Etape',S3),('comparatie','Cont vs salariu',S4),('drepturi','Drepturile debitorului',S5),('contestatie','Contestația',S6),('ridicare','Ridicare',S7),('anaf','ANAF',S8),('practica','Greșeli',S9),('azi','Ce faci azi',S10)],
 faq=faq,faq_h2='Întrebări frecvente despre poprirea bancară',
 contact=dict(h2='Ai contul blocat?',lead='Trimite-ne adresa de poprire și extrasul de cont. Îți spunem în aceeași zi dacă poți contesta, cere suspendarea sau ridica poprirea prin consemnare. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum contești o poprire pe cont',steps=[('Ceri adresa de poprire','Notezi data primirii; de aici curge termenul.'),('Strângi dovezile','Extras de cont și dovada sumelor protejate.'),('Depui contestația','La instanța de executare, în 15 zile libere.'),('Ceri suspendarea','Cu cauțiune și cu ridicarea expresă a blocajului.'),('Sau consemnezi datoria','Poprirea se ridică la depunerea recipisei.')]),
 knows=['Poprire','Poprire cont bancar','Executare silită','Contestație la executare','Cod procedură civilă'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/poprire-cont.src.html','w',encoding='utf-8').write(build(P))
