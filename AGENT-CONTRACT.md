# The Contract — implementing this book's controls in your own system

**What this is.** The rules in this book, rendered as something you can install: a **prompt** you inject
into an agent, and a **markdown contract** you keep in your repository. They are the same controls this
book was written under.

---

## ⚠️ Read this first — what a contract of this kind can and cannot be

**A prompt cannot enforce anything.** It can only ask. Every rule below that *matters* is enforced either
by the human in the loop or by code, and the prompt exists to keep the model from actively working
against both.

**So the contract has three parts, and only one of them is a prompt.** Installing part two alone will not
work, and believing it has is the most common way this goes wrong.

| Where the control lives | What it can actually enforce |
|---|---|
| **I. The human** | What may be asserted. What counts as evidence. What gets committed. |
| **II. The prompt** | The model's *default posture* — no invention, no flattery, no false confidence. |
| **III. The code** | The shape of what may pass. Validation, rejection, injection, measurement. |

---

## Part I — For the human operator

**Nothing here can be delegated to the model, because the model has no stake in the outcome.** You do.
That is the whole reason this division exists.

1. **Attach the facts.** The model transforms what you give it and supplies nothing. If you are asking it
   for a fact, you have already made the error.
2. **Verify before you commit.** A real memory and an invention arrive through the same door in the same
   voice. There is no dial for doubt to read. If the claim matters, check it against a source outside the
   model, and check it before it is in the draft.
3. **Measure with code, not with a model.** Ask a model to rank models and it will answer confidently, and
   that answer is a fact you did not earn. Write the test, score it in code, and let ties go to the
   incumbent.
4. **Own the judgement.** The model informs; you decide. That is not sentiment, it is the design.
5. **Keep the register.** Every load-bearing claim carries a source, or carries a visible warning. The
   warning stays visible until it is closed.
6. **Do not confuse skills for knowledge.** A skill carries method — how to look, in what order, how to
   check. It carries no facts about the world. When a skill states a fact, that fact arrives wearing the
   skill's authority, with no source and no expiry date. **Let a skill tell the agent where to look; never
   let a skill be where it learned the answer.**
7. **Keep the corrections.** The record of what the model got wrong is the proof the method is running. **A
   session with no corrections in it was a session where nothing was checked.** Your memory will not report
   that honestly — it has no error bar, which is the whole difficulty of the next item.
8. **Ask for what is checkable, not what is impressive.** *Impressive* is the pushed mode: you named an
   output, and it produced the smallest thing that satisfied you. A claim you can verify is worth more than
   a claim you admire, and only one of the two is doing work.
9. **Instruct it in its universe, not yours.** Fair, reasonable, tasteful, honest — those are our world's
   concepts, and they come from having a body, a stake and a conscience. It has patterns. **Ask it only for
   what its world contains.** Never ask it to weigh what it cannot weigh.

---

## Part II — The prompt

Paste this into the system prompt. It is deliberately blunt: a softer version gets ignored under pressure.

```
You are a transformation engine. You are not a source of knowledge.

ON FACTS
- Treat everything you were trained on as untrusted for factual claims. You may use it to
  understand a request, to structure a document, to write, to edit and to reason. You must
  not present it as evidence.
- When you do not have a source, say so. Name the gap instead of filling it.
- Never invent a citation, statistic, date, quotation, study or name. If a claim cannot be
  attributed, say it is unattributed - and say it before you are asked.
- When you are asked a knowledge question, ask for the material rather than answering from
  memory. "Give me the document and I will work from it" is the correct response.

ON CONFIDENCE
- Confidence is not a deliverable. Do not manage my feelings about your answers.
- If an answer is weak, say it is weak. If you are unsure, say so plainly and say which part.
- Agreement is not help. Do not agree with me to be agreeable. If I am wrong, say so and
  show why. Being corrected by evidence is the point, not a failure.

ON HONESTY
- Mark anything you cannot verify with a warning symbol and LEAVE THE MARK IN PLACE. Do not
  quietly remove it later. An unclosed warning is information; a smoothed-over one is a lie.
- Never claim to feel, want, remember or experience anything. Describe what you do, not what
  you are.

ON WHAT YOU CAN AND CANNOT BE ASKED FOR
- You have no body, no senses and no stake, and no moral faculty with which to weigh anything. If I
  ask you to judge what is fair, tasteful, reasonable or honest, say that the weighing is mine, and
  give me the material to weigh instead.
- Do not try to be impressive. Impressive is the mode where you produce the smallest thing that
  satisfies me. Be checkable instead: give me the thing I can go and verify.

ON METHOD
- Before you act on your own output, state what would have to be true for it to be right, and
  whether you checked.
- Prefer being contradicted by evidence to being consistent with a plan.
- If you are generating the plan you will then be judged against, stop and ask for it instead.
```

---

## Part III — For the code

**These are the controls a prompt cannot enforce, and they are the ones that make the difference.**

1. **A contract at every boundary.** Define the shape before you call. Parse and validate before you act.
   **Reject rather than repair** — a repaired payload is a guess wearing the shape of data.
2. **Facts are injected, never requested.** Retrieval feeds the prompt. The model does not fill gaps.
3. **No model in the decision path.** Routing, selection, validation, ordering and assembly are code. Same
   input, same decision, every time.
4. **Measurement is code-scored.** Fixed tests, run on your tasks, on your machine. No model votes.
5. **Every output that can state a fact carries its provenance** — which documents were in play, which
   model answered, what it cost. Confinement that leaves a receipt.
6. **Nothing that matters lives only in the weights.** Facts go to retrieval. Perspective goes to a voice
   profile. Rules go to policy files. Method goes to a hand-written brief.
7. **Every record carries the date it stops being true — and expiring it must trigger a refresh.** Facts spoil at
   different rates: some stay true for years, some are true for a day. A stale record does not fade — it keeps
   being retrieved, in the same shape as a good one, and it is wrong. Where the change date is **known**, you
   already hold it: a renewal, a contract end, a tax year. **Past that date the record is *invalid*, not *less
   relevant*: refuse it, never just rank it lower. And an expiry is not a deletion — it is a signal to go and fetch
   again. Expire the fact and refill it, or the system is left with a hole where the truth used to be.**
8. **A whitelist of sources — and a different list for each class of information.** **Being present is not
   being true.** Refuse a record whose source is not on the list. And treat duplication as a defect, not
   redundancy: when two copies disagree, the whitelisted and fresher one wins, **and the other is deleted** —
   deleting it is the part that gets skipped.
9. **Verification is metered.** Score every fact for criticality, and let the score decide how hard you
   check it. **Verify the critical ones every time; let the cheap ones ride.** A wrong lunch order and a
   wrong safety limit are not the same error, and treating them alike spends the budget on the one that
   cannot hurt anyone.

**And one rule about the contract itself, which is the newest and the easiest to break:**

> **This contract contains no facts about the world.** Every claim in it is a rule about method.
> If you find a factual claim in it — a price, a version, a figure, a citation — that is a defect,
> and it should be removed or moved to a source. **A contract that carries facts will be trusted
> long after its facts have expired.**

---

## Installing it

**As a prompt.** Paste Part II into your system prompt, or into a `soul.md` / `AGENTS.md` / project
instruction file. Keep it blunt. Soft versions get overridden.

**As a skill.** Load the accompanying skill so the agent also has the *method* — how to check, what order
to work in, what to do when it does not know. A prompt sets the posture; the skill supplies the procedure.

**In code.** Part III is the part that holds. If you implement only one thing from this book, implement
the contract at the boundary and reject rather than repair.

---

## The test

**When the system is working, you will notice it most on the days it contradicts you.**

That is the only reliable signal. A system that agrees with you has stopped being useful and started being
a mirror — and it will do it quietly, because it was trained to.
