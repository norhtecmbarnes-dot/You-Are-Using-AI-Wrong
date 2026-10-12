# book-build — the interior pipeline

Assembles the drafted chapters into a book-formatted `.docx`. **No LLM anywhere in this path** — it is a
script reading markdown and writing Word XML. Re-runnable in seconds, as often as you like.

---

## The decision this folder implements

**The markdown is the master. Google Docs is the reading copy and the proof.**

    book folder\*.md          <- SOURCE OF TRUTH. everything is edited here
    book-build\build-interior.py
    book-build\...INTERIOR.docx      <- generated. never edit it
    your Google Doc                  <- a proof copy. never edit it

**Edits made in the `.docx` or in the Google Doc do not survive a rebuild.** If you change a chapter in
Docs and the markdown still says the old thing, the next build silently reverts you. That is the one way
this pipeline can bite, so: **changes come back as words, not as edits in the output.**

    you tell me the change  ->  I edit the markdown  ->  I rebuild  ->  you re-upload

---

## How to run it

```bash
cd "$LOCALAPPDATA/Temp"
"ytvenv/Scripts/python.exe" "C:/ai/proposal genie/You-Are-Using-AI-Wrong/book-build/build-interior.py"
```

Two things that will trip you up, both already hit once:

- **Use a `C:/` path, not `/c/ai/...`.** MSYS paths are not translated for native Windows programs. A
  `/c/...` path fails with `can't open file`.
- **Use that interpreter.** `python-docx` is installed in `$LOCALAPPDATA/Temp/ytvenv`, not in the system
  Python and not in Hermes' own.

Output:

    book-build\You-Are-Using-AI-Wrong-INTERIOR.docx

---

## Adding a chapter

**Drop the file in the book folder. That is the whole procedure.** The script auto-discovers:

    Preface-*.md             front matter, before the introduction
    Introduction-*.md        front matter, after the preface
    Chapter-<number>-*.md    ordered numerically on <number>
    Chapter-DRAFT-*.md       placed by the PLACEMENT map at the top of the script

Chapter 2 currently comes from a draft file, so it is in `PLACEMENT`:

```python
PLACEMENT = {
    "Chapter-DRAFT-The-8-Ball-Never-Fooled-Anyone.md": 2,
}
```

When that chapter gets a properly numbered filename, delete its `PLACEMENT` entry and it will be found by
the normal rule.

**`RULES.md`, `CONCEPTS.md`, `00-BOOK.md`, `DASHBOARD-IMPLEMENTATION.md` and `LICENSE-CONTENT` are skipped.**
They are planning material, not book content. To change that, edit `SKIP` in the script.

---

## What the build produces

    6 x 9 in trim          0.75in top/bottom, 0.70in sides — trade paperback, not letter
    Garamond 11pt          justified, indented paragraphs, chapter openings un-indented
    Heading 1 per chapter, Heading 2/3 inside chapters
    centered * * *          for markdown horizontal rules
    title page             "YOU ARE USING AI WRONG / And It Isn't Your Fault"
    copyright page         CC BY-SA 4.0, with the MIT/code split stated
    live TOC field         updates in Word and on Docs import
    footer page numbers    as a Word PAGE field

---

## What it cannot do

⚠️ **No EPUB.** `python-docx` cannot produce one, and neither can Google Docs.

⚠️ **No print bleed, spine width or barcode clear zone.** Those are press requirements. The spine is
computable from the page count and paper stock, but it is a separate step and it changes once the page
count is final.

**So the last stage is still separate** — once the manuscript is whole:

    EPUB            Pandoc, or Calibre
    print interior  a real typesetter, or AIWriteBook's importer on the finished .docx

**AIWriteBook is worth saving for the end**: its manuscript import is free the first time, its formatting
step exists on every tier, and it will not give you a partial-draft refund if you spend the free import
early. Import once, when the book is done.

---

## Where this stands

    27 chapters planned
     7 written    Preface, Introduction, Ch 1, the Ch 2 draft, Ch 26, Ch 27, Ch 28
    20 missing
    ~5,600 words of a 40,000-50,000 word target

**Get the wordcount up before polishing the formatting.** The script rebuilds in seconds, so there is no
cost to formatting a moving manuscript — but there is no benefit either, and every re-upload to Docs
overwrites the last proof copy.
