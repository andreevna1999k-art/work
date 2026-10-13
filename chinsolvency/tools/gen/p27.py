import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='contestatia-la-executare-pas-cu-pas.webp'; IMG2='ce-face-avocatul-in-contestatia-la-executare.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Ultima zi pentru contestație și <span class="accent">cât costă suspendarea</span></h2></div>
      <p>Introdu data la care ai primit somația sau adresa de poprire și suma contestată. Primești ultima zi de depunere (pe zile libere) și cauțiunea pentru suspendare, calculată după grila din art. 719 CPC.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Termenul</div>
          <div class="field full"><label for="f-d">Data primirii somației / a popririi</label><div class="inp"><input type="date" id="f-d"></div></div>
          <div class="grp">Suma contestată</div>
          <div class="field full"><label for="f-v">Valoarea contestată (lei)</label><div class="inp"><input id="f-v" inputmode="numeric" placeholder="40000"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: 40.000 lei</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Depune contestația până cel târziu pe</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">15 zile libere de la primirea actului (art. 715 și art. 181 CPC).</span></div>
            <div class="opt" id="c-c"><span class="k">Cauțiune pentru suspendare</span><span class="v" id="o-c">—</span><span class="s" id="o-cs">Art. 719 alin. (2) CPC.</span></div>
            <div class="opt" id="c-a"><span class="k">De avansat, fără onorariu</span><span class="v" id="o-a">—</span><span class="s" id="o-as">Cauțiune + 50 lei + taxa de cel mult 1.000 lei.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne actele spre analiză</a>
          <span class="disc">Calcul orientativ. Dacă ultima zi cade sâmbătă sau duminică, termenul se prelungește până luni; sărbătorile legale nu sunt luate în calcul aici. Depune cu cel puțin o zi înainte. Dacă invoci și motive de fond (art. 712 alin. (2) CPC), taxa de timbru se calculează după regulile generale și poate depăși 1.000 lei. Cauțiunea o stabilește instanța.</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  function dt(s){var p=s.split('-');return new Date(Date.UTC(+p[0],+p[1]-1,+p[2]))}
  function fmt(d){return ('0'+d.getUTCDate()).slice(-2)+'.'+('0'+(d.getUTCMonth()+1)).slice(-2)+'.'+d.getUTCFullYear()}
  var ZI=['duminică','luni','marți','miercuri','joi','vineri','sâmbătă'];
  function lei(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/[\s.]/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function caut(v){if(v<=10000)return v*0.10;if(v<=100000)return 1000+0.05*(v-10000);if(v<=1000000)return 5500+0.01*(v-100000);return 14500+0.001*(v-1000000)}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function calc(){
    var d=$('f-d').value,v=num('f-v');
    if(d){var e=dt(d);e.setUTCDate(e.getUTCDate()+16);var w=e.getUTCDay(),extra='';
      if(w===6){e.setUTCDate(e.getUTCDate()+2);extra=' Ultima zi calendaristică cădea sâmbătă, deci termenul se prelungește până luni.'}
      else if(w===0){e.setUTCDate(e.getUTCDate()+1);extra=' Ultima zi calendaristică cădea duminică, deci termenul se prelungește până luni.'}
      $('o-t').textContent=fmt(e)+' ('+ZI[e.getUTCDay()]+')';cls('c-t','alert');
      $('o-ts').textContent='15 zile libere după ziua primirii ('+fmt(dt(d))+'), conform art. 715 și art. 181 CPC.'+extra;
    }else{$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='15 zile libere de la primirea actului (art. 715 și art. 181 CPC).'}
    if(v>0){var c=caut(v);$('o-c').textContent=lei(c);$('o-cs').textContent='La '+lei(v)+' contestați, după grila din art. 719 alin. (2) CPC.';
      $('o-a').textContent='cel mult '+lei(c+50+1000);$('o-as').textContent=lei(c)+' cauțiune + 50 lei suspendare + taxa de cel mult 1.000 lei.'}
    else{$('o-c').textContent='—';$('o-cs').textContent='Art. 719 alin. (2) CPC.';$('o-a').textContent='—';$('o-as').textContent='Cauțiune + 50 lei + taxa de cel mult 1.000 lei.'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-d','f-v'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-d').value='2026-10-12';$('f-v').value='40000';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Contestație la executare: răspuns rapid</h2>
        <p>Contestația la executare este cererea prin care ceri judecătoriei să verifice dacă executarea silită e legală. O depui, de regulă, în 15 zile de la somație, de la poprire sau de la primul act de executare aflat. Nu oprește singură executarea. Pentru asta ceri suspendarea. Șansele depind de acte, nu de cât de grea e datoria.</p>
        <p>Un avocat contestație executare silită verifică în prima zi termenul, titlul și calculul. Apoi decide dacă cere și suspendarea.</p>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce înseamnă contestația la executare</h2>
        <p>Este calea prin care cel vătămat atacă executarea însăși, încheierile executorului sau orice act de executare (art. 712 CPC). Tot prin ea poți cere lămurirea titlului, adică „contestația la titlu”. O poate face debitorul, creditorul sau un terț care pretinde un drept asupra bunului urmărit. Ghidul general e la <a href="/contestatie-la-executare/">contestație la executare</a>.</p>
        <h3>Ce este executarea silită</h3>
        <p>Creditorul își ia banii prin executorul judecătoresc, fără acordul tău. Are nevoie de un titlu executoriu (art. 632 CPC): o hotărâre, un contract de credit, un bilet la ordin. Instanța de executare încuviințează executarea. Apoi executorul trimite somația și poate înființa poprirea. Etapele sunt explicate în ghidul despre <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>
        <h3>Când poți contesta executarea</h3>
        <ul class="chk">
          <li>Titlul nu e executoriu sau dreptul de a-l executa s-a prescris.</li>
          <li>Suma din somație depășește titlul sau încheierea de încuviințare.</li>
          <li>Actele nu ți-au fost comunicate sau au mers la o adresă veche.</li>
          <li>Poprirea ia mai mult decât permite art. 729 CPC.</li>
          <li>Bunul urmărit nu este al debitorului.</li>
        </ul>
        <h4>Exemple concrete</h4>
        <p>Situații tipice (anonimizate):</p>
        <div class="roles">
          <div><b>Credit cesionat de două ori</b>Poprire pe salariu pentru un credit de consum cesionat de două ori. Ultima plată e veche de mulți ani.</div>
          <div><b>Cheltuieli nejustificate</b>Somație în care cheltuielile de executare sunt aproape cât debitul, fără nicio justificare.</div>
          <div><b>Poprire pe cont protejat</b>Poprire pe contul în care intră alocația copilului.</div>
        </div>'''
S3='''        <span class="eyebrow">Motive</span>
        <h2>Motive pentru contestația la executare</h2>
        <p>Motivul trebuie să fie juridic, nu financiar. Cele mai folosite sunt prescripția, erorile din dosarul executorului, clauzele abuzive din contractul-titlu și lipsa documentelor care susțin suma. Atenție: contra unei hotărâri judecătorești nu poți relua apărările pe care le puteai face în proces (art. 713 CPC).</p>
        <h3>Prescripția datoriei</h3>
        <p>Dreptul de a obține executarea silită se prescrie, ca regulă, în 3 ani (art. 706 CPC). Pentru titlurile din materia drepturilor reale, termenul e de 10 ani. La hotărâri, curge de la rămânerea definitivă. Nu ajunge că „au trecut ani”. Avocatul caută întreruperile, plățile parțiale și actele de executare anterioare.</p>
        <h3>Erori în dosar</h3>
        <p>Somație trimisă la o adresă la care nu mai locuiai. Sumă mai mare decât cea încuviințată. Cheltuieli de executare fără justificare. Creditor nou fără dovada cesiunii. Fiecare poate duce la anularea unui act sau la reducerea sumei.</p>
        <h3>Clauze abuzive</h3>
        <p>Când titlul este un contract de credit, nu o hotărâre, poți invoca și apărări de fond (art. 713 CPC). Printre ele, clauzele abuzive. În cauza C-725/19 Impuls Leasing România (17 mai 2022), CJUE a cerut ca instanța de executare să le poată verifica, când acțiunea separată nu te protejează efectiv. Despre clauzele din contract, vezi <a href="/avocat-clauze-abuzive/">avocat clauze abuzive</a>.</p>
        <h4>Lipsa documentelor</h4>
        <p>Instanța cere executorului copia dosarului. Dacă lipsesc contractul, actul de cesiune sau calculul sumei, ai un argument. Fără ele, suma rămâne o afirmație a creditorului.</p>'''
S4='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura contestației la executare pas cu pas</h2>
        <p>Procedura are patru pași: strângi actele, calculezi termenul, depui cererea la instanța de executare și urmezi judecata. Instanța cere executorului dosarul și judecă de urgență. Hotărârea se atacă doar cu apel. Avocatul preia fiecare pas și îți spune, după fiecare termen, unde se află dosarul.</p>
        <h3>Depunerea contestației</h3>
        <p>Instanța competentă este instanța de executare: judecătoria de la domiciliul sau sediul debitorului la data sesizării executorului (art. 651 și art. 714 CPC). Contestația la titlu merge la instanța care a dat hotărârea. Cererea respectă forma cererii de chemare în judecată (art. 194 CPC). Anexezi actele primite, titlul și dovada taxei. Detalii practice: <a href="/unde-se-depune-contestatia-la-executare/">unde se depune contestația la executare</a>.</p>
        <h3>Termenul legal</h3>
        <p>Ai 15 zile (art. 715 CPC). Curg de la somație sau de la încheierea de încuviințare. La poprire, de la comunicarea ei sau, la salariu, cel târziu de la prima reținere. Termenul se calculează pe zile libere (art. 181 CPC): nu se numără nici ziua primirii, nici ultima zi. Dacă ultima zi cade într-o zi nelucrătoare, termenul se prelungește până în prima zi lucrătoare. Lămurirea titlului se poate cere oricând, cât timp executarea nu s-a prescris. Exemple de calcul: <a href="/termen-contestatie-la-executare/">termen contestație la executare</a>.</p>
        <h3>Judecata în instanță</h3>
        <p>Părțile sunt citate la termene scurte, iar cauza se judecă de urgență și cu precădere (art. 717 CPC). Creditorul depune întâmpinare. Avocatul răspunde, propune probe și cere, la nevoie, lămuriri executorului.</p>
        <h4>Decizia instanței</h4>
        <p>Dacă admite, instanța anulează sau îndreaptă actul, anulează ori încetează executarea sau lămurește titlul (art. 720 CPC). Hotărârea se atacă numai cu apel (art. 718 CPC). Dacă executarea cade, poți cere întoarcerea executării. Banii reținuți se întorc la tine (art. 723 CPC).</p>
'''+fig(IMG1,'avocat contestație executare silită — pașii de la somație la hotărâre','Contestația la executare, pas cu pas')
S5='''        <span class="eyebrow">Suspendare</span>
        <h2>Suspendarea executării silite</h2>
        <p>Contestația nu oprește poprirea. O oprește suspendarea, pe care o ceri odată cu contestația sau separat (art. 719 CPC). Instanța o acordă pentru motive temeinice și, de regulă, cu cauțiune. În cazuri urgente poți cere suspendare provizorie, până se judecă cererea de suspendare. Mai multe în ghidul despre <a href="/amanare-executare-silita/">suspendarea executării silite</a>.</p>
        <h3>Cum poți obține suspendarea</h3>
        <ol class="num">
          <li>Ceri suspendarea în contestație sau printr-o cerere separată.</li>
          <li>Plătești taxa de 50 lei și cauțiunea stabilită de instanță.</li>
          <li>Dacă poprirea golește contul, ceri și suspendarea provizorie. Instanța decide fără citarea părților, după plata cauțiunii.</li>
          <li>Încheierea de suspendare se comunică din oficiu executorului.</li>
        </ol>
        <h3>Condiții</h3>
        <p>Ai nevoie de motive serioase, vizibile din acte. Cauțiunea se calculează la valoarea obiectului contestației (art. 719 alin. (2) CPC):</p>
        <ul class="chk">
          <li>10%, până la 10.000 lei;</li>
          <li>1.000 lei plus 5% din ce depășește 10.000 lei;</li>
          <li>5.500 lei plus 1% din ce depășește 100.000 lei;</li>
          <li>14.500 lei plus 0,1% din ce depășește 1.000.000 lei.</li>
        </ul>
        <p>Dacă obiectul nu se poate evalua în bani, cauțiunea e de 1.000 lei. Suspendarea e obligatorie, fără cauțiune, în cazuri limitativ prevăzute de lege, de exemplu când titlul nu e executoriu sau înscrisul a fost declarat fals în primă instanță.</p>
        <h4>Cauțiunea pentru suspendare</h4>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Ești executat pentru 40.000 lei și contești toată suma. Cauțiunea: 1.000 lei + 5% × (40.000 − 10.000) = 1.000 + 1.500 = 2.500 lei. Adaugi 50 lei taxa pentru suspendare și cel mult 1.000 lei taxa pentru contestație. Total de avansat, fără onorariu: cel mult 3.550 lei.</p>
          <p>Cauțiunea nu e o taxă pierdută. Dacă pierzi, rămâne blocată pentru despăgubirile creditorului.</p>
          <span class="formula">1.000 + 5% × 30.000 = 2.500 lei · 2.500 + 50 + 1.000 = 3.550 lei</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S6='''        <span class="eyebrow">Durată</span>
        <h2>Cât durează contestația la executare</h2>
        <p>Legea nu fixează o durată în luni. Fixează urgența: termene scurte și judecare cu precădere. Durata reală depinde de cât de repede trimite executorul dosarul, de încărcarea instanței, de probe și de apel. Cererea de suspendare poate fi soluționată înaintea fondului. Suspendarea provizorie se decide fără citarea părților, deci mai repede.</p>
        <h3>Durata procesului</h3>
        <p>Etapele: înregistrare și cererea dosarului de executare, primul termen, probe, hotărâre, apel.</p>
        <h3>Factori care influențează durata</h3>
        <p>Volumul instanței, expertiza contabilă când suma e contestată și apelul.</p>
        <h4>Termene medii</h4>
        <p>Nu publicăm o medie, pentru că ar fi o cifră inventată. La prima discuție îți spunem ce durată e realistă la judecătoria ta, după dosarele similare.</p>'''
S7='''        <span class="eyebrow">Costuri</span>
        <h2>Costuri contestație la executare</h2>
        <p>Costul are trei părți: taxele de timbru, cauțiunea pentru suspendare și onorariul avocatului. Taxa pentru contestația la executare propriu-zisă se calculează la valoarea contestată, dar nu trece de 1.000 lei. Cererea de suspendare costă 50 lei. Cauțiunea depinde de sumă și nu e o cheltuială definitivă. Onorariul se stabilește după analiza actelor.</p>
        <h3>Taxa de timbru</h3>
        <p>Potrivit art. 10 din OUG nr. 80/2013, contestația la executare propriu-zisă se taxează la valoarea bunurilor urmărite sau a debitului, fără a depăși 1.000 lei. Cererea de suspendare se taxează cu 50 lei. Dacă invoci și motive de fond (art. 712 alin. (2) CPC), taxa se calculează după regulile generale și poate fi mai mare. Cere avocatului calculul exact pentru dosarul tău.</p>
        <h3>Onorariul avocatului</h3>
        <p>Se stabilește în contractul de asistență juridică. Poate fi fix, pe etape (contestație, suspendare, apel) sau orar. Primești în scris ce include și ce nu. Dacă câștigi, poți cere creditorului cheltuielile de judecată, inclusiv onorariul (art. 453 CPC).</p>
        <h4>Cost total estimat</h4>
        <p>Taxa, 50 lei pentru suspendare, cauțiunea după grilă și onorariul. Exemplul de 40.000 lei de mai sus: cel mult 3.550 lei fără onorariu, dacă nu invoci motive de fond.</p>'''
S8='''        <span class="eyebrow">Șanse</span>
        <h2>Șanse de câștig la contestația la executare</h2>
        <p>Șansele țin de motive și de probe. Sunt reale când poți arăta exact eroarea: un act, o dată, o sumă, un articol de lege. Sunt mici când singurul argument e că datoria e greu de plătit. Un avocat serios nu îți dă un procent înainte de a vedea dosarul de executare.</p>
        <h3>Factori decisivi</h3>
        <ul class="chk">
          <li><strong>Documentele:</strong> somația, încheierea de încuviințare, titlul, calculul sumei.</li>
          <li><strong>Prescripția:</strong> datele scadenței, ale ultimei plăți și ale primului act de executare.</li>
          <li><strong>Termenul:</strong> o contestație tardivă se respinge fără analiza motivelor.</li>
        </ul>
        <h3>Estimare șanse</h3>
        <p>După analiză primești o evaluare scrisă: motivele puternice, cele slabe și riscurile. Fără procente. Un procent dat fără dosar e marketing.</p>
        <h4>Riscuri</h4>
        <p>Dacă pierzi, poți fi obligat la despăgubiri pentru întârzierea executării. O contestație făcută cu rea-credință atrage și o amendă judiciară de la 1.000 la 7.000 lei (art. 720 alin. (3) CPC). Suporți și cheltuielile de judecată ale creditorului.</p>
        <div class="tbl wide"><table>
          <thead><tr><th>Opțiune</th><th>Când se potrivește</th><th>Cost</th><th>Durată</th><th>Ce obții</th><th>Recomandare</th></tr></thead>
          <tbody>
            <tr><td>Contestație la executare</td><td>Există o eroare concretă: prescripție, sumă greșită, act necomunicat</td><td>Taxă ≤ 1.000 lei, onorariu</td><td>Depinde de instanță și de apel</td><td>Anularea sau reducerea executării</td><td>Prima opțiune când actele au vicii</td></tr>
            <tr><td>Suspendare</td><td>Poprire activă sau vânzare iminentă</td><td>50 lei + cauțiune</td><td>Mai rapidă decât fondul</td><td>Oprirea temporară a executării</td><td>Împreună cu contestația</td></tr>
            <tr><td>Negociere</td><td>Datoria e reală, dar suma sau ritmul se pot discuta</td><td>Onorariu, fără taxe</td><td>Depinde de creditor</td><td>Reducere sau eșalonare, prin acord scris</td><td>Când actele sunt corecte</td></tr>
            <tr><td>Plată</td><td>Suma e verificată și corectă</td><td>Debitul și cheltuielile</td><td>Imediată</td><td>Încetarea executării</td><td>Doar după verificarea calculului</td></tr>
            <tr><td>Restructurare</td><td>Venit stabil, dar plata integrală nu e posibilă</td><td>Variabil</td><td>Depinde de creditor</td><td>Rate suportabile</td><td>Când contestația e slabă</td></tr>
          </tbody>
        </table></div>'''
S9='''        <span class="eyebrow">Practică</span>
        <h2>Practica judiciară și cazuri reale</h2>
        <p>Instanțele admit contestațiile bine documentate și le resping pe cele generale. Motivele admise des sunt prescripția, sumele peste titlu, cheltuielile de executare nejustificate și poprirea peste limitele legale. Mai jos sunt situații tipice. Hotărâri concrete poți căuta pe portal.just.ro, după număr de dosar și instanță.</p>
        <h3>Contestații admise</h3>
        <p>Situații tipice (anonimizate):</p>
        <ul class="chk">
          <li>Recuperator care execută fără să depună actul de cesiune la dosar.</li>
          <li>Executare pornită după ce dreptul de a o cere se prescrisese.</li>
          <li>Cheltuieli de executare calculate peste onorariul legal al executorului.</li>
        </ul>
        <h4>Strategii eficiente</h4>
        <p>Un motiv solid bate cinci slabe. Când există poprire, contestația și suspendarea pornesc împreună.</p>'''
S10='''        <span class="eyebrow">Legislație</span>
        <h2>Legislație aplicabilă</h2>
        <p>Baza este Codul de procedură civilă: art. 712–720 pentru contestație și suspendare, art. 651 pentru instanța de executare, art. 706 pentru prescripție, art. 729 pentru limitele popririi și art. 723 pentru întoarcerea executării. Taxele vin din OUG nr. 80/2013. Datoriile la stat urmează Codul de procedură fiscală.</p>
        <h3>Codul de procedură civilă</h3>
        <p>Articolele, explicate pe înțeles: <a href="/contestatia-la-executare-cod-procedura-civila/">contestația la executare în Codul de procedură civilă</a>.</p>
        <h3>Drepturile debitorului</h3>
        <p>Din salariu sau pensie se poate popri cel mult o treime pentru datorii obișnuite și cel mult jumătate pentru pensia de întreținere (art. 729 CPC). Când sunt mai multe popriri, totalul nu trece de jumătate. Alocațiile pentru copii nu pot fi poprite. Pentru conturi, vezi ghidul despre <a href="/poprire-cont/">poprire cont</a>.</p>
        <h4>Comparație norme</h4>
        <p>Executarea pornită de ANAF sau de primărie urmează Legea nr. 207/2015 privind Codul de procedură fiscală, cu reguli proprii pentru contestație. Verifică termenul și instanța cu avocatul înainte de a depune, fiindcă nu sunt aceleași ca în executarea civilă.</p>'''
S11='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente</h2>
        <p>Trei greșeli pierd cele mai multe dosare: termenul de 15 zile ratat, contestația fără probe și contestația depusă greșit. Toate se pot evita în primele zile. Ai nevoie de data exactă a primirii actelor, de dosarul de executare complet și de o cerere care atacă actul potrivit, la instanța potrivită.</p>
        <h3>Depășirea termenului</h3>
        <p>Mulți așteaptă să vadă „ce se întâmplă”. Termenul curge între timp. După 15 zile, contestația se respinge ca tardivă, oricât de bune ar fi motivele.</p>
        <h3>Lipsa dovezilor</h3>
        <p>„Suma e prea mare” nu e un motiv. Ai nevoie de contract, extrase, acte de executare și un calcul care arată diferența.</p>
        <h4>Contestație greșită</h4>
        <p>Fără cererea de suspendare, poprirea continuă. La instanța greșită, dosarul se declină și pierzi timp. Contra unei hotărâri nu mai poți relua apărările din proces.</p>'''
S12='''        <span class="eyebrow">Alegerea</span>
        <h2>Cum alegi un avocat pentru contestație la executare</h2>
        <p>Alegi după experiența reală în executare silită, dovezi verificabile și transparență. Un avocat potrivit îți spune din prima discuție cât timp mai ai, ce motive vede și dacă cere suspendarea. Îți spune și când contestația nu are sens. Cel care promite anularea datoriei înainte să citească actele nu e alegerea bună.</p>
        <h3>Experiența</h3>
        <p>Un avocat executare silită bun lucrează zilnic cu popriri, încuviințări și cauțiuni. Întreabă câte contestații a pledat în ultimul an și la ce instanțe. Răspunsurile vagi spun destul.</p>
        <h3>Cazuri câștigate</h3>
        <p>Cere hotărâri anonimizate, cu număr de dosar și instanță. Le poți verifica pe portal.just.ro sau pe rejust.ro. Verifică și dacă avocatul figurează în Tabloul avocaților pe site-ul UNBR.</p>
        <h3>Ce face avocatul în dosarul tău</h3>
        <ol class="num">
          <li><strong>Analiza actelor:</strong> titlul, încuviințarea, somația, poprirea, calculul.</li>
          <li><strong>Termenul:</strong> data exactă de la care curg cele 15 zile.</li>
          <li><strong>Contestația:</strong> motivele, probele, cererea dosarului de executare.</li>
          <li><strong>Suspendarea și cauțiunea:</strong> cererea, calculul cauțiunii, varianta provizorie.</li>
          <li><strong>Reprezentarea:</strong> termenele în instanță și apelul.</li>
          <li><strong>Întoarcerea executării:</strong> recuperarea sumelor deja reținute.</li>
        </ol>
        <h3>Ce acte aduci</h3>
        <p>Somația, încheierea de încuviințare, adresa de poprire, procesul-verbal de cheltuieli și plicurile cu data primirii. Dacă e un credit: contractul, graficul, extrasele și notificările de cesiune. Plicul cu ștampila poștei e adesea cea mai importantă probă pentru termen.</p>
        <h4>Transparența</h4>
        <p>Colaborarea începe cu o analiză a actelor și cu un contract scris. Știi dinainte ce etape acoperă onorariul. După fiecare termen afli ce s-a întâmplat și care e pasul următor.</p>
        <div class="note dark"><b>Poziția juridică.</b> Prima întrebare nu e „cât datorezi?”, ci „când ai primit actele?”. Un dosar cu motive bune și termen ratat e pierdut. Un dosar cu un singur motiv solid, depus la timp și însoțit de cerere de suspendare, protejează contul.</div>
'''+fig(IMG2,'avocat contestație executare silită — analiză, contestație, suspendare, reprezentare','Ce face avocatul în contestația la executare')
S13='''        <span class="eyebrow">Urgent</span>
        <h2>Ce trebuie să faci urgent dacă ești executat silit</h2>
        <p>Primele zile decid dosarul. Notezi data la care ai primit fiecare act și strângi tot ce ai de la executor și de la bancă. Nu plătești o sumă neverificată. Ceri o analiză juridică înainte să treacă jumătate din termenul de 15 zile. Viteza contează mai mult decât un argument perfect.</p>
        <h3>Pașii imediați</h3>
        <p>Fotografiază actele și plicurile. Verifică de când e blocat contul. Cere executorului copia dosarului.</p>
        <h4>Recomandări</h4>
        <p>Nu semna recunoașteri de datorie fără să le citești. Nu aștepta ca banca să rezolve poprirea: ea doar aplică adresa executorului.</p>'''
S14='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Scrie pe somație și pe adresa de poprire data la care le-ai primit. Păstrează plicurile.</li>
          <li>Numără 15 zile libere de la acea dată și notează ultima zi în telefon (sau folosește calculatorul de mai sus).</li>
          <li>Trimite unui avocat somația, încheierea de încuviințare și titlul, pentru o analiză înainte de ultima săptămână.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Ce este contestația la executare?","Cererea prin care ceri instanței să verifice legalitatea executării silite sau a unui act al executorului (art. 712 CPC)."),
("Care este termenul de depunere?","15 zile, de la somație, de la comunicarea popririi sau de la primul act aflat (art. 715 CPC). Se calculează pe zile libere."),
("Pot opri executarea silită?","Da, prin suspendare, cerută odată cu contestația sau separat, de regulă cu cauțiune (art. 719 CPC). În urgențe există suspendarea provizorie."),
("Cât durează procesul?","Nu există o durată fixă. Cauza se judecă de urgență, dar timpul real depinde de instanță, de probe și de apel."),
("Cât costă contestația?","Taxa de timbru la contestația propriu-zisă nu depășește 1.000 lei, suspendarea costă 50 lei, la care se adaugă cauțiunea și onorariul. La 40.000 lei contestați, fără onorariu și fără motive de fond, ajungi la cel mult 3.550 lei."),
("Ce șanse am să câștig?","Depinde de motive și de probe. Un motiv concret, dovedit cu acte, valorează mai mult decât multe motive generale."),
("Este obligatoriu avocatul?","Nu. Poți depune singur contestația. Termenul, motivele și calculul cauțiunii sunt însă tehnice, iar o greșeală nu se mai poate repara."),
("Ce se întâmplă dacă pierd?","Executarea continuă. Poți suporta cheltuielile de judecată și despăgubiri, iar cauțiunea rămâne blocată pentru acestea.")]
P=dict(slug='avocat-contestatie-executare-silita',crumb='Avocat contestație executare silită',
 title='Avocat contestație executare silită: procedură, suspendare',
 desc='Avocat contestație executare silită: verificăm actele și termenul de 15 zile, depunem contestația, cerem suspendarea și te reprezentăm în instanță.',
 nav='#calculator|Termen și cauțiune;#procedura|Procedura;#suspendare|Suspendarea;#costuri|Costuri;#intrebari|Întrebări',
 images=[IMG1,IMG2],date='13 octombrie 2026',
 hero=dict(eyebrow='Executare silită · poprire · suspendare',
  h1='Avocat contestație executare silită: <span class="accent">procedură și suspendarea executării</span>',
  lead=['Deschizi aplicația băncii și contul arată zero. Pe fluturașul de salariu apare „poprire”. Somația de la executor stă pe masă de cinci zile.',
        'Aici afli când ai nevoie de un <strong>avocat pentru contestația la executare silită</strong> și ce face el concret. Vezi ce acte îi aduci, cum se oprește executarea prin suspendare și cât costă taxele și cauțiunea. La final, cum alegi avocatul fără să cumperi promisiuni.'],
  meta2='Termen: 15 zile libere',cta='Calculează termenul și cauțiunea',
  answer='Contestația la executare este cererea prin care ceri judecătoriei să verifice dacă executarea silită e legală. O depui, de regulă, în 15 zile de la somație, de la poprire sau de la primul act de executare aflat. Nu oprește singură executarea: pentru asta ceri suspendarea, de regulă cu cauțiune. Șansele depind de acte, nu de cât de grea e datoria.',
  opts=[('Termen','15 zile libere (art. 715 CPC)'),('Suspendare','50 lei + cauțiune (art. 719 CPC)')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-inseamna','Ce înseamnă',S2),('motive','Motive',S3),('procedura','Procedura pas cu pas',S4),('suspendare','Suspendarea executării',S5),('durata','Cât durează',S6),('costuri','Costuri',S7),('sanse','Șanse de câștig',S8),('practica','Practica judiciară',S9),('legislatie','Legislație',S10),('greseli','Greșeli frecvente',S11),('alegi','Cum alegi avocatul',S12),('urgent','Ce faci urgent',S13),('azi','Ce faci azi',S14)],
 faq=faq,faq_h2='Întrebări frecvente despre contestația la executare',
 contact=dict(h2='Câte zile mai ai pentru contestație?',lead='Trimite-ne somația, adresa de poprire și titlul. Îți spunem câte zile mai ai, ce motive vedem și dacă merită cerută suspendarea. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum depui o contestație la executare',steps=[('Strângi actele','Somația, încheierea de încuviințare, titlul, adresa de poprire și plicurile cu data primirii.'),('Calculezi termenul','15 zile libere de la primirea actului (art. 715 și art. 181 CPC).'),('Depui cererea','La instanța de executare, cu motivele, probele și dovada taxei; ceri și suspendarea.'),('Urmezi judecata','Cauza se judecă de urgență; hotărârea se atacă cu apel.')]),
 knows=['Executare silită','Contestație la executare','Suspendarea executării','Poprire'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/avocat-contestatie-executare-silita.src.html','w',encoding='utf-8').write(build(P))
