const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();
const jobs=[['01-yak-diznatysia-chy-vziato-na-mene-mikrozaim','a1'],['hub','hub'],['home','home'],['04-yak-zakhystytysia-vid-kredytnykh-shakhraiv','a4']];
for(const [f,o] of jobs){const p=await b.newPage({viewport:{width:1280,height:900}});
const html='<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}</style></head><body>'+fs.readFileSync(path.join('preview',f+'.html'),'utf8')+'</body></html>';
const tmp=path.resolve('preview','_'+o+'.html');fs.writeFileSync(tmp,html);
await p.goto('file://'+tmp+'?preview=true',{waitUntil:'networkidle'}).catch(()=>{});await p.waitForTimeout(1500);
await p.screenshot({path:'/tmp/claude-0/jo/'+o+'.png',fullPage:true});await p.close();}
await b.close()})();
