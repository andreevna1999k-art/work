import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='cum-calculezi-termenul-de-15-zile.webp'; IMG2='ai-depasit-15-zile-trei-cai-de-verificat.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Ultima zi pentru contestație, <span class="accent">cu sărbători legale</span></h2></div>
      <p>Introdu data la care ai primit somația, înștiințarea de poprire sau prima reținere. Calculatorul numără 15 zile libere, ca în art. 181 CPC, și mută termenul peste weekend și sărbători legale.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Data actului</div>
          <div class="field full"><label for="f-d">Data primirii (de pe dovada de primire sau din prima reținere)</label><div class="inp"><input type="date" id="f-d"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: 2 martie 2026</button>
            <button type="button" class="btn btn-line" id="b-ex2">Exemplu: 25 martie 2026 (Paște)</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Ultima zi utilă pentru depunere</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Completați data primirii actului.</span></div>
            <div class="opt" id="c-c"><span class="k">Data + 16 zile</span><span class="v" id="o-c">—</span><span class="s" id="o-cs">Înainte de prelungire.</span></div>
            <div class="opt" id="c-r"><span class="k">Zile rămase de azi</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Până la ultima zi utilă.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Verificăm împreună termenul tău</a>
          <span class="disc">Calcul orientativ, după art. 715 și art. 181 CPC. Includem sărbătorile legale uzuale (inclusiv Vinerea Mare, Paștele ortodox, Rusaliile, 1 iunie, 30 noiembrie și 1 decembrie), dar nu orice zi liberă decisă ad-hoc. Dacă trimiți prin poștă sau curier, contează data predării (art. 183 CPC). Data primirii o dovedește actul de comunicare, nu memoria ta. Depune cu cel puțin o zi înainte.</span>
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
    if(!v){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Completați data primirii actului.';$('o-c').textContent='—';$('o-r').textContent='—';$('o-rs').textContent='Până la ultima zi utilă.';return}
    var s=dt(v),e=addD(s,16),raw=e,moved=[];
    while(off(e)){moved.push(fmt(e));e=addD(e,1)}
    $('o-c').textContent=fmt(raw)+' ('+ZI[raw.getUTCDay()]+')';
    $('o-cs').textContent=moved.length?'Zi nelucrătoare: termenul se prelungește.':'Zi lucrătoare: fără prelungire.';
    $('o-t').textContent=fmt(e)+' ('+ZI[e.getUTCDay()]+')';cls('c-t','alert');
    $('o-ts').textContent=moved.length?'Prelungit peste: '+moved.join(', ')+'.':'15 zile libere după '+fmt(s)+'.';
    var t=new Date();var today=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate()));
    var left=Math.round((e.getTime()-today.getTime())/864e5);
    if(left<0){$('o-r').textContent='Termen trecut';cls('c-r','alert');$('o-rs').textContent='Verifică dovada comunicării, un act nou sau repunerea în termen (vezi mai jos).'}
    else{$('o-r').textContent=left+' zile';cls('c-r',left<=3?'alert':'ok');$('o-rs').textContent=left<=3?'Depune cât mai repede.':'Până la ultima zi utilă.'}
  }
  $('b-calc').addEventListener('click',calc);
  $('f-d').addEventListener('input',calc);$('f-d').addEventListener('change',calc);
  function ex(){$('f-d').value='2026-03-02';calc()}
  function ex2(){$('f-d').value='2026-03-25';calc()}
  $('b-ex1').addEventListener('click',ex);$('b-ex2').addEventListener('click',ex2);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Termen contestație la executare: răspuns rapid</h2>
        <p>Termenul general pentru contestația la executare este de 15 zile (art. 715 CPC). El curge de la data la care ai primit somația, încheierea de încuviințare sau înștiințarea de poprire ori ai luat cunoștință de actul contestat. Se calculează pe zile libere. O contestație depusă după termen e respinsă ca tardivă, dacă termenul a curs legal.</p>
        <h3>Când poate fi depusă peste termen</h3>
        <p>O contestație la executare peste termen are șanse doar cu un argument real. Comunicarea a lipsit sau a fost nelegală. Ataci un act nou, cu termen propriu. Ceri lămurirea titlului. Sau ai un motiv temeinic pentru repunere în termen.</p>
        <h3>Ce prevede Codul de procedură civilă</h3>
        <p>Art. 714 CPC arată instanța competentă. Art. 715 CPC arată termenele. Art. 181 CPC spune cum numeri zilele.</p>
        <h3>Care sunt șansele de admitere</h3>
        <p>Depind de dovada comunicării din dosarul executorului. Dacă actele au ajuns legal la tine, șansele unei cereri tardive sunt mici. Dacă dovada lipsește, discuția se schimbă.</p>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este contestația la executare</h2>
        <p>Contestația la executare este cererea prin care ceri instanței să verifice executarea silită. Poți ataca executarea însăși, încheierile executorului sau orice act de executare (art. 712 CPC). Poți cere și lămurirea titlului executoriu. Pe scurt: judecătorul controlează legalitatea pașilor făcuți de executor. Ghidul complet este pe pagina despre <a href="/contestatie-la-executare/">contestație la executare</a>.</p>
        <h3>Rolul contestației</h3>
        <p>Protejează debitorul de acte nelegale: sume greșite, cheltuieli umflate, bunuri care nu pot fi urmărite. Nu oprește singură executarea. Pentru asta ceri separat <a href="/amanare-executare-silita/">suspendarea executării silite</a> (art. 719 CPC).</p>
        <h3>Când poate fi folosită</h3>
        <p>Când primești somația, când ți se blochează contul, când apare o publicație de vânzare sau un proces-verbal de cheltuieli. Fiecare act are propriul moment de pornire a termenului.</p>
        <h4>Exemple practice</h4>
        <p>Situații tipice (anonimizate):</p>
        <div class="roles">
          <div><b>Somație primită la domiciliu</b>Termenul curge de la data de pe dovada de primire.</div>
          <div><b>Cont blocat fără niciun plic</b>Afli de executare de la bancă, prin <a href="/poprire-cont/">poprire cont</a>.</div>
          <div><b>Reținere pe salariu</b>Angajatorul reține o parte din salariu, iar înștiințarea nu a ajuns la tine.</div>
          <div><b>Titlu neclar</b>Hotărârea nu spune clar de la ce dată curg dobânzile.</div>
        </div>'''
S3='''        <span class="eyebrow">Art. 714 și 715</span>
        <h2>Art. 714 și art. 715 CPC: unde depui și când depui</h2>
        <p>În forma actuală a Codului de procedură civilă, republicat în 2015, art. 714 reglementează instanța competentă. Art. 715 reglementează termenele. Înainte de republicare, termenele erau la art. 714. De aceea, multe modele și articole vechi citează „art. 714 – termene”. Verifică numerotarea înainte să o treci în cerere.</p>
        <p>Pe scurt: art. 714 răspunde la „unde?”, art. 715 la „până când?”. Detalii despre instanță găsești în ghidul <a href="/unde-se-depune-contestatia-la-executare/">unde se depune contestația la executare</a>.</p>
        <h3>Termenul general de 15 zile</h3>
        <p>Art. 715 alin. (1) CPC prevede că, dacă legea nu spune altfel, contestația se face în 15 zile de la data când:</p>
        <ul class="chk">
          <li>ai luat cunoștință de actul de executare pe care îl contești;</li>
          <li>ai primit comunicarea sau înștiințarea privind înființarea popririi;</li>
          <li>ca debitor care contești executarea însăși, ai primit încheierea de încuviințare sau somația.</li>
        </ul>
        <p>Dacă nu ai primit nici încheierea, nici somația, termenul curge de când ai aflat de primul act de executare. Termenul este legal și imperativ. Depășirea lui duce la decădere (art. 185 CPC).</p>
        <h3>Cum se calculează termenul</h3>
        <p>Termenul pe zile se calculează pe zile libere (art. 181 CPC). Nu intră în calcul ziua în care începe să curgă și nici ziua în care se împlinește. Dacă ultima zi este nelucrătoare, termenul se prelungește până la prima zi lucrătoare. Practic, ultima zi utilă este data comunicării plus 16 zile, apoi prima zi lucrătoare dacă aceasta cade într-o zi liberă.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Primești somația luni, 2 martie 2026. Ziua de 2 martie nu se numără. Între ea și ziua depunerii trebuie să rămână 15 zile întregi: 3–17 martie. Ultima zi în care poți depune contestația este miercuri, 18 martie 2026. Dacă trimiți cererea prin poștă recomandată sau curier, contează data predării (art. 183 CPC).</p>
          <span class="formula">2 martie + 16 zile = 18 martie 2026 (miercuri, zi lucrătoare)</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>
        <div class="tbl wide"><table>
          <thead><tr><th>Ai primit actul</th><th>Data + 16 zile</th><th>Ultima zi utilă</th><th>De ce</th></tr></thead>
          <tbody>
            <tr><td>Luni, 2 martie 2026</td><td>Miercuri, 18 martie</td><td>Miercuri, 18 martie 2026</td><td>Zi lucrătoare</td></tr>
            <tr><td>Miercuri, 25 martie 2026</td><td>Vineri, 10 aprilie</td><td>Marți, 14 aprilie 2026</td><td>Vinerea Mare, Paștele și a doua zi de Paște</td></tr>
            <tr><td>Vineri, 15 mai 2026 (prima reținere)</td><td>Duminică, 31 mai</td><td>Marți, 2 iunie 2026</td><td>Rusaliile și 1 iunie</td></tr>
            <tr><td>Vineri, 13 noiembrie 2026</td><td>Duminică, 29 noiembrie</td><td>Miercuri, 2 decembrie 2026</td><td>Sf. Andrei și Ziua Națională</td></tr>
          </tbody>
        </table></div>
'''+fig(IMG1,'termen contestație la executare — calcul pe zile libere, de la somație la ultima zi','Cum calculezi termenul de 15 zile')+'''
        <h4>Momentul de la care începe termenul</h4>
        <p>Data o dovedește actul de comunicare, nu memoria ta. Uită-te la dovada de primire, la procesul-verbal al agentului și la semnătura de pe ele. Termenele procedurale curg, de regulă, de la comunicarea actului (art. 184 CPC). Prima întrebare nu este „au trecut 15 zile?”. Este „de la ce dată, dovedită cu ce act?”.</p>'''
S4='''        <span class="eyebrow">Art. 715</span>
        <h2>Ce prevede art. 715 CPC</h2>
        <p>Art. 715 CPC stabilește momentul de început al termenului pentru fiecare tip de contestație. Regula este 15 zile, dar punctul de pornire diferă: actul contestat, poprirea, prima reținere din venituri, somația. Contestația la titlu și cea a terțului au reguli proprii. Calculul greșit al începutului este cea mai frecventă cauză de tardivitate.</p>
        <h3>Termene speciale în contestație</h3>
        <div class="tbl wide"><table>
          <thead><tr><th>Situația</th><th>Termen</th><th>De când curge</th></tr></thead>
          <tbody>
            <tr><td>Contești executarea însăși</td><td>15 zile</td><td>Primirea încheierii de încuviințare sau a somației; altfel, primul act de executare aflat</td></tr>
            <tr><td>Contești un act anume (proces-verbal, cheltuieli, vânzare)</td><td>15 zile</td><td>Data la care ai luat cunoștință de acel act</td></tr>
            <tr><td>Poprire</td><td>15 zile</td><td>Comunicarea sau înștiințarea privind înființarea popririi</td></tr>
            <tr><td>Poprire pe salariu sau pensie</td><td>15 zile</td><td>Cel mai târziu de la prima reținere făcută de terțul poprit</td></tr>
            <tr><td>Încheierile executorului care nu sunt definitive</td><td>15 zile</td><td>De la comunicare (art. 715 alin. (2) CPC)</td></tr>
            <tr><td>Contestația la titlu</td><td>Oricând</td><td>Înăuntrul termenului de prescripție a dreptului de a obține executarea silită (de regulă 3 ani, art. 706 CPC)</td></tr>
            <tr><td>Terț cu drept asupra bunului urmărit</td><td>În cursul executării</td><td>Cel mai târziu 15 zile după vânzare sau predarea silită a bunului</td></tr>
            <tr><td>Executare fiscală (ANAF)</td><td>De regulă 15 zile</td><td>Comunicare sau luare la cunoștință, după Codul de procedură fiscală; verifică cu un avocat</td></tr>
          </tbody>
        </table></div>
        <h3>Interpretarea instanțelor</h3>
        <p>Instanțele verifică întâi termenul. Compară data comunicării cu data depunerii. Nu se mulțumesc cu afirmația executorului că a trimis actul. Cer dovada comunicării. La poprirea pe salariu, contează și data primei rețineri, chiar dacă înștiințarea nu a ajuns. Hotărâri concrete poți căuta pe portal.just.ro, după număr de dosar și instanță.</p>
        <h4>Excepții procedurale</h4>
        <p>Principala este excepția tardivității. Creditorul o invocă de obicei prin întâmpinare. Dacă e admisă, contestația se respinge fără analiza motivelor. De aceea, explici termenul încă din cerere.</p>'''
S5='''        <span class="eyebrow">Peste termen</span>
        <h2>Când poate fi depusă contestația peste termen</h2>
        <p>O contestație la executare după termenul de 15 zile are șanse doar dacă termenul nu a început legal să curgă sau dacă ataci ceva cu termen propriu. Nu ajunge să spui că nu ai știut. Instanța verifică dovada comunicării, actul atacat și data la care ai aflat de el. Fiecare argument trebuie dovedit cu acte.</p>
        <h3>Lipsa comunicării actelor</h3>
        <p>Dacă somația sau încheierea nu ți-au fost comunicate, termenul pentru executarea însăși curge de când ai aflat de primul act de executare. Ceri executorului copia dosarului și verifici dovezile de comunicare.</p>
        <h3>Comunicarea nelegală</h3>
        <p>Adresă veche, semnătură care nu e a ta, proces-verbal incomplet. Astfel de vicii pot face ca termenul să nu fi curs. Nu orice neregulă contează. Trebuie să arăți că nu ai putut afla de act.</p>
        <h3>Nulitatea actelor de executare</h3>
        <p>Nulitatea unui act se invocă tot prin contestație, deci tot în termen. Ea nu redeschide termenul. Arăți actul, norma încălcată și vătămarea.</p>
        <h4>Alte excepții admise de instanțe</h4>
        <ul class="chk">
          <li><strong>Act nou:</strong> o poprire nouă sau un proces-verbal nou are termen propriu de 15 zile.</li>
          <li><strong>Contestația la titlu:</strong> poate fi făcută cât timp dreptul de a cere executarea nu s-a prescris.</li>
          <li><strong>Repunerea în termen (art. 186 CPC):</strong> dovedești un motiv temeinic, de exemplu spitalizarea. Depui contestația în cel mult 15 zile de la încetarea împiedicării și ceri repunerea.</li>
        </ul>
'''+fig(IMG2,'termen contestație la executare depășit — comunicare, act nou, repunere în termen','Ai depășit 15 zile? Trei căi de verificat')
S6='''        <span class="eyebrow">Titlu</span>
        <h2>Contestația la titlu și contestația la executare</h2>
        <p>Contestația la executare atacă ce a făcut executorul. Contestația la titlu cere instanței să lămurească înțelesul, întinderea sau aplicarea titlului executoriu. Diferența contează pentru termen: prima are 15 zile, a doua poate fi făcută oricând până la prescripția dreptului de a obține executarea silită.</p>
        <h3>Diferențe juridice</h3>
        <p>Contestația la titlu nu servește la rejudecarea procesului. Nu poți spune prin ea că hotărârea este greșită. Poți cere doar să se lămurească ce spune titlul.</p>
        <h3>Condiții de admisibilitate</h3>
        <p>Pentru hotărâri judecătorești, lămurirea se cere instanței care a pronunțat hotărârea. Titlul trebuie să fie neclar, iar neclaritatea să afecteze executarea.</p>
        <h4>Exemple comparative</h4>
        <div class="tbl wide"><table>
          <thead><tr><th>Criteriu</th><th>Contestație în termen</th><th>Contestație peste termen</th><th>Contestația la titlu</th></tr></thead>
          <tbody>
            <tr><td>Termen legal</td><td>15 zile (art. 715 CPC)</td><td>Expirat sau neînceput legal</td><td>Oricând până la prescripție</td></tr>
            <tr><td>Condiții</td><td>Cerere la timp, act clar, instanță competentă</td><td>Lipsă de comunicare, comunicare nelegală, act nou, repunere</td><td>Titlu neclar ca înțeles sau întindere</td></tr>
            <tr><td>Acte necesare</td><td>Somația, poprirea, actele executorului</td><td>Dosarul de executare, dovezile de comunicare</td><td>Titlul și actele de executare</td></tr>
            <tr><td>Șanse</td><td>Depind de motive</td><td>Mici fără dovada viciului de comunicare</td><td>Depind de cât de neclar e titlul</td></tr>
            <tr><td>Avantaj</td><td>Se judecă motivele</td><td>Poate salva o apărare reală</td><td>Fără termen scurt</td></tr>
            <tr><td>Dezavantaj</td><td>Nu suspendă executarea</td><td>Risc mare de respingere ca tardivă</td><td>Nu atacă actele executorului</td></tr>
            <tr><td>Recomandare</td><td>Depune imediat</td><td>Doar după analiza dovezilor</td><td>Când problema este titlul</td></tr>
          </tbody>
        </table></div>'''
S7='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura contestației la executare</h2>
        <p>Ceri dosarul de executare, verifici comunicarea și calculezi termenul. Alegi actele contestate și instanța de executare. Redactezi cererea, plătești taxa și o depui la timp. Pașii complecți sunt în ghidul despre <a href="/procedura-executare-silita-etape/">procedura executării silite</a> și pe pagina <a href="/contestatia-la-executare-cod-procedura-civila/">contestația la executare în Codul de procedură civilă</a>.</p>
        <h3>Redactarea contestației</h3>
        <p>Cererea respectă cerințele unei cereri de chemare în judecată (art. 194 CPC). Include un paragraf separat despre termen: data comunicării, dovada și calculul.</p>
        <h3>Actele necesare</h3>
        <p>Somația, încheierea de încuviințare, adresa de poprire, procesele-verbale, dovezile de comunicare, titlul executoriu și dovada taxei de timbru.</p>
        <h3>Instanța competentă</h3>
        <p>De regulă, judecătoria de la domiciliul sau sediul debitorului, de la data sesizării executorului (art. 714 și art. 651 CPC).</p>
        <h4>Judecata contestației</h4>
        <p>Contestația se judecă de urgență și cu precădere. Hotărârea se atacă, de regulă, numai cu apel (art. 718 CPC). În executare, termenul de apel este, de regulă, de 10 zile de la comunicare (art. 651 alin. (4) CPC), dacă legea nu dispune altfel.</p>'''
S8='''        <span class="eyebrow">Practică</span>
        <h2>Practica judiciară și jurisprudență relevantă</h2>
        <p>Practica arată două tipuri de dosare. În primele, debitorul credea că a pierdut termenul, dar comunicarea fusese făcută greșit. În celelalte, motivele erau bune, dar termenul cursese legal. Diferența a făcut-o dovada comunicării, nu forța argumentelor de fond. Hotărâri concrete poți căuta pe portal.just.ro, după număr de dosar și instanță.</p>
        <h3>Strategii juridice eficiente</h3>
        <p>Pune toate motivele în cererea depusă în termen. După depunere, poți adăuga motive noi doar dacă, pentru ele, termenul este respectat (art. 713 alin. (3) CPC). Separă actele: fiecare are propriul termen.</p>
        <div class="note dark"><b>Poziția juridică.</b> Cele mai multe contestații tardive nu sunt pierdute din lipsă de motive, ci din numărarea greșită. Debitorul pornește de la data la care a aflat de la bancă, nu de la data de pe dovada de primire. Calculează întâi termenul pe acte, apoi scrie motivele.</div>'''
S9='''        <span class="eyebrow">Legislație</span>
        <h2>Legislație aplicabilă</h2>
        <p>Termenul contestației la executare se citește din mai multe articole ale Codului de procedură civilă: art. 715 pentru termene, art. 181–186 pentru calcul, prelungire și repunere, art. 714 pentru instanță. Analiza articol cu articol este pe pagina despre <a href="/contestatia-la-executare-cod-procedura-civila/">contestația la executare în Codul de procedură civilă</a>.</p>
        <h3>Codul de procedură civilă</h3>
        <ul class="chk">
          <li><strong>Art. 714:</strong> instanța competentă.</li>
          <li><strong>Art. 715:</strong> termenele contestației.</li>
          <li><strong>Art. 181–184:</strong> calculul pe zile libere, ultima zi nelucrătoare, depunerea prin poștă, curgerea de la comunicare.</li>
          <li><strong>Art. 185–186:</strong> decăderea și repunerea în termen.</li>
        </ul>
        <h3>Interpretări doctrinare</h3>
        <p>Doctrina discută mai ales momentul „luării la cunoștință”. Un debitor poate afla de executare înaintea oricărei comunicări oficiale. Data se dovedește cu actele din dosarul executorului.</p>
        <h4>Comparație între soluții</h4>
        <p>Respinsă ca tardivă: instanța nu analizează motivele. Admisă: actul se anulează sau se îndreaptă, iar executarea poate înceta (art. 720 CPC).</p>'''
S10='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente ale debitorilor</h2>
        <p>Majoritatea greșelilor țin de calendar și de documente. Debitorii numără de la o dată greșită, așteaptă un răspuns de la bancă sau depun la altă instanță. Unii cred că o cerere de suspendare oprește termenul. Nu îl oprește.</p>
        <h3>Ignorarea actelor de executare</h3>
        <p>Un plic nedeschis nu oprește termenul. Data de pe dovada de primire contează.</p>
        <h3>Contestație depusă greșit</h3>
        <p>Un model vechi cu „art. 714 – termene” sau o instanță greșită pierd timp. Verifică numerotarea actuală.</p>
        <h4>Lipsa probelor</h4>
        <p>„Nu am primit nimic” nu e o probă. Ai nevoie de copia dosarului și de dovezile de comunicare.</p>'''
S11='''        <span class="eyebrow">Model</span>
        <h2>Model simplificat de contestație peste termen</h2>
        <p>Modelul de mai jos arată doar structura. Partea decisivă într-o contestație la executare peste termen este explicația despre termen, dovedită cu acte. Adaptează-l la actul atacat și la data reală la care ai aflat de el.</p>
        <h3>Structura modelului</h3>
        <p>Instanța, părțile, numărul dosarului de executare, executorul, actele contestate, paragraful despre termen, motivele de fapt și de drept, probele, semnătura.</p>
        <h4>Exemplu orientativ</h4>
        <div class="quote">„Formulez contestație la executare împotriva actelor din dosarul de executare nr. …. Termenul prevăzut de art. 715 CPC nu a început să curgă, deoarece somația nu mi-a fost comunicată legal. Am aflat de executare la data de …, prin …, iar cererea este depusă în termenul de 15 zile calculat potrivit art. 181 CPC.”</div>'''
S12='''        <span class="eyebrow">Urgent</span>
        <h2>Ce trebuie să faci dacă ai depășit termenul de 15 zile</h2>
        <p>Nu depune o cerere copiată. Află întâi dacă termenul chiar a curs: ceri dosarul executorului și dovezile de comunicare. Apoi vezi dacă ai un act nou, o problemă de titlu sau un motiv de repunere în termen. Dacă executarea continuă, analizezi și cererea de suspendare.</p>
        <h3>Pașii urgenți</h3>
        <ol class="num">
          <li>Cere copia dosarului de executare.</li>
          <li>Notează data fiecărei comunicări.</li>
          <li>Calculează termenul pentru fiecare act.</li>
          <li>Alege calea: contestație, contestație la titlu sau repunere în termen.</li>
        </ol>
        <h4>Recomandări finale</h4>
        <p>Nu aștepta răspunsul băncii. Dacă situația e complicată, discută cu un <a href="/avocat-contestatie-executare-silita/">avocat contestație executare silită</a> înainte de ultima zi.</p>'''
S13='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Caută plicul sau dovada de primire și notează data comunicării.</li>
          <li>Adaugă 16 zile și verifică dacă ultima zi pică într-o zi nelucrătoare (sau folosește calculatorul de mai sus).</li>
          <li>Cere executorului, în scris, copia dosarului de executare.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Pot face contestație după 15 zile?","Da, dacă termenul nu a curs legal, ataci un act nou, ceri lămurirea titlului sau obții repunerea în termen. Altfel, cererea se respinge ca tardivă."),
("Ce prevede art. 714 CPC?","În forma republicată, instanța competentă. Înainte de republicarea din 2015, același număr conținea termenele."),
("Ce prevede art. 715 CPC?","Termenul de 15 zile și momentul de la care curge, pe tipuri de contestație."),
("Când începe să curgă termenul?","De la primirea somației sau a încheierii, a înștiințării de poprire ori de la luarea la cunoștință de act. La poprirea pe salariu, cel mai târziu de la prima reținere."),
("Pot invoca lipsa comunicării actelor?","Da, dar trebuie dovedită cu dosarul executorului. Lipsa comunicării mută începutul termenului."),
("Ce șanse am să câștig contestația?","Depind de termen, de dovezi și de motive. Nimeni nu poate garanta rezultatul."),
("Pot suspenda executarea silită?","Da, prin cerere de suspendare, cu cauțiune (art. 719 CPC). Contestația singură nu suspendă executarea."),
("Ce acte trebuie depuse?","Cererea, actele de executare primite, dovezile de comunicare, titlul și dovada taxei de timbru."),
("Ce se întâmplă dacă ultima zi pică sâmbătă?","Termenul se prelungește până la prima zi lucrătoare (art. 181 CPC)."),
("Există repunere în termen?","Da, pentru motive temeinic justificate. Depui contestația în cel mult 15 zile de la încetarea împiedicării (art. 186 CPC).")]
P=dict(slug='termen-contestatie-la-executare',crumb='Termen contestație la executare',
 title='Termen contestație la executare: 15 zile și peste termen',
 desc='Termen contestație la executare: 15 zile libere (art. 715 CPC). Vezi de când curge, cum îl calculezi pe date reale și ce faci dacă l-ai depășit.',
 nav='#calculator|Calculator;#art-714|Art. 714 și 715;#peste-termen|Peste termen;#procedura|Procedura;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Art. 715 CPC · 15 zile libere · repunere în termen',
  h1='Termen contestație la executare: <span class="accent">15 zile, calcul și contestația peste termen</span>',
  lead=['Ai primit somația executorului luni. Ai pus plicul deoparte și ai sunat la bancă. Între timp, cele 15 zile au început să curgă. Sau poate nu ai primit nimic, iar salariul a venit deja cu o reținere.',
        'Aici afli <strong>de când curge termenul</strong> în fiecare situație și cum îl calculezi pe zile libere, cu date concrete. Vezi și ce poți face dacă termenul pare depășit.'],
  meta2='Ultima zi = data + 16 zile',cta='Calculează ultima zi',
  answer='Termenul general pentru contestația la executare este de 15 zile (art. 715 CPC). El curge de la data la care ai primit somația, încheierea de încuviințare sau înștiințarea de poprire ori ai luat cunoștință de actul contestat. Se calculează pe zile libere: ultima zi utilă este, practic, data primirii plus 16 zile, prelungită peste zilele nelucrătoare. O contestație depusă după termen e respinsă ca tardivă, dacă termenul a curs legal.',
  opts=[('Regula','data + 16 zile'),('Ultima zi liberă','se mută la prima zi lucrătoare')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este contestația',S2),('art-714','Art. 714 și 715',S3),('art-715','Ce prevede art. 715',S4),('peste-termen','Peste termen',S5),('titlu','Contestația la titlu',S6),('procedura','Procedura',S7),('practica','Practica judiciară',S8),('legislatie','Legislație',S9),('greseli','Greșeli frecvente',S10),('model','Model peste termen',S11),('urgent','Ai depășit termenul?',S12),('azi','Ce faci azi',S13)],
 faq=faq,faq_h2='Întrebări frecvente despre termenul contestației la executare',
 contact=dict(h2='Mai ești în termen?',lead='Trimite-ne somația, înștiințarea de poprire sau plicul primit. Îți spunem exact până când poți depune contestația și dacă termenul chiar a expirat. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum calculezi termenul de 15 zile',steps=[('Găsești data comunicării','De pe dovada de primire sau din prima reținere din venit.'),('Aplici regula zilelor libere','Nu numeri ziua primirii și nici ultima zi: ultima zi este data + 16 zile.'),('Verifici ziua nelucrătoare','Dacă ultima zi e sâmbătă, duminică sau sărbătoare, termenul se mută la prima zi lucrătoare.'),('Depui la timp','La registratură, prin poștă sau curier; păstrezi recipisa.')]),
 knows=['Executare silită','Termene procedurale','Contestație la executare','Cod procedură civilă'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/termen-contestatie-la-executare.src.html','w',encoding='utf-8').write(build(P))
