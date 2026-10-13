import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from mk import *
import calcs
from igx import steps,cards,table
IM={
 'cererea-debitorului-sau-a-creditorului':('Legea 85/2014','Cererea debitorului sau a creditorului',
   table(['','Cererea debitorului','Cererea creditorului'],[['Temei','Art. 66','Art. 70'],['Termen','Obligație: maximum 30 de zile de la insolvență','Facultativ; creanță peste valoarea-prag de 40.000 lei (art. 5 pct. 72)'],['Acte','Situații financiare, bunuri, creditori (art. 67)','Dovada creanței și CUI-ul debitorului (art. 70 alin. 2)'],['Garanție','Nu','Cauțiune de până la 10%, maximum 40.000 lei, dacă cere debitorul (art. 72)']]),
   'Legea nr. 85/2014. Orientativ; verifică forma consolidată.','Cererea debitorului și cererea creditorului: temei, termen, acte și cauțiune în deschiderea procedurii de insolvență','Cererea debitorului sau a creditorului'),
 'pasii-deschiderii-procedurii':('Legea 85/2014 · art. 71–75','Deschiderea procedurii, pas cu pas',
   steps([('Cererea','La tribunal','Debitor (art. 66) sau creditor (art. 70)'),('Debitorul','10 zile','Contestă sau recunoaște insolvența (art. 72 alin. 3)'),('Încheierea','Judecătorul-sindic','Procedură generală sau simplificată (art. 71)'),('Opoziții','10 zile + 5 zile','Opoziție la notificare; ședința în 5 zile (art. 71 alin. 2)'),('Efecte','Suspendare','Executările individuale, de drept (art. 75)')],
   'La cererea creditorului, instanța comunică cererea debitorului și organului fiscal în <b>48 de ore</b> (art. 72 alin. 2).'),
   'Legea nr. 85/2014. Orientativ.','Deschiderea procedurii de insolvență: cerere, 10 zile pentru debitor, încheiere, opoziții, suspendarea executărilor','Deschiderea procedurii, pas cu pas'),
}
def F(n): ey,t,b,f,alt,cap=IM[n]; return fig(n+'.webp',alt,cap)
fields='''          <div class="grp">Creanța ta</div>
          <div class="field"><label for="f-v">Valoarea creanței (lei)</label><div class="inp"><input id="f-v" inputmode="numeric" placeholder="120000"></div></div>
          <div class="field"><label for="f-d">Zile de la scadență, fără plată</label><div class="inp"><input id="f-d" inputmode="numeric" placeholder="75"></div></div>'''
outs='''            <div class="opt full" id="c-t"><span class="k">Poți cere deschiderea procedurii?</span><span class="v" id="o-t" style="font-size:19px">—</span><span class="s" id="o-ts">Introdu valoarea și zilele.</span></div>
            <div class="opt" id="c-m"><span class="k">Cauțiune maximă, dacă ți se cere</span><span class="v" id="o-m">—</span><span class="s" id="o-ms">Până la 10%, maximum 40.000 lei (art. 72).</span></div>
            <div class="opt" id="c-r"><span class="k">Prezumția de insolvență</span><span class="v" id="o-r" style="font-size:19px">—</span><span class="s" id="o-rs">După 60 de zile de la scadență (art. 5 pct. 29).</span></div>'''
calc=calcs._shell('Poți cere tu <span class="accent">deschiderea procedurii?</span>','Ca creditor, introdu valoarea creanței și zilele de la scadență. Verificăm valoarea-prag de 40.000 lei (art. 5 pct. 72), prezumția de insolvență după 60 de zile și cauțiunea posibilă (art. 72 din Legea nr. 85/2014).',fields,'Exemplu: creanță de 120.000 lei, 75 de zile',outs,'Calcul orientativ pentru creanțe de altă natură decât cele salariale; pentru salariați valoarea-prag este de 6 salarii medii brute (art. 5 pct. 72). Insolvența se prezumă după 60 de zile de la scadență, prezumție relativă; judecătorul-sindic verifică în fond starea de insolvență.')
js=r'''  function lei(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' lei'}
  function num(id){var v=($(id).value||'').replace(/[\s.]/g,'').replace(',','.');return v===''?null:parseFloat(v)}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function calc(){
    var v=num('f-v'),z=num('f-d');
    if(!(v>0)){$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Introdu valoarea și zilele.';$('o-m').textContent='—';$('o-r').textContent='—';return}
    var ok=v>=40000;
    $('o-t').textContent=ok?'Da, creanța depășește valoarea-prag':'Nu, sub valoarea-prag de 40.000 lei';cls('c-t',ok?'ok':'alert');
    $('o-ts').textContent=ok?'Valoarea-prag este de 40.000 lei pentru creanțe de altă natură decât cele salariale (art. 5 pct. 72).':'Cererea de deschidere nu poate fi introdusă pentru o creanță sub valoarea-prag.';
    $('o-m').textContent=lei(Math.min(0.1*v,40000));
    if(z>=0&&z!==null){var p=z>60;$('o-r').textContent=p?'Se prezumă':'Încă nu';cls('c-r',p?'ok':'alert');$('o-rs').textContent=p?'Au trecut peste 60 de zile de la scadență: prezumție relativă (art. 5 pct. 29).':'Mai trebuie '+(61-z)+' zile până la prezumție.'}
    else{$('o-r').textContent='—'}
  }
  $('b-calc').addEventListener('click',calc);
  ['f-v','f-d'].forEach(function(id){$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)});
  function ex(){$('f-v').value='120000';$('f-d').value='75';calc()}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){b.addEventListener('click',function(){ex();$('calculator').scrollIntoView({behavior:'smooth'})})});'''
S1='''        <span class="eyebrow">Pe scurt</span>
        <h2>Deschiderea procedurii insolvenței: răspuns rapid</h2>
        <p>Procedura se deschide prin încheierea judecătorului-sindic de la tribunal, la cererea debitorului (obligatorie în 30 de zile de la apariția insolvenței, art. 66) sau a unui creditor a cărui creanță depășește valoarea-prag de 40.000 lei (art. 70 și art. 5 pct. 72). De la deschidere, executările silite și acțiunile pentru realizarea creanțelor asupra averii debitorului se suspendă de drept (art. 75), iar creditorii își valorifică drepturile prin cereri de admitere.</p>
        <div class="example">
          <div class="t">Cifră pe șervețel</div>
          <p>Un furnizor are o creanță de 120.000 lei, neplătită de 75 de zile. Peste valoarea-prag de 40.000 lei și peste 60 de zile de la scadență, insolvența se prezumă (art. 5 pct. 29). Dacă debitorul cere, judecătorul-sindic poate impune o cauțiune de până la 10% din creanță, dar nu mai mult de 40.000 lei: aici, 10% = 12.000 lei, consemnată în 5 zile (art. 72).</p>
          <span class="formula">min(10% × 120.000; 40.000) = 12.000 lei</span>
          <button type="button" class="btn btn-line" data-ex="1">Verifică în calculator</button>
        </div>'''
S2='''        <span class="eyebrow">Cine cere</span>
        <h2>Cine poate cere deschiderea procedurii</h2>
'''+F('cererea-debitorului-sau-a-creditorului')+'''
        <h3>Cererea debitorului</h3>
        <p>Debitorul în stare de insolvență trebuie să ceară deschiderea procedurii în maximum 30 de zile de la apariția insolvenței, cu dovada notificării organului fiscal (art. 66 alin. 1). Dacă insolvența este doar iminentă, poate cere, dar nu este obligat (art. 66 alin. 4). Detalii: <a href="/insolventa-voluntara/">insolvența voluntară</a>.</p>
        <h3>Cererea creditorului</h3>
        <p>Creditorul precizează cuantumul și temeiul creanței, eventualul drept de preferință și intenția de a participa la reorganizare și anexează documentele justificative și dovada codului unic de înregistrare al debitorului (art. 70). Dacă mai mulți creditori depun cereri, ele se înregistrează în același dosar (art. 70 alin. 3–4).</p>'''
S3='''        <span class="eyebrow">Condiții</span>
        <h2>Condițiile pentru deschiderea procedurii</h2>
        <ul class="chk">
          <li><b>Starea de insolvență:</b> fonduri insuficiente pentru datorii certe, lichide și exigibile; prezumție după 60 de zile de la scadență, relativă (art. 5 pct. 29).</li>
          <li><b>Valoarea-prag:</b> 40.000 lei pentru creditori și debitor, pentru creanțe de altă natură decât cele salariale; la salariați, 6 salarii medii brute (art. 5 pct. 72).</li>
          <li><b>Actele:</b> la cererea debitorului, cele din art. 67 (situații financiare, lista bunurilor și a creditorilor, plăți din ultimele 6 luni, declarații); la cererea creditorului, dovada creanței și CUI-ul debitorului.</li>
          <li><b>Instanța:</b> tribunalul; judecătorul-sindic.</li>
        </ul>'''
S4='''        <span class="eyebrow">Procedura</span>
        <h2>Procedura deschiderii, pas cu pas</h2>
'''+F('pasii-deschiderii-procedurii')+'''
        <ol class="num">
          <li><b>Cererea</b> se depune la tribunal.</li>
          <li><b>La cererea creditorului,</b> instanța o comunică debitorului și organului fiscal în 48 de ore; debitorul are 10 zile să conteste sau să recunoască insolvența, cu probă doar prin înscrisuri (art. 72 alin. 2–3).</li>
          <li><b>Cauțiunea:</b> la cererea debitorului, judecătorul-sindic poate cere creditorului până la 10% din creanță, maximum 40.000 lei, în 5 zile, sub sancțiunea respingerii (art. 72 alin. 1).</li>
          <li><b>Încheierea de deschidere:</b> procedură generală sau simplificată (art. 71).</li>
          <li><b>Notificări și opoziții:</b> creditorii se pot opune în 10 zile de la notificare; judecătorul ține o ședință în 5 zile (art. 71 alin. 2).</li>
        </ol>'''
S5='''        <span class="eyebrow">Efecte</span>
        <h2>Efectele deschiderii procedurii</h2>
        <ul class="chk">
          <li><b>Suspendarea executărilor</b> și a acțiunilor individuale, de drept (art. 75); hotărârea de deschidere se comunică instanțelor și băncilor (art. 76).</li>
          <li><b>Administrator judiciar provizoriu</b> sau lichidator, numit prin sentința de deschidere (art. 73).</li>
          <li><b>Actele debitorului:</b> în 10 zile de la deschidere depune în dosar actele din art. 67 alin. 1 (art. 74).</li>
          <li><b>Utilitățile:</b> furnizorii nu pot întrerupe serviciile către consumatorul captiv în observație și reorganizare; plata se face în 90 de zile (art. 77).</li>
          <li><b>Creditorii cu garanții</b> pot cere ridicarea suspendării în condițiile art. 78.</li>
        </ul>'''
S6='''        <span class="eyebrow">După deschidere</span>
        <h2>Creditorii, reorganizarea și falimentul</h2>
        <p>Creditorii își depun cererile de admitere (art. 104), apar în tabele și votează planul. Dacă se propune un plan de reorganizare și este acceptat și confirmat, activitatea continuă sub supraveghere, cel mult 3 ani (art. 133 alin. 3); altfel, se ajunge la faliment (art. 145). Vezi <a href="/plan-reorganizare-insolventa/">planul de reorganizare</a> și <a href="/insolventa-sau-faliment/">insolvență sau faliment</a>.</p>'''
S7='''        <span class="eyebrow">Greșeli</span>
        <h2>Greșeli frecvente și ce faci acum</h2>
        <ul class="chk">
          <li>Depui cererea de creditor sub valoarea-prag (se respinge).</li>
          <li>Debitorul depune cererea după termenul de 30 de zile.</li>
          <li>Lipsesc documentele justificative sau CUI-ul debitorului.</li>
          <li>Debitorul nu conteste în 10 zile o cerere nefondată.</li>
        </ul>
        <ol class="num">
          <li>Verifică valoarea-prag și zilele de la scadență (calculator).</li>
          <li>Strânge actele creanței sau situația financiară, după caz.</li>
          <li>Trimite-ne datele în chat; îți spunem în aceeași zi dacă poți depune cererea.</li>
        </ol>
        <p>Textele din Legea nr. 85/2014 sunt cele publicate în Monitorul Oficial; verifică forma consolidată.</p>
        <!--@author practice="insolvență" -->'''
faq=[("Cine poate cere deschiderea procedurii insolvenței?","Debitorul (art. 66) sau un creditor îndreptățit, cu creanță peste valoarea-prag (art. 70)."),
("Ce condiții trebuie îndeplinite?","Stare de insolvență (prezumată după 60 de zile de la scadență) și, pentru creditor, o creanță de cel puțin 40.000 lei (art. 5 pct. 29 și 72)."),
("Ce efecte are deschiderea procedurii?","Executările se suspendă de drept (art. 75), se numește un administrator judiciar sau lichidator (art. 73) și creditorii își depun cererile de admitere."),
("Se suspendă executările silite?","Da, toate acțiunile și măsurile de executare pentru realizarea creanțelor asupra averii debitorului, de la data deschiderii (art. 75)."),
("Ce este masa credală?","Totalitatea creditorilor ale căror creanțe sunt admise în tabelul creanțelor, care se plătesc în cadrul procedurii."),
("Cât durează procedura insolvenței?","Nu există o durată fixă; planul de reorganizare nu poate depăși 3 ani de la confirmare (art. 133 alin. 3)."),
("Ce rol are administratorul judiciar?","Este desemnat prin sentința de deschidere (art. 73) și supraveghează averea și, dacă e cazul, planul."),
("Poate creditorul deschide insolvența firmei?","Da, dacă are o creanță peste valoarea-prag, iar insolvența se dovedește; debitorul poate contesta în 10 zile, iar judecătorul-sindic poate cere o cauțiune (art. 72).")]
P=dict(slug='deschiderea-procedurii-insolventei',crumb='Deschiderea procedurii insolvenței',
 title='Deschiderea procedurii insolvenței: cerere, condiții, efecte',
 desc='Cum se deschide procedura insolvenței: cererea debitorului sau a creditorului, valoarea-prag de 40.000 lei, cauțiunea, pașii la tribunal și efectele (suspendarea executărilor).',
 nav='#calculator|Calculator;#raspuns|Răspuns rapid;#cine|Cine cere;#procedura|Procedura;#efecte|Efecte;#intrebari|Întrebări',
 images=[k+'.webp' for k in IM],
 hero=dict(eyebrow='Legea 85/2014 · art. 66–76 · valoarea-prag 40.000 lei',
  h1='Deschiderea procedurii insolvenței: <span class="accent">cine cere, condiții și efecte</span>',
  lead=['Un client nu plătește sau firma ta nu mai poate plăti, și întrebarea este cine poate deschide procedura, ce condiții contează și ce se schimbă imediat după încheiere.',
        'Aici ai pașii la tribunal, valoarea-prag, cauțiunea posibilă și efectele deschiderii, cu un instrument care îți spune dacă, ca și creditor, poți depune cererea.'],
  meta2='Prag: 40.000 lei',cta='Verifică-ți creanța',
  answer='Procedura se deschide prin încheierea judecătorului-sindic de la tribunal, la cererea debitorului (obligatorie în 30 de zile de la insolvență, art. 66) sau a unui creditor cu creanță peste valoarea-prag de 40.000 lei (art. 70, art. 5 pct. 72). De la deschidere, executările individuale se suspendă de drept (art. 75), iar creditorii își depun cererile de admitere.',
  opts=[('Debitor','30 de zile (art. 66)'),('Creditor','prag 40.000 lei'),('Efect','executări suspendate')]),
 calc_html=calc,js=js,
 sections=[('raspuns','Răspuns rapid',S1),('cine','Cine cere',S2),('conditii','Condiții',S3),('procedura','Procedura',S4),('efecte','Efecte',S5),('dupa','După deschidere',S6),('greseli','Greșeli și pași',S7)],
 faq=faq,faq_h2='Întrebări frecvente despre deschiderea procedurii insolvenței',
 contact=dict(h2='Vrei să deschizi sau să eviți o insolvență?',lead='Trimite-ne creanța sau situația financiară a firmei. Îți spunem în aceeași zi ce condiții sunt îndeplinite și ce termene curg. Consultația nu te obligă la nimic.',nav='/|Acasă;/insolventa-voluntara/|Insolvența voluntară;#intrebari|Întrebări;#contact|Contact',note='Consultarius nu este afiliat tribunalelor sau administratorilor judiciari. Informațiile sunt orientative.'),
 howto=dict(name='Cum se deschide procedura insolvenței',steps=[('Verifici condițiile','Insolvență și valoarea-prag de 40.000 lei pentru creditor.'),('Depui cererea','La tribunal, cu actele din art. 67 sau art. 70.'),('Debitorul răspunde','În 10 zile, la cererea creditorului.'),('Încheierea de deschidere','Procedură generală sau simplificată.'),('Notificări și opoziții','10 zile pentru opoziții, ședință în 5 zile.')]),
 knows=['Insolvență','Deschiderea procedurii','Legea 85/2014','Valoarea-prag'])
if __name__=='__main__':
    open('/home/user/work/chinsolvency/deschiderea-procedurii-insolventei.src.html','w',encoding='utf-8').write(build(P))
