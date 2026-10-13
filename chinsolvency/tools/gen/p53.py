import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'etapele-planului-de-reorganizare':('Legea 85/2014 · art. 132–141','Planul de reorganizare, pe etape',
   steps([('Propunerea','30 de zile','De la publicarea tabelului definitiv (art. 132)'),('Votul','Pe categorii','Cel puțin 30% din masa credală (art. 139)'),('Confirmarea','În 15 zile','Judecătorul-sindic fixează termenul (art. 139 alin. 1)'),('Implementarea','Max. 3 ani','De la confirmarea planului (art. 133 alin. 3)'),('Soluția','Închidere sau faliment','Art. 141 și 145')],
   'Dacă planul nu este propus, acceptat și confirmat, judecătorul-sindic decide <b>intrarea în faliment</b> (art. 145).'),
   'Legea nr. 85/2014. Orientativ.','Planul de reorganizare pe etape: propunere în 30 de zile, vot, confirmare în 15 zile, implementare maximum 3 ani, soluție','Planul de reorganizare, pe etape'),
 'cine-poate-propune-planul':('Art. 132','Cine poate propune planul',
   cards([('Debitorul','Cu aprobarea AGA','În 30 de zile de la publicarea tabelului definitiv (art. 132 alin. 1 lit. a)',False),('Administratorul judiciar','Din numire','Până la 30 de zile de la publicarea tabelului definitiv (lit. b)',False),('Creditorii','Min. 20% din masa credală','Unul sau mai mulți creditori, în 30 de zile de la publicarea tabelului (lit. c)',True)],3),
   'Legea nr. 85/2014, art. 132. Orientativ.','Cine poate propune planul de reorganizare: debitorul, administratorul judiciar sau creditori cu cel puțin 20% din creanțe','Cine poate propune planul'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.deadline('Ultima zi pentru <span class="accent">propunerea planului</span>','Alege cine propune planul și data publicării tabelului definitiv de creanțe. Calculăm ultima zi de 30 de zile (art. 132), pe zile libere și cu sărbători legale.','Cine propune planul',[
 ('Debitorul (cu aprobarea adunării asociaților/acționarilor)','Debitorul: 30 de zile de la publicarea tabelului definitiv, dacă a formulat intenția de reorganizare (art. 132 alin. 1 lit. a).',31),
 ('Administratorul judiciar','Administratorul judiciar: până la 30 de zile de la publicarea tabelului definitiv (art. 132 alin. 1 lit. b).',31),
 ('Creditori cu cel puțin 20% din valoarea creanțelor','Unul sau mai mulți creditori, împreună cu cel puțin 20% din creanțe: 30 de zile de la publicare (art. 132 alin. 1 lit. c).',31)],
 'Data publicării tabelului definitiv','2026-10-01','Exemplu: tabel publicat la 1 octombrie 2026','Ultima zi pentru depunerea planului','Calcul orientativ după art. 132 din Legea nr. 85/2014: 30 de zile libere (data + 31 zile), mutate la prima zi lucrătoare. Termenele concrete pot fi stabilite și prin încheiere; verifică dosarul și BPI.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Planul de reorganizare în insolvență: răspuns rapid</h2>
        <p>Planul de reorganizare este documentul prin care debitorul persoană juridică în insolvență propune cum își plătește creditorii în timp, cu un program de plată a creanțelor (art. 133 alin. 2 din Legea nr. 85/2014). Îl pot propune debitorul, administratorul judiciar sau creditori cu cel puțin 20% din creanțe, în 30 de zile de la publicarea tabelului definitiv (art. 132). Creditorii votează pe categorii, judecătorul-sindic confirmă (art. 139), iar executarea planului nu poate depăși 3 ani de la confirmare (art. 133 alin. 3).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Tabelul definitiv de creanțe se publică la 1 octombrie 2026. Termenul de 30 de zile se calculează pe zile libere: 1 octombrie + 31 zile = 1 noiembrie 2026, duminică, deci ultima zi utilă este luni, 2 noiembrie 2026. Dacă planul nu se depune, falimentul devine, în general, calea (art. 145).</p>
          <span class="formula">1.10.2026 + 31 zile = 1.11 (duminică) → 2.11.2026</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este reorganizarea judiciară și cum diferă de faliment</h2>
        <p>Reorganizarea judiciară este procedura aplicabilă debitorului persoană juridică aflat în insolvență, în vederea achitării datoriilor conform programului de plată a creanțelor; presupune întocmirea, aprobarea, confirmarea, implementarea și respectarea unui plan (art. 5 pct. 54). Falimentul înseamnă lichidarea averii și dizolvarea (art. 145). Nu pot fi reorganizați debitorii persoane juridice care în ultimii 5 ani au mai fost supuși unei reorganizări (art. 69). Vezi <a href="/insolventa-sau-faliment/">insolvență sau faliment</a> și <a href="/reorganizare-judiciara/">reorganizarea judiciară</a>.</p>
        <h3>Cine poate propune planul</h3>
'''+F('cine-poate-propune-planul')+'''
        <p>Administratorul judiciar este obligat să pună la dispoziția creditorilor informațiile necesare, iar debitorul trebuie să furnizeze actele din art. 67 alin. 1 lit. a, b și e în maximum 10 zile de la solicitare (art. 132).</p>'''
S3='''        <span class="eyebrow">Etape</span>
        <h2>Etapele reorganizării, de la propunere la implementare</h2>
'''+F('etapele-planului-de-reorganizare')+'''
        <ol class="num">
          <li><b>Deschiderea procedurii</b> și suspendarea executărilor (art. 75).</li>
          <li><b>Elaborarea planului</b> și depunerea lui în termen (art. 132).</li>
          <li><b>Votul creditorilor</b>, pe categorii, în adunarea creditorilor.</li>
          <li><b>Confirmarea:</b> judecătorul-sindic fixează termenul în cel mult 15 zile de la depunerea procesului-verbal al adunării, iar planul trebuie să respecte legalitatea și viabilitatea (art. 139).</li>
          <li><b>Implementarea:</b> debitorul își conduce activitatea sub supravegherea administratorului judiciar, conform planului (art. 141).</li>
          <li><b>Eșecul sau încheierea:</b> încheierea procedurii sau trecerea la faliment (art. 141, 143, 145).</li>
        </ol>'''
S4='''        <span class="eyebrow">Votul</span>
        <h2>Condițiile pentru confirmarea planului</h2>
        <p>Planul este acceptat, după numărul de categorii de creanțe: la cinci categorii, cel puțin trei trebuie să-l accepte; la trei categorii, cel puțin două; la două sau patru, cel puțin jumătate. În toate cazurile trebuie ca una dintre categoriile defavorizate să accepte planul și ca cel puțin 30% din totalul valoric al masei credale să-l accepte (art. 139 alin. 1 lit. A–C). Categoria defavorizată care respinge planul trebuie tratată corect și echitabil (lit. D); creanțele plătite integral în 30 de zile de la confirmare ori potrivit contractelor de credit sau leasing sunt considerate nedefavorizate și acceptate (lit. E).</p>
        <h3>Tratamentul corect și echitabil</h3>
        <ul class="chk">
          <li>Nicio categorie care respinge planul nu primește mai puțin decât în faliment (art. 139 alin. 2 lit. a).</li>
          <li>Nicio categorie nu primește mai mult decât valoarea totală a creanței sale (lit. b).</li>
        </ul>'''
S5='''        <span class="eyebrow">Conținut</span>
        <h2>Ce trebuie să conțină planul de reorganizare</h2>
        <ul class="chk">
          <li><b>Perspectivele de redresare</b>, în raport cu posibilitățile și specificul activității, mijloacele financiare și cererea pieței (art. 133 alin. 1).</li>
          <li><b>Programul de plată a creanțelor</b>, obligatoriu (art. 133 alin. 2).</li>
          <li><b>Categoriile de creanțe nedefavorizate</b> și tratamentul celor defavorizate (art. 133 alin. 4).</li>
          <li><b>Măsurile de punere în aplicare</b>: păstrarea conducerii de către debitor sub supraveghere, resurse financiare, lichidarea parțială a activului, darea în plată către creditori doar cu acordul lor scris, modificarea cauzelor de preferință cu garanții echivalente (art. 133 alin. 5). Vezi <a href="/darea-in-plata-in-procedura-insolventei/">darea în plată în insolvență</a>.</li>
          <li><b>Durata:</b> maximum 3 ani de la confirmare; termenele din contracte de credit sau leasing pot fi menținute chiar dacă depășesc 3 ani (art. 133 alin. 3).</li>
        </ul>'''
S6='''        <span class="eyebrow">Efecte</span>
        <h2>Efectele confirmării și rolul administratorului judiciar</h2>
        <p>La intrarea în vigoare a sentinței de confirmare, activitatea debitorului este reorganizată, iar creanțele și drepturile creditorilor sunt modificate cum prevede planul (art. 140). În perioada de reorganizare, debitorul conduce activitatea sub supravegherea administratorului judiciar, conform planului, până când judecătorul-sindic dispune închiderea procedurii sau trecerea la faliment (art. 141). Raportările către comitetul creditorilor se fac trimestrial (art. 144).</p>
        <h3>Când eșuează reorganizarea</h3>
        <p>Dacă debitorul nu respectă planul ori activitatea produce pierderi sau noi datorii, oricare creditor sau administratorul judiciar poate cere falimentul; cererea se judecă de urgență și cu precădere (art. 143 alin. 1). Un creditor curent cu creanță certă, lichidă, exigibilă, mai veche de 60 de zile și peste valoarea-prag poate cere trecerea la faliment oricând în timpul planului (art. 143 alin. 3), cu excepția cazului în care creanța e achitată sau debitoarea încheie o convenție de plată.</p>'''
S7='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile creditorilor și avantajele reorganizării</h2>
        <ul class="chk">
          <li><b>Creditorii:</b> votează planul, urmăresc respectarea lui și pot cere falimentul dacă nu e respectat (art. 143).</li>
          <li><b>Creditorii garantați:</b> pot cere ridicarea suspendării în condițiile art. 78; sumele din vânzarea bunurilor grevate se distribuie titularilor garanțiilor (art. 133 alin. 5 lit. F).</li>
          <li><b>Debitorul:</b> continuă activitatea, cu executările suspendate (art. 75), dar sub supraveghere.</li>
          <li><b>Risc:</b> eșecul planului duce la faliment, iar sumele deja plătite se scad din creanțele înscrise în tabelul definitiv (art. 140 alin. 1).</li>
        </ul>'''
S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și cum redactezi planul</h2>
        <ul class="chk">
          <li>Proiecții financiare nerealiste și program de plăți imposibil de respectat: judecătorul verifică viabilitatea (art. 139 alin. 1 lit. F).</li>
          <li>Lipsa susținerii creditorilor: fără cvorumul din art. 139, planul nu se confirmă.</li>
          <li>Depunerea după termenul de 30 de zile (art. 132).</li>
        </ul>
        <p>Structura practică: situația actuală, cauzele insolvenței, programul de plată pe categorii, măsurile de redresare, fluxurile financiare estimate și calendarul plăților. Textele din Legea nr. 85/2014 sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>
        <!--@author practice="insolvență" -->'''
faq=[("Ce este un plan de reorganizare în insolvență?","Documentul prin care debitorul persoană juridică propune plata creanțelor în timp, cu un program de plăți, supus votului creditorilor și confirmat de judecătorul-sindic (art. 133, 139)."),
("Cine poate propune planul de reorganizare?","Debitorul, administratorul judiciar sau creditori cu cel puțin 20% din valoarea creanțelor, în 30 de zile de la publicarea tabelului definitiv (art. 132)."),
("Care este diferența dintre reorganizare și faliment?","Reorganizarea urmărește plata creanțelor prin plan, cu continuarea activității; falimentul înseamnă lichidarea averii și dizolvarea persoanei juridice (art. 145)."),
("Cât durează procedura de reorganizare?","Executarea planului nu poate depăși 3 ani de la confirmare (art. 133 alin. 3)."),
("Ce se întâmplă dacă planul este respins?","Dacă nu a fost acceptat și confirmat niciun plan, judecătorul-sindic decide intrarea în faliment (art. 145)."),
("Cum votează creditorii planul?","Pe categorii: de exemplu, la cinci categorii cel puțin trei trebuie să accepte, plus o categorie defavorizată și cel puțin 30% din valoarea masei credale (art. 139)."),
("Ce trebuie să conțină planul?","Perspectivele de redresare, programul de plată a creanțelor, tratamentul categoriilor defavorizate și măsurile de punere în aplicare (art. 133)."),
("Se suspendă executarea silită în reorganizare?","Da, de la deschiderea procedurii executările se suspendă de drept (art. 75).")]
P=dict(slug='plan-reorganizare-insolventa',crumb='Plan de reorganizare în insolvență',
 title='Plan de reorganizare în insolvență: etape și condiții',
 desc='Cum funcționează planul de reorganizare în insolvență: cine îl propune (art. 132), ce conține (art. 133), votul creditorilor și confirmarea (art. 139), durata maximă de 3 ani.',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#etape|Etape;#vot|Votul;#continut|Conținut;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Legea 85/2014 · art. 132–141 · maximum 3 ani',
  h1='Plan de reorganizare în insolvență: <span class="accent">etape, vot și condiții pentru firme și creditori</span>',
  lead=['Firma e în insolvență și creditorii întreabă dacă există un plan, sau ești creditor și vrei să știi ce primești și când. Planul de reorganizare are termene scurte de depunere și reguli precise de vot.',
        'Aici afli cine îl propune, ce trebuie să conțină, cum votează creditorii, cum îl confirmă judecătorul-sindic și ce urmează la eșec, plus un calculator pentru termenul de 30 de zile.'],
  meta2='Propunere: 30 de zile',cta='Calculează termenul',
  answer='Planul de reorganizare este documentul prin care debitorul persoană juridică în insolvență propune cum își plătește creditorii, cu un program de plată (art. 133 alin. 2 din Legea nr. 85/2014). Îl pot propune debitorul, administratorul judiciar sau creditori cu cel puțin 20% din creanțe, în 30 de zile de la publicarea tabelului definitiv (art. 132); se votează pe categorii și se confirmă de judecătorul-sindic (art. 139), pe cel mult 3 ani.',
  opts=[('Propunere','30 de zile (art. 132)'),('Vot','min. 30% din masa credală'),('Durată','max. 3 ani')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('etape','Etape',S3),('vot','Votul',S4),('continut','Conținut',S5),('efecte','Efecte',S6),('drepturi','Drepturi',S7),('greseli','Greșeli',S8)],
 faq=faq,faq_h2='Întrebări frecvente despre planul de reorganizare',
 contact=dict(h2='Vrei un plan de reorganizare sau îl votezi ca creditor?',lead='Trimite-ne tabelul de creanțe, situația financiară sau planul propus. Îți spunem în aceeași zi ce termene curg și ce șanse de confirmare ai. Consultația nu te obligă la nimic.',nav='/|Acasă;/reorganizare-judiciara/|Reorganizare judiciară;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat tribunalelor sau administratorilor judiciari. Informațiile sunt orientative.'),
 howto=dict(name='Cum se parcurge planul de reorganizare',steps=[('Propui planul','În 30 de zile de la publicarea tabelului definitiv.'),('Creditorii votează','Pe categorii, cu minimum 30% din masa credală.'),('Judecătorul confirmă','În cel mult 15 zile de la procesul-verbal al adunării.'),('Implementezi planul','Maximum 3 ani, sub supraveghere.'),('Închiderea sau falimentul','Conform art. 141 și 145.')]),
 knows=['Plan de reorganizare','Insolvență','Reorganizare judiciară','Legea 85/2014'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/plan-reorganizare-insolventa.src.html','w',encoding='utf-8').write(build(P))
