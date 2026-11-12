import json,subprocess,re,sys,os,time
sys.path.insert(0,__import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from scan import doms,get
APPLY="--apply" in sys.argv
ONLY=[a for a in sys.argv[1:] if not a.startswith("--")]
SUF=r"(?:покрокова інструкція юриста|покроковий план боржника від юриста|покроковий план від юриста|покроковий план юриста|покрокова перевірка від юриста|інструкція юриста для позичальника|інструкція юриста)"
W=r"(?![\wа-яіїєґ'’-])"
R=[
 # описи: кінець фрази/ речення
 (rf"Покроковий план від юриста Олега Бондаря\.", "Автор: юрист Олег Бондар."),
 (rf"Покроковий план від юриста Дмитра Яковенка\.", "Автор: юрист Дмитро Яковенко."),
 (r"Покрокова інструкція юриста й чекліст на сьогодні", "Чекліст на сьогодні"),
 (r"Покроковий план і чекліст юриста\.", "Чекліст на сьогодні."),
 (r"Покроковий план юриста й чекліст\.", "Чекліст на сьогодні."),
 (r"Покроковий план юриста\. (?=Опишіть)", ""),
 (r", покроковий план від юриста\.", "."),
 (r"та покроковий план\. (?=Консультація юриста)", "та план дій. "),
 (r"Покрокова інструкція по захисту від колекторів\.", "Як захиститися від колекторів: порядок дій."),
 (r"\s*Покрокова інструкція юриста\.", ""),
 (r"\s*Покроковий план від юриста\.", ""),
 (r"Покроковий план\.", "План дій."),
 # у середині описів
 (r": покрокова інструкція юриста, ", ": "),
 (r": покрокова інструкція, ", ": "),
 # заголовки/титули
 (r"боргів законно: покроковий план"+W, "боргів законно"),
 (rf"\s*:\s*{SUF}"+W, ""),
 (r"\s*:\s*покрокова перевірка"+W, ""),
 (r"(Що [^<\"]{0,60}?): покроковий план (?=для|після)", r"\1: план дій "),
 (r"(Що [^<\"]{0,60}?): покроковий план"+W, r"\1: план дій"),
 (r"Покрокова інструкція: як перевірити", "Як перевірити"),
 (r"Покрокова інструкція збору доказів:", "Як зібрати докази:"),
 (r"Покрокова інструкція подачі скарги:", "Як подати скаргу:"),
 (r"Що зробити сьогодні: покрокова інструкція", "Що зробити сьогодні: порядок дій"),
 (r": покрокова інструкція(?=<)", ": крок за кроком"),
 (r"та покрокова інструкція(?=<)", "та порядок дій"),
 # загальні
 (r"Покроковий план дій", "План дій"),
 (r"покроковий план дій", "план дій"),
 (r"покроковий план", "план дій"),
 (r"Покроковий план", "План дій"),
 (r"покрокова інструкція", "порядок дій"),
 (r"Покрокова інструкція", "Порядок дій"),
]
RC=[(re.compile(a),b) for a,b in R]
def fx(s):
    if not isinstance(s,str): return s
    for r,b in RC: s=r.sub(b,s)
    return s
PH=re.compile(r"(покрокова інструкція|покроковий план|інструкція юриста|покрокова перевірка|покрокове керівництво)",re.I)
def call(m,url,data=None):
    cmd=["curl","-s","-m","180","-X",m,url]; inp=None
    if data is not None: cmd+=["-H","Content-Type: application/json","--data-binary","@-"]; inp=json.dumps(data,ensure_ascii=False).encode()
    r=subprocess.run(cmd,input=inp,capture_output=True)
    try:return json.loads(r.stdout.decode())
    except: return {"raw":r.stdout.decode()[:200]}
os.makedirs("/tmp/ai-markers-backup",exist_ok=True)
tot=0
for d in doms:
    if ONLY and d not in ONLY: continue
    for typ in ("pages","posts"):
        for p in get(d,typ):
            upd={}
            t=p["title"].get("raw",""); c=p["content"].get("raw","")
            e=p["excerpt"].get("raw","") if isinstance(p.get("excerpt"),dict) else ""
            if PH.search(t): upd["title"]=fx(t)
            if PH.search(c): upd["content"]=fx(c)
            if PH.search(e): upd["excerpt"]=fx(e)
            mt={k:fx(v) for k,v in (p.get("meta") or {}).items() if isinstance(v,str) and PH.search(v)}
            if mt: upd["meta"]=mt
            if not upd: continue
            tot+=1
            left=[k for k,v in upd.items() if (PH.search(v) if isinstance(v,str) else any(PH.search(x) for x in v.values()))]
            print(d,typ,p["id"],p["status"],p["slug"][:42],list(upd),"LEFT:"+",".join(left) if left else "")
            if "title" in upd: print("   T:",t,"=>",upd["title"])
            if APPLY:
                json.dump(p,open(f"/tmp/ai-markers-backup/{d}-{typ}-{p['id']}.json","w"),ensure_ascii=False)
                r=call("POST",f"https://{d}/wp-json/wp/v2/{typ}/{p['id']}",upd)
                print("   ->",r.get("id"),r.get("status"),str(r.get("code",""))[:50],str(r.get("raw",""))[:80])
print("pages to change:",tot)
