"""Assemble the drafted chapters into a book-formatted .docx AND a real PDF.

Deterministic: no LLM anywhere in the path.

Chapters are AUTO-DISCOVERED from the book folder. Ordering:

    Preface-*.md             front matter, before the introduction
    Introduction-*.md        front matter, after the preface
    Chapter-<number>-*.md    ordered numerically on <number>
    Chapter-DRAFT-*.md       placed by PLACEMENT below (drafts carry no number)

Structure of the output:
    section 1  front matter (title, copyright, contents) - deliberately unnumbered
    section 2  body, page numbering restarts at 1, footer page numbers

The contents page is built in TWO PASSES. A Word TOC field does not update itself,
so pass 1 renders the book and the PDF is read to find the page each chapter
actually lands on; pass 2 emits a static contents page with the real numbers.
Formatting is arithmetic, not guesswork.

Run with the interpreter that has python-docx:

  "$TMPDIR/ytvenv/Scripts/python.exe" "C:/ai/proposal genie/You-Are-Using-AI-Wrong/book-build/build-interior.py"

Pass a C:/ native path. MSYS paths like /c/ai/... are NOT translated for native
Windows programs and fail with "can't open file".

Source of truth is the markdown. This script only reads it. Editing the .docx,
the .pdf, or a Google Doc copy will not survive a rebuild.
"""
import os, re, subprocess

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the book folder
OUT = os.path.join(B, "book-build")
os.makedirs(OUT, exist_ok=True)

DOCX = os.path.join(OUT, "You-Are-Using-AI-Wrong-INTERIOR.docx")
PDF  = os.path.join(OUT, "You-Are-Using-AI-Wrong-INTERIOR.pdf")
SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

# Un-numbered drafts -> where they belong in the running order.
# From 00-BOOK.md section 7: the 8-Ball chapter is planned as CHAPTER 8.
PLACEMENT = {
    "Chapter-DRAFT-The-8-Ball-Never-Fooled-Anyone.md": 8,
}

SKIP = {"00-BOOK.md", "RULES.md", "CONCEPTS.md", "CONCEPT.md",
        "DASHBOARD-IMPLEMENTATION.md", "LICENSE-CONTENT",
        "Review-Grok-2026-10-11-and-EO-14434.md"}


# ------------------------------------------------------------------ discovery

def prettify(s):
    return re.sub(r"[-_]+", " ", s).strip()


def title_for(fname):
    stem = re.sub(r"\.md$", "", fname)
    m = re.match(r"^Chapter-(\d+)-(.+)$", stem)
    if m:
        return "Chapter %d \u2014 %s" % (int(m.group(1)), prettify(m.group(2)))
    m = re.match(r"^Chapter-DRAFT-(.+)$", stem)
    if m:
        return "Chapter %d \u2014 %s" % (PLACEMENT[fname], prettify(m.group(1)))
    m = re.match(r"^Preface[-_]?(.*)$", stem)
    if m:
        return "Preface: " + prettify(m.group(1)) if m.group(1) else "Preface"
    m = re.match(r"^Introduction[-_]?(.*)$", stem)
    if m:
        return "Introduction: " + prettify(m.group(1)) if m.group(1) else "Introduction"
    return prettify(stem)


def discover():
    """[(kind, filename, title)] in reading order."""
    rows = []
    for f in sorted(os.listdir(B)):
        if not f.endswith(".md") or not os.path.isfile(os.path.join(B, f)):
            continue
        if f in SKIP or f.startswith("00-"):
            continue
        if f.startswith("Preface"):
            rows.append((-2, "front", f, title_for(f)))
        elif f.startswith("Introduction"):
            rows.append((-1, "front", f, title_for(f)))
        elif f.startswith("Chapter-DRAFT-"):
            if f in PLACEMENT:
                rows.append((PLACEMENT[f], "chapter", f, title_for(f)))
        elif re.match(r"^Chapter-\d+-", f):
            rows.append((int(re.match(r"^Chapter-(\d+)-", f).group(1)), "chapter", f, title_for(f)))
    rows.sort(key=lambda r: r[0])
    return [(r[1], r[2], r[3]) for r in rows]


FILES = discover()


# ------------------------------------------------------------------ docx helpers

def add_runs(p, text):
    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            p.add_run(part[2:-2]).bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            p.add_run(part[1:-1]).italic = True
        elif part.startswith("`") and part.endswith("`"):
            r = p.add_run(part[1:-1]); r.font.name = "Consolas"; r.font.size = Pt(9.5)
        else:
            p.add_run(part)


def page_field(par):
    r = par.add_run()
    f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = "PAGE"
    f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "separate")
    t  = OxmlElement("w:t"); t.text = "1"
    f3 = OxmlElement("w:fldChar"); f3.set(qn("w:fldCharType"), "end")
    for e in (f1, it, f2, t, f3):
        r._r.append(e)


def style_page(section):
    section.page_width, section.page_height = Inches(6), Inches(9)
    section.top_margin = section.bottom_margin = Inches(0.75)
    section.left_margin = section.right_margin = Inches(0.70)
    section.header_distance = section.footer_distance = Inches(0.45)


def restart_numbering(section, start=1):
    sectPr = section._sectPr
    pg = sectPr.find(qn("w:pgNumType"))
    if pg is None:
        pg = OxmlElement("w:pgNumType"); sectPr.append(pg)
    pg.set(qn("w:start"), str(start))


def build_styles(doc):
    st = doc.styles["Normal"]
    st.font.name = "Garamond"; st.font.size = Pt(11)
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    st.paragraph_format.space_after = Pt(0)
    st.paragraph_format.first_line_indent = Inches(0.22)
    st.paragraph_format.line_spacing = 1.08
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Garamond")

    h1 = doc.styles["Heading 1"]
    h1.font.name = "Garamond"; h1.font.size = Pt(20); h1.font.bold = True
    h1.font.color.rgb = RGBColor(0, 0, 0)
    h1.paragraph_format.space_before = Pt(0); h1.paragraph_format.space_after = Pt(24)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    h2 = doc.styles["Heading 2"]
    h2.font.name = "Garamond"; h2.font.size = Pt(13); h2.font.bold = True
    h2.font.color.rgb = RGBColor(0, 0, 0)
    h2.paragraph_format.space_before = Pt(16); h2.paragraph_format.space_after = Pt(8)


def strip_author_notes(text):
    """Remove author-facing scaffolding from the READING COPY only.

    The markdown keeps every note - they are how the open flags stay visible, and
    they must not be softened (they are what makes chapters 26-28 inspectable
    records rather than claims). None of it belongs in a book interior.
    """
    NOTE_HEAD = re.compile(r"^#{1,6}\s*Notes for the author", re.I)
    lines, out, skipping = text.split("\n"), [], False
    for ln in lines:
        if NOTE_HEAD.match(ln.strip()):
            skipping = True
            continue
        if skipping:
            if re.match(r"^#{1,2}\s+\S", ln) and not NOTE_HEAD.match(ln.strip()):
                skipping = False
            else:
                continue
        s = ln.strip()
        if re.match(r"^\**STATUS:", s, re.I):
            continue
        if "TO CONFIRM" in ln:
            continue
        if re.match(r"^\*?\u26a0", s):
            continue
        out.append(ln)
    return "\n".join(out)


# ------------------------------------------------------------------ build

def build(toc_entries=None):
    """toc_entries None -> chapter list (pass 1); [(title, page)] -> real numbers (pass 2)."""
    doc = Document()
    style_page(doc.sections[0])
    build_styles(doc)

    # ---- section 1: front matter, deliberately unnumbered ----
    f = doc.sections[0].footer
    f.is_linked_to_previous = False
    for p in f.paragraphs:
        p.text = ""

    t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.first_line_indent = Inches(0)
    t.paragraph_format.space_before = Inches(2.2)
    t.add_run("YOU ARE USING AI WRONG").bold = True
    t.runs[0].font.size = Pt(26)

    sub = doc.add_paragraph(); sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.paragraph_format.first_line_indent = Inches(0)
    sub.paragraph_format.space_before = Pt(14)
    r = sub.add_run("And It Isn't Your Fault"); r.font.size = Pt(15); r.italic = True

    au = doc.add_paragraph(); au.alignment = WD_ALIGN_PARAGRAPH.CENTER
    au.paragraph_format.first_line_indent = Inches(0)
    au.paragraph_format.space_before = Pt(48)
    au.add_run("Michael C. Barnes").font.size = Pt(13)

    doc.add_page_break()

    cp = doc.add_paragraph(); cp.paragraph_format.first_line_indent = Inches(0)
    cp.paragraph_format.space_before = Inches(3.0)
    for txt in [
        "You Are Using AI Wrong \u2014 And It Isn't Your Fault",
        "Copyright \u00a9 2026 Michael C. Barnes.",
        "",
        "This work is licensed under Creative Commons Attribution-ShareAlike 4.0 International",
        "(CC BY-SA 4.0). You may share and adapt it, including commercially, provided you give",
        "appropriate credit and license your contributions under the same terms.",
        "",
        "The companion repositories are released under the MIT licence. Code and content are",
        "licensed separately and deliberately.",
        "",
        "First edition.",
    ]:
        p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Inches(0)
        p.paragraph_format.space_after = Pt(2)
        p.add_run(txt).font.size = Pt(9.5)

    doc.add_page_break()

    # ---- contents ----
    doc.add_heading("Contents", level=1).paragraph_format.space_before = Inches(0.4)
    if toc_entries is None:
        for _k, _fn, ttl in FILES:
            e = doc.add_paragraph(); e.paragraph_format.first_line_indent = Inches(0)
            e.paragraph_format.space_after = Pt(6)
            e.add_run(ttl)
    else:
        for ttl, pg in toc_entries:
            e = doc.add_paragraph(); e.paragraph_format.first_line_indent = Inches(0)
            e.paragraph_format.space_after = Pt(6)
            e.add_run(ttl)
            e.add_run("\t")
            e.add_run(str(pg))
            e.paragraph_format.tab_stops.add_tab_stop(
                Inches(4.55), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)

    # ---- section 2: body, page numbering restarts at 1 ----
    body = doc.add_section(WD_SECTION.NEW_PAGE)
    style_page(body)
    restart_numbering(body, 1)
    body.footer.is_linked_to_previous = False
    bf = body.footer.paragraphs[0]
    bf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    page_field(bf)
    for r in bf.runs:
        r.font.name = "Garamond"; r.font.size = Pt(9)

    added = []
    for n, (_kind, fname, title) in enumerate(FILES):
        path = os.path.join(B, fname)
        if not os.path.exists(path):
            print("  MISSING:", fname)
            continue
        if n:                                   # every chapter starts on a fresh page
            doc.add_page_break()
        doc.add_heading(title, level=1)
        text = strip_author_notes(open(path, encoding="utf-8").read())
        first_para = True
        for raw in text.split("\n"):
            line = raw.rstrip()
            if not line.strip():
                continue
            if re.match(r"^#{1,6}\s", line):
                hx = len(re.match(r"^(#{1,6})", line).group(1))
                doc.add_heading(re.sub(r"[*`]", "", re.sub(r"^#{1,6}\s+", "", line)).strip(),
                                level=min(hx + 1, 3))
                first_para = True
                continue
            if line.strip() in ("---", "***", "___"):
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.first_line_indent = Inches(0)
                p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(10)
                p.add_run("\u2022  \u2022  \u2022")
                first_para = True
                continue
            if line.startswith("> "):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.3)
                p.paragraph_format.right_indent = Inches(0.3)
                p.paragraph_format.first_line_indent = Inches(0)
                p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)
                add_runs(p, line[2:])
                for r in p.runs:
                    r.italic = True; r.font.size = Pt(10.5)
                first_para = True
                continue
            m = re.match(r"^\s*[-*]\s+(.*)$", line)
            if m:
                p = doc.add_paragraph(style="List Bullet")
                p.paragraph_format.first_line_indent = Inches(0)
                add_runs(p, m.group(1)); first_para = False
                continue
            m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
            if m:
                p = doc.add_paragraph(style="List Number")
                p.paragraph_format.first_line_indent = Inches(0)
                add_runs(p, m.group(2)); first_para = False
                continue
            if line.startswith("    "):
                p = doc.add_paragraph()
                p.paragraph_format.first_line_indent = Inches(0)
                p.paragraph_format.left_indent = Inches(0.25)
                r = p.add_run(line.strip()); r.font.name = "Consolas"; r.font.size = Pt(9)
                first_para = False
                continue
            p = doc.add_paragraph()
            if first_para:
                p.paragraph_format.first_line_indent = Inches(0)   # chapter opening
            add_runs(p, line)
            first_para = False
        added.append(fname)

    doc.save(DOCX)
    return added


# ------------------------------------------------------------------ render + measure

def to_pdf():
    if not os.path.exists(SOFFICE):
        return False
    prof = "file:///" + os.path.join(os.environ.get("LOCALAPPDATA", ""), "Temp", "loprofile").replace("\\", "/")
    if os.path.exists(PDF):
        os.remove(PDF)
    with open(os.path.join(OUT, "_render.log"), "w") as log:
        subprocess.run([SOFFICE, "-env:UserInstallation=" + prof, "--headless", "--norestore",
                        "--convert-to", "pdf", "--outdir", OUT, DOCX],
                       stdout=log, stderr=subprocess.STDOUT, timeout=420)
    return os.path.exists(PDF)


def measure():
    """-> (contents_page_1based, [(title, printed_page)]) or None."""
    try:
        from pypdf import PdfReader
    except ImportError:
        print("   pypdf not available in this interpreter; skipping measurement")
        return None
    r = PdfReader(PDF)

    contents_pg = None
    for i, page in enumerate(r.pages):
        if "Contents" in (page.extract_text() or ""):
            contents_pg = i + 1
            break
    if contents_pg is None:
        return None

    # body numbering restarts at 1 on the page after the contents page
    offset = contents_pg

    out = []
    norm = lambda s: re.sub(r"\s+", " ", s or "").lower()
    for _k, _fn, title in FILES:
        # Match the WHOLE heading, not just the title phrase. Chapter titles also
        # occur in running prose ("ask me anything" appears in the Preface), and a
        # partial key lands on the prose instead of the heading.
        key = norm(title)
        hit = 0
        for i in range(contents_pg, len(r.pages)):        # never match front matter
            # Normalise whitespace: the PDF text layer wraps lines, so a raw
            # substring test misses a heading that is present but split.
            top = norm(r.pages[i].extract_text())[:200]
            if key and key in top:
                hit = (i + 1) - offset
                break
        out.append((title, hit))
    return contents_pg, out


if __name__ == "__main__":
    print("pass 1 - build with the chapter list, then render to measure")
    print("   files discovered:", len(FILES))
    build(None)
    if not to_pdf():
        print("   !! LibreOffice not found or the render failed; the .docx is still written")
        print("DOCX:", DOCX)
        raise SystemExit(0)

    m = measure()
    if not m:
        print("   !! could not measure; leaving the chapter-list contents page")
        print("DOCX:", DOCX, "\nPDF :", PDF)
        raise SystemExit(0)

    contents_pg, entries = m
    missing = [t for t, p in entries if not p]
    if missing:
        print("   !! not located:", missing)
    else:
        print("pass 2 - rebuild with real page numbers (body begins after contents, front matter p%d)" % contents_pg)
        for t, p in entries:
            print("      %-46s p%d" % (t[:46], p))
        build(entries)
        to_pdf()

    print("DOCX:", DOCX)
    print("PDF :", PDF if os.path.exists(PDF) else "(not produced)")
