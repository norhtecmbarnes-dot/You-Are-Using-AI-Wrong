# Chapter 20 — The Expert Is the Product

*(Concept 11 — a prompt-built agent knows nothing the model did not already
know at training time, so it is a commodity; the scarce input is expertise, and
the business of the next few years is agents built by experts. Placed in Part III,
after Ch. 19 ("An expert wrote this, not the model"), which establishes that the
model is not a source of method — this chapter is the commercial turn: the expert's
knowledge is the product. Framed throughout as a prediction, not a certainty.)*

---

I believe one important future business will be agents built by experts.

Today, many agents are built from simple prompts. Those prompts may be polished. They may sound thoughtful. They may include goals, roles, steps, and formatting rules.

But they often give the agent no knowledge beyond what the language model had at the point of training.

That is a weak foundation for a business.

This is a prediction, not a certainty. Markets can reward distribution, timing, execution, relationships, or luck. But the underlying logic is straightforward.

## The Model Is Becoming a Commodity

Many organizations can rent access to the same underlying models.

The models improve. Prices change. New providers appear. A capability that seemed remarkable last year becomes ordinary the next.

That does not make models unimportant.

It means the model itself is difficult to defend as the source of lasting advantage.

If your product is a general-purpose model with a simple prompt wrapped around it, someone else can often reproduce much of it quickly. They may use the same model. They may use a better model next month. They may offer it at a lower price.

The prompt does not solve this problem if it adds no knowledge.

A prompt can organize the model's behavior. It can define a role. It can specify a format. It can ask for careful reasoning or a particular tone.

But it cannot create experience that neither the prompt writer nor the model possesses.

A prompt-built agent is therefore often close to a commodity as well.

## The Scarce Input Is Knowledge

What makes an agent different is not its ability to generate text.

It is what the agent knows that the model does not.

That knowledge may include:

- how a specific job is actually performed;
- which information is authoritative;
- the order in which decisions should be made;
- the exceptions that matter;
- the errors that create real cost;
- regulatory, contractual, or operational constraints;
- the organization's own definitions and standards;
- and the judgment developed through repeated experience.

None of this appears automatically when a model is connected to a chat interface.

It must come from outside the model.

It must be supplied through expert-authored instructions, approved documents, carefully designed tools, selected data, tests, and operational feedback.

That is why the previous chapter matters commercially.

If the method must come from a person who understands the work, then the expert's knowledge is not a supporting detail. It is the part of the product that cannot simply be rented from a model provider.

> AI does not eliminate the expert. It makes the expert's knowledge the product.

## A Generic Agent Is Easy to Copy

A horizontal agent may be useful. It can help many people write, summarize, plan, search, and organize.

But broad usefulness is not the same as defensibility.

A generic agent has little industry nuance. It may lack the vocabulary, workflows, edge cases, benchmarks, permissions, and real-world procedures that distinguish competent work from merely plausible work.

A specialized agent can be different.

Not because it has a clever name or a more elaborate prompt.

Because it embodies real knowledge about a specific kind of work.

For example, a useful agent for a regulated process might include expert-defined decision paths, approved policy sources, documented exceptions, mandatory review points, and tests built from real mistakes. A useful agent for a technical workflow might know the organization's systems, formats, definitions, and escalation routes.

The model remains important.

But the product value comes from the knowledge architecture around it.

## This Does Not Make Deployment Easy

Expertise is a differentiator. It is not a shortcut.

Many agent products will fail to reach useful production scale. Some will be difficult to integrate. Some will struggle with adoption. Some will not justify their cost. Some will solve a problem that customers do not consider important enough to change how they work.

The hardest work may not be model selection at all.

It may be integration, workflow design, permissions, training, governance, change management, and earning the trust of the people who must use the system.

There is also a serious competing view: that distribution is the real moat.

A company with trusted channels, existing customers, strong partnerships, and effective sales and support may outperform a technically superior agent with no route to market. In many cases, that is true.

Distribution matters.

But distribution can be purchased, built, or lost. Better models can be rented. Features can be copied.

The knowledge of how work is actually done is harder to acquire.

It lives in the experience of people who have performed the work, made the mistakes, learned the exceptions, and understood what good looks like when the situation is not clean.

## Build Around the Knowledge the Model Lacks

This changes the question for anyone building with AI.

Do not begin by asking:

> Which model should we use?

Begin by asking:

> What knowledge does this work require that the model does not already have?

Then ask:

- Who possesses that knowledge?
- Can they explain the method?
- Can the method be written down, tested, and improved?
- What approved sources must the system use?
- Which decisions require human judgment?
- What would distinguish a useful result from a plausible one?
- What would a competitor need to learn before they could reproduce this system?

The answers are the product.

The model is the engine.

The expert knowledge is the map.

## The Test

Every AI product should be able to answer one question clearly:

> What does this agent know that the model does not?

If the answer is "nothing," you may have built a demonstration.

If the answer is specific, testable, and grounded in real work, you may be building something more durable.

## Remember This

> Models can be rented.
>
> Prompts can be copied.
>
> Expertise must be earned.
>
> That is where the value lands.

---

## The rules this chapter carries

**Rule 21 — *It is the expert's knowledge, not the model's, that made the work good.* (primary).**
The whole chapter is Rule 21: the model is the engine, the expert knowledge is the map;
the test is *"What does this agent know that the model does not?"*

**Rule 20 — *The prompt is a knowledge artifact.* (carried).** "A prompt can organize the model's
behavior... But it cannot create experience that neither the prompt writer nor the model
possesses" — a prompt-built agent adds no knowledge, which is the chapter's opening claim.

---

*Verification: the author's prose is adopted verbatim (1,489 words). The paste titled it
"Chapter 21 — The Expert Is the Product"; the content is Concept 11, which the outline
places at Ch. 20 (the paste's "21" is stale — it predates the Ch. 16 merge). Placed at
Ch. 20, after Ch. 19 ("An expert wrote this, not the model"), which this chapter's
"That is why the previous chapter matters commercially" line refers to.

No external factual claims requiring a source: the chapter's central claim — "I believe
one important future business will be agents built by experts" — is framed by the author
as a prediction, not a certainty ("This is a prediction, not a certainty. Markets can
reward distribution, timing, execution, relationships, or luck"). The register's handling
rule for Concept 11 is "Prediction — must be framed as one," and the chapter frames it
as one, in the author's own words, twice. The commodity argument (models rentable,
prompts copyable), the scarce-input argument, the distribution counterweight, and the
"Build Around the Knowledge" question list are argument and business logic, not external
facts.

⚠️ Note for the register: the outline's demo for this chapter cites market evidence —
vertical agent startups raised an estimated $12–18B from 2023 to early 2026, with the
moat named as "pre-built playbooks that general models can't replicate." The author's
chapter does NOT cite the $12–18B figure or any market statistic; it argues the
prediction from logic. The figure remains in the outline/register, flagged for
re-checking before print (it is the freshest and least-stable kind of number). The
chapter is stronger for not leaning on it — the prediction stands on its own framing.

The chapter also carries both counterweights the register requires: "Many agent products
will fail to reach useful production scale" (deployment difficulty) and "There is also a
serious competing view: that distribution is the real moat... In many cases, that is
true" (the distribution counterweight, stated honestly and conceded).*
