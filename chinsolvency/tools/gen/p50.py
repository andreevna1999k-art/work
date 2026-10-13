import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'cine-intra-sub-legea-insolventei':('Insolvență · cine și cum','Care lege ți se aplică?',
   table(['Debitor','Lege','Procedura'],[['Profesionist (societate, PFA, întreprindere)','Legea nr. 85/2014 (art. 3)','Reorganizare judiciară sau faliment'],['Regie autonomă','Legea nr. 85/2014 (art. 3 alin. 2)','Aceeași lege'],['Profesie liberală','Excluse din Legea 85/2014 (art. 3 alin. 1)','Regim propriu, dacă există'],['Persoană fizică neprofesionistă','Legea nr. 151/2015','Procedură separată, la judecătorie']]),
   'Legea nr. 85/2014, art. 3; Legea nr. 151/2015. Orientativ; verifică forma consolidată.','Care lege de insolvență se aplică: profesioniști, regii autonome, profesii liberale și persoane fizice neprofesioniste','Care lege de insolvență se aplică'),
 'etapele-insolventei-pe-scurt':('Legea 85/2014','Etapele insolvenței, pe scurt',
   steps([('Cererea','Debitor sau creditor','Art. 66 și art. 70'),('Deschiderea','Judecătorul-sindic','Procedură generală sau simplificată (art. 71)'),('Suspendarea','De drept','Executările individuale (art. 75)'),('Creanțele','Cereri de admitere','Tabel preliminar și definitiv'),('Soluția','Plan sau faliment','Reorganizare (art. 132) sau lichidare (art. 145)')],
   'Reorganizarea judiciară se aplică <b>persoanelor juridice</b>; planul nu poate depăși 3 ani (art. 133 alin. 3).'),
   'Legea nr. 85/2014. Orientativ.','Etapele insolvenței pe scurt: cerere, deschidere, suspendarea executărilor, cereri de admitere a creanțelor, plan sau faliment','Etapele insolvenței pe scurt'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.select('Ce lege <span class="accent">ți se aplică</span>','Alege cine ești. Îți arătăm legea aplicabilă, la ce instanță se depune cererea și primul pas.','Cine este debitorul',[
 ('Societate comercială sau alt profesionist','Legea nr. 85/2014, procedura generală sau simplificată.','Tribunalul (cererea debitorului: art. 66 alin. 1).','Stabilește starea de insolvență și termenul de 30 de zile.'),
 ('Persoană fizică autorizată sau întreprindere familială','Legea nr. 85/2014, de regulă procedura simplificată (art. 38 alin. 2).','Tribunalul.','Verifică dacă ești profesionist înregistrat și adună situația financiară.'),
 ('Regie autonomă','Legea nr. 85/2014 (art. 3 alin. 2).','Tribunalul.','Verifică regimul special aplicabil regiilor.'),
 ('Profesie liberală (avocat, medic, arhitect etc.)','Nu se aplică Legea 85/2014 (art. 3 alin. 1).','Depinde de legea specială; întreabă un specialist.','Verifică regimul propriu profesiei.'),
 ('Persoană fizică neprofesionistă, cu datorii personale','Legea nr. 151/2015 (insolvența persoanelor fizice).','Judecătoria (art. 10 din Legea 151/2015).','Verifică condițiile și comisia de insolvență din Legea 151/2015.')],
 0,'Exemplu: societate comercială','Legea aplicabilă','Instanța','Primul pas','Orientativ. Lista categoriilor de debitori și regimurile speciale sunt în Legea nr. 85/2014, art. 3; pentru persoane fizice, în Legea nr. 151/2015. Verifică forma consolidată.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Insolvența explicată simplu: răspuns rapid</h2>
        <p>Insolvența este starea patrimoniului debitorului în care fondurile bănești disponibile nu ajung pentru plata datoriilor certe, lichide și exigibile (art. 5 pct. 29 din Legea nr. 85/2014). Insolvența se prezumă după 60 de zile de la scadență fără plată, prezumție relativă. Nu înseamnă automat faliment: procedura poate duce la reorganizare pe bază de plan sau la lichidare. Legea nr. 85/2014 se aplică profesioniștilor; persoanele fizice neprofesioniste au Legea nr. 151/2015.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>O societate nu a plătit un furnizor la scadență, 1 august. După 60 de zile, adică la 30 septembrie, insolvența se prezumă (art. 5 pct. 29). Debitorul are obligația să ceară deschiderea procedurii în 30 de zile de la apariția stării de insolvență (art. 66).</p>
          <span class="formula">scadență + 60 de zile = prezumția de insolvență</span>
          <button type="button" class="btn btn-line" data-ex="1">Vezi legea aplicabilă</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este insolvența și cum se deosebește de faliment</h2>
        <p>Insolvența este o stare financiară; falimentul este o formă a procedurii. Legea distinge insolvența vădită de cea iminentă: aceasta din urmă apare când se dovedește că debitorul nu va putea plăti la scadență datoriile exigibile cu fondurile disponibile atunci (art. 5 pct. 29 lit. b). Procedura colectivă urmărește acoperirea pasivului debitorului, iar judecătorul-sindic o conduce sub controlul instanței. Pentru diferența practică, vezi <a href="/insolventa-sau-faliment/">insolvență sau faliment</a>.</p>
        <h3>Cine intră sub lege</h3>
'''+F('cine-intra-sub-legea-insolventei')
S3='''        <span class="eyebrow">Firme</span>
        <h2>Insolvența firmelor: obligații și reorganizare</h2>
        <p>Administratorii firmei în insolvență trebuie să ceară deschiderea procedurii în 30 de zile de la apariția stării de insolvență, cu notificarea organului fiscal (art. 66 alin. 1). Cererea se depune la tribunal. După deschidere, executările individuale se suspendă de drept (art. 75) și creditorii își depun cererile de admitere a creanțelor. Debitorul persoană juridică poate propune un plan de reorganizare; dacă nu există plan sau acesta eșuează, se trece la faliment (art. 145). Despre cerere și termen, vezi <a href="/insolventa-voluntara/">insolvența voluntară</a>.</p>'''
S4='''        <span class="eyebrow">Persoane fizice</span>
        <h2>Persoanele fizice neprofesioniste</h2>
        <p>Pentru persoanele fizice care nu sunt profesioniști, insolvența este reglementată de Legea nr. 151/2015 privind procedura insolvenței persoanelor fizice, cu organe proprii (comisia de insolvență) și cu posibilitatea eliberării de datoriile reziduale. Cererea se depune la judecătorie, nu la tribunal (art. 10). Condițiile exacte (praguri, bunuri, plan de rambursare) trebuie verificate în textul consolidat al acelei legi; nu le preluăm aici din memorie.</p>'''
S5='''        <span class="eyebrow">Etape</span>
        <h2>Etapele procedurii de insolvență (Legea 85/2014)</h2>
'''+F('etapele-insolventei-pe-scurt')+'''
        <ol class="num">
          <li><b>Cererea:</b> a debitorului (art. 66) sau a creditorului (art. 70).</li>
          <li><b>Deschiderea:</b> judecătorul-sindic pronunță încheierea de deschidere (procedură generală sau simplificată, art. 71) și desemnează un administrator judiciar provizoriu sau un lichidator (art. 73).</li>
          <li><b>Suspendarea executărilor</b> de drept (art. 75).</li>
          <li><b>Creanțele:</b> creditorii depun cererile de admitere (art. 104), apoi se întocmesc tabelele de creanțe.</li>
          <li><b>Soluția:</b> plan de reorganizare (art. 132 și urm.) sau faliment, cu lichidarea averii (art. 154 și urm.).</li>
          <li><b>Închiderea procedurii.</b></li>
        </ol>
        <p>Pe larg: <a href="/procedura-insolventei-etape/">procedura insolvenței, etapele</a>.</p>'''
S6='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile debitorului și ale creditorilor</h2>
        <ul class="chk">
          <li><b>Debitorul:</b> beneficiază de suspendarea executărilor (art. 75), dar depune actele (art. 74) și respectă planul. Furnizorii de utilități nu îi pot întrerupe serviciile în observație și reorganizare dacă e consumator captiv (art. 77).</li>
          <li><b>Creditorii:</b> își valorifică creanțele numai în procedură (art. 75). Creditorul cu cauză de preferință poate cere ridicarea suspendării în condițiile art. 78. Votează planul (art. 139).</li>
          <li><b>Ordinea de plată:</b> la distribuire, sumele se plătesc în ordinea legii (art. 159 pentru bunurile grevate de garanții).</li>
        </ul>'''
S7='''        <span class="eyebrow">Riscuri</span>
        <h2>Avantaje, riscuri și greșeli frecvente</h2>
        <ul class="chk">
          <li><b>Avantaj:</b> executările se opresc și creditorii intră într-o procedură colectivă.</li>
          <li><b>Risc:</b> pierderea administrării averii în faliment (art. 145 alin. 2) și dizolvarea persoanei juridice.</li>
          <li><b>Greșeli:</b> depunerea tardivă a cererii (termen de 30 de zile), lipsa actelor contabile, ascunderea bunurilor.</li>
        </ul>
        <p>Textele din Legea nr. 85/2014 sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>'''
S8='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Cum te pregătești</h2>
        <ol class="num">
          <li>Stabilește dacă ești profesionist sau persoană fizică neprofesionistă (calculator).</li>
          <li>Strânge situațiile financiare, lista bunurilor, a creditorilor și a plăților din ultimele 6 luni (art. 67).</li>
          <li>Trimite-ne datele în chat; îți spunem în aceeași zi ce procedură se potrivește.</li>
        </ol>
        <!--@author practice="insolvență" -->'''
faq=[("Ce înseamnă insolvența?","Starea patrimoniului în care fondurile disponibile nu ajung pentru plata datoriilor certe, lichide și exigibile (art. 5 pct. 29 din Legea nr. 85/2014)."),
("Care este diferența dintre insolvență și faliment?","Insolvența este starea financiară; falimentul este o formă a procedurii, cu lichidarea averii, când nu există plan de reorganizare sau acesta eșuează (art. 145)."),
("Cine poate intra în insolvență personală?","Persoanele fizice neprofesioniste, potrivit Legii nr. 151/2015; Legea nr. 85/2014 se aplică profesioniștilor."),
("Se suspendă executările silite în insolvență?","Da, de la deschiderea procedurii, toate acțiunile și măsurile de executare pentru realizarea creanțelor asupra averii debitorului se suspendă de drept (art. 75)."),
("Pot păstra locuința în procedura de insolvență?","Depinde de procedură și de regimul garanțiilor; la persoane fizice se aplică Legea nr. 151/2015, ale cărei condiții trebuie verificate în textul consolidat."),
("Cât durează procedura de insolvență?","Nu există o durată fixă; planul de reorganizare nu poate depăși 3 ani de la confirmare (art. 133 alin. 3)."),
("Ce rol are administratorul judiciar?","Este desemnat prin sentința de deschidere (art. 73) și supraveghează administrarea averii și realizarea planului."),
("Pot creditorii contesta procedura?","Pot depune opoziție la sentința de deschidere în termenul din notificare (art. 100) și pot contesta tabelele de creanțe, în condițiile legii.")]
P=dict(slug='insolventa',crumb='Insolvența',
 title='Insolvență: ce înseamnă, cine intră sub lege, etape',
 desc='Ce este insolvența, cum se deosebește de faliment, cine intră sub Legea 85/2014 sau Legea 151/2015, etapele procedurii, suspendarea executărilor și drepturile debitorilor și creditorilor.',
 nav='#calculator|Ce lege ți se aplică;#raspuns|Răspuns rapid;#etape|Etape;#drepturi|Drepturi;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Legea 85/2014 · Legea 151/2015 · etape',
  h1='Insolvența explicată simplu: <span class="accent">lege, etape și drepturi</span>',
  lead=['Datoriile s-au adunat, executorii bat la ușă și auzi „insolvență” ca soluție sau ca amenințare. Ce înseamnă, de fapt, și ce lege ți se aplică depinde de cine ești: firmă, profesionist sau persoană fizică.',
        'Aici afli, pe scurt, definiția legală, etapele procedurii, efectul asupra executărilor și drepturile fiecărei părți, cu un instrument care îți arată legea aplicabilă.'],
  meta2='Executări suspendate de drept (art. 75)',cta='Vezi legea aplicabilă',
  answer='Insolvența este starea în care fondurile disponibile nu ajung pentru plata datoriilor certe, lichide și exigibile (art. 5 pct. 29 din Legea nr. 85/2014); se prezumă după 60 de zile de la scadență fără plată. Procedura poate duce la reorganizare pe bază de plan sau la faliment. De la deschidere, executările individuale se suspendă de drept (art. 75). Persoanele fizice neprofesioniste au Legea nr. 151/2015.',
  opts=[('Prezumție','60 de zile de la scadență'),('Cerere debitor','30 de zile'),('Efect','executări suspendate')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('firme','Firme',S3),('fizice','Persoane fizice',S4),('etape','Etape',S5),('drepturi','Drepturi',S6),('riscuri','Riscuri',S7),('azi','Ce faci azi',S8)],
 faq=faq,faq_h2='Întrebări frecvente despre insolvență',
 contact=dict(h2='Ai datorii pe care nu le mai poți plăti?',lead='Trimite-ne situația financiară și lista creditorilor. Îți spunem în aceeași zi ce lege se aplică și ce procedură se potrivește. Consultația nu te obligă la nimic.',nav='/|Acasă;/insolventa-voluntara/|Insolvența voluntară;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat tribunalelor sau administratorilor judiciari. Informațiile sunt orientative.'),
 howto=dict(name='Cum afli ce procedură de insolvență ți se aplică',steps=[('Stabilești statutul','Profesionist sau persoană fizică neprofesionistă.'),('Verifici starea de insolvență','Fonduri insuficiente pentru datorii certe, lichide, exigibile.'),('Alegi legea','Legea 85/2014 sau Legea 151/2015.'),('Depui cererea','La tribunal sau la judecătorie, după caz.'),('Urmezi procedura','Suspendarea executărilor, creanțe, plan sau faliment.')]),
 knows=['Insolvență','Legea 85/2014','Legea 151/2015','Reorganizare judiciară','Faliment'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/insolventa.src.html','w',encoding='utf-8').write(build(P))
