import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
IMG1='ce-inseamna-executarea-silita-pe-scurt.webp'; IMG2='primii-pasi-cand-esti-executat-silit.webp'
calc='''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>Ce ai primit și <span class="accent">ce urmează</span></h2></div>
      <p>Alege actul pe care l-ai primit de la executor sau de la bancă. Îți arătăm ce înseamnă, de când curge termenul de contestație și care este primul pas.</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
          <div class="grp">Actul primit</div>
          <div class="field full"><label for="f-s">Ce ai în mână</label><div class="inp"><select id="f-s">
            <option value="0">Încheiere de încuviințare și somație de la executor</option>
            <option value="1">Adresă de poprire (cont sau salariu)</option>
            <option value="2">Proces-verbal de sechestru pe bunuri</option>
            <option value="3">Publicație de vânzare (licitație)</option>
            <option value="4">Nu am primit nimic, dar contul sau salariul sunt blocate</option>
          </select></div></div>
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Vezi ce înseamnă</button>
            <button type="button" class="btn btn-line" id="b-ex1">Exemplu: adresă de poprire</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
            <div class="opt full" id="c-t"><span class="k">Ce înseamnă</span><span class="v" id="o-t" style="font-size:19px">—</span><span class="s" id="o-ts">Alege actul primit.</span></div>
            <div class="opt" id="c-m"><span class="k">Termenul de contestație</span><span class="v" id="o-m" style="font-size:19px">—</span><span class="s" id="o-ms">15 zile, în general (art. 715 CPC).</span></div>
            <div class="opt" id="c-r"><span class="k">Primul pas</span><span class="v" id="o-r" style="font-size:19px">—</span><span class="s" id="o-rs">Ce faci chiar acum.</span></div>
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne actul primit</a>
          <span class="disc">Informare orientativă după CPC. Termenul exact depinde de actul contestat și de data primirii; folosește calculatorul din ghidul despre termenul contestației pentru ultima zi.</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
js=r'''  var D=[
   ['Executorul a încuviințat executarea; somația te cheamă să plătești.','15 zile libere de la primirea încheierii sau a somației (art. 715 alin. 1 pct. 3).','Fotografiază actele și notează data primirii.'],
   ['Executorul a blocat sumele de la bancă sau de la angajator, fără somație (art. 783).','15 zile de la înștiințarea despre poprire; la venituri periodice, cel mai târziu de la prima reținere (art. 715 alin. 1 pct. 2).','Cere copia adresei de poprire și verifică ce sume sunt nepopribile.'],
   ['Executorul a luat bunuri sub sechestru, pentru vânzare ulterioară.','15 zile de la data când ai luat cunoștință de act (art. 715 alin. 1 pct. 1).','Verifică lista bunurilor; unele sunt neurmăribile (art. 727).'],
   ['Bunurile sau imobilul urmează să fie vândute la licitație.','15 zile de la data când ai luat cunoștință de actul contestat (art. 715).','Cere dosarul executorului și verifică evaluarea și comunicările.'],
   ['Poprirea se înființează fără somație: primul semn poate fi contul blocat.','Termenul curge de la primul act aflat (art. 715 alin. 1 pct. 3).','Cere băncii și executorului copia adresei de poprire.']];
  function calc(){var s=parseInt($('f-s').value,10),d=D[s];$('o-t').textContent=d[0];$('o-m').textContent='15 zile';$('o-ms').textContent=d[1];$('o-r').textContent=d[2];$('c-t').classList.add('alert')}
  $('b-calc').addEventListener('click',calc);
  $('f-s').addEventListener('change',calc);
  function ex(){$('f-s').value='1';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Ce înseamnă executarea silită: răspuns rapid</h2>
        <p>Executarea silită înseamnă că datoria este recuperată cu forța, prin executor judecătoresc, fără acordul tău. Se pornește doar pe baza unui titlu executoriu: o hotărâre definitivă sau un înscris pe care legea îl declară executoriu, cum este contractul de credit bancar. Executorul poate bloca contul, reține din salariu, sechestra bunuri sau vinde un imobil. Ai, de regulă, 15 zile ca să contești.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Datorie de 12.000 lei, venit net de 3.000 lei. Din salariu se poate reține cel mult o treime: 1.000 lei pe lună. 12.000 ÷ 1.000 = 12 luni, fără dobânzi și cheltuieli de executare.</p>
          <span class="formula">12.000 ÷ (3.000 × 1/3) = 12 luni</span>
        </div>
        <h3>Ce trebuie să faci imediat</h3>
        <p>Notează data la care ai primit actul, fotografiază tot și nu plăti și nu semna nimic până nu verifici titlul și suma. Pașii în detaliu sunt mai jos și în ghidul despre <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este executarea silită, pe înțelesul tuturor</h2>
        <p>Dacă o datorie nu este plătită de bunăvoie, creditorul nu își poate lua banii singur. Trebuie să treacă prin stat: un executor judecătoresc, singurul care face acte de executare (art. 623 CPC). Acesta lucrează după reguli stricte: are nevoie de un titlu executoriu (art. 632), iar creanța trebuie să fie certă, lichidă și exigibilă (art. 663).</p>
        <h3>Cine este creditorul și cine este debitorul</h3>
        <p>Creditorul este cel care are de primit: o bancă, o firmă, o persoană. Debitorul este cel urmărit. Executorul nu ia partea nimănui: aplică legea la cererea creditorului, iar debitorul are drept de contestație.</p>
        <h3>Ce nu este executarea silită</h3>
        <ul class="chk">
          <li>Telefoanele și scrisorile unui recuperator: pot fi presiune, dar nu sunt executare.</li>
          <li>Somația trimisă de creditor înainte de proces: este o notificare, nu un act al executorului.</li>
          <li>O hotărâre pronunțată de instanță: este doar baza (titlul), executarea vine după.</li>
        </ul>
        <h3>Termeni pe care îi vei întâlni</h3>
        <div class="roles">
          <div><b>Titlu executoriu</b>Hotărârea sau înscrisul care permite executarea (art. 632).</div>
          <div><b>Încheiere de încuviințare</b>Decizia executorului că executarea poate începe (art. 666).</div>
          <div><b>Somație</b>Chemarea de a plăti, comunicată debitorului (art. 668).</div>
          <div><b>Poprire</b>Blocarea sumelor pe care un terț (banca, angajatorul) ți le datorează (art. 781).</div>
          <div><b>Sechestru</b>Indisponibilizarea bunurilor pentru vânzare.</div>
          <div><b>Terț poprit</b>Banca sau angajatorul care primește adresa de poprire.</div>
        </div>'''
S3='''        <span class="eyebrow">Când începe</span>
        <h2>Când începe executarea și cum afli</h2>
        <p>Creditorul cere executarea, iar executorul decide în cel mult 3 zile, fără să te cheme (art. 666 alin. 1–2). Apoi primești încheierea, titlul și, de regulă, o somație (art. 667–668). Dacă se pornește poprirea, nu există somație: adresa merge întâi la bancă sau la angajator (art. 783 alin. 1), iar tu ești înștiințat prin copie.</p>
        <p>De aceea, primul semn poate fi un card refuzat sau un salariu mai mic. Termenul de contestație nu pornește din ziua în care ai observat, ci din ziua în care ai primit sau ai aflat de act (art. 715).</p>
'''+fig(IMG1,'ce înseamnă executarea silită: cine, ce și când, de la cerere la încuviințare și măsuri','Executarea silită, pe scurt')
S4='''        <span class="eyebrow">Forme</span>
        <h2>Formele de executare: poprire, bunuri mobile, imobile</h2>
        <div class="t-grid">
          <div class="t-card"><h4>Poprirea</h4><p>Se aplică sumelor datorate ție de un terț: bancă, angajator, chiriaș. Se pot popri soldul și încasările viitoare din cont (art. 781 alin. 2). Detalii în ghidul despre <a href="/poprire-cont/">poprirea pe cont</a>.</p></div>
          <div class="t-card"><h4>Bunuri mobile</h4><p>Mașini, echipamente, bunuri de valoare se sechestrează și se vând la licitație. Nu pot fi urmărite bunurile de uz personal indispensabile, alimentele pe 3 luni și combustibilul pe iarnă (art. 727).</p></div>
          <div class="t-card"><h4>Imobile</h4><p>Urmărirea se notează în cartea funciară, iar imobilul se vinde la licitație. Este forma cea mai lentă și mai scumpă.</p></div>
        </div>
        <h3>Cât din venit poate fi reținut</h3>
        <p>Salariul și pensia pot fi urmărite până la o treime din venitul net pentru datorii obișnuite; dacă sunt mai multe urmăriri, totalul nu depășește jumătate (art. 729 alin. 1–2). Alocațiile de stat, indemnizațiile pentru copii și bursele nu pot fi urmărite pentru nicio datorie (art. 729 alin. 7).</p>'''
S5='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile debitorului în executarea silită</h2>
        <ul class="chk">
          <li><b>Contestația la executare</b>, în general în 15 zile (art. 712, 715). Vezi <a href="/contestatie-la-executare/">contestația la executare</a>.</li>
          <li><b>Suspendarea executării</b>, cu cauțiune, cerută instanței (art. 719). Vezi <a href="/amanare-executare-silita/">amânarea și suspendarea</a>.</li>
          <li><b>Prescripția:</b> dreptul de a cere executarea se prescrie în 3 ani, dacă o invoci (art. 706–707).</li>
          <li><b>Consemnarea:</b> poți opri măsurile depunând întreaga creanță, cu accesoriile și cheltuielile (art. 721).</li>
          <li><b>Restrângerea executării</b> când valoarea bunurilor urmărite e vădit excesivă (art. 702).</li>
        </ul>
        <h3>Drepturile creditorului</h3>
        <p>Creditorul are dreptul să ceară toate modalitățile de executare, simultan sau succesiv (art. 666 alin. 4), și să indice bunurile ce vor fi urmărite (art. 731). Dacă lasă să treacă 6 luni fără un act cerut în scris de executor, executarea se perimă (art. 697).</p>'''
S6='''        <span class="eyebrow">Durată și costuri</span>
        <h2>Cât durează și cât costă</h2>
        <p>Legea nu fixează o durată totală. Încuviințarea se dă în 3 zile, poprirea produce efecte din ziua în care banca primește adresa, iar terțul consemnează în 5 zile (art. 787). Vânzarea unui imobil poate dura luni sau ani. Orientativ, o poprire pe salariu durează cât plata ratelor reținute lunar.</p>
        <p>Cheltuielile le suportă, de regulă, debitorul: taxe de timbru, onorariul executorului, onorariul avocatului creditorului și costul actelor (art. 670). Dacă plătești de îndată după somație, datorezi doar actele efectiv făcute și onorariile proporționale (art. 670 alin. 2). O contestație costă o taxă de timbru de cel mult 1.000 lei (art. 10 OUG 80/2013).</p>'''
S7='''        <span class="eyebrow">Oprire</span>
        <h2>Cum poți opri executarea silită</h2>
        <div class="tbl wide"><table>
          <thead><tr><th></th><th>Negociere</th><th>Contestație</th><th>Suspendare</th></tr></thead>
          <tbody>
            <tr><td>Scop</td><td>Eșalonare sau reducere</td><td>Anularea actului sau a executării</td><td>Oprirea executării până la decizie</td></tr>
            <tr><td>Cost</td><td>Fără taxă</td><td>Taxă de timbru, până la 1.000 lei</td><td>Taxă 50 lei + cauțiune</td></tr>
            <tr><td>Termen</td><td>Oricând, cu acordul creditorului</td><td>15 zile, în general</td><td>Odată cu contestația sau separat</td></tr>
            <tr><td>Risc</td><td>Creditorul poate refuza</td><td>Se respinge dacă e tardivă</td><td>Cauțiunea poate fi pierdută</td></tr>
          </tbody>
        </table></div>
'''+fig(IMG2,'primii pași când ești executat silit: notezi data, ceri dosarul, verifici titlul, contești în 15 zile, ceri suspendarea','Primii pași când ești executat silit')+'''
        <p>Orice înțelegere cu creditorul se face în scris. Dacă ți se suspendă executarea la cererea creditorului, măsurile deja luate, inclusiv blocarea conturilor, rămân în ființă dacă nu se dispune altfel (art. 701 alin. 3).</p>'''
S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și ce faci dacă ești executat silit</h2>
        <ul class="chk">
          <li>Ignori actele, pentru că „oricum nu am bani”.</li>
          <li>Plătești fără să ceri calculul sumei, cu dobânzi și cheltuieli.</li>
          <li>Muți bani sau bunuri: nu ajută, iar plata sau cesiunea creanței poprite nu se opune creditorului (art. 784 alin. 4).</li>
          <li>Contești după 15 zile.</li>
        </ul>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată la data la care acționezi.</p>'''
S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Notează data primirii fiecărui act și fotografiază tot.</li>
          <li>Cere executorului copia dosarului și calculul sumei.</li>
          <li>Trimite-ne actele în chat; îți spunem în aceeași zi dacă merită contestația, suspendarea sau o negociere.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Ce înseamnă executarea silită?","Recuperarea unei datorii prin executor judecătoresc, pe baza unui titlu executoriu, fără acordul debitorului: poprire, sechestru, vânzarea bunurilor."),
("Cine poate începe executarea silită?","Creditorul care are un titlu executoriu, prin cerere la executorul judecătoresc (art. 664 CPC)."),
("Cât durează procedura?","Legea nu fixează o durată. Încuviințarea se dă în 3 zile; ritmul de după depinde de forma de executare."),
("Ce este poprirea pe cont?","Blocarea sumelor din conturile tale prin adresa trimisă băncii, fără somație (art. 781–783)."),
("Pot opri executarea silită?","Da, prin plata sau consemnarea datoriei, prin înțelegere cu creditorul sau prin suspendarea cerută instanței, cu cauțiune (art. 719, 721)."),
("Ce drepturi are debitorul?","Contestația la executare, suspendarea, protecția veniturilor (art. 729), prescripția și consemnarea creanței."),
("Cât costă executarea silită?","Cheltuielile (taxe, onorariul executorului, onorariul avocatului) se adaugă, de regulă, la datorie. Plata imediată după somație le reduce (art. 670)."),
("Ce fac dacă primesc somație?","Notezi data, ceri dosarul, verifici titlul și suma, apoi alegi între plată, înțelegere și contestație în 15 zile.")]
P=dict(slug='executare-silita-definitie',crumb='Ce înseamnă executarea silită',
 title='Ce înseamnă executarea silită: procedură și drepturi',
 desc='Ce înseamnă executarea silită, pe înțelesul tuturor: cine o pornește, ce poate bloca executorul, cât din venit se reține, ce drepturi ai și cum o oprești.',
 nav='#calculator|Ce ai primit;#raspuns|Răspuns rapid;#forme|Forme;#drepturi|Drepturi;#oprire|Cum o oprești;#intrebari|Întrebări',
 images=[IMG1,IMG2],
 hero=dict(eyebrow='Definiție · titlu executoriu · drepturi',
  h1='Ce înseamnă executarea silită: <span class="accent">procedura și drepturile debitorului</span>',
  lead=['Ai auzit cuvântul „executare silită” de la bancă, de la un vecin sau dintr-un plic cu antet de executor, și nu e clar ce urmează. Poate ți se pare că „nu se poate lua nimic”, poate că ți s-a blocat deja cardul.',
        'Aici afli, în limbaj simplu, ce înseamnă, cine o pornește, ce poate lua executorul și ce nu, cât durează și cum o oprești, plus un mic instrument: alege actul pe care l-ai primit și vezi ce înseamnă.'],
  meta2='Contestație: 15 zile',cta='Vezi ce ai primit',
  answer='Executarea silită înseamnă recuperarea unei datorii prin executor judecătoresc, fără acordul debitorului, pe baza unui titlu executoriu (hotărâre definitivă sau un înscris declarat executoriu de lege, cum este contractul de credit bancar). Executorul poate bloca contul, reține din salariu, sechestra bunuri sau vinde un imobil. Debitorul are, de regulă, 15 zile ca să conteste (art. 715 CPC).',
  opts=[('Cine','executor judecătoresc'),('Temei','titlu executoriu'),('Contestație','15 zile')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('cand','Când începe',S3),('forme','Forme',S4),('drepturi','Drepturi',S5),('costuri','Durată și costuri',S6),('oprire','Cum o oprești',S7),('greseli','Greșeli',S8),('azi','Ce faci azi',S9)],
 faq=faq,faq_h2='Întrebări frecvente despre executarea silită',
 contact=dict(h2='Ai primit un act de executare?',lead='Trimite-ne încheierea, somația sau adresa de poprire. Îți spunem în aceeași zi ce înseamnă și ce poți face. Consultația nu te obligă la nimic.',nav='/|Acasă;/procedura-executare-silita-etape/|Procedura;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Ce faci când ești executat silit',steps=[('Notezi data primirii','Termenul de 15 zile curge de aici.'),('Ceri dosarul','Titlul, calculul și actele executorului.'),('Verifici titlul și suma','Titlu executoriu, creanță certă, lichidă, exigibilă.'),('Alegi calea','Plată, înțelegere sau contestație.'),('Ceri suspendarea','Dacă ai motive temeinice, cu cauțiune.')]),
 knows=['Executare silită','Titlu executoriu','Poprire','Contestație la executare','Cod procedură civilă'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/executare-silita-definitie.src.html','w',encoding='utf-8').write(build(P))
