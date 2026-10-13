import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='contestatia-la-executare-art-712720-cpc.webp'; IMG2='cautiunea-pentru-suspendare-3-calcule.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Cauțiunea din <span class="accent">art. 719 CPC</span>, pe treapta ta</h2></div>
      <p>Introdu valoarea obiectului contestației. Vezi în ce treaptă a grilei din art. 719 alin. (2) te afli, cât este cauțiunea și cât avansezi în total pentru suspendare.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Obiectul contestației</div>
          <div class="field"><label for="f-t">Tipul obiectului</label><div class="inp"><select id="f-t"><option value="b" selected>Evaluabil în bani</option><option value="n">Neevaluabil în bani</option></select></div></div>
          <div class="field" id="w-v"><label for="f-v">Valoarea contestată (lei)</label><div class="inp"><input id="f-v" inputmode="numeric" placeholder="40000"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: 40.000 lei</button>
            <button type="button" class="btn btn-line" id="b-ex2">Exemplu: 250.000 lei</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-c"><span class="k">Cauțiunea pentru suspendare</span><span class="v" id="o-c">—</span><span class="s" id="o-cs">Completați valoarea contestată.</span></div>
            <div class="opt" id="c-f"><span class="k">Formula treptei</span><span class="v" id="o-f" style="font-size:17px">—</span><span class="s" id="o-fs">Art. 719 alin. (2) CPC.</span></div>
            <div class="opt" id="c-a"><span class="k">+ taxa pentru suspendare</span><span class="v" id="o-a">—</span><span class="s" id="o-as">50 lei, fără taxa contestației și fără onorariu.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne actele spre analiză</a>
          <span class="disc">Calcul orientativ, după grila din art. 719 alin. (2) CPC. Cauțiunea o stabilește instanța. Suspendarea e obligatorie, fără cauțiune, doar în cazurile prevăzute de lege. Dacă pierzi contestația, cauțiunea rămâne indisponibilizată pentru despăgubirile creditorului (art. 720 alin. (6) CPC).</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  function lei(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/[\s.]/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function f(v){if(v<=10000)return [v*0.10,'10% × valoarea'];if(v<=100000)return [1000+0.05*(v-10000),'1.000 + 5% din ce depășește 10.000'];if(v<=1000000)return [5500+0.01*(v-100000),'5.500 + 1% din ce depășește 100.000'];return [14500+0.001*(v-1000000),'14.500 + 0,1% din ce depășește 1.000.000']}
  function mode(){var n=$('f-t').value==='n';$('w-v').style.display=n?'none':''}
  function calc(){
    mode();
    if($('f-t').value==='n'){$('o-c').textContent='1.000 lei';$('o-cs').textContent='Obiect neevaluabil în bani: cauțiune fixă.';$('o-f').textContent='fixă';$('o-a').textContent='1.050 lei';$('o-as').textContent='1.000 cauțiune + 50 taxă suspendare.';return}
    var v=num('f-v');
    if(v>0){var r=f(v);$('o-c').textContent=lei(r[0]);$('o-cs').textContent='La '+lei(v)+' contestați.';$('o-f').textContent=r[1];$('o-a').textContent=lei(r[0]+50);$('o-as').textContent=lei(r[0])+' cauțiune + 50 lei taxă suspendare.'}
    else{$('o-c').textContent='—';$('o-cs').textContent='Completați valoarea contestată.';$('o-f').textContent='—';$('o-a').textContent='—';$('o-as').textContent='50 lei, fără taxa contestației și fără onorariu.'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-t','f-v'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-t').value='b';$('f-v').value='40000';calc()}
  function ex2(){$('f-t').value='b';$('f-v').value='250000';calc()}
  $('b-ex1').addEventListener('click',ex);$('b-ex2').addEventListener('click',ex2);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});
  mode();'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Contestația la executare în CPC: răspuns rapid</h2>
        <p>Contestația la executare este cererea prin care ceri instanței să verifice legalitatea executării silite. Temeiul este art. 712 din Codul de procedură civilă. Poți ataca executarea însăși, încheierile executorului și orice act de executare. Termenul general este de 15 zile (art. 715). Contestația nu oprește singură executarea. Pentru asta ceri suspendarea, cu cauțiune (art. 719).</p>
        <ul class="chk">
          <li><strong>„Art. 711” sau „art. 712”?</strong> În forma republicată în 2015, obiectul contestației este la art. 712. Numărul 711 vine din numerotarea de dinainte de republicare.</li>
          <li><strong>Termenele din art. 715:</strong> 15 zile, cu momente de început diferite. Contestația la titlu se poate face oricând înăuntrul termenului de prescripție a executării.</li>
        </ul>'''
S2='''        <span class="eyebrow">Capitolul</span>
        <h2>Ce este contestația la executare conform Codului de procedură civilă</h2>
        <p>În Codul de procedură civilă, contestația la executare este calea prin care instanța controlează executarea silită. Ea are un capitol propriu, art. 712–720. Acolo găsești obiectul, condițiile de admisibilitate, instanța, termenele, forma, judecata, calea de atac, suspendarea și soluțiile. Pentru o prezentare generală, vezi ghidul despre <a href="/contestatie-la-executare/">contestație la executare</a>.</p>
        <h3>Rolul contestației la executare</h3>
        <p>Executorul aplică titlul, nu judecă. Dacă îl depășește sau sare peste o etapă, doar instanța îl corectează. Contestația te protejează ca debitor.</p>
        <h3>Când poate fi formulată contestația</h3>
        <p>După ce executarea a început. De regulă, după ce primești încheierea de încuviințare și somația ori afli de o poprire. Dacă nu ai primit nimic, poți contesta din momentul în care afli de primul act de executare.</p>
        <h4>Exemple practice</h4>
        <p>Situații tipice (anonimizate):</p>
        <div class="roles">
          <div><b>Poprire și plăți parțiale</b>Poprire pe salariu, deși datoria fusese plătită parțial. Somația nu ține cont de plăți.</div>
          <div><b>Cheltuieli peste limită</b>Procesul-verbal de cheltuieli de executare depășește onorariul permis.</div>
          <div><b>Cesionar fără dovadă</b>Executare pornită de un cesionar, fără dovada cesiunii în dosar.</div>
        </div>'''
S3='''        <span class="eyebrow">Art. 712</span>
        <h2>Art. 711 sau art. 712 CPC: obiectul contestației explicat simplu</h2>
        <p>Mulți caută „contestația la executare art. 711”. În Codul de procedură civilă republicat în 2015, textul despre obiectul contestației este art. 712. Republicarea a renumerotat articolele. Fostul art. 711 a devenit art. 712, iar fostul art. 714 privind termenele a devenit art. 715. Modelele vechi păstrează numerotarea veche. Verifică mereu forma în vigoare.</p>
        <h3>Ce prevede art. 712</h3>
        <ul class="chk">
          <li><strong>Alin. (1):</strong> se poate contesta executarea silită, încheierile executorului și orice act de executare. Tot aici intră refuzul executorului de a face un act de executare.</li>
          <li><strong>Alin. (2):</strong> poți cere lămurirea înțelesului, întinderii sau aplicării titlului executoriu, adică „contestația la titlu”.</li>
          <li><strong>Alin. (3):</strong> poți cere și anularea încheierii de încuviințare a executării, dacă a fost dată fără condițiile legale.</li>
        </ul>
        <h3>Cine poate formula contestația</h3>
        <p>Art. 712 spune: „cei interesați sau vătămați prin executare”. Concret:</p>
        <ul class="chk">
          <li><strong>Debitorul:</strong> cel urmărit prin titlu.</li>
          <li><strong>Garantul:</strong> fideiusorul sau garantul ipotecar urmărit pentru datoria altuia.</li>
          <li><strong>Terțul:</strong> la urmărirea bunurilor, doar dacă pretinde un drept de proprietate sau alt drept real asupra bunului (art. 713 alin. (5)).</li>
        </ul>
        <h3>Ce acte pot fi contestate</h3>
        <ul class="chk">
          <li><strong>Somația</strong> și încheierea de încuviințare.</li>
          <li><strong>Poprirea</strong>, inclusiv <a href="/poprire-cont/">poprire cont</a> sau pe salariu.</li>
          <li><strong>Executarea însăși</strong>: când nu există titlu sau dreptul de a executa s-a prescris.</li>
          <li>Procesul-verbal de cheltuieli, publicația de vânzare, actele de evaluare.</li>
        </ul>
        <h4>Limitele contestației</h4>
        <p>Art. 713 stabilește ce nu poți invoca. Dacă titlul este o hotărâre judecătorească, nu poți aduce apărări pe care le puteai ridica în proces sau într-o cale de atac. Dacă titlul e altul, de exemplu un contract de credit, poți discuta și fondul datoriei, dacă legea nu prevede o cale specială pentru desființarea lui. Nu poți face o a doua contestație pentru motive care existau la prima, dar poți adăuga motive noi, dacă pentru ele termenul este respectat (art. 713 alin. (3)).</p>'''
S4='''        <span class="eyebrow">Art. 715</span>
        <h2>Articolul 715 CPC și termenele legale</h2>
        <p>Art. 715 stabilește un termen de 15 zile pentru contestația împotriva executării. Diferă momentul de la care curge: data la care ai luat cunoștință de act, data comunicării popririi sau a somației. Contestația la titlu nu are acest termen. Dacă depui după 15 zile, contestația poate fi respinsă ca tardivă. Detaliile sunt în ghidul despre <a href="/termen-contestatie-la-executare/">termen contestație la executare</a>.</p>
        <h3>Termenul de 15 zile</h3>
        <p>Termenul se calculează pe zile libere (art. 181 CPC). Nu se numără ziua în care primești actul și nici ultima zi. Dacă ultima zi cade într-o zi nelucrătoare, termenul se prelungește până la prima zi lucrătoare.</p>
        <h3>Momentul de la care curge termenul</h3>
        <ul class="chk">
          <li>de la data la care ai luat cunoștință de actul de executare contestat;</li>
          <li>la poprire, de la comunicarea popririi; la veniturile periodice, cel târziu de la prima reținere;</li>
          <li>pentru executarea însăși, de la primirea încheierii de încuviințare sau a somației; dacă nu le-ai primit, de la primul act de executare de care afli.</li>
        </ul>
        <h4>Excepții și cazuri speciale</h4>
        <ul class="chk">
          <li><strong>Contestația la titlu:</strong> oricând înăuntrul termenului de prescripție a dreptului de a obține executarea (art. 715 alin. (3)).</li>
          <li><strong>Încheierile executorului:</strong> 15 zile de la comunicare, când nu sunt definitive (art. 715 alin. (2)).</li>
          <li><strong>Terțul cu drept real:</strong> pe tot parcursul executării, dar cel târziu în 15 zile de la vânzare sau de la predarea silită a bunului (art. 715 alin. (4)).</li>
        </ul>
'''+fig(IMG1,'contestația la executare în Codul de procedură civilă — obiect, instanță, termene, suspendare și soluții','Contestația la executare: art. 712–720 CPC')
S5='''        <span class="eyebrow">Motive</span>
        <h2>Motive pentru contestația la executare</h2>
        <p>Motivele trebuie să fie juridice. Faptul că datoria e mare sau că nu poți plăti nu este motiv. Cele mai solide sunt prescripția dreptului de a executa, lipsa titlului executoriu, erorile de procedură și suma care nu rezultă din titlu. La contractele de consum se adaugă clauzele abuzive. Le ordonezi după forța lor juridică.</p>
        <h3>Prescripția executării silite</h3>
        <p>Dreptul de a cere executarea se prescrie, de regulă, în 3 ani. Pentru drepturile reale, termenul este de 10 ani (art. 706). Verifici data la care titlul a devenit executoriu, plățile făcute și actele care au întrerupt prescripția. Prescripția se invocă, nu se aplică singură.</p>
        <h3>Lipsa titlului executoriu</h3>
        <p>Executarea se face numai în temeiul unui titlu executoriu (art. 632). Ceri dosarul și verifici: există titlul? Este executoriu? Cine e creditorul în titlu și cine îți cere banii? Suma din somație rezultă din titlu?</p>
        <h3>Erori procedurale</h3>
        <p>Acte necomunicate sau comunicate la altă adresă. Cheltuieli de executare nejustificate. Poprire peste limitele din art. 729, de exemplu peste partea din salariu care poate fi reținută. Încuviințare dată fără condițiile legale.</p>
        <h4>Clauze abuzive</h4>
        <p>Când titlul este un contract de credit cu un consumator, art. 713 alin. (2) permite apărări de fond. Aici intră și clauzele abuzive din Legea nr. 193/2000. Le legi de suma concretă din somație. O invocare generală nu ajută. Detalii la <a href="/avocat-clauze-abuzive/">avocat clauze abuzive</a>.</p>'''
S6='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura contestației pas cu pas</h2>
        <p>Procedura are patru pași: verifici termenul din art. 715, alegi motivele, redactezi cererea după art. 716 și art. 194 și o depui la instanța de executare. Dacă executarea continuă, ceri în aceeași cerere și suspendarea. Instanța judecă urgent, iar hotărârea se atacă doar cu apel. Ansamblul etapelor executării îl găsești la <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>
        <h3>Redactarea contestației</h3>
        <p>Art. 716 cere aceleași condiții de formă ca la cererea de chemare în judecată (art. 194): părțile, obiectul și valoarea, motivele de fapt și de drept, probele, semnătura. Indici numărul dosarului de executare și actele contestate. Întâmpinarea creditorului este obligatorie. Dacă nu locuiești în localitatea instanței, îți poți alege acolo un domiciliu procesual.</p>
        <h3>Instanța competentă</h3>
        <p>Regula este instanța de executare (art. 714 alin. (1)). Potrivit art. 651, aceasta este judecătoria în a cărei circumscripție se află domiciliul sau sediul debitorului la data sesizării executorului. Contestația la titlu privind o hotărâre se depune la instanța care a pronunțat-o (art. 714 alin. (3)). La urmărirea imobilelor din raza altei curți de apel, contestația se poate depune și la judecătoria locului imobilului (art. 714 alin. (2)). Detalii practice: <a href="/unde-se-depune-contestatia-la-executare/">unde se depune contestația la executare</a>.</p>
        <h3>Documentele necesare</h3>
        <ul class="chk">
          <li>somația, încheierea de încuviințare și adresa de poprire, cu plicul sau dovada comunicării;</li>
          <li>titlul executoriu și procesul-verbal de cheltuieli;</li>
          <li>dovezile de plată și dovada taxei de timbru.</li>
        </ul>
        <h4>Judecata contestației</h4>
        <p>Art. 717: instanța cere executorului copii certificate de pe dosar. Părțile sunt citate în termen scurt. Contestația se judecă urgent și cu precădere. Art. 718: hotărârea se atacă numai cu apel. Art. 720: dacă admite, instanța poate anula sau îndrepta actul, anula ori înceta executarea sau lămuri titlul. Dacă respinge, contestatorul poate fi obligat la despăgubiri, iar la rea-credință, și la o amendă judiciară de la 1.000 la 7.000 lei (art. 720 alin. (3)).</p>'''
S7='''        <span class="eyebrow">Suspendare</span>
        <h2>Suspendarea executării silite</h2>
        <p>Contestația nu oprește executarea. Pentru asta ceri <a href="/amanare-executare-silita/">suspendarea executării silite</a>, odată cu contestația sau separat, pentru motive temeinice (art. 719). Plătești o cauțiune calculată pe o grilă fixă din lege, plus o taxă de 50 lei. În cazuri urgente, poți obține o suspendare provizorie până se judecă cererea de suspendare.</p>
        <h3>Cum se cere suspendarea</h3>
        <p>Formulezi un capăt de cerere separat sau o cerere distinctă. Arăți ce pierzi dacă executarea continuă. Instanța decide prin încheiere, cu citarea părților. Încheierea se atacă separat cu apel, în 5 zile.</p>
        <h3>Condiții pentru suspendare</h3>
        <p>Cauțiunea din art. 719 alin. (2) se raportează la valoarea obiectului contestației:</p>
        <ul class="chk">
          <li>până la 10.000 lei: 10%;</li>
          <li>peste 10.000 lei: 1.000 lei plus 5% din ce depășește 10.000 lei;</li>
          <li>peste 100.000 lei: 5.500 lei plus 1% din ce depășește 100.000 lei;</li>
          <li>peste 1.000.000 lei: 14.500 lei plus 0,1% din ce depășește 1.000.000 lei.</li>
        </ul>
        <p>Obiect neevaluabil în bani: 1.000 lei. Fără cauțiune, suspendarea e obligatorie dacă titlul nu e executoriu, dacă a fost declarat fals în primă instanță sau dacă dovedești cu înscris autentic o amânare de la creditor.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Executorul urmărește 40.000 lei. Cauțiunea: 1.000 lei + 5% × 30.000 lei = 2.500 lei. La 8.000 lei, cauțiunea ar fi 800 lei. La 250.000 lei: 5.500 lei + 1% × 150.000 lei = 7.000 lei.</p>
          <span class="formula">40.000 → 1.000 + 5% × 30.000 = 2.500 lei · 8.000 → 10% = 800 lei · 250.000 → 5.500 + 1% × 150.000 = 7.000 lei</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>
        <h4>Efectele suspendării</h4>
        <p>Executorul nu mai face acte noi până la soluționarea contestației. Încheierea i se comunică din oficiu. Suspendarea nu desființează actele deja făcute. Dacă pierzi contestația, cauțiunea rămâne indisponibilizată pentru despăgubirile creditorului.</p>
        <p>Contestația, suspendarea și negocierea cu creditorul nu se exclud. Comparația de mai jos te ajută să alegi.</p>
        <div class="tbl wide"><table>
          <thead><tr><th>Criteriu</th><th>Contestația la executare</th><th>Suspendarea executării</th><th>Negocierea cu creditorul</th></tr></thead>
          <tbody>
            <tr><td>Scop</td><td>Anulează actele nelegale</td><td>Oprește temporar executarea</td><td>Acord de plată sau eșalonare</td></tr>
            <tr><td>Cost</td><td>Taxă de cel mult 1.000 lei</td><td>Taxă 50 lei + cauțiune</td><td>Fără taxe judiciare</td></tr>
            <tr><td>Durată</td><td>Luni, plus apelul</td><td>Mai scurtă, se judecă urgent</td><td>Depinde de creditor</td></tr>
            <tr><td>Șanse</td><td>Depind de termen și acte</td><td>Depind de motive și cauțiune</td><td>Depind de poziția creditorului</td></tr>
            <tr><td>Avantaj</td><td>Rezolvă legalitatea</td><td>Protejează salariul sau casa</td><td>Evită procesul</td></tr>
            <tr><td>Dezavantaj</td><td>Nu oprește singură executarea</td><td>Nu rezolvă fondul</td><td>Datoria rămâne</td></tr>
            <tr><td>Când o alegi</td><td>Există vicii de legalitate</td><td>Executarea produce pagube urgente</td><td>Datoria e reală și clară</td></tr>
          </tbody>
        </table></div>
'''+fig(IMG2,'contestația la executare cod procedură civilă — cauțiunea din art. 719 pentru 8.000, 40.000 și 250.000 lei','Cauțiunea pentru suspendare: 3 calcule')
S8='''        <span class="eyebrow">Practică</span>
        <h2>Practica judiciară și jurisprudență</h2>
        <p>Instanțele aplică strict termenele din art. 715 și limitele din art. 713. Contestațiile admise se sprijină, de regulă, pe acte: dovada comunicării, calculul sumei, titlul lipsă. Practica locală diferă de la o judecătorie la alta. De aceea, o hotărâre favorabilă nu garantează rezultatul în alt dosar.</p>
        <h3>Hotărâri relevante</h3>
        <p>Hotărâri românești concrete poți căuta pe portal.just.ro, după număr de dosar și instanță. La nivel european, CJUE a decis în cauza C-725/19 Impuls Leasing România (17 mai 2022) că instanța de executare trebuie să poată verifica clauzele abuzive din contractul-titlu.</p>
        <h3>Contestații admise de instanțe</h3>
        <p>Cel mai des: prescripția dreptului de a executa, cheltuieli nejustificate, poprire peste limite, creditor fără calitate dovedită.</p>
        <h4>Strategii juridice eficiente</h4>
        <p>Contestația câștigă când are un motiv principal clar, dovedit cu un act. Zece motive slabe îl ascund pe cel bun.</p>
        <div class="note dark"><b>Poziția juridică.</b> Prima verificare este data comunicării, nu fondul datoriei. Termenul din art. 715 decide dacă instanța mai ascultă restul. Al doilea pas este o cerere de suspendare cu cauțiunea calculată corect, ca executarea să nu se termine înaintea procesului.</div>'''
S9='''        <span class="eyebrow">Legislație</span>
        <h2>Legislație aplicabilă</h2>
        <p>Baza este Codul de procedură civilă republicat (Legea nr. 134/2010), Cartea a V-a, capitolul despre contestația la executare, art. 712–720. Se aplică împreună cu art. 651 (instanța de executare), art. 181 (calculul termenelor), art. 194 (cuprinsul cererii) și art. 723 și următoarele (întoarcerea executării). Taxele vin din OUG nr. 80/2013, art. 10.</p>
        <h3>Codul de procedură civilă</h3>
        <div class="tbl wide"><table>
          <thead><tr><th>Articol</th><th>Ce spune</th><th>Ce înseamnă pentru tine</th></tr></thead>
          <tbody>
            <tr><td>Art. 712</td><td>Obiectul: executarea, încheierile, orice act; lămurirea titlului</td><td>Poți ataca orice act al executorului</td></tr>
            <tr><td>Art. 713</td><td>Condiții de admisibilitate</td><td>La hotărâri, nu rediscuți procesul</td></tr>
            <tr><td>Art. 714 + 651</td><td>Instanța competentă: instanța de executare</td><td>Judecătoria de la domiciliul tău la data sesizării executorului</td></tr>
            <tr><td>Art. 715 + 181</td><td>Termene: 15 zile; contestația la titlu, oricând în termenul de prescripție</td><td>Numeri pe zile libere de la primirea actului</td></tr>
            <tr><td>Art. 716 + 194</td><td>Forma cererii de chemare în judecată; întâmpinare obligatorie</td><td>Cerere scrisă, motivată, cu probe</td></tr>
            <tr><td>Art. 717</td><td>Judecată urgentă, cu precădere</td><td>Termene scurte în instanță</td></tr>
            <tr><td>Art. 718</td><td>Calea de atac: numai apelul</td><td>Nu există recurs</td></tr>
            <tr><td>Art. 719</td><td>Suspendarea, cu cauțiune pe grilă</td><td>Plătești cauțiunea ca să oprești executarea</td></tr>
            <tr><td>Art. 720</td><td>Soluțiile: anulare, îndreptare, încetare, lămurire</td><td>Știi ce poți cere în petit</td></tr>
            <tr><td>Art. 723 și urm.</td><td>Întoarcerea executării</td><td>Recuperezi ce s-a executat nelegal</td></tr>
          </tbody>
        </table></div>
        <h3>Interpretarea art. 711 și 715</h3>
        <p>Fostul art. 711 este azi art. 712, iar fostul art. 714 este azi art. 715. O trimitere veche arată un model copiat. Folosește numerotarea republicată.</p>
        <h4>Comparație: executarea civilă și executarea fiscală</h4>
        <p>Executarea făcută de ANAF sau de primărie nu urmează art. 712–720 CPC, ci Codul de procedură fiscală (Legea nr. 207/2015). Executorul este fiscal, nu judecătoresc. Contestația se depune la instanța judecătorească competentă, iar termenul este, de regulă, tot de 15 zile. Verifică instanța și momentul de început al termenului cu un avocat înainte de a depune.</p>'''
S10='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente în contestația la executare</h2>
        <p>Cele mai multe contestații se pierd pe formă, nu pe fond. Debitorul depune după 15 zile, nu atașează actele sau copiază un model cu articole vechi. Altă greșeală frecventă: crede că simpla depunere a contestației oprește executarea. Fără cererea de suspendare și fără cauțiune, executorul merge mai departe.</p>
        <h3>Depunerea tardivă</h3>
        <p>Contestația depusă după termen este respinsă ca tardivă. Instanța nu mai analizează motivele.</p>
        <h3>Lipsa probelor</h3>
        <p>Invoci prescripția fără titlu și fără dovezi de plată. Motivul nu poate fi verificat.</p>
        <h4>Contestație incompletă</h4>
        <p>Lipsesc actul atacat, numărul dosarului de executare, valoarea sau dovada taxei. Instanța cere completarea, iar timpul curge.</p>'''
S11='''        <span class="eyebrow">Costuri</span>
        <h2>Cât costă contestația la executare</h2>
        <p>Costul are trei părți: taxa de timbru, cauțiunea pentru suspendare, dacă o ceri, și onorariul avocatului. Potrivit art. 10 din OUG nr. 80/2013, contestația propriu-zisă se taxează la valoarea bunurilor urmărite sau a debitului, fără a depăși 1.000 lei. Cererea de suspendare costă 50 lei. Dacă invoci și motive de fond (art. 712 alin. (2)), taxa se calculează după regulile generale. Pentru un calcul pe dosarul tău, vezi <a href="/unde-se-depune-contestatia-la-executare/">unde se depune contestația la executare</a>.</p>'''
S12='''        <span class="eyebrow">Model</span>
        <h2>Model simplificat de contestație la executare</h2>
        <p>Un model te ajută să nu uiți elementele obligatorii din art. 194 CPC, la care trimite art. 716. Nu înlocuiește analiza dosarului. Structura de mai jos este orientativă. O adaptezi la actele tale, la termenul din art. 715 și la motivele reale. Nu depune modelul fără aceste completări.</p>
        <h3>Structura modelului</h3>
        <ol class="num">
          <li>Instanța: „Către Judecătoria …”.</li>
          <li>Contestatorul și intimatul (creditorul), cu date de identificare.</li>
          <li>Obiectul: actele contestate, nr. dosarului de executare, valoarea.</li>
          <li>Cererea de suspendare, ca petit distinct.</li>
          <li>Motivele de fapt și de drept: art. 712–720 CPC și normele încălcate.</li>
          <li>Probele: înscrisuri, dosarul de executare.</li>
          <li>Anexe, dovada taxei, semnătura.</li>
        </ol>
        <h4>Exemplu orientativ</h4>
        <div class="quote">„Formulez contestație la executare împotriva somației din … și a popririi din …, emise în dosarul de executare nr. …, și solicit anularea acestora, precum și suspendarea executării până la soluționarea contestației.”</div>'''
S13='''        <span class="eyebrow">Urgent</span>
        <h2>Ce trebuie să faci dacă primești acte de executare</h2>
        <p>Păstrezi actele împreună cu plicul, notezi data primirii și calculezi termenul de 15 zile din art. 715. Ceri copia dosarului de executare și verifici titlul, suma și cheltuielile. Dacă executarea îți blochează contul sau salariul, pregătești și cererea de suspendare, cu cauțiunea din art. 719.</p>
        <h3>Pașii urgenți</h3>
        <ul class="chk">
          <li>Scrie data primirii pe fiecare act.</li>
          <li>Cere executorului dosarul complet.</li>
          <li>Calculează cauțiunea după grila din art. 719.</li>
        </ul>
        <h4>Recomandări finale</h4>
        <p>Nu aștepta ultima zi. La sume mari, un <a href="/avocat-contestatie-executare-silita/">avocat contestație executare silită</a> verifică termenul și motivele înainte să depui.</p>'''
S14='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Așază actele primite de la executor în ordinea datelor și notează data de pe plic.</li>
          <li>Numără 15 zile libere de la data primirii și scrie în calendar ultima zi.</li>
          <li>Calculează cauțiunea pentru suma urmărită și verifică dacă poți consemna banii.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Ce prevede art. 711 CPC?","În numerotarea veche, art. 711 reglementa obiectul contestației. După republicarea din 2015, același text este art. 712: poți contesta executarea, încheierile executorului și orice act de executare."),
("Care este termenul din art. 715 CPC?","15 zile, calculate pe zile libere. Curg de la data la care ai luat cunoștință de act, de la comunicarea popririi sau de la primirea somației."),
("Pot contesta executarea după 15 zile?","De regulă, nu. Excepție: contestația la titlu, care se poate face înăuntrul termenului de prescripție a executării. Verifică întâi data reală a comunicării."),
("Ce acte pot fi contestate?","Executarea însăși, încheierile executorului, somația, poprirea, procesul-verbal de cheltuieli, publicația de vânzare și încheierea de încuviințare."),
("Cât costă contestația la executare?","Taxa se calculează după valoarea urmărită, dar nu depășește 1.000 lei. Suspendarea: 50 lei taxă, plus cauțiunea."),
("Pot suspenda executarea silită?","Da, prin cerere motivată, odată cu contestația sau separat, și cu plata cauțiunii (art. 719). În urgență, poți cere suspendarea provizorie."),
("Este obligatoriu avocatul?","Nu. Poți depune contestația singur. Avocatul ajută la calculul termenului, alegerea motivelor și cauțiune."),
("Ce șanse am să câștig contestația?","Depind de acte. Prescripția, lipsa titlului sau cheltuielile nejustificate, dovedite cu înscrisuri, dau șanse reale. Nimeni nu poate garanta rezultatul.")]
P=dict(slug='contestatia-la-executare-cod-procedura-civila',crumb='Contestația la executare în Codul de procedură civilă',
 title='Contestația la executare, Cod procedură civilă: art. 712–720',
 desc='Contestația la executare în Codul de procedură civilă, articol cu articol: obiectul (art. 712), termenele (art. 715), suspendarea și cauțiunea (art. 719).',
 nav='#calculator|Cauțiunea art. 719;#art-712|Art. 712;#art-715|Art. 715;#suspendare|Suspendarea;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Cod procedură civilă · art. 712–720',
  h1='Contestația la executare în Codul de procedură civilă: <span class="accent">art. 712 și termenele din art. 715</span>',
  lead=['Ai găsit pe internet un model care trimite la „art. 711 CPC”. L-ai completat și vrei să-l depui. Între timp, banca ți-a blocat contul, iar somația are deja o săptămână.',
        'Aici afli ce spune <strong>fiecare articol din capitolul despre contestația la executare</strong>, art. 712–720 din Codul de procedură civilă republicat. Vezi ce înseamnă concret pentru tine: ce poți ataca, în ce termen, la ce instanță, cât costă suspendarea și ce poate hotărî judecătorul.'],
  meta2='Art. 712–720 CPC, forma republicată',cta='Calculează cauțiunea din art. 719',
  answer='Contestația la executare este cererea prin care ceri instanței să verifice legalitatea executării silite. Temeiul este art. 712 CPC. Poți ataca executarea însăși, încheierile executorului și orice act de executare. Termenul general este de 15 zile (art. 715). Contestația nu oprește singură executarea: pentru asta ceri suspendarea, cu cauțiune (art. 719).',
  opts=[('Art. 712','obiectul contestației'),('Art. 715','termenul de 15 zile')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('capitol','Ce este conform CPC',S2),('art-712','Art. 711 sau 712',S3),('art-715','Art. 715 și termenele',S4),('motive','Motive',S5),('procedura','Procedura',S6),('suspendare','Suspendarea',S7),('practica','Practica judiciară',S8),('legislatie','Legislație',S9),('greseli','Greșeli frecvente',S10),('costuri','Costuri',S11),('model','Model',S12),('urgent','Ce faci urgent',S13),('azi','Ce faci azi',S14)],
 faq=faq,faq_h2='Întrebări frecvente despre contestația la executare în CPC',
 contact=dict(h2='Ce articol se aplică în cazul tău?',lead='Trimite-ne somația, adresa de poprire și titlul. Îți spunem în ce termen ești, ce articol se aplică și cât ar fi cauțiunea. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum folosești Codul de procedură civilă pentru contestație',steps=[('Verifici termenul','15 zile libere, după art. 715 și art. 181 CPC.'),('Alegi motivele','Prescripție, titlu, erori procedurale, clauze abuzive (art. 712–713).'),('Redactezi cererea','După art. 716 și art. 194 CPC și o depui la instanța de executare.'),('Ceri suspendarea','Odată cu contestația, cu cauțiunea din art. 719.')]),
 knows=['Executare silită','Cod procedură civilă','Contestație la executare','Suspendarea executării'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/contestatia-la-executare-cod-procedura-civila.src.html','w',encoding='utf-8').write(build(P))
