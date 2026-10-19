"""home-draft.html -> wp-page.html: самодостатній блок для вставки в WordPress.
Усі стилі ізольовані під #kr, щоб тема/Elementor не ламали верстку."""
import re, base64, sys

src = open('home-draft.html', encoding='utf-8').read()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)

def scope(sel):
    out = []
    for s in sel.split(','):
        s = s.strip()
        if s == ':root' or s == 'body':
            out.append('#kr')
        elif s == 'html':
            return None
        elif s == '*':
            out.append('#kr *')
        else:
            out.append('#kr ' + s)
    return ','.join(out)

def parse(css):
    res, i = [], 0
    while i < len(css):
        j = css.find('{', i)
        if j < 0: break
        head = css[i:j].strip()
        depth, k = 1, j + 1
        while depth:
            c = css[k]
            depth += (c == '{') - (c == '}')
            k += 1
        body = css[j + 1:k - 1]
        if head.startswith('@media'):
            res.append(f'{head}{{{parse(body)}}}')
        else:
            sel = scope(head)
            if sel: res.append(f'{sel}{{{body}}}')
        i = k
    return ''.join(res)

scoped = parse(css)
scoped = scoped.replace('.page{', '.kr-wrap{').replace('#kr .page{', '#kr .kr-wrap{')

reset = """
body.page-id-1901 .entry-title,body.page-id-1901 .page-title,body.page-id-1901 .page-header{display:none!important}
html{scroll-behavior:smooth}
body{overflow-x:hidden}
#kr{width:100vw;max-width:none;position:relative;left:50%;margin-left:-50vw;margin-top:0;margin-bottom:0;padding:0;text-align:left;display:block;float:none;min-height:100vh}
#kr,#kr *,#kr *::before,#kr *::after{box-sizing:border-box}
#kr h1,#kr h2,#kr h3,#kr p,#kr ul,#kr li,#kr div,#kr details,#kr summary{margin:0;padding:0;border:0;text-transform:none;letter-spacing:normal;float:none}
#kr h1,#kr h2,#kr h3{font-family:var(--serif)!important;font-weight:600!important;line-height:1.1;letter-spacing:-.012em;color:inherit;word-break:normal}
#kr p,#kr li,#kr a,#kr span,#kr small,#kr b,#kr summary{font-family:var(--sans)}
#kr ul{list-style:none}
#kr a{color:inherit;text-decoration:none;box-shadow:none;border-bottom:0}
#kr a:hover,#kr a:focus{color:inherit;text-decoration:none}
#kr img{max-width:100%;height:auto;border:0;box-shadow:none}
#kr nav a,#kr .bar a{white-space:nowrap}
#kr .btn,#kr .btn:hover{text-decoration:none}
"""
# відновлюємо специфічні правила після reset (reset стоїть ПЕРЕД scoped з тією ж специфічністю → scoped перемагає за порядком)
body = re.search(r'<body>(.*?)</body>', src, re.S).group(1)
body = body.replace('<div class="page">', '<div class="kr-wrap">')

for n in ('portrait-suit', 'portrait-office'):
    b = base64.b64encode(open(f'img/{n}.jpg', 'rb').read()).decode()
    body = body.replace(f'img/{n}.jpg', f'data:image/jpeg;base64,{b}')

head = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@500;600;700&display=swap&subset=cyrillic" rel="stylesheet">
'''
ld = re.search(r'<script type="application/ld\+json">.*?</script>', src, re.S).group(0)
open('wp-page.html', 'w', encoding='utf-8').write(f'{head}{ld}\n<style>{reset}{scoped}</style>\n<div id="kr">{body}</div>')
print(len(scoped))
