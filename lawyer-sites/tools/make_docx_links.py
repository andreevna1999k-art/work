"""payload (HTML із посиланнями на закони) -> text-fixed-links.docx (Title/Description, H1, H2/H3, списки, таблиці, цитати, ГІПЕРПОСИЛАННЯ).
Запуск: python3 make_docx_links.py <payload.json> <out.docx>"""
import sys, json, re
from bs4 import BeautifulSoup, NavigableString
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import RGBColor

def add_link(par, url, text):
    part = par.part
    rid = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    st = OxmlElement("w:rStyle"); st.set(qn("w:val"), "Hyperlink"); rpr.append(st)
    c = OxmlElement("w:color"); c.set(qn("w:val"), "1155CC"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    r.append(rpr); t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t); h.append(r)
    par._p.append(h)

def fill(par, node):
    for ch in node.children:
        if isinstance(ch, NavigableString): par.add_run(str(ch))
        elif ch.name == "a": add_link(par, ch.get("href"), ch.get_text())
        else: fill(par, ch)

payload = json.load(open(sys.argv[1], encoding="utf-8"))
html = payload["content"]; meta = payload.get("meta", {})
soup = BeautifulSoup(html, "html.parser")
body = soup.select_one("div.art-body")
h1 = soup.find("h1").get_text()
doc = Document()
doc.add_paragraph("Title: " + meta.get("_yoast_wpseo_title", "")); doc.add_paragraph("Description: " + meta.get("_yoast_wpseo_metadesc", ""))
doc.add_heading(h1, 1)
for el in body.children:
    if isinstance(el, NavigableString): continue
    n = el.name
    if n in ("figure", "nav", "script", "style") or "art-toc" in (el.get("class") or []): continue
    if n == "p": fill(doc.add_paragraph(), el)
    elif n in ("h2", "h3"):
        p = doc.add_heading("", int(n[1])); fill(p, el)
    elif n == "ul":
        for li in el.find_all("li", recursive=False): fill(doc.add_paragraph(style="List Bullet"), li)
    elif n == "ol":
        for i, li in enumerate(el.find_all("li", recursive=False), 1):
            p = doc.add_paragraph(f"{i}. "); fill(p, li)
    elif n == "blockquote":
        for q in el.find_all("p"): fill(doc.add_paragraph(style="Quote"), q)
    elif n == "div" and el.find("table"):
        tb = el.find("table"); rows = tb.find_all("tr")
        t = doc.add_table(rows=len(rows), cols=len(rows[0].find_all(["th", "td"]))); t.style = "Table Grid"
        for i, r in enumerate(rows):
            for j, c in enumerate(r.find_all(["th", "td"])): fill(t.cell(i, j).paragraphs[0], c)
doc.save(sys.argv[2])
