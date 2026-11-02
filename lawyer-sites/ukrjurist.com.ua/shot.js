const {chromium}=require('/opt/node-tools/node_modules/playwright');
const fs=require('fs');
let src=fs.readFileSync(__dirname+'/home.wp.html','utf8');
src=src.split('https://ukrjurist.com.ua/wp-content/uploads/2026/10/goncharuk-').join('file://'+__dirname+'/img/goncharuk-');
const theme='<style>h1,h2,h3{color:#000}a{text-decoration:underline}body{margin:0;font-family:serif}</style>';
const html='<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'+theme+'<body>'+src;
const out='/tmp/claude-0/-home-user-work/bd2e8cc1-3024-54de-bcd5-7f29eaa7db16/scratchpad/g_';
(async()=>{const b=await chromium.launch();
for(const [n,w,h] of [['d1440',1440,900],['d1024',1024,768],['m390',390,844]]){
 const pg=await b.newPage({viewport:{width:w,height:h}});
 fs.writeFileSync(__dirname+'/_t.html',html);await pg.goto('file://'+__dirname+'/_t.html');await pg.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}window.scrollTo(0,0)});await pg.waitForTimeout(1500);
 await pg.screenshot({path:out+n+'.png',fullPage:true});
 console.log(n,await pg.evaluate('document.documentElement.scrollWidth'),await pg.evaluate('document.documentElement.scrollHeight'));
}
await b.close();})();
