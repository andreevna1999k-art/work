import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'avocat-in-executarea-silita-pasii':('București · debitor','Unde intervine avocatul',
   steps([('Actele primite','Încheiere, somație','Notezi data primirii; termenul curge de aici'),('Dosarul','Cerut executorului','Titlul, calculul, comunicările'),('Contestația','15 zile','La judecătoria sectorului (art. 712, 715 CPC)'),('Suspendarea','Cu cauțiune','Odată cu contestația (art. 719 CPC)'),('Soluția','Anulare sau înțelegere','Sau plată, dacă datoria e reală')],
   'Judecătoria competentă este cea a domiciliului sau sediului debitorului (art. 651 CPC): în București, <b>judecătoria sectorului</b>.'),
   'Cod procedură civilă. Orientativ.','Unde intervine avocatul în executarea silită: acte primite, dosar, contestație în 15 zile, suspendare, soluție','Unde intervine avocatul'),
 'contestatie-negociere-sau-plata':('Comparație','Contestație, negociere sau plată',
   table(['','Contestație','Negociere','Plată'],[['Scop','Anulare sau corectare','Eșalonare, reducere','Stinge datoria'],['Termen','15 zile, în general','Oricând, cu acordul creditorului','Imediat'],['Efect asupra executării','Nu oprește singură; ceri suspendare','Doar dacă creditorul suspendă','Încetează la plata integrală'],['Se potrivește când','Titlu sau calcul greșit','Datorie reală, venit limitat','Datorie reală, ai banii']]),
   'Orientativ; alegerea depinde de titlu și de dosar.','Contestație, negociere sau plată: scop, termen, efect asupra executării și când se potrivește fiecare','Contestație, negociere sau plată'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
opts=[(f'Debitor în Sectorul {i}, București',f'Judecătoria Sectorului {i}: instanța de executare pentru domiciliul sau sediul din Sectorul {i}, 15 zile libere (art. 651, 715 CPC).') for i in range(1,7)]
calc,js=calcs.deadline('Ultima zi pentru contestație <span class="accent">și judecătoria competentă</span>','Alege sectorul în care ai domiciliul sau sediul și data primirii somației ori a adresei de poprire. Vezi judecătoria competentă și ultima zi de depunere, cu sărbători legale.','Sectorul din București',opts,'Data primirii actului','2026-10-12','Exemplu: act primit la 12 octombrie 2026','Ultima zi utilă pentru contestație','Calcul orientativ după art. 715 și art. 181 CPC; competența depinde de domiciliul sau sediul de la data când creditorul a sesizat executorul (art. 651), nu de sediul executorului. Pentru executare fiscală (ANAF) se aplică Codul de procedură fiscală, cu termene proprii. Depune cu cel puțin o zi înainte.',days=16)
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Avocat executare silită în București: răspuns rapid</h2>
        <p>Un avocat de executare silită îți verifică dosarul executorului, calculează termenele, depune contestația la executare la judecătoria competentă, cere suspendarea cu cauțiune (art. 719 CPC) și negociază cu creditorul. În București, instanța de executare este judecătoria sectorului în care ai domiciliul sau sediul, nu biroul executorului (art. 651 CPC). Termenul general este de 15 zile libere (art. 715).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Primești o adresă de poprire pe 12 octombrie 2026. Ultima zi pentru contestație este 12 octombrie + 16 zile = 28 octombrie 2026 (miercuri). Cauțiunea pentru suspendare, la o poprire de 35.000 lei, este 1.000 + 5% × 25.000 = 2.250 lei (art. 719).</p>
          <span class="formula">12.10.2026 + 16 zile = 28.10.2026</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce înseamnă executarea silită și cum începe</h2>
        <p>Executarea silită este recuperarea unei datorii prin executor judecătoresc, pe baza unui titlu executoriu (art. 632 CPC). Începe la cererea creditorului, iar executorul o încuviințează în maximum 3 zile, fără să te cheme (art. 666). Apoi primești încheierea, titlul și, de regulă, o somație (art. 667–668); poprirea se înființează fără somație (art. 783).</p>
        <h3>Forme de executare</h3>
        <div class="t-grid">
          <div class="t-card"><h4>Poprire</h4><p>Conturi și venituri, până la o treime din venitul net la datorii obișnuite (art. 729). Vezi <a href="/poprire-cont/">poprirea pe cont</a>.</p></div>
          <div class="t-card"><h4>Bunuri mobile</h4><p>Sechestru și vânzare; unele bunuri sunt neurmăribile (art. 727).</p></div>
          <div class="t-card"><h4>Imobile</h4><p>Notarea urmăririi în cartea funciară și licitație.</p></div>
        </div>
        <p>Detalii pe etape: <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>'''
S3='''        <span class="eyebrow">Ajutorul avocatului</span>
        <h2>Cum te poate ajuta avocatul de executare silită</h2>
        <ul class="chk">
          <li><b>Verifică dosarul:</b> titlul, caracterul cert, lichid și exigibil al creanței (art. 663), calculul sumei, comunicările.</li>
          <li><b>Depune contestația</b> la executare la instanța competentă (art. 712 CPC). Vezi <a href="/contestatie-la-executare/">contestația la executare</a>.</li>
          <li><b>Cere suspendarea</b> executării, cu cauțiune (art. 719). Vezi <a href="/amanare-executare-silita/">amânarea și suspendarea</a>.</li>
          <li><b>Negociază</b> cu creditorul o eșalonare în scris.</li>
          <li><b>Invocă prescripția</b> sau perimarea, când există (art. 697, 706–707).</li>
        </ul>
'''+F('avocat-in-executarea-silita-pasii')
S4='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura pas cu pas, ca debitor</h2>
        <ol class="num">
          <li><b>Notează data primirii</b> fiecărui act. Termenul de 15 zile curge, de regulă, de la primirea încheierii sau a somației, de la înștiințarea despre poprire (la venituri periodice, cel mai târziu de la prima reținere) ori de la luarea la cunoștință de actul contestat (art. 715).</li>
          <li><b>Cere dosarul de executare.</b></li>
          <li><b>Verifică titlul și calculul.</b></li>
          <li><b>Alege:</b> plată, înțelegere sau contestație. Plata imediată după somație reduce cheltuielile (art. 670 alin. 2).</li>
          <li><b>Depune contestația</b> și, dacă ai motive temeinice, cererea de suspendare.</li>
        </ol>'''
S5='''        <span class="eyebrow">Contestație</span>
        <h2>Contestația la executare: când, unde și cu ce rezultat</h2>
        <p>Poți ataca executarea însăși, încheierile executorului și orice act de executare (art. 712 CPC), dar nu motive pe care le puteai ridica în procesul care a dus la hotărâre (art. 713 alin. 1). O depui la instanța de executare, adică la judecătoria sectorului în care ai domiciliul sau sediul (art. 651, 714). Dacă se admite, instanța anulează actul sau executarea ori încetează executarea (art. 720 alin. 1). Vezi <a href="/unde-se-depune-contestatia-la-executare/">unde se depune contestația</a>.</p>
        <h3>Contestație, negociere sau plată</h3>
'''+F('contestatie-negociere-sau-plata')
S6='''        <span class="eyebrow">Suspendare</span>
        <h2>Suspendarea executării: ce oprește și ce nu</h2>
        <p>Până la soluționarea contestației, instanța poate suspenda executarea pentru motive temeinice, în schimbul unei cauțiuni: 10% din valoare până la 10.000 lei, 1.000 lei + 5% pentru ce depășește 10.000 lei, apoi 5.500 lei + 1% peste 100.000 lei (art. 719 alin. 2). Suspendarea simplă nu ridică singură poprirea existentă (art. 701 alin. 3): ceri expres ridicarea blocajului.</p>'''
S7='''        <span class="eyebrow">Durată și costuri</span>
        <h2>Cât durează și cât costă</h2>
        <p>Legea nu fixează o durată totală. Încuviințarea se dă în 3 zile, iar contestația se judecă de urgență și cu precădere (art. 717 alin. 3). La costuri: taxa de timbru pentru contestație, cel mult 1.000 lei (art. 10 OUG 80/2013), taxa pentru cererea de suspendare și cauțiunea, plus onorariul avocatului, stabilit prin contract scris. Cheltuielile de executare sunt, de regulă, în sarcina debitorului (art. 670).</p>
        <h3>Șanse de câștig</h3>
        <p>Depind de motive și de dovezi: titlu neexecutoriu, sumă greșită, executor necompetent, prescripție, sume nepopribile (art. 729 alin. 7). Nimeni nu poate garanta un rezultat; un motiv real, dovedit cu acte, face diferența.</p>'''
S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și ce faci urgent</h2>
        <ul class="chk">
          <li>Ignori actele executorului.</li>
          <li>Aștepți și ratezi cele 15 zile.</li>
          <li>Plătești fără să ceri calculul.</li>
          <li>Alegi un avocat fără contract scris de onorarii.</li>
        </ul>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată la data la care acționezi.</p>'''
S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi dacă ești executat silit</h2>
        <ol class="num">
          <li>Fotografiază actele și notează data primirii.</li>
          <li>Calculează ultima zi de contestație cu calculatorul de mai sus.</li>
          <li>Trimite-ne actele în chat; îți spunem în aceeași zi dacă merită contestația, suspendarea sau o negociere.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Ce este executarea silită?","Recuperarea unei datorii prin executor judecătoresc, pe baza unui titlu executoriu: poprire, sechestru, vânzarea bunurilor."),
("Cum pot opri executarea silită?","Prin plata sau consemnarea datoriei, prin înțelegere cu creditorul sau prin suspendarea cerută instanței, cu cauțiune (art. 719, 721 CPC)."),
("Ce este contestația la executare?","Cererea prin care ceri instanței să verifice executarea sau actele executorului (art. 712 CPC), în general în 15 zile."),
("Cât durează procedura?","Nu există o durată fixă. Încuviințarea se dă în 3 zile; contestația se judecă de urgență."),
("Cât costă un avocat?","Onorariul se stabilește prin contract. La el se adaugă taxa de timbru (cel mult 1.000 lei pentru contestație) și cauțiunea pentru suspendare."),
("Pot anula executarea silită?","Da, dacă instanța admite contestația: poate anula actul, executarea ori titlul (art. 720 CPC)."),
("Ce șanse am să câștig?","Depind de motive și de dovezi. Nimeni nu poate garanta un rezultat."),
("Ce fac dacă am poprire pe cont?","Notezi data primirii, ceri copia adresei, arăți sumele protejate și contești în 15 zile; suspendarea se cere separat.")]
P=dict(slug='avocat-executare-silita-bucuresti',crumb='Avocat executare silită București',
 title='Avocat executare silită București: contestație, suspendare',
 desc='Cum te ajută un avocat de executare silită în București: verificarea dosarului, contestația la judecătoria sectorului în 15 zile, suspendare cu cauțiune, negociere și costuri.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#servicii|Cum te ajută;#contestatie|Contestație;#suspendare|Suspendare;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='București · executare silită · contestație în 15 zile',
  h1='Avocat executare silită în București: <span class="accent">contestație, suspendare și negociere</span>',
  lead=['Ai primit o somație, o adresă de poprire sau ți s-a blocat contul, iar termenul de 15 zile curge deja. În București, la ce judecătorie depui depinde de sectorul în care locuiești sau ai sediul, nu de biroul executorului.',
        'Aici afli ce face un avocat în fiecare etapă, ce oprește și ce nu oprește o suspendare și cum calculezi ultima zi, cu judecătoria competentă pe sectoare.'],
  meta2='Ultima zi = data + 16 zile',cta='Calculează ultima zi',
  answer='Un avocat de executare silită îți verifică dosarul executorului, calculează termenele, depune contestația la judecătoria sectorului în care ai domiciliul sau sediul (art. 651 CPC), cere suspendarea cu cauțiune (art. 719) și negociază cu creditorul. Termenul general este de 15 zile libere (art. 715).',
  opts=[('Instanță','judecătoria sectorului'),('Contestație','15 zile libere'),('Suspendare','cauțiune, art. 719')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('servicii','Cum te ajută',S3),('procedura','Procedura',S4),('contestatie','Contestația',S5),('suspendare','Suspendarea',S6),('costuri','Durată și costuri',S7),('greseli','Greșeli',S8),('azi','Ce faci azi',S9)],
 faq=faq,faq_h2='Întrebări frecvente despre executarea silită',
 contact=dict(h2='Ai primit acte de executare în București?',lead='Trimite-ne încheierea, somația sau adresa de poprire. Îți spunem în aceeași zi ce termene curg și ce poți face. Consultația nu te obligă la nimic.',nav='/|Acasă;/contestatie-la-executare/|Contestație la executare;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele sunt orientative.'),
 howto=dict(name='Cum contești o executare silită în București',steps=[('Notezi data primirii','Termenul de 15 zile curge de aici.'),('Ceri dosarul','Titlul, calculul și comunicările.'),('Alegi calea','Plată, negociere sau contestație.'),('Depui contestația','La judecătoria sectorului tău.'),('Ceri suspendarea','Cu cauțiune, dacă ai motive temeinice.')]),
 knows=['Executare silită','Contestație la executare','Suspendare','Avocat București'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/avocat-executare-silita-bucuresti.src.html','w',encoding='utf-8').write(build(P))
