import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
V={
 'iasi':dict(n=54,slug='insolventa-iasi',ci='Iași',trib='Tribunalul Iași',ca='Curtea de Apel Iași',focus='administrator',
  title='Practician în insolvență Iași: servicii, reorganizare firme',h1='Practician în insolvență Iași pentru firme și persoane',
  desc='Ce face un practician în insolvență din Iași: administrator judiciar, lichidator, termene din Legea 85/2014, reorganizare sau faliment și cum alegi un specialist.',
  lead='Firma ta din Iași are datorii scadente și ai auzit că „te preia un practician”. Practicianul în insolvență nu este avocatul tău: este un specialist numit în procedură, cu atribuții și termene stabilite de lege.'),
 'bacau':dict(n=55,slug='insolventa-bacau',ci='Bacău',trib='Tribunalul Bacău',ca='Curtea de Apel Bacău',focus='lichidator',
  title='Practician în insolvență Bacău: servicii și lichidare',h1='Practician în insolvență Bacău pentru firme și persoane',
  desc='Ce face un practician în insolvență din Bacău: administrator, lichidator judiciar, licitații și lichidarea activelor (art. 154–158), reorganizare sau faliment.',
  lead='Firma ta din Bacău se apropie de faliment și vrei să știi cine vinde bunurile, cum se fac licitațiile și cum sunt plătiți creditorii. În insolvență, aceste lucruri le face lichidatorul judiciar, după reguli precise din Legea nr. 85/2014.'),
 'consultant':dict(n=56,slug='consultant-insolventa-sprl',ci='',trib='tribunalul debitorului',ca='',focus='consultant',
  title='Consultant insolvență: servicii, reorganizare și faliment',h1='Consultant insolvență pentru firme și proceduri juridice',
  desc='Ce face un consultant în insolvență, cum diferă de practician și de avocat, când ai nevoie de fiecare, cu termenele din Legea 85/2014 pentru reorganizare și faliment.',
  lead='Firma are probleme cu plățile și cauți un „consultant în insolvență”. Înainte să semnezi ceva, clarifică ce poate face un consultant, ce poate face doar un practician numit de instanță și ce ține de avocat.'),
}
def build_for(k):
    d=V[k]; ci=d['ci']; place=ci or 'România'
    pfx={'iasi':'iasi','bacau':'bacau','consultant':'consultant'}[k]
    IMa=f'rolul-practicianului-{pfx}'; IMb=f'reorganizare-sau-faliment-{pfx}'
    IM={
     IMa:(f'Legea 85/2014 · {place}','Cine face ce în procedură',
      cards([('Judecătorul-sindic','Conduce procedura','Deschide procedura, numește practicianul, confirmă planul (art. 45)',True),('Administratorul judiciar','Supraveghează','Raport în max. 20 de zile și raport asupra cauzelor în max. 40 de zile (art. 58)',False),('Lichidatorul judiciar','Lichidează averea','Vinde bunurile în bloc sau individual, sub controlul judecătorului-sindic (art. 154)',False),('Creditorii','Aprobă și votează','Adunarea creditorilor aprobă tipul de vânzare (art. 154) și votează planul (art. 139)',False),('Debitorul','Depune actele','În 10 zile de la deschidere (art. 74)',False),('Consultantul','Nu este organ al procedurii','Pregătește dosarul și analiza, fără puterile practicianului numit',False)],3),
      'Legea nr. 85/2014, art. 45, 58, 64, 74, 139, 154. Orientativ.',f'Cine face ce în procedura de insolvență: judecătorul-sindic, administratorul judiciar, lichidatorul, creditorii, debitorul și consultantul','Cine face ce în procedură'),
     IMb:('Comparație','Reorganizare sau faliment',
      table(['','Reorganizare judiciară','Faliment'],[['Scop','Plata creanțelor prin plan, cu continuarea activității','Lichidarea averii și plata creditorilor'],['Durată plan','Maximum 3 ani (art. 133 alin. 3)','Până la valorificare și distribuire'],['Rolul practicianului','Administrator judiciar: supraveghere','Lichidator judiciar: vânzarea bunurilor (art. 154)'],['Debitorul persoană juridică','Continuă activitatea, sub supraveghere','Se dizolvă; dreptul de administrare se ridică (art. 145)']]),
      'Legea nr. 85/2014. Orientativ.','Reorganizare judiciară sau faliment: scop, durata planului, rolul practicianului și efectul pentru debitor','Reorganizare sau faliment'),
    }
    def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
    if k=='consultant':
        calc,js=calcs.select('Cine te poate ajuta <span class="accent">în situația ta?</span>','Alege situația. Îți arătăm cine poate face ce: consultantul, practicianul în insolvență numit în procedură sau avocatul.','Situația firmei',[
         ('Firma are întârzieri la plăți, dar nu este în procedură','Analiză financiară și plan de negociere cu creditorii (consultant, practician sau avocat).','Nu există termen legal; insolvența se prezumă după 60 de zile de la scadență (art. 5 pct. 29).','Calculează datoriile scadente și verifică termenul de 30 de zile pentru cerere (art. 66).'),
         ('Firma este în insolvență și trebuie să ceară deschiderea procedurii','Cerere la tribunal, cu actele din art. 67; avocat sau specialist pentru dosar.','30 de zile de la apariția insolvenței (art. 66).','Strânge situațiile financiare, lista bunurilor și a creditorilor.'),
         ('Procedura este deschisă, firma are un administrator judiciar','Administratorul judiciar este numit de judecătorul-sindic (art. 73), nu ales de debitor.','Debitorul depune actele în 10 zile (art. 74).','Colaborează cu administratorul; un consultant te poate ajuta la plan și la documente.'),
         ('Se pregătește planul de reorganizare','Plan propus de debitor, administrator sau creditori cu minimum 20% (art. 132).','30 de zile de la publicarea tabelului definitiv.','Un avocat sau consultant redactează planul; instanța confirmă (art. 139).'),
         ('Firma intră în faliment','Lichidatorul judiciar preia lichidarea (art. 154); consultantul nu poate vinde bunurile.','Adunarea creditorilor în 15 zile de la raportul de evaluare (art. 156).','Urmărește evaluarea, regulamentul de vânzare și distribuirea sumelor.')],
         0,'Exemplu: firma are întârzieri la plăți','Ce se poate face','Termen','Primul pas','Orientativ, după Legea nr. 85/2014. Titlurile profesionale și regimul de autorizare al practicienilor în insolvență se verifică la UNPIR.')
    elif d['focus']=='administrator':
        calc,js=calcs.deadline('Termenele administratorului judiciar <span class="accent">de la numire</span>','Introdu data la care a fost desemnat administratorul judiciar. Calculăm termenele maxime pentru cele două rapoarte din art. 58 alin. 1 din Legea nr. 85/2014, pe zile libere.','Raportul',[
         ('Raportul asupra situației economice (art. 58 alin. 1 lit. a)','Maximum 20 de zile de la desemnare, termen stabilit de judecătorul-sindic (art. 58 alin. 1 lit. a).',21),
         ('Raportul asupra cauzelor insolvenței și șanselor de reorganizare (art. 58 alin. 1 lit. b)','Maximum 40 de zile de la desemnare, termen stabilit de judecătorul-sindic (art. 58 alin. 1 lit. b).',41)],
         'Data desemnării administratorului judiciar','2026-10-01','Exemplu: desemnat la 1 octombrie 2026','Termen maxim pentru raport','Calcul orientativ: judecătorul-sindic stabilește termenul concret, care nu poate depăși 20, respectiv 40 de zile de la desemnare. Se calculează pe zile libere și se mută la prima zi lucrătoare.')
    else:
        calc,js=calcs.deadline('Adunarea creditorilor <span class="accent">după raportul de evaluare</span>','Introdu data la care raportul de evaluare a fost depus la dosar. Calculăm termenul maxim în care lichidatorul judiciar convoacă adunarea creditorilor pentru tipul de vânzare (art. 156 alin. 1).','Etapa',[
         ('Convocarea adunării creditorilor pentru tipul de vânzare','Lichidatorul judiciar convoacă adunarea în maximum 15 zile de la depunerea raportului de evaluare (art. 156 alin. 1).',16)],
         'Data depunerii raportului de evaluare','2026-10-01','Exemplu: raport depus la 1 octombrie 2026','Convocare, cel târziu','Calcul orientativ: 15 zile libere de la depunerea raportului, mutate la prima zi lucrătoare. Tipul de vânzare (licitație publică, negociere directă sau combinație) și regulamentul se aprobă de adunarea creditorilor, la propunerea lichidatorului (art. 154).')
    fm=d['focus']
    loc=(f'Competența aparține tribunalului (sau secției de insolvență, dacă există) în a cărui circumscripție debitorul și-a avut sediul social cel puțin 6 luni înainte de sesizare (art. 41 alin. 1). Pentru debitorii cu sediul în {ci}, aceasta înseamnă {d["trib"]}; apelul merge la {d["ca"]}. Verifică pe portalul instanțelor existența și denumirea secției de insolvență.' if ci else 'Competența aparține tribunalului (sau secției de insolvență, dacă există) în a cărui circumscripție debitorul și-a avut sediul social cel puțin 6 luni înainte de sesizare (art. 41 alin. 1).')
    S1=f'''        <span class="eyebrow">Pe scurt</span>
        <h2>{"Consultant în insolvență" if k=="consultant" else "Practician în insolvență"}: răspuns rapid</h2>
        <p>{"Un consultant în insolvență analizează situația financiară, pregătește dosarul și negocierile, dar nu este organ al procedurii. În procedura de insolvență, activitatea este condusă de judecătorul-sindic, iar administratorul judiciar sau lichidatorul judiciar, numit prin sentința de deschidere (art. 73), supraveghează sau lichidează averea. Termenele contează: cererea debitorului se depune în 30 de zile (art. 66), iar executările se suspendă de drept după deschidere (art. 75)." if k=="consultant" else "Practicianul în insolvență este specialistul numit în procedură ca administrator judiciar sau ca lichidator judiciar (art. 73). Administratorul examinează situația debitorului și depune rapoarte în termene de până la 20, respectiv 40 de zile de la desemnare (art. 58); lichidatorul vinde bunurile, sub controlul judecătorului-sindic (art. 154). Nu este avocatul debitorului și nu poate fi ales liber de acesta, pentru că este desemnat de judecătorul-sindic."}</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>{"Cererea debitorului se depune în 30 de zile de la apariția insolvenței (art. 66). Dacă insolvența apare la 1 octombrie, calculul pe zile libere duce la 1 noiembrie, duminică, deci la luni, 2 noiembrie. Planul de reorganizare, dacă există, se propune în 30 de zile de la publicarea tabelului definitiv (art. 132)." if k=="consultant" else ("Administratorul este desemnat la 1 octombrie 2026. Raportul asupra situației economice poate fi cerut în maximum 20 de zile, deci până la 22 octombrie (pe zile libere, art. 58 alin. 1 lit. a), iar raportul asupra cauzelor insolvenței, în maximum 40 de zile, deci până la 11 noiembrie." if k=="iasi" else "Raportul de evaluare a bunurilor este depus la 1 octombrie 2026. Lichidatorul convocă adunarea creditorilor în maximum 15 zile, pe zile libere până la 16 octombrie, ca să se stabilească tipul de vânzare (art. 156 alin. 1).")}</p>
          <span class="formula">{"1.10.2026 + 31 zile → 2.11.2026" if k=="consultant" else ("1.10.2026 + 21 zile = 22.10.2026" if k=="iasi" else "1.10.2026 + 16 zile = 17.10.2026")}</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
    if k=='bacau': S1=S1.replace('pe zile libere până la 16 octombrie','pe zile libere până la sâmbătă, 17 octombrie, deci mutat luni, 19 octombrie').replace('1.10.2026 + 16 zile = 17.10.2026','1.10.2026 + 16 zile = 17.10 (sâmbătă) → 19.10.2026')
    S2=f'''        <span class="eyebrow">Rolul</span>
        <h2>{"Ce face un consultant și cum diferă de practician și de avocat" if k=="consultant" else "Ce face un practician în insolvență"}</h2>
'''+F(IMa)+f'''
        <p>{loc}</p>
        <h3>Administratorul judiciar</h3>
        <p>Examinează situația economică a debitorului și actele depuse (art. 67, 74), propune procedura simplificată sau continuarea observației, întocmește raportul asupra cauzelor insolvenței și a șanselor de reorganizare și supraveghează activitatea (art. 58).</p>
        <h3>Lichidatorul judiciar</h3>
        <p>Examinează activitatea debitorului în procedura simplificată, conduce activitatea debitorului, inventariază bunurile, introduce acțiuni pentru anularea actelor frauduloase și valorifică averea (art. 64, 154).</p>
        <h3>{"Consultantul și avocatul" if k=="consultant" else "Practician sau avocat"}</h3>
        <p>Practicianul este numit de judecătorul-sindic și acționează în interesul procedurii colective, nu al debitorului. Avocatul reprezintă clientul în instanță. {"Consultantul pregătește analize, dosare și negocieri, dar nu are atribuțiile unui administrator sau lichidator. Verifică în contract ce anume ți se promite." if k=="consultant" else "Poți avea nevoie de ambii: practicianul conduce procedura, avocatul îți apără interesele."}</p>'''
    S3=f'''        <span class="eyebrow">Servicii</span>
        <h2>Servicii: reorganizare, faliment și consultanță</h2>
        <ul class="chk">
          <li><b>Reorganizare judiciară:</b> planul cuprinde obligatoriu programul de plată a creanțelor și nu poate depăși 3 ani de la confirmare (art. 133). Vezi <a href="/plan-reorganizare-insolventa/">planul de reorganizare</a>.</li>
          <li><b>Faliment și lichidare:</b> vânzarea bunurilor în bloc sau individual, distribuirea sumelor după art. 159 pentru bunurile grevate. Vezi <a href="/insolventa-sau-faliment/">insolvență sau faliment</a>.</li>
          <li><b>Consultanță:</b> analiza situației financiare, a riscului de insolvență (prezumție după 60 de zile de la scadență, art. 5 pct. 29), soluții preventive (mandat ad-hoc, concordat preventiv, art. 66 alin. 3).</li>
          <li><b>Persoane fizice:</b> insolvența persoanelor fizice neprofesioniste este în Legea nr. 151/2015; condițiile se verifică în textul consolidat.</li>
        </ul>'''
    S4='''        <span class="eyebrow">Procedura</span>
        <h2>Cum funcționează procedura de insolvență</h2>
        <ol class="num">
          <li><b>Cererea:</b> debitorul, în 30 de zile (art. 66), sau un creditor cu creanță peste valoarea-prag de 40.000 lei (art. 70).</li>
          <li><b>Deschiderea:</b> judecătorul-sindic pronunță încheierea și desemnează administratorul sau lichidatorul provizoriu (art. 71, 73); executările se suspendă de drept (art. 75).</li>
          <li><b>Creanțele:</b> creditorii depun cereri de admitere (art. 104); se întocmesc tabelele (art. 112).</li>
          <li><b>Reorganizare sau faliment</b> (art. 132, 145).</li>
        </ol>
        <p>Detalii: <a href="/procedura-insolventei-etape/">etapele procedurii insolvenței</a> și <a href="/deschiderea-procedurii-insolventei/">deschiderea procedurii</a>.</p>'''
    S5=f'''        <span class="eyebrow">Alegerea specialistului</span>
        <h2>Cum alegi {"consultantul" if k=="consultant" else "practicianul"}</h2>
        <ul class="chk">
          <li><b>Experiență documentată</b> în proceduri similare.</li>
          <li><b>Calitatea de practician în insolvență:</b> cere dovada autorizării și a apartenenței la Uniunea Națională a Practicienilor în Insolvență din România (UNPIR); verifică-o la UNPIR.</li>
          <li><b>Contract scris</b> cu serviciile, onorariul și etapele.</li>
          <li><b>Fără promisiuni de rezultat:</b> nimeni nu poate garanta reorganizarea sau recuperarea creanțelor.</li>
        </ul>
        <p>Atenție: în procedură, practicianul este desemnat de judecătorul-sindic după verificarea incompatibilităților (art. 45 alin. 1 lit. d), nu ales liber de debitor.</p>'''
    S6='''        <span class="eyebrow">Reorganizare sau faliment</span>
        <h2>Diferența dintre reorganizare și faliment</h2>
'''+F(IMb)+'''
        <p>Reorganizarea este recomandată când activitatea are perspective și creditorii acceptă un plan (art. 139). Falimentul urmează când nu s-a propus un plan, planul nu a fost acceptat și confirmat sau nu este respectat (art. 145).</p>'''
    S7='''        <span class="eyebrow">Licitații</span>
        <h2>Lichidarea activelor și licitațiile în insolvență</h2>
        <p>Bunurile din averea debitorului pot fi vândute în bloc sau individual. Tipul de vânzare (licitație publică, negociere directă sau combinație) și regulamentul de vânzare sunt aprobate de adunarea creditorilor, la propunerea lichidatorului; în cazul licitației publice, publicitatea se face și pe site-ul UNPIR. Bunurile se evaluează de evaluatori membri ANEVAR (art. 154). Raportul de evaluare se publică în BPI (art. 155), iar adunarea creditorilor se convocă în maximum 15 zile de la depunerea lui (art. 156 alin. 1). Procesul-verbal de adjudecare semnat de lichidator constituie titlu de proprietate (art. 158 alin. 2). Sumele se distribuie creditorilor în ordinea legii (art. 159).</p>'''
    S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente în procedurile de insolvență</h2>
        <ul class="chk">
          <li>Depunerea tardivă a cererii (30 de zile, art. 66).</li>
          <li>Lipsa documentelor financiare (art. 67).</li>
          <li>Nerespectarea obligațiilor din procedură: actele în 10 zile (art. 74).</li>
          <li>Colaborarea cu persoane neautorizate care promit „rezolvarea” procedurii.</li>
        </ul>
        <p>Textele din Legea nr. 85/2014 sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>'''
    S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Stabilește dacă firma este în stare de insolvență și calculează termenul de 30 de zile.</li>
          <li>Strânge situațiile financiare, lista bunurilor, a creditorilor și a plăților din ultimele 6 luni.</li>
          <li>Trimite-ne datele în chat; îți spunem în aceeași zi ce procedură se potrivește.</li>
        </ol>
        <!--@author practice="insolvență" -->'''
    faq=[("Ce face un practician în insolvență?","Este numit ca administrator judiciar sau lichidator judiciar: supraveghează sau lichidează averea debitorului, sub controlul judecătorului-sindic (art. 58, 64, 154)."),
    (f"Cum aleg {'un consultant' if k=='consultant' else 'un practician'}?","Verifici autorizarea și apartenența la UNPIR, experiența, contractul scris și lipsa promisiunilor de rezultat."),
    ("Care este diferența dintre reorganizare și faliment?","Reorganizarea înseamnă plata creanțelor prin plan, de maximum 3 ani; falimentul înseamnă lichidarea averii și, pentru persoane juridice, dizolvarea (art. 133, 145)."),
    ("Ce servicii oferă un lichidator judiciar?","Inventariază și evaluează bunurile, le vinde în bloc sau individual și distribuie sumele creditorilor (art. 154–159)."),
    ("Cât durează procedura de insolvență?","Nu există o durată fixă; planul de reorganizare nu poate depăși 3 ani de la confirmare (art. 133 alin. 3)."),
    ("Ce rol are administratorul judiciar?","Examinează situația economică și cauzele insolvenței și supraveghează activitatea debitorului; rapoartele se depun în maximum 20, respectiv 40 de zile de la desemnare (art. 58)."),
    ("Se suspendă executarea silită în insolvență?","Da, de la deschiderea procedurii, de drept (art. 75)."),
    ("Ce este masa credală?","Totalitatea creditorilor cu creanțe admise în tabel, plătiți în cadrul procedurii."),
    ("Poate o persoană fizică intra în insolvență?","Persoanele fizice neprofesioniste pot folosi Legea nr. 151/2015, cu condiții de verificat în textul consolidat."),
    ("Ce acte sunt necesare pentru deschiderea procedurii?","La cererea debitorului, actele din art. 67: situații financiare, lista bunurilor și a creditorilor, plăți din ultimele 6 luni, declarații.")]
    answer=(f'Practicianul în insolvență este specialistul numit în procedură ca administrator judiciar sau lichidator judiciar (art. 73 din Legea nr. 85/2014). Administratorul depune rapoarte în maximum 20, respectiv 40 de zile de la desemnare (art. 58), iar lichidatorul vinde bunurile, sub controlul judecătorului-sindic (art. 154). Nu este avocatul debitorului și este desemnat de judecătorul-sindic.' if k!='consultant' else 'Consultantul în insolvență analizează situația financiară și pregătește dosarul și negocierile, dar nu este organ al procedurii: administratorul judiciar sau lichidatorul este numit de judecătorul-sindic (art. 73 din Legea nr. 85/2014). Cererea debitorului se depune în 30 de zile (art. 66), iar executările se suspendă de drept după deschidere (art. 75).')
    opts=[('Raport','20 / 40 de zile (art. 58)'),('Plan','max. 3 ani'),('Executări','suspendate de drept')] if k=='iasi' else ([('Adunare creditori','15 zile de la evaluare'),('Vânzare','în bloc sau individual'),('Titlu','proces-verbal de adjudecare')] if k=='bacau' else [('Cerere','30 de zile (art. 66)'),('Numire','de judecătorul-sindic'),('Executări','suspendate de drept')])
    P=dict(slug=d['slug'],crumb=('Practician în insolvență '+ci) if ci else 'Consultant în insolvență',title=d['title'],desc=d['desc'],
     nav='#calculator|Calculator;#raspuns|Răspuns rapid;#rol|Rolul;#procedura|Procedura;#alegere|Cum alegi;#intrebari|Întrebări',
     images=[x+'.webp' for x in IM],
     hero=dict(eyebrow=('Legea 85/2014 · '+(ci+' · ' if ci else '')+'administrator · lichidator'),
      h1=d['h1'].replace(ci,'<span class="accent">'+ci+'</span>',1) if ci else d['h1'].replace('Consultant insolvență','<span class="accent">Consultant insolvență</span>',1),
      lead=[d['lead'],'Aici vezi rolul fiecăruia, procedura, termenele din lege, cum alegi specialistul și un calculator pentru termenul care contează.'],
      meta2='Legea nr. 85/2014',cta='Calculează termenul',answer=answer,opts=opts),
     calc_html=calc,js=js,
     sections=[('raspuns','Răspuns rapid',S1),('rol','Rolul',S2),('servicii','Servicii',S3),('procedura','Procedura',S4),('alegere','Cum alegi',S5),('diferenta','Reorganizare sau faliment',S6),('licitatii','Licitații',S7),('greseli','Greșeli',S8),('azi','Ce faci azi',S9)],
     faq=faq,faq_h2='Întrebări frecvente despre insolvență',
     contact=dict(h2='Firma ta are datorii scadente?',lead='Trimite-ne situația financiară și lista creditorilor. Îți spunem în aceeași zi ce procedură se potrivește și ce termene curg. Consultația nu te obligă la nimic.',nav='/|Acasă;/insolventa/|Insolvența;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat tribunalelor, UNPIR sau practicienilor. Informațiile sunt orientative.'),
     howto=dict(name='Cum afli ce specialist ai nevoie în insolvență',steps=[('Stabilești situația','Insolvență, procedură deschisă sau faliment.'),('Verifici termenele','30 de zile pentru cerere; 20 și 40 de zile pentru rapoartele administratorului.'),('Distingi rolurile','Practicianul este numit de judecătorul-sindic; avocatul și consultantul te asistă.'),('Verifici autorizarea','La UNPIR, pentru practicieni.'),('Încheii contract scris','Cu servicii, onorariu și etape.')]),
     knows=['Insolvență','Practician în insolvență','Legea 85/2014','Reorganizare judiciară','Faliment'])
    return P,IM
