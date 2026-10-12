# Rules audit — are there holes?

**Written 12 October 2026. The author's question: *"Is there a list of rules that show any holes? If there are no
holes, then we don't need to force a chapter count."***

**Short answer: there is no such list, and there is no hole in the sense that matters. There are three gaps — and
one of them is in the chapter the author found most profound.**

---

## Method, and what counts as a hole

Five kinds, checked in this order. The first is the one that matters.

1. **A missing rule** — the book argues something load-bearing and never rules on it.
2. **A rule with no chapter** — the reader is told the rule and never shown it.
3. **A rule with no evidence** — it makes a factual claim and §9 does not back it.
4. **Duplicate rules** — two rules doing one job.
5. **Contradictions** — two rules pulling against each other.

---

## The shape of the list, and it is lopsided

    Part 1 — What it is             7 rules   1, 1b, 2, 3, 3b, 4, 5
    Part 2 — How it behaves         3 rules   6, 7, 8
    Part 3 — How to use it          7 rules   9, 10, 11, 12, 12b, 12c
    Part 4 — How to choose / pay   10 rules   13, 14, 14b, 15, 16, 17, 18, 19, 20, 21

**Parts 1, 3 and 4 are developed. Part 2 is three rules and a gap.** And notice what every rule since the audit
began has been about: **the model.** Rules 1–8 are all *what it is* and *how it behaves*.

---

## 1. Missing rules — one big one, and one small one

### ⚑⚑⚑ THE HOLE — Chapter 26's runnable method is not on the rules page.

**Chapter 26 is the chapter the model wrote, at the author's request, and the one he called profound. It contains a
six-condition method under the heading *"The conditions, as something you can run"* — including the verbatim prompt
text — and not one line of it appears in `RULES.md`:**

> **1. Supply the facts yourself.** The model's memory is not evidence. If a fact matters, hand it over.
>
> **2. State the rule at the start.** *"Every statement is backed by fact and research. If you cannot show where it
> comes from, say so. If my claim is unsupported, say so. Do not agree with me to be agreeable."*
>
> **3. Give the problem, not the answer.** Describe what is wrong. Do not describe what to write.
>
> **4. Expect contradictions, and reward them.** When the model challenges you, answer with evidence or concede. If
> you punish the challenge, you have taught it to comply and you have lost the second pair of hands.
>
> **5. ⚑ Keep the corrections.** *"The record of what the model got wrong is the proof the method is running.*
> ***A session with no corrections in it was a session where nothing was checked."***
>
> **6. ⚑⚑ Do not ask it to be impressive.** *"Impressive is the pushed mode. Ask it to be **checkable**."*

**Why this is a real hole and not a matter of taste:** every other chapter's method made it onto the rules page.
Chapter 13's contract discipline became Rule 6. Chapter 20's brief became Rule 20. Chapter 21's question became Rule
21. **Chapter 26 — the one the author found profound — is the only chapter whose method stayed in the chapter.**

**And two of its six conditions are stronger than anything currently numbered:**

- **#5 is the answer to the book's own hardest question.** Chapter 28 argues *"memory has no error bar; the honest
  product is an error bar on your own claims"* — and then gives the reader no rule for it. **Condition 5 is that
  rule, already written.** *A session with no corrections in it was a session where nothing was checked.* **That is
  measurable. You can count corrections.**
- **#6 may be the single best rule in the book.** *Ask it to be checkable, not impressive.* **Every other rule on the
  page says what to distrust. This one says what to ask for** — and it is the only positive instruction on the list.

**Proposed placement: Rule 11b — *Ask it to be checkable, not impressive.*** Rule 11 is already *"your question is
usually the real problem"*, so 11b is what to do about it. **11 diagnoses; 11b prescribes.** Conditions 1–4 are
already covered — by Rules 1, 12, 11 and 2 respectively. **5 and 6 are genuinely new.**

*(A full Rule 22 would also work, but it would break every "21 rules" cross-reference in the book — which is why Rule
1b was numbered the way it was.)*

**⚑ Note on the obvious candidate that turned out not to be a separate hole.** It looked as though the book had no
rule for the reader's own error bar — Chapter 28 argues *"memory has no error bar; the honest product is an error bar
on your own claims,"* and nothing numbered says so. **It is a real absence, but it is the same hole as the one above.**
Condition 5 of Chapter 26 — *keep the corrections; a session with no corrections in it was a session where nothing
was checked* — **is that rule, already written, sitting in the chapter rather than on the page.** One hole, not two.

### ⚑ CANDIDATE C — nothing about what to do *after* it has already gone wrong. **Medium confidence.**

**The rules page is entirely preventative, and every documented case in §9 was discovered late.** Dallas: 20 months.
NCS: four months after departure. The Anthropic incidents: found only by a retrospective review of 141,006 runs.
FinWise: over a year. **Nobody caught their own problem.**

**Rules 12b and 12c say refuse an expired record and delete the stale copy — but neither says who goes looking, or
how you find the records that were already used before anyone noticed.** Rule 14b budgets verification *before* the
fact is used.

**Proposed shape:** a detection rule — *reconcile on a schedule, not on a hunch*, and make the reconciliation
something a machine does, because the whole finding in §9 is that humans doing it by hand miss it for years.

---

## 2. Rules with no chapter

**One existed. It is now fixed.** Rule 9 had no chapter carrying it; it now sits in **Chapter 9 — *It will not set
you free***, which was always its home (Concept 3's own text: *"AI will benefit some people more than others"*).

**No others.** Verified by search across `chapters/` and the root chapter files.

⚠️ **But the check is weaker than it looks, and this is honest:** **22 of 25 skeletons still hold the placeholder in
their "rules this chapter carries" section**, so for most chapters nobody has declared a rule yet. The check can
prove a rule *is* carried. **It cannot yet prove one is not.** That is a gap in the working notes, not in the book.

---

## 3. Rules with no evidence

**All rules that make a factual claim have a §9 entry.** Two carry visible cautions, and both are stated rather than
hidden:

- **Rule 10** leans on **[19] Bastani and [21] Lehmann, which are working papers, not peer-reviewed.** §9 says so and
  says to lean hardest on **[20] Darvishi**, which is peer-reviewed.
- **Rule 9** — *"it multiplies what you bring"* — is now backed by the misuse block in §9. **Before this session it had
  no evidence at all.**

---

## 4. Duplicate rules

**None.** Checked all 26. The closest pair is **13** (*right-size the model*) and **14b** (*spend the verification*),
and they are different axes — one is about *which model*, the other about *how hard you check*. **14 and 14b** are
adjacent by design: 14 is about effort, 14b is about spending it where it matters.

---

## 5. Contradictions

**None found.** The one pair that looks like a conflict resolves cleanly and the book already says so:

- **Rule 12 says build RAG.** **Chapter 6 says RAG does not fix staleness, it relocates it.**
- **These agree.** RAG cures *provenance*; it does not cure *time*. Those were never the same problem, and Rule 12b
  is what covers the second one.

---

## ⚑ And the answer to the second half of the question

**The chapter count does not need forcing, and the author is right about why.** The count was never designed — it is
an artifact of a long back-and-forth, recorded by the model. **What has to be true is not a number. It is two things:**

1. **Every rule has a chapter that shows it.** (One hole found; fixed.)
2. **Every chapter carries at least one rule.** (22 still undeclared — a working-notes gap, not a book gap.)

**The 26/27 numbering collision is therefore not a structural crisis.** It is a build artifact: the contents page
needs numbers to order the chapters, and two files claim the same one. **It gets fixed by numbering, not by adding or
cutting a chapter.**

**And the last word belongs to the author, not to this audit.** The model-written chapter was meant to be the ending.
**A book that ends where its author wanted it to end does not owe anyone a chapter count.**

---

## ⚑ The finding worth keeping

**The rules page was built by a human dictating rules and a model recording them. The one chapter written the other
way round — the model drafting, the human judging — produced the most runnable method in the book, and it never made
it onto the page.**

**That is not a coincidence worth ignoring.** The rules page is the most-copied page in the book, and it is missing
the only part of the book that reads like instructions.
