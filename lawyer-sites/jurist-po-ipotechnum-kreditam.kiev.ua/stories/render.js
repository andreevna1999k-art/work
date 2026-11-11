const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const items=JSON.parse(fs.readFileSync('content.json','utf8'));
const only=process.argv[2];
for(const it of items){ if(only&&it.n!==only) continue;
 const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+process.cwd()+'/story.html?d='+encodeURIComponent(JSON.stringify(it)));
 await p.waitForFunction(()=>document.title==='ready',{timeout:20000});await p.waitForTimeout(300);
 await p.screenshot({path:`out/${it.n}-${it.slug}.png`});await p.close();console.log(it.n)}
await b.close()})();
