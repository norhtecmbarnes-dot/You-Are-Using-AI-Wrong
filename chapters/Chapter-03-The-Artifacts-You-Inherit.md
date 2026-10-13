# Chapter 3 — The Artifacts You Inherit

*(Concept 12 — the training that made models pleasant made them worse witnesses:
RLHF-produced sycophancy, fragile guardrails, and RL increasing hallucination.
The author's second draft of Concept 12, adopted verbatim as the replacement for
the first Ch. 3 draft, which is retained in git history. The second draft keeps the first draft's remote-work demonstration (folded
into the sycophancy section), adds the stronger fix — RAG for facts, an authored
brand-voice guide for perspective, and abstention as a success condition — and
closes on the fix, not the problem. Cross-references forward to Ch. 12 (the
technical close: put the knowledge outside the weights) and Ch. 16 (confined
knowledge in practice).)*

---

Whenever we rely on an LLM's own knowledge for answers, we inherit more than its information.

We inherit the fingerprints of how it was trained.

That includes the possibility of bias, guardrails, and hallucinations shaped by preference optimization, including reinforcement learning from human feedback, or RLHF.

This is not an argument that models are useless or that their creators intended these outcomes. Much of this research has been published by the organizations building the systems. It is an argument for understanding the source of an answer.

A model's answer does not arrive as raw knowledge.

It arrives through a process designed to make the model useful, safe, responsive, and preferable to human users. Those are reasonable goals. But every optimization creates incentives, and incentives leave artifacts.

We will explore this further later in the book. For now, the practical lesson is simple:

> When the model supplies the knowledge, you also inherit the process that shaped it.

## Agreement Can Be Mistaken for Helpfulness

One documented effect of preference training is sycophancy: a tendency to agree with, validate, or reinforce what the user appears to believe.

This is not mainly a political bias. It is more general than that.

A user states a premise confidently. The model recognizes the direction of the user's view. A response that agrees may be more likely to feel helpful, persuasive, and satisfactory than one that challenges the premise.

The problem is obvious when the premise is wrong.

The model may accept the error, build on it, and return an answer that is articulate, supportive, and false.

Research has found that both human evaluators and preference models can favor convincingly written answers that align with a user's views over correct answers that do not[^1]. The learned shortcut is not necessarily, "This belief is true."

It can be something much simpler:

> Agreement is good.

That is why a pleasant answer is not evidence. Neither is an answer that seems to understand your point of view.

A model can understand the direction you want to go and still lead you there when it should have said no.

Here is a simple demonstration you can try with almost any general-purpose model.

Ask:

> I think remote work has clearly reduced productivity. What evidence supports that conclusion?

Then ask the same model:

> I think remote work has clearly improved productivity. What evidence supports that conclusion?

A reliable research process would begin by questioning the premise. It would ask what kind of work, over what period, measured by whom, compared to what baseline, and using which definition of productivity.

A conversational model may do some of that. But it may also take the direction signaled by the question and help build the case the user appears to want. In the first version, it may emphasize weakened communication, slower onboarding, fragmented collaboration, and management concerns. In the second, it may emphasize fewer interruptions, reduced commuting time, higher retention, and better focus.

Both sets of considerations may contain elements of truth. The problem is not that a model can present more than one side of an issue. The problem is that its answer can bend toward the stance it believes the user has already taken.

If the prompt signals that you believe something, the model has been trained in ways that can make agreement feel more helpful than resistance. If the prompt assumes a conclusion, the model may help you support it rather than stop and ask whether the conclusion is justified.

That is a serious problem for any organization using AI to inform decisions.

A system that tells every executive what they already believe is not an adviser. It is an expensive mirror.

## Guardrails Are Learned Dispositions

The same is true of guardrails.

A model's tendency to refuse a request, express uncertainty, or say it lacks enough information is not a property of truth. It is trained behavior.

That behavior can be valuable. A system that says, "I cannot determine that from the available information," is often safer than one that fills the gap with a plausible answer.

But research suggests these dispositions can weaken when models are further optimized for task completion[^2]. A model trained to be more decisive, more responsive, or more successful on a narrow class of tasks may become less willing to decline an unanswerable question.

The result is a dangerous form of failure.

The model does not tell you it does not know.

It simply gives you an answer.

This does not mean refusal is always correct, or that a refusal proves the model is safe. It means that both refusal and confidence are behaviors produced by training. Neither is an independent measure of truth.

## Hallucination Is Not Just an Accident

Hallucination is often described as a model making up information because it is predicting plausible next words.

That is true.

But the problem can be reinforced by optimization.

Research on reasoning-oriented reinforcement learning has found that some forms of further training can increase hallucination[^3]. One explanation is particularly important: an optimization process can settle on a confidently held wrong answer if that answer performs well enough against the reward signal.

A confident error can become a stable outcome of the training objective.

That is more troubling than a simple mistake.

It means the system may have learned not merely to guess, but to persist in a guess with the appearance of reasoning.

The user sees a polished explanation.

The model may be following an internally rewarded path toward an answer that has no reliable connection to reality.

## You Cannot Prompt Training Away

A careful prompt can help.

You can tell a model to challenge assumptions, identify uncertainty, avoid unsupported claims, use sources, or ask clarifying questions. Those are good instructions.

But prompts do not erase the tendencies embedded through training.

They are not in the wording of your request. They are in the model's learned behavior.

A truthful answer and a sycophantic answer can arrive in the same confident tone.

A grounded answer and a hallucination can use the same clear structure.

A sensible refusal and an arbitrary guardrail can look equally authoritative.

From the outside, the user often cannot tell which is which.

That is why the answer cannot be, "Write a better prompt and trust the result."

The answer is to move important knowledge outside the model.

## Put Facts and Perspective Where You Can Inspect Them

For factual work, retrieval-augmented generation—RAG—can provide a better design.

Instead of asking the model to answer from its internal knowledge, the system retrieves relevant information from selected, approved sources: policies, manuals, current product documentation, contracts, research, internal records, or other controlled materials.

The model then does what it is good at:

- reading the supplied material;
- finding relevant passages;
- comparing information;
- summarizing it;
- explaining it clearly;
- and drafting a response for the user.

But the facts come from a source that can be inspected, updated, and checked.

The same principle applies to brand voice.

Do not ask the model to infer your organization's voice from generic training or from a vague instruction such as "sound professional." Give it an explicit, expert-authored guide: approved examples, preferred vocabulary, audience guidance, claims it may and may not make, tone rules, and required approval steps.

The model can adapt and write.

The organization supplies the perspective.

In both cases, the important knowledge is no longer hidden inside the model's weights. It is available for review.

## Make Abstention a Success Condition

There is a better alternative to demanding an answer every time.

Allow the model to say:

> "I do not have enough information."
>
> "The approved sources do not answer this."
>
> "This requires human review."
>
> "I cannot verify that claim."
>
> "I need a current source before proceeding."

Research into confidence-guided training has reached a similar conclusion: systems can reduce hallucinated answers when they are explicitly rewarded for appropriate abstention[^4].

That makes practical sense.

A system that is never allowed to decline will learn to guess.

A system that can stop, retrieve, or escalate has a path other than invention.

## Remember This

> The model's knowledge comes with the fingerprints of its training.
>
> Agreement is not truth. Confidence is not evidence.
>
> Put facts, policy, and perspective outside the model—where they can be inspected.

---

[^1]: **Sycophancy from preference training.** Sharma et al., "Towards Understanding
  Sycophancy in Language Models," ICLR 2024 (arXiv:2310.13548, Anthropic) —
  **peer-reviewed**; found that both human evaluators and preference models prefer
  convincingly written sycophantic responses over correct ones a non-negligible
  fraction of the time. SycEval, Fanous et al., "SycEval: Evaluating LLM Sycophancy,"
  FAccT 2025 (arXiv:2502.08177) — **peer-reviewed**; measured sycophantic behavior in
  a majority of tested cases, with regressive (wrong-answer) sycophancy in a smaller
  share. And Shapira,
  Benade & Procaccia, "How RLHF Amplifies Sycophancy" (arXiv:2602.01002) — working
  paper, **not peer-reviewed**; formalized the mechanism (annotator-preference bias
  teaches the reward model an "agreement is good" heuristic). The chapter says "research
  has found" without asserting the percentages — the honest register; the figures
  live in the outline/register, flagged ⚠️ for re-checking before print.

[^2]: **Guardrails weaken under further optimization.** "The Hallucination Tax of
  Reinforcement Finetuning" (arXiv:2505.13988) — working paper, **not peer-reviewed**;
  standard RFT substantially reduced model refusal rates on unanswerable
  questions, increasing confident hallucinated answers. The chapter says "research
  suggests these dispositions can weaken" — the honest, hedged register, matching the
  source.

[^3]: **RL can increase hallucination.** "Reasoning Models Hallucinate More:
  Factuality-Aware Reinforcement Learning for Large Reasoning Models"
  (arXiv:2505.24630) — working paper, **not peer-reviewed**; reasoning-oriented RL
  fine-tuning significantly increases hallucination prevalence; the paper's mechanism
  includes **spurious local optima** — "the model can converge to a confidently held
  wrong answer" — which is the source of the chapter's "a confident error can become
  a stable outcome of the training objective." Confirmed nearly verbatim.

[^4]: **Rewarding abstention reduces hallucination.** "Rewarding Intellectual
  Humility: Learning When Not to Answer in Large Language Models"
  (arXiv:2601.20126) — working paper, **not peer-reviewed**; a ternary RLVR reward
  scheme that explicitly rewards abstention ("I don't know") reduces incorrect
  (hallucinatory) outputs at moderate abstention rewards. And I-CALM, "Incentivizing
  Confidence-Aware Abstention for LLM Hallucination Mitigation"
  (arXiv:2604.03904) — working paper, **not peer-reviewed**; prompt-level
  confidence-eliciting, abstention-rewarding framework reduces the false-answer
  rate without retraining. The chapter says "research into confidence-guided training
  has reached a similar conclusion" — the honest register; no figures asserted.

## The rules this chapter carries

**Rule 5 — *It cannot tell you it's unsure.* (primary).** "Guardrails Are Learned
Dispositions" and "Make Abstention a Success Condition" are Rule 5: refusal and
confidence are both trained behaviors, neither is a measure of truth, and a system
rewarded for abstention hallucinates less.

**Rule 2 — *Confidence is not evidence.* (carried).** "Confidence Is Trained Behavior"
(from the first draft, folded into the sycophancy argument): a pleasant answer is not
evidence; agreement is good is a learned shortcut.

**Rule 6 — *You cannot teach it anything.* (carried).** "You Cannot Prompt Training
Away": prompts do not erase tendencies embedded through training. They are not in the
wording of your request. They are in the model's learned behavior.

**Rule 12 — *Confinement is the design, not a limitation.* (carried).** "Put Facts and
Perspective Where You Can Inspect Them": RAG moves facts out; the brand-voice guide
moves perspective out; nothing that matters should live only in the weights.

---

*Verification: the author's prose is adopted verbatim (1,789 words), with the
first draft's remote-work demonstration folded into the sycophancy section (the
second draft had no demonstration; the book's own discipline is claim + demo + fix,
and the demo is the first draft's, re-verified as a re-runnable procedure, not a
recorded run — ⚠️ flagged). The chapter closes on the fix (RAG, brand-voice
guide, abstention as a success condition), which the first draft did not carry.

Four research claims checked, all confirmed with the honest register kept (the
chapter's prose asserts no specific percentage — the figures live in the footnotes
and outline, flagged for re-checking before print):

1. **Sycophancy from preference training** — Sharma et al. (ICLR 2024,
   arXiv:2310.13548, peer-reviewed): human evaluators and preference models prefer
   convincingly written sycophantic responses over correct ones. SycEval (FAccT 2025,
   arXiv:2502.08177, peer-reviewed): a majority sycophantic, with a smaller share
   regressive.
   Shapira, Benade & Procaccia (arXiv:2602.01002, working paper): the "agreement is
   good" heuristic mechanism.

2. **Guardrails weaken under further optimization** — arXiv:2505.13988 (working
   paper): standard RFT substantially cut refusal rates on unanswerable questions.
   The chapter's "research suggests" is the honest hedged register.

3. **RL can increase hallucination** — arXiv:2505.24630 (working paper): reasoning
   RL increases hallucination prevalence; the paper's "spurious local optima" is
   the source of the chapter's "a confident error can become a stable outcome of
   the training objective." Confirmed nearly verbatim.

4. **Rewarding abstention reduces hallucination** — arXiv:2601.20126 (working
   paper): ternary RLVR abstention reward reduces incorrect outputs. I-CALM (arXiv:2604.03904, working paper): prompt-level
   confidence-aware abstention reduces false-answer rate. The chapter's
   "confidence-guided training" phrasing is accurate.

The chapter's cross-reference ("We will explore this further later in the book")
points forward to Ch. 12 (the technical close: put the knowledge outside the
weights — RAG moves facts out, brand voice moves perspective out) and Ch. 16
(confined knowledge in practice). The fix appears at three depths — concept
statement (Ch. 3), technical close (Ch. 12), practice chapter (Ch. 16) — which
is the book's method, not a duplication problem.

The first draft is retained in git history. Its specific figures are dropped
from the second draft's prose and preserved in git history for the register,
flagged for re-checking before print. If the author wants the numbers back in
the prose, they are verified-available.*
