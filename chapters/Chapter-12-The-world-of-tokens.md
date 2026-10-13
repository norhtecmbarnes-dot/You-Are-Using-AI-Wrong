# Chapter 12 — The World of Tokens

*(Concept 6 — the technical spine. Part II: what the model actually is — fragments, numerical representations, learned patterns — and why that matters. The ML review (21–22 Oct 2026) corrected six claims in this chapter's earlier draft; the author's paste incorporates those corrections. Pairs with Ch. 11 (what the model is for) and sets up Ch. 13–15 (the system around the model).)*

---

You see a sentence.
The model processes a sequence of numbers representing pieces of text.
You see a question about the world.
The model receives an input from which it can generate a continuation.
Those are not the same view of the task.
That difference explains why a tool that writes an elegant paragraph can stumble over counting letters. It explains why a confident answer may contain an invented detail. And it explains why asking the same question again is not necessarily a check.
The useful picture is this:
It does not operate directly in our world. It operates through fragments, numerical representations, and learned patterns.
That picture needs care. We do not need to make the machinery mysterious to explain its limitations. Nor should we replace the machinery with an appealing but inaccurate story.
The technical details matter because they tell us what the tool can—and cannot—establish.

## Tokens Are Not Words

For a text model, a token is a numerical identifier representing a piece of text.
That piece might be a letter, punctuation, part of a word, or a whole word. It may include a space.
A common English rule of thumb is about four characters per token. That is a rough estimate, not a definition. The division varies with the text and the tokenizer the model uses.
A tokenizer is simply the mechanism that turns text into those pieces and assigns their identifiers.
This means the model does not necessarily receive a word as a sequence of individually visible letters.
It might receive the word as one token. Or several fragments. The boundary between those fragments need not match the boundary a reader would choose.
That distinction matters when you ask it to count.
Counting the letters in a word requires access to the letters and a reliable counting procedure. Generating a plausible answer about the word is a different operation.
A model may perform the task correctly. But tokenization helps explain why success with language does not guarantee dependable character-level counting.
The fix is not a more forceful instruction to "think carefully."
If the task requires an exact count, use a procedure that explicitly counts the characters.

## Fluent Language Is Not Exact Calculation

The same practical distinction applies to arithmetic.
A text model can generate the correct answer to a calculation. It may also generate a convincing explanation of how to reach it.
But the act of generating text is not, by itself, an exact arithmetic procedure.
Where a number matters, a calculator or a tested software function supplies a different kind of assurance.
The model can interpret the request and explain the result. The calculation can be performed separately.
This is not a claim that models cannot count or calculate. It is a rule about where to place trust.
Do not infer an exact capability from fluent performance on a neighboring task.
Writing about arithmetic and executing arithmetic are not the same job.

## Pictures of Words Are Another Problem

Text rendered inside a generated image introduces a related but distinct difficulty.
An image generator is not necessarily placing verified characters on a page as a typesetting program would. Depending on its design, it may be generating visual patterns that resemble lettering.
A sign can therefore look convincing at a glance while containing malformed or incorrect text.
⚠️ Image-generation systems differ, and some use mechanisms that improve text rendering. Text-tokenization alone does not explain every rendering failure.
The practical lesson survives that qualification.
If exact wording matters, verify the wording—or add it using a tool that renders the specified characters directly.
An image that resembles a document is not evidence that the document's text is correct.

## Training Is Not Filing

The next distinction is between learning patterns and storing records.
During training, a model's numerical parameters—its weights—are adjusted. Those adjustments enable it to produce patterns learned from the training material.
It is useful to think of this as a kind of compression, provided we do not confuse it with a compressed archive.
A compressed archive contains files that can be recovered.
A trained model does not generally contain an inspectable filing system in which each claim is attached to its original document.
Training can produce memorization, including reproduction of particular passages. But that does not turn the weights into a dependable source register.
The model may produce a fact without producing evidence of where that fact came from.
It may also produce something that resembles a fact without any supporting source at all.
That is the load-bearing distinction:

> The weights are not a provenance ledger.

Provenance means the history of a claim: its source, version, authority, and route into the answer.
A business needs that history when the claim matters.

## A Map, Not a Three-Dimensional Warehouse

Models represent tokens and other information using numerical vectors.
These representations can have hundreds or thousands of dimensions. A three-dimensional map is a useful illustration, but it is not a literal description of the machinery.
In the illustration, related things occupy related positions.
That helps us picture how a system can recognize patterns across different expressions. Similar wording, related subjects, and comparable uses can influence the representations it learns.
But "similarity, not meaning" needs qualification.
Models can represent substantial semantic relationships. It would be misleading to say that they handle only superficial resemblance.
The narrower point is more important:
A learned relationship does not certify a claim's truth.
Two policies can discuss the same subject while imposing different rules. Two companies can have similar names while being different organizations. A convincing continuation can fit the surrounding text without matching reality.
Similarity helps generate an answer. It does not establish authority.

## It Writes Forward

For a standard autoregressive language model, generation proceeds one token at a time.
The model uses the available preceding context to produce scores for possible next tokens. A selection procedure chooses the next token. That token becomes part of the context for the next step.
It does not predict from the last token alone.
Attention across the available context is a central feature of transformer architecture. The relevant input may include your instructions, supplied documents, and the answer already generated.
But during an ordinary forward generation, the model does not reach back and replace a token it has already emitted.
This creates an important distinction between continuing and revising.
A human writer may stop, inspect a sentence, delete it, and begin again.
A model's output can be placed inside a workflow that drafts, checks, and rewrites. It can also issue a later correction. But those are additional operations, not proof that each original token passed a factual check.

> A falsehood can be built by the same generation process as a truth—one token at a time.

The model can use its context to catch some problems. What the basic process lacks is a guarantee that each claim has been verified against evidence before being emitted.

## Confidence Is Not a Separate Verification Stage

An answer can sound confident because confident wording fits the continuation.
"There is no doubt" is text.
"The correct answer is" is text.
A precise-looking date is text.
None of those expressions constitutes a verification procedure.
This is why a polished answer cannot serve as its own evidence. Its certainty belongs to the output, not necessarily to an established relationship with the world.
The remedy is external support: supplied sources, appropriate tools, and checks proportionate to the consequence.
The previous chapter's rule follows directly:
Treat the model as a function transforming supplied information, not as the authority supplying it.

## A Seed Changes the Draw

Generation often includes sampling: selecting a token from a probability distribution rather than always choosing the highest-scoring candidate.
A seed initializes the random-number process used in that selection.
Changing the seed can change the generated answer without changing the model's weights or the supplied evidence.
That makes "ask again" a weak method of verification.
A second answer may differ because the system followed a different generation path. The difference does not tell you which answer is true.
Agreement is not conclusive either. The same unsupported answer can recur.
There is also a technical caution:
⚠️ The same prompt, settings, and seed do not guarantee byte-identical output across all platforms. Reproducibility can depend on the implementation, hardware, and other sources of nondeterminism.
The managerial lesson does not require perfect reproducibility.
A new draw is not a new source.

## Temperature Changes Selection, Not Evidence

Temperature adjusts how strongly token selection favors higher-scoring candidates.
Lower temperature generally concentrates probability on the stronger candidates. Higher temperature generally allows more variation.
That can be useful when choosing between predictable wording and a wider range of creative possibilities.
But temperature does not update a policy, retrieve a missing document, or establish whether a statement is true.
It changes selection, not the evidence available to the system.
Low temperature may produce an unsupported answer consistently.
High temperature may produce more varied language without producing better facts.
"Low for research, higher for poetry" is therefore a useful starting preference—not a guarantee of research accuracy or poetic quality.
The source requirements remain the same at either setting.

## Quantization Makes the Numbers Smaller

Model weights are stored as numbers.
Quantization represents those numbers using fewer bits or a smaller set of possible values. This can reduce the memory needed to hold a model.
Think of recording measurements with less numerical precision.
The broad pattern may remain useful even though some fine distinctions are lost.
Quantization is not primarily about moving similar tokens closer together on a map. It changes the numerical representation used for weights and, in some implementations, other computations.
Its effect depends on the model, the quantization method, and the task.
A quantized model may perform adequately for a particular workflow. Another configuration may lose capability that the workflow needs.
That is a testing question, not an article of faith.
The right-sizing lesson is straightforward: use the smaller configuration when it meets your requirements, and demonstrate that it does.

## We Know a Great Deal—and Still Have Open Questions

"Nobody knows how it works" is not a sound foundation for this book.
We know how tokenization works. We know the architecture's operations. We know how generation and sampling are implemented.
Understanding every learned internal mechanism is a different problem.
Interpretability research investigates those mechanisms and has real results alongside unresolved questions.
⚠️ Specific interpretability findings require their own citations before inclusion; the supplied chapter material does not identify particular studies.
There is no need to turn those open questions into total ignorance.
The stronger argument is more precise:

> The model does not come with a dependable internal record linking each generated claim to its training source.

Asking "Where did you learn that?" does not create such a record. Without external retrieval or another provenance mechanism, the model can generate a plausible attribution just as it generates other text.
That is why knowledge must be confined.
Supply the approved material. Require claims to remain within it. Check important statements against it.
The model's world of tokens can be extraordinarily useful.
But the bridge back to our world needs evidence—not merely a convincing continuation.

## Remember This

> It does not operate directly in our world. It operates through fragments, numerical representations, and learned patterns.
>
> The weights are not a provenance ledger.
>
> The previous chapter's rule follows directly: treat the model as a function transforming supplied information, not as the authority supplying it.

---

## The rules this chapter carries

**Rule 2 — *Confidence is not evidence.* (primary).** "Confidence Is Not a Separate
Verification Stage" is Rule 2: confident wording fits the continuation; "there is no
doubt" is text; a polished answer cannot serve as its own evidence.

**Rule 8 — *'It reasoned about it' is not proof.* (carried).** "It Writes Forward":
a falsehood can be built by the same generation process as a truth—one token at a
time—with no guarantee that each claim was verified against evidence before being
emitted.

**Rule 7 — *Asking again is a re-roll, not a re-check.* (carried).** "A Seed Changes
the Draw": changing the seed changes the answer without changing the weights or the
evidence; a new draw is not a new source.

**Rule 13 — *Right-size the model to the task.* (carried).** "Quantization Makes the
Numbers Smaller": use the smaller configuration when it meets your requirements, and
demonstrate that it does.

---

*Verification: the author's prose is adopted verbatim (2,487 words). The paste's
"Source note" ([1] CONCEPTS.md, Concept 6) is the manuscript's internal source, not
an independent technical citation — the author flagged it himself ("External references
for tokenization, transformers, sampling, quantization, and interpretability should be
added before publication"). That flag is preserved here as a ⚠️: the chapter's mechanism claims
(tokenization, autoregressive generation, attention, sampling, seed, temperature,
quantization, the absence of a provenance record in the weights) are standard,
well-established descriptions of how these systems work, and the chapter states them
with appropriate care (hedged qualifiers throughout: "a rough estimate, not a
definition," "the broad pattern may remain useful even though some fine distinctions
are lost," "it would be misleading to say that they handle only superficial
resemblance"). No specific external study is asserted. The chapter does NOT claim
"nobody knows how it works" — it explicitly rejects that framing ("'Nobody knows how it
works' is not a sound foundation for this book"), and instead makes the reviewer-endorsed
claim: there is no provenance inside the weights.

The ML review (21–22 October 2026, recorded in the skeleton's reviewer-findings
section) corrected six claims; the author's paste incorporates those corrections:
temperature reframed as selection-not-evidence (finding 4), seed with the
environment caveat (finding 5), quantization with non-uniform loss (finding 3), and
the no-"nobody-knows" pivot to no-provenance (finding 6). The paste does NOT add
CoT/thinking-model claims — it covers the mechanism (autoregression, attention,
one-directional generation) without asserting faithfulness claims about reasoning
traces, so the Turpin et al. (2023), Anthropic (2307.13702), and "Reasoning Models
Don't Always Say What They Think" (2025) sources the reviewer cited are NOT needed here.
Those three sources were verified this session for the register: Turpin et al.,
"Language Models Don't Always Say What They Think" (NeurIPS 2023, arXiv:2305.04388,
peer-reviewed — CoT explanations can be "plausible yet misleading"); Anthropic,
"Measuring Faithfulness in Chain-of-Thought Reasoning" (arXiv:2307.13702, working
paper — "as models become larger and more capable, they produce less faithful
reasoning on most tasks we study"); Chen et al., "Reasoning Models Don't Always Say
What They Think" (arXiv:2505.05410, working paper — reveal rates often below 20%).
They remain available for the register if the chapter is later expanded to cover
thinking models.

The chapter's two ⚠️ flags (image-rendering and interpretability) are the author's own,
kept verbatim. The "four characters per token" rule of thumb is stated as a rough
estimate, not a definition — the honest register. Placement: Chapter 12, Part II
(the technical spine), between Ch. 11 (A function, not a source) and Ch. 13
(Language at the edges, code in the middle). Carries Rule 2 (primary), Rules 8, 7,
13.*
