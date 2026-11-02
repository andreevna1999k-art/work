"""Примітиви для тематичних SVG-ілюстрацій у палітрі сайту (коричневий/золото/кремовий/бордо)."""
BG1,BG2,CREAM,PAPER,GOLD,GOLD2,MAROON,INK,SOFT='#6B3424','#2B1711','#F4E6D0','#FBF3E6','#D4B27A','#B88C4A','#8A1D30','#2A1812','#8A7466'
SERIF="font-family=\"Georgia,'Times New Roman',serif\""
def g(body,x=0,y=0,rot=0,s=1,cx=0,cy=0):
    return f'<g transform="translate({x} {y}) rotate({rot} {cx} {cy}) scale({s})">{body}</g>'
def shadow(): return '<filter id="sh" x="-20%" y="-20%" width="150%" height="150%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity=".38"/></filter>'
def paper(w=300,h=380,lines=5,title=True,fold=True,seal=None):
    o=f'<g filter="url(#sh)"><rect width="{w}" height="{h}" rx="14" fill="{PAPER}"/>'
    if fold: o+=f'<path d="M{w-60} 0 L{w} 60 V0z" fill="{CREAM}"/><path d="M{w-60} 0 V46a14 14 0 0 0 14 14H{w}z" fill="{GOLD}" opacity=".55"/>'
    o+='</g>'
    if title: o+=f'<rect x="30" y="34" width="{w*0.5:.0f}" height="16" rx="8" fill="{BG1}"/>'
    for i in range(lines):
        y=84+i*((h-150)/max(lines,1)); ww=(w-60)*(1 if i%3!=2 else .62)
        o+=f'<rect x="30" y="{y:.0f}" width="{ww:.0f}" height="9" rx="4.5" fill="{SOFT}" opacity=".35"/>'
    if seal: o+=seal
    return o
def stamp(cx,cy,r,col=MAROON,txt='',rot=-14):
    return (f'<g transform="rotate({rot} {cx} {cy})"><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="7" opacity=".9"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r-14}" fill="none" stroke="{col}" stroke-width="2.5" opacity=".9"/>'
            f'<text x="{cx}" y="{cy+r*0.28:.0f}" text-anchor="middle" font-size="{r*0.8:.0f}" font-weight="700" fill="{col}" {SERIF}>{txt}</text></g>')
def coin(cx,cy,r=44,sym='₴'):
    return (f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gold)"/><circle cx="{cx}" cy="{cy}" r="{r*0.78:.0f}" fill="none" stroke="{GOLD2}" stroke-width="3"/>'
            f'<text x="{cx}" y="{cy+r*0.3:.0f}" text-anchor="middle" font-size="{r*0.95:.0f}" font-weight="700" fill="{BG1}" {SERIF}>{sym}</text></g>')
def stack(cx,cy,n,r=62,h=20):
    o=''
    for i in range(n):
        y=cy-i*h
        o+=(f'<ellipse cx="{cx}" cy="{y+h*0.55:.0f}" rx="{r}" ry="{r*0.34:.0f}" fill="{GOLD2}"/><rect x="{cx-r}" y="{y-h*0.45:.0f}" width="{2*r}" height="{h}" fill="url(#gold)"/>'
            f'<ellipse cx="{cx}" cy="{y-h*0.45:.0f}" rx="{r}" ry="{r*0.34:.0f}" fill="{GOLD}"/><ellipse cx="{cx}" cy="{y-h*0.45:.0f}" rx="{r*0.7:.0f}" ry="{r*0.22:.0f}" fill="none" stroke="{GOLD2}" stroke-width="2"/>')
    return o
def note(w=250,h=120,sym='₴',rot=0):
    return (f'<g filter="url(#sh)"><rect width="{w}" height="{h}" rx="12" fill="#E5D3B0"/><rect x="8" y="8" width="{w-16}" height="{h-16}" rx="8" fill="none" stroke="{GOLD2}" stroke-width="2.5"/>'
            f'<circle cx="{w/2}" cy="{h/2}" r="{h*0.28:.0f}" fill="{GOLD}"/><text x="{w/2}" y="{h/2+h*0.12:.0f}" text-anchor="middle" font-size="{h*0.34:.0f}" font-weight="700" fill="{BG1}" {SERIF}>{sym}</text></g>')
def phone(w=210,h=400,screen=''):
    return (f'<g filter="url(#sh)"><rect width="{w}" height="{h}" rx="34" fill="#1B0E0A"/><rect x="9" y="9" width="{w-18}" height="{h-18}" rx="27" fill="{BG2}"/>'
            f'<rect x="{w/2-32}" y="20" width="64" height="12" rx="6" fill="#1B0E0A"/></g>{screen}')
def lock(cx,cy,s=1,open_=False,col=GOLD):
    sh=f'M-34 -8V-34a34 34 0 0 1 68 0V-8' if not open_ else 'M-34 -8V-34a34 34 0 0 1 64 -12'
    return (f'<g transform="translate({cx} {cy}) scale({s})"><path d="{sh}" fill="none" stroke="{col}" stroke-width="13" stroke-linecap="round"/>'
            f'<rect x="-56" y="-12" width="112" height="86" rx="16" fill="url(#gold)" filter="url(#sh)"/><circle cx="0" cy="26" r="11" fill="{BG1}"/><rect x="-4" y="30" width="8" height="24" rx="4" fill="{BG1}"/></g>')
def clock(cx,cy,r=100,a=40):
    import math
    mx,my=cx+math.cos(math.radians(a))*r*0.62,cy+math.sin(math.radians(a))*r*0.62
    o=f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAPER}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GOLD}" stroke-width="9"/></g>'
    for i in range(12):
        t=math.radians(i*30); o+=f'<line x1="{cx+math.cos(t)*r*0.8:.0f}" y1="{cy+math.sin(t)*r*0.8:.0f}" x2="{cx+math.cos(t)*r*0.9:.0f}" y2="{cy+math.sin(t)*r*0.9:.0f}" stroke="{BG1}" stroke-width="4" stroke-linecap="round"/>'
    o+=f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-r*0.45:.0f}" stroke="{BG1}" stroke-width="8" stroke-linecap="round"/><line x1="{cx}" y1="{cy}" x2="{mx:.0f}" y2="{my:.0f}" stroke="{MAROON}" stroke-width="6" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="9" fill="{BG1}"/>'
    return o
def calendar(w=260,h=280,num='',top='',col=MAROON):
    return (f'<g filter="url(#sh)"><rect width="{w}" height="{h}" rx="18" fill="{PAPER}"/><path d="M0 18a18 18 0 0 1 18-18H{w-18}a18 18 0 0 1 18 18V70H0z" fill="{col}"/></g>'
            f'<circle cx="60" cy="10" r="9" fill="{CREAM}"/><circle cx="{w-60}" cy="10" r="9" fill="{CREAM}"/>'
            f'<text x="{w/2}" y="52" text-anchor="middle" font-size="26" font-weight="700" fill="{CREAM}" letter-spacing="3" {SERIF}>{top}</text>'
            f'<text x="{w/2}" y="{h*0.8:.0f}" text-anchor="middle" font-size="{h*0.46:.0f}" font-weight="700" fill="{BG1}" {SERIF}>{num}</text>')
def house(w=300,h=260,door=True):
    return (f'<g filter="url(#sh)"><path d="M{w/2} 0 L{w+30} {h*0.42:.0f} H-30z" fill="{MAROON}"/><rect x="10" y="{h*0.42:.0f}" width="{w-20}" height="{h*0.58:.0f}" fill="{CREAM}"/></g>'
            f'<rect x="{w*0.14:.0f}" y="{h*0.55:.0f}" width="{w*0.2:.0f}" height="{h*0.2:.0f}" rx="4" fill="{GOLD}"/><rect x="{w*0.66:.0f}" y="{h*0.55:.0f}" width="{w*0.2:.0f}" height="{h*0.2:.0f}" rx="4" fill="{GOLD}"/>'
            +(f'<rect x="{w*0.4:.0f}" y="{h*0.62:.0f}" width="{w*0.2:.0f}" height="{h*0.38:.0f}" rx="6" fill="{BG1}"/><circle cx="{w*0.56:.0f}" cy="{h*0.82:.0f}" r="4" fill="{GOLD}"/>' if door else '')
            +f'<circle cx="{w/2}" cy="{h*0.26:.0f}" r="{w*0.07:.0f}" fill="{CREAM}"/>')
def shield(cx,cy,s=1,check=True,col=GOLD):
    p='M0 -90 L74 -62 V4 C74 52 40 82 0 98 C-40 82 -74 52 -74 4 V-62z'
    o=f'<g transform="translate({cx} {cy}) scale({s})"><path d="{p}" fill="url(#gold)" filter="url(#sh)"/><path d="{p}" fill="none" stroke="{GOLD2}" stroke-width="6" transform="scale(.84)"/>'
    if check: o+=f'<path d="M-30 4 l22 24 L36 -22" fill="none" stroke="{BG1}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
    return o+'</g>'
def scales(cx,cy,s=1):
    return (f'<g transform="translate({cx} {cy}) scale({s})" fill="none" stroke="{GOLD}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M0 -110V110M-50 110H50M-140 -70H140"/><path d="M-140 -70l-50 110M-140 -70l50 110M140 -70l-50 110M140 -70l50 110"/>'
            f'<path d="M-195 40a55 28 0 0 0 110 0zM85 40a55 28 0 0 0 110 0z" fill="{GOLD2}"/><circle cx="0" cy="-122" r="14" fill="{GOLD}"/></g>')
def gavel(cx,cy,s=1,rot=-30):
    return (f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})" filter="url(#sh)"><rect x="-26" y="-28" width="190" height="56" rx="14" fill="url(#gold)" transform="translate(-40 -80) rotate(0)"/>'
            f'<rect x="-14" y="-52" width="22" height="104" rx="8" fill="{GOLD2}" transform="translate(-30 -80)"/><rect x="-14" y="-52" width="22" height="104" rx="8" fill="{GOLD2}" transform="translate(120 -80)"/>'
            f'<rect x="25" y="-60" width="26" height="250" rx="12" fill="#9B5A3A"/></g>')
def magnifier(cx,cy,s=1):
    return (f'<g transform="translate({cx} {cy}) scale({s})"><circle r="70" fill="{CREAM}" fill-opacity=".18" stroke="{GOLD}" stroke-width="14"/>'
            f'<path d="M50 50L110 112" stroke="{GOLD}" stroke-width="22" stroke-linecap="round"/></g>')
def bars(x,y,w,h,n=7):
    o=''
    for i in range(n): o+=f'<rect x="{x+i*(w/(n-1))-8:.0f}" y="{y}" width="16" height="{h}" rx="8" fill="#1B0E0A" opacity=".75"/>'
    return o+f'<rect x="{x-20}" y="{y-10}" width="{w+40}" height="20" rx="8" fill="#1B0E0A"/><rect x="{x-20}" y="{y+h-10}" width="{w+40}" height="20" rx="8" fill="#1B0E0A"/>'
def key(cx,cy,s=1,rot=-35):
    return (f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})" filter="url(#sh)"><circle r="46" fill="none" stroke="url(#gold)" stroke-width="22"/><rect x="40" y="-9" width="190" height="18" rx="9" fill="{GOLD}"/>'
            f'<rect x="170" y="-9" width="14" height="46" rx="5" fill="{GOLD}"/><rect x="200" y="-9" width="14" height="32" rx="5" fill="{GOLD}"/></g>')
def person(cx,cy,s=1,col=CREAM,body=BG1):
    return (f'<g transform="translate({cx} {cy}) scale({s})" filter="url(#sh)"><circle cy="-92" r="34" fill="{col}"/><path d="M-62 90V0a62 62 0 0 1 124 0V90z" fill="{col}"/></g>')
def badge(cx,cy,r,txt,col=MAROON,fs=None):
    fs=fs or r*0.9
    return f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/><text x="{cx}" y="{cy+fs*0.34:.0f}" text-anchor="middle" font-size="{fs:.0f}" font-weight="700" fill="{CREAM}" {SERIF}>{txt}</text></g>'
def frame(inner,seed=0):
    deco=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{GOLD}" opacity="{o}"/>' for x,y,r,o in [(140,120,60,.07),(1080,640,90,.07),(980,90,26,.12),(220,620,34,.10),(60,420,16,.14),(1130,330,20,.12),(560,60,12,.12)])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="750" viewBox="0 0 1200 750"><defs>'
            f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>'
            f'<radialGradient id="glow" cx=".55" cy=".45" r=".6"><stop offset="0" stop-color="{GOLD}" stop-opacity=".34"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#EBCD94"/><stop offset="1" stop-color="{GOLD2}"/></linearGradient>{shadow()}</defs>'
            f'<rect width="1200" height="750" fill="url(#bg)"/><rect width="1200" height="750" fill="url(#glow)"/>'
            f'<g fill="none" stroke="{GOLD}" stroke-opacity=".13" stroke-width="2"><circle cx="600" cy="375" r="330"/><circle cx="600" cy="375" r="250"/></g>{deco}{inner}</svg>')
