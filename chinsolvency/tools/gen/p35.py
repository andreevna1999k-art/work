import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='amanare-vs-suspendare-executare-silita.webp'; IMG2='cautiunea-pentru-suspendare-executare.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Cât este cauțiunea pentru <span class="accent">suspendarea executării</span></h2></div>
      <p>Introdu valoarea contestată. Calculatorul aplică grila din art. 719 alin. 2–3 CPC și adaugă taxa pentru cererea de suspendare, ca să știi ce sumă pregătești înainte de depunere.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Situația ta</div>
          <div class="field full"><label for="f-s">Situația pentru suspendare</label><div class="inp"><select id="f-s">
            <option value="0">Obiect evaluabil în bani (poprire, sumă din titlu)</option>
            <option value="1">Obiect neevaluabil în bani</option>
            <option value="2">Titlul nu e executoriu / am înscris autentic de amânare (fără cauțiune)</option>
          </select></div></div>
          <div class="grp">Suma</div>
          <div class="field full"><label for="f-v">Valoarea contestată (lei)</label><div class="inp"><input id="f-v" inputmode="numeric" placeholder="35000"></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: poprire de 35.000 lei</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Cauțiune de consemnat</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Introdu valoarea contestată.</span></div>
            <div class="opt" id="c-x"><span class="k">Taxă cerere de suspendare</span><span class="v" id="o-x">50 lei</span><span class="s" id="o-xs">Conform OUG 80/2013.</span></div>
            <div class="opt" id="c-m"><span class="k">Total de pregătit</span><span class="v" id="o-m">—</span><span class="s" id="o-ms">Cauțiune + taxă.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne încheierea și somația</a>
          <span class="disc">Calcul orientativ după art. 719 CPC. Nu include taxa de timbru a contestației (cel mult 1.000 lei) și onorariul avocatului. Cauțiunea se consemnează înainte de soluționarea cererii. Dacă contestația se respinge, ea rămâne indisponibilizată (art. 720 alin. 6).</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  function lei(n){return (Math.round(n*100)/100).toString().replace('.',',').replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/[\s.]/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function caut(v){if(10000>=v)return v*0.1;if(100000>=v)return 1000+0.05*(v-10000);if(1000000>=v)return 5500+0.01*(v-100000);return 14500+0.001*(v-1000000)}
  function calc(){
    var s=parseInt($('f-s').value,10),v=num('f-v'),c=null,t='';
    if(s===2){c=0;t='Suspendarea este obligatorie și cauțiunea nu se cere (art. 719 alin. 4), dacă dovedești situația.'}
    else if(s===1){c=1000;t='Obiect neevaluabil în bani: 1.000 lei (art. 719 alin. 3).'}
    else if(v>0){c=caut(v);t=(v<=10000?'10% din valoare':(v<=100000?'1.000 lei + 5% din ce depășește 10.000 lei':(v<=1000000?'5.500 lei + 1% din ce depășește 100.000 lei':'14.500 lei + 0,1% din ce depășește 1.000.000 lei')))+' (art. 719 alin. 2).'}
    if(c===null){$('o-t').textContent='—';$('o-ts').textContent='Introdu valoarea contestată.';$('o-m').textContent='—';cls('c-t');return}
    $('o-t').textContent=lei(c);cls('c-t',c>0?'alert':'ok');$('o-ts').textContent=t;
    $('o-m').textContent=lei(c+50);
  }
  $('b-calc').addEventListener('click',calc);
  ['f-s','f-v'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-s').value='0';$('f-v').value='35000';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Amânare vs suspendare: diferența pe scurt</h2>
        <p>Amânarea o dispune executorul și doar în două situații: citarea sau publicațiile de vânzare nu au fost îndeplinite, ori creditorul nu și-a îndeplinit obligațiile la termen (art. 700 CPC). Suspendarea o dispune instanța, legea sau executorul la cererea creditorului (art. 701). Debitorul nu poate cere executorului o „amânare” pe motiv că nu are bani.</p>
        <div class="tbl wide"><table>
          <thead><tr><th></th><th>Amânare</th><th>Suspendare</th><th>Contestație la executare</th></tr></thead>
          <tbody>
            <tr><td>Scop</td><td>Corectarea unei lipse procedurale</td><td>Oprirea executării până la decizie</td><td>Anularea actului sau a executării</td></tr>
            <tr><td>Cine decide</td><td>Executorul, prin încheiere</td><td>Instanța, legea sau creditorul</td><td>Instanța de executare</td></tr>
            <tr><td>Cost</td><td>Fără taxă</td><td>Taxă 50 lei + cauțiune</td><td>Taxă de timbru, până la 1.000 lei</td></tr>
            <tr><td>Termen</td><td>Până la îndeplinirea lipsei</td><td>Până la soluționarea contestației</td><td>15 zile, de regulă (art. 715)</td></tr>
            <tr><td>Avantaj</td><td>Rapidă</td><td>Oprește reținerile noi</td><td>Poate desființa executarea</td></tr>
            <tr><td>Dezavantaj</td><td>Se aplică rar</td><td>Cauțiune imediată; măsurile existente rămân</td><td>Nu oprește singură executarea</td></tr>
          </tbody>
        </table></div>
'''+fig(IMG1,'amânare și suspendare în executarea silită: cine decide, când, cât costă','Amânare și suspendare: diferențele')+'''
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Contești o poprire de 35.000 lei. Cauțiunea pentru suspendare: 1.000 lei + 5% din ce depășește 10.000 lei = 1.000 + 5% × 25.000 = 2.250 lei. Pentru 8.000 lei cauțiunea este 10% = 800 lei. Pentru 120.000 lei: 5.500 + 1% × 20.000 = 5.700 lei.</p>
          <span class="formula">1.000 + 5% × (35.000 − 10.000) = 2.250 lei</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">La cererea creditorului</span>
        <h2>Suspendarea la cererea creditorului</h2>
        <p>Singura „amânare” pe care o poți obține fără instanță este cea la care creditorul consimte: executarea se suspendă la cererea creditorului urmăritor, de către executor (art. 701 alin. 2 CPC). Se întâmplă, de obicei, când ai încheiat o înțelegere de eșalonare. Trei lucruri contează:</p>
        <ul class="chk">
          <li>Cere ca înțelegerea să fie în scris, semnată de creditor, cu mențiunea că va cere executorului suspendarea.</li>
          <li>Pe durata suspendării, actele deja făcute, inclusiv indisponibilizarea bunurilor, veniturilor și conturilor, rămân în ființă dacă nu se dispune altfel (art. 701 alin. 3). Cere în scris și ridicarea popririi, altfel contul rămâne blocat.</li>
          <li>Termenul de perimare (6 luni) nu se suspendă cât timp executarea e suspendată la cererea creditorului (art. 697 alin. 2). Îl privește pe creditor, dar explică de ce unii nu vor să suspende.</li>
        </ul>
        <p>O alternativă este un înscris autentic din care rezultă că ai obținut de la creditor o amânare ori un termen de plată: atunci suspendarea instanței este obligatorie, fără cauțiune (art. 719 alin. 4 pct. 3).</p>'''
S3='''        <span class="eyebrow">Art. 719</span>
        <h2>Suspendarea cerută instanței odată cu contestația: cauțiunea</h2>
        <p>Până la soluționarea contestației la executare, instanța competentă poate suspenda executarea, la cerere și numai pentru motive temeinice (art. 719 alin. 1). Cererea se depune odată cu contestația sau separat.</p>
        <h3>Cum se calculează cauțiunea</h3>
        <div class="tbl"><table>
          <thead><tr><th>Valoarea contestată</th><th>Cauțiune (art. 719 alin. 2–3)</th></tr></thead>
          <tbody>
            <tr><td>Până la 10.000 lei</td><td>10%</td></tr>
            <tr><td>10.000 – 100.000 lei</td><td>1.000 lei + 5% din ce depășește 10.000 lei</td></tr>
            <tr><td>100.000 – 1.000.000 lei</td><td>5.500 lei + 1% din ce depășește 100.000 lei</td></tr>
            <tr><td>Peste 1.000.000 lei</td><td>14.500 lei + 0,1% din ce depășește 1.000.000 lei</td></tr>
            <tr><td>Obiect neevaluabil în bani</td><td>1.000 lei</td></tr>
          </tbody>
        </table></div>
'''+fig(IMG2,'cauțiunea pentru suspendarea executării: 10% până la 10.000 lei, apoi 1.000 lei + 5%, 5.500 lei + 1%, 14.500 lei + 0,1%','Grila cauțiunii din art. 719 CPC')+'''
        <p>Cauțiunea se depune în prealabil. Dacă contestația este respinsă, suma rămâne indisponibilizată și poate servi la acoperirea despăgubirilor pentru întârzierea executării sau a creanței din titlu (art. 720 alin. 6). Dacă ai contestat cu rea-credință, instanța poate aplica și o amendă judiciară de 1.000–7.000 lei (art. 720 alin. 3).</p>
        <h3>Când nu mai plătești cauțiune</h3>
        <p>Suspendarea este obligatorie și cauțiunea nu e necesară în trei cazuri (art. 719 alin. 4): hotărârea sau înscrisul executat nu este executoriu; înscrisul a fost declarat fals printr-o hotărâre dată în primă instanță; ai un înscris autentic cu amânare sau termen de plată din partea creditorului.</p>
        <h3>Suspendarea provizorie</h3>
        <p>Dacă este urgent și ai plătit cauțiunea, instanța poate dispune suspendarea provizorie fără citarea părților, până la soluționarea cererii de suspendare. Încheierea nu are cale de atac. Atenție: cauțiunea rămâne indisponibilizată chiar dacă suspendarea provizorie este respinsă; ea se scade din cauțiunea finală (art. 719 alin. 7).</p>'''
S4='''        <span class="eyebrow">Procedura</span>
        <h2>Cum ceri suspendarea, pas cu pas</h2>
        <ol class="num">
          <li><b>Calculează ultima zi pentru contestație</b> (15 zile libere de la actul primit, art. 715). Cererea de suspendare poate fi depusă și ulterior, cât timp contestația este în curs.</li>
          <li><b>Pregătește motive temeinice:</b> titlu neexecutoriu, sumă greșită, executare nelegală, pagubă greu de reparat.</li>
          <li><b>Calculează și consemnează cauțiunea</b> la dispoziția instanței (vezi calculatorul).</li>
          <li><b>Depune cererea și dovada cauțiunii</b> la instanța de executare, plus taxa de 50 lei.</li>
          <li><b>Prezintă-te la termen.</b> Instanța se pronunță prin încheiere, chiar înainte de judecarea contestației; părțile sunt citate, iar încheierea se atacă doar cu apel separat, în 5 zile (art. 719 alin. 6).</li>
          <li><b>Dacă se admite,</b> încheierea se comunică de îndată executorului (art. 719 alin. 8).</li>
        </ol>
        <p>Pentru contestația propriu-zisă, vezi <a href="/contestatie-la-executare/">contestația la executare</a>, <a href="/termen-contestatie-la-executare/">termenul de contestație</a> și <a href="/unde-se-depune-contestatia-la-executare/">instanța competentă</a>.</p>'''
S5='''        <span class="eyebrow">Salariu</span>
        <h2>Amânarea popririi pe salariu: ce se poate și ce nu</h2>
        <p>Pe salariu nu există „amânare” a popririi. Ai trei variante reale: suspendare convenită cu creditorul, suspendare dispusă de instanță cu cauțiune și limitarea legală. Se poate reține cel mult o treime din venitul net pentru datorii obișnuite și cel mult jumătate dacă sunt mai multe urmăriri (art. 729 alin. 1–2). Dacă venitul este sub salariul minim net, se urmărește doar partea care depășește jumătate din acest nivel (art. 729 alin. 3). Poprirea continuă dacă îți schimbi locul de muncă sau ieși la pensie: noul plătitor primește actele (art. 786).</p>'''
S6='''        <span class="eyebrow">Durată și efecte</span>
        <h2>Cât durează și ce se întâmplă după</h2>
        <p>Legea nu dă o durată fixă. Contestația se judecă de urgență și cu precădere, cu citarea părților în termen scurt (art. 717 alin. 3), iar cererea de suspendare se soluționează prin încheiere chiar înainte de termenul contestației. În practică, ia în calcul de la câteva zile (suspendare provizorie) la câteva săptămâni (suspendare obișnuită). După încetarea suspendării, executorul continuă executarea la cererea părții interesate, dacă actele nu au fost desființate de instanță (art. 701 alin. 5).</p>
        <p>Un efect pe care mulți îl ratează: actele de executare făcute chiar în ziua soluționării cererii de suspendare sunt desființate de drept dacă se admit și suspendarea, și contestația (art. 701 alin. 4).</p>
        <h3>Când se respinge cererea de suspendare</h3>
        <ul class="chk">
          <li>Nu ai consemnat cauțiunea în prealabil (art. 719 alin. 2).</li>
          <li>Nu ai motive temeinice: simpla lipsă de bani nu ajunge.</li>
          <li>Invoci motive care puteau fi ridicate în procesul inițial (art. 713 alin. 1).</li>
          <li>Contestația este depusă tardiv.</li>
        </ul>'''
S7='''        <span class="eyebrow">Model</span>
        <h2>Model simplificat de cerere de suspendare</h2>
        <p>Modelul arată doar structura; motivele se adaptează după dosar.</p>
        <div class="quote">„Către Judecătoria [__]. Dosar nr. [__]. Contestator: [nume, domiciliu]. Intimat: [creditor]. În temeiul art. 719 CPC, solicit suspendarea executării silite în dosarul [__] al executorului [__], până la soluționarea contestației. Motive: [titlu neexecutoriu / sumă calculată greșit / …]. Valoarea contestată: [__] lei; cauțiunea de [__] lei a fost consemnată (se anexează dovada). Anexez: contestația, încheierea de încuviințare, somația, dovada cauțiunii, taxa de 50 lei.”</div>'''
S8='''        <span class="eyebrow">Poziția juridică</span>
        <h2>Poziția juridică: ce nu face suspendarea</h2>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată la data depunerii. Suspendarea nu „șterge” datoria și nu ridică singură poprirea existentă: art. 701 alin. 3 păstrează măsurile de indisponibilizare, iar art. 784 alin. 1 cere terțului poprit să nu facă nicio plată către debitor. Pentru ridicarea efectivă a blocajului ai nevoie de o dispoziție expresă a instanței sau de consemnarea integrală a creanței (art. 721).</p>'''
S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Notează data primirii actului și calculează cele 15 zile libere.</li>
          <li>Calculează cauțiunea cu calculatorul de mai sus și vezi dacă o poți consemna rapid.</li>
          <li>Trimite-ne încheierea și somația în chat; îți spunem în aceeași zi dacă ai motive temeinice pentru suspendare.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Care este diferența dintre amânare și suspendare?","Amânarea o dispune executorul în cazuri limitate (art. 700); suspendarea o dispune instanța, legea sau executorul la cererea creditorului (art. 701, 719)."),
("Este obligatorie cauțiunea?","Da, în principiu, și se depune în prealabil (art. 719 alin. 2). Excepțiile sunt cele trei cazuri din art. 719 alin. 4."),
("Cât costă suspendarea executării?","Taxa de 50 lei plus cauțiunea: 10% până la 10.000 lei; 1.000 lei + 5% pentru restul până la 100.000 lei; apoi 5.500 lei + 1% și 14.500 lei + 0,1% peste 1.000.000 lei. Obiect neevaluabil: 1.000 lei."),
("Pot opri poprirea pe cont?","Doar printr-o suspendare cu ridicarea expresă a măsurii ori prin consemnarea creanței (art. 721). Suspendarea simplă lasă contul indisponibilizat (art. 701 alin. 3)."),
("Cât durează procedura?","Legea nu fixează o durată: contestația se judecă de urgență (art. 717), iar cererea de suspendare se soluționează prin încheiere, chiar înainte de termenul contestației."),
("Ce acte sunt necesare?","Contestația, încheierea de încuviințare, somația sau adresa de poprire, dovada cauțiunii și taxa de 50 lei."),
("Ce se întâmplă cu cauțiunea dacă pierd?","Rămâne indisponibilizată și poate acoperi despăgubirile sau creanța din titlu (art. 720 alin. 6)."),
("Ce șanse am?","Depind de motive: sunt mari când titlul nu e executoriu sau ai un înscris autentic de amânare, și mici când invoci doar lipsa banilor.")]
P=dict(slug='amanare-executare-silita',crumb='Amânare și suspendare executare silită',
 title='Amânare și suspendare executare silită: cauțiune, termene',
 desc='Cum oprești o executare silită: diferența dintre amânare și suspendare, cererea către instanță, cauțiunea (10% sau 1.000 lei + 5%), suspendarea provizorie și ce rămâne blocat în timpul suspendării.',
 nav='#calculator|Calculator;#raspuns|Amânare vs suspendare;#cautiune|Cauțiune;#procedura|Procedura;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Art. 700, 701, 719 CPC · cauțiune · suspendare provizorie',
  h1='Amânarea și suspendarea executării silite: <span class="accent">cereri, termene și cauțiune</span>',
  lead=['Primești o poprire și ți se blochează contul în aceeași zi. Cauți „amânare”, dar legea vorbește de „suspendare”, iar cele două nu sunt același lucru. Cine confundă termenii pierde zile prețioase, iar cine nu pregătește cauțiunea este respins.',
        'Aici vezi, articol cu articol, cum se oprește executarea silită, cât costă și ce nu se oprește de fapt, plus un calculator pentru cauțiune.'],
  meta2='Cauțiune: 10% până la 10.000 lei',cta='Calculează cauțiunea',
  answer='Amânarea o dispune executorul, doar în două situații (art. 700 CPC). Suspendarea o dispune instanța, legea sau executorul la cererea creditorului (art. 701, 719). Pentru suspendarea cerută instanței, de regulă consemnezi o cauțiune: 10% din valoarea contestată până la 10.000 lei, apoi 1.000 lei + 5% din excedent. Suspendarea simplă nu ridică singură poprirea existentă.',
  opts=[('Amânare','executorul, caz limitat'),('Suspendare','instanța, cu cauțiune'),('Taxă cerere','50 lei')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Amânare vs suspendare',S1),('creditor','La cererea creditorului',S2),('cautiune','Cauțiunea',S3),('procedura','Procedura',S4),('salariu','Poprirea pe salariu',S5),('durata','Durată și efecte',S6),('model','Model de cerere',S7),('pozitia','Poziția juridică',S8),('azi','Ce faci azi',S9)],
 faq=faq,faq_h2='Întrebări frecvente despre suspendarea executării silite',
 contact=dict(h2='Vrei să oprești executarea?',lead='Trimite-ne încheierea de încuviințare și somația sau adresa de poprire. Îți spunem în aceeași zi dacă ai motive temeinice pentru suspendare și cât ar fi cauțiunea. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum ceri suspendarea executării silite',steps=[('Calculezi termenul','15 zile libere pentru contestație.'),('Pregătești motivele','Titlu neexecutoriu, sumă greșită, executare nelegală.'),('Consemnezi cauțiunea','Conform grilei din art. 719 CPC.'),('Depui cererea','La instanța de executare, cu dovada cauțiunii și taxa de 50 lei.'),('Aștepți încheierea','Se atacă doar cu apel separat, în 5 zile.')]),
 knows=['Executare silită','Suspendarea executării','Cauțiune','Contestație la executare','Cod procedură civilă'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/amanare-executare-silita.src.html','w',encoding='utf-8').write(build(P))
