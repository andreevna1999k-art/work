import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'cum-ridici-poprirea-pasii':('Model cerere · poprire','Cum ridici poprirea pe cont',
   steps([('Plătești sau consemnezi','Toată datoria','Cu accesorii și cheltuieli (art. 721 CPC)'),('Cererea','La executor','Cu dovada plății sau recipisa de consemnare'),('Încheierea','Executorul decide','De urgență, cu citarea părților (art. 721 alin. 2)'),('Banca','Este înștiințată','Executorul informează terțul poprit (art. 784 alin. 6)'),('Contul','Se deblochează','Sumele revin la tine, după încheiere')],
   'Banca <b>nu poate ridica singură</b> poprirea: ea se ridică prin executor, după dovada plății sau prin hotărâre.'),
   'Cod procedură civilă, art. 703, 721, 784. Orientativ.','Cum ridici poprirea pe cont: plată sau consemnare, cerere la executor, încheiere, înștiințarea băncii, deblocare','Cum ridici poprirea, pas cu pas'),
 'ridicare-suspendare-contestatie':('Comparație','Ridicare, suspendare sau contestație',
   table(['','Ridicare (plată)','Suspendare','Contestație'],[['Când','Datoria e plătită sau consemnată','Ai motive temeinice','Executare nelegală'],['Cui','Executorului','Instanței de executare','Instanței de executare'],['Cost','Fără taxă; cheltuielile de executare','Taxă 50 lei + cauțiune','Taxă de timbru, până la 1.000 lei'],['Efect','Executarea încetează sau măsura se desființează','Opresc executarea provizoriu','Anulează actul sau executarea']]),
   'Orientativ; pașii depind de dosar.','Ridicare, suspendare sau contestație: când se folosesc, cui se adresează, cost și efect','Ridicare, suspendare sau contestație'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
calc,js=calcs.select('Ce ceri pentru <span class="accent">ridicarea popririi</span>','Alege motivul pentru care vrei ridicarea. Îți arătăm cui te adresezi, ce dovezi atașezi și temeiul din CPC.','Motivul ridicării',[
 ('Am plătit integral datoria, cu cheltuieli','Cerere de încetare a executării / ridicare a popririi, la executor.','Executorului judecătoresc (art. 703 alin. 1 pct. 1)','Dovada plății, extras de cont, calculul sumei de la executor.'),
 ('Vreau să consemnez toată datoria','Cerere de desființare a măsurilor prin consemnare, la executor.','Executorului; recipisa o depui la el (art. 721, 784 alin. 6)','Recipisa de consemnare cu afectațiune specială, calculul creanței și al cheltuielilor.'),
 ('Poprirea vizează sume nepopribile (alocații, burse)','Contestație la executare, cu cerere de suspendare.','Instanței de executare (art. 712, 714 CPC)','Extras de cont, dovada originii sumelor (art. 729 alin. 7).'),
 ('Titlul nu e executoriu sau datoria e prescrisă','Contestație la executare pentru anularea executării.','Instanței de executare; 15 zile în general (art. 715)','Titlul, actele de executare, dovada comunicărilor.'),
 ('Creditorul renunță la executare','Cerere de încetare a executării, cu acordul creditorului.','Executorului (art. 703 alin. 1 pct. 3)','Înscris de renunțare semnat de creditor.')],
 0,'Exemplu: am plătit integral','Ce ceri','Cui te adresezi','Ce dovezi atașezi','Orientativ, după CPC. Pentru poprirea ANAF se aplică Codul de procedură fiscală, cu proceduri și termene proprii; verifică actul de poprire și cere sfatul unui specialist.')
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Model cerere de ridicare a popririi: răspuns rapid</h2>
        <p>Poprirea pe cont nu o ridică banca, ci executorul judecătoresc, după ce datoria este plătită, consemnată sau executarea este anulată ori încetează (art. 703, 721 CPC). Cererea se adresează executorului, cu dovada plății sau recipisa de consemnare. Dacă poprirea este nelegală, ai nevoie de o contestație la instanța de executare, nu doar de o cerere. Mai jos ai trei modele și instrumentul care îți arată ce ceri.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Datorie de 20.000 lei, cheltuieli de executare 1.500 lei, dobânzi 800 lei. Consemnezi 22.300 lei la dispoziția executorului (art. 721): creanța, accesoriile și cheltuielile. Cât timp nu consemnezi toate sumele pentru care s-a înființat poprirea, indisponibilizarea nu încetează (art. 784 alin. 6).</p>
          <span class="formula">20.000 + 800 + 1.500 = 22.300 lei de consemnat</span>
          <button type="button" class="btn btn-line" data-ex="1">Vezi ce ceri</button>
        </div>'''
S2='''        <span class="eyebrow">Definiție</span>
        <h2>Ce este poprirea bancară și cine o poate înființa</h2>
'''+F('cum-ridici-poprirea-pasii')+'''
        <p>Poprirea indisponibilizează sumele din conturi (soldul și încasările viitoare, art. 781 alin. 2 CPC), din momentul comunicării adresei către bancă (art. 784 alin. 1). O înființează un executor judecătoresc, la cererea creditorului cu titlu executoriu; datoriile către stat se execută prin organele fiscale, după Codul de procedură fiscală. Ghidul complet: <a href="/poprire-cont/">poprirea pe cont</a>.</p>'''
S3='''        <span class="eyebrow">Când se ridică</span>
        <h2>Când poate fi ridicată poprirea</h2>
        <ul class="chk">
          <li><b>Datoria este achitată integral</b>, cu accesorii și cheltuieli: executarea încetează (art. 703 alin. 1 pct. 1).</li>
          <li><b>Consemnezi toată creanța</b> la dispoziția executorului, până la adjudecare: măsurile se desființează (art. 721).</li>
          <li><b>Creditorul renunță</b> la executare (art. 703 alin. 1 pct. 3).</li>
          <li><b>Titlul sau executarea sunt desființate</b> de instanță (art. 703 alin. 1 pct. 4–5, art. 720).</li>
          <li><b>Suspendarea executării</b>, dar atenție: suspendarea simplă păstrează blocajul, dacă nu se dispune altfel (art. 701 alin. 3).</li>
          <li><b>Prescripția</b> dreptului de a cere executarea, invocată de tine (art. 706–707).</li>
        </ul>
        <p>După încetare, executorul întocmește încheierea de încetare, motivată, și o comunică de îndată creditorului și debitorului (art. 703 alin. 2).</p>
'''+F('ridicare-suspendare-contestatie')
S4='''        <span class="eyebrow">Model 1</span>
        <h2>Model: cerere de ridicare a popririi după plată</h2>
        <p>Folosește-l când ai achitat întreaga datorie. Completează datele din dosarul de executare.</p>
        <div class="quote">„Către Biroul Executorului Judecătoresc [__]. Dosar de executare nr. [__]. Subsemnatul/a [nume, CNP, domiciliu], în calitate de debitor în dosarul menționat, vă solicit, în temeiul art. 703 alin. 1 pct. 1 CPC, constatarea încetării executării silite și ridicarea popririi înființate asupra conturilor mele deschise la [bancă], întrucât am achitat integral creanța, dobânzile și cheltuielile de executare. Anexez: dovada plății din data de [__], extrasul de cont, calculul sumei comunicat de executor. Vă rog să comunicați de îndată băncii și mie încheierea de încetare. Data, semnătura.”</div>
        <h3>Date care trebuie completate</h3>
        <ul class="chk">
          <li>Numărul dosarului de executare și datele executorului (din încheiere sau adresa de poprire).</li>
          <li>Datele tale de identificare și contul vizat.</li>
          <li>Suma plătită și data plății, cu documentele.</li>
        </ul>'''
S5='''        <span class="eyebrow">Model 2</span>
        <h2>Model: consemnarea creanței și cererea de desființare a măsurilor</h2>
        <div class="quote">„Către Biroul Executorului Judecătoresc [__]. Dosar nr. [__]. Subsemnatul/a [nume], debitor, am consemnat la [unitatea de consemnare], la dispoziția dumneavoastră, suma de [__] lei, reprezentând creanța, accesoriile și cheltuielile de executare, conform art. 721 CPC. Vă solicit desființarea măsurilor de executare, inclusiv ridicarea popririi asupra conturilor mele, și înștiințarea de îndată a terțului poprit. Anexez recipisa de consemnare. Data, semnătura.”</div>
        <p>Executorul se pronunță de urgență, prin încheiere dată cu citarea părților (art. 721 alin. 2). Recipisa o depui la executor, care îl înștiințează de îndată pe terțul poprit (art. 784 alin. 6).</p>'''
S6='''        <span class="eyebrow">Model 3</span>
        <h2>Model: contestație la executare pentru anularea popririi</h2>
        <p>Dacă poprirea este nelegală (sume nepopribile, titlu neexecutoriu, prescripție, executor necompetent), cererea la executor nu ajunge: depui contestație la instanța de executare, în general în 15 zile (art. 712, 715).</p>
        <div class="quote">„Către Judecătoria [__]. Contestator: [nume]. Intimat: [creditor]. Prin prezenta contestație la executare, în baza art. 712 CPC, solicit anularea popririi înființate în dosarul de executare nr. [__] asupra contului [__], în măsura în care vizează sume nepopribile, potrivit art. 729 alin. 7 CPC, și suspendarea executării până la soluționare, conform art. 719 CPC, cauțiunea fiind consemnată (se anexează dovada). Motive: [__]. Probe: extrasul de cont, dovada originii sumelor, actele de executare. Data, semnătura.”</div>
        <p>Detalii și modele: <a href="/contestatie-la-executare/">contestația la executare</a>, <a href="/amanare-executare-silita/">suspendarea executării</a>, <a href="/termen-contestatie-la-executare/">termenul contestației</a>.</p>'''
S7='''        <span class="eyebrow">ANAF</span>
        <h2>Poprirea ANAF: ce diferă</h2>
        <p>Datoriile către stat se execută prin organele fiscale, după Codul de procedură fiscală, nu prin executor judecătoresc. Cererea de ridicare se adresează organului fiscal care a înființat poprirea, cu dovada plății sau a stingerii obligației. Termenele și căile de contestare sunt cele din legislația fiscală, nu cele din CPC. Verifică actul care fundamentează poprirea și cere sfatul unui specialist înainte să depui.</p>'''
S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente când ceri ridicarea popririi</h2>
        <ul class="chk">
          <li>Trimiți cererea doar băncii: banca nu poate ridica singură poprirea.</li>
          <li>Plătești o parte și crezi că s-a ridicat: executarea încetează doar la plata integrală, cu cheltuieli (art. 703).</li>
          <li>Nu atașezi calculul sumei sau dovada plății.</li>
          <li>Aștepți și ratezi cele 15 zile pentru contestație.</li>
        </ul>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>'''
S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Ce faci azi</h2>
        <ol class="num">
          <li>Cere executorului calculul exact al sumei de plată sau de consemnat.</li>
          <li>Plătește sau consemnează și păstrează dovada.</li>
          <li>Trimite-ne dosarul în chat; îți spunem în aceeași zi ce model folosești.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
faq=[("Cum se face o cerere de ridicare a popririi?","Se adresează executorului judecătoresc, cu dovada plății integrale sau recipisa de consemnare, și cere încetarea executării sau desființarea măsurilor (art. 703, 721 CPC)."),
("Cui se transmite cererea?","Executorului din dosarul de executare. Banca nu ridică singură poprirea; executorul o înștiințează."),
("Cât durează ridicarea popririi bancare?","Legea nu fixează o durată. La consemnare, executorul se pronunță de urgență, prin încheiere dată cu citarea părților (art. 721 alin. 2)."),
("Cum se ridică poprirea ANAF?","Cu cerere la organul fiscal care a înființat-o, cu dovada stingerii obligației, după Codul de procedură fiscală; termenele sunt cele fiscale."),
("Pot suspenda executarea silită?","Da, instanța o poate suspenda cu cauțiune (art. 719 CPC), dar suspendarea simplă nu ridică singură blocajul (art. 701 alin. 3)."),
("Când poate fi anulată poprirea?","Când titlul nu e executoriu, datoria e prescrisă, executorul e necompetent, actele nu ți-au fost comunicate sau se poprește peste limita legii."),
("Ce documente sunt necesare?","Dovada plății sau recipisa de consemnare, extrasul de cont, calculul sumei de la executor și actele de executare primite."),
("Cum contest poprirea bancară?","Prin contestație la executare la instanța de executare, în general în 15 zile (art. 712, 715 CPC).")]
P=dict(slug='model-cerere-ridicare-poprire-cont-bancar-persoana-fizica',crumb='Model cerere ridicare poprire',
 title='Model cerere ridicare poprire cont bancar (persoană fizică)',
 desc='Modele de cerere pentru ridicarea popririi pe cont: după plata datoriei, prin consemnare (art. 721 CPC) și contestație. Cui o trimiți, ce acte atașezi și ce diferă la ANAF.',
 nav='#calculator|Ce ceri;#raspuns|Răspuns rapid;#cand|Când se ridică;#model1|Modele;#anaf|ANAF;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Model cerere · poprire cont · art. 703, 721 CPC',
  h1='Model de cerere pentru ridicarea popririi pe cont bancar <span class="accent">(persoană fizică)</span>',
  lead=['Ai plătit datoria sau vrei să consemnezi suma, dar contul rămâne blocat. Banca spune că ridică poprirea doar la cererea executorului, iar executorul cere acte. Aici ai trei modele gata de completat și instrumentul care îți arată ce ceri și cui.',
        'Modelele se adaptează după dosar și nu înlocuiesc consultanța juridică.'],
  meta2='Se ridică prin executor',cta='Vezi ce ceri',
  answer='Poprirea pe cont o ridică executorul judecătoresc, nu banca: după plata integrală, consemnarea creanței (art. 721 CPC), renunțarea creditorului sau anularea executării (art. 703). Cererea se adresează executorului, cu dovada plății sau recipisa de consemnare. Dacă poprirea este nelegală, depui contestație la instanța de executare, în general în 15 zile (art. 715).',
  opts=[('Cui','executorului'),('Dovadă','plată sau consemnare'),('Dacă e nelegală','contestație, 15 zile')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('ce-este','Ce este',S2),('cand','Când se ridică',S3),('model1','Model: după plată',S4),('model2','Model: consemnare',S5),('model3','Model: contestație',S6),('anaf','ANAF',S7),('greseli','Greșeli',S8),('azi','Ce faci azi',S9)],
 faq=faq,faq_h2='Întrebări frecvente despre ridicarea popririi',
 contact=dict(h2='Ai contul poprit?',lead='Trimite-ne adresa de poprire și dovada plății. Îți spunem în aceeași zi ce cerere depui și cui. Consultația nu te obligă la nimic.',nav='/|Acasă;/poprire-cont/|Poprire cont;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Modelele sunt orientative.'),
 howto=dict(name='Cum ridici poprirea pe cont',steps=[('Plătești sau consemnezi','Toată creanța, cu accesorii și cheltuieli.'),('Depui cererea la executor','Cu dovada plății sau recipisa.'),('Aștepți încheierea','Executorul se pronunță de urgență.'),('Banca este înștiințată','De executor, nu de tine.'),('Verifici contul','Dacă blocajul persistă, contești.')]),
 knows=['Poprire','Ridicare poprire','Executare silită','Model cerere'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/model-cerere-ridicare-poprire-cont-bancar-persoana-fizica.src.html','w',encoding='utf-8').write(build(P))
