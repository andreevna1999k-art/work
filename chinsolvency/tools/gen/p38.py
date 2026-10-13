import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'intrarea-in-insolventa-pasii':('Legea 85/2014 · art. 66','Intrarea în insolvență, pas cu pas',
   steps([('Starea de insolvență','Apare','Fonduri insuficiente pentru datorii certe, lichide, exigibile'),('Cererea','Max. 30 zile','La tribunal, cu notificarea organului fiscal (art. 66)'),('Actele','Art. 67','Situații financiare, lista bunurilor și a creditorilor'),('Deschiderea','Judecătorul-sindic','Procedură generală sau simplificată (art. 71)'),('Efecte','Suspendare','Executările individuale se suspendă de drept (art. 75)')],
   'Termenul de <b>30 de zile</b> curge de la apariția stării de insolvență (art. 66 alin. 1).'),
   'Legea nr. 85/2014. Orientativ.','Intrarea în insolvență la cererea debitorului: starea de insolvență, cerere în 30 de zile, acte, deschidere, efecte','Intrarea în insolvență, pas cu pas'),
 'reorganizare-sau-faliment':('Comparație','Reorganizare sau faliment?',
   table(['','Reorganizare judiciară','Faliment (lichidare)'],[['Scop','Redresare prin plan','Vânzarea averii și plata creditorilor'],['Durata planului','Maximum 3 ani (art. 133 alin. 3)','Nu are plan; depinde de valorificare'],['Debitorul','Păstrează, de regulă, conducerea, sub supraveghere','Pierde dreptul de administrare'],['Creditorii','Votează planul (art. 139)','Se distribuie sumele după ordinea legii']]),
   'Orientativ; condițiile exacte sunt în Legea nr. 85/2014.','Reorganizare judiciară sau faliment: scop, durata planului, rolul debitorului și al creditorilor','Reorganizare sau faliment'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.deadline('Până când depui <span class="accent">cererea de insolvență</span>','Alege situația și data de la care curge termenul. Vezi ultima zi pentru cererea debitorului către tribunal, după art. 66 din Legea nr. 85/2014 și regula zilelor libere (art. 181 CPC).','De când curge termenul',[
 ('De la apariția stării de insolvență','30 de zile libere de la apariția stării de insolvență (art. 66 alin. 1).',31),
 ('De la eșuarea negocierilor extrajudiciare, când debitorul negociază cu bună-credință','5 zile libere de la eșuarea negocierilor (art. 66 alin. 2).',6)],
 'Data de la care curge termenul','2026-10-01','Exemplu: insolvență apărută la 1 octombrie 2026','Ultima zi pentru cererea de deschidere','Calcul orientativ. Starea de insolvență se prezumă după 60 de zile de la scadență fără plată (art. 5 pct. 29), prezumție relativă. Data exactă a apariției insolvenței se stabilește din situația financiară; verifică cu un specialist înainte de depunere. Termenul se calculează pe zile libere (+1 zi) și se mută la prima zi lucrătoare.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Intrarea în insolvență voluntară: răspuns rapid</h2>
        <p>Insolvența „voluntară” este deschiderea procedurii la cererea debitorului. Debitorul aflat în stare de insolvență trebuie să ceară tribunalului deschiderea procedurii în cel mult 30 de zile de la apariția stării de insolvență, cu notificarea organului fiscal (art. 66 alin. 1 din Legea nr. 85/2014). Judecătorul-sindic deschide procedura generală sau simplificată (art. 71), iar de la deschidere executările individuale se suspendă de drept (art. 75).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Starea de insolvență apare la 1 octombrie 2026. Termenul de 30 de zile se calculează pe zile libere: 1 octombrie + 31 zile = 1 noiembrie 2026, care este duminică, deci termenul se mută luni, 2 noiembrie 2026. Dacă firma negociază cu bună-credință un acord extrajudiciar și negocierile eșuează, cererea se depune în 5 zile de la eșuare (art. 66 alin. 2).</p>
          <span class="formula">1.10.2026 + 31 zile = 1.11 (duminică) → 2.11.2026</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este insolvența și când apare</h2>
        <p>Legea o definește ca starea patrimoniului debitorului caracterizată prin insuficiența fondurilor bănești disponibile pentru plata datoriilor certe, lichide și exigibile (art. 5 pct. 29). Insolvența se prezumă atunci când debitorul nu a plătit o datorie după 60 de zile de la scadență; prezumția este relativă, deci poate fi răsturnată cu probe. Insolvența este iminentă când se dovedește că debitorul nu va putea plăti la scadență datoriile exigibile cu fondurile disponibile atunci. În acest caz, debitorul poate cere deschiderea procedurii (art. 66 alin. 4), dar nu este obligat.</p>
        <h3>Cine intră sub Legea nr. 85/2014</h3>
        <p>Legea se aplică debitorilor profesioniști (societăți, persoane fizice autorizate etc.). Persoanele fizice neprofesioniste au un regim separat, Legea nr. 151/2015. Pentru restructurarea înainte de insolvență, vezi <a href="/reorganizare-judiciara/">reorganizarea judiciară</a>.</p>'''
S3='''        <span class="eyebrow">Cererea debitorului</span>
        <h2>Deschiderea procedurii la cererea debitorului</h2>
        <p>Cererea se adresează tribunalului. Dacă debitorul negociază cu bună-credință, la data expirării termenului, un acord extrajudiciar, cererea se depune în 5 zile de la eșuarea negocierilor (art. 66 alin. 2). Cererile persoanelor juridice sunt semnate de persoanele care le reprezintă potrivit actelor constitutive, fără hotărâre a asociaților (art. 66 alin. 5).</p>
        <h3>Actele cererii (art. 67)</h3>
        <ul class="chk">
          <li>Ultima situație financiară anuală, certificată de administrator și cenzor sau auditor, și balanța de verificare din luna precedentă.</li>
          <li>Lista completă a bunurilor, cu toate conturile și băncile, și datele din registrele de publicitate pentru bunurile grevate.</li>
          <li>Lista creditorilor, cu sumele, cauzele și drepturile de preferință.</li>
          <li>Lista plăților și transferurilor din ultimele 6 luni, contul de profit și pierdere pe anul anterior.</li>
          <li>Declarația privind intrarea în procedura simplificată sau în reorganizare pe bază de plan, și descrierea sumară a modalităților de reorganizare.</li>
          <li>Declarații pe propria răspundere (autentificate sau certificate de avocat) despre o eventuală reorganizare în ultimii 5 ani și despre condamnările definitive.</li>
        </ul>
        <p>Debitorul depune actele și informațiile din art. 67 alin. 1 în dosar în termen de 10 zile de la deschiderea procedurii (art. 74).</p>'''
S4='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura pas cu pas</h2>
        <ol class="num">
          <li><b>Cererea</b> la tribunal, în maximum 30 de zile de la apariția insolvenței, cu dovada notificării organului fiscal (art. 66 alin. 1).</li>
          <li><b>Încheierea de deschidere:</b> procedură generală sau simplificată (art. 71). Simplificată se aplică, de pildă, persoanelor fizice profesioniste înregistrate, întreprinderilor familiale sau debitorilor fără bunuri ori fără sediu (art. 38 alin. 2).</li>
          <li><b>Administratorul judiciar provizoriu</b> (procedura generală) sau lichidatorul judiciar provizoriu (cea simplificată) este numit prin sentința de deschidere (art. 73).</li>
          <li><b>Suspendarea executărilor:</b> toate acțiunile și măsurile de executare pentru realizarea creanțelor asupra averii debitorului se suspendă de drept (art. 75).</li>
          <li><b>Creditorii</b> își depun cererile de admitere a creanțelor în procedură.</li>
          <li><b>Reorganizare sau faliment:</b> debitorul propune un plan sau se trece la lichidare.</li>
        </ol>
'''+F('intrarea-in-insolventa-pasii')
S5='''        <span class="eyebrow">Reorganizare și faliment</span>
        <h2>Reorganizarea judiciară și falimentul</h2>
'''+F('reorganizare-sau-faliment')+'''
        <p>Planul de reorganizare cuprinde obligatoriu programul de plată a creanțelor (art. 133 alin. 2), iar executarea lui nu poate depăși 3 ani de la confirmare (art. 133 alin. 3). Nu pot fi supuși reorganizării debitorii persoane juridice care în ultimii 5 ani au mai fost supuși unei proceduri de reorganizare (art. 69). Dacă nu există plan sau planul eșuează, se trece la lichidarea averii și distribuirea sumelor creditorilor. Detalii în ghidul despre <a href="/reorganizare-judiciara/">reorganizarea judiciară</a>.</p>'''
S6='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile și obligațiile debitorului și ale creditorilor</h2>
        <ul class="chk">
          <li><b>Debitorul:</b> beneficiază de suspendarea executărilor (art. 75), dar trebuie să depună actele (art. 74) și să respecte planul; poate fi supus unor restricții privind administrarea averii.</li>
          <li><b>Furnizorii de utilități:</b> nu pot întrerupe serviciile către debitorul consumator captiv în perioada de observație și reorganizare, iar debitorul plătește în 90 de zile (art. 77).</li>
          <li><b>Creditorii:</b> își valorifică drepturile numai în procedură, prin cerere de admitere a creanței (art. 75); creditorul cu garanție poate cere ridicarea suspendării în condițiile art. 78.</li>
        </ul>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și cum previi insolvența</h2>
        <ul class="chk">
          <li><b>Depui cererea târziu:</b> obligația este de 30 de zile de la apariția insolvenței (art. 66).</li>
          <li><b>Lipsesc actele contabile:</b> situația financiară și lista creditorilor sunt obligatorii (art. 67).</li>
          <li><b>Administrezi riscant averea</b> după apariția insolvenței.</li>
        </ul>
        <p>Înainte de insolvență, există variante de restructurare: negocierea cu creditorii și procedurile preventive (mandat ad-hoc, concordat preventiv, art. 66 alin. 3). Pentru creditele bancare, vezi <a href="/restructurare-credit-vs-refinantare/">restructurare credit</a>. Textele din Legea nr. 85/2014 sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>'''
S8='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci dacă firma intră în insolvență</h2>
        <ol class="num">
          <li>Stabilește data la care a apărut starea de insolvență și calculează ultima zi pentru cerere (calculator).</li>
          <li>Strânge situația financiară, lista bunurilor, a creditorilor și a plăților din ultimele 6 luni.</li>
          <li>Trimite-ne datele în chat; îți spunem în aceeași zi ce procedură se potrivește.</li>
        </ol>
        <!--@author practice="insolvență" -->'''
faq=[("Ce înseamnă insolvența voluntară?","Deschiderea procedurii insolvenței la cererea debitorului, nu a creditorului. Debitorul în stare de insolvență trebuie să o ceară în maximum 30 de zile (art. 66 din Legea nr. 85/2014)."),
("Cine poate cere deschiderea procedurii?","Debitorul (art. 66) sau un creditor îndreptățit (art. 70). Cererea se adresează tribunalului."),
("Care este pragul pentru insolvență?","Legea nu fixează o sumă; insolvența se prezumă după 60 de zile de la scadență fără plată (art. 5 pct. 29), prezumție relativă."),
("Ce diferență există între reorganizare și faliment?","Reorganizarea urmărește redresarea pe baza unui plan, de maximum 3 ani; falimentul înseamnă lichidarea averii și plata creditorilor."),
("Ce face administratorul judiciar?","Este numit prin sentința de deschidere (art. 73) și supraveghează administrarea averii și realizarea planului, sub controlul judecătorului-sindic."),
("Pot creditorii recupera datoriile?","Își valorifică creanțele numai în procedură, prin cerere de admitere (art. 75); sumele se distribuie după ordinea legii."),
("Cât durează procedura?","Nu există o durată fixă; planul de reorganizare nu poate depăși 3 ani de la confirmare (art. 133 alin. 3)."),
("Cum poate fi prevenit falimentul?","Prin negocieri cu creditorii, mandat ad-hoc sau concordat preventiv, urmărirea fluxului de numerar și depunerea la timp a cererii.")]
P=dict(slug='insolventa-voluntara',crumb='Insolvența voluntară',
 title='Insolvență voluntară: cerere în 30 de zile, procedură',
 desc='Cum intri în insolvență la cererea debitorului: termenul de 30 de zile, actele cererii, deschiderea procedurii, suspendarea executărilor și diferența dintre reorganizare și faliment.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#cerere|Cererea;#procedura|Procedura;#reorganizare|Reorganizare și faliment;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Legea 85/2014 · art. 66 · cererea debitorului',
  h1='Intrarea în insolvență voluntară: <span class="accent">procedură, termen de 30 de zile și faliment</span>',
  lead=['Firma nu mai poate plăti datoriile scadente și te întrebi dacă trebuie să ceri tu insolvența sau să aștepți un creditor. Legea îți dă un termen scurt, iar întârzierea are urmări.',
        'Aici afli când apare obligația, ce acte pui în dosar, ce urmează după deschidere și cum diferă reorganizarea de faliment, cu un calculator pentru ultima zi de depunere.'],
  meta2='Cerere: maximum 30 de zile',cta='Calculează termenul',
  answer='Insolvența voluntară este deschiderea procedurii la cererea debitorului. Debitorul aflat în stare de insolvență trebuie să adreseze tribunalului cererea în maximum 30 de zile de la apariția insolvenței, cu notificarea organului fiscal (art. 66 din Legea nr. 85/2014). După deschidere, executările individuale se suspendă de drept (art. 75).',
  opts=[('Cerere','30 de zile (art. 66)'),('Dacă negociezi','5 zile de la eșuare'),('Efect','executări suspendate')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('cerere','Cererea',S3),('procedura','Procedura',S4),('reorganizare','Reorganizare și faliment',S5),('drepturi','Drepturi',S6),('greseli','Greșeli',S7),('azi','Ce faci azi',S8)],
 faq=faq,faq_h2='Întrebări frecvente despre insolvența voluntară',
 contact=dict(h2='Firma are datorii scadente?',lead='Trimite-ne situația financiară și lista creditorilor. Îți spunem în aceeași zi dacă ești în insolvență, ce termen curge și ce procedură se potrivește. Consultația nu te obligă la nimic.',nav='/|Acasă;/reorganizare-judiciara/|Reorganizare judiciară;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat tribunalelor sau administratorilor judiciari. Calculele sunt orientative.'),
 howto=dict(name='Cum intri în insolvență la cererea debitorului',steps=[('Stabilești starea de insolvență','Fonduri insuficiente pentru datorii certe, lichide și exigibile.'),('Notifici organul fiscal','Dovada se atașează cererii.'),('Depui cererea la tribunal','În maximum 30 de zile (art. 66).'),('Depui actele din art. 67','Situații financiare, bunuri, creditori, plăți.'),('Aștepți încheierea','Procedură generală sau simplificată; executările se suspendă (art. 75).')]),
 knows=['Insolvență','Legea 85/2014','Reorganizare judiciară','Faliment'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/insolventa-voluntara.src.html','w',encoding='utf-8').write(build(P))
