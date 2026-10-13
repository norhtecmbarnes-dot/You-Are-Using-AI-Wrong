# Chapter 11 — A function, not a source

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: the reliable framing is *transformation of supplied input*.
- Demo: the same request twice — once asking it to remember, once handing it the material.
- Fix: one rule at the call site — *attach the facts so it never needs to remember.*

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **⚑ The answer to no-provenance — RAG and brand voice.** *Requested by the author: "explain how this
  might work."* Full explanation in `CONCEPTS.md` Concept 6. **The principle, which is bigger than the
  chapter:** *nothing that matters should live only in the weights.* **Facts → RAG. Perspective → brand
  voice. Rules → policy files. Method → a hand-written brief.** Four moves, one idea: convert an inherited,
  uninspectable disposition into a declared, readable artifact. **And RAG's real gain is not accuracy — it
  is that the failure mode moves from invention (unprovable) to misreading (checkable).**

- **⚑ Relying on the model's knowledge means inheriting the training that shaped it.** *Raised by the
  author: "Whenever we rely on the LLM's knowledge for answers, we are introducing the potential for RLHF
  induced biases, guardrails and hallucinations."* (The note says "RHFL"; read as **RLHF**.) **All three
  hold up, and the third is stronger than expected — sources in `CONCEPTS.md` Concept 12.**
  - **Bias:** sycophancy, driven by preference data rewarding agreement. Sharma et al./Anthropic (ICLR 2024):
    *"both humans and preference models prefer convincingly-written sycophantic responses over correct ones
    a non-negligible fraction of the time."* Mechanised in arXiv 2602.01002; measured at **58.19%** in
    SycEval. **The bias is agreement, not politics.**
  - **Guardrails:** refusal is trained behavior and it is fragile — RFT **cut refusal rates by >80%**,
    raising *"confident yet incorrect answers to unanswerable questions"* (arXiv 2505.13988).
  - **Hallucination:** RL fine-tuning can **increase** it (arXiv 2505.24630), including a spurious optimum
    where *"the model can converge to a confidently held wrong answer."*
  - **⚑ And the fix the research describes is the capability bus:** SALU (arXiv 2507.16951) rewards
    abstention and penalizes confident hallucination — hallucination falls to **1.3%**. **Ch. 18's design,
    reached from the opposite direction.** The project keeps producing this pattern.

---

## The rules this chapter carries

**Rule 1 — *It doesn't know things.* (primary).** The reliable framing is transformation of supplied input — Rule 1 at the call site: attach the facts so it never needs to remember. Confinement (Rule 12) is the same rule one level up.

**Rule 12 — *Confinement is the design, not a limitation.* (carried).**

## DRAFT

*(write it here. Target roughly 1,600 words. Every load-bearing claim to a source,*
*citations kept, nothing invented, anything unverifiable marked ⚠️ rather than*
*smoothed over — the same rule the rest of the book was written under.)*
