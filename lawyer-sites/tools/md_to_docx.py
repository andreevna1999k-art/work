"""Markdown (з read_file_content Google Docs) -> docx: заголовки, списки, **жирний**, таблиці, [посилання](url).
Запуск: python3 md_to_docx.py in.md out.docx"""
import sys, re
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_link(par, url, text):
    rid = par.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), "1155CC"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    r.append(rpr); t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t); h.append(r); par._p.append(h)

def unesc(s): return re.sub(r"\\(.)", r"\1", s)
TOK = re.compile(r"(\*\*.+?\*\*|\[[^\]]+\]\([^)]+\))")
def inline(par, s, bold=False):
    for part in TOK.split(s):
        if not part: continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            r = par.add_run(unesc(part[2:-2])); r.bold = True
        elif part.startswith("["):
            m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part)
            add_link(par, m.group(2), unesc(m.group(1)))
        else:
            r = par.add_run(unesc(part)); r.bold = bold or None

def main(src, out):
    doc = Document(); lines = open(src, encoding="utf-8").read().split("\n"); i = 0
    while i < len(lines):
        l = lines[i].rstrip()
        if not l.strip(): i += 1; continue
        m = re.match(r"^(#{1,3})\s+(.*)$", l)
        if m:
            h = doc.add_heading("", len(m.group(1))); inline(h, m.group(2).replace("**", "")); i += 1; continue
        if l.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells if c): rows.append(cells)
                i += 1
            rows = [r for r in rows if any(r)]
            if rows:
                t = doc.add_table(rows=len(rows), cols=max(len(r) for r in rows)); t.style = "Table Grid"
                for a, r in enumerate(rows):
                    for b, c in enumerate(r): inline(t.cell(a, b).paragraphs[0], c)
            continue
        m = re.match(r"^\s*[-•]\s+(.*)$", l)
        if m: inline(doc.add_paragraph(style="List Bullet"), m.group(1)); i += 1; continue
        m = re.match(r"^\s*(\d+)\\?\.\s+(.*)$", l)
        if m: inline(doc.add_paragraph(f"{m.group(1)}. "), m.group(2)); i += 1; continue
        inline(doc.add_paragraph(), l); i += 1
    doc.save(out)
if __name__ == "__main__": main(sys.argv[1], sys.argv[2])
