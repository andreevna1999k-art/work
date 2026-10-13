import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='traseul-recuperarii-unei-creante.webp'; IMG2='ce-lege-se-aplica-la-recuperarea-creantelor.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Până când poți cere <span class="accent">executarea silită</span></h2></div>
      <p>Dreptul de a obține executarea silită se prescrie, ca regulă, în 3 ani (art. 706 CPC). Alege punctul de pornire, introdu data și vezi ultima zi, înainte de orice întrerupere.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Titlul tău</div>
          <div class="field full"><label for="f-s">De când curge termenul</label><div class="inp"><select id="f-s">
            <option value="0">Hotărâre judecătorească: data rămânerii definitive</option>
            <option value="1">Alt titlu executoriu (contract, înscris): data când s-a născut dreptul de a cere executarea</option>
          </select></div></div>
          <div class="field full"><label for="f-d">Data</label><div class="inp"><input type="date" id="f-d"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: hotărâre definitivă la 15 februarie 2024</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Ultima zi pentru cererea de executare</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Completează data.</span></div>
            <div class="opt" id="c-r"><span class="k">Zile rămase</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Până la împlinirea termenului.</span></div>
            <div class="opt" id="c-m"><span class="k">Dacă termenul trece</span><span class="v" id="o-m" style="font-size:19px">Repunere</span><span class="s" id="o-ms">Doar pentru motive temeinice, în 15 zile de la încetarea împiedicării (art. 710).</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne titlul executoriu</a>
          <span class="disc">Calcul orientativ după art. 706 CPC: 3 ani, 10 ani pentru titlurile în materia drepturilor reale (nu e inclus aici). Termenul se suspendă sau se întrerupe în cazurile din art. 708–709 CPC (de exemplu prin cererea de executare sau prin plata voluntară a debitorului), deci data reală poate fi mai târzie. Verifică dosarul înainte de a te baza pe data afișată.</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  var ZI=['duminică','luni','marți','miercuri','joi','vineri','sâmbătă'];
  function dt(s){var p=s.split('-');return new Date(Date.UTC(+p[0],+p[1]-1,+p[2]))}
  function fmt(d){return ('0'+d.getUTCDate()).slice(-2)+'.'+('0'+(d.getUTCMonth()+1)).slice(-2)+'.'+d.getUTCFullYear()}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function calc(){
    var v=$('f-d').value;
    if(!v){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Completează data.';$('o-r').textContent='—';return}
    var s=dt(v),e=new Date(Date.UTC(s.getUTCFullYear()+3,s.getUTCMonth(),s.getUTCDate()));
    $('o-t').textContent=fmt(e)+' ('+ZI[e.getUTCDay()]+')';cls('c-t','alert');
    $('o-ts').textContent='3 ani de la '+fmt(s)+' (art. 706 CPC).';
    var t=new Date();var today=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate()));
    var left=Math.round((e.getTime()-today.getTime())/864e5);
    if(0>left){$('o-r').textContent='Termen trecut';cls('c-r','alert');$('o-rs').textContent='Verifică întreruperile (art. 709) sau cere repunerea în termen.'}
    else{$('o-r').textContent=left+' zile';cls('c-r',left>90?'ok':'alert');$('o-rs').textContent=left>90?'Ai timp, dar nu aștepta.':'Depune cererea de executare cât mai repede.'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-s','f-d'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-s').value='0';$('f-d').value='2024-02-15';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Legea recuperării creanțelor: răspuns rapid</h2>
        <p>Nu există o singură „lege a recuperării creanțelor”. Traseul legal este: somație către debitor, apoi un titlu executoriu (o hotărâre sau o ordonanță de plată, ori un titlu pe care îl ai deja), cererea de executare la executorul judecătoresc și, în fine, poprirea sau urmărirea bunurilor. Regulile sunt în Codul civil și, mai ales, în Codul de procedură civilă (CPC). Cel mai important termen: dreptul de a cere executarea se prescrie, de regulă, în 3 ani.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Ai o hotărâre rămasă definitivă la 15 februarie 2024. Poți cere executarea silită până la 15 februarie 2027 (3 ani, art. 706 CPC). Depui cererea de executare cu titlul: prescripția se întrerupe pe data depunerii (art. 709 alin. 1 pct. 2) și începe un nou termen de 3 ani.</p>
          <span class="formula">15.02.2024 + 3 ani = 15.02.2027</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>
        <p>Ghidul este scris din punctul de vedere al creditorului. Dacă ești debitorul și vrei să-ți vezi drepturile, vezi <a href="/legea-impotriva-recuperatorilor-de-credite/">legea împotriva recuperatorilor de credite</a>.</p>'''
S2='''        <span class="eyebrow">Legea aplicabilă</span>
        <h2>Ce lege se aplică la recuperarea unei creanțe</h2>
        <div class="tbl wide"><table>
          <thead><tr><th>Act</th><th>Ce reglementează</th><th>Când îl folosești</th></tr></thead>
          <tbody>
            <tr><td>Codul civil</td><td>Obligațiile, prescripția extinctivă, cesiunea de creanță</td><td>Înainte de orice proces: scadență, dobânzi, prescripție, transfer către o firmă de recuperare</td></tr>
            <tr><td>CPC: ordonanța de plată</td><td>Procedură rapidă pentru creanțe certe, lichide și exigibile din contracte civile constatate prin înscris (art. 1013 și urm.)</td><td>Nu ai un titlu executoriu și debitorul nu contestă serios datoria</td></tr>
            <tr><td>CPC: executarea silită</td><td>Titlul executoriu, cererea, executorul, poprirea (art. 622 și urm.)</td><td>Ai titlul și vrei banii</td></tr>
            <tr><td>Legea nr. 85/2014</td><td>Insolvența debitorului; suspendarea executărilor (art. 75)</td><td>Debitorul intră în insolvență: te înscrii la masa credală</td></tr>
          </tbody>
        </table></div>
'''+fig(IMG2,'ce lege se aplică la recuperarea creanțelor: Codul civil, ordonanța de plată din CPC, executarea silită și insolvența','Legile care contează la recuperarea unei creanțe')+'''
        <p>Un contract de credit al unei bănci este, prin lege specială, titlu executoriu. Un contract obișnuit, o factură sau un împrumut între persoane nu este, de regulă, titlu executoriu: ai nevoie întâi de o hotărâre sau de o ordonanță de plată.</p>'''
S3='''        <span class="eyebrow">Pasul 1</span>
        <h2>Pasul 1: somația și negocierea</h2>
        <p>Înainte de instanță, trimite debitorului o somație scrisă: suma, temeiul (contractul, factura), scadența și un termen de plată. Folosește o modalitate care dovedește primirea: scrisoare recomandată cu confirmare, executor judecătoresc sau e-mail cu confirmare. Somația este și condiția ordonanței de plată: fără ea, cererea se respinge.</p>
        <h3>Ce trebuie să conțină somația</h3>
        <ul class="chk">
          <li>Identificarea părților și a contractului sau a facturii.</li>
          <li>Suma datorată, cu dobânzile calculate separat.</li>
          <li>Un termen de plată clar și consecința neplății: acțiune în instanță.</li>
          <li>Dovada transmiterii și a primirii.</li>
        </ul>
        <p>Negocierea (eșalonare, reducerea dobânzilor) merită încercată în același timp. Orice acord se face în scris; plata voluntară sau recunoașterea datoriei de către debitor întrerupe prescripția (art. 709 alin. 1 pct. 1).</p>'''
S4='''        <span class="eyebrow">Fără titlu</span>
        <h2>Ordonanța de plată și alte căi pentru a obține titlul</h2>
        <p>Dacă nu ai titlu executoriu, ai două căi: acțiunea obișnuită în instanță sau procedura simplificată a ordonanței de plată. Aceasta din urmă cere o creanță certă, lichidă și exigibilă, rezultată dintr-un contract civil (inclusiv între profesioniști) și constatată printr-un înscris (art. 1013 CPC). Cere o somație prealabilă. Verifică termenele din art. 1014 și 1015 înainte să depui: ele decid dacă cererea este admisibilă.</p>
        <h3>Când nu funcționează ordonanța de plată</h3>
        <p>Dacă datoria se discută serios (facturi contestate, servicii nelivrate, calculul dobânzilor), judecătorul poate respinge procedura simplificată și îți rămâne acțiunea obișnuită, mai lentă. Pentru sume mici există și proceduri speciale pentru cereri de valoare redusă; verifică condițiile lor în textul CPC.</p>
        <h3>Titluri executorii pe care le ai deja</h3>
        <p>Hotărârile judecătorești definitive sau executorii, contractele de credit ale băncilor și alte înscrisuri declarate executorii de lege (art. 632–634 CPC) te scutesc de proces: mergi direct la executor.</p>'''
S5='''        <span class="eyebrow">Executarea</span>
        <h2>Executarea silită: titlu executoriu și executor</h2>
        <ol class="num">
          <li><b>Cererea de executare</b> se depune la executorul competent, cu titlul și actele justificative (art. 664 CPC). Ea poate cere mai multe modalități: poprire, bunuri mobile, imobile.</li>
          <li><b>Încuviințarea:</b> executorul decide în 3 zile, fără citarea părților (art. 666 alin. 1–2).</li>
          <li><b>Comunicarea:</b> debitorul primește încheierea, titlul și, de regulă, somația (art. 667–668). Poprirea se înființează fără somație (art. 783).</li>
          <li><b>Măsurile:</b> poprirea veniturilor și a conturilor, sechestrul, vânzarea la licitație.</li>
          <li><b>Distribuirea:</b> executorul îți eliberează sumele sau le distribuie între creditori (art. 864 și urm.).</li>
        </ol>
'''+fig(IMG1,'traseul recuperării unei creanțe: somație, titlu executoriu, cerere de executare, executor, încasare','Traseul recuperării unei creanțe')+'''
        <h3>Costuri</h3>
        <p>Cheltuielile de executare (taxe, onorariul executorului, onorariul avocatului) sunt, de regulă, în sarcina debitorului (art. 670 alin. 2), dar tu le avansezi (art. 670 alin. 1) și le recuperezi din sumele încasate. Dacă renunți la executare, le suporți tu.</p>
        <p>Detalii pe etape găsești în ghidul <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>'''
S6='''        <span class="eyebrow">Termene</span>
        <h2>Termenul de prescripție (3 ani) și ce îl oprește</h2>
        <p>Dreptul de a obține executarea silită se prescrie în 3 ani (10 ani pentru titlurile în materia drepturilor reale). Termenul curge de la rămânerea definitivă a hotărârii sau de la nașterea dreptului (art. 706 CPC). Prescripția nu operează de drept: o invocă debitorul (art. 707).</p>
        <div class="tbl wide"><table>
          <thead><tr><th>Eveniment</th><th>Efect</th><th>Temei</th></tr></thead>
          <tbody>
            <tr><td>Debitorul plătește o parte sau recunoaște datoria</td><td>Se întrerupe; curge un nou termen de 3 ani</td><td>Art. 709 alin. 1 pct. 1</td></tr>
            <tr><td>Depui cererea de executare cu titlul</td><td>Se întrerupe, chiar dacă executorul era necompetent</td><td>Art. 709 alin. 1 pct. 2</td></tr>
            <tr><td>Se face un act de executare</td><td>Se întrerupe</td><td>Art. 709 alin. 1 pct. 4</td></tr>
            <tr><td>Executarea e suspendată prin lege sau de instanță</td><td>Se suspendă (nu și când suspendarea e la cererea ta)</td><td>Art. 708</td></tr>
            <tr><td>Debitorul nu are bunuri urmăribile</td><td>Se suspendă cât durează situația</td><td>Art. 708 alin. 1 pct. 3</td></tr>
            <tr><td>Executarea s-a perimat sau a fost anulată</td><td>Nu mai întrerupe prescripția</td><td>Art. 709 alin. 3</td></tr>
          </tbody>
        </table></div>
        <p>Perimarea apare dacă lași 6 luni fără să faci un act cerut în scris de executor (art. 697). După termen, poți cere repunerea numai pentru motive temeinice, în 15 zile de la încetarea împiedicării (art. 710).</p>'''
S7='''        <span class="eyebrow">Cesiunea</span>
        <h2>Cesiunea creanței către o firmă de recuperare</h2>
        <p>Poți vinde creanța unei firme de recuperare (cesiune). Cesionarul preia drepturile tale și poate cere executarea în locul tău. Pentru debitor, cesiunea produce efecte după ce i-a fost notificată sau după ce a acceptat-o; până atunci poate plăti valabil cedentului. Debitorul păstrează, de regulă, apărările pe care le avea față de tine, inclusiv prescripția.</p>
        <h3>Ce să verifici înainte să cesionezi</h3>
        <ul class="chk">
          <li>Că titlul și actele sunt complete: cesionarul le va cere.</li>
          <li>Că prețul reflectă termenul de prescripție rămas.</li>
          <li>Că firma are autorizațiile cerute; vezi <a href="/societati-recuperare-creante/">societățile de recuperare creanțe</a>.</li>
        </ul>
        <p>Detalii despre comportamentul interzis al recuperatorilor și drepturile debitorului sunt în ghidul <a href="/legea-impotriva-recuperatorilor-de-credite/">legea împotriva recuperatorilor de credite</a>.</p>'''
S8='''        <span class="eyebrow">Insolvență</span>
        <h2>Ce se întâmplă dacă debitorul intră în insolvență</h2>
        <p>De la data deschiderii procedurii de insolvență, executările silite și acțiunile pentru realizarea creanțelor asupra averii debitorului se suspendă de drept; creanța se valorifică numai în procedură, prin cerere de admitere (art. 75 din Legea nr. 85/2014). Dacă ai deja o poprire sau o executare în curs, ea se oprește și trebuie să te înscrii la masa credală.</p>'''
S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Verifică ce titlu ai și calculează ultima zi a termenului de 3 ani (folosește calculatorul).</li>
          <li>Dacă nu ai titlu, trimite o somație cu dovadă de primire.</li>
          <li>Trimite-ne titlul și datele debitorului în chat; îți spunem în aceeași zi ce cale se potrivește.</li>
        </ol>
        <!--@author practice="recuperare creanțe" -->'''
faq=[("Ce lege se aplică la recuperarea creanțelor?","Codul civil pentru obligații, prescripție și cesiune, iar Codul de procedură civilă pentru ordonanța de plată și executarea silită. Insolvența debitorului are regim separat (Legea nr. 85/2014)."),
("Pot recupera o datorie fără proces?","Da, dacă ai deja titlu executoriu (hotărâre, contract de credit bancar sau alt înscris declarat executoriu de lege). Atunci mergi direct la executorul judecătoresc."),
("Ce este ordonanța de plată?","O procedură simplificată pentru creanțe certe, lichide și exigibile, rezultate dintr-un contract civil și constatate printr-un înscris (art. 1013 CPC). Cere o somație prealabilă."),
("În cât timp se prescrie dreptul de a cere executarea?","În 3 ani, de regulă, de la rămânerea definitivă a hotărârii sau de la nașterea dreptului. Pentru titlurile în materia drepturilor reale termenul este de 10 ani (art. 706 CPC)."),
("Ce întrerupe prescripția executării?","Plata sau recunoașterea datoriei de către debitor, cererea de executare, cererea de intervenție în executarea altui creditor și orice act de executare (art. 709 CPC)."),
("Cine plătește cheltuielile executării?","De regulă debitorul (art. 670 alin. 2), dar tu le avansezi. Dacă renunți la executare, le suporți tu."),
("Pot vinde creanța unei firme de recuperare?","Da, prin cesiune. Debitorul trebuie notificat sau trebuie să accepte cesiunea pentru ca aceasta să-i fie opozabilă."),
("Ce fac dacă debitorul intră în insolvență?","Executările se suspendă de drept (art. 75 din Legea nr. 85/2014). Îți depui cererea de admitere a creanței în procedura de insolvență.")]
P=dict(slug='lege-recuperare-creante',crumb='Legea recuperării creanțelor',
 title='Legea recuperării creanțelor: somație, ordonanță, executare',
 desc='Cum recuperezi legal o creanță: somația, ordonanța de plată, titlul executoriu, cererea la executor, prescripția de 3 ani și cesiunea către o firmă de recuperare.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#pasi|Pași;#prescriptie|Prescripție;#cesiune|Cesiune;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Creditor · somație · ordonanță de plată · executare',
  h1='Legea recuperării creanțelor: <span class="accent">somație, ordonanță de plată și executare</span>',
  lead=['Ai o factură neplătită sau un împrumut dat și vrei banii înapoi, legal și fără să pierzi dreptul la acțiune. Problema nu e lipsa legii, ci ordinea pașilor și termenul de 3 ani, pe care mulți creditori îl observă prea târziu.',
        'Aici ai traseul complet, din punctul de vedere al creditorului, cu articolele din CPC, tabelul întreruperilor de prescripție și un calculator pentru ultima zi de depunere.'],
  meta2='Prescripție: 3 ani',cta='Calculează termenul',
  answer='Nu există o singură lege: traseul este somație, apoi titlu executoriu (hotărâre, ordonanță de plată sau un titlu pe care îl ai deja), cerere de executare la executor și poprire sau urmărirea bunurilor. Regulile sunt în Codul civil și în CPC. Dreptul de a cere executarea se prescrie, de regulă, în 3 ani (art. 706 CPC), dar prescripția se întrerupe prin cererea de executare și prin actele de executare.',
  opts=[('Titlu executoriu','hotărâre, ordonanță, contract bancar'),('Încuviințare','3 zile (art. 666)'),('Prescripție','3 ani (art. 706)')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('lege','Ce lege se aplică',S2),('pasi','Pasul 1: somația',S3),('ordonanta','Ordonanța de plată',S4),('executare','Executarea',S5),('prescriptie','Prescripția',S6),('cesiune','Cesiunea',S7),('insolventa','Insolvența debitorului',S8),('azi','Ce faci azi',S9)],
 faq=faq,faq_h2='Întrebări frecvente despre recuperarea creanțelor',
 contact=dict(h2='Ai o creanță de recuperat?',lead='Trimite-ne titlul, contractul sau factura și datele debitorului. Îți spunem în aceeași zi ce cale se potrivește și cât mai ai din termenul de prescripție. Consultația nu te obligă la nimic.',nav='/|Acasă;/procedura-executare-silita-etape/|Procedura executării;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum recuperezi legal o creanță',steps=[('Trimiți somația','Cu dovadă de primire, suma și un termen de plată.'),('Obții titlul executoriu','Hotărâre, ordonanță de plată sau un titlu pe care îl ai deja.'),('Depui cererea de executare','La executorul competent, cu titlul și actele.'),('Alegi modalitatea','Poprire, bunuri mobile sau imobile.'),('Urmărești termenul','Prescripția de 3 ani se întrerupe prin cerere și acte de executare.')]),
 knows=['Recuperare creanțe','Ordonanță de plată','Executare silită','Prescripție','Cesiune de creanță'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/lege-recuperare-creante.src.html','w',encoding='utf-8').write(build(P))
