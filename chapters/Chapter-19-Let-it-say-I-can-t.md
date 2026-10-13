# Chapter 19 — Let it say I can't

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

**Claim.** **a small model should be asked whether the job is its to do, and "no" should be the cheap answer.** Everywhere else in this book a model's confidence is worthless — because it is reported about facts it cannot see. This asks a different kind of question: not *"is this true?"* but **"is this mine to do?"** — and *that* answer is checkable, because you find out immediately whether the cheap path held.

**Demonstration.** the escalation bus — the smallest available model triages the request, and the prompt's fail-safe is the whole design: ***"If you're UNSURE, lean toward canHandle: false."*** Doubt escalates. The cheap mistake is the default; the expensive one requires confidence. If the assessment itself fails, the fallback still leans the right way.

**Fix.** **the smallest model that correctly declines is the model you need.** Every task the small model *accepts* is a task that can move down — off the cloud, off the GPU, off the big machine. **The capability bus is a hardware-migration engine disguised as a router.** - ⚑ *The hardware claim, from the author's own experience, and it should be told that way:* research on models as small as **1.5B parameters, on CPU-only laptops**. The usual story is that AI demands more compute; this design makes the requirement **fall over time**. - ⚠️ Caveat to carry: do **not** claim the model knows its limits. It doesn't. The value is architectural — *a cheap default, a cautious failure, and a bounded cost of being wrong.*

---

## Concept 7 — Let the model declare its own limits

> This is the captured material this chapter expands. It is in `CONCEPTS.md`.

*The capability bus. Outside the notebook frame entirely — this one is not about what a model knows, but
about what it will admit it cannot do.*

**As stated by the author:** (verbatim — preserve the words; they carry intent)

> I believed I described this in a model escalation message service that provided a mechanism for models
> to test their limits and only do tasks they were confident that they could complete. I have had good
> luck doing research using models as small as 1.5b parameters--even running these tasks on laptops
> without CPUs. Giving a model the ability to test its limits opens up the possiblity of migrating tasks
> to smaller and smaller hardware.

**It exists, and it is already built — `src/lib/services/model-bus.ts`, 699 lines, in both repos.** Its
own header states the architecture:

> *"Uses self-assessment: local model decides if it can handle a task or needs to escalate to a smarter
> cloud model. 1. Small local model receives query with self-assessment prompt. 2. Model honestly
> evaluates: can I answer this well? 3. If yes, process locally (cheap, fast). 4. If no, escalate to
> user's preferred cloud model."*

### The question the author remembered — it is in the prompt

`getSelfAssessmentPrompt()`, verbatim:

```
You are a tiny local AI model with limited capabilities. Your job is to be HONEST about what you can handle.

Analyze the user's query and decide:
1. Can you answer this COMPLETELY and ACCURATELY right now?
2. Would the user be SATISFIED with your answer?
3. Should this go to a smarter cloud model?

Rules:
- If the query is a simple fact, definition, calculation, format, or routine task → canHandle: true
- If the query requires deep reasoning, up-to-date knowledge, creative writing, complex analysis → canHandle: false
- If you're UNSURE, lean toward canHandle: false
- If the query is in a language you weren't trained on, lean toward canHandle: false

Answer ONLY with valid JSON... {"canHandle": true/false, "reason": "...", "suggestedTier": 2}
```

**⚑ And the most important line in the whole design is the fail-safe:**

> **"If you're UNSURE, lean toward canHandle: false."**

Doubt escalates. The system is built so that the **cheap mistake** ("I'll pass, send it up") is the
default, and the **expensive mistake** ("I've got this") requires confidence. That single line is what
makes the mechanism safe to run unattended.

### Why this is the book's concept, and not just an implementation detail

**It is the one place in the entire book where a model's self-report is worth something — and the reason
is precise.** Everywhere else, confidence is worthless because it is reported about *facts the model
cannot see*. Here the model is asked a different kind of question: not *"is this true?"* but *"is this
job mine to do?"* That is a routing decision, and routing decisions are **checkable** — because you find
out immediately whether the cheap path held.

**So the design does not trust the model's self-assessment. It bounds it.** The book must say it that
way: the value is architectural, not epistemic.

### And it inverts the hardware question — which is the payoff

The usual story is that AI demands more compute. **This design makes the requirement fall over time.**

- `ModelTier` carries an explicit **`isCPUFriendly`** flag, and `local-small` is set to it.
- **BitNet is integrated** (`src/lib/services/bitnet.ts`, `/api/bitnet`) for Microsoft's 1.58-bit models —
  *"enabling AI inference on machines WITHOUT a GPU."*
- `docs/CPU-ONLY-SETUP.md` documents running on CPU alone and recommends **`qwen2.5:1.5b`** — 1.5 GB,
  ~2.5 GB RAM, rated *"Very Fast"*, *"Good"*, **"Recommended"**.

**And this is the practical consequence, which is the chapter's closing claim:**

> **The smallest model that correctly declines is the model you need.** Every task the small model
> *accepts* is a task that can migrate down — off the cloud, off the GPU, off the big machine. Start
> expensive, watch what the cheap model agrees to do, and move those tasks down. **The capability bus is
> a hardware-migration engine disguised as a router.**

**The 1.5B research claim is the author's first-hand experience, and should be presented as exactly
that** — *"I have had good luck doing research using models as small as 1.5b parameters"* is stronger
than any statistic the book could cite, because it is a report from someone who did it.

**Why it works:** (the sharp part)

1. **It is right-sizing by capability instead of by guess.** The `model-router.ts` escalates on *task
   type* — a static table. This escalates on *the model's own read of the job* — dynamic. Together they
   are the difference between a policy and a mechanism.
2. **It makes the failure cheap.** One extra triage call at `temperature: 0.3`, `maxTokens: 200`, on the
   smallest available model — and the response carries `costSavings` and a `delegationPath` so the
   routing is visible.
3. **It fails safe.** If the assessment call itself errors, the fallback is
   `canHandle: context.length < 500` — short task, handle it; long task, escalate. Even the failure path
   leans the right way.
4. **It produces the migration map.** The log of what the small model accepted *is* the list of tasks
   that no longer need the big machine.

**The handling rule:** (tone, framing, what to avoid)

- **Never claim the model's self-assessment is accurate.** It isn't, and it doesn't need to be. The claim
  is: *a cheap default, a cautious failure, and a bounded cost of being wrong.*
- **Quote the fail-safe line.** *"If you're UNSURE, lean toward canHandle: false"* is the design in one
  sentence, and it is the direct answer to the reader's reasonable objection — *"won't the small model
  just say yes to everything?"* No: the prompt is written so that uncertainty escalates.
- **Do not turn "would the user be satisfied?" into a promise.** It is a **routing** question. Say so, or
  a technical reader will (correctly) point out that a model cannot predict user satisfaction either.
- **Present the small-model numbers as reproducible, not as a benchmark.** Cite the CPU-only setup doc;
  do not invent a score.
- **Keep it distinct from the confinement ideas.** This concept is *not* about what the model knows. It
  is about what it will decline. **It sits outside the notebook frame** — and the book is stronger for
  having both axes.

**Where it lands.** **A new chapter in Part III, directly after "The most expensive model for
everything."** Working title: **"Let it say *I can't*."** Ch. 18 is the indictment of over-provisioning;
this chapter is the mechanism that makes the alternative work. It also pays off **Rule 14** (match the
effort to the question) and gives Ch. 25 ("The recipe, assembled") its second pillar.

**Guard rails:** (specific things the draft must not do)

- **Do not describe it as "the model knows its limits."** It does not. It is asked to make a routing
  call, under a prompt that biases toward declining.
- **Do not let the chapter become a product tour of BitNet or a particular small model.** The mechanism
  is the durable part; the models are not. **The book's own rule applies.**
- **Do not overstate the migration claim.** It is a direction, not a guarantee — some tasks will always
  need the big model. *"Falls over time"*, not *"falls to zero."*
- **Verify `qwen2.5:1.5b` still exists and still runs CPU-only before printing the specific figure.**

---

## The rules this chapter carries

**Rule 17 — *Let the small model say "I can't".* (primary).** A small model asked whether the job is its to do can answer usefully, because routing is a checkable question. The chapter is Rule 17 — let the small model say 'I can't' — and it exists precisely because of Rule 5: everywhere else the model cannot report its own uncertainty.

**Rule 5 — *It cannot tell you it's unsure.* (carried).**

## DRAFT

*(write it here. Target roughly 1,600 words. Same rule as the rest of the book: every*
*load-bearing claim to a source, citations kept, nothing invented, anything unverifiable*
*marked ⚠️ rather than smoothed over.)*
