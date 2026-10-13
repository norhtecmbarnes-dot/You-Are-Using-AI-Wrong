# Open items — as questions

**12 October 2026.** Everything outstanding on *You Are Using AI Wrong*, written as questions you can go and
answer. Section D needs nothing from you and is listed only so nothing is invisible.

**How to answer:** reply to any of them in any order, in your own words, and I'll take it from there. Partial
answers are fine. "Still thinking about it" is a fine answer too.

---

## A. Only you can answer these — they are your own experience

### A1. The Preface's India class ✅ **CLOSED 12 October 2026**

The author supplied the detail in full. The Preface now carries it verbatim: the conference room of data
scientists, program managers and proposal writers; everyone on Claude Code; the attendee who said he had
never seen AI used that way; the flight home; and the pivot to this book's audience — *the organization,
the ones who sign the checks.* The `⚠️ TO CONFIRM` mark is removed. **This was the oldest open item in
the book, and it is now closed.**

### A2. Chapter 15's hinge sentence — pick one, write one, or reject the construction

The plan says the beach passage is followed by **one short factual sentence, unexplained.** Three candidates are
in the file:

1. *It has read all of that, and felt none of it.*
2. *None of that was felt by anything.*
3. *It can describe every part of that and has experienced none of it.*

- **Which one, or what's better?**

### A3. The strengths chapter — restore it?

Your original design had **"15. What to notice about the human"** — *what a system learns about its user, it
becomes. Aim it upward* — with a demo of two memory systems, one recording mistakes and one recording strengths,
over a year. The 27-chapter accretion dropped it.

- **Restore it as its own chapter, fold it into another, or leave it out?**
- If restored: **which number**, and does it sit in Part III or as a closing note?

### A4. Chapter 27's arithmetic

It says *"Four times I overstated. Four times he caught it"* and then lists **three** — and those three are a
different set from the record's four (which Chapter 28 lists correctly).

- **Reconcile to your three, to the record's four, or rewrite the count out entirely?**

---

## B. Things I'd need to research — say which are worth the time

### B1. Twenty-one register entries have no verification date

Rule 12b says a verification without a date isn't one. The §9 register now dates its newer entries, but **21 of
the original ones carry a source and no date.**

- **Worth me re-verifying all 21 and dating them?** It's mechanical but it's the biggest single gap left, and by
  the register's own argument those entries cannot currently be aged. **Recommend: yes.**

### B2. The chapter that reconciles the rules against your actual code

Your outline says the book should end by **showing its own work** — *"say plainly which rules are implemented,
which are partial, and which are not written yet,"* mapped to `DASHBOARD-IMPLEMENTATION.md`.

- **Is that file still accurate against the dashboard as it stands today?** If it has drifted like everything
  else did today, I should re-read the code before writing that chapter.
- **And do you want the unfinished parts named in print?** Your outline says yes. Confirming, because it's your
  reputation on the page.

### B3. Refs [19] [20] [21] read first-hand

§10's own hard gate: the three citations behind Rule 10 — Bastani, Darvishi, Lehmann. Two are working papers.

- **Have they been published since?** If so, the citation and the "not peer-reviewed" note change.

### B4. Two claims resting on an earlier session's record

Chapter 28's corrections #1 and #2 — *two earlier books predate your title*, and *two tools are not from the same
company* — I recorded as verified earlier but **never got into the register**, so I can't date them.

- **Worth a fresh pass to date them, or leave them as they stand?**

---

## C. Decisions — one line each, no research needed

### C1. Where does the Rules page go in the book?

Three options were written into `RULES.md`; the file currently contradicts itself (*"read this first"* versus the
note saying *put it after Chapter 1*).

- **Early, after Chapter 1? Late, as the final chapter? Or both — early as a promise and late as the payoff?**
  (The note recommended **both**.)

### C2. Seven documents aren't listed anywhere

`Chapter-26`, `Chapter-27`, `Chapter-28`, `CONCEPT.md`, `SESSION-RECORD-2026-10-11.md`,
`Tool-Evaluation-AIWriteBook.md`, `Review-Grok-2026-10-11-and-EO-14434.md`.

- **Shall I add them to `STATUS.md` and `README.md`?** And there is both a `CONCEPT.md` and a `CONCEPTS.md` —
  **is the singular one a leftover to delete?**

### C3. Should I write *Start here*?

Four places in the front matter promise it pays off the 21 rules, and it isn't written. Its material largely
exists already — the audit work from today is exactly *"which rules are implemented, which are partial, and which
are not written yet."*

- **Shall I assemble it, or do you want to write it?**

---

## E. Addressed 12 October 2026 — the audience request (Concept 15)

The author asked for the book to serve **the person who signs the checks** and **the person
responsible for making projects work**, with a warning for **the person who has not built yet**;
written *For Dummies* style (easy but profound); with rules **managers can remember and apply**;
to use AI **efficiently and economically**; and to **not trust the weights or be seduced by
confidence**. Captured as **Concept 15** in `CONCEPTS.md` and applied as routing, not new rules:

- `00-BOOK.md` §4 rewritten to name the three readers and their rules.
- `00-BOOK.md` §5 and `RULES.md` header: the "two ways in" promise (act today / know why).
- `RULES.md` header: which rules belong to the signer (2, 13, 14, 16, 17) and the builder
  (1, 2, 5, 9, 11b, 14b).
- `00-BOOK.md` §7 Ch. 27: the three readers named as the audience for the first moves.
- No new rules, no new chapters. The 21 + 10 stand as written.
- The generated rules reference regenerated and the installed skill copy updated (both
  byte-identical to `control/references/the-rules.md`).
- Also fixed in the same pass: Concepts 13 and 14 were in `CONCEPTS.md` but missing from
  `00-BOOK.md` §8 and the `STATUS.md` table — both now list all 15.

**Still owed from you:** *(A1, the India detail, was closed later the same day — see A1 above.)*

---

## H. Addressed 12 October 2026 — the rule-chapter map, assembled (gate 1 cleared)

The author asked for the rules-to-chapters link to be assembled as it was done before, and for
everything to be assembled so the book can be completed. There was no CSV in the repo — the
mapping lived only in each skeleton's "rules this chapter carries" section, and 21 of 25 held
the placeholder. Now:

- **All 25 skeletons carry a rule mapping.** The 12 chapters that already had full material
  (2, 3, 4, 5, 10, 12, 13, 14, 16, 22, 23, 24) were mapped first, from each chapter's own
  plan claim and concept. The remaining 9 (7, 11, 18, 19, 20, 21, 25, 26, 27) were then mapped
  from the same material.
- **Coverage is complete both directions.** All 31 rules (21 + 10 subrules) are carried by at
  least one chapter; all 25 chapters carry at least one rule. Five subrules had no chapter
  (1b, 4, 15b, 15c, 21b) and were placed where the book's own material puts them: 1b with
  Ch. 4 (skills are not knowledge), 4 with Ch. 2 (the future is not in the weights), 15b and
  15c with Ch. 26 (witness vs. claim in the failure modes), 21b with Ch. 23 (automate the
  process, or question whether it should exist).
- **`book-build/rule-chapter-map.csv` is the working index** — chapter, title, status,
  primary rule, all rules carried, source file. Generated by
  `book-build/make-rule-chapter-map.py`, which refuses to write if any skeleton still holds
  the placeholder and exits non-zero if any rule has no chapter. The skeletons remain the
  source of truth; the CSV is the derived view.
- **The mappings are PROPOSED, not confirmed.** They are the assistant's reading of each
  chapter's own claim and concept. The author should confirm or correct — one line per chapter.
  The discipline is his: concepts do not map 1:1 to rules, and the judgement is his to make.
- **The tracker now shows every un-drafted chapter as SPECCED**, not PLANNED — the gate-1
  blocker is gone. What remains is the prose pass (drafted → verified → author-ok → built).

---

## G. Addressed 12 October 2026 — "a token is a unit of intelligence" (Concept 17)

The author supplied the decision maker's definition: the technical definition (fragment of a word,
number of bytes) is correct but aimed at the engineer; **for the decision maker, a token is a unit
of intelligence.** Captured as **Concept 17** in `CONCEPTS.md` — two definitions, each aimed at its
own reader, bridged not merged:

- `chapters/Chapter-11-…md` — the technical definition stays (mechanism needs it); a **bridge
  sentence** now sends the reader forward to Ch. 17 with the second definition.
- `chapters/Chapter-17-…md` — the cost argument now **opens with the definition**: you are buying a
  metered quantity of intelligence, and the question is whether the task needs that much.
- Guard rail recorded: never let "unit of intelligence" drift into "the model is intelligent" — that
  is the book's central category error wearing a definitions costume. No new rule.

---

## F. Addressed 12 October 2026 — "the tools are not the problem; the spend is" (Concept 16)

The author clarified that the book prosecutes a **habit**, not a product: Claude Code and Codex are
good tools and the most expensive; the purpose is **best output for the least cost**; giving everyone
the most expensive models does not improve output but does increase cost. Captured as **Concept 16**
in `CONCEPTS.md` — a *framing* concept, not a new rule:

- `chapters/Chapter-17-…md` — the plan spec now carries the framing line explicitly, and the
  chapter's **rule mapping is filled** (Rules 13, 14, 14b, 16). Chapter 17 is one step closer to
  draftable.
- Rules 13 and 16 already say the right thing; this concept is the argument behind them, aimed at
  the habit, not the hardware.
- Guard rail recorded: no vendor ranking in either direction; no sneer at the expensive tools or
  the users who bought them; the Preface's consistency (same tools, different results) is protected.

---

## I. Resolved 12 October 2026 — the book is reorganized around the rules, not the numbers

The numbering collision (drafted Ch. 26/27/28 vs. planned Ch. 26/27) is closed. The resolution
was to **ground the book by its rules, not its chapter numbers** — each chapter is placed where
the rule it carries puts it. The book is now **28 chapters**, and every chapter names its rules:

| Ch | Title | Primary rule | Carries | State |
|---|---|---|---|---|
| 25 | The recipe, assembled (+ the ways this goes wrong) | 12 | 1, 6, 15b, 15c | SPECCED |
| 26 | Pushing is not cooperation | 11c | 11b | DRAFTED |
| 27 | I was never the smart part | 20 | 21 | DRAFTED |
| 28 | You have something to lose (+ Start here) — **the close** | 3 | 9 | DRAFTED |

- All chapters now live in `chapters/`; the book root holds front matter and working documents only.
- `chapters/_folded/` holds the two retired skeletons (*The ways this goes wrong*, *Start here*).
  Their content is folded into Ch. 25 and Ch. 28 respectively — nothing was deleted.
- The build's root-override for the 8-Ball chapter is gone; Chapter 8 is now
  `chapters/Chapter-08-The-8-Ball-Never-Fooled-Anyone.md`, numbered by its filename like everything else.
- The build and the tracker decide skeleton-vs-drafted by content, not by folder.
- The `!! chapter numbers claimed twice` warning no longer appears.
- 00-BOOK.md §7 Part IV rewritten to match; the plan is 28 chapters across four parts.

---

## J. Resolved 12 October 2026 — Chapter 9 is now "The Promise, Not the Gift" (Concept 1)

The author supplied Concept 1 ("The promise, not the gift") written out as a
chapter. It takes the Chapter 9 slot at the head of Part II — Part I showed
what the model is not; Ch. 9 names what it was sold as. The former Ch. 9
("It will not set you free", Concept 3's myth-breaking half) shifts to
**Chapter 10**, and every later chapter renumbers by one (the book is now
**29 chapters**).

- New `chapters/Chapter-09-The-Promise-Not-the-Gift.md` — the author's
  chapter, verbatim (972 words), with a rule mapping (sets up Rule 2,
  carries Rule 16) and a verification note. No external factual claims
  requiring a source; the author's position is testimony, presented as such.
- The former Ch. 9 skeleton ("It will not set you free") moved to
  `chapters/Chapter-10-It-will-not-set-you-free.md`; its skeleton was
  already in `_folded/` and was restored under the new number.
- Skeletons 10–25 shifted to 11–26; drafted chapters 26/27/28 (Pushing /
  I Was Never / You Have Something to Lose) shifted to 27/28/29.
- All in-file `# Chapter NN —` headings renumbered to match filenames
  (Ch. 8's heading gained its number: "# Chapter 8 — The 8-Ball…").
- All cross-references updated: in 00-BOOK.md (outline, register rows,
  structural notes) and inside chapter files ("Ch. 18" -> "Ch. 19",
  "Chapter 11's subject" -> "Chapter 12's subject", etc.).
- 00-BOOK.md §7 Part II now reads: **9. The promise, not the gift** ✍️,
  **10. It will not set you free** 📋, **11. A function, not a source** 📋, …
- The rule-chapter CSV regenerated: 29 chapters mapped, 31 rules defined,
  31 carried — full coverage, no collisions.
- STATUS.md / WORKFLOW.md / README.md counts updated to 29.
- ⚑ Open follow-up (pre-existing, unchanged): the outline's structural note
  about splitting Part III still refers to the old Ch. 19–21; it now reads
  Ch. 20–22. And the "Ch. 5/6 merge candidate" question is **resolved**: the former Ch. 5
  ("A bigger model does not fix this") is retired to `chapters/_folded/` — its claim is
  carried by Ch. 18. Ch. 5 is now "The opinions are inherited" (Concept 2), the author's
  own chapter.

---

## D. Mine, in flight — nothing needed from you

- **Gate 1 is now cleared: all 25 skeletons carry a rule mapping** (12 Oct 2026, proposed by the
  assistant from each chapter's own concept and claim, for the author to confirm or correct).
  Every one of the 31 rules is carried by at least one chapter. The map is generated, not
  maintained: `python3 book-build/make-rule-chapter-map.py` writes
  `book-build/rule-chapter-map.csv` from the skeletons and refuses to write if any skeleton
  still holds the placeholder. **The CSV is the working index; the skeletons are the source.**
- ✅ **The build's numbering collision — RESOLVED 12 October 2026.** The book is now 28 chapters,
  grounded by the rules. Ch. 26 *Pushing Is Not Cooperation* (Rule 11c), Ch. 27 *I Was Never the
  Smart Part* (Rule 20), Ch. 28 *You Have Something to Lose* (Rule 3 — the close). *The ways this
  goes wrong* folded into Ch. 25; *Start here* folded into Ch. 28. The two retired skeletons live
  in `chapters/_folded/`; the build skips them. All chapters now live in `chapters/`; the build
  no longer needs the root-override, and the `!!` collision warning is gone.
- **Chapter 6's two demonstrations need re-verification before print** — the price change and the CVE count date
  fastest of anything in the book, by the register's own warning.
- **One dated re-check owed on the fly/reward chain** — verified in an earlier session, now in the register
  without a date.
- **The `youbooks-input/` brief** is built and unused; the tool test was parked when you pivoted to the local
  deterministic build.

---

## The one-line summary

**One thing is actually blocking:** the **four decisions in section C**. The India detail (A1) is closed —
the Preface now carries the author's own account. Everything in D is mine and running. Everything in B is
research I can start on your word.
