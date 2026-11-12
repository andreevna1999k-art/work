import json,subprocess,re,sys,collections
doms=["advokat-kharkov.org.ua","advokato.in.ua","argument-consulting.com.ua","bankruptcyukraine.com","jurist-po-ipotechnum-kreditam.kiev.ua","lawmsb.com.ua","legaladdress.com.ua","pravovid.com.ua","profconsulting.com.ua","rada-advokat.uz.ua","uchet.com.ua","ukrjurist.com.ua","urists.com.ua","yuristy.in.ua","jurist-online.info","spacelaw.com.ua"]
PH=re.compile(r"(покрокова інструкція|покроковий план|інструкція юриста|покрокова перевірка|покрокове керівництво)",re.I)
def get(d,typ="pages"):
    out=[]
    for page in range(1,6):
        r=subprocess.run(["curl","-s","-m","60",f"https://{d}/wp-json/wp/v2/{typ}?per_page=100&page={page}&status=any&context=edit&_fields=id,status,slug,title,content,excerpt,meta"],capture_output=True,text=True)
        try:j=json.loads(r.stdout)
        except: break
        if not isinstance(j,list) or not j:break
        out+=j
    return out
if __name__=="__main__":
    ctx=collections.Counter(); per={}
    for d in doms:
        for typ in ("pages","posts"):
            pg=get(d,typ)
            for p in pg:
                fields={"title":p["title"].get("raw",""),"content":p["content"].get("raw",""),"excerpt":p["excerpt"].get("raw","") if isinstance(p.get("excerpt"),dict) else ""}
                if isinstance(p.get("meta"),dict):
                    for k,v in p["meta"].items():
                        if isinstance(v,str): fields["meta:"+k]=v
                for fn,t in fields.items():
                    for m in PH.finditer(t):
                        s=t[max(0,m.start()-45):m.end()+40].replace("\n"," ")
                        ctx[(d,fn,s)]+=1
            print(d,typ,len(pg),file=sys.stderr)
    for (d,fn,s),n in sorted(ctx.items()): print(f"{d}|{fn}|{n}|{s}")
