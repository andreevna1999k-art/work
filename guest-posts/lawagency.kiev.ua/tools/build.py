"""md (статья) -> HTML для Google Doc и колонки «Контент для розміщення».
Использование: python3 build.py article.md [--body]   (--body: без H1, для CSV/таблицы)
Печатает в stdout HTML; в stderr: знаков без пробелов, слов, H2, ссылок."""
import re,sys
p=sys.argv[1]; body='--body' in sys.argv
lines=[l for l in open(p,encoding='utf-8').read().split('\n') if l.strip()]
out=[];inl=False;tbl=False
for l in lines:
    if l.startswith('|'):
        cells=[c.strip() for c in l.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-+:?',c) for c in cells): continue
        if not tbl: out.append('<table border="1">'); tbl=True; tag='th'
        else: tag='td'
        out.append('<tr>'+''.join('<%s>%s</%s>'%(tag,c,tag) for c in cells)+'</tr>'); continue
    if tbl: out.append('</table>'); tbl=False
    l=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<a href="\2">\1</a>',l)
    if l.startswith('- '):
        if not inl: out.append('<ul>'); inl=True
        out.append('<li>%s</li>'%l[2:]); continue
    if inl: out.append('</ul>'); inl=False
    if l.startswith('# '):
        if not body: out.append('<h1>%s</h1>'%l[2:])
    elif l.startswith('### '): out.append('<h3>%s</h3>'%l[4:])
    elif l.startswith('## '): out.append('<h2>%s</h2>'%l[3:])
    else: out.append('<p>%s</p>'%l)
if inl: out.append('</ul>')
if tbl: out.append('</table>')
h='\n'.join(out); print(h)
plain=re.sub(r'<[^>]+>','',h)
sys.stderr.write('chars_no_spaces=%d words=%d h2=%d links=%d\n'%(len(re.sub(r'\s','',plain)),len(plain.split()),h.count('<h2>'),h.count('<a ')))
