# Status — where this book is

**Last updated:** 11 October 2026
**Read this after `README.md`.** Everything here is measured from the files, not recalled.

---

## The one-line state

**The thinking is essentially complete. The drafting is not.**

    27 chapters planned
     4 exist as prose           Preface, Introduction, Ch 1, Ch 8
    25 have starting markdown   chapters/ — spec + concept + evidence, ready to expand
    12 concepts captured        CONCEPTS.md
    21 rules + 5 subrules      RULES.md   (1b skills aren't knowledge; 3b instruct in its universe;
                                          12b date it; 12c whitelist the source; 14b verify by criticality)
    21 evidence entries         verified, in 00-BOOK.md section 9
    ⚠️  3 of 25 skeletons         have their "rules this chapter carries" filled in.
                                 22 still hold the placeholder. The template says every
                                 chapter carries at least one rule, so this is a real gap —
                                 and it is the SAME defect Chapter 15 had: an unfilled
                                 field nobody had looked at. Filling it needs a judgement
                                 per chapter (concepts do not map 1:1 to rules), so it is
                                 done one at a time and confirmed, not bulk-written.

**And the controls are now installable** — the book is not only an argument:

    AGENT-CONTRACT.md   the rules as a contract in three parts + a prompt to paste
    control/SKILL.md    the same rules as a loadable agent skill
    control/references/the-rules.md   the full 22-rule register the skill draws on

Installed here as the skill `ai-usage-contract`. See README for what each is for.

---

## Where prose goes

**The build reads the book root AND `chapters/`.** Both work.

    Chapter-NN-slug.md  in the book root     the drafted chapters live here
    chapters/Chapter-NN-slug.md             written UNDER a '## DRAFT' heading

**From a skeleton, only the text under `## DRAFT` reaches the book.** The plan spec, the concept and the
evidence in the same file are reference material and are ignored. A skeleton with nothing under DRAFT is
skipped, so unfilled files cannot put empty chapter headings in the manuscript.

**If two files claim the same chapter number, the build keeps the one in the root and prints a warning.** It
does not resolve the collision silently — an unnoticed dropped chapter is exactly the failure this book is
about. At the time of writing it is warning about chapters 26 and 27.

---

## The plan — 27 chapters, four parts

`00-BOOK.md` section 7 is the outline, and it carries its own status on every chapter:
**✍️ drafted · 📋 captured · ⬜ planned.**

    Front      Preface — Why This Book Exists                        ✍️  drafted
    Front      Introduction — AI Is Already Smart Enough             ✍️  drafted

    Part I    1  Ask me anything                                     ✍️  drafted
              2  It cannot tell you it's unsure                      📋  captured
              3  Why it got worse on purpose                         📋  captured
              4  You cannot teach it anything                        📋  captured
              5  A bigger model does not fix this                    📋  captured
              6  The clock is always running                         📋  captured
              7  Activity is not work                                📋  captured
              8  The 8-Ball never fooled anyone                      ✍️  drafted
              9  It will not set you free                            📋  captured

    Part II   10 A function, not a source                           📋  captured
              11 The world of tokens                                 📋  captured
              12 Language at the edges, code in the middle           📋  captured
              13 Everything is a contract                            📋  captured
              14 Your plumbing is your ceiling                       📋  captured
              15 The sand and the sun                                📋  captured

    Part III  16 Tell it where you want the truth from              📋  captured
              17 The most expensive model for everything             📋  captured
              18 Let it say I can't                                  📋  captured
              19 They cooperate — that's the problem                 📋  captured
              20 An expert wrote this, not the model                 📋  captured
              21 The expert is the product                           📋  captured
              22 You cannot ask a model who's best                   📋  captured
              23 Let it fetch, let it write                          📋  captured
              24 Let it build code, because code is checkable        📋  captured

    Part IV   25 The recipe, assembled                              ⬜  planned
              26 The ways this goes wrong                            ⬜  planned
              27 Start here                                          ⬜  planned

**"Captured" means the material is written; it is not yet prose.** It lives in `CONCEPTS.md`
(17,612 words, 12 concepts) or in section 9's evidence register. The `chapters/` folder is where each
chapter's material has been gathered so it can be expanded into a chapter.

---

## What `chapters/` contains

25 files, one per chapter still to draft (2–7 and 9–27). Each holds:

    - the plan's claim / demonstration / fix      (from 00-BOOK.md section 7)
    - the captured concept, in full               (where CONCEPTS.md has one)
    - the verified evidence bearing on it         (quoted from section 9, cautions included)
    - a slot to map the chapter to its rules
    - an empty DRAFT section, with the book's rule restated

    11 files carry a full concept or a written one   (7, 9, 11, 17, 18, 19, 20, 21 + 25, 26, 27)
    14 files carry the plan spec and section-9 evidence
     2 of those 14 carry neither a concept nor evidence — chapters 6 and 15. They make no
       load-bearing factual claim; their material is the argument, not a source.

---

## The two registers, and how they differ

    RULES.md        21 rules, each written as:  assumption -> what's actually true -> the rule
    CONCEPTS.md     12 concepts, each written in full, most owning a chapter

    Concept  1  The promise, not the gift                          -> unplaced
    Concept  2  The opinions are inherited, and you cannot argue   -> unplaced
    Concept  3  It will not set you free                           -> Ch 9
    Concept  4  The 8-Ball                                         -> Ch 8
    Concept  5  The most expensive model for everything            -> Ch 17
    Concept  6  The world of tokens                                -> Ch 11
    Concept  7  Let the model declare its own limits               -> Ch 18
    Concept  8  Do not hand the agent the keys                     -> Ch 7
    Concept  9  They cooperate, and that is the problem            -> Ch 19
    Concept 10  The prompt is a knowledge artifact                 -> Ch 20
    Concept 11  The expert is the product                          -> Ch 21
    Concept 12  The artifacts you inherit                          -> unplaced

**Three concepts own no chapter (1, 2, 12).** They are written and substantial. Concept 2 belongs
near chapter 4, Concept 12 near chapter 24.

---

## Open items

### Decisions owed by the author

1. **Where do the three written-but-unplaced chapters go?**
   `Chapter-26-Pushing-Is-Not-Cooperation`, `Chapter-27-I-Was-Never-the-Smart-Part`,
   `Chapter-28-You-Have-Something-to-Lose` — none of these three appears in the 27-chapter plan,
   whose 25/26/27 are *The recipe, assembled / The ways this goes wrong / Start here*.
   **And section 7 commits to the plan's ending:** *"the reader is now the student"* — the bookend
   to the Preface. **"You Have Something to Lose" competes with "Start here" as the close.**
   The numbering cannot be settled until this is decided.

2. **Chapters 25, 26, 27 have no concept and no evidence yet.** Concepts were written for them in
   `chapters/`, assembled from material already on disk — but they have not been reviewed.

### ⚠️ Corrections still to propagate

3. **`00-BOOK.md` section 9 still carries a sentence the primary source refutes.**
   It says *"The name was enacted before the definition was written."* The order **does** define
   the term — in **§3(a)**, as *exactly the existing AI definition by statute* — while **§1** claims
   the technologies *"far exceed"* it. The Introduction was corrected; **section 9 was not.**
   The stronger claim, verified against the Federal Register: **the order refutes itself between
   its own sections.**

4. **15 U.S.C. § 9401(3)** — the definition the order borrows — is quoted from commentary, not read
   from the statute. One fetch closes it. Do not print until then.

5. **Chapter 6 (The clock is always running) and Chapter 15 (The sand and the sun)** have neither a
   concept nor a section-9 entry. Both need real material before drafting, or they are the two
   chapters most likely to become opinion.

### Verify before print

6. NotebookLM tiers and the watermark detail; Pro's cloud storage figure (**do not state one**);
   OpenClaw's CVE and cost figures (**these date fastest of anything in the book**); `qwen2.5:1.5b`
   running CPU-only; and the 2023 agent product names.

### Reference checks outstanding

7. Refs **[19], [20], [21]** (the cognitive-offloading citations) to be read first-hand. **[20] is
   peer-reviewed — lean on it hardest; [19] and [21] are working papers and must be described as such.**
   The source supplied alongside them (`PMC12255134`) is a **study protocol that reports no results** —
   never cite it as findings.

8. A competent ML reader should check chapter 11 before print.

### Housekeeping

9. `youbooks-input/` — a full evaluation and source pack prepared for Youbooks, **now retired**:
   its own documentation says sources are optional and it drafts "from your brief", with four
   frontier models generating the ideas. It writes *around* your material; it does not carry it.
   Keep for the record, or delete.
10. `samples/surviving-the-ai-apocalypse-…pdf` (35 MB) is gitignored; the extracted text (61,577 words)
    is committed. The PDF remains in `~/Downloads`.

---

## What happens next

**The bottleneck is drafting, not thinking.** 25 chapters have their material gathered and their
specifications written. What is missing is the prose pass.

**And the per-chapter target is not a guess — it is arithmetic.** The plan targets 40,000–50,000
words, and front matter accounts for 2,349 of them, so:

    (45,000 planned - 2,349 front matter) / 27 chapters  =  1,580 words per chapter

**The chapter files therefore carry a target of 1,600 words**, not the 1,300 they carried until
11 October 2026. At 1,300 the book would have landed near 38,000 words — under its own floor, and
the shortfall would not have shown up until the draft was finished.

Two ways to do it, and they are not exclusive:

- **The author expands them.** Each file in `chapters/` is written to be expanded. This keeps the
  author the author, which is the whole point of the rule the book is about.
- **The model drafts and the author checks.** Permitted — the method this book describes — provided
  every load-bearing claim goes to a source first, exactly as `00-BOOK.md` §9 requires.

**Either way, the chapter is not done until it has been checked against section 9.**
