import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
C={
 'vrancea':dict(n=43,slug='executari-focsani',key='Vrancea',town='Focșani',judet='Vrancea',jud='Judecătoria Focșani',trib='Tribunalul Vrancea',ca='Curtea de Apel Galați',ex=180000,
   title='Licitații executări silite Vrancea și bunuri executate',h1='Licitații executări silite Vrancea pentru apartamente și case',
   desc='Cum cumperi apartamente, case și bunuri executate în Vrancea prin licitații de executare silită: garanția de 10%, prețul la a doua licitație, termene și riscuri.',loc='Focșani și județul Vrancea',
   lead='Cauți un apartament sau o casă în Focșani sau în Vrancea sub prețul pieței și ai văzut anunțuri de licitație. Prețul mic vine cu reguli stricte și cu riscuri juridice care se verifică înainte să consemnezi garanția.'),
 'giurgiu':dict(n=44,slug='executari-silite-giurgiu',key='Giurgiu',town='Giurgiu',judet='Giurgiu',jud='Judecătoria Giurgiu',trib='Tribunalul Giurgiu',ca='Curtea de Apel București',ex=120000,
   title='Licitații executări silite Giurgiu și imobile executate',h1='Licitații executări silite Giurgiu pentru apartamente și case',
   desc='Cum cumperi apartamente, case și imobile executate silit în Giurgiu: garanția de 10%, prețul la a doua licitație, termene, riscuri și diferența față de licitațiile ANAF.',loc='municipiul Giurgiu și județul Giurgiu',
   lead='Imobilele scoase la licitație în Giurgiu pot fi cumpărate sub valoarea pieței, dar numai dacă știi cum se participă și ce verifici înainte. O ofertă greșită sau o garanție consemnată prea târziu te scoate din cursă.'),
 'prahova':dict(n=45,slug='executari-ploiesti',key='Prahova',town='Ploiești',judet='Prahova',jud='Judecătoria Ploiești',trib='Tribunalul Prahova',ca='Curtea de Apel Ploiești',ex=300000,
   title='Licitații executări silite Prahova și imobile executate',h1='Licitații executări silite Prahova pentru case și apartamente',
   desc='Cum cumperi case, apartamente și imobile executate în Ploiești și Prahova prin licitație: garanția de 10%, prețul la a doua licitație, termene, riscuri și ANAF.',loc='Ploiești și județul Prahova',
   lead='Ploiești și Prahova au un număr mare de anunțuri de licitație imobiliară, iar diferența dintre o achiziție bună și una problematică stă în verificări. Aici vezi regulile din Codul de procedură civilă, pe care le poți aplica oricărui anunț.'),
 'sibiu':dict(n=46,slug='executari-sibiu',key='Sibiu',town='Sibiu',judet='Sibiu',jud='Judecătoria Sibiu',trib='Tribunalul Sibiu',ca='Curtea de Apel Alba Iulia',ex=350000,
   title='Licitații executări silite Sibiu și imobile executate',h1='Licitații executări silite Sibiu pentru case și apartamente',
   desc='Cum cumperi case, apartamente și terenuri executate silit în Sibiu și Mediaș prin licitație: garanția de 10%, prețul la a doua licitație, termene și riscuri.',loc='Sibiu, Mediaș și județul Sibiu',
   lead='La Sibiu și Mediaș, prețurile imobilelor sunt ridicate, iar licitațiile de executare silită par o scurtătură. Pot fi, dacă respecți termenele și verifici situația juridică a imobilului înainte de ofertă.'),
 'bistrita':dict(n=47,slug='executari-bistrita',key='Bistrița',town='Bistrița',judet='Bistrița-Năsăud',jud='Judecătoria Bistrița',trib='Tribunalul Bistrița-Năsăud',ca='Curtea de Apel Cluj',ex=150000,
   title='Licitații executări silite Bistrița și imobile executate',h1='Licitații executări silite Bistrița pentru case și apartamente',
   desc='Cum cumperi case, apartamente și terenuri executate silit în Bistrița-Năsăud prin licitație: garanția de 10%, prețul la a doua licitație, termene și riscuri.',loc='Bistrița și județul Bistrița-Năsăud',
   lead='Anunțurile de licitație din Bistrița-Năsăud promit imobile sub prețul pieței. Câștigi doar dacă înțelegi procedura, termenele și ce se întâmplă cu actele după adjudecare.'),
}
def build_for(k):
    d=C[k]; ci=d['key']; sl=d['slug']
    IMa=f'licitatie-imobiliara-{k}-pasii'; IMb=f'pretul-la-licitatia-imobiliara-{k}'
    IM={
     IMa:(f'{ci} · licitație imobiliară','Cum participi la licitație',
      steps([('Publicația','20–40 de zile','Termenul pentru vânzare, de la afișare (art. 838)'),('Garanția','10%','Din prețul de începere, consemnată la dispoziția executorului (art. 844)'),('Oferta','Cu dovada garanției','Cel târziu în ziua dinaintea licitației (art. 844)'),('Licitația','3 strigări','Se citesc publicația și ofertele (art. 846)'),('Prețul','30 de zile','Se depune la executor de la adjudecare (art. 850)')],
      'Actul de adjudecare îți servește ca <b>titlu de proprietate</b> (art. 855); intabularea se cere de executor (art. 856).'),
      'Cod procedură civilă, art. 838–856. Orientativ.',f'Cum participi la o licitație imobiliară în {ci}: publicație, garanție de 10%, ofertă, licitație, plata prețului în 30 de zile','Cum participi la licitație'),
     IMb:('Art. 843–846','Prețul pe termene',
      cards([('Primul termen','100%','Prețul de începere din publicație; garanția este 10% din el',True),('Al doilea termen','75%','Licitația începe de la 75% din prețul primei licitații (art. 846 alin. 8)',False),('Preț minim','30%','Cu cel puțin 2 licitatori, la același termen, nu mai puțin de 30% din prețul primei licitații',False)],3)+'<div class="card dark" style="margin-top:18px"><div class="s" style="font-size:17px;margin:0">Creditorii urmăritori sau intervenienți nu pot adjudeca sub <b>75%</b> din prețul de pornire al primei licitații (art. 843 alin. 5).</div></div>',
      'Cod procedură civilă, art. 843, 846. Orientativ.','Prețul la licitația imobiliară pe termene: 100% la primul termen, 75% la al doilea, minimum 30% cu cel puțin doi licitatori','Prețul pe termene'),
    }
    def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
    ex=d['ex']
    calc,js=calcs.select.__wrapped__(ex) if False else (None,None)
    fields='''          <div class="grp">Anunțul de licitație</div>
          <div class="field full"><label for="f-v">Prețul de începere din publicație (lei)</label><div class="inp"><input id="f-v" inputmode="numeric" placeholder="%d"></div></div>'''%ex
    outs='''            <div class="opt full" id="c-t"><span class="k">Garanție de participare (10%)</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Introdu prețul de începere.</span></div>
            <div class="opt" id="c-m"><span class="k">Al doilea termen (75%)</span><span class="v" id="o-m">—</span><span class="s" id="o-ms">Prețul de la care începe licitația (art. 846 alin. 8).</span></div>
            <div class="opt" id="c-r"><span class="k">Preț minim cu 2+ licitatori (30%)</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Nu mai puțin de 30% din prețul primei licitații.</span></div>'''
    calc=calcs._shell(f'Garanția și prețul pe termene, <span class="accent">pentru un imobil din {ci}</span>','Introdu prețul de începere din publicația de vânzare. Calculăm garanția de participare, prețul de la care începe al doilea termen și pragul minim, după art. 844 și art. 846 CPC.',fields,'Exemplu: preț de începere %s lei'%f'{ex:,}'.replace(',','.'),outs,'Calcul orientativ după CPC. Prețurile din exemple sunt ilustrative, nu date de piață. Verifică în publicație prețul exact, termenul și condițiile; cele 75% și 30% se aplică la termenele următoare, în condițiile art. 846 alin. 8.')
    js=r'''  function lei(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/[\s.]/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function calc(){
    var p=num('f-v');
    if(!(p>0)){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Introdu prețul de începere.';$('o-m').textContent='—';$('o-r').textContent='—';return}
    $('o-t').textContent=lei(p*0.1);cls('c-t','alert');$('o-ts').textContent='Se consemnează la dispoziția executorului și se anexează ofertei (art. 844).';
    $('o-m').textContent=lei(p*0.75);$('o-r').textContent=lei(p*0.3);
  }
  $('b-calc').addEventListener('click',calc);
  $('f-v').addEventListener('input',calc);$('f-v').addEventListener('change',calc);
  function ex(){$('f-v').value='%d';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''%ex
    g,s75,s30=ex//10,int(ex*0.75),int(ex*0.3)
    fm=lambda x:f'{x:,}'.replace(',','.')
    S1=f'''        <span class="eyebrow">Pe scurt</span>
        <h2>Licitații executări silite {ci}: răspuns rapid</h2>
        <p>Licitația de executare silită este vânzarea publică a unui bun urmărit, făcută de executorul judecătoresc pentru plata creditorilor. Pentru un imobil din {d['loc']}, participi cu o ofertă însoțită de garanția de 10% din prețul de începere, depusă cel mai târziu în ziua dinaintea licitației (art. 844 CPC). Termenul de vânzare este între 20 și 40 de zile de la afișarea publicației (art. 838). La adjudecare ai 30 de zile să depui prețul (art. 850).</p>
        <div class="example">
          <div class="t">Cifră pe șervețel (exemplu ilustrativ)</div>
          <p>Prețul de începere din publicație este {fm(ex)} lei. Garanția este 10%: {fm(g)} lei. Dacă nu se oferă nici acest preț, licitația se amână cel mult 30 de zile și începe de la 75%: {fm(s75)} lei. La același al doilea termen, cu cel puțin 2 licitatori, imobilul se poate vinde și la cel mai mare preț oferit, dar nu sub 30% din prețul primei licitații: {fm(s30)} lei (art. 846 alin. 8).</p>
          <span class="formula">{fm(ex)} × 10% = {fm(g)} lei garanție</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>
        <p>Prețurile și imobilele concrete din {ci} se văd în publicațiile executorilor; aici ai regulile care se aplică oricărui anunț.</p>'''
    S2=f'''        <span class="eyebrow">Definiție</span>
        <h2>Ce înseamnă executarea silită a bunurilor</h2>
        <p>Executarea silită este recuperarea unei datorii prin executor judecătoresc, pe baza unui titlu executoriu (art. 632 CPC). Când debitorul nu plătește, executorul poate urmări imobilul: notează urmărirea în cartea funciară, fixează prețul de începere prin încheiere (art. 837) și îl vinde la licitație. Procedura generală este în ghidul <a href="/procedura-executare-silita-etape/">procedura executării silite</a>.</p>
        <h3>Cine organizează licitațiile</h3>
        <p>Licitația imobiliară o ține executorul judecătoresc, în baza unui titlu executoriu: o poate cere o bancă, un recuperator (cesionar), un alt creditor sau statul. Creanțele către buget se execută prin organele fiscale, după Codul de procedură fiscală, cu proceduri proprii; citește anunțul fiecărei vânzări, pentru că regulile de participare pot diferi.</p>
        <h3>Instanțele din zonă</h3>
        <p>Pentru {d['loc']}, instanțele relevante sunt {d['jud']}, {d['trib']} și {d['ca']}. Contestațiile la executare se depun, de regulă, la instanța de executare, adică judecătoria domiciliului sau sediului debitorului (art. 651 CPC); pentru urmărirea imobilelor, contestația se poate depune și la judecătoria de la locul imobilului, dacă acesta se află în circumscripția altei curți de apel (art. 714 alin. 2). Verifică denumirile și competența pe portalul instanțelor înainte de orice depunere.</p>'''
    S3=f'''        <span class="eyebrow">Tipuri de bunuri</span>
        <h2>Ce poți cumpăra la o licitație de executare silită</h2>
        <div class="tbl wide"><table>
          <thead><tr><th></th><th>Apartamente</th><th>Case și vile</th><th>Terenuri</th></tr></thead>
          <tbody>
            <tr><td>Avantaj</td><td>Preț de pornire fixat prin încheiere</td><td>Preț de pornire fixat prin încheiere</td><td>Preț de pornire fixat prin încheiere</td></tr>
            <tr><td>Verifici</td><td>Cartea funciară, sarcinile, locatarii</td><td>Cartea funciară, construcții intabulate, vecinătăți</td><td>Intravilan sau extravilan, acces, servituți</td></tr>
            <tr><td>Documente</td><td>Act de identitate, garanție, ofertă</td><td>La fel</td><td>La fel</td></tr>
            <tr><td>Costuri în plus</td><td>Notarea în cartea funciară, pe cheltuiala adjudecatarului (art. 849, 856)</td><td>La fel</td><td>La fel</td></tr>
          </tbody>
        </table></div>
        <p>Bunurile mobile (mașini, echipamente) se vând după regulile urmăririi mobiliare; vezi <a href="/procedura-executare-silita-etape/">etapele executării</a> și art. 727 pentru bunurile neurmăribile. Prețul mediu nu poate fi dat pe baza legii: el depinde de evaluarea din dosar și de anunț.</p>'''
    S4=f'''        <span class="eyebrow">Procedura</span>
        <h2>Cum participi la o licitație de executare silită, pas cu pas</h2>
        <ol class="num">
          <li><b>Citește publicația</b> de vânzare: imobilul, numărul cadastral, prețul de începere, locul și ora (art. 839).</li>
          <li><b>Verifică imobilul</b> în cartea funciară și în dosarul de executare.</li>
          <li><b>Consemnează garanția</b> de 10% din prețul de începere la dispoziția executorului (art. 844 alin. 1).</li>
          <li><b>Depune oferta</b> cu dovada consemnării, cel târziu în ziua dinaintea licitației; ofertele cel puțin egale cu prețul de începere pot fi depuse și în ziua licitației.</li>
          <li><b>La licitație,</b> executorul citește publicația și ofertele, apoi oferă imobilul prin 3 strigări succesive (art. 846).</li>
          <li><b>Dacă adjudeci,</b> depui prețul în cel mult 30 de zile, ținând seama de garanție (art. 850); debitorul nu poate licita, nici prin persoane interpuse (art. 843 alin. 2).</li>
        </ol>
'''+F(IMa)
    S5=f'''        <span class="eyebrow">Prețul</span>
        <h2>Prețul la licitație: primul și al doilea termen</h2>
'''+F(IMb)+f'''
        <p>Prețul „sub piață” nu este garantat. Dacă la primul termen nu se oferă prețul de începere, vânzarea se amână cel mult 30 de zile, cu nouă publicație, iar la al doilea termen licitația începe de la 75% din prețul primei licitații. Dacă nici atunci nu se obține prețul de începere și sunt cel puțin 2 licitatori, bunul se vinde la cel mai mare preț oferit, dar nu mai puțin de 30% din prețul primei licitații (art. 846 alin. 8). O vânzare se amână, de asemenea, dacă nu au fost respectate termenele de înștiințare sau de publicitate (art. 845).</p>'''
    S6=f'''        <span class="eyebrow">Riscuri</span>
        <h2>Riscurile licitațiilor de executare silită</h2>
        <ul class="chk">
          <li><b>Contestația:</b> procesul-verbal de licitație poate fi atacat prin contestație la executare, în termen de o lună de la înscrierea adjudecării în cartea funciară (art. 849 alin. 2); instanța poate suspenda eliberarea sumelor.</li>
          <li><b>Nedepunerea prețului:</b> imobilul se scoate din nou în vânzare pe contul tău, iar tu plătești cheltuielile și eventuala diferență de preț (art. 851).</li>
          <li><b>Sarcini și drepturi:</b> drepturile înscrise în cartea funciară după notarea urmăririi nu se opun adjudecatarului (art. 827); verifică restul.</li>
          <li><b>Locatari:</b> adjudecatarul nu este ținut să respecte o locațiune încheiată la un preț cu o treime sub piață (art. 828).</li>
          <li><b>Evaluarea:</b> un preț de pornire mic poate ascunde o problemă juridică sau tehnică.</li>
        </ul>
        <p>Vezi și <a href="/contestatie-la-executare/">contestația la executare</a> și <a href="/executare-silita-fara-somatie/">executarea fără somație</a>.</p>'''
    S7='''        <span class="eyebrow">Banci și ANAF</span>
        <h2>Licitațiile bancare și cele ale ANAF</h2>
        <p>Licitațiile cerute de bănci se desfășoară tot prin executor judecătoresc, după CPC, ca orice executare imobiliară. Creanțele fiscale se execută prin organele fiscale, după Codul de procedură fiscală; anunțurile lor pot avea condiții și termene proprii, pe care le citești în publicația fiecărei vânzări. Regula practică: cere publicația oficială, verifică titlul executoriu și imobilul, apoi consemnează garanția.</p>'''
    S8='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente ale participanților</h2>
        <ul class="chk">
          <li>Nu verifici cartea funciară și sarcinile.</li>
          <li>Consemnezi garanția după termenul-limită pentru ofertă.</li>
          <li>Nu ai banii pentru preț în 30 de zile.</li>
          <li>Te bazezi pe „prețul de piață” fără evaluare.</li>
        </ul>
        <p>Textele din CPC sunt cele publicate în Monitorul Oficial; verifică forma consolidată la data licitației.</p>'''
    S9='''        <span class="eyebrow">Ce faci acum</span>
        <h2>Cum cumperi avantajos și sigur</h2>
        <ol class="num">
          <li>Cere publicația oficială și dosarul imobilului.</li>
          <li>Verifică cartea funciară și calculează garanția (calculator).</li>
          <li>Trimite-ne publicația în chat; îți spunem în aceeași zi ce verificări lipsesc.</li>
        </ol>
        <!--@author practice="executare silită" -->'''
    faq=[("Ce sunt licitațiile de executare silită?","Vânzări publice ale bunurilor urmărite, ținute de executorul judecătoresc pentru plata creditorilor, după regulile CPC."),
    ("Cum pot participa la o licitație imobiliară?","Consemnezi garanția de 10% din prețul de începere, depui oferta cu dovada consemnării și te prezinți la licitație (art. 844, 846 CPC)."),
    ("Ce documente sunt necesare pentru participare?","Actul de identitate, dovada consemnării garanției, oferta de cumpărare și, dacă ești mandatar, procura specială autentică (art. 843, 844)."),
    ("Pot cumpăra un apartament executat silit?","Da, dacă ai capacitate deplină de exercițiu; debitorul însuși nu poate licita, nici prin persoane interpuse (art. 843)."),
    ("Care sunt riscurile unei licitații?","Contestația la executare, sarcinile imobilului, nedepunerea prețului în 30 de zile (art. 851) și o evaluare greșită."),
    ("Cum verific actele unui imobil executat?","Din cartea funciară, publicația de vânzare și dosarul de executare, la executor."),
    ("Ce este garanția de participare?","10% din prețul de începere a licitației, consemnată la dispoziția executorului și anexată ofertei (art. 844)."),
    ("Pot fi contestate licitațiile de executare?","Da, procesul-verbal de licitație poate fi atacat în termen de o lună de la înscrierea adjudecării în cartea funciară (art. 849).")]
    P=dict(slug=sl,crumb=f'Licitații executări silite {ci}',title=d['title'],desc=d['desc'],
     nav='#calculator|Calculator;#raspuns|Răspuns rapid;#bunuri|Bunuri;#participare|Cum participi;#riscuri|Riscuri;#intrebari|Întrebări',
     images=[k2+'.webp' for k2 in IM],
     hero=dict(eyebrow=f'{ci} · licitații imobiliare · garanție 10%',h1=f'{d["h1"][:-0] if False else d["h1"].replace(ci,"<span class=\"accent\">"+ci+"</span>",1)}',
      lead=[d['lead'],'Aici ai pașii, garanția, prețul pe termene, riscurile și instanțele relevante, cu un calculator pentru orice anunț de licitație.'],
      meta2='Garanție: 10% din prețul de începere',cta='Calculează garanția',
      answer=f'Licitația de executare silită este vânzarea publică a unui bun urmărit, făcută de executorul judecătoresc. Pentru un imobil, participi cu o ofertă însoțită de garanția de 10% din prețul de începere (art. 844 CPC), depusă cel mult în ziua dinaintea licitației. Termenul de vânzare este între 20 și 40 de zile de la publicație (art. 838), iar prețul se depune în 30 de zile de la adjudecare (art. 850).',
      opts=[('Garanție','10% din prețul de începere'),('Al doilea termen','de la 75%'),('Preț','în 30 de zile')]),
     calc_html=calc,js=js,
     sections=[('raspuns','Răspuns rapid',S1),('ce-este','Executarea bunurilor',S2),('bunuri','Bunuri',S3),('participare','Cum participi',S4),('pret','Prețul',S5),('riscuri','Riscuri',S6),('banci','Bănci și ANAF',S7),('greseli','Greșeli',S8),('azi','Ce faci azi',S9)],
     faq=faq,faq_h2='Întrebări frecvente despre licitațiile de executare silită',
     contact=dict(h2=f'Vrei să cumperi un imobil la licitație în {ci}?',lead='Trimite-ne publicația de vânzare și numărul dosarului de executare. Îți spunem în aceeași zi ce verificări lipsesc și ce termene curg. Consultația nu te obligă la nimic.',nav='/|Acasă;/procedura-executare-silita-etape/|Procedura;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat executorilor sau băncilor. Calculele și exemplele sunt orientative.'),
     howto=dict(name=f'Cum participi la o licitație imobiliară în {ci}',steps=[('Citești publicația','Imobil, preț de începere, loc și oră.'),('Verifici imobilul','Carte funciară și dosar de executare.'),('Consemnezi garanția','10% din prețul de începere.'),('Depui oferta','Cu dovada consemnării, până în ziua dinaintea licitației.'),('Plătești prețul','În cel mult 30 de zile de la adjudecare.')]),
     knows=['Executare silită','Licitație imobiliară','Garanție de participare',ci])
    return P,IM
