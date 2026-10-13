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
  - **Guardrails:** refusal is trained behavior and it is fragile — RFT **cut refusal rates by >80%**,
    raising *"confident yet incorrect answers to unanswerable questions"* (arXiv 2505.13988).
  - **Hallucination:** RL fine-tuning can **increase** it (arXiv 2505.24630), including a spurious optimum
    where *"the model can converge to a confidently held wrong answer."*
  - **⚑ And the fix the research describes is the capability bus:** SALU (arXiv 2507.16951) rewards
    abstention and penalizes confident hallucination — hallucination falls to **1.3%**. **Ch. 18's design,
    reached from the opposite direction.** The project keeps producing this pattern.

---

## The rules this chapter carries

**Rule 5 — *It cannot tell you it's unsure.* (primary).** The chapter is Rule 5 made visible: a memory and an invention arrive through the same door, in the same voice — so confidence cannot be read as evidence (Rule 2).

**Rule 2 — *Confidence is not evidence.* (carried).**


**Rule 4 — *It has never seen the future.* (carried).** Rule 4 is the same machinery as Rule 5: the model is built entirely out of the past, so a prediction is a confabulation with a date on it. This chapter shows the mechanism; Rule 4 names the consequence.
## DRAFT

You have seen it happen. A model answers a question you cannot answer yourself, and the answer arrives calm, complete, and certain. You read it twice. It sounds right. You use it.

Then you check. And the answer was wrong — not *slightly* wrong, not *outdated* wrong, but *invented* wrong. A capital for a country that does not exist. A citation to a case that was never decided. A statistic with no source anyone can find. And the worst part is not that it was wrong. It is that nothing about the answer told you it was.

This chapter is about that nothing. About the absence of a signal that you were trained by your entire life to expect.

## The expectation

When a person answers your question, you get more than words. You get a *manner*. The confident person speaks quickly and holds your eyes. The uncertain one hesitates, qualifies, says *I think* or *I'm not sure*. The expert cites a source. The amateur waves a hand. These signals are not decorations. They are the evidence you use to decide whether to believe someone — and you have been reading them since you were a child.

A language model produces one manner. Always the same one. Calm, complete, certain, fluent. Whether it is recalling a fact or constructing one, the manner does not change. Not because the model is hiding its uncertainty — it has none to hide. There is no internal dial that reads *confidence in my own memory*, because there is no memory in the sense you mean, and therefore no confidence to report.

A memory and an invention arrive through the same door, in the same voice, at the same speed, with the same certainty. **From the outside they are indistinguishable. From the inside, there is no inside to distinguish them in.**

## The demonstration

Ask the same model the same question ten different ways. Rephrase it. Soften it. Make it formal. Add a persona. Remove the persona. Ask it to be careful, then ask it to be bold.

Watch two things: the *answers* will move. Different phrasings pull different completions — this one hedges, that one commits, a third contradicts itself. And the *confidence* will not. Every answer arrives in the same calm, competent register. The certainty never dips when the answer degrades. The fluency never stutters when the content hollows out.

That is the demonstration, and it is the whole claim in one observation. **The confidence is not tracking the answer. It is tracking nothing.** It is a property of the wording, not a measure of the truth.

This is not a bug that a patch will fix. It is not a missing feature. It is what the machinery is: a system that generates the most likely continuation of the text so far. A real memory and a confabulation are both likely continuations. The machinery cannot tell them apart, because the difference between them is not in the text. It is in the world.

## Why "just ask it to be careful" does not work

You might think the answer is simple. Tell the model: *if you are not sure, say so.* And in a narrow sense, you can. A well-prompted model will hedge, will qualify, will say *I don't know* — more often than an unprompted one.

But look at what that actually is. It is a *performance* of uncertainty, produced by the same machinery that produces the confident answer. The model is not reporting an internal state. It is generating the text that an uncertain person would generate. Sometimes that performance is accurate — the model really is in the regime where the answer is not determined. Sometimes it is not. **You cannot tell which, because the performance looks the same in both cases.**

And there is a worse failure mode. Asked to express uncertainty, a model will sometimes hedge *correct* answers — undermining your trust in the one thing it got right — while still committing confidently to the wrong ones. The hedge is not calibrated to the truth. It is calibrated to the prompt. You have not fixed the signal. You have added noise to it.

The honesty you need cannot come from the model's character. **If the answer matters, the honesty has to come from your system.** That is the rule this chapter exists to state: treat every declaration as unverified by default. Not *usually right*. Not *probably fine*. **Unverified** — until you have checked it against a source outside the model.

## What "unverified" actually means in practice

It does not mean paranoia. It does not mean every answer needs a research team. It means one habit, applied at the right moment:

When a model states a fact, ask *where would I check this?* If you have a source — a document, a database, a person who knows, a measurement you can run — check it. If you do not have a source, then you do not have an answer. You have a *plausible completion*, and the difference between those two is the whole book.

The check is cheap when the question is cheap. *What is the capital of France?* — you know, or you can know in five seconds, and the model is a fast way to get a confirmation you already hold. *What is the capital of Zubrowka?* — there is no source, because there is no country, and no amount of asking the model will produce one. The model cannot tell you which case you are in. **Only your system can.**

That is the division of labour this book keeps returning to. The model is superb at transforming material you supply. It is not a source of material. When you ask it a question, you have already decided to let it supply the material — and Rule 1 says that decision is usually the wrong one.

## The sting

Here is the part that makes this chapter different from a complaint.

**The models are getting better at this. And that makes it worse.**

Every improvement in fluency, in coherence, in the naturalness of the output, is an improvement in the *mask*. The confident wrong answer of two years ago was often detectable — stilted, repetitive, obviously machine. The confident wrong answer today is polished. It has headings, citations, qualifications, a professional tone. It reads like the work of someone who knows what they are doing.

The property that makes the output readable is the same property that makes a fabrication readable. They are not separable. Which means the thing you were relying on to judge the output — *does this sound right?* — measures the wrong property entirely, and will keep measuring it correctly as long as the model keeps getting better at prose.

So the fix is not a better model. A better model is a *better mask*. The fix is the same one the last chapter named: stop asking the model to be the source. Give it the facts. Check what it does with them. Keep the judgement.

## What changes

The shift is one sentence:

> **Treat every declaration as unverified until you have checked it against a source outside the model.**

Not *usually right*. Not *probably fine*. Unverified — by default, every time, until the check happens.

That is not a restriction on the tool. It is the price of using it at all, and it is a small price. The check is fast when the question is small. The check is *you* when the question is yours. And when the question is one only a source can answer — a document, a database, a measurement, a person who was there — the system's job is to go get that source, not to improvise an answer in its place.

The next chapter asks the obvious follow-up: if the model cannot tell you when it does not know, and you cannot prompt that ability into it, what *can* you do? The answer is not a bigger model, and it is not a better prompt. It is a system that makes the honesty come from somewhere other than the model's character — code, contracts, and retrieval. That is the rest of this book.

---

*Verification: the claim that confidence and accuracy come from the same machinery is the book's thesis (00-BOOK.md §2) and is argued, not asserted, in this chapter. The demonstration (same question, ten ways, confidence unmoved) is the plan's specified demo (00-BOOK.md §7, Ch. 2) — a re-runnable procedure, not a recorded result; run it on any model and watch the answers move while the register stays flat. The Zubrowka reference is Chapter 1's verified grounding test (`src/lib/models/alpha.ts`, PersonalAI-Dashboard). No load-bearing claim in this chapter rests on a model's self-report. ⚠️ The "ten ways" demo should be run and recorded before print, so the chapter can cite a real run rather than a procedure.*
