# Status — where this book is

**Last updated:** 11 October 2026
**Read this after `README.md`.** Everything here is measured from the files, not recalled.

---

## The one-line state

**The thinking is essentially complete. The drafting is not.**
**The Preface's India detail is confirmed (12 Oct 2026) — the oldest open item is closed.**

    29 chapters planned
     4 exist as prose           Preface (India detail confirmed), Introduction, Ch 1, Ch 8
    25 have starting markdown   chapters/ — spec + concept + evidence, ready to expand
    17 concepts captured        CONCEPTS.md
    21 rules + 7 subrules      RULES.md   (1b skills aren't knowledge; 3b instruct in its universe;
                                          11b be checkable; 11c keep the corrections;
                                          12b date it; 12c whitelist the source;
                                          14b verify by criticality)
    ⚠️→✅ the rule list existed in three places at three different counts - 28, 22 and 25.
                                 The 22 was control/references/the-rules.md and the 25 was the
                                 installed skill copy an agent actually loads. Both now
                                 REGENERATED from RULES.md by book-build/make-rules-reference.py
                                 and all three are byte-identical. This is Rule 12c, found in the
                                 book's own shipped artifacts. Never hand-maintain that reference.
    ⚑  RULES-AUDIT.md          the rules page audited for holes. One real hole found, and it
                                 was Chapter 26: the model-written chapter's six-condition
                                 method - the most runnable thing in the book - was not on the
                                 page at all. Rules 11b and 11c come from it.
    21 evidence entries         verified, in 00-BOOK.md section 9
    ✅  25 of 25 skeletons        have their "rules this chapter carries" filled in.
                                 (12 Oct 2026.) All 31 rules are carried by at least one
                                 chapter; the map is GENERATED from the skeletons by
                                 book-build/make-rule-chapter-map.py into
                                 book-build/rule-chapter-map.csv — the CSV is the index,
                                 the skeletons are the source. Mappings are PROPOSED from
                                 each chapter's own claim and concept; the author confirms
                                 or corrects, one line per chapter.

**And the controls are now installable** — the book is not only an argument:

    AGENT-CONTRACT.md   the rules as a contract in three parts + a prompt to paste
    control/SKILL.md    the same rules as a loadable agent skill
    control/references/the-rules.md   the full 22-rule register the skill draws on

Installed here as the skill `ai-usage-contract`. See README for what each is for.

---

## Where prose goes

**All chapters live in `chapters/`** — drafted chapters and skeletons alike. (This was
reorganized 12 October 2026; the root no longer holds chapters.)

    chapters/Chapter-NN-slug.md             drafted chapters read whole; skeletons write
                                            UNDER a '## DRAFT' heading
    chapters/_folded/                       retired material, folded into another chapter;
                                            the build skips it

**From a skeleton, only the text under `## DRAFT` reaches the book.** The plan spec, the concept and the
evidence in the same file are reference material and are ignored. A skeleton with nothing under DRAFT is
skipped, so unfilled files cannot put empty chapter headings in the manuscript.

**If two files claim the same chapter number, the build keeps the one in the root and prints a warning.** It
does not resolve the collision silently — an unnoticed dropped chapter is exactly the failure this book is
about. At the time of writing it is warning about chapters 26 and 27.

---

## The plan — 29 chapters, four parts

`00-BOOK.md` section 7 is the outline, and it carries its own status on every chapter:
**✍️ drafted · 📋 captured · ⬜ planned.**

    Front      Preface — Why This Book Exists                        ✍️  drafted
    Front      Introduction — AI Is Already Smart Enough             ✍️  drafted

    Part I    1  Ask me anything                                     ✍️  drafted
              2  It cannot tell you it's unsure                      📋  captured
              3  The artifacts you inherit (Concept 12)               ✍️  drafted
              4  You cannot teach it anything                        📋  captured
              5  The opinions are inherited (Concept 2)             ✍️  drafted
              6  The clock is always running                         📋  captured
              7  Activity is not work                                📋  captured
              8  The 8-Ball never fooled anyone                      ✍️  drafted
              9  It will not set you free                            📋  captured

    Part II   11 A function, not a source                           ✍️  drafted
              12 The world of tokens                                 ✍️  drafted
              13 Language at the edges, code in the middle           ✍️  drafted
              14 Everything is a contract                          ✍️  drafted
              15 Your plumbing is your ceiling                       ✍️  drafted

    Part III  16 The most expensive model for everything          ✍️  drafted
              17 Let it say I can't                                  ✍️  drafted
              18 They cooperate — that's the problem                 ✍️  drafted
              19 An expert wrote this, not the model                 ✍️  drafted
              20 The expert is the product                           ✍️  drafted
              21 You cannot ask a model who's best                   ✍️  drafted
              22 Let it fetch, let it write                          ✍️  drafted
              23 Let it build code, because code is checkable        📋  captured
              24 The recipe, assembled                               ✍️  drafted

    Part IV   25 Pushing is not cooperation                         ✍️  drafted
              26 I was never the smart part                           ✍️  drafted
              27 You have something to lose                           ✍️  drafted — the close

**"Captured" means the material is written; it is not yet prose.** It lives in `CONCEPTS.md`
(now 17 concepts) or in section 9's evidence register. The `chapters/` folder is where each
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
    CONCEPTS.md     17 concepts, each written in full, most owning a chapter

    Concept  1  The promise, not the gift                          -> unplaced
    Concept  2  The opinions are inherited, and you cannot argue   -> unplaced
    Concept  3  It will not set you free                           -> Ch 10
    Concept  4  The 8-Ball                                         -> Ch 8
    Concept  5  The most expensive model for everything            -> Ch 16
    Concept  6  The world of tokens                                -> Ch 12
    Concept  7  Let the model declare its own limits               -> Ch 17
    Concept  8  Do not hand the agent the keys                     -> Ch 7
    Concept  9  They cooperate, and that is the problem            -> Ch 19
    Concept 10  The prompt is a knowledge artifact                 -> Ch 20
    Concept 11  The expert is the product                          -> Ch 21
    Concept 12  The artifacts you inherit                          -> unplaced
    Concept 13  The clock is always running                       -> Ch 6
    Concept 14  Presence is not provenance                       -> Ch 16 (beside confinement)
    Concept 15  The manager's page (rules a signer and            -> §4, RULES.md header, Ch 27
                a builder can both hold)
    Concept 16  The tools are not the problem; the spend is       -> Ch 17 (framing), Rules 13/16
                                                                      and Preface (consistency)
    Concept 17  A token is a unit of intelligence               -> Ch 11 (bridge), Ch 17 (opening)

**Three concepts own no chapter (1, 2, 12).** They are written and substantial. Concept 2 belongs
near chapter 4, Concept 12 near chapter 24. **Concepts 13 and 14 were captured in CONCEPTS.md but
missing from this table and from 00-BOOK.md §8 — added 12 October 2026.** Concept 15 (the manager's
page) adds no chapter and no rule by design; it routes the existing readers.

---

## Open items

### Decisions owed by the author

1. ✅ **RESOLVED 12 October 2026 — the numbering collision is closed.** The three drafted
   chapters are the book's actual spine at the close, and the plan now reflects them:
   - **Ch. 26 *Pushing Is Not Cooperation*** (Rule 11c, with 11b) — the practical chapter,
     sits immediately before the close.
   - **Ch. 27 *I Was Never the Smart Part*** (Rule 20, with 21) — the testimony chapter.
   - **Ch. 28 *You Have Something to Lose*** (Rule 3, with 9) — **the close.** Added to the plan
     as a fourth Part IV chapter; the book is now 28 chapters.
   - *The ways this goes wrong* is **folded into Ch. 25** (*The recipe, assembled*) as its second
     half — the recipe and its failure modes are one chapter. Its skeleton is retired to
     `chapters/_folded/`.
   - *Start here* is **folded into Ch. 28** (the close) — the rules paid off, the running-system
     map, and a first move for each of the three readers. Its skeleton is retired to
     `chapters/_folded/`.
   Grounded by the rules, not the numbers: each chapter is placed where its rule puts it.

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

**The bottleneck is now the prose pass, not the mapping.** 25 chapters have their material gathered,
their specifications written, and (as of 12 Oct 2026) their rule mapping declared. Every chapter
in the tracker now shows SPECCED or better. What is missing is the drafting itself.

**And the per-chapter target is not a guess — it is arithmetic.** The plan targets 40,000–50,000
words, and front matter accounts for 2,349 of them, so:

    (45,000 planned - 2,349 front matter) / 28 chapters  =  1,520 words per chapter

**The chapter files therefore carry a target of 1,600 words**, not the 1,300 they carried until
11 October 2026. At 1,300 the book would have landed near 38,000 words — under its own floor, and
the shortfall would not have shown up until the draft was finished.

Two ways to do it, and they are not exclusive:

- **The author expands them.** Each file in `chapters/` is written to be expanded. This keeps the
  author the author, which is the whole point of the rule the book is about.
- **The model drafts and the author checks.** Permitted — the method this book describes — provided
  every load-bearing claim goes to a source first, exactly as `00-BOOK.md` §9 requires.

**Either way, the chapter is not done until it has been checked against section 9.**
