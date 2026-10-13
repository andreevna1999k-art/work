# Reusable calculator blocks for page generator. Each returns (html, js) using ids b-calc, b-ex1, o-t/o-ts, o-c, o-r, f-s, f-d.
def _shell(h2, intro, fields, ex_btn, outs, disc):
    return f'''<section id="calculator" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Calculator</span><h2>{h2}</h2></div>
      <p>{intro}</p>
    </div>
    <div class="calc">
      <div class="panel">
        <form class="fields" onsubmit="return false">
{fields}
          <div class="row-btns">
            <button type="button" class="btn btn-primary" id="b-calc">Calculează</button>
            <button type="button" class="btn btn-line" id="b-ex1">{ex_btn}</button>
          </div>
        </form>
        <div class="result" aria-live="polite">
          <span class="lbl">Rezultat</span>
          <div class="duo">
{outs}
          </div>
          <a href="http://chat.la.co.ua/o1r0iw" target="_blank" rel="noopener" class="btn btn-primary">Trimite-ne actele în chat</a>
          <span class="disc">{disc}</span>
        </div>
      </div>
    </div>
  </div>
</section>'''
HOL=r'''  var ZI=['duminică','luni','marți','miercuri','joi','vineri','sâmbătă'];
  function dt(s){var p=s.split('-');return new Date(Date.UTC(+p[0],+p[1]-1,+p[2]))}
  function fmt(d){return ('0'+d.getUTCDate()).slice(-2)+'.'+('0'+(d.getUTCMonth()+1)).slice(-2)+'.'+d.getUTCFullYear()}
  function key(d){return d.getUTCFullYear()+'-'+(d.getUTCMonth()+1)+'-'+d.getUTCDate()}
  function addD(d,n){var x=new Date(d.getTime());x.setUTCDate(x.getUTCDate()+n);return x}
  function easter(y){var a=y%4,b=y%7,c=y%19,d=(19*c+15)%30,e=(2*a+4*b-d+34)%7,m=Math.floor((d+e+114)/31),day=((d+e+114)%31)+1;return addD(new Date(Date.UTC(y,m-1,day)),13)}
  function hol(y){var s={},add=function(m,d){s[y+'-'+m+'-'+d]=1},E=easter(y);
    [[1,1],[1,2],[1,6],[1,7],[1,24],[5,1],[6,1],[8,15],[11,30],[12,1],[12,25],[12,26]].forEach(function(x){add(x[0],x[1])});
    [-2,0,1,49,50].forEach(function(n){s[key(addD(E,n))]=1});return s}
  function off(d){var w=d.getUTCDay();if(w===0||w===6)return true;return !!hol(d.getUTCFullYear())[key(d)]}
  function cls(id,c){var e=$(id);e.classList.remove('alert','ok');if(c)e.classList.add(c)}
  function addM(d,y,m){var x=new Date(Date.UTC(d.getUTCFullYear()+y,d.getUTCMonth()+m,d.getUTCDate()));return x}
'''
def deadline(h2,intro,sel_label,opts,date_label,ex_date,ex_btn,k_main,disc,y=0,m=0,days=0,roll=True,note_by_opt=None):
    """opts: list of (label, explanation shown under result). Deadline = date + y years + m months + days (+ roll to working day)."""
    o=''.join(f'<option value="{i}">{x[0]}</option>' for i,x in enumerate(opts))
    fields=f'''          <div class="field full"><label for="f-s">{sel_label}</label><div class="inp"><select id="f-s">{o}</select></div></div>
          <div class="field full"><label for="f-d">{date_label}</label><div class="inp"><input type="date" id="f-d"></div></div>'''
    outs=f'''            <div class="opt full" id="c-t"><span class="k">{k_main}</span><span class="v" id="o-t">—</span><span class="s" id="o-ts">Completează data.</span></div>
            <div class="opt" id="c-c"><span class="k">Înainte de prelungire</span><span class="v" id="o-c">—</span><span class="s" id="o-cs">Data calculată.</span></div>
            <div class="opt" id="c-r"><span class="k">Zile rămase</span><span class="v" id="o-r">—</span><span class="s" id="o-rs">Până la ultima zi.</span></div>'''
    import json
    expl=json.dumps([x[1] for x in opts],ensure_ascii=False); dl=json.dumps([x[2] if len(x)>2 else days for x in opts])
    js=HOL+f'''  var EX={expl},DL={dl};
  function calc(){{
    var v=$('f-d').value,s=parseInt($('f-s').value,10);
    if(!v){{$('o-t').textContent='—';cls('c-t');$('o-ts').textContent='Completează data.';$('o-c').textContent='—';$('o-r').textContent='—';return}}
    var st=dt(v),e=addD(addM(st,{y},{m}),DL[s]),raw=e,moved=[];
    {"while(off(e)){moved.push(fmt(e));e=addD(e,1)}" if roll else ""}
    $('o-c').textContent=fmt(raw)+' ('+ZI[raw.getUTCDay()]+')';
    $('o-cs').textContent=moved.length?'Zi nelucrătoare: se prelungește.':'Zi lucrătoare.';
    $('o-t').textContent=fmt(e)+' ('+ZI[e.getUTCDay()]+')';cls('c-t','alert');
    $('o-ts').textContent=EX[s];
    var t=new Date();var today=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate()));
    var left=Math.round((e.getTime()-today.getTime())/864e5);
    if(0>left){{$('o-r').textContent='Termen trecut';cls('c-r','alert');$('o-rs').textContent='Verifică dovada comunicării, întreruperile sau repunerea în termen.'}}
    else{{$('o-r').textContent=left+' zile';cls('c-r',left<=3?'alert':'ok');$('o-rs').textContent=left<=3?'Acționează cât mai repede.':'Până la ultima zi.'}}
  }}
  $('b-calc').addEventListener('click',calc);
  ['f-s','f-d'].forEach(function(id){{$(id).addEventListener('input',calc);$(id).addEventListener('change',calc)}});
  function ex(){{$('f-s').value='0';$('f-d').value='{ex_date}';calc()}}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){{b.addEventListener('click',function(){{ex();$('calculator').scrollIntoView({{behavior:'smooth'}})}})}});'''
    return _shell(h2,intro,fields,ex_btn,outs,disc),js
def select(h2,intro,sel_label,rows,ex_idx,ex_btn,k1,k2,k3,disc):
    """rows: list of (option label, result1, result2, result3)."""
    import json
    o=''.join(f'<option value="{i}">{r[0]}</option>' for i,r in enumerate(rows))
    fields=f'''          <div class="field full"><label for="f-s">{sel_label}</label><div class="inp"><select id="f-s">{o}</select></div></div>'''
    outs=f'''            <div class="opt full" id="c-t"><span class="k">{k1}</span><span class="v" id="o-t" style="font-size:19px">—</span><span class="s" id="o-ts">Alege o variantă.</span></div>
            <div class="opt" id="c-m"><span class="k">{k2}</span><span class="v" id="o-m" style="font-size:17px">—</span><span class="s" id="o-ms"> </span></div>
            <div class="opt" id="c-r"><span class="k">{k3}</span><span class="v" id="o-r" style="font-size:17px">—</span><span class="s" id="o-rs"> </span></div>'''
    D=json.dumps([list(r[1:]) for r in rows],ensure_ascii=False)
    js=f'''  var D={D};
  function calc(){{var d=D[parseInt($('f-s').value,10)];$('o-t').textContent=d[0];$('o-m').textContent=d[1];$('o-r').textContent=d[2];$('c-t').classList.add('alert')}}
  $('b-calc').addEventListener('click',calc);
  $('f-s').addEventListener('change',calc);
  function ex(){{$('f-s').value='{ex_idx}';calc()}}
  $('b-ex1').addEventListener('click',ex);
  root.querySelectorAll('[data-ex]').forEach(function(b){{b.addEventListener('click',function(){{ex();$('calculator').scrollIntoView({{behavior:'smooth'}})}})}});'''
    return _shell(h2,intro,fields,ex_btn,outs,disc).replace('>Calculează<','>Vezi rezultatul<'),js
