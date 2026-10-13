import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'perimarea-executarii-pasii':('Art. 697–699 CPC','Perimarea executării silite',
   steps([('Cererea scrisă','A executorului','Creditorul e invitat să facă un act necesar executării'),('Inactivitate','6 luni','Din culpa creditorului, fără act sau demers (art. 697)'),('Perimare','De drept','Se constată de instanța de executare (art. 698)'),('Efect','Actele se desființează','Cu excepția celor care au dus la plata unei părți'),('Nouă cerere','În prescripție','Creditorul poate reîncepe (art. 699)')],
   'Dacă executarea a fost <b>suspendată</b>, termenul de perimare curge de la încetarea suspendării (art. 697 alin. 2).'),
   'Cod procedură civilă, art. 697–699. Orientativ.','Perimarea executării silite: cerere scrisă a executorului, 6 luni de inactivitate, constatare de instanță, desființarea actelor, nouă cerere','Perimarea executării silite, pas cu pas'),
 'perimare-prescriptie-suspendare':('Comparație','Perimare, prescripție, suspendare',
   table(['','Perimare','Prescripție','Suspendare'],[['Termen','6 luni (art. 697)','3 ani (art. 706)','Cât durează cauza suspendării'],['Pornește de la','Cererea scrisă a executorului rămasă fără răspuns','Rămânerea definitivă a hotărârii sau nașterea dreptului','Lege, instanță sau cererea creditorului (art. 701)'],['Operează','De drept; o constată instanța de executare','Doar la cerere (art. 707)','Prin încheiere sau prin lege'],['Efect','Se desființează actele de executare (art. 698)','Se stinge dreptul de a executa','Executarea se oprește temporar']]),
   'Orientativ; condițiile exacte sunt în CPC.','Perimare, prescripție și suspendare: termen, de când curge, cum operează și efect','Perimare, prescripție, suspendare'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.deadline('Când se împlinesc <span class="accent">6 luni de perimare</span>','Introdu data la care creditorul a primit cererea scrisă a executorului (sau data încetării suspendării). Vezi când se poate împlini termenul de perimare de 6 luni (art. 697 CPC), dacă creditorul rămâne inactiv din culpa sa.','De când curge termenul',[
 ('De la cererea scrisă a executorului către creditor','6 luni de la cererea scrisă a executorului rămasă fără răspuns din culpa creditorului (art. 697 alin. 1).'),
 ('De la încetarea suspendării executării (nu la cererea creditorului)','Dacă executarea a fost suspendată, termenul curge de la încetarea suspendării (art. 697 alin. 2).')],
 'Data de la care curge termenul','2026-04-15','Exemplu: cerere scrisă la 15 aprilie 2026','Perimarea se poate constata după','Calcul orientativ: 6 luni calendaristice, mutate la prima zi lucrătoare dacă ultima zi cade în weekend sau sărbătoare. Perimarea cere culpa creditorului și cererea scrisă a executorului; nu operează pentru simpla trecere a timpului. O constată instanța de executare (art. 698). Nu se suspendă cât timp executarea e suspendată la cererea creditorului.',m=6)
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Perimarea executării silite: răspuns rapid</h2>
        <p>Perimarea executării silite înseamnă că executarea se stinge de drept dacă, din culpa sa, creditorul lasă să treacă 6 luni fără să facă un act sau un demers necesar executării, care i-a fost cerut în scris de executor (art. 697 alin. 1 CPC). O constată instanța de executare, la cererea executorului sau a părții interesate, prin încheiere dată cu citarea în termen scurt (art. 698). Efectul: actele de executare se desființează, în afară de cele care au dus deja la realizarea în parte a creanței.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Executorul cere în scris creditorului, pe 15 aprilie 2026, să depună un act necesar (de exemplu avansul cheltuielilor sau indicarea bunurilor). Dacă, din culpa sa, creditorul nu face nimic până pe 15 octombrie 2026, executarea poate fi socotită perimată. Perimarea nu apare însă „automat” în dosar: o constată instanța, iar tu o invoci prin cerere sau contestație.</p>
          <span class="formula">15.04.2026 + 6 luni = 15.10.2026</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este executarea silită și rolul executorului</h2>
        <p>Executarea silită este recuperarea unei datorii prin executor judecătoresc, pe baza unui titlu executoriu (art. 632 CPC). Creditorul pornește executarea prin cerere (art. 664) și are obligația să sprijine executorul și să avanseze cheltuielile necesare (art. 647 alin. 1). Tocmai aceste obligații stau la baza perimării: dacă nu le îndeplinește, executarea poate muri. Despre etape, vezi <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>'''
S3='''        <span class="eyebrow">Art. 697</span>
        <h2>Ce înseamnă perimarea și când intervine</h2>
        <p>Condițiile sunt cumulative: (1) executorul i-a cerut creditorului, în scris, un act sau un demers necesar executării; (2) au trecut 6 luni; (3) creditorul nu a făcut nimic din culpa sa. Fără cererea scrisă a executorului, termenul nu curge. În caz de suspendare, termenul de perimare curge de la încetarea suspendării, iar când suspendarea este la cererea creditorului, termenul nu se suspendă (art. 697 alin. 2).</p>
        <h3>Perimare, prescripție și suspendare</h3>
'''+F('perimare-prescriptie-suspendare')+'''
        <p>Diferența practică: prescripția pune capăt dreptului de a cere executarea (3 ani, art. 706–707), perimarea pune capăt unei executări începute, dar creditorul poate relua în termenul de prescripție (art. 699).</p>'''
S4='''        <span class="eyebrow">Calcul</span>
        <h2>Cum calculezi termenul de perimare</h2>
        <ol class="num">
          <li>Găsește cererea scrisă a executorului către creditor (data și ce act cerea).</li>
          <li>Numără 6 luni de la comunicarea ei către creditor.</li>
          <li>Verifică dacă a existat o suspendare: dacă da, numeri de la încetarea ei.</li>
          <li>Verifică dacă, între timp, creditorul a făcut actul cerut sau altceva util executării: dacă da, nu mai e vorba de inactivitate din culpă.</li>
        </ol>
'''+F('perimarea-executarii-pasii')
S5='''        <span class="eyebrow">Procedura</span>
        <h2>Cum invoci perimarea și cu ce rezultat</h2>
        <p>Perimarea se constată de instanța de executare, la cererea executorului sau a părții interesate, prin încheiere dată cu citarea în termen scurt (art. 698 alin. 1). În practică, debitorul cere constatarea perimării sau o invocă într-o contestație la executare (art. 712). Depui la instanța de executare, în general în 15 zile de la actul pe care îl contești (art. 715). Vezi <a href="/contestatie-la-executare/">contestația la executare</a>.</p>
        <h3>Ce trebuie să dovedești</h3>
        <ul class="chk">
          <li>Cererea scrisă a executorului către creditor și data comunicării.</li>
          <li>Trecerea a 6 luni fără răspuns sau act din partea creditorului.</li>
          <li>Lipsa unei suspendări care să fi oprit termenul și lipsa altor acte ale creditorului.</li>
        </ul>'''
S6='''        <span class="eyebrow">Efecte</span>
        <h2>Efectele perimării și posibilitatea unei noi executări</h2>
        <p>Perimarea atrage desființarea tuturor actelor de executare, cu excepția celor care au dus la realizarea, în parte, a creanței și a accesoriilor (art. 698 alin. 2). Creditorul poate face, în termenul de prescripție, o nouă cerere de executare; executorul comunică atunci debitorului încheierea și o nouă somație (art. 699). Executarea perimată nu mai întrerupe prescripția (art. 709 alin. 3), deci dacă termenul de 3 ani s-a împlinit între timp, creditorul poate pierde dreptul la executare.</p>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente ale debitorilor</h2>
        <ul class="chk">
          <li><b>Confunzi perimarea cu prescripția:</b> termene și efecte diferite.</li>
          <li><b>Pornești de la „6 luni fără acte”</b> fără să verifici cererea scrisă a executorului.</li>
          <li><b>Contești prea târziu</b> actul care te vizează, peste cele 15 zile.</li>
          <li><b>Nu ceri dosarul</b> pentru a vedea ce a cerut executorul și când.</li>
        </ul>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>'''
S8='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Cere executorului copia dosarului și caută cererile scrise către creditor.</li>
          <li>Calculează termenul cu calculatorul și verifică suspendările.</li>
          <li>Trimite-ne dosarul în chat; îți spunem în aceeași zi dacă poți invoca perimarea.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Ce este perimarea executării silite?","Stingerea de drept a executării dacă, din culpa creditorului, au trecut 6 luni fără un act sau demers cerut în scris de executor (art. 697 CPC)."),
("Care este termenul de perimare?","6 luni, de la cererea scrisă a executorului către creditor. În caz de suspendare, termenul curge de la încetarea ei (art. 697)."),
("Cum se calculează termenul?","Numeri 6 luni de la comunicarea cererii scrise a executorului, după ce verifici suspendările și actele făcute de creditor."),
("Care este diferența dintre perimare și prescripție?","Perimarea stinge o executare începută, după 6 luni de inactivitate din culpă; prescripția stinge dreptul de a cere executarea, în 3 ani (art. 706)."),
("Cum pot invoca perimarea?","Prin cerere de constatare sau în contestația la executare, la instanța de executare, care o constată prin încheiere (art. 698)."),
("Ce efecte produce perimarea?","Se desființează actele de executare, în afară de cele care au dus la realizarea în parte a creanței (art. 698 alin. 2)."),
("Pot anula executarea silită prin contestație?","Da, dacă instanța admite contestația (art. 720 CPC). Perimarea poate fi unul dintre motive."),
("Ce acte întrerup termenul de perimare?","Orice act sau demers necesar executării pe care creditorul îl face la cererea executorului; plata sau recunoașterea de către debitor întrerupe prescripția (art. 709), nu perimarea.")]
P=dict(slug='perimarea-executarii-silite',crumb='Perimarea executării silite',
 title='Perimarea executării silite: termen de 6 luni, efecte',
 desc='Ce înseamnă perimarea executării silite: termenul de 6 luni (art. 697 CPC), cum se constată, ce efecte are, diferența față de prescripție și cum o invoci într-o contestație.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#termen|Art. 697;#procedura|Procedura;#efecte|Efecte;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Art. 697–699 CPC · 6 luni · constatare de instanță',
  h1='Perimarea executării silite: <span class="accent">termenul de 6 luni și anularea executării</span>',
  lead=['Dosarul de executare stă pe loc de luni de zile și te întrebi dacă executarea „s-a stins”. Răspunsul nu e „după 6 luni, automat”: perimarea cere o cerere scrisă a executorului, culpa creditorului și constatarea instanței.',
        'Aici vezi condițiile, calculul, efectele și cum o invoci, cu un calculator pentru cele 6 luni.'],
  meta2='Termen: 6 luni',cta='Calculează termenul',
  answer='Perimarea executării silite înseamnă că executarea se stinge de drept dacă, din culpa creditorului, au trecut 6 luni fără un act sau demers cerut în scris de executor (art. 697 CPC). O constată instanța de executare prin încheiere (art. 698). Efectul: actele de executare se desființează, în afară de cele care au dus la plata în parte a creanței; creditorul poate relua în termenul de prescripție (art. 699).',
  opts=[('Termen','6 luni (art. 697)'),('Condiție','cerere scrisă a executorului'),('Efect','actele se desființează')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('termen','Art. 697',S3),('calcul','Calcul',S4),('procedura','Procedura',S5),('efecte','Efecte',S6),('greseli','Greșeli',S7),('azi','Ce faci azi',S8)],
 faq=faq,faq_h2='Întrebări frecvente despre perimarea executării silite',
 contact=dict(h2='Crezi că executarea s-a perimat?',lead='Trimite-ne dosarul de executare și cererile executorului către creditor. Îți spunem în aceeași zi dacă poți invoca perimarea. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum invoci perimarea executării silite',steps=[('Găsești cererea scrisă a executorului','Către creditor, cu data comunicării.'),('Numeri 6 luni','De la comunicare sau de la încetarea suspendării.'),('Verifici actele creditorului','Dacă a făcut actul cerut, nu e inactivitate din culpă.'),('Ceri constatarea','La instanța de executare sau în contestație.'),('Aștepți încheierea','Actele de executare se desființează.')]),
 knows=['Perimare','Executare silită','Contestație la executare','Cod procedură civilă'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/perimarea-executarii-silite.src.html','w',encoding='utf-8').write(build(P))
