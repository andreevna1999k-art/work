import sys,os,re,importlib; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import mkdoc
A={ # page: (№, arts verified, unverified, notes)
'26':(26,'CPC art. 632–634, 664, 666, 670, 697, 706–709, 729, 731, 781, 787, 864, 1013; Legea 85/2014 art. 75','Cod civil (prescripția dreptului la acțiune 3 ani, cesiunea) — fără numere de articole, de verificat. Onorariile: fără cifre (neinventate). Sărăcie de «cazuri reale» din ТЗ: nu s-au inventat.','Таблица «avocat vs firmă» — общая, без цен. Кросс-ссылки: /lege-recuperare-creante/, /procedura-executare-silita-etape/.'),
'28':(28,'CPC art. 632, 647, 651, 663, 666–668, 670, 679, 697, 701, 704, 706–707, 712–715, 717, 719–721, 727, 729, 781–783','Названия 6 judecătorii de sector (Judecătoria Sectorului 1–6) и принцип competenței по домициliu: art. 651 CPC; список секторов не сверялся с реестром инстанций. OUG 80/2013 (taxa până la 1.000 lei) — сверить.','Нет «cazuri reale» (не выдумывались). «Sanse: procente» из ТЗ — не даны, нельзя гарантировать.'),
'38':(38,'Legea 85/2014 art. 5 pct. 29, 38 alin. 2, 66, 67, 69, 71, 73, 74, 75, 77, 133 alin. 2–3','Legea 151/2015 (persoane fizice) упомянута без деталей. «Pragul valoric» из ТЗ — см. №51 (40.000 lei). Judecătorul-sindic/administrator — общее описание.','Страница про cererea debitorului (art. 66), не дублирует №51 (deschiderea, creditor).'),
'41':(41,'CPC art. 701, 703, 712–715, 719–721, 729, 781, 784','Poprirea ANAF: процедура описана обобщённо (Codul de procedură fiscală), без номеров статей и сроков — сверить. Модели cererilor — ориентировочные, должен просмотреть юрист.','Slug: model-cerere-ridicare-poprire-cont-bancar-persoana-fizica (по плану Конвеєр).'),
'42':(42,'CPC art. 647, 697–699, 700, 706–709, 712, 715, 720','Раздел «comparatie cu Codul din 1865» и «decizii CCR» из ТЗ не включены (нет проверенного источника). Culpa creditorului оценивается инстанцией.','Дата-пример: 15.04.2026 + 6 luni = 15.10.2026.'),
'48':(48,'CPC art. 666, 670, 697, 706–709, 787, 1013; формула DSO = creanțe ÷ vânzări × zile (финансовый показатель, не норма закона)','«Durata optimă» — без цифр: порога в законе нет. Раздел «solutii moderne / softuri» из ТЗ не раскрыт (нет проверенных данных).','Калькулятор DSO: пример 120.000 ÷ 600.000 × 365 = 73 дня.'),
'49':(49,'CPC art. 663, 667–669, 674, 675, 679, 704, 715, 719–720, 729, 782–783','Исключения «obligații de predare / evacuare» и «măsuri urgente ale instanței» из ТЗ не включены (нет проверенного текста). Executare fiscală (ANAF) — только отсылка.','Исключения из somație: poprire (783), art. 669 pct. 1–2.'),
'50':(50,'Legea 85/2014 art. 3, 5 pct. 29 и 42, 38, 66, 67, 70–78, 100, 104, 132, 133, 139, 145, 154, 159','Legea 151/2015 (persoane fizice): только то, что закон существует и подаётся в judecătorie (art. 10); praguri/condiții/protecția locuinței НЕ описаны — сверить. Jurisprudență/cazuri reale не добавлялись.','Overview-страница; детали вынесены на №38, 51, 52, 53, 57.'),
'51':(51,'Legea 85/2014 art. 5 pct. 29 и 72 (valoarea-prag 40.000 lei), 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 104, 133 alin. 3, 145','Praguri для salariați (6 salarii medii brute) — как в тексте закона, суммы не пересчитывались. Jurisprudență не добавлялась.','Калькулятор: min(10% × creanță; 40.000 lei) — art. 72.'),
'52':(52,'Legea 85/2014 art. 3, 5 pct. 29 и 54, 38, 66, 67, 71, 73, 74, 75, 104, 133, 139, 141, 143, 145, 154, 159, 174','⚠ ТЗ в таблице для этого ключа («insolventa sau faliment») на самом деле описывает «Procedura simplificata de insolventa». Страница написана под фокусный ключ из Конвеєра (insolventa sau faliment) и включает раздел про procedura simplificată. Показать боссу/СЕО. Legea 151/2015 — без деталей.','Если нужна отдельная страница под «procedura simplificata de insolventa» — это новый URL.'),
'53':(53,'Legea 85/2014 art. 5 pct. 54, 67, 69, 75, 78, 132, 133 (alin. 1–5), 139, 140, 141, 143, 144, 145','Составы категорий creanțe (art. 138) не перечислены, потому что не сверены. ⚠ ТЗ-файл этого ключа — другого формата (укр.), содержание совпадает по теме.','Калькулятор: 30 zile libere de la publicarea tabelului definitiv (art. 132).'),
'57':(57,'Legea 85/2014 art. 3, 5 pct. 29 и 42, 66, 67, 70–78, 100, 104, 112, 132–133, 139, 143–145, 154, 159, 174, 178','Legea 151/2015 — только упоминание. «Durata estimativă» этапов из ТЗ не указана: фиксированных сроков в законе нет. Раздел «România vs UE» не включён.','Селектор «etapa ta»: что происходит / кто / что делать.'),
}

for _n,_k in [('43','Vrancea / Focșani'),('44','Giurgiu'),('45','Prahova / Ploiești'),('46','Sibiu / Mediaș'),('47','Bistrița-Năsăud')]:
    A[_n]=(int(_n),'CPC art. 632, 651, 714 alin. 2, 727, 827–828, 837, 838, 839, 843–847, 849–851, 855–856','⚠ Местные данные ('+_k+': названия judecătorie/tribunal/curte de apel) — из общих знаний, не сверялись с portal.just.ro. Реальные цены, количество и список аукционов не приводятся (нет проверенных данных); цифры в примере — иллюстративные. ANAF: только общее различие, без номеров статей Codului de procedură fiscală. «Cazuri reale», «Banca Transilvania» из ТЗ — не включены. Реестр публикаций (art. 845) — только упоминание.','⚠ Риск дублирования: 5 городских страниц (№43–47) построены на одной проверенной процедуре (art. 838–856); отличаются местными судами и примерами. Для SEO рекомендуется добавить реальные локальные данные (список текущих лицитаций, executori по городу) или объединить в хаб. Калькулятор: 10% / 75% / 30% — art. 844, 846 alin. 8.')

def audit(n):
    P=importlib.import_module('p'+n).P
    num,ver,unv,notes=A[n]
    doc=mkdoc.doc(P); words=len(re.sub(r'<[^>]+>',' ',doc).split())
    t=len(P['title']); m=len(P['desc'])
    return f'''<html><body>
<h1>Аудит головреда — №{num} /{P['slug']}/</h1>
<p>Дата: 13.10.2026. Текст ~{words} слов (лимит ТЗ 3000). Title {t} символов, Meta {m} (лимит 200).</p>
<h2>Соответствие ТЗ</h2>
<p>H1, структура H2, прямой ответ, «Cifră pe șervețel», таблица/сетка, «Ce faci azi» (3 шага), CTA в чат, FAQ (8), 2 инфографики с alt — выполнены. Разделы ТЗ без проверенного источника (jurisprudență, «cazuri reale») не выдумывались.</p>
<h2>Сверка с первоисточником (lege5.ro)</h2>
<p>{ver}.</p>
<h2>Не проверено (человеку)</h2>
<p>{unv}</p>
<h2>Примечания</h2>
<p>{notes}</p>
<h2>Вердикт</h2>
<p>Готов; блок автора «[DE COMPLETAT]»; тексты закона — в редакции Monitorul Oficial, сверить с консолидированной версией перед публикацией.</p>
</body></html>'''
if __name__=='__main__':
    for n in [x for x in A if x in ('43','44','45','46','47')]:
        importlib.import_module('p'+n)
        open(f'/tmp/doc{n}.html','w').write(mkdoc.doc(importlib.import_module('p'+n).P))
        open(f'/tmp/audit{n}.html','w').write(audit(n))
    print('ok',len(A))
