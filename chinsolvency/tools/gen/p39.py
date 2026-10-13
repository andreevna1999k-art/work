import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'cesiunea-creantei-rabon':('Cesiunea creanței','Datoria a trecut la altcineva',
   steps([('Contractul','Banca și debitorul','Creditul inițial'),('Cesiunea','Banca vinde creanța','Către un cesionar'),('Notificarea','Debitorul este înștiințat','Cesiunea nu schimbă datoria'),('Verificarea','Suma, actele, prescripția','Ceri documentele'),('Răspunsul','Plată, negociere sau contestație','Cu respectarea termenelor')]),
   'Orientativ; despre drepturile generale ale debitorului, nu despre o companie anume.','Cesiunea creanței: banca vinde creanța, debitorul este înștiințat, verifică suma, actele și prescripția și răspunde în termen','Cesiunea creanței pas cu pas'),
 'contestatia-la-executare-pasii-rabon':('Contestația la executare','Pașii contestației',
   steps([('Primești actul','Somație sau poprire','Notează data primirii'),('Termen','15 zile','De la luarea la cunoștință (art. 715)'),('Cererea','La instanța de executare','Motive și probe (art. 712)'),('Suspendare','Cu cauțiune','Doar pentru motive temeinice (art. 719)'),('Soluția','Admitere sau respingere','Hotărâre cu căi de atac')]),
   'CPC art. 712, 715, 719. Orientativ.','Pașii contestației la executare: actul de executare, termenul de 15 zile, cererea la instanță, suspendarea cu cauțiune și soluția','Pașii contestației la executare'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.deadline('Termenul contestației la executare <span class="accent">de la primirea actului</span>','Introdu data la care ai luat cunoștință de actul de executare (somație, poprire). Calculăm termenul de 15 zile din art. 715 CPC, pe zile libere.','Actul primit',[
 ('Somație sau alt act de executare propriu-zisă','Contestația se face în 15 zile de la data când ai luat cunoștință de actul contestat (art. 715 alin. 1 pct. 1).',16),
 ('Înștiințare de înființare a popririi','Termenul curge de la primirea înștiințării; la venituri periodice, cel mai târziu de la prima reținere (art. 715 alin. 1 pct. 2).',16)],
 'Data primirii actului','2026-10-01','Exemplu: act primit la 1 octombrie 2026','Contestația, cel târziu','Calcul orientativ: 15 zile libere, mutate la prima zi lucrătoare dacă ultima zi este nelucrătoare. Termenul poate diferi în alte situații (art. 715, 716); verifică actul concret.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Rabon Credit Solutions: răspuns rapid</h2>
        <p>Rabon Credit Solutions România SRL este, potrivit datelor publice din registre, o societate cu obiect de activitate legat de recuperarea creanțelor (CAEN 8291), cunoscută ca cesionar al unor credite bancare. Dacă ai primit o notificare, nu se schimbă existența datoriei prin simplul fapt al cesiunii, dar ai dreptul să verifici suma, documentele și prescripția. Dacă a început executarea silită, termenul pentru contestație este în general de 15 zile de la luarea la cunoștință de actul de executare (art. 715 CPC).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Primești o somație la 1 octombrie 2026. Termenul de 15 zile, calculat pe zile libere, se încheie la 16 octombrie 2026. Dacă ratezi termenul, pierzi, de regulă, contestația pentru acel act.</p>
          <span class="formula">1.10.2026 + 16 zile = 17.10 (sâmbătă) → 19.10.2026</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S1=S1.replace('se încheie la 16 octombrie 2026','se încheie sâmbătă, 17 octombrie, deci se mută luni, 19 octombrie 2026')
S2='''        <span class="eyebrow">Cine</span>
        <h2>Cine este Rabon Credit Solutions România (doar date publice)</h2>
        <p>Date din registre publice: Rabon Credit Solutions România SRL, CUI 26394839, fostă Rabon Expert SRL, cu activitate principală CAEN 8291 (activități ale agențiilor de colectare). Se menționează public ca achizitor și recuperator de credite, în special foste credite ipotecare. Statutul curent al societății se verifică la Registrul Comerțului la data la care citești. Nu evaluăm compania; ne interesează drepturile tale ca debitor.</p>'''
S3='''        <span class="eyebrow">Cesiunea</span>
        <h2>Ce înseamnă că datoria ta a fost cesionată</h2>
'''+F('cesiunea-creantei-rabon')+'''
        <p>Cesiunea de creanță este transmiterea dreptului de a cere plata de la creditorul inițial (banca) către un alt creditor (cesionarul). Datoria rămâne aceeași ca întindere: cesionarul nu poate cere mai mult decât avea banca, dar poate cere ce era datorat valabil. Regulile cesiunii sunt în Codul civil; numerele articolelor se verifică în textul consolidat.</p>
        <p>Verifică: cine este creditorul acum, dacă ai primit notificarea de cesiune, ce sumă se cere (capital, dobânzi, penalități) și pe ce document. Detalii despre recuperatori găsești la <a href="/recuperatorii-de-creante/">recuperatorii de creanțe</a> și la <a href="/legea-impotriva-recuperatorilor-de-credite/">legea împotriva recuperatorilor de credite</a>.</p>'''
S4='''        <span class="eyebrow">Notificarea</span>
        <h2>Notificarea de scadență anticipată: ce verifici</h2>
        <ul class="chk">
          <li><b>Expeditorul:</b> cine a trimis-o și în ce calitate (creditor, cesionar, mandatar).</li>
          <li><b>Contractul de credit și actul de cesiune:</b> ai dreptul să ceri copii ale documentelor pe care se bazează cererea.</li>
          <li><b>Suma:</b> defalcare pe capital, dobândă, comisioane, penalități și plățile făcute de tine.</li>
          <li><b>Termenul de plată</b> din notificare și consecințele anunțate.</li>
          <li><b>Răspunsul scris:</b> trimite-l cu confirmare de primire, fără să recunoști suma înainte de verificare.</li>
        </ul>'''
S5='''        <span class="eyebrow">Verificarea</span>
        <h2>Cum verifici suma cerută și prescripția</h2>
        <p>Cere extrasul de cont al creditului și calculul sumei. Compară cu ce ai plătit. Dreptul de a obține executarea silită se prescrie în 3 ani, dacă legea nu prevede altfel (art. 706 CPC); termenul începe când se naște dreptul de a obține executarea. Prescripția dreptului la acțiune și întreruperea ei sunt reglementate în Codul civil; calculul concret depinde de data scadenței și de actele întreruptive, de aceea se verifică cu un jurist.</p>
        <p>Vezi și <a href="/perimarea-executarii-silite/">perimarea executării silite</a>.</p>'''
S6='''        <span class="eyebrow">Executarea</span>
        <h2>Contestația la executare dacă a început executarea</h2>
'''+F('contestatia-la-executare-pasii-rabon')+'''
        <p>Împotriva executării silite și a oricărui act de executare se poate face contestație de către cei interesați sau vătămați (art. 712 CPC). Termenul este de 15 zile de la luarea la cunoștință de actul contestat, ori de la primirea înștiințării despre poprire, dacă legea nu prevede altfel (art. 715). Până la soluționare, instanța poate suspenda executarea pentru motive temeinice, cu cauțiune stabilită procentual din valoarea obiectului contestației (art. 719).</p>
        <p>Pe larg: <a href="/contestatie-la-executare/">contestația la executare</a> și <a href="/termen-contestatie-la-executare/">termenul contestației</a>. Dacă ai cont blocat: <a href="/poprire-cont/">poprirea contului</a>.</p>'''
S7='''        <span class="eyebrow">Opțiuni</span>
        <h2>Darea în plată (Legea 77/2016) și alte opțiuni</h2>
        <ul class="chk">
          <li><b>Negociere:</b> eșalonare, reducerea dobânzilor sau achitarea unei sume globale, convenite în scris.</li>
          <li><b>Darea în plată a imobilului ipotecat:</b> Legea nr. 77/2016 reglementează darea în plată pentru anumite credite garantate cu ipotecă; condițiile (sume, tipul creditului, calitatea creditorului) se verifică în textul actual al legii și pentru situația ta concretă.</li>
          <li><b>Insolvența persoanei fizice:</b> Legea nr. 151/2015 pentru debitori neprofesioniști, cu condiții de verificat.</li>
          <li><b>Contestația la executare</b>, dacă executarea nu este legală sau suma este greșită.</li>
        </ul>'''
S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente ale debitorilor</h2>
        <ul class="chk">
          <li>Ignorarea actelor de executare: termenul de 15 zile curge din ziua în care ai luat cunoștință.</li>
          <li>Plata unei sume fără a verifica calculul și documentele.</li>
          <li>Recunoașterea datoriei în convorbiri, fără răspuns scris.</li>
          <li>Pierderea termenului pentru contestație.</li>
        </ul>'''
S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Notează data la care ai primit fiecare act și calculează cele 15 zile.</li>
          <li>Cere în scris contractul, actul de cesiune și calculul sumei.</li>
          <li>Trimite-ne documentele în chat; îți spunem în aceeași zi ce pași se potrivesc.</li>
        </ol>
        <!--@author practice="recuperare creanțe" -->'''
faq=[("Cine este Rabon Credit Solutions România?","O societate cu răspundere limitată, CUI 26394839, cu activitate principală legată de recuperarea creanțelor, potrivit datelor din registre publice; statutul se verifică la Registrul Comerțului."),
("Ce este recuperarea creanțelor?","Procesul prin care un creditor sau un cesionar cere plata unei datorii, amiabil sau pe cale judiciară."),
("Poate un recuperator să înceapă executarea silită?","Executarea silită se face de executor judecătoresc, pe baza unui titlu executoriu; un recuperator poate cere executarea doar dacă are calitatea de creditor și un titlu executoriu."),
("Cum contest executarea silită?","Prin contestație la executare, în general în 15 zile de la luarea la cunoștință de actul de executare (art. 712, 715 CPC)."),
("Ce este cesiunea de creanță?","Transmiterea dreptului de a cere plata de la creditorul inițial către un alt creditor; datoria nu devine mai mare prin cesiune."),
("Pot suspenda executarea silită?","Instanța poate suspenda executarea, la cerere și pentru motive temeinice, cu cauțiune (art. 719 CPC)."),
("Cum verific dacă datoria este prescrisă?","Se verifică data scadenței și actele întreruptive; dreptul de a obține executarea se prescrie în 3 ani, dacă legea nu prevede altfel (art. 706 CPC). Cere un calcul concret unui jurist."),
("Ce drepturi are debitorul?","Să primească notificarea, să ceară documentele și calculul sumei, să conteste executarea și să negocieze sau să ceară soluții legale.")]
answer='Dacă ai primit o notificare de la Rabon Credit Solutions România, cesiunea nu schimbă faptul că verifici suma, documentele și prescripția. Dacă a început executarea silită, contestația se face în general în 15 zile de la luarea la cunoștință de actul de executare (art. 715 CPC), iar instanța poate suspenda executarea cu cauțiune (art. 719).'
P=dict(slug='rabon-credit-solutions-executare-silita',crumb='Rabon Credit Solutions',title='Rabon Credit Solutions: executare silită și contestație',
 desc='Ai primit o notificare de la Rabon Credit Solutions? Cesiunea creanței, verificarea sumei și a prescripției, contestația la executare în 15 zile și drepturile debitorului.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#cesiune|Cesiunea;#contestatie|Contestația;#optiuni|Opțiuni;#intrebari|Întrebări',
 images=[x+'.webp' for x in IM],
 hero=dict(eyebrow='Ghid pentru debitori · cesiune · executare silită',h1='<span class="accent">Rabon Credit Solutions</span>: ce faci dacă ai primit o notificare',
  lead=['Ai primit o scrisoare sau un telefon despre o datorie preluată de Rabon Credit Solutions și nu știi ce urmează. Nu panica, dar nu ignora actele: unele au termene scurte.','Aici vezi ce înseamnă cesiunea, ce verifici, cum contești executarea și un calculator pentru termenul de 15 zile.'],
  meta2='CPC art. 712, 715, 719',cta='Calculează termenul',answer=answer,opts=[('Contestație','15 zile (art. 715)'),('Suspendare','cu cauțiune (art. 719)'),('Prescripție','3 ani pentru executare (art. 706)')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('cine','Cine este',S2),('cesiune','Cesiunea',S3),('notificare','Notificarea',S4),('verificare','Verificarea',S5),('contestatie','Contestația',S6),('optiuni','Opțiuni',S7),('greseli','Greșeli',S8),('azi','Ce faci azi',S9)],
 faq=faq,faq_h2='Întrebări frecvente despre Rabon Credit Solutions',
 contact=dict(h2='Ai primit o notificare sau un act de executare?',lead='Trimite-ne documentele în chat. Îți spunem în aceeași zi ce termene curg și ce pași se potrivesc. Consultația nu te obligă la nimic.',nav='/|Acasă;/recuperatorii-de-creante/|Recuperatori;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat Rabon Credit Solutions. Informațiile sunt generale și orientative; nu evaluăm compania.'),
 howto=dict(name='Ce faci dacă ai primit o notificare de la un cesionar',steps=[('Notezi datele','Data primirii fiecărui act.'),('Ceri documentele','Contract, cesiune, calculul sumei.'),('Verifici suma și prescripția','Cu un calcul concret.'),('Calculezi termenul de 15 zile','Dacă a început executarea.'),('Contești sau negociezi','În scris, cu probe.')]),
 knows=['Cesiune de creanță','Executare silită','Contestație la executare','Recuperare creanțe'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/rabon-credit-solutions-executare-silita.src.html','w',encoding='utf-8').write(build(P))
