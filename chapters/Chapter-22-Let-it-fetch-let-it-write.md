# Chapter 22 — Let It Fetch, Let It Write

*(Part III — What Right Looks Like. The working-pipeline chapter: code fetches, a cheap model ranks, the best model writes, code validates and queues, a human approves. The five-stage research loop — a real, verified run in the author's own system — is the chapter's spine. Pairs with Ch. 21 (measure, don't ask) and Ch. 23 (let it build code, because code is checkable).)*

---

The wrong instruction is deceptively simple:

> Research this and write me something useful.

It gives the model an objective without defining where the facts must come from. The output may be fluent. It may be well organized. But unless the sources and checks are part of the system, the finished prose does not tell you which claims were retrieved, which were inferred, and which were supplied without evidence.
The better instruction is not necessarily longer. It belongs to a different design.
Code retrieves the material. A model works over that material. Code checks the requirements it can check. A human approves the result.
The distinction is not between an unintelligent component and an intelligent one. It is between jobs with different contracts.
Fetching has a contract. Writing has a contract. Validation has a contract. Approval has a contract.
When you collapse them into "do the research," you make those contracts difficult to see.
Rule 1 says to attach the facts. This chapter makes the attachment a working pipeline.

## The loop, end to end

The chapter's recorded demonstration is a research loop with five stages:

1. Code pulls the facts.
2. A cheap model ranks the material.
3. The best model writes.
4. Code validates and queues the output.
5. A human approves it.

The plan identifies this as a real, verified run. The related evidence register records the self-education loop as verified live, with ten tools checked and nine baselines.[^1][^2]
That is the supported shape of the demonstration.
⚠️ The supplied material does not include the run's retrieved documents, ranking criteria, written output, validation rules, or approval record. Those details cannot be reconstructed here. The stage sequence is supported by the chapter plan; the counts come from the evidence register.
Even at that level, the important design choice is visible.
The writer does not begin with an empty page and a request to know the world. It begins with material retrieved for the task.
The ranking model does not have to perform the final writing. The writing model does not have to manage the queue. The queue does not approve its own contents.
Each component receives a bounded job.

## Fetching is not knowing

"Code pulls facts" needs a careful reading.
Code can retrieve a document, extract a field, record a date, or request information from a designated service. That does not make every retrieved statement true.
A bad source can be fetched perfectly.
An outdated record can arrive intact.
A correct extraction can preserve a claim that never deserved to be trusted.
The fetch therefore needs a source contract: where the material may come from, what counts as relevant, how its origin is retained, and when it needs renewing. These are design requirements for the pipeline, not additional claims about the verified run.
The point is to stop the model's fluent answer from becoming the source.
You should be able to follow a factual statement back through the draft to the retrieved material. Where the material does not support the statement, the system needs to expose the gap rather than quietly complete the sentence.
That is the boundary carried by Rule 12: confinement is the design.
The model may transform the supplied material. It may organize it, compare passages, extract themes, and write an explanation. But those permissions do not include manufacturing the missing evidence.

## Ranking is not a certificate of truth

The cheap model's job in the recorded pipeline is to rank.[^1]
That can be a useful division of labor, provided you say what the ranking means.
Relevance to the task is not the same as reliability. Readability is not the same as accuracy. A document that looks promising is not necessarily one that supports the final claim.
A ranking stage should therefore have a named criterion. Otherwise, "these are the best results" hides another undefined judgment.
This also carries forward the lesson of the previous chapter. A model's judgment remains something to check. Putting it in the middle of a pipeline does not turn it into evidence.
The ranking can narrow the material the writer receives. It should not erase provenance or make a source's unsupported claims authoritative.
Likewise, "the best model writes" should not mean the model that announces it is best. It means the writer selected for the task under the relevant evaluation.
⚠️ The supplied record does not identify the models or establish their comparative performance in this particular run. "Cheap" and "best" are the roles named in the plan, not independently documented price or quality findings.[^1]

## Let language do the language work

Once the material is attached, the writing task becomes more precise.
Not: Tell me what is true about this subject.
But: Explain what this material supports, for this reader, in this form.
That still leaves substantial work.
The model can turn fragmented notes into a readable argument. It can separate a main point from supporting detail. It can organize information around the reader's question rather than the order in which documents arrived.
Those are the intended language operations in this design. Their success still needs checking in the output.
A useful writing contract would require the draft to preserve the distinction between supported claims, interpretation, and missing information. It would require citations to remain attached. It would forbid silently replacing an awkward uncertainty with a smooth conclusion.
The writing can become clearer without making the evidence appear stronger.
That is the standard: improve the expression, not the apparent certainty.

## Validation is not approval

In the recorded loop, code validates the output and puts it in a queue. A human then approves it.[^1]
Those are separate stages for a reason.
Code can test requirements you have made executable. Depending on the implementation, those might include required fields, permitted formats, or the presence of source references.
But passing such checks would establish only that those checks passed.
It would not automatically establish that a cited passage supports the sentence beside it, that an interpretation is fair, or that the work should be published.
⚠️ The actual validation checks in the verified run were not supplied. These examples describe possible checks, not observed features.
The queue is similarly modest. It holds work awaiting a decision. It is not a decision.
Keeping human approval distinct prevents the completed draft from being mistaken for completed judgment. The pipeline can prepare an output for consideration without granting itself authority to release it.

## A second axis: who should do the job?

The notebook boundary answers one question:
What material may this task use?
The capability bus addresses another:
Which model should attempt it?
This second axis sits outside the notebook frame. It concerns routing rather than the evidential contents of a particular writing task.
The verified implementation is recorded in src/lib/services/model-bus.ts, a 699-line file present in both repositories. Its self-assessment prompt asks, in substance:
Can you answer this completely and accurately right now? Would the user be satisfied with your answer? Should this go to a smarter cloud model?
It also supplies a conservative instruction:
> If you're unsure, lean toward canHandle: false.
That is an important qualification. The system is not discovering an inner faculty of reliable self-knowledge.
It is asking for a routing decision under an instruction biased toward declining.
The useful claim is not "the model knows its limits."
It is "the model can propose whether to attempt this task, and the system can check what happens next."

## The self-report is a route, not evidence

This is the narrow place where a model's self-report can serve a practical purpose.
If it says the task should be escalated, the system has a routing signal.
If it accepts, the attempted output still has to meet the task's checks.
Acceptance is not proof of competence. Declining is not proof that a stronger model is necessary. Both are decisions within a bounded process.
The evidence register describes the design this way: it does not trust the self-assessment; it bounds it.[^3]
That distinction keeps the capability bus compatible with Rule 1.
The model's answer to "can you do this?" is not used as a source for the research. It does not establish a fact about the world. It proposes where the work should go.
And even that proposal earns its usefulness through outcomes.
⚠️ Routing is checkable only to the extent that the attempted task has meaningful checks. The supplied record does not establish universal routing accuracy or provide an acceptance-and-failure rate.

## Smaller hardware becomes a question to test

The author reports good results doing research with models as small as 1.5 billion parameters. That is first-hand experience, not a benchmark statistic.[^4]
The implementation record also identifies local-small as isCPUFriendly, includes BitNet integration for GPU-free inference, and records a CPU-only setup document recommending qwen2.5:1.5b.[^3][^5]
⚠️ These are recorded implementation and documentation facts. Current CPU-only operation of qwen2.5:1.5b remains a pre-publication verification requirement; it is not established here by the recommendation alone.
⚠️ The author's quoted recollection also mentions "laptops without CPUs." That wording cannot establish a literal hardware configuration. It should not be silently converted into a verified claim about machines without GPUs.
The design nevertheless poses a useful hardware question.
How much of the work can a smaller model handle when the facts are supplied, the task is bounded, and declining is allowed?
Every verified success on the smaller route identifies work that need not take the larger route. Every correctly handled escalation preserves the option to use more capable resources when needed.
This is a possibility for reducing the requirement, not evidence that compute use inevitably falls over time.
The smallest useful model is not simply the smallest one that says yes. It is the smallest one whose accepted work passes the checks—and whose routing decisions do not undermine the process.

## Should the process exist?

Before making the loop faster, ask what it is for.
Rule 21b belongs here: automating a process is not the same as justifying it.
A pipeline can efficiently retrieve material nobody needs, rank it against a poorly defined objective, write an unnecessary report, and fill an approval queue that consumes human attention.
Every stage might operate as designed.
The process might still be the wrong process.
Name the decision the research is supposed to support. Name the person who needs the output. Name what would count as enough.
Then ask whether the proposed automation improves that work or merely increases its volume.
The human approval stage should preserve that question, not reduce the human to the final button in an otherwise unquestioned machine.

## Split the task

The practical fix is simple to state:

> Separate what code must do from what language should do.

Let code retrieve designated material, preserve its origin, enforce executable requirements, and manage state.
Let the model work over the material within the writing contract.
Let routing decide which model gets the attempt—not which unsupported claims become true.
Let a human decide whether the result deserves approval and whether the process deserves to continue.
The boundaries do not make the tool less useful.
They make its usefulness inspectable.

## Remember This

> Separate what code must do from what language should do.
>
> Give code the fetched material, the origin, the executable requirements, and the state.
>
> Give the model the material within the writing contract.
>
> Let a human decide approval—and whether the process deserves to continue.

---

[^1]: **The research-loop demonstration** — the author's own system, verified in
  documentation this session. `docs/SELF-EDUCATION.md` in the PersonalAI-Dashboard
  repo documents the loop's stages: RESEARCH (code — GitHub releases API per tool,
  diffed against last seen), RANK (low-cost model — relevance 0–10 plus a one-line
  note per change), CONTEXTUALISE (Alpha model — writes a markdown improvement report
  grounded in the findings), REPORT (disk), QUEUE (disk — `proposals.json`, status
  pending → approved/rejected), HUMAN APPROVES (nothing is implemented
  automatically). ⚠️ The doc shows a six-stage loop (research, rank, contextualise,
  report, queue, approve); the chapter's five-stage summary compresses report+queue
  into "validates and queues." The chapter's ⚠️ — that the run's retrieved documents,
  ranking criteria, written output, validation rules, and approval record were not
  supplied — is the honest register, and the chapter frames the stage sequence as
  "supported by the chapter plan." No distinct code-validation stage is documented in
  SELF-EDUCATION.md; the validation examples in the chapter are the author's own,
  framed as "possible checks, not observed features."

[^2]: **The self-education loop** — confirmed in `docs/SELF-EDUCATION.md`,
  "Verified behaviour (live)": `POST {action:'run'}` → `checked: 10`,
  `baselines: 9`, report written to `data/improvements/…-improvement-report.md`.
  The chapter reports only the counts, with the author's own ⚠️ that the
  tool-level records and outcomes were not supplied.

[^3]: **The capability bus** — confirmed in `src/lib/services/model-bus.ts` (699
  lines): the self-assessment prompt ("Can you answer this COMPLETELY and
  ACCURATELY right now? Would the user be SATISFIED with your answer? Should this
  go to a smarter cloud model?") and the fail-safe ("If you're UNSURE, lean toward
  canHandle: false") at line 361. `local-small` tier flagged `isCPUFriendly: true`
  (line 103). BitNet integration confirmed in `src/lib/models/model-router.ts`
  (BitNet b1.58 2B, provider `bitnet`, "CPU-optimized" — line 48-54). ⚠️ The author's
  paste says the implementation record "includes BitNet integration for GPU-free
  inference" — confirmed in model-router.ts, not model-bus.ts; the chapter's
  attribution to the model-bus file is the plan's shorthand for the routing layer.

[^4]: **The author's 1.5-billion-parameter testimony** — first-hand experience,
  presented as such; no external source required. ⚠️ The register's existing note
  stands: re-verify the 1.5b CPU-only figure on the author's hardware before print.
  The author has since pointed to a newer demonstration (a sub-1.5b model following
  instructions, https://www.youtube.com/watch?v=40FXBcRz4_k). The author's quoted
  recollection says "laptops without CPUs" — the chapter keeps the author's own ⚠️
  that this wording cannot establish a literal hardware configuration.

[^5]: **CPU-only documentation** — confirmed: `docs/CPU-ONLY-SETUP.md` recommends
  `qwen2.5:1.5b` (line 36: `ollama pull qwen2.5:1.5b`; line 96: the model table marks
  it "Recommended"). ⚠️ Recommending a model in a setup doc is not the same as
  verifying it runs CPU-only today; the chapter carries the author's own ⚠️ to that
  effect.

## The rules this chapter carries

**Rule 1 — *It doesn't know things.* (primary).** "Fetching Is Not Knowing": code
retrieves material, but that does not make every retrieved statement true — the model
must work over supplied material, not become the source.

**Rule 12 — *Confinement is the design, not a limitation.* (carried).** "Fetching Is
Not Knowing" and "A Second Axis": the boundary is where the material comes from and
what the model may do with it; the capability bus is a second, independent axis
(routing, not evidential contents).

**Rule 21b — *Automating a process is not the same as justifying it.* (carried).**
"Should the Process Exist?": a pipeline can efficiently do the wrong thing; name the
decision the research is supposed to support before automating it.

**Rule 13 — *Right-size the model to the task.* (carried).** "Smaller Hardware
Becomes a Question to Test": the smallest useful model is the one whose accepted work
passes the checks.

---

*Verification: the author's prose is adopted verbatim (2,287 words), with one
disclosed correction ("judgement" -> "judgment," 1 occurrence — U.S. English is
the book standard). A trailing block in the paste ("Ask for help with your
writing… / No project / No writing style / Enhanced") is a UI artifact — a
writing-assistant prompt that leaked into the paste — not chapter prose; removed.
The paste's "Sources and evidence boundaries" block ([1]-[5]) is converted into
footnotes; all five verified this session against the PersonalAI-Dashboard repo:

- [1] The research-loop demonstration — confirmed in docs/SELF-EDUCATION.md. The
  doc shows a SIX-stage loop (research, rank, contextualise, report, queue,
  approve); the chapter's five-stage summary compresses report+queue into "validates
  and queues." ⚠️ No distinct code-validation stage is documented in the doc — the
  chapter's validation examples are the author's own, framed as "possible checks,
  not observed features," and the chapter's ⚠️ that the run's validation rules were
  not supplied is kept verbatim. The stage SEQUENCE is supported by the chapter plan;
  the counts come from the evidence register.
- [2] The self-education loop — confirmed in docs/SELF-EDUCATION.md ("checked:
  10, baselines: 9").
- [3] The capability bus — confirmed in model-bus.ts (699 lines; fail-safe at line
  361; local-small isCPUFriendly: true at line 103). BitNet integration confirmed in
  model-router.ts (BitNet b1.58 2B, provider 'bitnet', 'CPU-optimized'). The
  chapter's attribution of BitNet to the model-bus file is the plan's shorthand for
  the routing layer — noted, not corrected (the author's framing).
- [4] The author's 1.5b testimony — footnoted as such; the YouTube demonstration
  link is recorded; the register's ⚠️ to re-verify before print stands.
- [5] CPU-ONLY-SETUP.md — confirmed: recommends qwen2.5:1.5b.

The chapter's three ⚠️ flags (run artifacts not supplied; models not identified /
"cheap" and "best" are roles not findings; validation checks are possible not
observed) and the two hardware ⚠️ flags (CPU-only operation unverified today;
"laptops without CPUs" is recollection, not a literal configuration) are the author's
own, kept verbatim. The chapter quotes Rule 1, Rule 12, and Rule 21b by name — the
book's own established rules. Placement: Chapter 22, Part III — between Ch. 21
(You cannot ask a model who's best) and Ch. 23 (Let it build code, because code is
checkable). The five-stage pipeline is the chapter's spine. Carries Rule 1 (primary),
Rules 12, 21b, 13.*
