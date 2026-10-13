import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='dare-in-plata-adjudecare-si-executare-comparatie.webp'; IMG2='adjudecare-in-contul-creantei-exemplu.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Adjudecare în contul creanței: <span class="accent">cât depui în plus</span></h2></div>
      <p>Introdu prețul de adjudecare și valoarea creanței tale. Vezi diferența pe care creditorul adjudecatar trebuie să o depună în cel mult 5 zile (art. 771 alin. 2 CPC) sau cât din creanță rămâne neacoperită.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Sume</div>
          <div class="field"><label for="f-v">Prețul de adjudecare (lei)</label><div class="inp"><input id="f-v" inputmode="numeric" placeholder="80000"></div></div>
          <div class="field"><label for="f-d">Valoarea creanței (lei)</label><div class="inp"><input id="f-d" inputmode="numeric" placeholder="60000"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: preț 80.000 lei, creanță 60.000 lei</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Diferență de depus în maximum 5 zile</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Introdu prețul și creanța.</span></div>
            <div class="opt" id="c-m"><span class="k">Creanță acoperită prin adjudecare</span><span class="v" id="o-m">—</span><span class="s" id="o-ms">Din creanța ta.</span></div>
            <div class="opt" id="c-r"><span class="k">Creanță rămasă de recuperat</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Rămâne urmăribilă.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne dosarul</a>
          <span class="disc">Calcul orientativ după art. 771 alin. 2 CPC: creditorul urmăritor care adjudecă poate depune creanța în contul prețului doar dacă nu participă alți creditori sau aceștia au rang inferior; dacă prețul depășește creanța, diferența se depune de îndată sau în cel mult 5 zile de la licitație. Nu include cheltuielile de executare și eventualele creanțe prioritare.</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  function lei(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/[\s.]/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function calc(){
    var p=num('f-v'),c=num('f-d');
    if(!(p>0)||!(c>0)){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Introdu prețul și creanța.';$('o-m').textContent='—';$('o-r').textContent='—';return}
    if(p>c){$('o-t').textContent=lei(p-c);cls('c-t','alert');$('o-ts').textContent='Prețul depășește creanța: diferența se depune de îndată sau în cel mult 5 zile.';$('o-m').textContent=lei(c);$('o-r').textContent=lei(0);cls('c-r','ok')}
    else{$('o-t').textContent=lei(0);cls('c-t','ok');$('o-ts').textContent='Prețul nu depășește creanța: nu depui nicio diferență.';$('o-m').textContent=lei(p);$('o-r').textContent=lei(c-p);cls('c-r',c>p?'alert':'ok')}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-v','f-d'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-v').value='80000';$('f-d').value='60000';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Darea în plată în insolvență: răspuns rapid</h2>
        <p>În Legea nr. 85/2014 nu există o „dare în plată specială” ca instituție separată. Există, în schimb, trei mecanisme care se confundă des: darea în plată a bunurilor către creditori prin planul de reorganizare (art. 133 alin. 5 lit. E, doar cu acordul scris al creditorilor), adjudecarea în contul creanței în executarea silită (art. 771 CPC) și preluarea unui bun mobil nevândut în contul creanței (art. 779 CPC). De la deschiderea insolvenței, executările individuale se suspendă de drept (art. 75).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Creditorul tău are o creanță de 60.000 lei și adjudecă imobilul cu 80.000 lei, în executare silită. Poate depune creanța în contul prețului, dar trebuie să depună diferența de 20.000 lei de îndată sau în cel mult 5 zile de la licitație (art. 771 alin. 2). Dacă nu o depune, licitația se reia.</p>
          <span class="formula">80.000 − 60.000 = 20.000 lei de depus în maximum 5 zile</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Termeni</span>
        <h2>Ce înseamnă darea în plată și adjudecarea în contul creanței</h2>
        <p>Darea în plată înseamnă că debitorul își stinge datoria predând creditorului un alt bun decât suma de bani. Adjudecarea în contul creanței înseamnă că tocmai creditorul care a pornit executarea cumpără bunul la licitație și „plătește” prețul, în tot sau în parte, cu propria creanță. Sunt lucruri diferite, cu reguli diferite.</p>
        <div class="tbl wide"><table>
          <thead><tr><th></th><th>Dare în plată prin plan</th><th>Adjudecare în contul creanței</th><th>Preluarea bunului mobil nevândut</th></tr></thead>
          <tbody>
            <tr><td>Unde se întâmplă</td><td>Procedura de reorganizare</td><td>Executarea silită, la licitație</td><td>Executarea silită, după licitații eșuate</td></tr>
            <tr><td>Temei</td><td>Art. 133 alin. 5 lit. E, Legea nr. 85/2014</td><td>Art. 771 alin. 2 CPC</td><td>Art. 779 CPC</td></tr>
            <tr><td>Condiție</td><td>Acordul scris al creditorilor care primesc bunurile</td><td>Nu participă alți creditori sau au rang inferior</td><td>Bunul sechestrat nu s-a putut vinde</td></tr>
            <tr><td>Prețul</td><td>Stabilit prin plan</td><td>Prețul de adjudecare; diferența se depune în 5 zile</td><td>Prețul din ultimul anunț de vânzare</td></tr>
            <tr><td>Efect</td><td>Creanța se stinge în măsura valorii bunurilor</td><td>Creanța se stinge până la prețul adjudecat</td><td>Creanța se stinge până la valoarea preluată</td></tr>
          </tbody>
        </table></div>
'''+fig(IMG1,'dare în plată, adjudecare în contul creanței și executare silită clasică: temei, condiții, preț și efect','Trei mecanisme diferite, des confundate')
S3='''        <span class="eyebrow">În plan</span>
        <h2>Darea în plată prin planul de reorganizare</h2>
        <p>Planul de reorganizare poate prevedea lichidarea bunurilor debitorului sau darea lor în plată către creditori, în contul creanțelor pe care aceștia le au față de avere. Darea în plată se poate face doar cu acordul scris prealabil al creditorilor, cu privire la această modalitate de stingere a creanței (art. 133 alin. 5 lit. E din Legea nr. 85/2014).</p>
        <h3>Ce trebuie să știi</h3>
        <ul class="chk">
          <li>Planul trebuie să cuprindă programul de plată a creanțelor (art. 133 alin. 2).</li>
          <li>Executarea planului nu poate depăși 3 ani de la confirmare (art. 133 alin. 3).</li>
          <li>Planul se supune votului creditorilor și confirmării judecătorului-sindic; regulile de vot sunt în art. 139. Vezi <a href="/reorganizare-judiciara/">reorganizarea judiciară</a>.</li>
          <li>Creditorul care nu consimte în scris nu poate fi obligat să primească bunul în loc de bani.</li>
        </ul>
        <p>Administratorul judiciar supraveghează realizarea planului, sub controlul judecătorului-sindic.</p>'''
S4='''        <span class="eyebrow">În executare</span>
        <h2>Adjudecarea în contul creanței în executarea silită</h2>
        <p>În urmărirea silită, după adjudecare, adjudecatarul trebuie să depună de îndată întregul preț sau, la cerere acceptată de creditor, în cel mult 5 zile de la licitație (art. 771 alin. 1). Dacă adjudecatar este chiar creditorul urmăritor și nu participă alți creditori, sau cei care participă au rang inferior, el poate depune în contul prețului creanța sa, în tot sau în parte (art. 771 alin. 2). Dacă prețul este mai mare decât creanța, depune diferența în același termen.</p>
        <h3>Ce se întâmplă dacă nu depune diferența</h3>
        <p>Dacă prețul sau diferența nu se depune, licitația se reia sau se alege altă modalitate de valorificare, iar primul adjudecatar răspunde de scăderea prețului obținut la a doua vânzare și de cheltuielile făcute (art. 771 alin. 3).</p>
        <h3>Diferența față de executarea clasică</h3>
        <p>În executarea clasică, bunul se vinde unui terț, iar banii ajung la creditor prin distribuire. În adjudecarea în contul creanței, creditorul ia bunul și își stinge creanța prin compensare cu prețul, fără ca banii să circule, în măsura creanței.</p>
        <h3>Preluarea bunului mobil nevândut</h3>
        <p>Dacă bunul mobil sechestrat nu s-a putut vinde, orice creditor care putea urmări bunurile mobile îl poate prelua în contul creanței, la prețul din publicațiile pentru ultimul termen de licitație. Dacă prețul depășește creanța, preia bunul numai dacă depune diferența (art. 779 alin. 1). Între mai mulți creditori, bunul se atribuie după ordinea de preferință din art. 865 și 867 (art. 779 alin. 2). Bunurile nevândute rămân indisponibilizate cel mult un an de la sechestru (art. 780 alin. 1).</p>
'''+fig(IMG2,'adjudecare în contul creanței: exemplu cu preț de 80.000 lei, creanță de 60.000 lei și diferență de 20.000 lei în 5 zile','Exemplu: adjudecare în contul creanței')
S5='''        <span class="eyebrow">Insolvență</span>
        <h2>De ce adjudecarea clasică nu merge după deschiderea insolvenței</h2>
        <p>De la data deschiderii procedurii se suspendă de drept toate acțiunile judiciare, extrajudiciare sau măsurile de executare silită pentru realizarea creanțelor asupra averii debitorului. Valorificarea drepturilor se face numai în cadrul procedurii insolvenței, prin cereri de admitere a creanțelor (art. 75 din Legea nr. 85/2014). În practică, mecanismele din CPC se aplică înainte de insolvență, iar în insolvență ai dare în plată prin plan sau valorificarea bunurilor în procedură.</p>
        <h3>Drepturile creditorilor</h3>
        <p>Creditorii își depun creanțele în procedură, votează planul și pot accepta sau refuza darea în plată. Creditorii care au o cauză de preferință rămân protejați: sumele obținute din vânzarea bunurilor asupra cărora poartă garanții se distribuie obligatoriu titularilor acelor cauze (art. 133 alin. 5 lit. F).</p>
        <h3>Obligațiile și protecția debitorului</h3>
        <p>Debitorul respectă planul și programul de plată. Darea în plată nu poate fi impusă fără acordul scris al creditorului care primește bunul.</p>'''
S6='''        <span class="eyebrow">Avantaje și riscuri</span>
        <h2>Avantajele și riscurile pentru creditor și debitor</h2>
        <ul class="chk">
          <li><b>Pentru creditor:</b> recuperare mai rapidă, fără să aștepți vânzarea către un terț; riscul este să preiei un bun greu de vândut mai departe.</li>
          <li><b>Pentru debitor:</b> își stinge datoria fără să plătească în bani, dar pierde bunul; evaluarea corectă contează.</li>
          <li><b>Probleme frecvente:</b> evaluare greșită, lipsa acordului scris al creditorului, contestații împotriva vânzării.</li>
        </ul>
        <p>Pentru o vânzare silită greșită, debitorul poate contesta executarea în 15 zile (art. 715 CPC). Vezi <a href="/contestatie-la-executare/">contestația la executare</a>.</p>'''
S7='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Stabilește în ce etapă ești: executare silită sau insolvență deschisă (hotărârea de deschidere).</li>
          <li>Dacă ești creditor, verifică dacă ai rang suficient pentru adjudecare în contul creanței (art. 771 alin. 2) și calculează diferența.</li>
          <li>Trimite-ne dosarul în chat; îți spunem în aceeași zi ce mecanism se potrivește.</li>
        </ol>
        <!--@author practice="insolvență" -->'''
faq=[("Ce este darea în plată în insolvență?","Predarea unor bunuri ale debitorului către creditori, în contul creanțelor, prin planul de reorganizare, doar cu acordul scris al creditorilor (art. 133 alin. 5 lit. E, Legea nr. 85/2014)."),
("Există o „dare în plată specială” în lege?","Legea nr. 85/2014 nu folosește această denumire. Mecanismele reale sunt darea în plată prin plan, adjudecarea în contul creanței (art. 771 CPC) și preluarea bunului mobil nevândut (art. 779 CPC)."),
("Ce înseamnă adjudecarea în contul creanței?","Creditorul urmăritor care adjudecă bunul depune creanța sa în contul prețului, în tot sau în parte, dacă nu participă alți creditori sau aceștia au rang inferior (art. 771 alin. 2)."),
("Când poate creditorul prelua bunurile debitorului?","Bunurile mobile nevândute pot fi preluate în contul creanței, la prețul ultimului termen de licitație (art. 779). În plan, cu acordul scris al creditorilor."),
("Care este diferența dintre adjudecare și executare silită?","Executarea clasică vinde bunul unui terț și distribuie banii. În adjudecarea în contul creanței creditorul ia bunul și își compensează creanța cu prețul."),
("Ce rol are administratorul judiciar?","Supraveghează realizarea planului de reorganizare și a măsurilor din procedură, sub controlul judecătorului-sindic."),
("Poate fi contestată adjudecarea?","Da, executarea și actele ei pot fi contestate în general în 15 zile (art. 715 CPC). Când adjudecatar a fost creditorul, vânzarea se poate desființa dacă există temei de nulitate."),
("Ce se întâmplă cu executările după deschiderea insolvenței?","Se suspendă de drept, iar creditorul își valorifică dreptul prin cerere de admitere a creanței (art. 75 din Legea nr. 85/2014).")]
P=dict(slug='darea-in-plata-in-procedura-insolventei',crumb='Darea în plată în insolvență',
 title='Darea în plată în insolvență: adjudecare, drepturi',
 desc='Cum funcționează darea în plată și adjudecarea în contul creanței: art. 133 din Legea 85/2014, art. 771 și 779 CPC, diferența de 5 zile, drepturile creditorilor.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#plan|Dare în plată prin plan;#adjudecare|Adjudecare;#insolventa|Insolvență;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Legea 85/2014 · art. 133 · art. 771 și 779 CPC',
  h1='Darea în plată în procedura insolvenței <span class="accent">și adjudecarea în contul creanței</span>',
  lead=['Auzi „dare în plată specială” și „adjudecare în contul creanței” și nu e clar dacă sunt același lucru, dacă sunt în Legea insolvenței sau în Codul de procedură civilă. De confuzia asta depinde dacă un creditor poate sau nu să ia un bun în locul banilor.',
        'Aici despărțim mecanismele reale, cu articolele verificate, și îți dăm un calculator pentru diferența pe care o depune creditorul adjudecatar.'],
  meta2='Diferența se depune în 5 zile',cta='Calculează diferența',
  answer='În Legea nr. 85/2014 nu există o „dare în plată specială” separată. Există darea în plată prin planul de reorganizare (art. 133 alin. 5 lit. E, doar cu acordul scris al creditorilor), adjudecarea în contul creanței în executarea silită (art. 771 CPC) și preluarea bunului mobil nevândut (art. 779 CPC). După deschiderea insolvenței, executările se suspendă de drept (art. 75).',
  opts=[('Prin plan','acord scris al creditorilor'),('Adjudecare','diferența în 5 zile'),('Insolvență','executări suspendate')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('termeni','Termeni',S2),('plan','Dare în plată prin plan',S3),('adjudecare','Adjudecare în contul creanței',S4),('insolventa','În insolvență',S5),('riscuri','Avantaje și riscuri',S6),('azi','Ce faci azi',S7)],
 faq=faq,faq_h2='Întrebări frecvente despre darea în plată și adjudecare',
 contact=dict(h2='Ești creditor sau debitor într-o insolvență?',lead='Trimite-ne hotărârea de deschidere, planul sau dosarul de executare. Îți spunem în aceeași zi ce mecanism se aplică și ce drepturi ai. Consultația nu te obligă la nimic.',nav='/|Acasă;/reorganizare-judiciara/|Reorganizare judiciară;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau administratorilor judiciari. Calculele sunt orientative.'),
 howto=dict(name='Cum se face adjudecarea în contul creanței',steps=[('Verifici condițiile','Creditor urmăritor; nu participă alți creditori sau au rang inferior.'),('Participi la licitație','Adjudeci bunul la prețul de adjudecare.'),('Depui creanța în contul prețului','În tot sau în parte.'),('Depui diferența','Dacă prețul depășește creanța, de îndată sau în maximum 5 zile.'),('Primești actul de adjudecare','La imobile, exemplarul predat adjudecatarului îi servește ca titlu de proprietate (art. 855 CPC).')]),
 knows=['Insolvență','Dare în plată','Adjudecare în contul creanței','Executare silită','Legea 85/2014'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/darea-in-plata-in-procedura-insolventei.src.html','w',encoding='utf-8').write(build(P))
