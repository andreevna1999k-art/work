// node shot.js <каталог-blog> <hub_id> <preview_id> <каталог-для-png>  — локальний рендер out/blog-hub.html і out/block-preview.html (десктоп і телефон)
const {chromium}=require('playwright');const fs=require('fs');
const [dir,hub,prev,outd]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();
for(const [name,id] of [['blog-hub',hub],['block-preview',prev]]){
 const src=fs.readFileSync(`${dir}/out/${name}.html`,'utf8').replace(/<!-- \/?wp:html -->/g,'');
 const f=`${outd}/k-${name}.html`;
 fs.writeFileSync(f,`<!doctype html><html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body class="page-id-${id}" style="margin:0">${src}</body></html>`);
 for(const [vw,tag] of [[1366,'d'],[390,'m']]){
  const p=await b.newPage({viewport:{width:vw,height:900}});
  await p.goto('file://'+f,{waitUntil:'load'}).catch(()=>{});await p.waitForTimeout(1200);
  console.log(name,tag,'scrollWidth',await p.evaluate(()=>document.documentElement.scrollWidth));
  await p.screenshot({path:`${outd}/k-${name}-${tag}.png`,fullPage:true});await p.close();}
}
await b.close()})();
