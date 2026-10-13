import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='motivele-pentru-anularea-executarii-silite.webp'; IMG2='de-la-depunere-la-decizia-instantei.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Ce obiect alegi pentru contestație și <span class="accent">cât blochezi cu cauțiunea</span></h2></div>
      <p>Cauțiunea pentru suspendare se calculează la valoarea obiectului contestației. Dacă datoria este reală și contești doar cheltuielile de executare, suma blocată e mult mai mică. Compară cele două variante.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Suma urmărită</div>
          <div class="field"><label for="f-t">Total urmărit (lei)</label><div class="inp"><input id="f-t" inputmode="numeric" placeholder="60000"></div></div>
          <div class="field"><label for="f-c">Din care, cheltuieli de executare contestate (lei)</label><div class="inp"><input id="f-c" inputmode="numeric" placeholder="6000"></div></div>
          <div class="field full"><label for="f-d">Data primirii somației sau a popririi (opțional)</label><div class="inp"><input type="date" id="f-d"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: 60.000 lei, din care 6.000</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt" id="c-a"><span class="k">Contești toată executarea</span><span class="v" id="o-a">—</span><span class="s" id="o-as">Cauțiune la valoarea totală.</span></div>
            <div class="opt" id="c-b"><span class="k">Contești doar cheltuielile</span><span class="v" id="o-b">—</span><span class="s" id="o-bs">Cauțiune la valoarea cheltuielilor.</span></div>
            <div class="opt full" id="c-r"><span class="k">Diferență de sumă blocată</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Alegerea corectă a obiectului poate reduce mult cauțiunea.</span></div>
            <div class="opt full" id="c-t"><span class="k">Ultima zi de depunere</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">15 zile libere de la primirea actului (art. 715 și art. 181 CPC).</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne actele spre analiză</a>
          <span class="disc">Calcul orientativ, după grila din art. 719 alin. (2) CPC. Cauțiunea o stabilește instanța. Dacă ultima zi cade sâmbătă sau duminică, termenul se prelungește până luni; sărbătorile legale nu sunt luate în calcul aici. Depune cu cel puțin o zi înainte. Taxa de timbru și cererea de suspendare (50 lei) se adaugă.</span>
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
    var t=num('f-t'),c=num('f-c');
    if(t>0){var a=caut(t);$('o-a').textContent=lei(a);$('o-as').textContent='La '+lei(t)+' contestați.';
      if(c>0&&t>=c){var b=caut(c);$('o-b').textContent=lei(b);$('o-bs').textContent='La '+lei(c)+' contestați.';$('o-r').textContent=lei(a-b);cls('c-r','ok');$('o-rs').textContent=b>0?'Cauțiunea e de '+(a/b).toFixed(1).replace('.',',')+' ori mai mică. Alege obiectul în funcție de ce contești cu adevărat.':'—'}
      else{$('o-b').textContent='—';$('o-bs').textContent='Introdu cheltuielile contestate.';$('o-r').textContent='—';cls('c-r');$('o-rs').textContent='Alegerea corectă a obiectului poate reduce mult cauțiunea.'}
    }else{$('o-a').textContent='—';$('o-b').textContent='—';$('o-r').textContent='—';cls('c-r');$('o-as').textContent='Cauțiune la valoarea totală.';$('o-bs').textContent='Cauțiune la valoarea cheltuielilor.'}
    var d=$('f-d').value;
    if(d){var e=dt(d);e.setUTCDate(e.getUTCDate()+16);var w=e.getUTCDay();if(w===6)e.setUTCDate(e.getUTCDate()+2);else if(w===0)e.setUTCDate(e.getUTCDate()+1);
      $('o-t').textContent=fmt(e)+' ('+ZI[e.getUTCDay()]+')';cls('c-t','alert');$('o-ts').textContent='15 zile libere după '+fmt(dt(d))+' (art. 715 și art. 181 CPC), cu prelungire la prima zi lucrătoare.'}
    else{$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='15 zile libere de la primirea actului (art. 715 și art. 181 CPC).'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-t','f-c','f-d'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-t').value='60000';$('f-c').value='6000';$('f-d').value='2026-10-12';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Contestație la executare: răspuns rapid</h2>
        <p>Contestația la executare este cererea prin care ceri judecătoriei să verifice dacă executarea silită pornită împotriva ta respectă legea (art. 712 CPC). Termenul general este de 15 zile. Depunerea nu oprește singură executarea. Pentru asta ceri, separat sau în aceeași cerere, suspendarea. Șansele depind de motive și de acte.</p>
        <ul class="chk">
          <li><strong>Ce este:</strong> controlul instanței asupra executării.</li>
          <li><strong>Când o depui:</strong> de regulă, în 15 zile de la somație, poprire sau actul contestat.</li>
          <li><strong>Ce șanse ai:</strong> bune cu un viciu dovedit, slabe când doar nu poți plăti.</li>
        </ul>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce înseamnă contestația la executare</h2>
        <p>Este calea prin care ataci executarea silită însăși, încheierile executorului sau orice act de executare. Poți contesta și refuzul executorului de a face un act. O variantă aparte este contestația la titlu: ceri lămurirea înțelesului, întinderii sau aplicării titlului executoriu. Contestația poate fi făcută de debitor, dar și de alte persoane vătămate prin executare.</p>
        <h3>Ce este executarea silită</h3>
        <p>Executarea silită este plata obținută cu forța, prin executorul judecătoresc. Creditorul are nevoie de un titlu executoriu (art. 632 CPC): o hotărâre, un contract de credit, un bilet la ordin. Executorul obține încuviințarea instanței și îți trimite somația. Urmează poprirea, sechestrul sau vânzarea. Etapele complete le găsești în ghidul despre <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>
        <h3>Când apare dreptul la contestație</h3>
        <p>Dreptul apare când există un act de executare care te vatămă:</p>
        <ul class="chk">
          <li>ai primit încheierea de încuviințare și somația;</li>
          <li>banca ți-a blocat contul sau angajatorul reține din salariu;</li>
          <li>procesul-verbal de cheltuieli are sume pe care nu le înțelegi;</li>
          <li>executorul a pus sechestru pe mașină sau pe casă.</li>
        </ul>
        <h4>Exemple concrete</h4>
        <p>Situații tipice (anonimizate):</p>
        <div class="roles">
          <div><b>Credit de consum vechi</b>Recuperatorul reia executarea la ani după ultimul act. Se verifică prescripția.</div>
          <div><b>Poprire pe pensie</b>Se reține mai mult decât permite legea pentru veniturile periodice.</div>
          <div><b>Terț proprietar</b>Executorul sechestrează un autoturism înmatriculat pe numele fratelui debitorului.</div>
        </div>'''
S3='''        <span class="eyebrow">Motive</span>
        <h2>Motive pentru contestație la executare</h2>
        <p>Motivele frecvente sunt prescripția, lipsa unui titlu executoriu valabil, erorile de procedură, clauzele abuzive din contractul-titlu și sumele greșite. Contează natura titlului. Dacă titlul este o hotărâre judecătorească, nu poți relua discuția despre datorie. Dacă este un contract, poți invoca și apărări de fond (art. 713 CPC).</p>
        <h3>Prescripția datoriei</h3>
        <p>Atenție la confuzie. În contestație invoci, de regulă, prescripția dreptului de a obține executarea silită (art. 706 CPC). Termenul general este de 3 ani, iar pentru titlurile privind drepturi reale, de 10 ani. Se poate întrerupe, de exemplu printr-o plată parțială sau un act de executare. Prescripția datoriei înseși contează mai ales când titlul este un contract. Executorul nu aplică prescripția din oficiu. O invoci tu.</p>
        <h3>Lipsa titlului executoriu</h3>
        <p>Fără titlu executoriu nu există executare. Verifici dacă actul are această putere și dacă suma urmărită rezultă din el. O hotărâre care nu este încă executorie nu poate fi executată.</p>
        <h3>Erori procedurale</h3>
        <ul class="chk">
          <li>somația sau încheierea de încuviințare nu ți-au fost comunicate;</li>
          <li>bunurile urmărite sunt, potrivit legii, neurmăribile;</li>
          <li>poprirea depășește limitele pentru salariu și pensie (art. 729 CPC);</li>
          <li>cheltuielile de executare (art. 670 CPC) nu sunt justificate.</li>
        </ul>
        <h3>Clauze abuzive</h3>
        <p>Când titlul executoriu este chiar contractul de credit, poți invoca în contestație că o clauză este abuzivă. În cauza C-725/19 Impuls Leasing România (17 mai 2022), CJUE a cerut ca instanța de executare să poată verifica astfel de clauze. Detalii la <a href="/avocat-clauze-abuzive/">avocat clauze abuzive</a>.</p>
        <h4>Alte motive legale</h4>
        <ul class="chk">
          <li>datoria a fost plătită, integral sau parțial, înainte de executare;</li>
          <li>creditorul ți-a acordat o amânare sau un termen de plată;</li>
          <li>bunul urmărit aparține unui terț.</li>
        </ul>
'''+fig(IMG1,'contestație la executare — motive: prescripție, titlu, procedură, sume','Motivele pentru anularea executării silite')
S4='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura contestație la executare pas cu pas</h2>
        <p>Procedura are cinci pași: obții dosarul de executare, calculezi termenul, redactezi cererea, o depui la judecătoria competentă și plătești taxa. Instanța cere apoi executorului copii certificate ale dosarului. Părțile sunt citate în termen scurt. Judecata se face de urgență și cu precădere (art. 717 CPC).</p>
        <h3>Redactarea contestației</h3>
        <p>Cererea respectă art. 194 CPC: părțile, obiectul și valoarea, motivele de fapt și de drept, probele, semnătura. Indici exact actele contestate. Anexezi actele de la executor, titlul, dovezile de plată și dovada taxei.</p>
        <h3>Unde se depune</h3>
        <p>Regula este instanța de executare. Aceasta este judecătoria în circumscripția căreia se afla domiciliul sau sediul debitorului la data sesizării executorului (art. 651 și art. 714 CPC). Sediul executorului nu contează. Excepțiile, inclusiv contestația la titlu, sunt explicate în ghidul <a href="/unde-se-depune-contestatia-la-executare/">unde se depune contestația la executare</a>.</p>
        <h3>Termenul de 15 zile</h3>
        <p>Termenul curge diferit, după actul atacat (art. 715 CPC):</p>
        <ul class="chk">
          <li><strong>Executarea însăși:</strong> de la primirea încheierii de încuviințare sau a somației.</li>
          <li><strong>Poprirea:</strong> de la comunicarea ei, dar pe salariu sau pensie cel târziu de la prima reținere.</li>
          <li><strong>Un act de executare:</strong> de la data când ai aflat de el.</li>
          <li><strong>Contestația la titlu:</strong> oricând, cât timp nu s-a prescris dreptul de a cere executarea.</li>
        </ul>
        <p>Termenul se calculează pe zile libere (art. 181 CPC): nu se socotesc prima și ultima zi. Dacă ultima zi e nelucrătoare, termenul se prelungește până în prima zi lucrătoare. Exemple cu date găsești în ghidul despre <a href="/termen-contestatie-la-executare/">termen contestație la executare</a>.</p>
        <h4>Judecata</h4>
        <ol class="num">
          <li>Instanța fixează primul termen și cere executorului dosarul.</li>
          <li>Creditorul depune întâmpinare.</li>
          <li>Se judecă, de regulă înaintea fondului, cererea de suspendare.</li>
          <li>Se administrează probele, inclusiv o eventuală expertiză contabilă.</li>
          <li>Hotărârea se atacă, în principiu, numai cu apel.</li>
        </ol>'''
S5='''        <span class="eyebrow">Suspendare</span>
        <h2>Suspendarea executării silite</h2>
        <p>Contestația nu oprește executarea. Dacă poprirea continuă sau se apropie vânzarea, ceri suspendarea (art. 719 CPC). Instanța o acordă doar pentru motive temeinice și, de regulă, după ce plătești o cauțiune. În urgențe, există și suspendarea provizorie. Detalii în ghidul despre <a href="/amanare-executare-silita/">suspendarea executării silite</a>.</p>
        <h3>Cum poți obține suspendarea</h3>
        <p>O ceri odată cu contestația sau separat. Taxa este de 50 lei. Plătești cauțiunea și depui dovada. Instanța decide prin încheiere, cu citarea părților, atacabilă cu apel în 5 zile. În urgență, cu cauțiunea plătită, instanța poate dispune suspendarea provizorie fără citare.</p>
        <h3>Condiții legale</h3>
        <p>Cauțiunea se calculează la valoarea obiectului contestației:</p>
        <ul class="chk">
          <li>până la 10.000 lei: 10%;</li>
          <li>între 10.000 și 100.000 lei: 1.000 lei plus 5% din ce depășește 10.000 lei;</li>
          <li>între 100.000 și 1.000.000 lei: 5.500 lei plus 1% din ce depășește 100.000 lei;</li>
          <li>peste 1.000.000 lei: 14.500 lei plus 0,1% din ce depășește 1.000.000 lei.</li>
        </ul>
        <p>Dacă obiectul nu e evaluabil în bani, cauțiunea este de 1.000 lei. Suspendarea e obligatorie și fără cauțiune când titlul nu este executoriu, când a fost declarat fals în primă instanță sau când ai act autentic de amânare de la creditor.</p>
        <h4>Efecte</h4>
        <p>Executarea se oprește în stadiul în care se află. Încheierea se comunică din oficiu executorului. Banii deja reținuți nu se întorc prin suspendare, ci prin anularea executării și întoarcerea ei.</p>'''
S6='''        <span class="eyebrow">Durată</span>
        <h2>Cât durează contestația la executare</h2>
        <p>Legea nu fixează o durată. Spune doar că judecata se face de urgență și cu precădere. Durata reală depinde de încărcarea instanței, de cât de repede trimite executorul dosarul și de probe. Expertiza și apelul adaugă timp. Suspendarea se judecă, de regulă, mai repede decât fondul.</p>
        <h3>Durata procesului</h3>
        <p>Până la primul termen: comunicarea cererii, întâmpinarea și solicitarea dosarului de la executor. Urmează suspendarea, probele, hotărârea și, eventual, apelul.</p>
        <h3>Factori care influențează durata</h3>
        <ul class="chk">
          <li>dosarul de executare ajunge târziu sau incomplet;</li>
          <li>se cere expertiză pentru calculul debitului;</li>
          <li>contestația se depune la instanța necompetentă și dosarul este trimis mai departe.</li>
        </ul>
        <h4>Exemple reale</h4>
        <p>Situații tipice (anonimizate): o contestație doar pentru cheltuieli, cu înscrisuri, durează de obicei mai puțin decât una pentru prescripție, unde se verifică toate actele anterioare. Dosarul complet de la început scurtează procesul mai mult decât orice cerere de urgentare.</p>
'''+fig(IMG2,'contestație la executare — etapele procedurii, de la depunere la apel','De la depunere la decizia instanței')
S7='''        <span class="eyebrow">Costuri</span>
        <h2>Costuri contestație executare</h2>
        <p>Costul are trei părți: taxa de timbru, cauțiunea pentru suspendare, dacă o ceri, și onorariul avocatului. Taxa pentru contestația la executare propriu-zisă depinde de valoarea urmărită, dar nu trece de 1.000 lei. Cererea de suspendare costă 50 lei. Cauțiunea este cea mai mare sumă, dar nu este o taxă: rămâne blocată pe durata procesului.</p>
        <h3>Taxa de timbru</h3>
        <p>Potrivit art. 10 din OUG nr. 80/2013, contestația propriu-zisă se taxează la valoarea bunurilor urmărite sau a debitului, dacă e mai mic, fără a depăși 1.000 lei. Dacă invoci și motive de fond (art. 712 alin. (2) CPC), taxa se calculează după regulile generale. Cere avocatului calculul exact pentru dosarul tău.</p>
        <h3>Onorariu avocat</h3>
        <p>Onorariul depinde de actele contestate, de suspendare, de expertiză și de apel. Se stabilește în contract, după ce avocatul vede actele. Prima analiză o facem gratuit. Cum lucrează un avocat pe astfel de dosare afli în pagina <a href="/avocat-contestatie-executare-silita/">avocat contestație executare silită</a>.</p>
        <h4>Cost total estimat</h4>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Ești urmărit pentru 60.000 lei. Din ei, 6.000 lei sunt cheltuieli de executare pe care le consideri nejustificate. Dacă contești toată executarea, cauțiunea pentru suspendare este 1.000 lei + 5% × (60.000 − 10.000) = 3.500 lei.</p>
          <p>Dacă datoria e reală și contești doar cheltuielile, obiectul contestației este 6.000 lei, iar cauțiunea, 10% × 6.000 = 600 lei. Plus 50 lei taxa pentru suspendare și taxa de timbru a contestației, de cel mult 1.000 lei. Alegerea corectă a obiectului poate reduce de aproape șase ori suma blocată.</p>
          <span class="formula">1.000 + 5% × 50.000 = 3.500 lei · 10% × 6.000 = 600 lei · 3.500 / 600 ≈ 5,8</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S8='''        <span class="eyebrow">Șanse</span>
        <h2>Șanse de câștig contestație executare</h2>
        <p>Șansele se judecă pe trei lucruri: un motiv recunoscut de lege, acte care îl dovedesc și termenul respectat. Prescripția documentată, plata dovedită sau lipsa comunicării sunt motive puternice. Nemulțumirea față de suma totală, fără calcul, este un motiv slab. Nimeni nu îți poate da un procent onest înainte să vadă dosarul.</p>
        <h3>Factori decisivi</h3>
        <ul class="chk">
          <li><strong>Prescripția:</strong> data ultimului act de executare și a ultimei plăți.</li>
          <li><strong>Dovezile:</strong> plicul, confirmarea de primire, extrasele, chitanțele.</li>
          <li><strong>Termenul:</strong> o contestație tardivă se respinge fără analiza motivelor.</li>
          <li><strong>Natura titlului:</strong> hotărâre judecătorească sau contract.</li>
        </ul>
        <h3>Estimare șanse</h3>
        <p>Nu dăm procente. Dăm o evaluare pe trepte: <strong>puternică</strong> (viciu clar, dovedit cu acte), <strong>discutabilă</strong> (motiv real, dar probe incomplete) sau <strong>slabă</strong> (fără temei juridic). În ultimul caz îți spunem direct și discutăm alte opțiuni.</p>
        <h4>Riscuri</h4>
        <p>Dacă pierzi, executarea continuă și poți plăti cheltuielile de judecată ale creditorului. La cerere, instanța poate acorda despăgubiri pentru întârziere. O contestație făcută cu rea-credință atrage și o amendă judiciară de la 1.000 la 7.000 lei (art. 720 alin. (3) CPC). Cauțiunea rămâne blocată pentru aceste sume.</p>'''
S9='''        <span class="eyebrow">Jurisprudență</span>
        <h2>Practica judiciară și jurisprudența</h2>
        <p>Jurisprudența arată ce motive trec în fața instanțelor. CJUE a întărit dreptul consumatorului de a invoca clauzele abuzive chiar în executare. Contestațiile admise privesc des prescripția, comunicarea actelor și cheltuielile de executare. Fiecare soluție depinde însă de actele din dosar.</p>
        <h3>Hotărâri relevante</h3>
        <p><strong>C-725/19 Impuls Leasing România (CJUE, 17 mai 2022):</strong> legislația care împiedică instanța de executare să verifice clauzele abuzive din contractul-titlu este contrară Directivei 93/13/CEE, când suspendarea în acțiunea separată cere o cauțiune descurajantă. Hotărâri românești concrete poți căuta pe portal.just.ro, după număr de dosar și instanță.</p>
        <h3>Contestații admise</h3>
        <p>Tipurile de cazuri care se repetă: executare prescrisă, somație necomunicată, onorariu de executor nejustificat, poprire peste limitele legale.</p>
        <h4>Strategii juridice eficiente</h4>
        <div class="note dark"><b>Poziția juridică.</b> Prima întrebare nu este „datorez sau nu?”, ci „ce act atac și de când curge termenul lui?”. Când primul termen a trecut, un act nou, precum o poprire recentă sau un proces-verbal de cheltuieli, poate redeschide discuția pentru acel act. Iar o contestație cu un singur motiv solid convinge mai mult decât una cu zece motive generale.</div>'''
S10='''        <span class="eyebrow">Legislație</span>
        <h2>Legislație aplicabilă</h2>
        <p>Baza este Codul de procedură civilă republicat: art. 712–720 pentru contestație și suspendare, art. 651 pentru instanța de executare, art. 706 pentru prescripție, art. 723 și următoarele pentru întoarcerea executării. Taxele vin din OUG nr. 80/2013. Datoriile către stat urmează Codul de procedură fiscală.</p>
        <h3>Codul de procedură civilă</h3>
        <p>Fiecare articol, explicat pe înțeles, îl găsești în ghidul <a href="/contestatia-la-executare-cod-procedura-civila/">contestația la executare în Codul de procedură civilă</a>.</p>
        <h3>Drepturile debitorului</h3>
        <ul class="chk">
          <li>să primească încheierea de încuviințare și somația;</li>
          <li>să păstreze partea protejată din salariu sau pensie;</li>
          <li>să conteste și să ceară suspendarea;</li>
          <li>să își recupereze banii dacă executarea este desființată.</li>
        </ul>
        <h4>Comparație interpretări</h4>
        <p>Executarea pornită de ANAF sau de primărie nu urmează aceleași reguli. Se aplică Codul de procedură fiscală (Legea nr. 207/2015), cu reguli proprii pentru contestație. Verifică termenul și instanța cu avocatul înainte de a depune.</p>'''
S11='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente în contestație</h2>
        <p>Cele mai multe contestații pierdute au aceleași cauze: termen depășit, lipsa dovezilor, cerere fără actul exact atacat, lipsa cererii de suspendare. Frecventă este și depunerea la instanța de lângă executor, în loc de cea de la domiciliul debitorului. Toate se evită cu o verificare în primele zile.</p>
        <h3>Depășirea termenului</h3>
        <p>Termenul nu se prelungește pentru că ai așteptat răspunsul creditorului. Repunerea în termen este o excepție: ceri și dovedești un motiv temeinic care te-a împiedicat.</p>
        <h3>Lipsa probelor</h3>
        <p>„Executarea e nelegală” nu este o probă. Instanța are nevoie de plic, confirmare de primire, extrase, chitanțe și calcul.</p>
        <h4>Contestație incompletă</h4>
        <p>Toate motivele existente se invocă în aceeași contestație. O a doua contestație pentru ele nu este admisibilă. Poți completa cererea cât timp termenul pentru acele motive curge.</p>'''
S12='''        <span class="eyebrow">Model</span>
        <h2>Model contestație la executare</h2>
        <p>Un model te ajută să nu uiți elementele obligatorii. Nu îți spune însă ce motiv ai și de când curge termenul. Folosește-l ca listă de verificare, nu ca text gata de copiat. Motivele generale, fără legătură cu dosarul, slăbesc contestația.</p>
        <h3>Structura model</h3>
        <ol class="num">
          <li>Instanța: Judecătoria … (instanța de executare).</li>
          <li>Contestator și intimat: numele, domiciliul sau sediul, CNP sau CUI.</li>
          <li>Obiectul: actele atacate, cu număr și dată, și valoarea contestată.</li>
          <li>Cererile: anularea actelor sau a executării, suspendarea, întoarcerea executării, cheltuielile de judecată.</li>
          <li>Motivele de fapt și de drept.</li>
          <li>Probele: înscrisuri, eventual expertiză.</li>
          <li>Anexele, dovada taxei, data și semnătura.</li>
        </ol>
        <h4>Exemplu simplificat</h4>
        <div class="quote">„Formulez contestație la executare împotriva executării silite din dosarul nr. … al BEJ …, a somației din … și a adresei de înființare a popririi din …. Solicit anularea acestora și a executării însăși, întrucât dreptul de a obține executarea silită s-a prescris. Solicit suspendarea executării până la soluționarea contestației și întoarcerea executării pentru sumele reținute.”</div>'''
S13='''        <span class="eyebrow">Urgent</span>
        <h2>Ce trebuie să faci urgent dacă ești executat silit</h2>
        <p>În primele zile păstrezi dovezile de comunicare, obții dosarul de la executor și alegi calea: contestația, plata sau negocierea. Nu plăti și nu semna nimic până nu verifici suma. O eșalonare semnată în grabă poate fi folosită ca recunoaștere a datoriei, iar recunoașterea întrerupe prescripția.</p>
        <h3>Pașii imediați</h3>
        <div class="tbl wide"><table>
          <thead><tr><th>Criteriu</th><th>Contestație la executare</th><th>Plata datoriei</th><th>Negocierea cu creditorul</th></tr></thead>
          <tbody>
            <tr><td>Metoda potrivită când</td><td>Executarea are vicii</td><td>Suma e reală și verificată</td><td>Plata integrală e grea</td></tr>
            <tr><td>Cost</td><td>Taxă de până la 1.000 lei, plus cauțiune dacă ceri suspendarea</td><td>Debitul plus cheltuielile de executare</td><td>Depinde de acord</td></tr>
            <tr><td>Durată</td><td>Luni, în funcție de instanță</td><td>Rapidă</td><td>Variabilă</td></tr>
            <tr><td>Șanse</td><td>Bune doar cu motiv și probe</td><td>Executarea se încheie sigur</td><td>Depind de creditor</td></tr>
            <tr><td>Avantaje</td><td>Poate anula executarea și aduce banii înapoi</td><td>Închide dosarul</td><td>Controlezi ratele și costurile</td></tr>
            <tr><td>Dezavantaje</td><td>Nu oprește singură executarea</td><td>Poți plăti sume nedatorate</td><td>Nu anulează actele nelegale</td></tr>
            <tr><td>Recomandare</td><td>Când ai un viciu dovedit</td><td>După verificarea sumei</td><td>Doar în scris, după analiza actelor</td></tr>
          </tbody>
        </table></div>
        <h4>Recomandări</h4>
        <p>Păstrează plicul și notează pe el data primirii. Verifică ce sumă a blocat banca și ce parte e protejată: detalii în ghidul despre <a href="/poprire-cont/">poprire cont</a>. Nu aștepta „să vezi ce se întâmplă”: termenul curge.</p>'''
S14='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Scrie data la care ai primit somația, adresa de poprire sau încheierea. Calculează a 15-a zi liberă.</li>
          <li>Cere executorului, în scris, copia dosarului de executare și calculul debitului.</li>
          <li>Pune deoparte titlul, dovezile de plată și extrasele, apoi cere o analiză juridică a actelor.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Ce este contestația la executare?","Cererea prin care instanța verifică legalitatea executării silite sau a unui act de executare."),
("Care este termenul legal?","De regulă, 15 zile, calculate pe zile libere. Curge de la somație, de la comunicarea popririi sau de la data când ai aflat de act. Contestația la titlu se poate face oricând, cât timp executarea nu s-a prescris."),
("Pot opri executarea silită?","Da, prin cererea de suspendare, nu prin simpla contestație. De regulă plătești o cauțiune. În urgențe poți cere suspendarea provizorie."),
("Cât durează procesul?","Nu există o durată fixă. Judecata e urgentă, dar probele și apelul adaugă timp."),
("Cât costă contestația?","Taxa de timbru la contestația propriu-zisă depinde de valoare, dar nu trece de 1.000 lei. Suspendarea costă 50 lei plus cauțiunea, calculată la valoarea contestată."),
("Ce șanse am să câștig?","Bune dacă ai un motiv legal dovedit cu acte și ai respectat termenul. Slabe dacă motivul este doar lipsa banilor."),
("Este obligatoriu avocatul?","Nu. Avocatul ajută însă la termen, la alegerea motivelor și la suspendare."),
("Ce se întâmplă dacă pierd?","Executarea continuă. Poți plăti cheltuielile de judecată ale creditorului. Hotărârea se poate ataca, de regulă, cu apel.")]
P=dict(slug='contestatie-la-executare',crumb='Contestație la executare',
 title='Contestație la executare: procedură, termene, motive',
 desc='Contestație la executare: ce poți ataca, motivele frecvente, termenul de 15 zile, suspendarea cu cauțiune, taxa de timbru și pașii până la decizie.',
 nav='#calculator|Calculator;#motive|Motive;#procedura|Procedura;#suspendare|Suspendarea;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Executare silită · termen 15 zile · suspendare',
  h1='Contestație la executare: <span class="accent">procedură, termene și motive de anulare</span>',
  lead=['Ai luat un credit de consum acum opt ani și l-ai uitat. Azi găsești în cutia poștală somația unui executor. Suma e de trei ori mai mare, iar creditorul e o firmă de recuperare de care n-ai auzit.',
        'Aici afli ce este <strong>contestația la executare</strong>, ce poți ataca și pe ce motive. Vezi pașii până la decizie, cum oprești temporar executarea și cât costă.'],
  meta2='Termen: 15 zile libere',cta='Calculează cauțiunea și termenul',
  answer='Contestația la executare este cererea prin care ceri judecătoriei să verifice dacă executarea silită pornită împotriva ta respectă legea (art. 712 CPC). Termenul general este de 15 zile. Depunerea nu oprește singură executarea: pentru asta ceri suspendarea. Șansele depind de motive și de acte.',
  opts=[('Termen','15 zile libere (art. 715 CPC)'),('Șanse','bune cu un viciu dovedit')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-inseamna','Ce înseamnă',S2),('motive','Motive',S3),('procedura','Procedura pas cu pas',S4),('suspendare','Suspendarea',S5),('durata','Cât durează',S6),('costuri','Costuri',S7),('sanse','Șanse de câștig',S8),('practica','Practica judiciară',S9),('legislatie','Legislație',S10),('greseli','Greșeli frecvente',S11),('model','Model contestație',S12),('urgent','Ce faci urgent',S13),('azi','Ce faci azi',S14)],
 faq=faq,faq_h2='Întrebări frecvente despre contestația la executare',
 contact=dict(h2='Până când poți depune contestația?',lead='Trimite-ne somația, adresa de poprire sau încheierea primită. Îți spunem până când poți depune contestația și dacă motivele tale au temei. Consultația nu te obligă la nimic.',nav='/|Acasă;/avocat-contestatie-executare-silita/|Avocat contestație;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum depui o contestație la executare',steps=[('Obții dosarul','Ceri executorului copia dosarului de executare și calculul debitului.'),('Calculezi termenul','15 zile libere de la primirea actului atacat (art. 715 și art. 181 CPC).'),('Redactezi cererea','Părțile, obiectul, motivele, probele și anexele (art. 194 CPC).'),('Depui și plătești taxa','La judecătoria de executare; ceri și suspendarea, cu cauțiune.')]),
 knows=['Executare silită','Contestație la executare','Suspendarea executării','Poprire'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/contestatie-la-executare.src.html','w',encoding='utf-8').write(build(P))
