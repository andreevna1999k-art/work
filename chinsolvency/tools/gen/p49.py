import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'somatia-regula-si-exceptii':('Art. 667–669 CPC','Somația: regula și excepțiile',
   cards([('Regula','Somație','Încheiere + titlu + somație comunicate debitorului (art. 667)',True),('Poprirea','Fără somație','Se înființează prin adresă către terț (art. 783)',False),('Decădere din termen','Fără comunicare','Când creditorul cere decăderea din termenul de plată (art. 669 + 675)',False),('Hotărâri executorii','Fără comunicare','Ordonanțe și încheieri date de instanță, executorii prin lege (art. 669 pct. 2)',False),('Lipsa comunicării','Nulitate','Când legea o cere și lipsește, executarea e nulă (art. 667 alin. 2)',True),('Termen de contestație','15 zile','De la primul act aflat, dacă nu ai primit nimic (art. 715)',False)],3),
   'Cod procedură civilă, art. 667–669, 715, 783. Orientativ.','Somația în executarea silită: regula, excepțiile fără somație, nulitatea și termenul de contestație','Somația: regula și excepțiile'),
 'executare-legala-sau-fara-procedura':('Comparație','Executare legală sau cu vicii',
   table(['','Executare legală','Executare fără respectarea procedurii'],[['Comunicare','Încheiere, titlu și somație, când legea le cere','Lipsesc actele pe care legea le impune'],['Drepturile debitorului','Contestație, în general în 15 zile','Contestație pentru nulitate (art. 667 alin. 2, 704)'],['Efect','Executarea continuă','Actul nelegal și cele subsecvente se anulează (art. 704)'],['Ce faci','Verifici titlul și calculul','Ceri dosarul și contești']]),
   'Orientativ; nulitatea depinde de vătămare și de dosar.','Executare legală și executare cu vicii de procedură: comunicare, drepturi, efect și ce faci','Executare legală sau cu vicii'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.select('Se cere somație <span class="accent">în cazul tău?</span>','Alege felul executării. Îți arătăm dacă legea cere somație, ce poți contesta și primul pas.','Ce fel de executare ai',[
 ('Poprire pe cont sau pe salariu','Nu se cere somație: poprirea se înființează prin adresă către terț (art. 783 alin. 1).','Termen: 15 zile de la înștiințarea despre poprire (art. 715 alin. 1 pct. 2).','Cere copia adresei de poprire și a încheierii de încuviințare.'),
 ('Sechestru pe bunuri sau urmărire imobiliară','Regula: încheierea, titlul și somația se comunică (art. 667–668).','Dacă lipsesc, poți invoca nulitatea (art. 667 alin. 2); termen 15 zile (art. 715).','Verifică dosarul: ce acte ți s-au comunicat și când.'),
 ('Ordonanță sau încheiere a instanței, executorie prin lege','Nu e necesară comunicarea titlului și a somației (art. 669 pct. 2).','Termen de contestație: 15 zile de la luarea la cunoștință de act (art. 715).','Verifică dacă hotărârea e într-adevăr executorie și suma cerută.'),
 ('Creditorul cere să pierzi termenul de plată din titlu','Nu e necesară comunicarea în cazurile art. 675 (art. 669 pct. 1).','Instanța hotărăște de urgență, cu citarea ta (art. 675 alin. 2).','Pregătește-te să dovedești că ești în termen și nu te sustragi.'),
 ('Nu am primit niciun act, dar am aflat de executare','Verifică dacă legea scutea de somație sau dacă lipsește un act obligatoriu.','Termenul curge de la primul act de executare aflat (art. 715 alin. 1 pct. 3).','Cere dosarul executorului și notează data la care ai aflat.')],
 0,'Exemplu: poprire pe cont','Se cere somație?','Termen','Primul pas','Orientativ, după CPC. Dacă executarea este fiscală (ANAF), se aplică Codul de procedură fiscală, cu reguli proprii de comunicare.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Executare silită fără somație: răspuns rapid</h2>
        <p>Da, poți fi executat fără somație în anumite cazuri. Regula este că debitorul primește încheierea de încuviințare, o copie a titlului executoriu și o somație, iar lipsa comunicării, când legea o cere, atrage nulitatea executării (art. 667 CPC). Excepții: poprirea se înființează fără somație (art. 783 alin. 1); nu se comunică titlul și somația în cazurile de decădere din termen (art. 675) și pentru ordonanțele și încheierile instanței declarate executorii de lege (art. 669). Termenul de contestație este, în general, de 15 zile.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Afli de executare pe 12 octombrie 2026, din refuzul unui card, fără să fi primit vreo somație. Pentru poprire legea nu cere somație. Termenul de contestație curge de la înștiințarea despre poprire; ultima zi este 12 octombrie + 16 zile = 28 octombrie 2026. Cere imediat copia adresei de poprire și a încheierii.</p>
          <span class="formula">12.10.2026 + 16 zile = 28.10.2026</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este somația și când este obligatorie</h2>
        <p>Somația este chemarea de a-ți plăti datoria de îndată sau în termenul acordat de lege, cu avertismentul că altfel executarea continuă (art. 668 CPC). Se comunică împreună cu încheierea de încuviințare și cu o copie certificată a titlului (art. 667 alin. 1). Nu este același lucru cu o notificare trimisă de creditor înainte: aceea este o scrisoare, somația este un act al executorului.</p>
'''+F('somatia-regula-si-exceptii')
S3='''        <span class="eyebrow">Excepții</span>
        <h2>Situații în care poți fi executat fără somație</h2>
        <ul class="chk">
          <li><b>Poprirea</b> se înființează fără somație, prin adresă către bancă sau angajator (art. 783 alin. 1); tu primești copia adresei.</li>
          <li><b>Decăderea din termenul de plată</b> (art. 675): creditorul poate cere decăderea dacă te sustragi, risipești averea, ești insolvabil notoriu ori alți creditori execută; nu se comunică titlul și somația (art. 669 pct. 1). Instanța hotărăște de urgență, cu citarea ta.</li>
          <li><b>Ordonanțe și încheieri ale instanței</b> declarate de lege executorii (art. 669 pct. 2).</li>
        </ul>
        <p>Într-o executare obișnuită pe bunuri, încuviințarea nu înseamnă, singură, că se poate sechestra pe loc: regula comunicării titlului și somației rămâne (art. 667), dacă legea nu prevede altfel. Dacă titlul fixează un termen de plată, executarea nu poate începe înainte de împlinirea lui (art. 674).</p>'''
S4='''        <span class="eyebrow">Executare nelegală</span>
        <h2>Când executarea fără somație este nelegală</h2>
        <p>Dacă legea cere comunicarea titlului și a somației, iar acestea lipsesc, executarea este supusă nulității (art. 667 alin. 2). Nerespectarea dispozițiilor privind executarea sau un act de executare atrage nulitatea actului nelegal și a celor următoare (art. 704). Dovada comunicării se face din dosarul executorului, nu din memorie.</p>
'''+F('executare-legala-sau-fara-procedura')+'''
        <h3>Cum verifici dacă executarea este legală</h3>
        <ul class="chk">
          <li>Există titlu executoriu (art. 632) și creanță certă, lichidă, exigibilă (art. 663)?</li>
          <li>Ți s-au comunicat încheierea, titlul și somația, când legea le cere?</li>
          <li>Executorul este competent (pentru poprire pe cont: art. 782)?</li>
          <li>Suma cerută, cu dobânzile și cheltuielile, este corectă?</li>
        </ul>'''
S5='''        <span class="eyebrow">Contestație</span>
        <h2>Contestația la executare când nu ai primit somația</h2>
        <p>Poți ataca executarea însăși și orice act de executare (art. 712 CPC). Termenul general este de 15 zile: de la primirea încheierii sau a somației, de la înștiințarea despre poprire ori, dacă nu ai primit nici încheierea, nici somația sau executarea se face fără somație, de la primul act de executare de care ai luat cunoștință (art. 715 alin. 1 pct. 3). Contestația nu oprește singură executarea; pentru asta ceri suspendarea, cu cauțiune (art. 719). Vezi <a href="/contestatie-la-executare/">contestația la executare</a> și <a href="/amanare-executare-silita/">suspendarea executării</a>.</p>
        <h3>Documente necesare</h3>
        <p>Contestația, actele de executare pe care le ai, copia dosarului de la executor, dovada datei la care ai aflat, extrasele de cont și dovada taxei de timbru (cel mult 1.000 lei, art. 10 OUG 80/2013).</p>'''
S6='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile debitorului și rolul executorului</h2>
        <ul class="chk">
          <li>Dreptul de a primi actele pe care legea le impune și de a cere copii din dosar.</li>
          <li>Dreptul de apărare, prin contestație și prin cerere de suspendare (art. 712, 719).</li>
          <li>Protecția veniturilor: o treime din venitul net la datorii obișnuite, jumătate la mai multe urmăriri (art. 729); sumele nepopribile (art. 729 alin. 7).</li>
        </ul>
        <p>Executorul judecătoresc încheie procese-verbale pentru actele de executare (art. 679) și răspunde pentru abaterile de la procedură. Detalii despre procedură: <a href="/procedura-executare-silita-etape/">etapele executării silite</a>.</p>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și ce faci imediat</h2>
        <ul class="chk">
          <li>Ignori actele primite, pentru că „nu e somație”.</li>
          <li>Depășești termenul de 15 zile.</li>
          <li>Contești fără să ceri dosarul și fără dovada datei la care ai aflat.</li>
        </ul>
        <ol class="num">
          <li>Notează data la care ai aflat de executare.</li>
          <li>Cere executorului copia dosarului și a adresei de poprire.</li>
          <li>Calculează ultima zi de contestație și decide dacă ceri și suspendarea.</li>
        </ol>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>
        <!--@author practice="executare silită" -->'''
faq=[("Poți fi executat silit fără somație?","Da, în cazurile prevăzute de lege: poprirea se înființează fără somație (art. 783), iar în unele situații nu se comunică titlul și somația (art. 669 CPC)."),
("Când este obligatorie somația?","Regula este că încheierea, titlul și somația se comunică debitorului (art. 667–668); lipsa lor, când legea le cere, atrage nulitatea executării."),
("Ce pot face dacă nu am primit actele?","Ceri copia dosarului de executare, notezi data la care ai aflat și contești executarea în 15 zile de la primul act de care ai luat cunoștință (art. 715)."),
("Cum verific legalitatea executării silite?","Verifici titlul executoriu, comunicarea actelor, competența executorului și calculul sumei, pe baza dosarului."),
("În cât timp pot face contestație?","În general în 15 zile, de la actul care curge termenul (art. 715)."),
("Executarea fără notificare poate fi anulată?","Da, dacă lipsea o comunicare obligatorie și instanța admite contestația: se anulează actul nelegal și cele subsecvente (art. 704, 720)."),
("Ce acte trebuie să primesc de la executor?","Încheierea de încuviințare, o copie certificată a titlului executoriu și, de regulă, o somație; la poprire, copia adresei de poprire."),
("Pot suspenda executarea silită?","Da, prin cerere către instanță, cu cauțiune (art. 719). Suspendarea simplă nu ridică singură poprirea existentă.")]
P=dict(slug='executare-silita-fara-somatie',crumb='Executare silită fără somație',
 title='Executare silită fără somație: când e legală, ce poți face',
 desc='Poți fi executat silit fără somație? Cazurile prevăzute de lege (poprire, art. 669 CPC), nulitatea executării, termenul de contestație de 15 zile și pașii de urmat.',
 nav='#calculator|Se cere somație?;#raspuns|Răspuns rapid;#exceptii|Excepții;#nelegala|Executare nelegală;#contestatie|Contestație;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Art. 667–669 CPC · poprire fără somație · nulitate',
  h1='Executat silit fără somație: <span class="accent">ce poate face debitorul</span>',
  lead=['Ți s-a blocat contul și nu ai primit nicio somație. Te întrebi dacă executorul poate face asta și dacă merită să contești. Răspunsul depinde de felul executării: la poprire legea nu cere somație, dar în alte cazuri lipsa comunicării duce la nulitate.',
        'Aici vezi regula, excepțiile, cum verifici legalitatea și cum contești, cu un instrument care îți spune dacă în cazul tău se cere somație.'],
  meta2='Contestație: 15 zile',cta='Vezi cazul tău',
  answer='Da, poți fi executat fără somație în cazurile prevăzute de lege: poprirea se înființează fără somație (art. 783), iar titlul și somația nu se comunică în cazurile din art. 669 CPC. În celelalte situații, lipsa comunicării atrage nulitatea executării (art. 667 alin. 2). Termenul de contestație este, în general, de 15 zile (art. 715).',
  opts=[('Poprire','fără somație'),('Regula','somație obligatorie'),('Contestație','15 zile')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este somația',S2),('exceptii','Excepții',S3),('nelegala','Executare nelegală',S4),('contestatie','Contestație',S5),('drepturi','Drepturi',S6),('greseli','Greșeli și pași',S7)],
 faq=faq,faq_h2='Întrebări frecvente despre executarea fără somație',
 contact=dict(h2='Nu ai primit nicio somație?',lead='Trimite-ne tot ce ai primit și data la care ai aflat de executare. Îți spunem în aceeași zi dacă lipsește un act obligatoriu și ce termen curge. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Ce faci dacă ești executat fără somație',steps=[('Notezi data','La care ai aflat de executare.'),('Ceri dosarul','Încheierea, titlul, adresa de poprire.'),('Verifici legalitatea','Titlu, comunicări, competență, calcul.'),('Contești','În general în 15 zile.'),('Ceri suspendarea','Cu cauțiune, dacă ai motive temeinice.')]),
 knows=['Executare silită','Somație','Contestație la executare','Poprire'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/executare-silita-fara-somatie.src.html','w',encoding='utf-8').write(build(P))
