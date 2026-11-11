#!/usr/bin/env python3
"""Конвертер тексту статті (text-fixed.txt) у HTML для сторінки блогу."""
import re, html

def esc(s): return html.escape(s, quote=False)
def inline(s):
    s = esc(s)
    return s

TABLES = {  # ключ: (перший рядок шапки, стовпців, рядків разом із шапкою)
    1: [("Спосіб", 5, 6)],
    2: [("Куди", 4, 6)],
    3: [("Ситуація", 4, 6), ("Критерій", 3, 6)],
    4: [("Спосіб", 5, 6)],
}
H3_RE = re.compile(r"^(Справа\b.*№|Правова позиція: справа|Що каже закон$|Що зробити сьогодні:?$|Алгоритм дій$|Які документи підготувати$|Зразок (заяви кредитодавцю|документа)$|Куди звертатися далі$|Чи можуть Вас притягнути за несплату такого кредиту$|Якщо Ви самі ввели код із SMS$|Крок \d\. .{0,70}$)")
SAMPLE_STARTS = ("Кому:", "Від:", "Претензія щодо", "Відповідно до ст. 203 та 215", "Додатки:", "Дата: [")

def split_inline(line):
    """Розбиває «довгий» рядок на логічні фрагменти: ('p',txt) / ('li',txt) / ('table',rows)."""
    out = []
    # markdown-таблиця
    m = re.search(r"\|\s*Період\s*\|.*?1300 грн\s*\|", line)
    if m:
        pre, tab, post = line[:m.start()], m.group(0), line[m.end():]
        rows = [r for r in re.split(r"\|\s+\|", tab.strip().strip("|")) ]
        rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
        rows = [r for r in rows if not all(set(c) <= set(":- ") for c in r)]
        out += split_inline(pre.strip()) if pre.strip() else []
        out.append(("table", rows))
        out += split_inline(post.strip()) if post.strip() else []
        return out
    for key in ("Умовний приклад зростання боргу.", "Розрахунок:", "Поки Ви не знаєте", "Як захиститися від мікрозаймів?", "Перевірте себе:", "Тест на готовність до спору"):
        pass
    parts = re.split(r"\s\*\s", line)
    if len(parts) > 1:
        first = parts[0].strip()
        if first: out += paragraphs(first)
        items = parts[1:]
        for k, it in enumerate(items):
            it = it.strip()
            if k == len(items) - 1:
                mm = re.search(r"(?<=[а-яіїєґ0-9\)»%])\.\s+(?=[А-ЯІЇЄҐ])", it)
                if mm and mm.start() < 70 and not it.startswith("«"):
                    out.append(("li", it[:mm.start()+1].strip()))
                    out += paragraphs(it[mm.end():].strip())
                    continue
            out.append(("li", it))
        return out
    return paragraphs(line)

def paragraphs(s):
    # додаткові розриви абзаців за маркерами
    marks = ["Умовний приклад зростання боргу.", "Розрахунок:", "Поки Ви не знаєте", "Як захиститися від мікрозаймів?", "Тест на готовність до спору", "Спірні ситуації:", "У моїй практиці був випадок"]
    pos = sorted({s.find(m) for m in marks if s.find(m) > 0})
    res, prev = [], 0
    for p in pos:
        res.append(s[prev:p].strip()); prev = p
    res.append(s[prev:].strip())
    return [("p", x) for x in res if x]

def parse(txt, n=None, tables=None, extra_h3=()):
    txt = txt.replace("копії документів. Закон, суд, я: спірні питання\n", "копії документів. \nЗакон, суд, я: спірні питання\n")
    lines = [l.rstrip() for l in txt.split("\n")]
    meta = {"title": lines[0].replace("Title:", "").strip(), "desc": lines[1].replace("Description:", "").strip()}
    h1 = lines[2].strip()
    body_lines = lines[3:]
    # TOC -> H2 список
    ti = next(i for i, l in enumerate(body_lines) if l.strip() == "Зміст")
    toc = []
    j = ti + 1
    while j < len(body_lines) and re.match(r"\s+\d+\.\s", body_lines[j]):
        toc.append(re.sub(r"^\s+\d+\.\s", "", body_lines[j]).strip()); j += 1
    intro = [l for l in body_lines[:ti] if l.strip()]
    rest = body_lines[j:]
    h2set = {t for t in toc}
    h2set |= {"Висновок юриста", "Висновок юриста і що зробити сьогодні", "FAQ", "Підсумок"}
    blocks = []  # (kind, data)
    for l in intro:
        for b in split_inline(l.strip()): blocks.append(b)
    i = 0
    tabs = tables if tables is not None else TABLES.get(n, [])
    section = None
    while i < len(rest):
        raw = rest[i]; l = raw.strip(); i += 1
        if not l: continue
        # таблиці по рядках
        hit = next((t for t in tabs if l == t[0] and i + t[1]*t[2] - 1 <= len(rest)), None)
        if hit and (section is not None):
            nc, nr = hit[1], hit[2]
            cells = [rest[i-1+k].strip() for k in range(nc*nr)]
            # перевірка: наступний рядок після таблиці не порожній і не частина клітинок
            rows = [cells[r*nc:(r+1)*nc] for r in range(nr)]
            blocks.append(("table", rows)); i += nc*nr - 1
            continue
        if l in h2set and len(l) < 120:
            if any(b == ("h2", l) for b in blocks): l = "Підсумок"
            section = l; blocks.append(("h2", l)); continue
        if section == "FAQ" and l.endswith("?") and len(l) < 150:
            blocks.append(("h3", l)); continue
        if (l in extra_h3 or H3_RE.match(l)) and len(l) < 120:
            blocks.append(("h3", l.rstrip(":"))); continue
        m = re.match(r"^[•◦]\s+(.*)$", l)
        if m: blocks.append(("li", m.group(1).strip())); continue
        m = re.match(r"^\d+\.\s+(.*)$", l)
        if m and raw.startswith(" "): blocks.append(("oli", m.group(1).strip())); continue
        if re.match(r"^\d\.\s+Крок \d\.", l):
            # крок в одному рядку з іншими
            pass
        # алгоритм у одному абзаці (стаття 1)
        if n == 1 and l.startswith("Щоб дізнатися, чи взято на мене мікрозайм, дійте за п’ятьма кроками."):
            pre, steps = l.split("кроками.", 1)
            blocks.append(("p", pre.strip() + " кроками."))
            sp = re.split(r"\s(?=\d\.\s*Крок \d\.)", steps.strip())
            for s in sp:
                s = re.sub(r"^\d\.\s*", "", s.strip())
                if not s: continue
                if "Зразок вимоги:" in s:
                    a, b = s.split("Зразок вимоги:", 1)
                    blocks.append(("oli", a.strip()))
                    q = b.strip().strip("«»")
                    q = re.sub(r"\s(Від:|Прошу|Дата:|Підпис:)", r"\n\1", q)
                    blocks.append(("quote", [x.strip() for x in q.split("\n")]))
                elif s.startswith("Крок 5.") and " У моїй практиці" in s:
                    a, b = s.split(" У моїй практиці", 1)
                    blocks.append(("oli", a.strip())); blocks.append(("p", "У моїй практиці" + b))
                else:
                    blocks.append(("oli", s))
            continue
        if l.startswith(SAMPLE_STARTS) and n == 4:
            # блок зразка заяви
            q = [l]
            while i < len(rest) and rest[i].strip() and (rest[i].strip().startswith(SAMPLE_STARTS) or True) and not rest[i].strip() in h2set:
                q.append(rest[i].strip()); i += 1
            blocks.append(("quote", q)); continue
        for b in split_inline(l): blocks.append(b)
    return meta, h1, toc, blocks

def render(blocks):
    out, i = [], 0
    n = 0
    def flush_list(kind, items):
        tag = "ol" if kind == "oli" else "ul"
        return f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>"
    while i < len(blocks):
        k, d = blocks[i]
        if k in ("li", "oli"):
            items = []
            while i < len(blocks) and blocks[i][0] == k: items.append(blocks[i][1]); i += 1
            out.append(flush_list(k, items)); continue
        if k == "h2":
            n += 1; out.append(f'<h2 id="s{n}">{inline(d)}</h2>')
        elif k == "h3": out.append(f"<h3>{inline(d)}</h3>")
        elif k == "p": out.append(f"<p>{inline(d)}</p>")
        elif k == "quote": out.append("<blockquote>" + "".join(f"<p>{inline(x)}</p>" for x in d) + "</blockquote>")
        elif k == "table":
            head, rows = d[0], d[1:]
            t = "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>"
            out.append('<div class="art-table">' + t + "</div>")
        i += 1
    return "\n".join(out)

if __name__ == "__main__":
    import sys, pathlib
    for n, d in enumerate(["01-yak-diznatysia-chy-vziato-na-mene-mikrozaim","02-shcho-robyty-iakshcho-na-tebe-oformyly-mikrozaim","03-chy-mozhut-oformyty-kredyt-bez-moho-vidoma","04-yak-zakhystytysia-vid-kredytnykh-shakhraiv"], 1):
        txt = (pathlib.Path(__file__).parent / d / "text-fixed.txt").read_text(encoding="utf-8")
        meta, h1, toc, blocks = parse(txt, n)
        print("=====", n, h1, "| blocks", len(blocks))
        for b in blocks:
            s = b[1] if isinstance(b[1], str) else f"<{len(b[1])} rows/lines>"
            print("  ", b[0], "|", s[:90])
