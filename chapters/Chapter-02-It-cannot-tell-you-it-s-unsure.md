# Chapter 2 — It cannot tell you it's unsure

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: not a bug to patch. Confidence and accuracy come from the same machinery, so a memory and a
  confabulation are indistinguishable from outside *and* from inside.
- Demo: the same question asked ten ways — the confidence never moves while the answer does.
- Fix: treat every declaration as unverified by default. Not "usually right" — *unverified*.

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **The grounding test** (Ch. 1, Ch. 18) — real, run on this machine. Four models; three scored 5/5;
  one failed the grounding test by inventing a capital for a fictional country. Reproducible.

- **⚑ Relying on the model's knowledge means inheriting the training that shaped it.** *Raised by the
  author: "Whenever we rely on the LLM's knowledge for answers, we are introducing the potential for RLHF
  induced biases, guardrails and hallucinations."* (The note says "RHFL"; read as **RLHF**.) **All three
  hold up, and the third is stronger than expected — sources in `CONCEPTS.md` Concept 12.**
  - **Bias:** sycophancy, driven by preference data rewarding agreement. Sharma et al./Anthropic (ICLR 2024):
    *"both humans and preference models prefer convincingly-written sycophantic responses over correct ones
    a non-negligible fraction of the time."* Mechanised in arXiv 2602.01002; measured at **58.19%** in
    SycEval. **The bias is agreement, not politics.**
  - **Guardrails:** refusal is trained behaviour and it is fragile — RFT **cut refusal rates by >80%**,
    raising *"confident yet incorrect answers to unanswerable questions"* (arXiv 2505.13988).
  - **Hallucination:** RL fine-tuning can **increase** it (arXiv 2505.24630), including a spurious optimum
    where *"the model can converge to a confidently held wrong answer."*
  - **⚑ And the fix the research describes is the capability bus:** SALU (arXiv 2507.16951) rewards
    abstention and penalises confident hallucination — hallucination falls to **1.3%**. **Ch. 18's design,
    reached from the opposite direction.** The project keeps producing this pattern.

---

## The rules this chapter carries

**Rule 5 — *It cannot tell you it's unsure.* (primary).** The chapter is Rule 5 made visible: a memory and an invention arrive through the same door, in the same voice — so confidence cannot be read as evidence (Rule 2).

**Rule 2 — *Confidence is not evidence.* (carried).**


**Rule 4 — *It has never seen the future.* (carried).** Rule 4 is the same machinery as Rule 5: the model is built entirely out of the past, so a prediction is a confabulation with a date on it. This chapter shows the mechanism; Rule 4 names the consequence.
## DRAFT

*(write it here. Target roughly 1,600 words. Every load-bearing claim to a source,*
*citations kept, nothing invented, anything unverifiable marked ⚠️ rather than*
*smoothed over — the same rule the rest of the book was written under.)*
