import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'insolventa-faliment-reorganizare':('Legea 85/2014','Insolvență, reorganizare, faliment',
   table(['','Insolvență','Reorganizare judiciară','Faliment'],[['Ce este','Starea financiară (art. 5 pct. 29)','Procedură cu plan, max. 3 ani','Lichidarea averii'],['Cine conduce afacerea','Debitorul, până la deschidere','Debitorul, sub supraveghere','Lichidatorul judiciar'],['Efect pentru persoana juridică','Executări suspendate după deschidere','Activitatea continuă','Dizolvare (art. 145 alin. 2)'],['Creditorii','Se înscriu la masa credală','Votează planul (art. 139)','Primesc sume la distribuire']]),
   'Legea nr. 85/2014. Orientativ; verifică forma consolidată.','Insolvență, reorganizare judiciară și faliment: ce sunt, cine conduce afacerea, efectele și rolul creditorilor','Insolvență, reorganizare, faliment'),
 'procedura-generala-sau-simplificata':('Legea 85/2014 · art. 38','Procedura generală sau simplificată',
   table(['','Procedura generală','Procedura simplificată'],[['Cui se aplică','Debitorilor din art. 3, în afara celor simplificați (art. 38 alin. 1)','PFA înregistrați, întreprinderi familiale, debitori fără bunuri, fără acte, fără administrator sau fără sediu (art. 38 alin. 2)'],['Organ desemnat','Administrator judiciar provizoriu (art. 73)','Lichidator judiciar provizoriu (art. 73)'],['Calea tipică','Reorganizare sau faliment','Faliment, direct cu lichidare']]),
   'Legea nr. 85/2014, art. 38, 71, 73. Orientativ.','Procedura generală și procedura simplificată de insolvență: cui se aplică, organul desemnat și calea tipică','Procedura generală sau simplificată'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.select('Reorganizare sau faliment: <span class="accent">ce urmează?</span>','Alege situația procedurii. Îți arătăm calea probabilă, temeiul din Legea nr. 85/2014 și efectul pentru debitor.','Situația procedurii',[
 ('Debitorul nu a declarat intenția de reorganizare','Faliment','Art. 145 alin. 1 lit. A, pct. b','Se ridică dreptul de administrare și se numește lichidator (art. 145 alin. 2).'),
 ('Debitorul a declarat intenția de a intra în procedura simplificată','Faliment, prin procedura simplificată','Art. 145 alin. 1 lit. A, pct. a','Lichidatorul judiciar conduce lichidarea.'),
 ('Nimeni nu a propus un plan sau niciun plan nu a fost acceptat și confirmat','Faliment','Art. 145 alin. 1 lit. A, pct. c','Dizolvarea persoanei juridice și lichidarea averii.'),
 ('Planul confirmat este respectat','Reorganizare continuă','Art. 141 alin. 1','Debitorul conduce activitatea sub supravegherea administratorului judiciar.'),
 ('Debitorul nu respectă planul sau acumulează pierderi','Creditorii pot cere falimentul','Art. 143 alin. 1 și art. 145 alin. 1 lit. C','Judecătorul-sindic judecă cererea de urgență și cu precădere.')],
 0,'Exemplu: nu s-a depus plan','Calea probabilă','Temei','Efect','Orientativ, după art. 141, 143 și 145 din Legea nr. 85/2014. Soluția concretă o stabilește judecătorul-sindic, în funcție de dosar.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Insolvență sau faliment: răspuns rapid</h2>
        <p>Insolvența este starea financiară în care fondurile disponibile nu ajung pentru datoriile certe, lichide și exigibile (art. 5 pct. 29 din Legea nr. 85/2014). Falimentul este una dintre căile procedurii: lichidarea averii și, pentru persoanele juridice, dizolvarea (art. 145). Cealaltă cale este reorganizarea judiciară, pe bază de plan, de cel mult 3 ani (art. 133 alin. 3). Procedura poate fi generală sau simplificată (art. 38).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Debitorul nu a declarat intenția de reorganizare în cererea lui. Chiar dacă a intrat în insolvență, judecătorul-sindic decide intrarea în faliment (art. 145 alin. 1 lit. A, pct. b). Dacă, în schimb, un plan este confirmat în ziua 100 a procedurii și respectat, activitatea continuă, iar falimentul nu mai este pe agendă (art. 141).</p>
          <span class="formula">fără intenție de reorganizare → faliment (art. 145)</span>
          <button type="button" class="btn btn-line" data-ex="1">Vezi în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Diferența</span>
        <h2>Diferența dintre insolvență, reorganizare și faliment</h2>
'''+F('insolventa-faliment-reorganizare')+'''
        <p>Reorganizarea judiciară este procedura aplicabilă debitorului persoană juridică aflat în insolvență, care presupune un plan de reorganizare, cu programul de plată a creanțelor (art. 5 pct. 54, art. 133 alin. 2). În faliment, judecătorul-sindic pronunță dizolvarea persoanei juridice, ridică dreptul de administrare al debitorului și desemnează un lichidator judiciar (art. 145 alin. 2). Vezi <a href="/reorganizare-judiciara/">reorganizarea judiciară</a>.</p>'''
S3='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura generală și procedura simplificată</h2>
        <p>Procedura generală se aplică debitorilor din art. 3, cu excepția celor cărora li se aplică procedura simplificată (art. 38 alin. 1). Procedura simplificată se aplică, printre altele, profesioniștilor persoane fizice înregistrați la registrul comerțului (fără profesii liberale), întreprinderilor familiale, debitorilor care nu au bunuri, nu au acte constitutive sau contabile, nu au administrator sau nu mai au sediul și celor care au declarat prin cerere intenția de a intra în procedura simplificată (art. 38 alin. 2).</p>
'''+F('procedura-generala-sau-simplificata')+'''
        <p>Judecătorul-sindic deschide procedura generală sau simplificată prin încheierea de deschidere (art. 71) și desemnează administratorul judiciar provizoriu, respectiv lichidatorul judiciar provizoriu (art. 73). Detalii despre cerere: <a href="/deschiderea-procedurii-insolventei/">deschiderea procedurii insolvenței</a>.</p>'''
S4='''        <span class="eyebrow">Cine intră</span>
        <h2>Cine poate beneficia de procedură</h2>
        <p>Legea nr. 85/2014 se aplică profesioniștilor, cu excepția celor care exercită profesii liberale, și regiilor autonome (art. 3). Persoanele fizice neprofesioniste au o lege separată, Legea nr. 151/2015, cu condiții proprii pe care trebuie să le verifici în textul consolidat. Pentru panoramă, vezi <a href="/insolventa/">insolvența explicată simplu</a>.</p>'''
S5='''        <span class="eyebrow">Faliment</span>
        <h2>Când se ajunge la faliment și ce urmează</h2>
        <ul class="chk">
          <li>Debitorul nu a declarat intenția de reorganizare sau a declarat intenția de procedură simplificată (art. 145 alin. 1 lit. A).</li>
          <li>Nu s-a propus un plan sau niciunul nu a fost acceptat și confirmat.</li>
          <li>Debitorul nu respectă planul sau activitatea produce pierderi (art. 143, 145 alin. 1 lit. C).</li>
        </ul>
        <p>Urmează lichidarea bunurilor de către lichidatorul judiciar, sub controlul judecătorului-sindic (art. 154), vândute în bloc sau individual, apoi distribuirea sumelor. Pentru bunurile grevate de garanții, sumele se distribuie în ordinea din art. 159 alin. 1: întâi taxele și cheltuielile vânzării, apoi creditorii titulari ai cauzelor de preferință. Procedura se închide când nu mai există bunuri ori acestea nu acoperă cheltuielile și niciun creditor nu avansează sumele (art. 174).</p>'''
S6='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile și obligațiile debitorului și ale creditorilor</h2>
        <ul class="chk">
          <li><b>Debitorul:</b> executările se suspendă de drept (art. 75); depune actele din art. 67 în 10 zile de la deschidere (art. 74).</li>
          <li><b>Creditorii:</b> se înscriu prin cerere de admitere (art. 104), votează planul (art. 139), pot cere falimentul dacă planul nu este respectat (art. 143).</li>
          <li><b>Creditorul curent</b> cu creanță certă, lichidă, exigibilă, mai veche de 60 de zile și peste valoarea-prag poate cere trecerea la faliment în timpul planului (art. 143 alin. 3).</li>
        </ul>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și cum alegi un specialist</h2>
        <ul class="chk">
          <li>Documentație incompletă la cerere (art. 67).</li>
          <li>Întârzierea cererii: termen de 30 de zile (art. 66).</li>
          <li>Creanțe neînscrise la timp în procedură.</li>
          <li>Plan lipsit de viabilitate: judecătorul verifică legalitatea și viabilitatea (art. 139 alin. 1 lit. F).</li>
        </ul>
        <p>Alege un practician sau un avocat cu experiență în insolvență, cu contract scris și fără promisiuni de rezultat garantat. Textele din Legea nr. 85/2014 sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>
        <!--@author practice="insolvență" -->'''
faq=[("Care este diferența dintre insolvență și faliment?","Insolvența este starea financiară; falimentul este calea procedurii care duce la lichidarea averii și, pentru persoane juridice, la dizolvare (art. 145)."),
("Ce este procedura simplificată de insolvență?","Procedura aplicată categoriilor din art. 38 alin. 2 (PFA înregistrați, întreprinderi familiale, debitori fără bunuri sau fără sediu etc.), cu lichidator judiciar provizoriu."),
("Cine poate intra în procedura simplificată?","Debitorii din art. 38 alin. 2 din Legea nr. 85/2014, inclusiv cei care au declarat în cerere intenția de a intra în procedura simplificată."),
("Ce condiții trebuie îndeplinite pentru a intra în insolvență?","Stare de insolvență (prezumată după 60 de zile de la scadență) și, pentru creditor, valoarea-prag de 40.000 lei (art. 5 pct. 29 și 72)."),
("Cât durează procedura?","Nu există o durată fixă; planul de reorganizare nu poate depăși 3 ani de la confirmare (art. 133 alin. 3)."),
("Se suspendă executarea silită?","Da, de la deschiderea procedurii, de drept (art. 75)."),
("Ce rol are administratorul judiciar?","Supraveghează administrarea și planul; în procedura simplificată, atribuțiile revin lichidatorului judiciar (art. 73)."),
("Ce acte sunt necesare?","La cererea debitorului, actele din art. 67: situații financiare, lista bunurilor și a creditorilor, plăți din ultimele 6 luni, declarații.")]
P=dict(slug='insolventa-sau-faliment',crumb='Insolvență sau faliment',
 title='Insolvență sau faliment: diferența și procedura simplificată',
 desc='Care este diferența dintre insolvență, reorganizare judiciară și faliment, când se ajunge la faliment (art. 145) și cum diferă procedura generală de cea simplificată (art. 38) în Legea 85/2014.',
 nav='#calculator|Ce urmează;#raspuns|Răspuns rapid;#diferenta|Diferența;#procedura|Generală sau simplificată;#faliment|Faliment;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Legea 85/2014 · art. 38, 133, 145',
  h1='Insolvență sau faliment: <span class="accent">diferența și procedura simplificată</span>',
  lead=['Auzi „firma e în insolvență” și „firma a intrat în faliment” ca și cum ar fi același lucru. Nu sunt: unul este o stare financiară, celălalt o cale a procedurii, iar între ele există reorganizarea.',
        'Aici vezi diferențele, cazurile în care se ajunge la faliment, cum diferă procedura generală de cea simplificată și ce poți face în fiecare situație.'],
  meta2='Reorganizare: maximum 3 ani',cta='Vezi ce urmează',
  answer='Insolvența este starea financiară în care fondurile nu ajung pentru datoriile certe, lichide și exigibile (art. 5 pct. 29 din Legea nr. 85/2014). Falimentul este calea procedurii care înseamnă lichidarea averii și, pentru persoanele juridice, dizolvarea (art. 145). Cealaltă cale este reorganizarea judiciară, pe bază de plan de cel mult 3 ani (art. 133). Procedura poate fi generală sau simplificată (art. 38).',
  opts=[('Insolvență','starea financiară'),('Reorganizare','plan, max. 3 ani'),('Faliment','lichidarea averii')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('diferenta','Diferența',S2),('procedura','Generală sau simplificată',S3),('cine','Cine intră',S4),('faliment','Faliment',S5),('drepturi','Drepturi',S6),('greseli','Greșeli',S7)],
 faq=faq,faq_h2='Întrebări frecvente despre insolvență și faliment',
 contact=dict(h2='Firma ta riscă falimentul?',lead='Trimite-ne situația financiară și datele procedurii. Îți spunem în aceeași zi ce cale este probabilă și ce poți face. Consultația nu te obligă la nimic.',nav='/|Acasă;/insolventa/|Insolvența;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat tribunalelor sau administratorilor judiciari. Informațiile sunt orientative.'),
 howto=dict(name='Cum afli dacă procedura duce la reorganizare sau la faliment',steps=[('Verifici declarația debitorului','Intenția de reorganizare sau de procedură simplificată.'),('Verifici planul','Propus, acceptat de creditori și confirmat.'),('Verifici respectarea planului','Plăți îndeplinite, fără pierderi.'),('Citești încheierea','Judecătorul-sindic decide faliment sau reorganizare.'),('Urmezi etapele','Lichidare și distribuire sau continuarea activității.')]),
 knows=['Insolvență','Faliment','Reorganizare judiciară','Procedura simplificată','Legea 85/2014'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/insolventa-sau-faliment.src.html','w',encoding='utf-8').write(build(P))
