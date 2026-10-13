# Chapter 11 — A Function, Not a Source

*(Part II — The Model That Works. The transformation-of-input framing: the model is a function, not a source. The same-request-twice demo (asking it to remember vs. handing it the material) is the chapter's spine. Pairs with Ch. 12 (the world of tokens — what the model actually is) and sets up Ch. 13–15 (the system around the model).)*

---

Most of us begin using AI as though we have hired someone who knows a great deal.
We ask a question. It answers. We ask for more detail. It supplies that too.
The experience encourages a familiar assumption: somewhere behind the conversation is knowledge we can draw on.
That assumption is understandable. The interface invites it. A tool that responds fluently to almost any question looks like a source.
But for work that must be dependable, there is a better starting point:

> Treat the model as a way to transform information you supply, not as the authority that supplies the information.

Give it material to summarize. Give it evidence to organize. Give it a policy to explain. Give it an approved brief to turn into a draft.
The distinction changes the assignment.
Instead of asking, "What do you know about this?" you ask, "What can you do with this?"
That is the difference between a source and a function.

## The Same Request, Two Different Jobs

Consider a manager preparing a customer update.
The first request reads:

> "Write an update explaining our current service commitments and escalation process."

The model may produce a polished message. It may describe response times, support arrangements, and escalation stages that sound entirely reasonable.
But where did those details come from?
Unless the relevant material is supplied or retrieved, the model has no dependable basis for establishing this organization's current commitments.
It may produce something typical rather than something true.
Now change the request:

> "Using the attached approved service agreement and escalation procedure, draft a customer update. Preserve the stated commitments. Do not add response times or promises that are not in these documents. Identify anything the documents do not resolve."

The writing task is similar. The factual task is different.
In the first request, the model must supply the substance as well as the wording.
In the second, the substance has an identified source. The model's job is to communicate it.
This is an illustrative comparison, not a performance test. The second request does not guarantee a correct answer. The model can still misread a condition, omit an exception, or introduce an unsupported detail.
But the result can now be checked against something definite.
You can ask whether it accurately transformed the approved material.
That is a much stronger basis for acceptance than asking whether the answer sounds knowledgeable.

## What "A Function" Means

You do not need to be a programmer to understand this framing.
A function takes something in and produces something out.
For a writing task, the input might be interview notes, a policy, a customer message, or an approved set of facts. The output might be a summary, an explanation, a comparison, or a draft.
The model is useful because the transformation is not always mechanical.
It can turn technical wording into plain language. It can organize scattered notes. It can adapt a message for a different audience.
But its usefulness does not require you to treat it as the factual authority.
Imagine giving an editor a report and asking for a shorter version.
You expect the editor to improve the expression while preserving the substance. You do not expect them to invent a stronger financial result because it makes the paragraph read better.
The same distinction belongs in AI work.
The model may have discretion over wording and organization. It should not quietly acquire discretion over what is true.

## "It Doesn't Know Things" Is an Operating Rule

Rule 1 says:

> It doesn't know things.

Taken literally as a description of every model capability, that phrase would be too broad. Models can produce correct information across many subjects.
As an operating rule, however, its purpose is clear:
Do not treat a model's answer as established organizational knowledge simply because it can produce one.
A correct-looking response does not tell you where the claim came from, whether it is current, or whether it applies to your situation.
For a manager, those questions matter more than the model's ability to answer a general knowledge quiz.
Your approved price, current policy, customer commitment, and project requirement need identifiable authority.
The model's training is not that authority.
The rule therefore asks you to change the source of the work, not deny the tool's capabilities.
Use its language abilities. Supply the facts.

## You Also Inherit How It Was Trained

When you rely on the model to supply an answer, you rely on more than the information represented in its training.
You also encounter behavior shaped by training: what kinds of responses were rewarded, discouraged, or preferred.
One documented concern is sycophancy—the tendency to agree with a user rather than challenge an incorrect premise.
Research by Sharma and colleagues found that people and preference models sometimes preferred convincingly written, agreeable responses over correct ones.[^1]
The concern here is not simply political bias. It is agreement.
A manager asks, "This proposal clearly meets all the requirements, doesn't it?"
A dependable review should examine the requirements and evidence. It should not become more favorable because the question signals the answer the manager wants.
Supplying the requirements does not eliminate this risk. The brief must also direct the model to assess them rather than endorse the user's position.
The framing matters:
"Confirm that we comply" is not the same assignment as "Compare each requirement with the supplied evidence and report unsupported claims."
One seeks reassurance. The other commissions work that can be inspected.

## Confidence and Refusal Are Behaviors, Not Evidence

Other research in the supplied material examines how training changes refusal and hallucination.
One study reported that a fine-tuning approach substantially reduced refusals while increasing confident, incorrect responses to questions that could not be answered. Another found that reinforcement learning could increase hallucination under the conditions studied, including convergence on a confidently held wrong answer.[^2][^3]
These findings should not be stretched into a claim about every model or every training method.
Their managerial lesson is narrower and more useful:
A confident answer is not evidence that the question was answerable.
A refusal is not a complete explanation of the system's limits.
And a model that answers more often is not necessarily doing better work.
The assignment needs a legitimate stopping point.
If the supplied material does not establish the answer, "The documents do not answer this question" should count as successful performance.
Otherwise, you are rewarding completion even when completion requires invention.

## Make the Missing Information Visible

Suppose the approved service agreement states ordinary support hours but says nothing about holiday coverage.
A customer asks about a public holiday.
The model should not fill the gap with what similar organizations usually do.
It should identify the gap.
That may feel less impressive than an immediate answer. It is more useful.
The organization can then obtain the missing information from someone authorized to provide it.
This is where transformation becomes a dependable assignment. The model can explain what the source establishes and distinguish it from what the source does not establish.
Research described in the supplied evidence also explores rewarding abstention and penalizing confident hallucination.[^4] Its reported results apply to the study's evaluation conditions, not automatically to your workflow.
The design lesson is to make declining an unsupported answer an acceptable outcome.
Do not force the tool to finish a job for which you have not supplied the necessary material.

## Put Important Things Where You Can Read Them

Facts are not the only inputs that need an explicit home.
Four different elements shape useful work:

- **Facts:** the information supporting the claims.
- **Perspective:** the voice and position from which the organization communicates.
- **Rules:** what the tool may and may not do.
- **Method:** the approved way to carry out the assignment.

These elements should not live only as an expectation that the model will somehow understand your organization.
Give them readable form.
Approved documents can supply facts. A brand voice can define tone and preferred language. Policies can define permissions and limits. An expert's brief can establish the method.
Keeping them separate also prevents one from substituting for another.
A confident voice does not establish a fact.
A persuasive message does not authorize a promise.
A detailed procedure does not supply missing evidence.
The model can help express these elements. It should not silently invent the governing substance.

## Attach the Facts Where the Work Begins

The practical fix is simple to state:

> Attach the facts so the model never needs to remember them.

For an individual user, this may mean supplying the approved document with the request.
For an application, it may mean retrieving the relevant material before the model is asked to answer.
Builders call that retrieval-augmented generation, or RAG. In plain language, the system finds the material and puts it in front of the model at the moment of work.
The important point is not the acronym.
It is the timing.
The facts should accompany the assignment that needs them. Do not rely on an earlier conversation or assume the model has retained the right version.
If a policy has changed, the current policy must be supplied.
If the project has changed, the current project's material must be supplied.
If the available evidence is incomplete, that incompleteness must remain visible.

## Confinement Gives the Assignment a Boundary

Rule 12 says:

> Confinement is the design, not a limitation.

For this chapter, confinement means defining the material from which the model may make factual claims.
"Use these documents" gives the work a boundary.
It does not mean the model loses its ability to write, organize, or explain. Those are the capabilities you are asking it to use.
It means those capabilities serve a defined body of evidence.
There is an important qualification: supplying documents and requesting confinement does not itself guarantee that every sentence will remain supported. The answer still needs appropriate checking.
The benefit is that the standard becomes clear.
A specific claim should be traceable to the supplied material. If it cannot be traced, it needs removal, qualification, or further evidence.

## The Question to Ask Before Every Request

Before commissioning an AI answer, pause over one question:
Am I asking it to transform information, or am I asking it to supply information I have not established?
Sometimes discovery is exactly what you want. Brainstorming, exploration, and tentative suggestions can be useful.
But those outputs should remain candidates for investigation—not quietly become approved facts.
For dependable organizational work, supply the material and define the transformation.
Ask it to summarize the policy, not invent the policy.
Ask it to compare the proposal with the requirements, not reassure you that it is good.
Ask it to explain the evidence, not manufacture a case.
This framing will not eliminate every error. It gives errors somewhere to be found.
The source can be inspected. The interpretation can be checked. The missing information can be named.
That is how a fluent answer becomes accountable work.

## Remember This

> Supply the facts. Define the transformation. Accept an honest gap. Check the result against the source.
>
> The model does not need to be your source to be valuable.
>
> It needs a clear job—and the material to do it.

---

[^1]: Sharma, M., et al. "Towards Understanding Sycophancy in Language Models."
  ICLR 2024 (arXiv:2310.13548, Anthropic). **Peer-reviewed.** Finding: both human
  evaluators and preference models preferred convincingly written, agreeable
  (sycophantic) responses over correct ones a non-negligible fraction of the time.
  ⚠️ Working-paper-adjacent percentages in the broader literature are fastest-spoiling;
  the chapter asserts the finding, not a figure.

[^2]: "The Hallucination Tax of Reinforcement Finetuning" (arXiv:2505.13988).
  Working paper (arXiv preprint); **not peer-reviewed.** Finding: standard RFT
  substantially reduced model refusal rates on unanswerable questions while
  increasing confident, incorrect (hallucinated) responses. The chapter's "substantially
  reduced refusals while increasing confident, incorrect responses" is the honest,
  hedged register.

[^3]: "Reasoning Models Hallucinate More: Factuality-Aware Reinforcement Learning
  for Large Reasoning Models" (arXiv:2505.24630). Working paper (arXiv preprint);
  **not peer-reviewed.** Finding: reasoning-oriented RL fine-tuning increased
  hallucination prevalence; the paper's mechanism includes spurious local optima —
  "the model can converge to a confidently held wrong answer." The chapter's "under
  the conditions studied, including convergence on a confidently held wrong answer"
  is source-accurate.

[^4]: "Harnessing RLHF for Robust Unanswerability Recognition and Trustworthy
  Response Generation in LLMs" (SALU, arXiv:2507.16951). Working paper (arXiv
  preprint); **not peer-reviewed.** Finding: a confidence-score-guided RLHF phase
  that explicitly penalizes hallucinated responses and rewards appropriate abstentions
  reduced hallucination on unanswerable questions in the study's evaluation. The
  chapter's "research... explores rewarding abstention and penalizing confident
  hallucination" and "its reported results apply to the study's evaluation conditions,
  not automatically to your workflow" is the honest register. ⚠️ The paper's headline
  figures (e.g., hallucination rate reduced to ~1.3%) are on a custom Chinese-LLM
  conversational-IR dataset; not asserted in the chapter.

## The rules this chapter carries

**Rule 1 — *It doesn't know things.* (primary).** "'It Doesn't Know Things' Is an
Operating Rule" is Rule 1 reframed: as an operating rule, do not treat a model's
answer as established organizational knowledge. "Use its language abilities. Supply
the facts."

**Rule 12 — *Confinement is the design, not a limitation.* (carried).** "Confinement
Gives the Assignment a Boundary": confinement means defining the material from which
the model may make factual claims.

**Rule 2 — *Confidence is not evidence.* (carried).** "Confidence and Refusal Are
Behaviors, Not Evidence": a confident answer is not evidence that the question was
answerable.

**Rule 5 — *It cannot tell you it's unsure.* (carried).** The same section: a refusal
is not a complete explanation of the system's limits; the assignment needs a
legitimate stopping point.

---

*Verification: the author's prose is adopted verbatim (1,852 words). The paste's
"Research references" block ([1]-[4]) is converted into full footnotes with peer-review
status, per the established pattern; all four verified this session: [1] Sharma et al.,
ICLR 2024 (arXiv:2310.13548, peer-reviewed); [2] arXiv:2505.13988 (working paper);
[3] arXiv:2505.24630 (working paper); [4] SALU, arXiv:2507.16951 (working paper —
verified: "Harnessing RLHF for Robust Unanswerability Recognition and Trustworthy
Response Generation in LLMs," confidence-score-guided RLHF that penalizes hallucinated
responses and rewards appropriate abstentions). The chapter's research claims are all
framed honestly by the author: "sometimes preferred" (not "always"), "under the
conditions studied" (not universally), "its reported results apply to the study's
evaluation conditions, not automatically to your workflow" (SALU). The "Same Request,
Two Different Jobs" demo is framed by the author as "an illustrative comparison, not a
performance test" — the honest register, kept. The editor metaphor, the four elements
(facts/perspective/rules/method), and the RAG explanation are argument and standard
practice, not external facts. Placement: Chapter 11, Part II — between Ch. 10 (It
will not set you free) and Ch. 12 (The world of tokens). Carries Rule 1 (primary),
Rules 12, 2, 5.*
