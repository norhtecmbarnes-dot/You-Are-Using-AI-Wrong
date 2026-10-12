# Chapter 24 — Let it build code, because code is checkable

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: code has a property prose never will — it either runs or it doesn't. Verifiable output is where
  the model's weakness stops mattering. *(Payoff of Ch. 17's two waves.)*
- Demo: a real bug caught by **looking at the bytes** — a payload that was JSON wearing an audio file's
  name — not by asking a model whether it looked right.
- Fix: prefer the model for work whose output can be tested. Trust the test, not the model.

### Part IV — The scaffold

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **The VocalLab bug** (Ch. 23) — a payload that was JSON wearing an audio file's name, caught by
  inspecting the bytes. Real.

- **The Alpha challenge** (Ch. 18) — five code-scored tests, ties to the incumbent. Real result.

---

## The rules this chapter carries

**Rule 15 — *Your first wave's trust may not transfer.* (primary).** Code is checkable — it runs or it doesn't — so verifiable output is where a model's weakness stops mattering. Rule 15 (find your test) aimed at the model's strongest output, with Rule 11b as the discipline.

**Rule 11b — *Ask it to be checkable, not impressive.* (carried).**

## DRAFT

*(write it here. Target roughly 1,600 words. Every load-bearing claim to a source,*
*citations kept, nothing invented, anything unverifiable marked ⚠️ rather than*
*smoothed over — the same rule the rest of the book was written under.)*
