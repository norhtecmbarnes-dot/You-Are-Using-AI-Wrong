# The workflow — from skeleton to printed page

**12 October 2026.** Every chapter moves through seven states, and each transition has a gate. **The gates
are the point: every problem found today was a chapter that got past a gate nobody was checking.**

Run `python3 book-build/chapter-status.py` to see where everything stands, and `--blockers` for what is stuck.

---

## The states, and the gate at each

| # | State | What is true | The gate — and who passes it |
|---|---|---|---|
| 1 | **MAPPED** | The skeleton names **which rule this chapter carries.** | **"Which rule does this chapter carry?"** If the answer is none, the chapter is wrong, not the mapping. **Me, with your confirmation.** |
| 2 | **SPECCED** | Plan spec + concept + live §9 evidence + rule mapping all present. | Has the evidence block gone stale? **Chapter 15's did, and nobody noticed for weeks. Me.** |
| 3 | **SOURCED** | Every load-bearing claim has a §9 entry **with a source and a date.** | **Rule 12b:** a verification with no date is not a verification. **Me.** |
| 4 | **DRAFTED** | ~1,600 words under `## DRAFT`. | **Your material first.** I draft against the spec and the register, never from the model's knowledge. **Me.** |
| 5 | **VERIFIED** | Every claim re-checked against the register; `de-ai-ify` run; no scaffolding leaking. | Is every claim traceable, and does the build agree? **Me, and it is mechanical.** |
| 6 | **AUTHOR-OK** | You have read it and signed off. | **Only you can pass this gate.** Nothing skips it. |
| 7 | **BUILT** | It renders into the interior PDF with a page number. | Does it appear in the contents? **The build.** |

---

## ⚑ Where we are right now

    29 outline chapters · 11 pieces drafted (2 front matter + 9 chapters)
    11,621 words drafted = 26% of 45,000 · 33,379 words remaining ≈ 21 chapters

    at 1,600 words/chapter the arithmetic closes exactly, which is a good sign
    that the per-chapter target was set from the same numbers

**Pages:** 288 words/page at 6×9 with front matter. So:

    now        39 pages
    40,000 w  ~139 pages      45,000 w  ~156 pages      50,000 w  ~174 pages

**The plan says 40,000–50,000. Call it a 160-page book, and that is the right size for the argument.**

---

## ⚑ And the bottleneck is gate 1, not the writing

**22 of 25 skeletons have no rule mapping.** That is why the tracker shows most chapters as `PLANNED` even
though 12 of them already carry good §9 evidence. **They are not blocked on writing. They are blocked on a
question nobody has asked them: *which rule does this chapter carry?***

**That gate is also the cheapest, and it is the one that found the real problems.** Chapter 15's stale
evidence block, Rule 9 having no chapter, and eventually the loss of *What to notice about the human* — all
surfaced by asking that question.

**So the order of work is:**

1. **Gate 1, in batches, with you.** Twelve chapters already have evidence: **2, 3, 4, 5, 10, 12, 13, 14, 16,
   22, 23, 24.** Each needs one sentence naming its rule. **That is one session.**
2. **Then those twelve draft, roughly in outline order.** Each is 1,600 words against a spec that already
   exists, with evidence that is already verified.
3. **Then the nine with neither** — **7, 11, 17, 18, 19, 20, 21, 25** and the two plan chapters shadowed by
   drafted ones — need evidence found first, or an explicit note saying the chapter carries no factual claim.
4. **`Start here` last**, because its material is everything above it.

**At 1,600 words a chapter and 21 chapters to go: five sessions of four chapters, plus the gates.**
Not a long project. A short one done carefully.

---

## What I need from you at each gate

**Gate 1** — *"does this chapter carry the rule I think it does?"* One line each, 12 times.
**Gate 6** — you read it. This is the only gate that cannot be delegated, and it is the one that has caught
the most, including four corrections to the model's own chapters.

**Everything else is mine.** And gates 3 and 5 get a script rather than a memory, because the one thing today
proved over and over is that **anything restated by hand drifts from the thing it restates.**

    chapter-status.py       what state is every chapter in, and what is blocking it
    make-rules-reference.py the shipped rule list, generated from RULES.md so it cannot drift
    build-interior.py       renders the book, and refuses to print author notes as prose

**Three scripts, three rules that used to be habits.** That is the workflow.
