"""text-fixed.txt -> text-fixed.docx (Title/Description + H1/H2/H3, списки, таблиці).
Запуск: python3 make_docx.py <папка-статті> '<tables json>' '<extra_h3 json>'"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "jurist-online.info/blog-drafts"))
import convert
from docx import Document
d = pathlib.Path(sys.argv[1])
tables = [tuple(x) for x in json.loads(sys.argv[2])]
h3 = tuple(json.loads(sys.argv[3]))
meta, h1, toc, blocks = convert.parse((d / "text-fixed.txt").read_text(encoding="utf-8"), tables=tables, extra_h3=h3)
doc = Document()
doc.add_paragraph("Title: " + meta["title"]); doc.add_paragraph("Description: " + meta["desc"])
doc.add_heading(h1, 1)
n = 0
for kind, v in blocks:
    if kind != "oli": n = 0
    if kind == "p": doc.add_paragraph(v)
    elif kind == "h2": doc.add_heading(v, 2)
    elif kind == "h3": doc.add_heading(v, 3)
    elif kind == "li": doc.add_paragraph(v, style="List Bullet")
    elif kind == "oli":
        n += 1; doc.add_paragraph(f"{n}. {v}")
    elif kind == "table":
        t = doc.add_table(rows=len(v), cols=len(v[0])); t.style = "Table Grid"
        for i, r in enumerate(v):
            for j, c in enumerate(r): t.cell(i, j).text = c
doc.save(d / "text-fixed.docx")
