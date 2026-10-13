import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'avocat-recuperari-creante-pasii':('Avocat · creditor','Recuperarea creanței, pas cu pas',
   steps([('Analiza','Titlul și actele','Ce titlu ai, cât a rămas din prescripție'),('Notificarea','Somație cu dovadă','Suma, temeiul și un termen de plată'),('Titlul','Hotărâre sau ordonanță','Dacă nu ai deja un titlu executoriu'),('Executarea','La executor','Încuviințare în 3 zile (art. 666 CPC)'),('Încasarea','Distribuire','Sume eliberate de executor (art. 864 CPC)')],
   'Prescripția dreptului de a cere executarea: <b>3 ani</b> (art. 706 CPC).'),
   'Cod civil și Cod procedură civilă. Orientativ.','Pașii recuperării unei creanțe prin avocat: analiză, notificare, titlu executoriu, executare, încasare','Pașii recuperării prin avocat'),
 'avocat-sau-firma-de-recuperare':('Comparație','Avocat sau firmă de recuperare?',
   table(['','Avocat','Firmă de recuperare'],[['Ce poate face','Notificări, acțiune în instanță, executare','Notificări și negociere; în instanță doar prin avocat'],['Răspundere','Profesională, față de client','Contractuală; verifică autorizarea'],['Cost','Onorariu fix sau de succes, în scris','Comision din suma recuperată'],['Când se potrivește','Titlu slab sau litigiu','Creanțe mici, multe, necontestate']]),
   'Orientativ; condițiile concrete se stabilesc în contract.','Comparație avocat și firmă de recuperare creanțe: ce poate face fiecare, răspundere și cost','Avocat sau firmă de recuperare'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.select('Ce cale se potrivește <span class="accent">creanței tale</span>','Alege situația în care ești. Îți arătăm calea cea mai scurtă, termenul care contează și primul pas, după regulile din CPC.','Situația creanței',[
 ('Am o hotărâre judecătorească definitivă','Cerere de executare la executorul judecătoresc, direct.','Prescripția executării: 3 ani de la rămânerea definitivă (art. 706).','Depune cererea de executare cu hotărârea; ea întrerupe prescripția (art. 709).'),
 ('Am un contract de credit bancar sau alt înscris executoriu','Cerere de executare, fără proces prealabil.','3 ani de la nașterea dreptului de a cere executarea (art. 706).','Verifică dacă legea declară înscrisul executoriu (art. 632).'),
 ('Am doar o factură sau un contract civil','Somație, apoi ordonanță de plată sau acțiune obișnuită.','Prescripția dreptului la acțiune este de 3 ani (Codul civil); verifică scadența.','Trimite o somație cu dovadă de primire.'),
 ('Debitorul a intrat în insolvență','Cerere de admitere a creanței în procedură.','Executările se suspendă de drept (art. 75, Legea 85/2014).','Depune cererea de admitere la administratorul judiciar sau lichidator.'),
 ('Datoria este veche, mai mult de 3 ani','Analiză a întreruperilor și suspendărilor de prescripție.','Prescripția nu operează de drept; o invocă debitorul (art. 707).','Caută acte de plată, recunoaștere sau acte de executare (art. 709).')],
 0,'Exemplu: am o hotărâre definitivă','Calea recomandată','Termenul care contează','Primul pas','Orientativ, după CPC și Legea 85/2014. Alegerea finală depinde de dosar și de documente; cere o analiză a actelor înainte de a acționa.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Avocat pentru recuperări creanțe: răspuns rapid</h2>
        <p>Un avocat pentru recuperarea creanțelor analizează titlul și prescripția, trimite somația, obține un titlu executoriu dacă nu ai unul, depune cererea de executare și te reprezintă în instanță, la contestații și în insolvență. Rezultatul depinde de titlu, de documente și de ce bunuri are debitorul. Nu există garanția că banii se recuperează; există însă pași cu termene clare, iar cel mai scump lucru este să aștepți.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Dacă ai o hotărâre definitivă din 15 februarie 2024, poți cere executarea până la 15 februarie 2027 (3 ani, art. 706 CPC). Cererea de executare întrerupe prescripția și începe un nou termen de 3 ani (art. 709). Dacă mai aștepți, riști să pierzi dreptul de a executa.</p>
          <span class="formula">15.02.2024 + 3 ani = 15.02.2027</span>
          <button type="button" class="btn btn-line" data-ex="1">Vezi în calculator</button>
        </div>
        <p>Pentru traseul complet al legii, vezi ghidul despre <a href="/lege-recuperare-creante/">legea recuperării creanțelor</a>.</p>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce înseamnă recuperarea creanțelor</h2>
        <p>Recuperarea creanțelor înseamnă obținerea sumelor care ți se datorează: facturi neplătite, împrumuturi, daune, chirii. Poate fi amiabilă (notificare și negociere) sau juridică (proces și executare silită). Majoritatea dosarelor încep amiabil, dar ajung la instanță când debitorul nu răspunde sau contestă datoria.</p>
        <h3>Tipuri de creanțe</h3>
        <div class="roles">
          <div><b>Comerciale</b>Facturi între firme, contracte de furnizare, servicii.</div>
          <div><b>Civile</b>Împrumuturi între persoane, chirii, despăgubiri.</div>
          <div><b>Bancare</b>Credite neplătite; contractul bancar este, prin lege specială, titlu executoriu.</div>
          <div><b>Salariale și de întreținere</b>Au reguli proprii la executare (art. 729 CPC).</div>
        </div>
        <h3>Recuperare amiabilă sau juridică</h3>
        <p>Amiabil: somație, negociere, plan de plată în scris. Juridic: ordonanță de plată sau acțiune, apoi executare silită. Amiabila este mai ieftină, dar nu are forță dacă debitorul refuză. Procesul devine necesar când debitorul tace, contestă sau când se apropie termenul de prescripție.</p>'''
S3='''        <span class="eyebrow">Servicii</span>
        <h2>Ce servicii oferă avocatul de recuperări creanțe</h2>
        <ul class="chk">
          <li><b>Analiza cazului:</b> titlul, scadența, dobânzile, prescripția, bunurile debitorului.</li>
          <li><b>Notificarea debitorului:</b> somație cu dovadă de primire, prima etapă.</li>
          <li><b>Negocierea:</b> eșalonare scrisă, reducerea dobânzilor, garanții.</li>
          <li><b>Acțiunea în instanță:</b> ordonanță de plată (art. 1013 CPC) sau acțiune obișnuită, dacă nu ai titlu.</li>
          <li><b>Executarea silită:</b> cererea la executor, poprire, bunuri mobile și imobile.</li>
          <li><b>Insolvența debitorului:</b> cerere de admitere a creanței (art. 75 și urm., Legea 85/2014).</li>
        </ul>'''
S4='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura de recuperare, pas cu pas</h2>
        <ol class="num">
          <li><b>Analiza actelor.</b> Titlu, scadență, calcul, prescripție.</li>
          <li><b>Notificarea.</b> Somație cu suma, temeiul și un termen de plată.</li>
          <li><b>Titlul executoriu.</b> Dacă nu ai unul: ordonanță de plată sau acțiune.</li>
          <li><b>Cererea de executare.</b> Executorul decide în 3 zile (art. 666 CPC).</li>
          <li><b>Măsurile.</b> Poprire pe conturi și venituri (art. 781 CPC), sechestru, vânzare.</li>
          <li><b>Distribuirea.</b> Sumele ajung la tine prin executor (art. 864 CPC).</li>
        </ol>
'''+F('avocat-recuperari-creante-pasii')+'''
        <p>Detalii pe etape: <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>'''
S5='''        <span class="eyebrow">Durată și costuri</span>
        <h2>Cât durează și cât costă</h2>
        <h3>Durata</h3>
        <p>Nu există o durată fixă. Încuviințarea executării se dă în 3 zile, poprirea produce efecte din ziua în care banca primește adresa, iar terțul consemnează în 5 zile (art. 787 CPC). Procesul pentru obținerea titlului și vânzarea imobilelor durează mai mult și depind de instanță și de contestații.</p>
        <h3>Onorariile</h3>
        <p>Onorariul se stabilește prin contract scris. Formele uzuale sunt onorariul fix, onorariul pe etape sau un onorariu de succes (procent din suma recuperată). Cere o ofertă în scris, cu ce include și ce nu: taxe de timbru, onorariul executorului, expertize. Cheltuielile de executare sunt, de regulă, în sarcina debitorului (art. 670 CPC), dar tu le avansezi.</p>
        <h3>Avocat sau firmă de recuperare</h3>
'''+F('avocat-sau-firma-de-recuperare')
S6='''        <span class="eyebrow">Șanse</span>
        <h2>Șansele de recuperare: ce contează</h2>
        <p>Nimeni nu poate promite un procent de recuperare. Contează trei lucruri: titlul (hotărâre sau contract executoriu), documentele (contract, facturi, dovada livrării) și solvabilitatea debitorului (venituri, conturi, bunuri). Un titlu executoriu fără bunuri urmăribile nu aduce bani; invers, un debitor solvabil cu un titlu slab se poate apăra.</p>
        <h3>Riscuri</h3>
        <ul class="chk">
          <li>Prescripția: dreptul de a cere executarea se stinge în 3 ani, dacă debitorul o invocă (art. 706–707 CPC).</li>
          <li>Perimarea: 6 luni fără un act cerut de executor (art. 697 CPC).</li>
          <li>Insolvența debitorului: executările se suspendă și te înscrii la masa credală (art. 75, Legea 85/2014).</li>
          <li>Contestațiile debitorului, în general în 15 zile (art. 715 CPC).</li>
        </ul>'''
S7='''        <span class="eyebrow">Legislație</span>
        <h2>Legislația aplicabilă</h2>
        <p>Codul civil reglementează obligațiile, prescripția și cesiunea creanței. Codul de procedură civilă reglementează ordonanța de plată (art. 1013 și urm.) și executarea silită (art. 622 și urm.). Legea nr. 85/2014 intervine când debitorul intră în insolvență. Drepturile creditorului: să ceară toate modalitățile de executare, simultan sau succesiv (art. 666 alin. 4 CPC), și să indice bunurile urmărite (art. 731 CPC).</p>'''
S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și cum alegi avocatul</h2>
        <ul class="chk">
          <li><b>Amâni acțiunea</b> până se apropie prescripția.</li>
          <li><b>Lipsesc documentele:</b> contractul, facturile, corespondența, dovada primirii somației.</li>
          <li><b>Alegi un avocat fără contract clar</b> de onorarii și fără explicații despre riscuri.</li>
          <li><b>Plătești comisioane</b> unor firme fără autorizare verificată.</li>
        </ul>
        <h3>Cum alegi avocatul</h3>
        <p>Cere experiență pe recuperări și executări, un contract scris cu onorariu și etape, explicații despre prescripție și riscuri și rapoarte periodice. Fii atent la promisiuni de rezultat garantat: legea nu permite să garantezi un rezultat într-un proces.</p>'''
S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci dacă nu îți recuperezi banii</h2>
        <ol class="num">
          <li>Strânge titlul, contractul, facturile și dovezile de comunicare.</li>
          <li>Calculează ultima zi a termenului de prescripție (folosește calculatorul din <a href="/lege-recuperare-creante/">ghidul despre legea recuperării</a>).</li>
          <li>Trimite-ne actele în chat; îți spunem în aceeași zi calea și primul pas.</li>
        </ol>
        <!--@author practice="recuperare creanțe" -->'''
faq=[("Ce face un avocat de recuperări creanțe?","Analizează titlul și prescripția, trimite somația, obține titlul executoriu dacă nu ai unul, cere executarea și te reprezintă în instanță."),
("Cât durează recuperarea unei datorii?","Nu există o durată fixă. Încuviințarea executării se dă în 3 zile; procesul și vânzarea bunurilor pot dura luni sau ani."),
("Cât costă serviciile?","Onorariul se stabilește prin contract: fix, pe etape sau de succes. La cheltuielile de executare se adaugă taxele și onorariul executorului."),
("Pot recupera orice datorie?","Doar creanțe certe, lichide și exigibile, în termenul de prescripție. Datoria prescrisă nu mai poate fi executată dacă debitorul invocă prescripția."),
("Ce șanse am să recuperez banii?","Depind de titlu, documente și de bunurile debitorului. Nimeni nu poate garanta un procent."),
("Este obligatoriu procesul?","Nu, dacă ai deja un titlu executoriu sau debitorul plătește după somație. Altfel poți avea nevoie de ordonanță de plată sau de acțiune."),
("Ce înseamnă executarea silită?","Recuperarea datoriei prin executor judecătoresc, pe baza unui titlu executoriu: poprire, sechestru, vânzarea bunurilor."),
("Cum aleg un avocat bun?","Verifică experiența, contractul de onorarii, transparența și lipsa promisiunilor de rezultat garantat.")]
P=dict(slug='avocat-recuperari-creante',crumb='Avocat recuperări creanțe',
 title='Avocat recuperări creanțe: servicii, onorarii, procedură',
 desc='Cum te ajută un avocat să recuperezi o creanță: analiză, notificare, titlu executoriu, executare silită, prescripție de 3 ani, onorarii și diferența față de o firmă de recuperare.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#servicii|Servicii;#procedura|Procedura;#costuri|Costuri;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Avocat · creditor · executare silită',
  h1='Avocat pentru recuperări creanțe: <span class="accent">servicii, procedură și onorarii</span>',
  lead=['Ai facturi neplătite sau un împrumut dat și debitorul nu mai răspunde. Întrebarea nu e doar „cine mă ajută”, ci „ce pot face legal, în ce ordine și până când”, pentru că prescripția nu așteaptă.',
        'Aici afli ce face un avocat în fiecare etapă, cât durează, cum se stabilesc onorariile și cum diferă de o firmă de recuperare, plus un instrument care îți arată calea potrivită.'],
  meta2='Prescripție: 3 ani',cta='Alege situația ta',
  answer='Un avocat pentru recuperări creanțe analizează titlul și prescripția, trimite somația, obține un titlu executoriu dacă nu ai unul, depune cererea de executare (încuviințată în 3 zile, art. 666 CPC) și te reprezintă în instanță și în insolvență. Rezultatul depinde de titlu, de documente și de bunurile debitorului; nu poate fi garantat.',
  opts=[('Titlu','hotărâre, contract bancar, ordonanță'),('Încuviințare','3 zile'),('Prescripție','3 ani')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('servicii','Servicii',S3),('procedura','Procedura',S4),('costuri','Durată și costuri',S5),('sanse','Șanse',S6),('legislatie','Legislație',S7),('greseli','Greșeli',S8),('azi','Ce faci azi',S9)],
 faq=faq,faq_h2='Întrebări frecvente despre recuperări creanțe',
 contact=dict(h2='Ai o creanță de recuperat?',lead='Trimite-ne titlul, contractul sau factura și datele debitorului. Îți spunem în aceeași zi ce cale se potrivește și cât mai ai din prescripție. Consultația nu te obligă la nimic.',nav='/|Acasă;/lege-recuperare-creante/|Legea recuperării;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum recuperezi o creanță cu avocat',steps=[('Analiza cazului','Titlu, scadență, prescripție.'),('Notificarea','Somație cu dovadă de primire.'),('Titlul executoriu','Ordonanță de plată sau acțiune, dacă nu ai deja un titlu.'),('Executarea','Cerere la executor, poprire, sechestru.'),('Încasarea','Sumele se distribuie prin executor.')]),
 knows=['Recuperare creanțe','Executare silită','Prescripție','Ordonanță de plată'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/avocat-recuperari-creante.src.html','w',encoding='utf-8').write(build(P))
