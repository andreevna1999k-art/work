"""Сторінка WordPress (будь-який шаблон) -> docx з гіперпосиланнями: Title/Description, H1, H2/H3, списки, таблиці, цитати.
Запуск: python3 make_docx_generic.py <payload.json> <out.docx>   (payload: {"content": raw html, "meta": {...}})"""
import sys, json, re
from bs4 import BeautifulSoup, NavigableString, Tag
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_link(par, url, text):
    rid = par.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    st = OxmlElement("w:rStyle"); st.set(qn("w:val"), "Hyperlink"); rpr.append(st)
    c = OxmlElement("w:color"); c.set(qn("w:val"), "1155CC"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    r.append(rpr); t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t); h.append(r); par._p.append(h)

def fill(par, node):
    for ch in node.children:
        if isinstance(ch, NavigableString):
            s = re.sub(r"\s+", " ", str(ch))
            if not par.text and not par._p.xpath("./w:hyperlink"): s = s.lstrip()
            if s: par.add_run(s)
        elif ch.name == "a" and ch.get("href"): add_link(par, ch["href"], ch.get_text())
        elif ch.name == "br": par.add_run(" ")
        else: fill(par, ch)

BAD = ("nav", "header", "footer", "aside", "script", "style", "form", "button", "noscript", "svg")
def bad(el):
    for p in [el] + list(el.parents):
        if getattr(p, "name", None) in BAD: return True
        cls = " ".join(p.get("class") or []) if isinstance(p, Tag) else ""
        if re.search(r"(toc|breadcrumb|crumbs|cta-band|ctabox|share|related|menu)", cls): return True
    return False

def main(src, out):
    pl = json.load(open(src, encoding="utf-8")); html = pl["content"]; meta = pl.get("meta", {})
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    doc = Document()
    mt = re.search(r"<title>(.*?)</title>", html, re.S); md = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    title = meta.get("_yoast_wpseo_title") or meta.get("rank_math_title") or meta.get("_mbx_t") or (mt.group(1).strip() if mt else "")
    desc = meta.get("_yoast_wpseo_metadesc") or meta.get("rank_math_description") or meta.get("_mbx_d") or meta.get("_esv_d") or (md.group(1).strip() if md else "")
    doc.add_paragraph("Title: " + title); doc.add_paragraph("Description: " + desc)
    doc.add_heading(h1.get_text(" ", strip=True) if h1 else "", 1)
    seen = set(); started = h1 is None
    for el in soup.find_all(True):
        if el is h1: started = True; continue
        if not started or el.name not in ("h2", "h3", "p", "ul", "ol", "table", "blockquote"): continue
        if bad(el): continue
        if el.name == "p" and el.get_text(strip=True).startswith("←"): continue
        if "art-back" in " ".join((el.parent.get("class") or [])) if el.parent else False: continue
        if any(id(p) in seen for p in el.parents): continue   # уже оброблено як вкладене
        seen.add(id(el))
        if el.name in ("h2", "h3"): fill(doc.add_heading("", int(el.name[1])), el)
        elif el.name == "p":
            if el.find_parent("li") or el.find_parent("td") or el.find_parent("th"): continue
            if el.get_text(strip=True): fill(doc.add_paragraph(), el)
        elif el.name == "blockquote":
            for q in el.find_all("p") or [el]: fill(doc.add_paragraph(style="Quote"), q)
        elif el.name == "ul":
            for li in el.find_all("li", recursive=False): fill(doc.add_paragraph(style="List Bullet"), li)
        elif el.name == "ol":
            for i, li in enumerate(el.find_all("li", recursive=False), 1):
                p = doc.add_paragraph(f"{i}. "); fill(p, li)
        elif el.name == "table":
            rows = el.find_all("tr")
            if not rows: continue
            t = doc.add_table(rows=len(rows), cols=max(len(r.find_all(["th", "td"])) for r in rows)); t.style = "Table Grid"
            for i, r in enumerate(rows):
                for j, c in enumerate(r.find_all(["th", "td"])): fill(t.cell(i, j).paragraphs[0], c)
    doc.save(out)

if __name__ == "__main__": main(sys.argv[1], sys.argv[2])
