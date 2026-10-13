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
SKIP = {"00-BOOK.md", "RULES.md", "CONCEPTS.md", "CONCEPT.md",
        "DASHBOARD-IMPLEMENTATION.md", "LICENSE-CONTENT",
        "Review-Grok-2026-10-11-and-EO-14434.md",
        # working documents. They do not match "Chapter-*" today, so discovery already
        # passes them by - listed anyway, because a rename is all it would take, and this
        # project has already printed author notes into the manuscript once.
        "START-HERE.md", "WORKFLOW.md", "OPEN-ITEMS.md", "RULES-AUDIT.md",
        "OUTLINE-RECONCILIATION.md", "SESSION-RECORD-2026-10-11.md",
        "STATUS.md", "README.md", "AGENT-CONTRACT.md", "Tool-Evaluation-AIWriteBook.md"}


# ------------------------------------------------------------------ discovery

def prettify(s):
    return re.sub(r"[-_]+", " ", s).strip()


def title_for(fname):
    stem = re.sub(r"\.md$", "", fname)
    m = re.match(r"^Chapter-(\d+)-(.+)$", stem)
    if m:
        return "Chapter %d \u2014 %s" % (int(m.group(1)), prettify(m.group(2)))
    m = re.match(r"^Part[-_]0*(\d+)[-_](.*)$", stem)
    if m:
        return "Part %s \u2014 %s" % (int(m.group(1)), prettify(m.group(2)))
    m = re.match(r"^Preface[-_]?(.*)$", stem)
    if m:
        return "Preface: " + prettify(m.group(1)) if m.group(1) else "Preface"
    m = re.match(r"^Introduction[-_]?(.*)$", stem)
    if m:
        return "Introduction: " + prettify(m.group(1)) if m.group(1) else "Introduction"
    m = re.match(r"^Reader-Guide[-_]?(.*)$", stem)
    if m:
        return "Reader's Guide: " + prettify(m.group(1)) if m.group(1) else "Reader's Guide"
    return prettify(stem)


SHADOWED = []          # chapter numbers claimed twice; the root wins, and we say so


AUTHOR_MARKER = re.compile(
    r"^\s*(?:\*\*|\*)?\s*(?:[\u26a0\ufe0f]|STATUS\s*:|NOTE\s*:|TODO\s*:|\*\()", re.I | re.M)

def extract_draft(text):
    """-> the chapter prose, or None if this is not a chapter yet.

    The skeletons carry the plan spec, the concept and the evidence as REFERENCE
    material. None of that belongs in the book, so once the author writes under
    '## DRAFT' the build reads that section and nothing else.

    A skeleton whose DRAFT section is still the placeholder is NOT a chapter, and
    returns None so the caller skips it. Otherwise including chapters/ would put
    twenty-three empty chapter headings in the manuscript.

    ⚑ 12 Oct 2026 - a chapter's own author notes PRINTED IN THE MANUSCRIPT as though
    they were the chapter, because the placeholder check below only matched an *italic
    parenthetical* and this note had been written as bold text. The build cannot tell
    good prose from scaffolding, so it no longer tries to: a DRAFT section that OPENS
    with an author-facing marker is not a chapter. Skips are reported by
    unfilled_skeletons() rather than being silent, because the whole failure was that
    nobody could see it.
    """
    m = re.search(r"(?m)^##\s+DRAFT\s*$", text)
    if not m:
        return text                                  # a real chapter file: use it whole
    body = re.sub(r"(?s)^\s*\*\(.*?\)\*", "", text[m.end():])
    if AUTHOR_MARKER.match(body):
        return None                                  # scaffolding, not prose
    body = body.strip()
    return body or None


def unfilled_skeletons():
    """[(title, words)] - skeletons holding notes under ## DRAFT instead of prose.

    Reported on every build. These are the files where an author note could leak into
    the reading copy, so the count is printed whether or not anything is wrong.
    """
    out = []
    for kind, fname, title in FILES:
        p = os.path.join(B, fname)
        if not os.path.exists(p):
            continue
        text = open(p, encoding="utf-8").read()
        m = re.search(r"(?m)^##\s+DRAFT\s*$", text)
        if not m or extract_draft(text) is not None:
            continue
        tail = re.sub(r"(?s)^\s*\*\(.*?\)\*", "", text[m.end():]).strip()
        if not tail:
            continue                      # a plain unfilled skeleton: expected, not a warning
        out.append((title, len(tail.split())))
    return out


def discover():
    """[(kind, filename, title)] in reading order.

    Scans the book root AND chapters/. A chapter found in the root wins, because
    the root holds promoted chapters and chapters/ holds the skeletons. Filenames
    come back relative to the book folder, so a path like
    'chapters/Chapter-02-x.md' resolves correctly when the content is read.
    """
    found = {}

    def consider(relpath, f):
        if not f.endswith(".md") or f in SKIP or f.startswith("00-"):
            return
        if f.startswith("Preface"):
            key, sortkey, kind = "front-preface", -2, "front"
        elif f.startswith("Introduction"):
            key, sortkey, kind = "front-intro", -1, "front"
        elif f.startswith("Reader-Guide"):
            key, sortkey, kind = "front-guide", -0.5, "front"
        elif f.startswith("Chapter-DRAFT-"):
            if f not in PLACEMENT:
                return
        m = re.match(r"^Part-0*(\d+)-", f)
        if m:
            n = int(m.group(1))
            key, sortkey, kind = "part-%d" % n, n - 0.5, "part"
            if key not in found:
                found[key] = (sortkey, kind, relpath, title_for(f))
            return
        m = re.match(r"^Chapter-(\d+)-", f)
        if not m:
            return
        key, sortkey, kind = "ch-%d" % int(m.group(1)), int(m.group(1)), "chapter"
        if key not in found:                 # root scanned first, so root wins
            found[key] = (sortkey, kind, relpath, title_for(f))
        else:
            SHADOWED.append((key, relpath, found[key][2]))

    for f in sorted(os.listdir(B)):
        if os.path.isfile(os.path.join(B, f)):
            consider(f, f)
    subdir = os.path.join(B, "chapters")
    if os.path.isdir(subdir):
        for f in sorted(os.listdir(subdir)):
            full = os.path.join(subdir, f)
            if os.path.isfile(full) and not f.startswith("_"):
                # _folded/ and any underscore-prefixed file is retired material,
                # not a chapter. Its content lives in the chapter that absorbed it.
                consider("chapters/" + f, f)

    return [(r[1], r[2], r[3]) for r in sorted(found.values(), key=lambda r: r[0])]


FILES = discover()


def buildable():
    """The entries that will actually become chapters — those with prose written.

    Discovery returns every file it can see, including the unfilled skeletons in
    chapters/. This filters to the ones that have something to print, and must be
    used for BOTH the body and the contents placeholder, or the contents lists
    chapters that are not in the book.
    """
    out = []
    for kind, fname, title in FILES:
        p = os.path.join(B, fname)
        if not os.path.exists(p):
            continue
        if extract_draft(open(p, encoding="utf-8").read()) is None:
            continue
        out.append((kind, fname, title))
    return out


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
        for k, _fn, ttl in buildable():
            e = doc.add_paragraph(); e.paragraph_format.first_line_indent = Inches(0)
            e.paragraph_format.space_after = Pt(6)
            r = e.add_run(ttl)
            if k == "part":
                r.bold = True
                e.paragraph_format.space_before = Pt(10)
    else:
        kind_by_title = {t: k for k, _f, t in FILES}
        for ttl, pg in toc_entries:
            e = doc.add_paragraph(); e.paragraph_format.first_line_indent = Inches(0)
            e.paragraph_format.space_after = Pt(6)
            r = e.add_run(ttl)
            if kind_by_title.get(ttl) == "part":
                r.bold = True
                e.paragraph_format.space_before = Pt(10)
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

    added, skipped = [], []
    for n, (_kind, fname, title) in enumerate(buildable()):
        path = os.path.join(B, fname)
        if not os.path.exists(path):
            print("  MISSING:", fname)
            continue
        body_text = extract_draft(open(path, encoding="utf-8").read())
        if body_text is None:                   # a skeleton with no prose written yet
            skipped.append(title)
            continue
        if n:                                   # every chapter starts on a fresh page
            doc.add_page_break()
        if _kind == "part":
            # A part divider: a full-page break already happened; render it centered
            # and larger, as a section title rather than a chapter heading.
            h = doc.add_heading(title, level=1)
            for r in h.runs:
                r.font.size = Pt(20)
        else:
            doc.add_heading(title, level=1)
        text = strip_author_notes(body_text)
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


def measure(only=None):
    """-> (offset, [(title, printed_page)]) or None.

    `only` is the list of filenames actually written into the document. Without it
    this would try to locate the skeleton entries too, report them all missing, and
    skip the page-number pass on a book that is perfectly fine.

    The printed page number is derived from where the FIRST chapter's heading
    actually lands, not from the Contents page. Counting from the Contents page
    fails silently the moment the contents runs to two pages, which shifts every
    number in the book by one.
    """
    try:
        from pypdf import PdfReader
    except ImportError:
        print("   pypdf not available in this interpreter; skipping measurement")
        return None
    r = PdfReader(PDF)

    norm = lambda s: re.sub(r"\s+", " ", s or "").lower()

    def top_of(i):
        return norm(r.pages[i].extract_text())[:200]     # headings sit at the top

    def find(title, start_page):
        """1-based pdf page carrying this heading at the top, or 0.

        start_page is 1-based, matching the page numbers this function returns;
        searching begins ON that page, not after it.
        """
        key = norm(title)
        if not key:
            return 0
        for i in range(max(0, start_page - 1), len(r.pages)):
            # Match the WHOLE heading: chapter titles also occur in running prose
            # ("ask me anything" appears in the Preface), and a partial key lands
            # on the prose instead of the heading.
            if key in top_of(i):
                return i + 1
        return 0

    entries = [(t, f) for _k, f, t in FILES if only is None or f in only]
    if not entries:
        return None

    # The first heading appears at least twice: once in the contents list and once
    # on its own page. The body begins on its own page, so take the LAST occurrence.
    # (Counting from "the page after the contents" breaks as soon as the contents
    # runs to two pages, and matching "Contents" anywhere in the text catches body
    # prose that happens to use the word.)
    key0 = norm(entries[0][0])
    pages_with_first = [i + 1 for i in range(len(r.pages)) if key0 and key0 in top_of(i)]
    if not pages_with_first:
        return None
    first_pg = pages_with_first[-1]
    offset = first_pg - 1          # that page is printed page 1

    out = []
    for title, _f in entries:
        pg = find(title, first_pg)
        out.append((title, (pg - offset) if pg else 0))
    return offset, out


if __name__ == "__main__":
    print("pass 1 - build with the chapter list, then render to measure")
    print("   files discovered:", len(FILES))
    unfilled = unfilled_skeletons()
    if unfilled:
        print("   skeletons holding notes under '## DRAFT' rather than prose: %d" % len(unfilled))
        for title, words in unfilled[:6]:
            print("      - %s  (%d words of notes, not printed)" % (title, words))
        if len(unfilled) > 6:
            print("      ... and %d more" % (len(unfilled) - 6))
        print("      (their notes stay in the markdown and are NOT built into the book)")
    if SHADOWED:
        print("   !! chapter numbers claimed twice - the root file wins in each case:")
        for key, shadowed, kept in SHADOWED:
            print("      %s : keeping %s, ignoring %s" % (key, kept, shadowed))
        print("      (settle the numbering, or one of these chapters is not in the book)")
    added = build(None)
    if not to_pdf():
        print("   !! LibreOffice not found or the render failed; the .docx is still written")
        print("DOCX:", DOCX)
        raise SystemExit(0)

    m = measure(added)
    if not m:
        print("   !! could not measure; leaving the chapter-list contents page")
        print("DOCX:", DOCX, "\nPDF :", PDF)
        raise SystemExit(0)

    offset, entries = m
    pages = [p for _t, p in entries]
    problems = []
    if any(p <= 0 for p in pages):
        problems.append("some chapters were not located: %s" % [t for t, p in entries if not p])
    if pages and pages[0] != 1:
        problems.append("the first chapter should be p1, measured p%d" % pages[0])
    if pages != sorted(pages):
        problems.append("page numbers are not in reading order: %s" % pages)

    if problems:
        print("   !! the page measurement looks wrong, so the contents keeps the chapter list")
        for pr in problems:
            print("      " + pr)
        print("DOCX:", DOCX, "\nPDF :", PDF)
        raise SystemExit(0)

    print("pass 2 - rebuild with real page numbers (front matter spans %d page(s))" % offset)
    for t, p in entries:
        print("      %-46s p%d" % (t[:46], p))
    build(entries)
    to_pdf()

    print("DOCX:", DOCX)
    print("PDF :", PDF if os.path.exists(PDF) else "(not produced)")
