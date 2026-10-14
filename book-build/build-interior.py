"""Assemble the book interior into a real .docx AND .pdf.

Deterministic: no LLM anywhere in the path. Source of truth is the markdown
in the book folder and chapters/; editing the .docx, .pdf or a Google Doc copy
will not survive a rebuild.

v2 — 14 October 2026. What changed from v1, and why:

  READER-COPY CLEANING. The drafted chapters carry their verification apparatus
  in the same files as the prose: trailing "*Verification: ...*" provenance
  blocks, "## The rules this chapter carries" mapping sections, register-narration
  sentences inside the scholarly footnotes, and process-flag paragraphs. v1
  shipped all of it. v2 strips it from the READING COPY ONLY - the markdown keeps
  every note. Every dropped block is logged to book-build/_interior-drops.md so
  the process record lives outside the book (and on GitHub) for anyone who wants it.

  THE RULES PAGE IS IN THE BOOK. v1 had RULES.md in the SKIP list while 00-BOOK.md
  section 7 places the rules page inside the book as front matter ("four pieces
  before Chapter 1"). That is the trap the book's own build notes warn about: a
  skip keyed on file name, not on outline placement, drops the book's most-copied
  page and reports nothing. RULES.md is now emitted as front matter, after the
  Reader's Guide, with its author-facing "Placement note" section stripped here.

  REAL TABLES. Markdown tables become native Word tables (Table Grid, header row
  bold) - formattable in any word processor. v1 had no table branch: pipe rows
  printed as literal text.

  REAL FOOTNOTES. [^N] definitions become a "Source notes" section at the end of
  their chapter; inline [^N] markers become superscripts. The notes keep the
  citation and its honest grade (working paper, not peer-reviewed, self-reported)
  and lose only the session-narration (what the chapter says, what the register
  holds, re-check before print). Those sentences are process - they exist in this
  repo's registers and do not belong in a book a stranger reads.

  PART DIVIDERS IN THE RIGHT PLACE. v1 sorted Part-N at N - 0.5, which put
  Part 2 between chapters 1 and 2. Placement now comes from the outline
  (00-BOOK.md section 7): Part I opens at Ch. 1, Part II at Ch. 11, Part III at
  Ch. 16, Part IV at Ch. 24, Part V at Ch. 28. A part divider whose chapter range
  holds no drafted prose is skipped and reported (Part V now - Ch. 28-29 are not
  drafted yet), so the interior never ends on an empty part page.

  NO DOUBLE HEADINGS. Drafted chapters carry their own "# Chapter N - Title" line
  and v1 printed the discovered title AND the in-file heading. The in-file H1 is
  now dropped when it matches the discovered title.

Structure of the output:
  section 1  front matter (title, copyright, contents) - deliberately unnumbered
  section 2  body, page numbering restarts at 1, footer page numbers

The contents page is built in TWO PASSES (a Word TOC field does not update under
a headless render): pass 1 renders, the PDF is read for the page each heading
lands on, pass 2 rebuilds with real numbers. The numbers are validated against a
monotonic reading-order invariant before they are used; on any failure the build
falls back to the plain chapter list rather than print numbers it does not
believe.

Run with the interpreter that has python-docx and pypdf (this repo uses the
TMPDIR/ytvenv venv) and pass C:/-style native paths.
"""
import os, re, subprocess
from collections import OrderedDict

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
DROPS_LOG = os.path.join(OUT, "_interior-drops.md")
SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

# Working documents. They do not match the discovery patterns today - listed
# anyway, because a rename is all it would take. RULES.md was here in v1 and
# that was wrong: the outline places it in the book. Do not add it back.
SKIP = {"00-BOOK.md", "CONCEPTS.md", "CONCEPT.md",
        "DASHBOARD-IMPLEMENTATION.md", "LICENSE-CONTENT",
        "Review-Grok-2026-10-11-and-EO-14434.md",
        "START-HERE.md", "WORKFLOW.md", "OPEN-ITEMS.md", "RULES-AUDIT.md",
        "OUTLINE-RECONCILIATION.md", "SESSION-RECORD-2026-10-11.md",
        "STATUS.md", "README.md", "AGENT-CONTRACT.md", "Tool-Evaluation-AIWriteBook.md"}

# Part dividers live before their first chapter, per the outline (00-BOOK.md
# section 7): Part I opens at Ch. 1, Part II at Ch. 11, Part III at Ch. 16,
# Part IV at Ch. 24, Part V at Ch. 28. Re-check this table whenever the outline
# is reconciled - the outline is the authority, not file order.
PART_FIRST = {1: 1, 2: 11, 3: 16, 4: 24, 5: 28}

# Where the reading copy of a file ends - the region after this anchor is
# working material and stays out of the interior. Documented per instance.
DROP_FROM = {
    # Ch. 27's draft ends on the bookend line. Everything after - the unfolded
    # "Start here (folded from the retired Chapter 27 skeleton)" plan tail, the
    # verbatim outline structural notes, and the plan-echo of the close - is
    # scaffolding. Whether the payoff material lands here or in Ch. 29 is the
    # author's open editorial call (STATUS.md open item 15).
    "chapters/Chapter-27-You-Have-Something-to-Lose.md":
        "## Start here (folded from the retired Chapter 27 skeleton",
    # The Introduction's tail is a working note to the author: cross-reference
    # decisions about the predecessor book and its listing metadata. The
    # garbled-text argument inside it is candidate prose, flagged to the author
    # in the drop log - moving it into the book is his call, not the build's.
    "Introduction-AI-Is-Already-Smart-Enough.md":
        "**One thing to decide.**",
}

# Individual paragraphs dropped for cause the generic rules cannot express.
DROP_PARAS = {
    "⚑ The exact size varies by model and product":
        "truncated apparatus fragment (ends mid-sentence) in Ch. 4",
}

# Session-vocabulary: a sentence containing one of these is process narration,
# not book prose. Kept as data so the reading copy can be audited. Deliberately
# narrow on the "supplied" family: the book itself teaches "compare the answer
# with the SUPPLIED evidence" (reader-supplied material - thesis vocabulary),
# so only the session-voice constructions are matched, never the bare phrase.
PROCESS_VOCAB = [
    "00-BOOK", "CONCEPTS.md", "CONCEPT.md", "DASHBOARD-IMPLEMENTATION", "RULES-AUDIT",
    "the register", "register's", "outline/register", "per the register",
    "the outline", "the skeleton", "the retired", "skeleton's",
    "re-check before print", "before print", "pre-publication verification",
    "verified this session", "this session",
    "git history", "open items",
    "not supplied", "cannot be reproduced", "cannot be expanded",
    "cannot be supplied", "cannot be audited", "was not included",
    "the supplied evidence does not", "the supplied material does not",
    "the supplied record does not", "the supplied ledger", "the supplied project ledger",
    "the supplied verification record", "the supplied chapter material",
    "does not include the run's",
    "kept verbatim", "the author's own ⚠", "the chapter's ⚠",
    "the chapter says", "the chapter itself says", "the chapter reports only",
    "not asserted in the", "not cited here", "the honest register",
    "the chapter's two ⚠", "the chapter's three ⚠", "the chapter's four ⚠",
    "the paste said", "the paste titled", "corrected to match the source",
    "the register row", "adopted verbatim", "the author's prose is", "Verification:",
    "one-word edit", "are the author's own", "are my own",
]

GLYPH_RE = re.compile(r"[⚑⚠]\ufe0f?")

DROPS = {"blocks": [], "paras": [], "sentences": [], "notes": [], "glyphs": 0}


def vocab_hit(s):
    low = s.lower()
    return any(v.lower() in low for v in PROCESS_VOCAB)


# ------------------------------------------------------------------ discovery

def prettify(s):
    return re.sub(r"[-_]+", " ", s).strip()

def title_for(fname):
    stem = re.sub(r"\.md$", "", fname)
    if stem == "RULES":
        return "The Rules"
    m = re.match(r"^Chapter-(\d+)-(.+)$", stem)
    if m:
        return "Chapter %d \u2014 %s" % (int(m.group(1)), prettify(m.group(2)))
    m = re.match(r"^Part[-_]0*(\d+)[-_](.*)$", stem)
    if m:
        return "Part %d \u2014 %s" % (int(m.group(1)), prettify(m.group(2)))
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
    r"^\s*(?:\*\*|\*)?\s*(?:[⚠]|STATUS\s*:|NOTE\s*:|TODO\s*:|\*\()", re.I | re.M)

def extract_draft(text):
    """-> the chapter prose, or None if this is not a chapter yet."""
    m = re.search(r"(?m)^##\s+DRAFT\s*$", text)
    if not m:
        return text                                    # a drafted chapter: read whole
    body = re.sub(r"(?s)^\s*\*\(.*?\)\*", "", text[m.end():])
    if AUTHOR_MARKER.match(body):
        return None                                    # scaffolding, not prose
    return body.strip() or None


def discover():
    """[(kind, filename, title)] in reading order. The root wins a number claimed
    twice; chapters/ holds the skeletons. Front matter order follows the outline:
    Preface, Introduction, Reader's Guide, The Rules. Parts sit before their
    first chapter per PART_FIRST."""
    found = {}

    def add(key, sortkey, kind, relpath, title):
        if key not in found:
            found[key] = (sortkey, kind, relpath, title)
        elif kind == "chapter":
            pass

    def consider(relpath, f):
        if not f.endswith(".md") or f in SKIP or f.startswith("00-"):
            return
        if f == "RULES.md":
            add("front-rules", -0.4, "front", relpath, title_for(f)); return
        if f.startswith("Preface"):
            add("front-preface", -2, "front", relpath, title_for(f)); return
        if f.startswith("Introduction"):
            add("front-intro", -1, "front", relpath, title_for(f)); return
        if f.startswith("Reader-Guide"):
            add("front-guide", -0.5, "front", relpath, title_for(f)); return
        m = re.match(r"^Part-0*(\d+)-", f)
        if m:
            n = int(m.group(1))
            add("part-%d" % n, PART_FIRST[n] - 0.5, "part", relpath, title_for(f)); return
        m = re.match(r"^Chapter-(\d+)-", f)
        if not m:
            return
        n = int(m.group(1))
        key = "ch-%d" % n
        if key not in found:                           # root scanned first: root wins
            found[key] = (n, "chapter", relpath, title_for(f))
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
                # _folded/ and any underscore-prefixed file is retired material
                consider("chapters/" + f, f)

    return [(r[1], r[2], r[3]) for r in sorted(found.values(), key=lambda r: r[0])]


FILES = discover()


def has_prose(relpath):
    p = os.path.join(B, relpath)
    if not os.path.exists(p):
        return False
    return extract_draft(open(p, encoding="utf-8").read()) is not None


def buildable():
    """Entries that will actually print - used for the body AND the contents."""
    out = []
    for i, (kind, fname, title) in enumerate(FILES):
        if kind == "part":
            n = int(re.match(r"Part (\d+)", title).group(1))
            first = PART_FIRST[n]
            nxt = [PART_FIRST[k] for k in PART_FIRST if PART_FIRST[k] > first]
            last = min(nxt) - 1 if nxt else 10 ** 6
            if not any(has_prose(fn) for k, fn, t in FILES
                       if k == "chapter" and first <= int(re.match(r"Chapter (\d+)", t).group(1)) <= last):
                DROPS["blocks"].append((fname, "part divider skipped - no drafted chapter in its range (Ch. %d-%d)" % (first, last)))
                continue
        if not has_prose(fname):
            continue
        out.append((kind, fname, title))
    return out


def unfilled_skeletons():
    """[(title, words)] - skeletons holding notes under ## DRAFT instead of prose."""
    out = []
    for kind, fname, title in FILES:
        p = os.path.join(B, fname)
        if not os.path.exists(p):
            continue
        text = open(p, encoding="utf-8").read()
        m = re.search(r"(?m)^##\s+DRAFT\s*$", text)
        if not m or extract_draft(text) is not None:
            continue
        tail = re.sub(r"(?s)^\s*\(.*?\)\*", "", text[m.end():]).strip()
        tail = re.sub(r"(?s)^\s*\*\(.*?\)\*", "", tail).strip()
        if not tail:
            continue                       # plain unfilled skeleton: expected
        out.append((title, len(tail.split())))
    return out


# ------------------------------------------------------- reader-copy cleaning

def cut_from(text, anchor, fname):
    i = text.find(anchor)
    if i == -1:
        return text
    dropped = text[i:]
    DROPS["blocks"].append((fname, "working-material tail dropped at %r (%d chars)" % (anchor[:60], len(dropped))))
    return text[:i]


def drop_metadata_sections(lines, fname):
    """Remove sections whose heading is build apparatus, wherever they appear."""
    out, i, n = [], 0, len(lines)
    while i < n:
        s = lines[i]
        if re.match(r"^(#{1,3})\s+(The rules this chapter carries|Structural notes)\b.*$", s):
            label = s.strip()[:60]
            j = i + 1
            while j < n and not re.match(r"^#{1,3}\s", lines[j]) and lines[j].strip() != "---":
                j += 1
            size = sum(len(x) for x in lines[i:j])
            DROPS["blocks"].append((fname, "apparatus section dropped: %r (%d chars)" % (label, size)))
            i = j
            continue
        out.append(lines[i]); i += 1
    return out


def split_sentences(s):
    parts = re.split(r"(?<=[.!?;])\s+", s)
    return [p for p in parts if p.strip()]


def clean_sentence_stream(text, fname, where):
    """Sentence-level process-vocabulary filter. Returns cleaned text."""
    keep, dropped = [], []
    for sent in split_sentences(text):
        if vocab_hit(sent):
            dropped.append(sent.strip())
        else:
            keep.append(sent.strip())
    if dropped:
        DROPS["sentences"].append((fname, where, " ".join(dropped)[:160]))
    return " ".join(keep).strip()


def clean_footnote_def(line, rest_lines, fname):
    """Merge a [^N]: definition with its indented continuation, then clean it."""
    num = int(re.match(r"\[\^(\d+)\]:", line).group(1))
    body = [re.sub(r"^\[\^\d+\]:\s*", "", line)]
    body += [l.strip() for l in rest_lines]
    text = " ".join(x for x in body if x)
    return num, text


FOOTNOTE_SPLIT = re.compile(r"(?m)^\[\^(\d+)\]:\s*(.*)$")


def process_footnotes(lines, fname):
    """Pull [^N]: definitions out of the body flow, clean them, keep order.
    Returns (flow_lines, [(num, text)]) - entries keep their citation facts and
    honest grades; session narration is dropped at sentence level."""
    flow, entries, i, n = [], [], 0, len(lines)
    while i < n:
        m = FOOTNOTE_SPLIT.match(lines[i])
        if m:
            rest = []
            j = i + 1
            while j < n and lines[j].strip() and not re.match(r"^\[\^\d+\]:", lines[j]) \
                    and not re.match(r"^#{1,3}\s", lines[j]) and not re.match(r"^[-*]\s|\d+\.\s", lines[j]):
                rest.append(lines[j]); j += 1
            num, text = clean_footnote_def(lines[i], rest, fname)
            kept = clean_sentence_stream(GLYPH_RE.sub("", text).replace("**", "").replace("*", ""),
                                         fname, "footnote [%d]" % num)
            if kept:
                entries.append((num, kept))
            else:
                DROPS["notes"].append((fname, "footnote [%d]: only process narration; dropped entire note" % num))
            i = j
            continue
        flow.append(lines[i]); i += 1
    return flow, entries


PARA_START_MARKER = re.compile(r"^\s*(?:\*\*)?\s*[⚠⚑]\ufe0f?\s*")

def is_plain_paragraph(block):
    """A plain prose block - every line is flowing text, not a heading, table
    row, quote, list item or code block. Only plain paragraphs go through the
    sentence-level filter: honest content inside ledger entries ('What
    happened: ...') and list items is structure, not narration, and survives."""
    for l in block:
        s = l.strip()
        if not s:
            continue
        if s.startswith(("#", "|", ">", "    ", "- ", "* ")) or re.match(r"^\d+\.\s", s):
            return False
    return True


def clean_body_paragraphs(lines, fname):
    """Paragraph pass over the body flow:
    - STATUS:/TO CONFIRM paragraphs: dropped whole
    - plain paragraphs: sentence-level session-vocabulary filter (markers or not);
      glyph stripped from surviving text
    - DROP_PARAS per-instance removals"""
    out, i, n = [], 0, len(lines)
    while i < n:
        if lines[i].strip() == "":
            out.append(lines[i]); i += 1; continue
        j = i
        while j < n and lines[j].strip() != "":
            j += 1
        block = lines[i:j]
        s0 = block[0].strip()
        if re.match(r"^\**\s*STATUS\s*:", s0, re.I) or "TO CONFIRM" in " ".join(block):
            DROPS["paras"].append((fname, "(process marker paragraph) " + " ".join(x.strip() for x in block)[:160]))
            i = j; continue
        if any(s0.startswith(k) for k in DROP_PARAS):
            DROPS["paras"].append((fname, "(per-instance) " + s0[:160]))
            i = j; continue
        first = block[0].strip()
        joined_plain = " ".join(x.strip() for x in block)
        is_marker = bool(PARA_START_MARKER.match(first)) or first.startswith("*(") or \
                    (first.startswith("**") and vocab_hit(first))
        if (is_marker or vocab_hit(joined_plain)) and is_plain_paragraph(block):
            joined = " ".join(x.strip().lstrip("*") for x in block)
            kept = clean_sentence_stream(GLYPH_RE.sub("", joined), fname, "paragraph")
            if kept:
                out.append(kept)
            else:
                DROPS["paras"].append((fname, "(apparatus paragraph) " + joined[:160]))
            i = j; continue
        out.extend(block); i = j
    return out


def cut_verification_tail(text, rel):
    """Drop the trailing italic provenance block ('*Verification: ...*') that the
    drafting sessions append AFTER the chapter's prose. This is the book's
    single largest piece of reading-copy scaffolding: every drafted chapter
    carries one, each runs to end-of-file, and each is pure session narration
    (what was adopted verbatim, what the register holds). The markdown keeps
    it; the interior drops it."""
    last = None
    for m in re.finditer(r"(?m)^\*?\(?\s*Verification:\s?", text):
        last = m
    if last:
        dropped = text[last.start():]
        DROPS["blocks"].append((rel, "trailing provenance block dropped: %d chars from %r" %
                                (len(dropped), dropped.strip()[:60])))
        return text[:last.start()]
    return text


def cut_leading_italic_note(lines, rel):
    """Drop a leading italic '*( ... )*' provenance block immediately after a
    front-matter file's own heading (the Reader's Guide's head note). Only when
    the block is provenance-shaped (it names the working documents or the
    adoption), so a legitimate italic aside can never be caught by this."""
    i = next((k for k, l in enumerate(lines) if l.startswith("# ")), None)
    if i is None:
        return lines
    k = i + 1
    while k < len(lines) and not lines[k].strip():
        k += 1
    if k < len(lines) and lines[k].lstrip().startswith("*("):
        j = k
        while j < len(lines) and not lines[j].rstrip().endswith(")*"):
            j += 1
        if j < len(lines):
            block = " ".join(x.strip("*( )") for x in lines[k:j+1])
            if vocab_hit(block) or "adopted" in block.lower():
                DROPS["blocks"].append((rel, "leading italic provenance block dropped after the heading: %r" % block[:70]))
                return lines[:k] + lines[j+1:]
    return lines


def clean(fname, text):
    """The full reading-copy pipeline for one file. The markdown is untouched."""
    rel = fname.replace(os.sep, "/")
    # 0. per-file working-tail cuts (documented in DROP_FROM)
    for key, anchor in DROP_FROM.items():
        if rel == key:
            text = cut_from(text, anchor, rel)
    # 1. the trailing '*Verification: ...*' provenance block (all drafted chapters)
    text = cut_verification_tail(text, rel)
    lines = text.split("\n")
    # 2. front matter leading-italic note (after the file's own H1)
    if rel.startswith(("Preface", "Introduction", "Reader-Guide", "RULES")):
        lines = cut_leading_italic_note(lines, rel)
    # 3. metadata sections
    lines = drop_metadata_sections(lines, rel)
    lines = "\n".join(lines).split("\n")
    # 4. footnotes out of the flow
    lines, notes = process_footnotes(lines, rel)
    lines = "\n".join(lines).split("\n")
    # 5. paragraph pass
    lines = clean_body_paragraphs(lines, rel)
    return "\n".join(lines), notes


def dedupe_own_h1(lines, title):
    """If the file's first non-blank line is the chapter's own H1, drop it -
    the build emits the discovered title as Heading 1 (no double heading)."""
    norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
    for i, l in enumerate(lines):
        if not l.strip():
            continue
        if l.lstrip().startswith("# "):
            if norm(l) == norm(title):
                return lines[:i] + lines[i+1:]
        break
    return lines


# ------------------------------------------------------------------ docx helpers

TOKEN = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\[\^\d+\])")

def add_runs(p, text, size=None):
    for part in TOKEN.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = p.add_run(part[1:-1]); r.italic = True
        elif part.startswith("`") and part.endswith("`"):
            r = p.add_run(part[1:-1]); r.font.name = "Consolas"; r.font.size = Pt(size or 9.5)
        elif re.fullmatch(r"\[\^(\d+)\]", part):
            r = p.add_run(part[2:-1]); r.font.superscript = True
        else:
            r = p.add_run(part)
        if size:
            r.font.size = Pt(size)


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


def md_table(doc, rows):
    """Render a markdown table block as a native Word table (formattable)."""
    header = rows[0]
    ncol = len(header)
    table = doc.add_table(rows=len(rows), cols=ncol)
    try:
        table.style = "Table Grid"
    except KeyError:
        pass
    table.autofit = True
    for ri, row in enumerate(rows):
        for ci in range(ncol):
            cell = table.cell(ri, ci)
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.first_line_indent = Inches(0)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_runs(p, row[ci] if ci < len(row) else "", size=9)
            if ri == 0:
                for r in p.runs:
                    r.bold = True
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def parse_table_line(l):
    s = l.strip()
    s = re.sub(r"^\|", "", s); s = re.sub(r"\|$", "", s)
    return [c.strip() for c in s.split("|")]


def is_table_row(l):
    s = l.strip()
    return s.startswith("|") and s.endswith("|")


def is_table_sep(l):
    s = l.strip()
    return bool(re.fullmatch(r"\|(\s*:?-{3,}:?\s*\|)+", s))


def emit_source_notes(doc, notes):
    doc.add_heading("Source notes", level=2)
    for num, text in notes:
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Inches(0)
        p.paragraph_format.left_indent = Inches(0.3)
        p.paragraph_format.space_after = Pt(6)
        add_runs(p, "%d. %s" % (num, text), size=9.5)


def emit_line(doc, line, state):
    """The markdown->book furniture mapper for one line."""
    if re.match(r"^\[\^\d+\]:", line):            # handled by footnote pass
        return
    if re.match(r"^#{1,6}\s", line):
        hx = len(re.match(r"^(#{1,6})", line).group(1))
        doc.add_heading(GLYPH_RE.sub("", re.sub(r"[*`]", "", re.sub(r"^#{1,6}\s+", "", line)).strip()),
                        level=min(hx + 1, 3))
        state["first_para"] = True
        return
    if line.strip() in ("---", "***", "___"):
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.first_line_indent = Inches(0)
        p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(10)
        p.add_run("\u2022  \u2022  \u2022")
        state["first_para"] = True
        return
    if line.startswith("> "):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.3); p.paragraph_format.right_indent = Inches(0.3)
        p.paragraph_format.first_line_indent = Inches(0)
        p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)
        add_runs(p, line[2:])
        for r in p.runs:
            r.italic = True; r.font.size = Pt(10.5)
        state["first_para"] = True
        return
    indent = len(line) - len(line.lstrip())
    m = re.match(r"^\s*[-*]\s+(.*)$", line)
    if m:
        p = doc.add_paragraph(style="List Bullet")
        lvl = 0 if indent == 0 else (1 if indent <= 3 else 2)
        if lvl:
            p.paragraph_format.left_indent = Inches(0.25 * lvl + 0.25)
        p.paragraph_format.first_line_indent = Inches(0)
        add_runs(p, GLYPH_RE.sub("", m.group(1)))
        state["first_para"] = False
        return
    m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
    if m:
        p = doc.add_paragraph(style="List Number")
        p.paragraph_format.first_line_indent = Inches(0)
        add_runs(p, GLYPH_RE.sub("", m.group(2)))
        state["first_para"] = False
        return
    if line.startswith("    ") and not is_table_row(line):
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Inches(0)
        p.paragraph_format.left_indent = Inches(0.25)
        r = p.add_run(line.strip()); r.font.name = "Consolas"; r.font.size = Pt(9)
        state["first_para"] = False
        return
    p = doc.add_paragraph()
    if state["first_para"]:
        p.paragraph_format.first_line_indent = Inches(0)   # chapter opening
    add_runs(p, GLYPH_RE.sub("", line))
    state["first_para"] = False


def build(toc_entries=None):
    """toc_entries None -> chapter list (pass 1); [(title, page)] -> numbers."""
    doc = Document()
    style_page(doc.sections[0])
    build_styles(doc)

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

    # ---- section 2: body ----
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
        raw = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if raw is None:
            print("  MISSING:", fname); continue
        body_text = extract_draft(raw)
        if body_text is None:
            skipped.append(title)
            continue
        if n:
            doc.add_page_break()
        if _kind == "part":
            h = doc.add_heading(title, level=1)
            for r in h.runs:
                r.font.size = Pt(20)
        else:
            doc.add_heading(title, level=1)
        text, notes = clean(fname, body_text)
        norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
        flines = dedupe_own_h1(text.split("\n"), title)
        state = {"first_para": True}
        i = 0
        while i < len(flines):
            line = flines[i]
            if is_table_row(line):
                block = []
                while i < len(flines) and is_table_row(flines[i]):
                    block.append(parse_table_line(flines[i])); i += 1
                rows = [r for r in block if not is_table_sep("|" + "|".join(r) + "|")]
                if rows:
                    md_table(doc, rows)
                state["first_para"] = True
                continue
            emit_line(doc, GLYPH_RE.sub("", line), state)
            i += 1
        if notes:
            emit_source_notes(doc, sorted(notes))
        added.append(fname)

    doc.save(DOCX)
    return added, skipped


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
    try:
        from pypdf import PdfReader
    except ImportError:
        print("   pypdf not available in this interpreter; skipping measurement")
        return None
    r = PdfReader(PDF)
    norm = lambda s: re.sub(r"\s+", " ", s or "").lower()

    PAGE_NO = re.compile(r"^\d+\s+")

    def top_of(i):
        # The footer page number is extracted BEFORE the heading on body pages
        # ("1 preface: why this book exists ..."), so strip a leading number
        # before prefix-matching the heading.
        return PAGE_NO.sub("", norm(r.pages[i].extract_text())[:210])

    def find(title, start_page):
        """1-based pdf page whose TOP 200 chars BEGIN with this heading, or 0.
        Prefix matching is deliberate: a substring match placed The Rules on the
        Reader's Guide's own page, because the Guide's top-of-page prose contains
        the phrase 'the rules page'. A heading sits at the START of its page."""
        key = norm(title)
        if not key:
            return 0
        for i in range(max(0, start_page - 1), len(r.pages)):
            if top_of(i).startswith(key):
                return i + 1
        return 0

    entries = [(t, f) for _k, f, t in FILES if only is None or f in only]
    if not entries:
        return None

    key0 = norm(entries[0][0])
    pages_with_first = [i + 1 for i in range(len(r.pages))
                        if top_of(i).startswith(key0)]
    if not pages_with_first:
        return None
    first_pg = pages_with_first[-1]
    offset = first_pg - 1

    out = []
    for title, _f in entries:
        pg = find(title, first_pg)
        out.append((title, (pg - offset) if pg else 0))
    return offset, out


def write_drops_log():
    lines = ["# Interior-build drop log", "",
             "*Generated by `book-build/build-interior.py` on the reading copy only -",
             "the markdown source keeps everything.*", ""]
    if not any(DROPS[k] for k in DROPS):
        lines.append("(nothing was dropped - the reading copy matched the source)")
    if DROPS["blocks"]:
        lines += ["## Whole blocks and tails dropped", ""]
        for fname, why in DROPS["blocks"]:
            lines.append("- `%s` - %s" % (os.path.basename(fname), why))
        lines.append("")
    if DROPS["paras"]:
        lines += ["## Paragraphs dropped (process/apparatus)", ""]
        for fname, txt in DROPS["paras"]:
            lines.append("- `%s` - %s" % (os.path.basename(fname), txt))
        lines.append("")
    if DROPS["notes"]:
        lines += ["## Footnotes dropped whole", ""]
        for fname, why in DROPS["notes"]:
            lines.append("- `%s` - %s" % (os.path.basename(fname), why))
        lines.append("")
    if DROPS["sentences"]:
        lines += ["## Sentences dropped (session narration) - keepers of the citation apparatus", ""]
        for fname, where, txt in DROPS["sentences"]:
            lines.append("- `%s` (%s) - \u2026%s" % (os.path.basename(fname), where, txt))
        lines.append("")
    open(DROPS_LOG, "w", encoding="utf-8", newline="\n").write("\n".join(lines))


if __name__ == "__main__":
    print("pass 1 - build with the chapter list, then render to measure")
    print("   files discovered:", len(FILES))
    print("   discovered order (reading order; anything with no prose cannot print):")
    buildable_set = {(k, f) for k, f, _t in buildable()}
    for kind, fn, ttl in FILES:
        in_book = (kind, fn) in buildable_set
        print("      %-6s %-46s%s" % (kind, ttl[:46], "" if in_book else "   (not in book yet: no prose)"))
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

    added, skipped = build(None)
    print("   printed %d files; %d skeleton(s) had no prose and were skipped honestly" % (len(added), len(skipped)))
    for s in skipped:
        print("      skipped (no prose):", s)

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
        problems.append("some sections were not located: %s" % [t for t, p in entries if not p])
    if pages and pages[0] != 1:
        problems.append("the first front-matter piece should be p1, measured p%d" % pages[0])
    if pages != sorted(pages):
        problems.append("page numbers are not in reading order: %s" % pages)

    if problems:
        print("   !! the page measurement looks wrong, so the contents keeps the plain list")
        for pr in problems:
            print("      " + pr)
        print("DOCX:", DOCX, "\nPDF :", PDF)
        raise SystemExit(0)

    print("pass 2 - rebuild with real page numbers (front matter unnumbered, body spans after %d physical page(s))" % offset)
    for t, p in entries:
        print("      %-46s p%d" % (t[:46], p))
    build(entries)
    to_pdf()
    write_drops_log()
    n_dropped = sum(len(DROPS[k]) for k in ("blocks", "paras", "notes", "sentences"))
    print("   reading-copy cleaning: %d block(s)/paragraph(s)/sentence(s)/note(s) dropped - %s" % (
        n_dropped, os.path.basename(DROPS_LOG)))
    print("DOCX:", DOCX)
    print("PDF :", PDF if os.path.exists(PDF) else "(not produced)")