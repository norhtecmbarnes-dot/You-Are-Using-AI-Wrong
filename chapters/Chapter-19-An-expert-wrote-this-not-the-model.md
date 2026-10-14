# Chapter 19 — An Expert Wrote This, Not the Model

*(Concept 10 — the prompt is a knowledge artifact, not a model output. Rule 1 applied to method: facts need an approved source; methods need an accountable author. Pairs with Ch. 20 (The expert is the product), which is the commercial turn. The two-agent demo is illustrative, framed as such by the author.)*

---

The book's first rule has one more job to do.
We have applied it to facts. Do not ask the model to remember your policy, your price, or your customer's requirements. Supply the approved material, then ask it to work with that material.
Now apply the same rule to method.
Do not ask the model to invent how your organization performs the work, then give that invention to an agent as its operating instructions.
Supply the method too.
The model is not your authority for facts. It should not become your authority for procedure either.
This does not reduce the model to copying. Understanding a request, interpreting documents, drafting a response, and adapting an explanation are substantial tasks.
But deciding the governing method is a different responsibility.
That belongs to someone who knows the work.

## The First Rule, One Level Up

The author states the principle in the project's captured material:

> this is a theory but it is a rule. Agentic AI has great potential but the fault with agentic ai is thatmost people rely on the LLM to prompt the agent itself. A truely great agent should replect theknowledge of a true expert with experience, not a gneric self-generated prompt.

The spelling is incidental. The distinction is not.
An agent needs instructions. Those instructions can look impressive without containing the knowledge that makes the job dependable.
"Act as an experienced proposal manager" is a role description.
It is not the proposal manager's method.
"Be thorough, accurate, and persuasive" expresses an aspiration.
It does not establish what evidence is acceptable, which checks come first, or when the agent must stop.
The missing ingredient is not a more elaborate personality.
It is an authored procedure.

## A Plausible Process Is Not an Authorized Process

Ask a model to write instructions for a professional task and it may produce a useful starting draft.
It may identify sensible stages. It may organize familiar advice clearly.
But plausibility does not establish that the process matches your organization's obligations, evidence standards, or experience.
The question is not whether the generated instructions sound professional.
The question is whether a qualified person has established that these are the instructions the work should follow.
This is the procedural version of the problem with an unsupported fact.
A confident sentence does not establish its own truth.
A confident checklist does not establish its own fitness for the job.
If the agent follows an inadequate checklist consistently, consistency does not rescue the method. It reproduces the omission.
⚠️ The supplied evidence does not establish that all model-generated procedures are inferior to all human-authored procedures. The rule here concerns authority and validation, not an automatic ranking of every possible draft.
The governing method must earn approval outside the model that will execute it.

## Two Agents, One Difference

Consider two agents reviewing the same proposal against the same customer requirements.
They use the same model and receive the same documents.
The first receives instructions generated from a broad request:
"Create a professional process for reviewing a proposal."
Its brief tells it to assess completeness, clarity, persuasiveness, and alignment with the customer's needs.
The second receives a method written by an experienced practitioner:
"Identify each mandatory requirement before reviewing persuasive language. Compare each compliance claim with the supplied evidence. Distinguish an explicit commitment from a general capability statement. Where evidence is absent, identify the gap rather than infer compliance. Do not rewrite an unsupported claim to make it sound stronger."
These are illustrative briefs, not quoted Dashboard instructions or results from a measured experiment.
They show what the comparison should examine.
The first brief defines broad qualities. The second establishes distinctions, an order, and a refusal.
It tells the agent what must happen before polishing begins.
If the agents produce different reviews, the model alone cannot explain the difference. The governing instructions are a changed input.
⚠️ A controlled test would be needed to establish the size and reliability of any performance difference. No such result is supplied here.
Nevertheless, the design question is already visible:
Does the brief contain the knowledge that determines whether the work is acceptable?

## The Plan and the Execution

Two responsibilities must remain distinct.
The plan establishes the method: the sequence, the checks, the evidence standards, and the conditions for stopping.
The execution applies that method to the current request: reading, comparing, summarizing, drafting, formatting, and using permitted tools.
The model can do substantial work in execution.
It may decide how best to explain a finding. It may organize a long document into a useful structure. It may draft several versions of an approved message.
But those choices occur inside the governing method.
The rule is not that a model must never produce a plan-shaped piece of text.
It can draft a proposed procedure for expert review. It can summarize an existing procedure. It can adapt an approved checklist to a particular case.
The boundary is adoption.
A model-generated suggestion must not silently become the authority under which the agent operates.
Someone qualified must own that decision.

## What Experts Put Into a Brief

An expert's value is not confined to knowing the obvious steps.
The useful knowledge often concerns exceptions and distinctions:
What looks complete but is not?
Which source takes precedence?
What should never be inferred?
Which omission requires a question?
When is a polished answer worse than no answer?
These are the details a generic instruction can miss.
A proposal reviewer, for example, may distinguish between describing a capability and proving compliance with a requirement. A customer-service manager may distinguish between explaining policy and authorizing an exception.
The distinction determines what the agent may do.
Without it, the agent may produce fluent work that crosses a boundary the organization considers essential.
The expert does not need to produce literary instructions.
A rough but explicit rule—"If this evidence is missing, stop and ask"—can carry more operational value than a beautifully written paragraph about excellence.
That is a design judgment, not a claim that every rough human plan outperforms every polished generated one.
The point is to capture real knowledge rather than mistake polish for it.

## The Dashboard's Authorship Is Visible

The Dashboard provides a concrete example of this approach.
According to the supplied project evidence, its governing instructions are human-authored rather than generated by the model.[^1]
Its soul.md expresses a senior capture manager's voice, rules, and refusals. One instruction reads:

> "You ASK WHEN YOU DON'T KNOW… Guessing when you could ask is a failure."

This is more than a tone preference.
It establishes how the agent should handle uncertainty.
Other authored files carry distinct responsibilities:
knowledge-policy.ts defines the knowledge policy.
strengths-policy.ts carries the strengths-only rule.
local-first.ts defines the gate governing local-first behavior.
The significance is not the filenames.
It is that important decisions exist as readable artifacts with human authorship.
⚠️ This chapter relies on the supplied verification record; it does not independently inspect the repository. The record also does not establish how these instructions would compare experimentally with model-generated alternatives.
What it does establish is the design choice: the model executes governing instructions it did not originate.

## Refusals Belong in the Method

A useful brief says more than what to do.
It says what not to do—and what to do instead.
Do not infer a commitment from marketing language.
Do not treat an unsupported claim as established.
Do not conceal missing evidence by improving the prose.
Ask, identify the gap, or escalate.
These are illustrative rules. The applicable refusals must come from the people responsible for the actual workflow.
That matters because an agent's assignment can otherwise become "complete the task at all costs."
Completion is not always success.
Sometimes success is recognizing that a required input is absent and returning the work for clarification.
The Dashboard's instruction about asking instead of guessing makes that boundary explicit.
The expert's method should give the agent a legitimate stopping point.

## A Skill File Carries the Method

A skill file is one mechanism for delivering that knowledge.
It can contain a procedure, a checklist, examples, pitfalls, and conditions for refusal.
The important property is not its name or file format.
It is the relationship between the artifact and the agent:
The artifact carries the approved method. The agent applies it.
The supplied concept notes identify skills in several commercial tools as examples of this mechanism.
⚠️ Product-specific implementations are not independently documented in the supplied chapter evidence, so they should not be treated here as proof of effectiveness.
Nor is a file trustworthy merely because it is called a skill.
A skill file can contain generic advice, stale instructions, or an unreviewed model draft.
The same authorship questions apply:
Who wrote it?
Who approved it?
What experience informs it?
What happens when the method changes?
The artifact is a container. Expertise is the content.

## Extract the Method Before Automating It

If the expert has never written the procedure down, begin there.
Ask them to walk through an actual case.
Capture the order of decisions, not just the final result. Record what they checked, what they rejected, and what made them stop.
Then distinguish three things:
What must always happen.
What depends on the case.
What requires a person's authorization.
The model can help organize those notes. It can turn a recorded explanation into a draft checklist or reveal ambiguities for discussion.
That is transformation of supplied input—the framing from Chapter 11.
The expert must still review the result.
A clean summary can omit a crucial qualification. A tidy sequence can impose an order the expert never intended.
Do not let the convenience of transcription become a transfer of authority.

## Respect the People Who Learned This Already

This is not an argument against prompt engineering.
Practitioners who write effective instructions are often doing exactly this work: making assumptions explicit, defining boundaries, specifying evidence, and testing failure cases.
The principle explains why that work matters.
The prompt is not merely a clever sentence that makes the model behave.
It is a knowledge artifact.
For governing instructions, its quality depends on the method it carries and the accountability behind that method.
The expert's process need not be perfect. It needs to be explicit, reviewable, and open to correction.
An authored method gives a team something definite to improve when a failure occurs.
They can ask whether the instruction was wrong, incomplete, or badly executed.

## Who Wrote the Instructions?

Rule 20 completes Rule 1:

> The prompt is a knowledge artifact.

Facts need an approved source.
Methods need an accountable author.
The model can help draft both. It should not become the authority for either merely because its output reads well.
Before expanding the agent, improving its persona, or giving it more tools, inspect the brief.
Does it contain the real checks?
Does it preserve the necessary order?
Does it name the refusals?
And ask the question that matters most:
> Who wrote your agent's instructions—and have they ever done the job?

If the answer is "the model," you have a draft.
You do not yet have an expert's method.

## Remember This

> Facts need an approved source.
>
> Methods need an accountable author.
>
> Who wrote your agent's instructions—and have they ever done the job?

---

## The rules this chapter carries

**Rule 1 — *It doesn't know things.* (primary).** "The First Rule, One Level Up"
is Rule 1 applied to method, not just facts: the model is not your authority for
facts, and it should not become your authority for procedure either.

**Rule 20 — *The prompt is a knowledge artifact, not a model output.* (carried).**
"Respect the People Who Learned This Already" and "Who Wrote the Instructions?" are
Rule 20: the prompt is a knowledge artifact, and facts need an approved source
while methods need an accountable author.

**Rule 12 — *Confinement is the design, not a limitation.* (carried).** "A Skill
File Carries the Method": the artifact carries the approved method; the agent
applies it.

---

*Verification: the author's prose is adopted verbatim (2,057 words). The paste's
"Source notes" block ([1]-[3]) is converted into this verification note; all three
verified this session against the PersonalAI-Dashboard repo:
- **[2] soul.md quote** — confirmed verbatim at `soul.md` lines 32-34: "You ASK WHEN
  YOU DON'T KNOW... Guessing when you could ask is a failure." (The chapter's
  ellipsis form matches the source.)
- **[1][3] Policy files** — confirmed to exist: `src/lib/config/knowledge-policy.ts`,
  `src/lib/config/strengths-policy.ts`, `src/lib/config/local-first.ts`. The chapter's
  descriptions of their responsibilities (knowledge policy, strengths-only rule,
  local-first gate) match the register's record of them.
- **The quoted "theory" line** (the author's captured material, with its original
  spelling — "thatmost," "truely," "replect," "gneric") is the author's own statement
  from captured project material, presented as his. It is NOT found in the Dashboard
  repo's current files — it is testimony/quoted captured material, and the chapter
  itself says "The spelling is incidental. The distinction is not." The quote is
  preserved verbatim because that is the author's point. If the author wants the
  spelling corrected, that is a one-word edit per instance.
- **The two-agent demo** is framed by the author as illustrative ("These are
  illustrative briefs, not quoted Dashboard instructions or results from a measured
  experiment") — the honest register, kept. The ⚠️ note that a controlled test
  would be needed is the author's own, kept.
- **The author's book-writing-tools experience** (Ch. 14 carried it) is referenced
  here via "the author states the principle" — testimony, presented as such.
- The chapter's three ⚠️ flags (model-generated procedures not proven inferior;
  the chapter relies on the supplied verification record, not independent repo
  inspection; product-specific skill implementations not independently documented)
  are the author's own, kept verbatim.
- The chapter references Ch. 11 ("the framing from Chapter 11") — verified correct:
  Ch. 11 is "A function, not a source," drafted (commit 196fa9b).

Placement: Chapter 19, Part III — between Ch. 18 (They cooperate) and Ch. 20 (The
expert is the product, drafted). The pair reads: the method must be authored by an
expert (Ch. 19), and the expert's knowledge is the product (Ch. 20). Carries Rule 1
(primary), Rules 20, 12.*
