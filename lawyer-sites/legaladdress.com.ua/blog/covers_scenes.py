from covers_lib import *
def S1():
    return (g(calendar(300,320,'30','ТЕРМІН'),170,190,-5)+g(clock(0,0,130,70),740,330)+g(note(280,130),500,520,-7)
            +coin(930,560,52)+coin(1020,500,40)+badge(860,170,44,'!',MAROON,58)+stack(1000,640,3,50,16))
def S2():
    win=(f'<g filter="url(#sh)"><path d="M330 600V250a190 190 0 0 1 380 0V600z" fill="#3A1D14" transform="translate(70 -40)"/></g>'
         f'<path d="M400 560V250a120 120 0 0 1 240 0V560z" fill="#1B0E0A" opacity=".5" transform="translate(0 0)"/>')
    win=(f'<g filter="url(#sh)"><rect x="400" y="110" width="400" height="500" rx="34" fill="#1B0E0A"/></g><rect x="425" y="135" width="350" height="450" rx="22" fill="#4A2A1D"/>'
         f'<rect x="425" y="135" width="350" height="450" rx="22" fill="url(#glow)" opacity=".6"/>'+bars(470,135,260,450,6))
    return (win+g(paper(250,320,4,True,True,stamp(125,235,60,MAROON,'НІ')),230,300,-8)+lock(900,420,1.2,True)+coin(980,560,44)+badge(250,230,40,'?',GOLD2,56))
def S3():
    sig=f'<path d="M40 380c30-40 50 30 80-10s40 20 70-8" fill="none" stroke="{BG1}" stroke-width="5" stroke-linecap="round"/>'
    hl=f'<rect x="26" y="150" width="270" height="20" rx="6" fill="{GOLD}" opacity=".7"/>'
    return (g(paper(340,470,6,True,True,hl+sig),300,150,-4)+magnifier(740,330,1.6)+badge(880,170,46,'§',MAROON,60)
            +stamp(760,560,70,MAROON,'✓',10)+g(note(240,110),820,540,8)+coin(180,600,40))
def S4():
    scr=(f'<circle cx="105" cy="150" r="48" fill="{MAROON}"/><text x="105" y="170" text-anchor="middle" font-size="58" fill="{CREAM}" {SERIF}>☎</text>'
         f'<rect x="38" y="250" width="134" height="12" rx="6" fill="{SOFT}" opacity=".5"/><rect x="58" y="280" width="94" height="12" rx="6" fill="{SOFT}" opacity=".35"/>'
         f'<circle cx="58" cy="350" r="22" fill="{MAROON}"/><circle cx="152" cy="350" r="22" fill="#4C8A5A"/>')
    bub=(f'<g filter="url(#sh)"><rect x="170" y="190" width="250" height="120" rx="26" fill="{PAPER}"/><path d="M360 310l30 44 10-44z" fill="{PAPER}"/></g>'
         f'<text x="295" y="270" text-anchor="middle" font-size="76" font-weight="700" fill="{MAROON}" {SERIF}>! ! !</text>')
    return (g(phone(210,420,scr),480,150,4)+bub+shield(900,330,1.15)+g(note(250,115),760,540,-6)+coin(240,560,46))
def S5():
    card=(f'<g filter="url(#sh)"><rect width="440" height="270" rx="26" fill="url(#gold)"/><rect y="64" width="440" height="52" fill="{BG1}" opacity=".85"/>'
          f'<rect x="36" y="150" width="76" height="58" rx="10" fill="{CREAM}" opacity=".9"/><rect x="36" y="228" width="210" height="14" rx="7" fill="{BG1}" opacity=".6"/>'
          f'<rect x="270" y="228" width="130" height="14" rx="7" fill="{BG1}" opacity=".6"/></g>')
    return (g(paper(260,340,4,True,True,stamp(130,240,62,MAROON,'ВП')),770,170,9)+g(card,300,250,-9)+lock(560,470,1.25,False)+coin(900,570,46)+badge(260,200,40,'!',MAROON,56))
def S6():
    arrow=(f'<g filter="url(#sh)"><path d="M300 190 L520 300 L610 240 L860 400" fill="none" stroke="{MAROON}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="M800 380 L880 410 L860 330z" fill="{MAROON}"/></g>')
    return (arrow+stack(330,640,6,66,20)+stack(560,640,4,66,20)+stack(790,640,2,66,20)+badge(940,250,70,'%',GOLD2,92)+g(note(220,100),880,470,10)+coin(130,560,40))
def S7():
    hg=(f'<g filter="url(#sh)"><rect x="-90" y="-150" width="180" height="26" rx="12" fill="url(#gold)"/><rect x="-90" y="124" width="180" height="26" rx="12" fill="url(#gold)"/>'
        f'<path d="M-70 -124 C-70 -30 -10 -20 -10 0 S-70 30 -70 124 H70 C70 30 10 20 10 0 S70 -30 70 -124z" fill="{CREAM}" fill-opacity=".22" stroke="{CREAM}" stroke-opacity=".6" stroke-width="5"/>'
        f'<path d="M-50 -110H50C40 -70 12 -40 0 -22C-12 -40 -40 -70 -50 -110z" fill="{GOLD}"/><path d="M-12 124H12L0 40z M-62 124H62C52 100 24 86 0 80C-24 86 -52 100 -62 124z" fill="{GOLD}"/></g>')
    return (g(calendar(330,360,'3','РОКИ'),190,190,-4)+g(hg,830,380,6)+g(note(260,120),470,540,6)+badge(660,190,44,'?',MAROON,58)+coin(1000,600,42))
def S8():
    block=f'<g filter="url(#sh)"><rect x="-130" y="170" width="260" height="46" rx="14" fill="#7A4630"/><rect x="-100" y="140" width="200" height="40" rx="10" fill="#9B5A3A"/></g>'
    return (g(paper(380,500,5,True,True,stamp(190,380,78,MAROON,'№')),230,140,-5)+g(block,830,430)+gavel(830,330,1.0,-35)+badge(960,200,76,'15',MAROON,84)
            +f'<text x="960" y="318" text-anchor="middle" font-size="30" font-weight="700" fill="{CREAM}" letter-spacing="4" {SERIF}>ДНІВ</text>')
def S9():
    scr=(f'<rect x="30" y="70" width="150" height="90" rx="16" fill="{GOLD}"/><text x="105" y="132" text-anchor="middle" font-size="52" font-weight="700" fill="{BG1}" {SERIF}>5 000</text>'
         f'<rect x="30" y="190" width="150" height="14" rx="7" fill="{SOFT}" opacity=".5"/><rect x="30" y="218" width="110" height="14" rx="7" fill="{SOFT}" opacity=".35"/>'
         f'<rect x="30" y="300" width="150" height="56" rx="28" fill="{MAROON}"/><text x="105" y="337" text-anchor="middle" font-size="26" font-weight="700" fill="{CREAM}" {SERIF}>OK</text>')
    return (g(phone(210,420,scr),330,170,-6)+stack(800,620,4,64,19)+coin(930,300,56)+badge(680,230,56,'%',MAROON,76)+g(note(240,110),620,500,8)+coin(1020,520,36))
def S10():
    chain=''.join(f'<ellipse cx="{300+i*58}" cy="{560+(i%2)*6}" rx="36" ry="20" fill="none" stroke="{GOLD}" stroke-width="10" transform="rotate({(i%2)*90} {300+i*58} {560})"/>' for i in range(0))
    return (g(house(380,310),200,190)+lock(640,520,1.1,False)+g(paper(250,330,4,True,True,stamp(125,235,60,MAROON,'АРЕШТ'.replace('АРЕШТ','§'))),800,170,8)
            +shield(960,560,.75,False)+coin(250,610,44)+badge(240,260,44,'!',MAROON,58))
def S11():
    return (g(house(300,260),420,130)+person(400,540,1.15,CREAM)+person(600,550,1.05,GOLD)+shield(780,520,.9)+g(paper(230,300,4,True,True),900,150,8)+coin(960,560,46)+stack(250,640,3,50,16)+badge(250,260,38,'?',MAROON,52))
def S12():
    return (g(house(420,350),270,170)+key(560,610,1.0,-18)+g(paper(240,320,4,True,True,stamp(120,238,58,MAROON,'₴')),820,150,9)+stack(240,650,4,56,17)+coin(1020,650,40))
SCENES={1:S1,2:S2,3:S3,4:S4,5:S5,6:S6,7:S7,8:S8,9:S9,10:S10,11:S11,12:S12}
def svg(n): return frame(SCENES[n]())
