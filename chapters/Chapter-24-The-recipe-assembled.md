# Chapter 24 — The recipe, assembled

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

- The full architecture in one place: contracts, injection, code-scored measurement, discovery over
  assumption, human gates, and a system that improves itself without a model deciding anything. **Two
  pillars now bear the weight** — confinement of the knowledge (Ch. 16), and the capability bus that lets
  a small model decline (Ch. 17).

---

## Concept — The recipe, assembled — and it runs *(written for this chapter; no earlier capture existed)*

**What it is.** The whole architecture in one place, so a reader can see that the book is
one system and not twenty-seven complaints. Nothing new is introduced here; this is the
assembly chapter.

**Two pillars carry the weight now** — the confinement of knowledge (Ch. 16) and the
capability bus that lets a small model decline (Ch. 17). Everything else hangs off those.

**The parts, in the order they were built:**
- **Contracts at every boundary** — define the shape before you call, validate before you act,
  reject rather than repair. (Ch. 14)
- **Injection** — facts are attached, never requested. The model transforms supplied input.
  (Ch. 11, Ch. 16)
- **Code-scored measurement** — the Alpha. Fixed tests, scored by code, ties to the incumbent.
  No model votes. (Ch. 21)
- **Discovery over assumption** — the provider registry probes for what is present instead of
  assuming what should be. No LLM in the decision path. (Ch. 11, Ch. 13)
- **Human gates** — the system queues work for approval rather than acting. (Ch. 24 rule set)
- **A system that improves itself without a model deciding anything** — it measures, it
  records, it reports; the human promotes.

**The evidence that it runs, not that it is described:** `DASHBOARD-IMPLEMENTATION.md`, which
maps every rule to the file that implements it and marks honestly which are partial and which
are not written yet.

**The handling rule.** Do not add a single new idea here. If a section needs one, it belongs in
an earlier chapter and this chapter is wrong.

---

## The ways this goes wrong (folded from the retired Chapter 26 skeleton)

*The failure modes, from real scars. This section folds in the material of the former
"The ways this goes wrong" skeleton, which is retired - its content lives here now.*

(00-BOOK.md section 7)

- The failure modes, from real scars: assuming a tool exists, trusting a fluent answer, letting a model
  judge a model, fixing knowledge problems with bigger models, building on anything with a version number.

---

— The ways this goes wrong — from real scars *(written for this chapter; no earlier capture existed)*

**What it is.** The failure modes, each one taken from something that actually happened on
this project rather than from imagination. A failure catalog is only credible if the author
is visibly in it.

**The five, and where each one bit:**
1. **Assuming a tool exists.** The provider layer probed for tools that were registered and
   never present; the fix was to discover at call time instead of assuming at build time.
   (Rule: each user has their own tools.)
2. **Trusting a fluent answer.** Every correction in this book's own record — the claim of
   being first, the two tools assumed to be one company, the effect that did not replicate,
   the paper whose numbers moved between versions.
3. **Letting a model judge a model.** Asking a model to rank models produces a confident
   answer that is a fact you did not earn. Measure with code. (Ch. 21)
4. **Fixing a knowledge problem with a bigger model.** Scale improves fluency faster than
   factuality, so the failure gets harder to detect, not rarer. (Ch. 5)
5. **Building on anything with a version number.** Mechanisms survive and products churn; a
   book that names a model version is stale before it prints.

**Each entry, same shape:** what was assumed → what happened → the rule that prevents it.
This is the only chapter where the author's mistakes are the material, which is why it must
not be written in a warning register. It is a ledger.

**The handling rule.** No hypothetical failures. If it did not happen on this project, it does
not get a section.

---

## The rules this chapter carries

**Rule 12 — *Confinement is the design, not a limitation.* (primary).** The recipe, assembled: the full architecture in one place — contracts, injection, code-scored measurement, human gates. This chapter carries Rule 12 (confinement is the design) as its spine, with Rule 1 (attach the facts) and Rule 6 (rules persist in code) as the two pillars that bear the weight.

**Rule 1 — *It doesn't know things.* (carried).**

**Rule 6 — *You cannot teach it anything.* (carried).**

**Rule 15b — *Testimony is its own source, but only for what you witnessed.* (carried, in the failure-modes section).** The author's own cases (Dallas, NCS, FinWise, MARTA) are witness evidence, and this chapter must say which claims are sourced and which are witnessed.

**Rule 15c — *Most of what a person says is not a claim.* (carried, in the failure-modes section).** A reader who has just been told "trust nothing it says" needs the corollary - and not everything YOU say is a claim either.

## DRAFT

*(write it here. Target roughly 1,600 words. Same rule as the rest of the book: every*
*load-bearing claim to a source, citations kept, nothing invented, anything unverifiable*
*marked ⚠️ rather than smoothed over.)*
