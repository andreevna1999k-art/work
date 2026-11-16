import re, openpyxl, os
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
HOME='https://lawagency.kiev.ua/'; KOMP=HOME+'kompanii/'
def md2html(md):
    out=[];lst=None
    def close():
        nonlocal lst
        if lst: out.append('</%s>'%lst); lst=None
    def inl(t):
        t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
        return re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
    for line in md.split('\n')[1:]:
        line=line.strip()
        if not line: close(); continue
        if line.startswith('## '): close(); out.append('<h2>%s</h2>'%inl(line[3:]))
        elif line.startswith('- '):
            if lst!='ul': close(); out.append('<ul>'); lst='ul'
            out.append('<li>%s</li>'%inl(line[2:]))
        elif re.match(r'\d+\. ',line):
            if lst!='ol': close(); out.append('<ol>'); lst='ol'
            out.append('<li>%s</li>'%inl(re.sub(r'^\d+\. ','',line)))
        else: close(); out.append('<p>%s</p>'%inl(line))
    close(); return '\n'.join(out)
plan=openpyxl.load_workbook('GUEST-POSTS-PLAN.xlsx').active
rows=[]
files={}
for i in range(1,11): files[i]='bare-%02d.md'%i
for i in (11,13,14,15,17,18,19,20): files[i]='anchor-%d.md'%i
for i in range(21,26): files[i]='platform-%d.md'%i
for r in plan.iter_rows(min_row=2,max_row=26,values_only=True):
    typ,n,title,anchor,url,price,lang=r[:7]
    kind='Безанкорне' if n<=10 else 'Анкор'
    if n==18: anchor='юридична фірма ТОВ ЛА Консалтинг має оцінку 4,7 на порталі відгуків'
    if n==12: lang='Російська (уточнити)'
    else: lang='Українська'
    if n<=10: anchor=url
    content=md2html(open(files[n]).read()) if n in files else ''
    rows.append(['','lawagency.kiev.ua',lang,url,kind,anchor,title,content,'','',price.replace('–','-')]+['']*14)
H=['Дата публікації','Домен сайту','Мова','Сторінка акцептор','Тип посилання','Анкор','Заголовок/тема','Контент для розміщення','CSV','Домен (площадка)','Ціна до 1000','DR','Трафік','Тематика','Authority Score','Backlinks','Domains','IPs','Follow links','Nofollow links','Text links','Image links','Page','Індекс опублікованої статті']
rows=[r[:11]+['']*13 for r in rows]
wb=openpyxl.Workbook(); ws=wb.active; ws.title='Гест пости lawagency.kiev.ua'
ws.append(H)
for r in rows: ws.append(r)
for c in ws[1]:
    c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor='1F3864'); c.alignment=Alignment(wrap_text=True,vertical='center')
yellow=PatternFill('solid',fgColor='FFF2CC')
for i,r in enumerate(rows,start=2):
    if not r[7]: ws.cell(i,8).fill=yellow; ws.cell(i,8).value='Чекаємо відповідь керівника'
    ws.cell(i,8).alignment=Alignment(wrap_text=False)
    ws.cell(i,7).alignment=Alignment(wrap_text=True,vertical='top')
for i,w in enumerate([13,20,14,28,13,38,50,40,18,22,12]+[11]*13,start=1): ws.column_dimensions[get_column_letter(i)].width=w
ws.freeze_panes='D2'; ws.row_dimensions[1].height=32
wb.save('GUEST-POSTS-TABLE.xlsx')
print(len(rows), sum(1 for r in rows if r[7]))
