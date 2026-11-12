import json,subprocess,re,sys,os,time
sys.path.insert(0,__import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from scan import doms,get
APPLY="--apply" in sys.argv
ONLY=[a for a in sys.argv[1:] if not a.startswith("--")]

R=[
 (r"[Кк]оротка відповідь юриста", lambda m: m.group(0)[:-7]),
 (r":\s*відповідь юриста за ст\.", " за ст."),
 (r"\s*:\s*(?:відповідь юриста|алгоритм дій від юриста)(?=[\"<,]|$)", ""),
 (r"\s*:\s*(?:відповідь юриста|алгоритм дій від юриста)", ""),
 (r"відповідь юриста", "відповідь"),
 (r"алгоритм дій від юриста", "алгоритм дій"),
]
def fx(s):
    if not isinstance(s,str): return s
    for a,b in R: s=re.sub(a,b,s)
    return s
PH=re.compile(r"(відповідь юриста|алгоритм дій від юриста)",re.I)
def call(m,url,data=None):
    cmd=["curl","-s","-m","180","-X",m,url]; inp=None
    if data is not None: cmd+=["-H","Content-Type: application/json","--data-binary","@-"]; inp=json.dumps(data,ensure_ascii=False).encode()
    r=subprocess.run(cmd,input=inp,capture_output=True)
    try:return json.loads(r.stdout.decode())
    except: return {"raw":r.stdout.decode()[:200]}
os.makedirs("/tmp/ai-markers-backup3",exist_ok=True)
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
                json.dump(p,open(f"/tmp/ai-markers-backup3/{d}-{typ}-{p['id']}.json","w"),ensure_ascii=False)
                r=call("POST",f"https://{d}/wp-json/wp/v2/{typ}/{p['id']}",upd)
                print("   ->",r.get("id"),r.get("status"),str(r.get("code",""))[:50],str(r.get("raw",""))[:80])
print("pages to change:",tot)
