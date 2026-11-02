def h(c):
    c=c.lstrip('#'); return tuple(int(c[i:i+2],16) for i in (0,2,4))
def lum(rgb):
    f=lambda v:(v/255/12.92) if v/255<=.03928 else ((v/255+.055)/1.055)**2.4
    r,g,b=[f(x) for x in rgb]; return .2126*r+.7152*g+.0722*b
def mix(fg,bg,a): return tuple(round(fg[i]*a+bg[i]*(1-a)) for i in range(3))
def cr(fg,bg,a=1):
    f=mix(h(fg),h(bg),a) if a<1 else h(fg)
    l1,l2=lum(f),lum(h(bg)); 
    if l1<l2: l1,l2=l2,l1
    return (l1+.05)/(l2+.05)
V={
'V1 mahogany':[('ink-soft on white','#6B5A50','#FFFFFF',1),('ink-soft on page','#6B5A50','#F5EEE4',1),('ink on page','#2A1812','#F5EEE4',1),
 ('cream-soft(.74) on brown','#F4E6D0','#5C2B1D',.74),('cream on brown','#F4E6D0','#5C2B1D',1),('gold on brown','#D4B27A','#5C2B1D',1),
 ('cream-soft on brown-dark','#F4E6D0','#2B1711',.74),('gold on brown-dark','#D4B27A','#2B1711',1),('white on maroon btn','#FFFFFF','#6E1423',1),
 ('maroon on white (chip)','#6E1423','#FFFFFF',1),('ink-soft on soft card','#6B5A50','#FFFFFF',1),('cream-soft on svc card (brown+6%)','#F4E6D0','#6A3A2D',.74)],
'V2 light khaki':[('white on khaki btn','#FFFFFF','#A89B6B',1),('khaki on white (h2 span)','#A89B6B','#FFFFFF',1),('muted on white','#7C7A72','#FFFFFF',1),('muted on soft','#7C7A72','#F5F3EC',1),
 ('ink on soft','#262626','#F5F3EC',1),('khaki on night','#A89B6B','#0D1017',1),('white .78 on night','#FFFFFF','#0D1017',.78),('khaki on r-card #3B3B3B','#A89B6B','#3B3B3B',1),('white.75 on #3B3B3B','#FFFFFF','#3B3B3B',.75),('khaki-d on white','#857849','#FFFFFF',1),('white on khaki-d','#FFFFFF','#857849',1)],
'V3 navy gold':[('muted on white','#6F7189','#FFFFFF',1),('muted on page','#6F7189','#F1F1F5',1),('gold on navy','#C9A06A','#181A31',1),('white.7 on navy','#FFFFFF','#181A31',.7),('white.66 on navy','#FFFFFF','#181A31',.66),
 ('navy on gold btn','#181A31','#C9A06A',1),('gold-d on white (facts)','#A97F47','#FFFFFF',1),('muted on #FBFAF6','#6F7189','#FBFAF6',1),('white.7 on navy card','#FFFFFF','#23254A',.7),('gold on navy card','#C9A06A','#23254A',1),('muted on label','#6F7189','#FFFFFF',1)]}
for k,L in V.items():
    print('==',k)
    for n,f,b,a in L:
        r=cr(f,b,a); print(f'{r:5.2f} {"OK " if r>=4.5 else ("lg " if r>=3 else "BAD")} {n}')
