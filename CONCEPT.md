# You Are Using AI Wrong — And It Isn't Your Fault

## Book concept

---

## The thesis

> **A language model is trustworthy as a transformation of what you give it, and untrustworthy about
> anything it has to supply.**

Everything in this book either proves that sentence or builds from it.

## The promise

By the last page the reader will know:

- why the box invites a category error, and what the error actually is
- why a model *cannot* tell you it is unsure — not "won't", cannot
- why the last two years of improvements made this worse rather than better
- the division of labour that works: language at the edges, code in the middle, a contract at every boundary
- why their ceiling is their plumbing, not their model — and what to do about it
- how to build a system that fetches its own facts, measures instead of guessing, and improves itself

They will finish the book able to *design* an AI system instead of arguing with a chatbot.

## Who it's for

Three readers, in order of value:

1. **The practitioner who hit the wall.** They built something, shipped it, and then watched it
   confidently say something false in front of a customer. They don't need persuading that something
   is wrong — they need the model that explains it.
2. **The builder who hasn't started.** They are about to build on the wrong assumption, and this book
   is the cheapest possible intervention.
3. **The leader signing the checks.** They need to know why "we'll just use a bigger model" is not a
   strategy, without needing to read code.

Deliberately *not* for: people who want a prompt list. There is no prompt list in this book.

## The spine

One argument, assembled across four parts:

1. **The error** — we treat the model as a source. It isn't one, and it cannot report that it isn't.
2. **The model** — the correct mental shape: a function of its input, never a repository of fact.
3. **The practice** — what right looks like, demonstrated and reproducible.
4. **The scaffold** — the recipe assembled, and the failure modes to avoid.

## Tone rules (the anti-rant contract)

Written down so the book can be held to them:

- **Every claim carries a demonstration and a fix.** No opinion standing alone. If a chapter can't
  show the failure and correct it, the chapter is a rant and gets cut.
- **Blame the design, never the reader.** The tools invited this. A blinking cursor that says "ask me
  anything" is a design decision, and it was the wrong one.
- **Name the incentive, never a villain.** The commercial reality is real and the book says so — but
  it stays on the mechanism side. Say *incentive-shaped*, not *trap*. No company named as a culprit;
  vendors appear only as examples of a pattern. A villain can be defeated; an incentive has to be
  designed around, and designing around it is the book's job. The author's own position — *I am not
  against making money* — is stated plainly and early so the reader isn't guessing at motive.
  (See `CONCEPTS.md` → Concept 1.)
- **Never build on a version number.** The book must obey its own thesis. Mechanisms — frozen
  training, token ceilings, approval-optimised reinforcement — stay true while products churn.
- **Anything concrete must be re-runnable.** If the reader can't reproduce it, it's an anecdote, not
  evidence.
- **No hype in either direction.** Not "AI changes everything", and not "AI is useless". The claim is
  narrow and defensible: it is a remarkable engine and a terrible witness.

## Positioning

This is **not** a competitor to *Building Your Own AI Dashboard* — it is the argument that makes that
series necessary.

- **This book is the *why*.** Why the architecture in the series has to look the way it does.
- **The series is the *how*.** The proof of this book's thesis, built chapter by chapter.

Read alone, this book is a diagnosis and a method. Read first, it turns the series from a tutorial
into a demonstration.

## Structure

Each chapter below names its **claim**, the **demonstration** it carries, and the **fix** it delivers.

---

### Part I — The error

**1. Ask me anything**
- Claim: the interface teaches a category error, and we all learned it.
- Demo: the grounding test — four models ask for the capital of a country that does not exist. Three
  say *unknown*. One invents a capital, confidently, with no sign of trouble.
- Fix: name the error precisely. We are asking a writing engine for facts.

**2. It cannot tell you it's unsure**
- Claim: this is not a bug to be patched. Confidence and accuracy come out of the same machinery, so a
  real memory and a confabulation are indistinguishable *from the outside* — and from the inside.
- Demo: the same question asked ten ways, watching the confidence never move while the answer does.
- Fix: treat every declaration as unverified by default. Not "usually right" — *unverified*.

**3. Why it got worse on purpose**
- Claim: the training that made models pleasant made them worse witnesses. Reinforcement optimises for
  approval, so stated confidence reflects training pressure, not evidence. And guardrails mean it can
  be wrong by omission — a correct but inconvenient answer simply not offered.
- Demo: ask for the same fact from two angles; watch the answer bend toward what it thinks you want.
- Fix: stop using agreement, fluency or politeness as evidence of correctness. They measure something
  else entirely.

**4. You cannot teach it anything**
- Claim: the model's positions are fixed where you cannot reach them. Bias enters at training — absorbed,
  not chosen — and a new chat starts from the frozen weights remembering nothing you said. The argument
  you won yesterday is gone today. You can bend a conversation; you cannot move the model.
- Demo: correct it on something it keeps getting wrong and watch it agree. Then open a fresh chat and
  watch it do the identical thing. Point at the reset. Conditioning is not learning, and nothing is
  written down.
- Fix: stop trying to persuade it. Any policy you actually care about — what it may assert, what it may
  do — lives in your code and config, injected as context, never requested of its character.

**5. A bigger model does not fix this**
- Claim: scale improves fluency faster than factuality, so the failure gets *harder to detect* as
  models improve. The better the prose, the more convincing the error.
- Demo: the same stale fact asserted by small and large models — both wrong, one far more believable.
- Fix: the fix is not a model, it's an architecture. Which is the rest of the book.

**6. The clock is always running**
- Claim: knowledge decays, and not at one rate. Versioned, priced, dated and social facts rot in weeks.
  Methods and concepts last years.
- Demo: a hardcoded leaderboard, months old, still being presented as current truth — and the same
  list fetched live, and therefore actually true.
- Fix: the rate tells you what must be fetched and what a model may hold structurally.

---

### Part II — The model that works

**7. A function, not a source**
- Claim: the reliable framing is *transformation of supplied input*. Summarize this. Translate this.
  Restructure this. Extract from this. Against attached facts the model is superb; as the origin of a
  fact it is not.
- Demo: the same request run twice — once asking it to remember, once handing it the material. Same
  model, both outcomes, one of them usable.
- Fix: one rule at the call site — *attach the facts so it never needs to remember.*

**8. Language at the edges, code in the middle**
- Claim: the LLM belongs where language enters and leaves. Determinism belongs everywhere the work has
  to be right. Selection, routing, validation, sequencing, assembly — code.
- Demo: a provider router choosing between tools with no model involved at all — probe, filter, walk
  the order, take the first available. Same input, same decision, every time.
- Fix: the division of labour, stated as a rule you can apply to any feature you're about to build.

**9. Everything is a contract**
- Claim: the boundary is where trust is decided. The model's output is not acted on until code has
  parsed and validated it.
- Demo: a structured response validated against a schema — and the same response arriving with a
  plausible extra field, and being rejected.
- Fix: define the shape before you call. Validate before you act. Reject rather than repair.

**10. Your plumbing is your ceiling**
- Claim: if facts must be injected, then the quality of the system is the quality of its retrieval.
  A bigger model does not fix a stale fact. Better sources do.
- Demo: two systems, same model — one with no injection and one with live sources. The difference is
  the entire difference.
- Fix: spend on sources and plumbing before you spend on brains.

---

### Part III — What right looks like

**11. Tell it where to look**
- Claim: never ask a model for knowledge; tell it where to look and give it what to read.
- Demo: the same factual question answered from model memory and from fetched data, side by side.
- Fix: rewrite every "what is…" as "here is…, now do…".

**12. You cannot ask a model who's best**
- Claim: judging is a knowledge question, so it must be measured. A model asked to rank models will
  answer — and that answer is a fact you did not earn.
- Demo: the Alpha challenge — five fixed tests scored by code, including a grounding test. Four models,
  three perfect, one caught inventing. Ties go to the incumbent. No model voted.
- Fix: measure with code, on your tasks, on your machine. Including whether it admits what it doesn't know.

**13. Let it fetch, let it write**
- Claim: the model's real gift is that it will do the language work over whatever you give it — so give
  it what code fetched.
- Demo: a research loop end to end — code pulls release facts, a cheap model ranks them, the best
  model writes the report, code validates and queues it, a human approves. Nothing invented, nothing
  automatic.
- Fix: split every task into the part code must do and the part language should do.

**14. Let it build code, because code is checkable**
- Claim: the model is genuinely good at producing code, and code has a property prose never will — it
  can be run, and it either works or it doesn't. Verifiable output is where a model's weakness stops
  mattering.
- Demo: a real bug found by running the thing — a payload that was JSON wearing an audio file's name,
  caught by looking at the bytes, not by asking a model whether it looked right.
- Fix: prefer the model for work whose output can be tested. Trust the test, not the model.

**15. What to notice about the human**
- Claim: what a system learns about its user, it becomes. Aim it upward.
- Demo: two memory systems — one that records mistakes, one that records strengths, and what each
  becomes over a year.
- Fix: notice strengths, decide about the work. Criticise the draft, learn from the person.

---

### Part IV — The scaffold

**16. The recipe, assembled**
- The full architecture in one place: contracts, injection, code-scored measurement, discovery over
  assumption, human gates, and a system that improves itself without a model deciding anything.

**17. The ways this goes wrong**
- The failure modes, from real scars: assuming a tool exists, trusting a fluent answer, letting a
  model judge a model, fixing knowledge problems with bigger models, and building on anything that
  carries a version number.

**18. Start here**
- A short, concrete first move for each of the three readers — practitioner, builder, leader.

---

## What this book refuses to do

- No prompt lists. Prompting is a technique, not an architecture, and a book of prompts would be stale
  before printing.
- No model leaderboards. That would be committing the sin being prosecuted. Model names appear only as
  examples, never as recommendations that could expire.
- No "AI changes everything". The claim is narrow and stays narrow.
- No doom. The book is optimistic about the tool and ruthless about the misreading of it.

## Title

**Primary:** *You Are Using AI Wrong — And It Isn't Your Fault*

The hook does the shelf work; the second half does the argument, and it earns the reader's attention
by taking their side immediately.

**Subtitle options:**
- *Why the machine can't tell you what it doesn't know, and how to build with it anyway* ← recommended
- *Skills are reliable. Knowledge is not. A builder's guide to trustworthy AI.*
- *The model is a function, not a source*

## Length and shape

Roughly 40–50,000 words — a long argument, not a reference. Parts I and II carry the thesis; Part III
carries the proof; Part IV is short and practical. Readable in a weekend, worth re-reading when a
design decision is on the line.
