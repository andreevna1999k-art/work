import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'etapele-procedurii-insolventei-cronologic':('Legea 85/2014','Etapele insolvenței, cronologic',
   steps([('Cererea','Debitor sau creditor','Art. 66 și art. 70'),('Deschiderea','Judecătorul-sindic','Încheiere; administrator sau lichidator provizoriu (art. 71, 73)'),('Observația','Până la plan sau faliment','Executările suspendate de drept (art. 75, art. 5 pct. 42)'),('Creanțele','Admitere și tabele','Cerere de admitere (art. 104); tabel definitiv (art. 112)'),('Soluția','Plan sau lichidare','Reorganizare (art. 132) sau faliment (art. 145, 154)')],
   'Închiderea procedurii: lipsa bunurilor sau a sumelor pentru cheltuieli (art. 174) ori plata integrală a creditorilor (art. 178).'),
   'Legea nr. 85/2014. Orientativ.','Etapele procedurii insolvenței în ordine cronologică: cerere, deschidere, observație, creanțe, plan sau faliment, închidere','Etapele insolvenței, cronologic'),
 'cine-face-ce-in-procedura-insolventei':('Actori','Cine face ce în insolvență',
   cards([('Judecătorul-sindic','Conduce procedura','Deschide procedura, confirmă planul, decide falimentul (art. 71, 139, 145)',True),('Administratorul judiciar','Supraveghează','Supraveghează averea și planul; numit provizoriu la deschidere (art. 73)',False),('Lichidatorul judiciar','Lichidează averea','Vinde bunurile sub controlul judecătorului-sindic (art. 154)',False),('Debitorul','Depune actele','În 10 zile de la deschidere, actele din art. 67 (art. 74)',False),('Creditorii','Cerere de admitere','Se înscriu în tabel și votează planul (art. 104, 139)',False),('Comitetul creditorilor','Raportări','Primește rapoarte trimestriale (art. 144)',False)],3),
   'Legea nr. 85/2014. Orientativ.','Cine face ce în procedura insolvenței: judecătorul-sindic, administratorul judiciar, lichidatorul, debitorul, creditorii și comitetul creditorilor','Cine face ce în insolvență'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.select('În ce etapă <span class="accent">ești?</span>','Alege etapa în care se află procedura. Îți arătăm cine acționează, ce urmează și temeiul din Legea nr. 85/2014.','Etapa procedurii',[
 ('Insolvență apărută, procedură încă nedeschisă','Debitorul trebuie să ceară deschiderea în 30 de zile (art. 66); un creditor poate cere cu creanță de minimum 40.000 lei (art. 70).','Cerere la tribunal.','Strânge actele din art. 67 sau dovada creanței.'),
 ('Procedura a fost deschisă (încheiere / sentință)','Executările se suspendă de drept (art. 75); se numește administrator judiciar sau lichidator (art. 73).','Debitorul depune actele în 10 zile (art. 74).','Creditorii își depun cererile de admitere (art. 104).'),
 ('Perioada de observație: creanțe și tabele','Se verifică creanțele și se întocmesc tabelele; perioada durează până la confirmarea planului sau intrarea în faliment (art. 5 pct. 42).','Administratorul judiciar și judecătorul-sindic.','Contestă creanțele, dacă e cazul, și pregătește planul.'),
 ('Se propune un plan de reorganizare','Planul se depune în 30 de zile de la publicarea tabelului definitiv (art. 132), se votează și se confirmă (art. 139).','Debitor, administrator judiciar sau creditori cu minimum 20%.','Executarea planului: maximum 3 ani (art. 133 alin. 3).'),
 ('Faliment și lichidare','Judecătorul-sindic decide falimentul (art. 145), ridică dreptul de administrare și numește lichidator.','Lichidatorul judiciar (art. 154).','Distribuirea sumelor în ordinea legii (art. 159), apoi închiderea (art. 174).')],
 0,'Exemplu: insolvență apărută, procedură nedeschisă','Ce se întâmplă','Cine acționează / termen','Ce faci tu','Orientativ, după Legea nr. 85/2014. Termenele concrete se stabilesc prin încheieri și prin BPI; verifică dosarul.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Etapele procedurii insolvenței: răspuns rapid</h2>
        <p>Procedura insolvenței urmează, de regulă: cererea (a debitorului sau a unui creditor), deschiderea procedurii de către judecătorul-sindic, perioada de observație cu verificarea creanțelor, apoi un plan de reorganizare sau falimentul cu lichidarea averii, și în final închiderea procedurii (Legea nr. 85/2014). De la deschidere, executările silite se suspendă de drept (art. 75). Planul de reorganizare nu poate depăși 3 ani de la confirmare (art. 133 alin. 3).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Un debitor devine insolvent la 1 octombrie: are 30 de zile să ceară deschiderea procedurii (art. 66). După deschidere depune actele în 10 zile (art. 74), creditorii se pot opune în 10 zile de la notificare, iar tabelul definitiv fixează masa credală. Planul se propune în 30 de zile de la publicarea lui (art. 132) și se execută în maximum 3 ani.</p>
          <span class="formula">30 zile (cerere) + 10 zile (acte) + 30 zile (plan) + max. 3 ani (executare)</span>
          <button type="button" class="btn btn-line" data-ex="1">Vezi în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este procedura insolvenței și cine intră în ea</h2>
        <p>Insolvența este starea în care fondurile disponibile nu ajung pentru datoriile certe, lichide și exigibile; se prezumă după 60 de zile de la scadență fără plată (art. 5 pct. 29). Legea nr. 85/2014 se aplică profesioniștilor, cu excepția profesiilor liberale, și regiilor autonome (art. 3). Pentru persoane fizice neprofesioniste, vezi Legea nr. 151/2015. Panoramă: <a href="/insolventa/">insolvența explicată simplu</a>.</p>'''
S3='''        <span class="eyebrow">Etape</span>
        <h2>Etapele procedurii, pe rând</h2>
'''+F('etapele-procedurii-insolventei-cronologic')+'''
        <ol class="num">
          <li><b>Cererea.</b> Debitorul, în 30 de zile de la insolvență (art. 66), sau creditorul cu creanță peste valoarea-prag (art. 70). Vezi <a href="/deschiderea-procedurii-insolventei/">deschiderea procedurii</a>.</li>
          <li><b>Deschiderea.</b> Judecătorul-sindic pronunță încheierea sau sentința; desemnează administratorul judiciar provizoriu sau lichidatorul (art. 71, 73). Notificările către creditori se fac cu cel puțin 10 zile înainte de termenul-limită pentru cererile de admitere (art. 100).</li>
          <li><b>Suspendarea executărilor</b> de drept (art. 75), cu comunicarea către instanțe și bănci (art. 76).</li>
          <li><b>Perioada de observație</b> durează de la deschidere până la confirmarea planului sau intrarea în faliment (art. 5 pct. 42).</li>
          <li><b>Masa credală.</b> Creditorii depun cereri de admitere cu documentele justificative (art. 104); se întocmesc tabelul preliminar și cel definitiv (art. 112).</li>
          <li><b>Reorganizarea:</b> plan propus, votat și confirmat (art. 132–139); <b>sau falimentul</b> (art. 145).</li>
          <li><b>Lichidarea:</b> bunurile se vând în bloc sau individual (art. 154), iar sumele se distribuie în ordinea legii (art. 159 pentru bunurile grevate de garanții).</li>
          <li><b>Închiderea:</b> când nu există bunuri sau sunt insuficiente pentru cheltuieli și niciun creditor nu avansează sumele (art. 174), ori când creditorii sunt plătiți integral în observație (art. 178).</li>
        </ol>'''
S4='''        <span class="eyebrow">Actori</span>
        <h2>Rolul administratorului judiciar și al celorlalți</h2>
'''+F('cine-face-ce-in-procedura-insolventei')+'''
        <p>Administratorul judiciar este numit provizoriu prin sentința de deschidere (art. 73). Supraveghează activitatea debitorului, administrează averea dacă dreptul de administrare i s-a ridicat debitorului și raportează creditorilor și instanței. În procedura simplificată, lichidatorul judiciar preia lichidarea. Vezi <a href="/insolventa-sau-faliment/">insolvență sau faliment</a>.</p>'''
S5='''        <span class="eyebrow">Drepturi</span>
        <h2>Drepturile creditorilor și ale debitorului</h2>
        <ul class="chk">
          <li><b>Creditorii:</b> își depun cererea de admitere (art. 104), contestă creanțele și tabelele, votează planul (art. 139) și pot cere falimentul dacă planul nu este respectat (art. 143).</li>
          <li><b>Debitorul:</b> beneficiază de suspendarea executărilor (art. 75) și de continuarea serviciilor de utilități în observație și reorganizare, dacă e consumator captiv, cu plata în 90 de zile (art. 77); trebuie să depună actele (art. 74) și să colaboreze.</li>
          <li><b>Creditorii garantați</b> pot cere ridicarea suspendării în condițiile art. 78 și primesc sumele din bunurile grevate în ordinea art. 159.</li>
        </ul>'''
S6='''        <span class="eyebrow">Soluții</span>
        <h2>Reorganizare sau faliment</h2>
        <p>Reorganizarea ține afacerea în viață pe baza unui plan confirmat, de maximum 3 ani; falimentul duce la lichidarea averii și, pentru persoanele juridice, la dizolvare (art. 145 alin. 2). Detalii: <a href="/plan-reorganizare-insolventa/">planul de reorganizare</a> și <a href="/reorganizare-judiciara/">reorganizarea judiciară</a>. Pentru bunurile date în plată sau preluate de creditori, vezi <a href="/darea-in-plata-in-procedura-insolventei/">darea în plată în insolvență</a>.</p>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și cum eviți falimentul</h2>
        <ul class="chk">
          <li>Depunerea tardivă a cererii (termen de 30 de zile).</li>
          <li>Lipsa documentelor justificative (art. 67, art. 104).</li>
          <li>Nerespectarea obligațiilor din procedură: actele în 10 zile (art. 74).</li>
        </ul>
        <p>Falimentul se poate evita prin restructurare financiară, negocieri cu creditorii (mandat ad-hoc, concordat preventiv, art. 66 alin. 3) și un plan realist. Pentru creditele bancare, vezi <a href="/restructurare-credit-vs-refinantare/">restructurare credit</a>. Textele din Legea nr. 85/2014 sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>'''
S8='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Stabilește în ce etapă se află procedura (calculator).</li>
          <li>Notează termenele care curg: 30 de zile pentru cerere, 10 zile pentru actele din art. 74, 30 de zile pentru plan.</li>
          <li>Trimite-ne hotărârea sau notificarea primită în chat; îți spunem în aceeași zi ce faci mai departe.</li>
        </ol>
        <!--@author practice="insolvență" -->'''
faq=[("Ce este procedura insolvenței?","Procedura colectivă prin care creditorii sunt plătiți dintr-o avere comună, sub conducerea judecătorului-sindic, prin reorganizare sau lichidare (Legea nr. 85/2014)."),
("Care sunt etapele procedurii insolvenței?","Cererea, deschiderea, perioada de observație cu verificarea creanțelor, plan de reorganizare sau faliment, lichidare și închiderea procedurii."),
("Care este diferența dintre insolvență și faliment?","Insolvența este starea financiară; falimentul este calea procedurii care duce la lichidarea averii (art. 145)."),
("Cine poate cere deschiderea procedurii?","Debitorul (obligatoriu în 30 de zile, art. 66) sau un creditor cu creanță peste valoarea-prag de 40.000 lei (art. 70)."),
("Ce este masa credală?","Totalitatea creditorilor cu creanțe admise în tabelul creanțelor, plătiți în cadrul procedurii."),
("Ce rol are administratorul judiciar?","Supraveghează activitatea debitorului și administrarea averii și raportează creditorilor și instanței; este numit provizoriu prin sentința de deschidere (art. 73)."),
("Se suspendă executarea silită în insolvență?","Da, de la deschiderea procedurii, de drept (art. 75)."),
("Ce este perioada de observație?","Perioada dintre deschiderea procedurii și confirmarea planului de reorganizare sau intrarea în faliment (art. 5 pct. 42).")]
P=dict(slug='procedura-insolventei-etape',crumb='Etapele procedurii insolvenței',
 title='Etapele procedurii insolvenței: pas cu pas, art. 66–174',
 desc='Etapele procedurii insolvenței în Legea 85/2014: cerere, deschidere, suspendarea executărilor, perioada de observație, masa credală, plan sau faliment, lichidare și închidere.',
 nav='#calculator|În ce etapă ești;#raspuns|Răspuns rapid;#etape|Etape;#actori|Actori;#drepturi|Drepturi;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Legea 85/2014 · etape · observație · lichidare',
  h1='Etapele procedurii insolvenței: <span class="accent">pas cu pas pentru firme și creditori</span>',
  lead=['Procedura de insolvență pare un labirint: termene scurte, tabele, planuri, voturi. În realitate are o ordine clară, iar cine o cunoaște știe unde se află și ce are de făcut.',
        'Aici ai etapele în ordine cronologică, cine face ce, drepturile creditorilor și ale debitorului, plus un instrument care îți arată ce urmează în etapa în care te afli.'],
  meta2='Plan: maximum 3 ani',cta='Vezi etapa ta',
  answer='Procedura insolvenței urmează, de regulă: cererea (a debitorului sau a unui creditor), deschiderea de către judecătorul-sindic, perioada de observație cu verificarea creanțelor, apoi reorganizarea pe bază de plan sau falimentul cu lichidarea averii, și închiderea procedurii (Legea nr. 85/2014). De la deschidere, executările silite se suspendă de drept (art. 75), iar planul nu poate depăși 3 ani de la confirmare.',
  opts=[('Cerere debitor','30 de zile'),('Executări','suspendate de drept'),('Plan','maximum 3 ani')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('etape','Etape',S3),('actori','Actori',S4),('drepturi','Drepturi',S5),('solutii','Reorganizare sau faliment',S6),('greseli','Greșeli',S7),('azi','Ce faci azi',S8)],
 faq=faq,faq_h2='Întrebări frecvente despre procedura insolvenței',
 contact=dict(h2='Ești într-o procedură de insolvență?',lead='Trimite-ne încheierea, notificarea sau tabelul de creanțe. Îți spunem în aceeași zi în ce etapă ești și ce termene curg. Consultația nu te obligă la nimic.',nav='/|Acasă;/insolventa/|Insolvența;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat tribunalelor sau administratorilor judiciari. Informațiile sunt orientative.'),
 howto=dict(name='Etapele procedurii insolvenței',steps=[('Cererea','Debitorul în 30 de zile sau creditorul cu creanță peste 40.000 lei.'),('Deschiderea','Judecătorul-sindic; executările se suspendă.'),('Observația','Cereri de admitere și tabele de creanțe.'),('Planul sau falimentul','Reorganizare, maximum 3 ani, sau lichidare.'),('Închiderea','Plata creditorilor sau lipsa bunurilor.')]),
 knows=['Insolvență','Procedura insolvenței','Legea 85/2014','Reorganizare judiciară','Faliment'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/procedura-insolventei-etape.src.html','w',encoding='utf-8').write(build(P))
