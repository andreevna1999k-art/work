import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='procese-cu-bancile-ce-poti-obtine.webp'; IMG2='pasii-unui-proces-impotriva-bancii.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Cât poți recupera dintr-un comision și <span class="accent">ce rămâne sub semnul prescripției</span></h2></div>
      <p>Un proces „câștigat” poate însemna sume diferite. Introdu comisionul lunar și câte luni l-ai plătit. Vezi totalul plătit, ce intră în ultimii 3 ani și ce parte depinde de momentul de început al prescripției.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Comisionul tău</div>
          <div class="field"><label for="f-s">Sold mediu (lei)</label><div class="inp"><input id="f-s" inputmode="numeric" placeholder="100000"></div></div>
          <div class="field"><label for="f-c">Comision lunar din sold (%)</label><div class="inp"><input id="f-c" inputmode="decimal" placeholder="0,2"></div></div>
          <div class="field"><label for="f-l">Luni în care ai plătit comisionul</label><div class="inp"><input id="f-l" inputmode="numeric" placeholder="120"></div></div>
          <div class="field"><label for="f-a">Perioada de restituire (ani)</label><div class="inp"><select id="f-a"><option value="3" selected>3 ani (prescripția generală)</option><option value="2">2 ani</option><option value="5">5 ani</option><option value="10">Tot ce am plătit</option></select></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: 100.000 lei, 0,2%, 120 luni</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Total plătit cu titlu de comision</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Completați soldul, comisionul și lunile.</span></div>
            <div class="opt" id="c-r"><span class="k">Restituire în perioada aleasă</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Dacă instanța admite cererea.</span></div>
            <div class="opt alert" id="c-d"><span class="k">Rămâne în discuție</span><span class="v" id="o-d">—</span><span class="s" id="o-ds">Depinde de începutul prescripției.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne contractul spre analiză</a>
          <span class="disc">Calcul orientativ, pe un sold constant. Existența comisionului abuziv se stabilește după analiza contractului. Prescripția generală este de 3 ani (art. 2517 Cod civil), iar momentul de început al restituirii îl stabilești cu avocatul. Un „proces câștigat” poate fi și parțial.</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  function lei(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/\s/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function calc(){
    var s=num('f-s'),c=num('f-c'),l=num('f-l'),a=parseInt($('f-a').value,10);
    if(s>0&&c>0&&l>0){
      var m=s*c/100,t=m*l,lim=a>=10?l:Math.min(l,a*12),r=m*lim,d=t-r;
      $('o-t').textContent=lei(t);$('o-ts').textContent=lei(m)+' pe lună × '+l+' luni.';
      $('o-r').textContent=lei(r);$('o-rs').textContent='Ultimele '+lim+' luni plătite.';
      $('o-d').textContent=lei(d);$('o-ds').textContent=d>0?'Depinde de momentul de la care curge prescripția.':'Nimic în afara perioadei alese.';
    }else{$('o-t').textContent='—';$('o-ts').textContent='Completați soldul, comisionul și lunile.';$('o-r').textContent='—';$('o-rs').textContent='Dacă instanța admite cererea.';$('o-d').textContent='—';$('o-ds').textContent='Depinde de începutul prescripției.'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-s','f-c','f-l','f-a'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-s').value='100000';$('f-c').value='0,2';$('f-l').value='120';$('f-a').value='3';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Avocați care au câștigat procese cu băncile: răspuns rapid</h2>
        <p>Da, consumatorii câștigă procese cu băncile în România. Cele mai multe privesc clauze abuzive, comisioane, riscul valutar la creditele în franci elvețieni și executări silite nelegale. Succesul depinde de contract, de probe și de termene. Nu depinde de numele băncii. Nici de câte procese spune avocatul că a câștigat.</p>'''
S2='''        <span class="eyebrow">Tipuri de procese</span>
        <h2>Ce tipuri de procese cu băncile pot fi câștigate</h2>
        <p>Patru tipuri de litigii bancare ajung frecvent la o soluție favorabilă consumatorului. Primul: clauzele abuzive privind dobânda și comisioanele. Al doilea: contestația la executare silită. Al treilea: acțiunile privind contractul de credit, inclusiv riscul valutar. Al patrulea: darea în plată. Fiecare are alte probe, alte termene și alt rezultat posibil.</p>
        <h3>Clauze abuzive: dobânzi și comisioane</h3>
        <p>Se contestă des comisionul de administrare lunar, „comisionul de risc” și dobânda variabilă stabilită discreționar de bancă. Ce obții: constatarea caracterului abuziv, recalcularea ratelor și restituirea sumelor plătite. Detalii despre fiecare clauză găsești la <a href="/avocat-clauze-abuzive/">avocat clauze abuzive</a>.</p>
        <h3>Executare silită: suspendare și anulare</h3>
        <p>Dacă banca sau un recuperator a pornit executarea, contestația la executare (art. 712 Cod de procedură civilă) poate duce la anularea actelor sau la reducerea sumei. Termenul general este de 15 zile (art. 715 CPC). Poți cere și suspendarea executării (art. 719 CPC), de regulă cu plata unei cauțiuni. Pașii sunt la <a href="/contestatie-la-executare/">contestație la executare</a>.</p>
        <h3>Contracte de credit: nulitate și risc valutar</h3>
        <p>Nulitatea întregului contract se obține rar. Mai des, instanța elimină o clauză și menține creditul. La creditele în CHF, discuția e despre informarea privind riscul de curs.</p>
        <h4>Procese colective</h4>
        <p>ANPC și asociațiile de consumatori pot cere instanței încetarea folosirii unei clauze abuzive în contractele standard (Legea nr. 193/2000). Există și acțiuni în reprezentare a consumatorilor, în condițiile legii. Dacă ai executare sau cesiune, ai nevoie de dosar individual.</p>'''
S3='''        <span class="eyebrow">Exemple</span>
        <h2>Exemple reale de procese câștigate cu băncile</h2>
        <p>Cele mai solide exemple publice sunt hotărârile Curții de Justiție a Uniunii Europene. Ele au pornit din procese ale unor consumatori și obligă instanțele române. Hotărârile românești concrete trebuie verificate pe ReJust, cu număr și dată. Restul sunt situații tipice, descrise anonimizat, fără rezultate inventate.</p>
        <h3>Cazuri concrete</h3>
        <p><strong>Hotărâri CJUE (publice):</strong></p>
        <ul class="chk">
          <li><strong>C-26/13 Kásler (2014).</strong> Credit în valută, cu cursuri diferite la acordare și la plată. Clauza trebuie să-i permită consumatorului să înțeleagă consecințele economice, nu doar textul.</li>
          <li><strong>C-143/13 Matei (2015).</strong> Credit Volksbank România cu „comision de risc”. Instanța națională verifică dacă acesta ține de obiectul principal și dacă e redactat clar.</li>
          <li><strong>C-186/16 Andriciuc (20 septembrie 2017).</strong> Credite în CHF din România. Banca trebuie să informeze consumatorul asupra riscului de curs, ca să poată decide prudent.</li>
          <li><strong>C-154/15 Gutiérrez Naranjo (2016).</strong> Restituirea sumelor plătite în baza unei clauze abuzive nu poate fi limitată doar la plățile făcute după o anumită dată.</li>
          <li><strong>C-698/18 și C-699/18 Raiffeisen Bank și BRD (9 iulie 2020).</strong> Acțiunea de constatare a caracterului abuziv este imprescriptibilă. Restituirea poate fi supusă prescripției, dar termenul curge de când ai cunoscut sau trebuia să cunoști caracterul abuziv.</li>
        </ul>
        <p><strong>Hotărâri ale instanțelor române:</strong> le cauți pe portal.just.ro sau pe ReJust, după număr de dosar și instanță. Vezi mai jos cum verifici o hotărâre invocată de un avocat.</p>
        <p><strong>Situații tipice (anonimizate):</strong></p>
        <div class="roles">
          <div><b>Comision de administrare lunar</b>Clientul nu primea niciun serviciu distinct pentru comision. Proba centrală: contractul și extrasele cu sumele încasate.</div>
          <div><b>Dobândă „în funcție de politica băncii”</b>Clauza nu numea un indice verificabil. Discuția: claritatea clauzei și dezechilibrul produs.</div>
          <div><b>Poprire după cesiune</b>Recuperatorul executa o sumă mai mare decât debitul. Avocatul verifică titlul, notificarea cesiunii și calculul.</div>
        </div>
        <h3>Rezultate obținute</h3>
        <div class="tbl wide"><table>
          <thead><tr><th>Tip litigiu</th><th>Ce ceri instanței</th><th>Ce poți obține</th><th>Proba-cheie</th></tr></thead>
          <tbody>
            <tr><td>Clauze abuzive</td><td>Constatarea caracterului abuziv</td><td>Eliminarea clauzei, recalcularea ratelor, restituirea sumelor</td><td>Contractul, actele adiționale, extrasele</td></tr>
            <tr><td>Credit în CHF</td><td>Analiza clauzei de risc valutar</td><td>Depinde de informarea primită la semnare</td><td>Documentele precontractuale</td></tr>
            <tr><td>Executare silită</td><td>Contestație și suspendare</td><td>Anularea actelor, reducerea sumei</td><td>Actele executorului, titlul, cesiunea</td></tr>
            <tr><td>Dare în plată</td><td>Stingerea datoriei prin transferul imobilului</td><td>Liberarea de datoria garantată, în condițiile Legii nr. 77/2016</td><td>Notificarea, contractul de ipotecă</td></tr>
          </tbody>
        </table></div>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Comision lunar de 0,2% din sold. La un sold mediu de 100.000 lei, plătești 200 lei pe lună. În 10 ani (120 de luni), ai plătit 24.000 lei.</p>
          <p>Dacă instanța acordă restituirea doar pentru ultimii 3 ani, primești 36 × 200 = 7.200 lei. Restul de 16.800 lei depinde de momentul de început al prescripției. Ambele variante pot fi numite „proces câștigat”.</p>
          <span class="formula">100.000 × 0,2% = 200 lei/lună · 200 × 120 = 24.000 lei · 200 × 36 = 7.200 lei · 24.000 − 7.200 = 16.800 lei</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>
        <h4>Ce a contat în câștig</h4>
        <p>În dosarele favorabile apar aceleași patru elemente. Contractul complet, cu actele adiționale. Dovada plăților. Un calcul clar al sumelor. Un obiect precis al cererii. Dosarele se pierd mai des din cereri vagi decât din lipsă de drept.</p>
'''+fig(IMG1,'avocați care au câștigat procese cu băncile: tipuri de litigii bancare și rezultate','Procese cu băncile: ce poți obține')
S4='''        <span class="eyebrow">Șanse</span>
        <h2>Statistici și șanse de câștig în litigii bancare</h2>
        <p>Nu există o statistică oficială publică privind procentul de procese câștigate împotriva băncilor. Orice procent afișat pe un site de avocatură este o estimare internă, greu de verificat. Șansele reale se stabilesc după citirea contractului, a probelor și a termenelor.</p>
        <h3>Factori care influențează șansele</h3>
        <ul class="chk">
          <li><strong>Tipul cazului:</strong> clauzele abuzive, executarea și restituirea au reguli diferite.</li>
          <li><strong>Documentele:</strong> fără contract și extrase, dosarul pornește slab.</li>
          <li><strong>Termenele:</strong> 15 zile la contestația la executare, 3 ani la restituire (art. 2517 Cod civil).</li>
          <li><strong>Claritatea clauzei:</strong> o clauză clară privind prețul sau moneda e greu de atacat.</li>
        </ul>
        <h3>Estimare șanse reale</h3>
        <p>Un avocat serios îți dă o evaluare argumentată, nu un procent. Îți spune ce clauză atacă, pe ce temei și ce riscuri vede. Îți spune ce se întâmplă dacă pierzi: poți plăti cheltuielile de judecată ale băncii (art. 453 CPC). Un procent dat la telefon, înainte să vadă actele, e un semnal de alarmă.</p>
        <h4>Mituri vs realitate</h4>
        <div class="roles">
          <div><b>„Dacă am semnat, nu mai pot face nimic.”</b>Fals. Semnătura nu validează o clauză abuzivă.</div>
          <div><b>„Câștigat înseamnă că nu mai datorez nimic.”</b>Fals. De obicei se elimină o clauză, iar creditul rămâne.</div>
          <div><b>„Un avocat bun garantează rezultatul.”</b>Fals. Garanția de succes e un semnal de alarmă.</div>
        </div>'''
S5='''        <span class="eyebrow">Rolul avocatului</span>
        <h2>Cum te ajută un avocat să câștigi procesul</h2>
        <p>Avocatul transformă o nemulțumire într-o cerere de chemare în judecată bine construită. Citește contractul, identifică clauza atacabilă și calculează sumele. Alege calea: reclamație, CSALB, instanță sau contestație la executare. Apoi răspunde apărărilor băncii. Într-un litigiu bancar, calculul contează cât temeiul de drept.</p>
        <h3>Analiza juridică</h3>
        <p>Avocatul verifică contractul, actele adiționale, graficul de rambursare, notificările și extrasele. Rezultatul: o listă de clauze atacabile, cu temei, sumă și risc pentru fiecare.</p>
        <h3>Strategie procesuală</h3>
        <p>Strategia stabilește ce ceri și în ce ordine. Constatarea caracterului abuziv e imprescriptibilă. Restituirea se poate prescrie. De aceea, cererile se formulează separat și clar. Dacă banca a pornit executarea, contestația are prioritate din cauza termenului de 15 zile.</p>
        <h4>Reprezentare în instanță</h4>
        <p>Avocatul răspunde la întâmpinarea băncii, cere expertiza contabilă când e nevoie și invocă jurisprudența CJUE aplicabilă. Pentru o privire de ansamblu asupra serviciilor, vezi <a href="/avocat-specializat-credite-bancare/">avocat specializat în credite bancare</a>.</p>'''
S6='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura unui proces cu banca pas cu pas</h2>
        <p>Un litigiu bancar are patru etape: evaluarea cazului, pregătirea dosarului, judecata în primă instanță și calea de atac. Înainte de instanță, poți încerca o reclamație la bancă sau o procedură la CSALB. Primul pas este întotdeauna strângerea actelor. Fără contract și extrase, nimeni nu îți poate evalua corect șansele.</p>
        <h3>Evaluarea cazului</h3>
        <p>La consultație aduci contractul, actele adiționale și extrasele. Avocatul îți spune dacă merită o reclamație la bancă sau o procedură la CSALB, care este, de regulă, fără costuri pentru consumator. ANPC poate face controale. BNR supraveghează băncile, dar nu soluționează litigii individuale.</p>
        <h3>Pregătirea dosarului</h3>
        <p>Se ordonează actele, se calculează sumele și se redactează cererea. În anumite cazuri, acțiunile consumatorilor beneficiază de scutiri de taxă judiciară de timbru; întreabă ce taxe se plătesc în cazul tău.</p>
        <h3>Judecata</h3>
        <p>Competența se stabilește după valoare: judecătoria judecă cererile evaluabile în bani de până la 200.000 lei și pe cele neevaluabile în bani, iar tribunalul pe cele peste acest prag (art. 94–95 CPC). Banca depune întâmpinare, apoi urmează probele și hotărârea.</p>
        <h4>Hotărârea finală</h4>
        <p>Instanța poate admite cererea total, în parte sau o poate respinge. Hotărârea primei instanțe se atacă de regulă cu apel. Devine definitivă după judecarea apelului sau dacă nimeni nu a declarat apel în termen. Abia o hotărâre definitivă închide discuția. „Admite în parte” înseamnă câștig parțial.</p>
'''+fig(IMG2,'etapele unui proces împotriva băncii, de la consultație la hotărârea definitivă','Pașii unui proces împotriva băncii')
S7='''        <span class="eyebrow">Practică</span>
        <h2>Practica judiciară relevantă</h2>
        <p>Practica în litigiile bancare se sprijină pe jurisprudența CJUE: transparența (Kásler), riscul valutar (Andriciuc), restituirea integrală (Gutiérrez Naranjo) și prescripția (C-698/18). Instanțele române aplică aceste criterii de la caz la caz. Hotărârile lor sunt publice, dar anonimizate. Le poți verifica pe ReJust și pe portal.just.ro.</p>
        <h3>Cum verifici o hotărâre invocată de avocat</h3>
        <ul class="chk">
          <li><strong>portal.just.ro:</strong> cauți după numărul dosarului și instanță. Vezi părțile, termenele, soluția pe scurt și dacă s-a declarat apel.</li>
          <li><strong>ReJust (rejust.ro):</strong> găsești textul hotărârii, anonimizat. Numele avocaților și ale clienților nu apar, deci ceri numărul dosarului.</li>
          <li><strong>Verifici trei lucruri:</strong> e definitivă sau nedefinitivă, admisă total sau în parte, ce sumă s-a dispus efectiv.</li>
        </ul>
        <h3>Tendințe juridice</h3>
        <p>Tendința principală e testul transparenței: ce putea înțelege consumatorul la semnare, nu doar ce scria în contract. A doua tendință privește prescripția restituirii și momentul de la care curge. Instanțele interne îl apreciază diferit, deci îl stabilești cu avocatul, pe cazul tău.</p>
        <h4>Interpretări legale</h4>
        <p>Clauzele privind obiectul principal, adică prețul și moneda, pot fi analizate doar dacă nu sunt redactate clar și inteligibil. Eliminarea unei clauze nu anulează obligația de a rambursa capitalul. Asta explică de ce majoritatea câștigurilor sunt parțiale.</p>'''
S8='''        <span class="eyebrow">Legislație</span>
        <h2>Legislație aplicabilă în litigii bancare</h2>
        <p>Cinci acte normative acoperă majoritatea litigiilor bancare. Legea nr. 193/2000 pentru clauzele abuzive. OUG nr. 50/2010 pentru creditele de consum și OUG nr. 52/2016 pentru creditele imobiliare. Codul de procedură civilă pentru executare. Legea nr. 77/2016 pentru darea în plată. Peste ele se aplică Directiva 93/13/CEE și jurisprudența CJUE.</p>
        <h3>Drept financiar bancar</h3>
        <p>OUG nr. 50/2010 cere ca dobânda variabilă să fie legată de indici de referință verificabili. OUG nr. 52/2016 reglementează creditele imobiliare încheiate după intrarea ei în vigoare.</p>
        <h3>Protecția consumatorului</h3>
        <p>Legea nr. 193/2000 definește clauza abuzivă și are în anexă o listă exemplificativă. Codul civil fixează prescripția generală de 3 ani (art. 2517). Constatarea nulității absolute e imprescriptibilă. Pentru datorii multiple, există și insolvența persoanei fizice (Legea nr. 151/2015); vezi <a href="/calculator-insolventa/">calculator insolvență</a>.</p>
        <h4>Comparație între norme</h4>
        <div class="tbl"><table>
          <thead><tr><th>Problema</th><th>Actul aplicabil</th><th>Ce verifici</th></tr></thead>
          <tbody>
            <tr><td>Clauză neclară sau dezechilibrată</td><td>Legea nr. 193/2000</td><td>Negocierea, claritatea, dezechilibrul</td></tr>
            <tr><td>Dobândă, costuri, informare</td><td>OUG nr. 50/2010, OUG nr. 52/2016</td><td>Indicele, formula, documentele precontractuale</td></tr>
            <tr><td>Poprire, executare</td><td>Codul de procedură civilă</td><td>Titlul, termenul de 15 zile, suma</td></tr>
            <tr><td>Imobil ipotecat</td><td>Legea nr. 77/2016</td><td>Condițiile dării în plată</td></tr>
          </tbody>
        </table></div>'''
S9='''        <span class="eyebrow">Durată și cost</span>
        <h2>Cât durează și cât costă un proces cu banca</h2>
        <p>Durata depinde de instanță, de expertiză și de apel. Contestația la executare e, de regulă, mai rapidă decât acțiunea pentru clauze abuzive. Prima instanță plus apelul pot trece de un an. Costul include onorariul avocatului, eventual expertiza și riscul cheltuielilor de judecată.</p>
        <h3>Durata procesului</h3>
        <p>Dosarul se lungește din cauza expertizei, a amânărilor și a apelului. Nimeni nu poate garanta o durată fixă. Cere un calendar al etapelor.</p>
        <h3>Costuri avocat</h3>
        <p>Onorariul se stabilește prin contract de asistență juridică (Legea nr. 51/1995). Statutul profesiei interzice pactul de quota litis, adică un onorariu stabilit integral în funcție de rezultat; un onorariu de succes poate fi convenit doar în limitele Statutului. Dacă pierzi, poți fi obligat la cheltuielile de judecată ale băncii.</p>
        <h4>Factori care influențează costul</h4>
        <p>Vechimea contractului, numărul de clauze atacate, executarea în curs și nevoia de expertiză.</p>'''
S10='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente în procesele cu băncile</h2>
        <p>Cele mai multe procese bancare se pierd din trei motive. Lipsesc actele care dovedesc plățile sau clauza. Clientul alege un avocat după promisiuni, nu după metodă. Sau semnează sub presiune documente care îi schimbă poziția juridică. Toate trei pot fi evitate înainte de primul termen.</p>
        <h3>Lipsa dovezilor</h3>
        <p>Fără contract și extrase, cererea e greu de dovedit. Păstrează notificările și actele executorului. În instanță, ce nu e scris nu există.</p>
        <h3>Alegerea greșită a avocatului</h3>
        <p>Riscul major e avocatul care promite „câștig garantat” sau un procent de succes înainte să vadă actele. La fel, cel care cere tot onorariul doar „la succes”. Verifică întâi că e înscris în Tabloul avocaților, pe site-ul baroului sau al UNBR.</p>
        <h4>Decizii emoționale</h4>
        <p>Nu semna o reeșalonare sau o recunoaștere de datorie înainte de analiză. Uneori conține renunțări la drepturi. Vezi și <a href="/restructurare-credit-vs-refinantare/">restructurare credit</a>.</p>'''
S11='''        <span class="eyebrow">Alegerea</span>
        <h2>Cum alegi un avocat care câștigă procese cu băncile</h2>
        <p>Alegi după ce poți verifica, nu după ce ți se promite. Avocatul trebuie să fie înscris în Tabloul avocaților. Trebuie să-ți poată arăta hotărâri anonimizate din litigii bancare, cu număr de dosar. Și trebuie să-ți explice riscurile în scris. Un număr mare de „procese câștigate”, fără dosare, nu dovedește nimic.</p>
        <h3>Criterii importante</h3>
        <ul class="chk">
          <li><strong>Experiență în litigii bancare:</strong> clauze abuzive, executare, cesiune, CHF.</li>
          <li><strong>Cazuri câștigate verificabile:</strong> numere de dosar pe care le cauți pe portal.just.ro.</li>
          <li><strong>Claritate:</strong> îți explică problema în cuvinte simple, cu temeiul de drept.</li>
        </ul>
        <h3>Semne de încredere</h3>
        <p>Îți spune ce acte lipsesc și ce risc există. Îți dă contract scris, cu onorariul clar. Nu promite procente. Diferențiază câștigul definitiv de cel nedefinitiv și câștigul total de cel parțial.</p>
        <div class="note dark"><b>Poziția juridică.</b> Întrebarea „câte procese ați câștigat?” e mai puțin utilă decât „îmi arătați două hotărâri definitive, cu număr de dosar?”. Un câștig se măsoară în suma încasată efectiv de client, nu în soluția de la prima instanță. Restul e marketing.</div>
        <h4>Întrebări de pus avocatului</h4>
        <ol class="num">
          <li>Ce clauză atacăm și pe ce temei?</li>
          <li>Ce termen de prescripție riscăm?</li>
          <li>Puteți să-mi dați numere de dosar din litigii similare?</li>
          <li>Hotărârile sunt definitive? Admise total sau în parte?</li>
          <li>Cât mă costă dacă pierd?</li>
        </ol>'''
S12='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Cere băncii, în scris, copia contractului, a actelor adiționale și istoricul plăților.</li>
          <li>Marchează în contract fiecare comision și formula dobânzii. Adună sumele plătite din extrase.</li>
          <li>Dacă un avocat îți invocă procese câștigate, cere numerele de dosar și verifică-le pe portal.just.ro.</li>
        </ol>
        <!--@author practice="litigii bancare" -->'''
faq=[("Se pot câștiga procese cu băncile?","Da. Cel mai des, prin constatarea clauzelor abuzive, restituirea sumelor sau anularea actelor de executare. Rezultatul depinde de contract și de probe."),
("Ce șanse am să câștig un proces?","Nu există o statistică oficială publică. Șansele se evaluează după contract, probe și termene. Fii prudent cu orice procent dat înainte de analiza actelor."),
("Cât durează un litigiu bancar?","De la câteva luni, la o contestație la executare, până la câțiva ani, cu apel și expertiză. O durată fixă nu poate fi garantată."),
("Cât costă un avocat?","Onorariul se stabilește în contractul de asistență juridică. Depinde de complexitate. Un onorariu de succes poate fi convenit doar în limitele Statutului profesiei, nu ca unic onorariu."),
("Ce tipuri de procese se câștigă cel mai des?","Cele privind clauzele abuzive: comisioane fără contraprestație, dobânda modificată discreționar, informarea insuficientă la creditele în CHF. Apoi contestațiile la executare cu nereguli."),
("Pot recupera bani de la bancă?","Da, sumele plătite în baza unei clauze abuzive. Restituirea poate fi supusă prescripției de 3 ani, iar începutul termenului îl stabilești cu avocatul, după jurisprudența CJUE (C-698/18)."),
("Este mai bine individual sau colectiv?","Colectiv, pentru o clauză identică în multe contracte. Individual, dacă ai executare, cesiune sau sume proprii de recuperat."),
("Cum aleg un avocat bun?","Verifică-l în Tabloul avocaților. Cere hotărâri cu număr de dosar și verifică-le pe portal.just.ro. Evită garanțiile de succes.")]
P=dict(slug='avocati-care-au-castigat-procese-cu-bancile',crumb='Avocați care au câștigat procese cu băncile',
 title='Avocați care au câștigat procese cu băncile: cum verifici',
 desc='Ce procese cu băncile se câștigă, ce înseamnă un câștig definitiv sau parțial și cum verifici pe portal.just.ro ce îți promite avocatul.',
 nav='#calculator|Calculator;#exemple|Exemple;#procedura|Procedura;#alegi|Cum alegi;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Procese cu băncile · rezultate verificabile',
  h1='Avocați care au câștigat procese cu băncile: <span class="accent">exemple și rezultate</span>',
  lead=['Plătești de zece ani un comision lunar pe care nu l-ai înțeles niciodată. Un site îți spune că „avocații noștri au câștigat sute de procese cu băncile”. Altul îți promite banii înapoi „garantat”. Nu știi pe cine să crezi.',
        'Aici afli ce <strong>procese cu băncile</strong> se câștigă de fapt și ce înseamnă un „proces câștigat”. Vezi hotărârile CJUE care au schimbat litigiile bancare. Și înveți să verifici singur, pe portal.just.ro și ReJust, ce îți spune un avocat.'],
  meta2='Verifică hotărârile pe portal.just.ro',cta='Calculează ce poți recupera',
  answer='Da, consumatorii câștigă procese cu băncile în România: clauze abuzive, comisioane, riscul valutar la creditele în CHF, executări silite nelegale. Succesul depinde de contract, de probe și de termene, nu de numele băncii și nici de câte procese spune avocatul că a câștigat. Un câștig poate fi total sau parțial.',
  opts=[('Verifici','numărul de dosar pe portal.just.ro'),('Nu crezi','procente și „câștig garantat”')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('tipuri','Tipuri de procese',S2),('exemple','Exemple reale',S3),('sanse','Șanse de câștig',S4),('rolul','Cum te ajută avocatul',S5),('procedura','Procedura pas cu pas',S6),('practica','Practica judiciară',S7),('legislatie','Legislație',S8),('durata','Durată și cost',S9),('greseli','Greșeli frecvente',S10),('alegi','Cum alegi',S11),('azi','Ce faci azi',S12)],
 faq=faq,faq_h2='Întrebări frecvente despre procesele cu băncile',
 contact=dict(h2='Ce clauze pot fi atacate în contractul tău?',lead='Trimite-ne contractul și extrasele, iar noi îți spunem ce clauze pot fi atacate și ce sume sunt în joc. Dacă ai deja o hotărâre, îți explicăm ce înseamnă concret pentru tine. Consultația nu te obligă la nimic.',nav='/|Acasă;/avocat-clauze-abuzive/|Clauze abuzive;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum decurge un proces cu banca',steps=[('Evaluarea cazului','Aduci contractul, actele adiționale și extrasele; afli dacă merită reclamație, CSALB sau instanță.'),('Pregătirea dosarului','Se ordonează actele, se calculează sumele și se redactează cererea.'),('Judecata','Banca depune întâmpinare, apoi urmează probele și hotărârea.'),('Calea de atac','Hotărârea primei instanțe se atacă, de regulă, cu apel.')]),
 knows=['Drept bancar','Clauze abuzive','Executare silită','Litigii bancare'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/avocati-care-au-castigat-procese-cu-bancile.src.html','w',encoding='utf-8').write(build(P))
