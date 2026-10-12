# Chapter 26 — The ways this goes wrong

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

- The failure modes, from real scars: assuming a tool exists, trusting a fluent answer, letting a model
  judge a model, fixing knowledge problems with bigger models, building on anything with a version number.

---

## Concept — The ways this goes wrong — from real scars *(written for this chapter; no earlier capture existed)*

**What it is.** The failure modes, each one taken from something that actually happened on
this project rather than from imagination. A failure catalogue is only credible if the author
is visibly in it.

**The five, and where each one bit:**
1. **Assuming a tool exists.** The provider layer probed for tools that were registered and
   never present; the fix was to discover at call time instead of assuming at build time.
   (Rule: each user has their own tools.)
2. **Trusting a fluent answer.** Every correction in this book's own record — the claim of
   being first, the two tools assumed to be one company, the effect that did not replicate,
   the paper whose numbers moved between versions.
3. **Letting a model judge a model.** Asking a model to rank models produces a confident
   answer that is a fact you did not earn. Measure with code. (Ch. 22)
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

*(map the chapter to its rule numbers here before drafting — every chapter carries at least one)*

## DRAFT

*(write it here. Target roughly 1,300 words. Same rule as the rest of the book: every*
*load-bearing claim to a source, citations kept, nothing invented, anything unverifiable*
*marked ⚠️ rather than smoothed over.)*
