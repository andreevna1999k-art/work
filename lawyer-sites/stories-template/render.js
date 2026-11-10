const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch();
 const files=process.argv.slice(2);
 for(const f of files){
  const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
  await p.goto('file://'+process.cwd()+'/'+f+'.html');
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(900);
  // report widths of headline lines
  const info=await p.evaluate(()=>{const h=document.getElementById('h')||document.querySelector('.h');if(!h)return [];const r=document.createRange();r.selectNodeContents(h);return [...r.getClientRects()].map(x=>[Math.round(x.left),Math.round(x.right),Math.round(x.top),Math.round(x.bottom)])});
  console.log(f,JSON.stringify(info));
  await p.screenshot({path:f+'.png'});
  await p.close();
 }
 await b.close();
})();
