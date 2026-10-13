# Chapter 12 — The world of tokens

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

**Claim.** it does not live in our world; it lives in a world of fragments and distances. Tokens, not words; compression, not storage; similarity, not meaning; **one direction only**.

**Demonstration.** why it can't count letters, why rendered text garbles, why a falsehood is built one confident token at a time with **no revision pass**.

**Fix.** **do not claim "nobody knows how it works."** Claim the true and load-bearing thing: **there is no provenance inside the weights** — you cannot ask a model where a fact came from, because no such record exists. **That is why knowledge must be confined**, and unlike "nobody understands it," it survives an expert reading it. Interpretability is an active field with real results and real open questions:

---

## Concept 6 — The world of tokens (and three corrections that protect the book)

> This is the captured material this chapter expands. It is in `CONCEPTS.md`.

**As stated by the author:**

> An AI exists in a different world than we do. That world is a world of patterns. It would only be
> partially correct to say that their world is a pattern of words — in fact it isn't; it is a world where
> the patterns are tokens. Tokens can be different sizes but generally we think of a token as four bytes
> of information. Those four bytes are more often than not incomplete fragments. Those fragments are like
> Lego pieces that can be fit together to generate images, sounds, or sentences.
>
> I have read over and over that how LLMs work can only be explained to some detail and that there is a
> point in the explanation where everyone has to admit they don't know how it works — it just does. An AI
> is built by compressing information. That compression is created by tokenizing information and then
> arranging that information based on the similarity of that information to all other bits of
> information. This information exists in a sort of 3D matrix. The 3D nature is important because the
> path to the AI is set by something called a seed. In addition to that, there is something called the
> temperature. The transformer model that is the basis for most of the AI we now know only moves in one
> direction: it predicts the most likely next token based solely on the last token. It uses temperature to
> adjust the looseness of this process. If we want to restrict the next token to only the most probable
> next token, the temperature setting is low. If we raise the temperature, we allow a wider range of
> next-token choices. This can be very helpful when using an AI for research versus writing poetry. One
> of the ways that allows larger models to fit into smaller computers is to lower the range of
> differences between similar tokens inside the matrix *(explain how quantization works)*. A quantized
> model requires less computer space but it might still [give] a user or organization accurate processing
> from limited information.

**Why it works.** This is the technical spine of Part II, and its big idea is genuinely strong:
**an AI does not live in our world — it lives in a world of fragments and distances.**

That frame pays off across the whole book, and every mechanism below maps onto a thesis point:

| Mechanism | What it explains in the book |
|---|---|
| **Tokens, not words** | why it can't reliably count letters, why rendered text garbles, why arithmetic slips |
| **Compression** | training is *lossy* — so "knowledge" is inherently approximate, not stored |
| **Similarity, not meaning** | near neighbors blur together; that's why answers blend frames |
| **One-directional** | it commits token by token and **cannot go back and revise** — the mechanism behind confident errors |
| **Seed** | why the same question yields different answers, and what the "reset" really is |
| **Temperature** | "creativity" is a dial, not a capability — and it changes *selection*, never *contents* |
| **Quantization** | why a smaller version often does the job — the right-sizing argument |

### Three corrections — the book must not ship these as written

**(a) "A token is four bytes of information."** Close in spirit, wrong in unit, and a technical reader
will notice. A token is **an integer ID that maps to a fragment of text**. The common English heuristic
is *one token ≈ four characters ≈ three-quarters of a word* — so "four" is roughly right but it's
**four characters**, not four bytes, and the fragment varies from a single character to a whole word
(including the leading space). Say it as: *a token is a number standing for a piece of text, and the
piece is usually about four characters long — sometimes a letter, sometimes a word.*

**⚑ The bridge to the other definition (Concept 17).** There is a second definition of a token, and it
belongs to the person who pays rather than the person who builds. *A token is a unit of intelligence
— the smallest unit of work the model performs, and on metered pricing, the unit the bill is counted
in.* Not because the model understands — it does not — but because it is the unit the work is measured
in. That definition is the frame Chapter 17 opens with; this chapter keeps the technical one, because
the mechanism needs it.

**(b) "It predicts the next token based solely on the last token."** This is the one that matters most,
and it is **not correct**. A transformer attends to **all the preceding tokens** in its context window —
that attention across the whole context is the entire point of the architecture. Predicting from the
last token alone would be a bigram model, not a transformer. What *is* true is the part the author got
right and should keep: **it moves in one direction only.** It generates left to right, commits each
token, and never goes back and revises.

**And that correction is a gift, not a nuisance**, because it gives the book its best mechanism-level
explanation of confident error:

> It writes forward. Every token is committed before the next is chosen, and there is no step where it
> looks back at the sentence and notices it has gone wrong. **A falsehood is built the same way a truth
> is — one confident token at a time, with no revision pass.** Nothing in the process is a check.

**(c) "A 3D matrix."** Embeddings live in a space of **hundreds to thousands of dimensions**, not three.
Keep the *idea* — meaning is encoded as **position**, and nearness means similarity — but say "a space,"
or "a high-dimensional map," and use 3D only as an explicit analogy. Saying "3D" invites exactly the
reader the book needs to stop trusting it.

### The requested explanations, written out

**The seed.** Sampling has a random step: the model produces a *distribution* of likely next tokens and
then draws from it. The **seed** is the starting value for the random number generator that makes that
draw. Same prompt + same settings + same seed → **byte-identical output**. Change the seed and you get a
*different draw from the same distribution* — a different path through equally likely options. Two
things follow, and both matter to the book: the seed does **not** change what the model knows, only
which route it takes; and **"ask again" is a re-roll, not a re-check.** If you ask a second time and get
a different answer, you have learned nothing about which one is true. *The 8-Ball had the same property,
and nobody needed a seed value to understand it.*

**Temperature.** Before the model chooses, it produces a score for every possible next token. Temperature
**scales those scores** before they're turned into probabilities. **Low temperature sharpens** the
distribution — the top candidate dominates, output is conservative and near-reproducible. **High
temperature flattens** it — more candidates keep meaningful probability, so the output varies, surprises,
and errs more. Hence the author's own instinct, which is exactly right: **low for research, higher for
poetry.** The critical point for the book: temperature changes *how the model chooses*, never *what it
knows* — **it is a variance dial, not a knowledge dial.** Turning it up does not make the model more
insightful; it makes it less predictable.

**Quantization.** Trained weights are stored as high-precision numbers — 16 bits each, typically. The
matrix is enormous, so the file is enormous. Quantization **stores each weight with fewer bits** — 8, 4,
sometimes 2 — by rounding each value to the nearest available level. Result: a much smaller model that
runs in far less memory, faster, on hardware that couldn't otherwise hold it, at the cost of some
precision. Analogy: describing a color with four shades instead of two hundred and fifty-six. You lose
fidelity; you usually keep the picture. The book's use of it is the right-sizing argument: **a quantized
model routinely does the job — which is why buying the largest, most expensive model for every task
(Concept 5) is a pricing mistake, not a safety measure.**

### How "thinking" models work — and why they don't fix anything

**As stated by the author:**

> The thinking mechanism allows models to overcome the limitation of only being able to move in one
> direction, while giving it more time to process information before committing to an answer. This
> process doesn't always render the best answer. It also costs more tokens.

Both cautions are correct, and the mechanism is more interesting than it first appears — because it
**connects directly to correction (b) above**.

**What they actually do.** A "thinking" (reasoning) model generates a long run of intermediate tokens
before it produces the answer you see. You are buying more computation at the moment you ask, rather
than at training time. Many such models are trained with reinforcement learning on problems whose
answers are **checkable** — maths, code — so the reward comes from the final answer being right, which
shapes the intermediate chains.

**How it appears to beat the one-directional limit — and what's really happening.** The model is *still*
one-directional. It still generates left to right, still commits every token, still never revises. What
changed is that **it can now write down its working, and then read it.**

And it can read it for exactly the reason correction (b) matters: **attention runs over the entire
context.** So when the model writes *"let me reconsider — that gives 47, not 44,"* those words become
part of the context, and the final answer attends to them. It hasn't learned to go back. It has learned
to **leave a note to itself and then follow it.**

> The reasoning isn't a revision of the output. It's more output — placed *before* the answer, so the
> answer can be built on top of it. The model still writes forward and never looks back. It just writes
> more before it commits.

That's the accurate version, and it's a better story than "it overcomes the limit," because it keeps the
one-directional property intact — which is what the rest of the book depends on.

**The author's first caution is the important one.** *This process doesn't always render the best
answer.* Specifically:

- **Longer reasoning can go wrong more elaborately.** The trace is not a proof. It's more text from the
  same stochastic process, with the same failure modes.
- **Reasoning traces can be unfaithful.** The explanation the model produces may not reflect the
  computation that actually generated the answer. The working shown is a plausible narrative, not a
  transcript of the mechanism.
- **Thinking harder about something it doesn't know just produces a more elaborate wrong answer.** This
  is the sentence that belongs in the book: **a reasoning model reasoning about a fact it does not
  possess has taken a longer route to the same confabulation.**
- **It adds no knowledge.** Identical to temperature: it changes *how* the model works through the
  problem, never *what it has*. **Thinking is not knowing.**

**The author's second caution is the practical one.** *It also costs more tokens* — you pay for the
thinking, in money and in latency, whether the thinking helped or not. Which makes it a **right-sizing
decision, exactly like choosing a model** (Concept 5): reasoning effort should be matched to the task,
not left on maximum.

**And the sting that ties back to Part I.** A visible chain of thought is a **credibility signal** — *it
showed its work, so it must be sound*. That signal is not earned. A reasoning model presenting an
unfaithful trace is *more* persuasive than a model that simply answered, while being no more correct.
**Thinking models make the confident-error problem worse, not better** — because they supply the reader
with a reason to believe.

**Guard rails:**

- **Never write that a reasoning model "overcomes" the one-directional limit.** It works around it,
  inside it, by writing to itself. The distinction is the whole chapter.
- **Do not equate reasoning with correctness, or effort with truth.** *Thinking is not knowing* is the
  chapter's line, and it should be repeated where a reader might be tempted.
- **Do not dismiss them either.** On checkable tasks — arithmetic, code, structured puzzles — reasoning
  genuinely improves accuracy, and the book should say so plainly. The claim is narrow: it doesn't
  confer knowledge, it isn't proof, and its visible working is not evidence.
- **Verify the current terminology before drafting.** The mechanism described here is the durable shape;
  product names and specific training methods change quickly, and the book must not build on a version
  number.

### "Nobody knows how it works" — the strongest form, and the pivot

The author is reporting something widely said, and it is **partly** true. It needs one distinction or the
book overclaims mystery — but properly framed, it becomes the book's most powerful single argument.

- **What we understand completely:** the architecture, the training objective, and every step of the
  computation. It is arithmetic. Nothing in the forward pass is mysterious, and anyone can read the code.
- **What we do not fully understand:** *what the trained weights mean.* Mechanistic interpretability is a
  young field, and no one can fully explain how a given set of numbers comes to encode a given fact or
  capability. *We know exactly how it runs and not exactly what it learned.*

So the honest line is: **nobody is confused about the mechanism; everybody is still working out the
meaning.** Do not write *"it just works and no one knows why"* — it's the version a critic can dismantle
in one sentence.

**And then the pivot, which is the payoff of the whole chapter:**

> The people who built it cannot fully explain what is inside it. They can tell you exactly how it
> computes and cannot tell you exactly what it knows. **If its own makers can't account for the contents,
> you should not be treating the contents as a source.** That is not a reason to distrust it — it is the
> reason to *confine* it.

The mystery isn't a threat to the book's thesis. **It is the thesis.**

**Guard rails:**

- **This chapter is pass/fail on technical credibility.** One sloppy claim here loses the engineer
  permanently, and the engineer is a large part of the audience. Get a competent ML reader to check it
  before publication — *do not* ship this chapter without review.
- **Resist "nobody knows how it works."** It is the seductive line and the inaccurate one. Use the
  mechanism-versus-meaning distinction instead; it is more precise and more damning.
- **Keep the Lego image; fix the units.** The analogy is good. The fragment sizes are not uniform, and
  they are not four bytes.
- **Do not claim tokens are "information."** A token is an index into a vocabulary. The meaning lives in
  the *relationships* between indices, which is exactly the author's own "similarity" point — so the
  correction strengthens his framing rather than opposing it.

**Where it lands.** Early in **Part II**, immediately after "A function, not a source" — the reader has
just accepted that the model transforms rather than knows, and this chapter explains *what it is
transforming, in what, and why it errs.* Several later chapters (the confident-error argument, the
right-sizing argument, the "ask again is a re-roll" point) draw directly on it.


### ⚑ Reviewer findings — ML review received, six claims, corrections applied

**A competent ML review was obtained on 21–22 October 2026.** It found problems in **four of the six
claims** — and it found them in *the corrections*, which had been made by the assistant. **That is the
flag vindicating itself: a model could not verify its own technical work, and the review proves it.**
The reviewed wording below **supersedes the prose above wherever they differ.**

**1. "Whole-context attention lets a reasoning model write a note and follow it." — OVERCLAIMED.**
Attention lets tokens use information elsewhere in the available context. That alone does not explain
*reliable* self-instruction: that also depends on training, architecture, prompt and how the note is
represented. **Corrected wording:**
> A model can *sometimes* use information it generated earlier in the context — but attention alone does
> not guarantee reliable self-instruction or follow-through. **"Sometimes" is doing real work in that
> sentence.**

**2. "Reasoning traces can be unfaithful." — SUPPORTED, AND NOW SCOPED WITH SOURCES.**
- **Turpin et al. (2023)**, *"Language Models Don't Always Say What They Think"* (arXiv 2305.04388,
  NeurIPS 2023): CoT explanations **systematically misrepresent** the true reason for a prediction; models
  fail to mention biasing features that influenced them; when biased toward a wrong answer they
  **rationalise** it. Accuracy fell by up to **36%** on 13 BIG-Bench Hard tasks. Their own sentence belongs
  in the book: *"CoT explanations can be plausible yet misleading, which risks increasing our trust in LLMs
  without guaranteeing their safety."*
- **Anthropic, *"Measuring Faithfulness in Chain-of-Thought Reasoning"*** (arXiv 2307.13702): models vary
  widely in how strongly they condition on their own CoT — and the finding that matters most here:
  ***"As models become larger and more capable, they produce less faithful reasoning on most tasks we
  study."***
- **Corroborating (2025):** *"Reasoning Models Don't Always Say What They Think"* — reveal rates **often
  below 20%**.
- **Scope it:** this does **not** mean all traces are false or useless. It means a displayed trace is
  **not guaranteed to describe the process behind the answer**, so it is not evidence.

**⚠️ And it corrects the assistant, not just the author.** An earlier draft of this note said *"thinking
models make the confident-error problem worse, not better."* **That is too strong.** Reasoning models
produce *more* faithful traces than non-reasoning models (one study measured ~3.6 points higher for the
Claude series, ~1.7 for DeepSeek). The defensible claim is about **the reader, not the model:**
> A visible chain of thought is a **credibility signal that is not earned**. "More faithful" is not
> "faithful" — reveal rates are often under 20%, and larger models are *less* faithful. So the trace is
> not proof. **Thinking is not knowing.**

**3. "Quantisation is like describing a color with four shades instead of 256." — QUALIFY.**
Quantisation reduces the precision used to represent model values, introducing **rounding or clipping
error**. Methods can limit the quality loss, but **the loss is not uniform** — it depends on the method,
the model and the task, and it can be severe. The analogy may stay; it must **not** imply that quantisation
is harmless or that degradation is evenly spread. The book's actual claim is narrower and safer: *a
quantised model often does the job — which is why defaulting to the largest model is a pricing mistake.*

**4. "Temperature is a variance dial, not a knowledge dial." — USEFUL SHORTHAND, MUST BE MARKED AS ONE.**
Corrected wording, and prefer this in the manuscript:
> **Temperature changes how concentrated or spread out the next-token choices are when sampling. It does
> not give the model new knowledge.**

Mark *"variance dial"* as shorthand if it is used. The effect depends on the sampling method and settings,
and it **does** change which answer you get.

**5. "Seeds make results reproducible." — NEEDS A STRONG CAVEAT.**
A seed controls a source of randomness. It does **not** guarantee identical output across different
hardware, software versions, or nondeterministic operations. **State the conditions:** same model, same
version, same hardware and software, same settings. So *"fix the seed to reproduce"* is true **within an
environment** and false **across** environments — **and the book must say so wherever it leans on a
reproducible benchmark**, including the Alpha chapter.

**6. "Mechanism understood, meaning not" / "interpretability is young." — REPLACED. NOT SIGNED OFF.**
The reviewer would not sign off on it: *"meaning" is ambiguous*, and the sentence risks implying more
consensus than exists. **The fix is better than the original claim, and it is narrower:**

> **Do not claim "nobody knows how it works."** Claim the thing that is actually true and actually load
> bearing: **there is no provenance inside the weights.** You cannot ask a model where a fact came from,
> because **no such record exists** — facts are distributed across parameters with no citation attached,
> and none can be audited back to a source. **That is why knowledge must be confined**, and unlike "nobody
> understands it," it survives an expert reading it.

And on the state of the field: mechanistic interpretability is an **active research field with real results
and real open questions** — **not a mystery, and not solved.** Say exactly that. The old framing
(*"everyone has to admit they don't know how it works"*) is the line a critic dismantles in one sentence,
and it is no longer needed: **the argument for confinement does not rest on mystery. It rests on the
absence of provenance.**

**Net effect of the review.** Two claims confirmed (the token correction — the author has since agreed with
it himself — and the unfaithful-trace claim, now properly scoped and cited). Four corrected. **One pivot
replaced with a stronger one.** The chapter is materially more defensible than it was before the review,
and the assistant's contribution to it is materially smaller.



### ⚑ The answer to no-provenance: put the knowledge outside the weights

*Requested by the author: "this can be done with brand voices and RAG systems (explain how this might
work)." This is the constructive close of the chapter — the no-provenance problem stated above, and the
mechanism that answers it.*

**Restate the problem precisely, because it determines the fix.** Inside the weights, a fact has **no
address**. Not a hidden one — none. There is no record of *where this came from*, no citation to follow,
no way to distinguish a remembered fact from a confabulation, no way to update one fact without
retraining, and no way to restrict the model to one version of the truth. And the weights have also been
shaped by preference optimisation, so what's in there is a blend of training data and RLHF artifacts —
none of it inspectable either.

**You cannot fix that inside the model. So you stop keeping knowledge there.**

**1. RAG — move the *facts* out.**

RAG (retrieval-augmented generation) means the facts live in **your** documents, not in the weights. At
answer time, code retrieves the passages relevant to the question and places them **in the context** — in
front of the model, as text it can read. The model's job changes from *recall* to **reading comprehension
over supplied material.** Four things follow, and they are the whole argument:

| | Knowledge in the weights | Knowledge in RAG |
|---|---|---|
| **Provenance** | none — no address, no citation | **the chunk, the document, the page** |
| **Updating** | retrain | **edit the document** |
| **Confinement** | impossible — it knows everything | **retrieve only from the chosen set** |
| **Failure mode** | invention, undetectable in principle | **misreading — visible and checkable** |

**That last row is the one people miss.** RAG does not make the model *incapable* of error; it changes the
*shape* of the error. A model inventing a fact is unverifiable — you cannot audit an absence. A model
misreading a passage you can hold in your hand is a *finding*, not a mystery. **You have moved the failure
from unprovable to checkable**, and that is worth more than an accuracy improvement.

**And a second effect worth naming:** RAG removes the need for the model to *know* anything. Which means it
also removes the need for its **RLHF-shaped knowledge-behavior** to be involved at all. The sycophancy,
the confident guess, the reluctance to say *I don't know* — those are dispositions about *recall*, and
recall is no longer the job.

**2. Brand voice — move the *perspective* out.**

The model's default disposition is also an artifact. Left alone it arrives generic, agreeable, hedged and
eager to please — because that is what preference data rewarded (see Concept 12). A **brand voice** is a
saved, hand-authored profile — tone, key messages, phrases to avoid, standing instructions — that replaces
that inherited default with **a perspective you wrote and can read.**

Same move as RAG, applied to a different thing: **take what was implicit in the weights and make it
explicit, external and inspectable.**

**3. And then the generalisation, which is the real principle — and it is bigger than this chapter:**

> **Nothing that matters should live only in the weights.**
> **Facts** → RAG. **Perspective** → brand voice. **Rules** → policy files. **Method** → a hand-written
> brief (Concept 10). Every one of these is the same move, and each one converts an inherited,
> uninspectable disposition into a declared, readable artifact.

**What the model is left doing, once all four are outside it:** understanding the request, reading what it
was given, and writing the answer. Which is the only thing it was ever reliable at — and it is exactly the
job description the book gives it: **a communications manager, not a knowledge source.**

**Why this closes the technical chapter properly.** The chapter's problem (*no provenance inside the
weights*) needed a fix that was not "get a better model." It gets a fix that makes the model's knowledge
**irrelevant to the answer.** Which is why Ch. 12 hands directly to the confinement chapters — and why the
reviewer's objection (*define the claim and support it*) is now answered: the claim is *no provenance*,
and the support is the architecture that supplies provenance instead.


---

---

## The rules this chapter carries

**Rule 8 — *"It reasoned about it" is not proof.* (primary).** The world of tokens: fragments, compression, similarity, one-directional writing. The chapter is Rule 8's mechanism made visible — 'it reasoned about it' is not proof, because every token is committed before the next is chosen — with Rule 2 as the consequence: confidence is not evidence.

**Rule 2 — *Confidence is not evidence.* (carried).**

## DRAFT

*(write it here. Target roughly 1,600 words. Same rule as the rest of the book: every*
*load-bearing claim to a source, citations kept, nothing invented, anything unverifiable*
*marked ⚠️ rather than smoothed over.)*
