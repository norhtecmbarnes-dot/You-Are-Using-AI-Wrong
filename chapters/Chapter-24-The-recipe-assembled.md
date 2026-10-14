# Chapter 24 — The Recipe, Assembled

*(Part III — What Right Looks Like. The assembly chapter: the full architecture in one place — two pillars (confinement of knowledge, the capability bus), the connecting elements (contracts, measurement, discovery, human gates), the failure ledger, and the eight-step recipe. The LAST SPECCED SKELETON — after this chapter, every chapter in the book is drafted.)*

---

The architecture is easier to see when you stop looking at the model.
Look instead at what surrounds it.
Where do the facts enter? What is the model allowed to do with them? What happens when it declines? What checks the output? Who authorizes the next action? What survives after the conversation ends?
Those questions describe one system.
The contracts, the attached sources, the tests, the provider registry, the approval queue: they are not separate remedies for unrelated complaints. They place boundaries around the same problem.
A model can produce a plausible response without establishing that the response deserves to be used.
The scaffold makes that distinction operational.
Two pillars carry it: confinement of knowledge, and a capability bus that lets a smaller model decline. The first bounds the evidence. The second routes the work. Contracts, measurement, discovery, and human gates connect them.[^1]
Nothing needs to be added here. This is the recipe assembled.

## First pillar: confine the knowledge

Begin with a defined unit of work: the notebook, project, or other boundary established for the task.
Attach the material that belongs inside it.
The model's job is to transform that material, not substitute its own unsupported account of the subject. This is Rule 1 made architectural: attach the facts rather than request that the model possess them.[^1]
Confinement does not certify the sources. It establishes which sources the work is allowed to depend on.
That distinction matters. A bounded system can still receive bad material. But the boundary gives the investigation somewhere to go. You can inspect what was supplied, identify what supported a statement, and see where the output exceeded the evidence.
Without that record, an unsupported sentence can disappear into the general explanation that "the model said it."
Rule 12 is the spine: confinement is the design, not a limitation.
The boundary is not something to relax when the answer becomes inconvenient. It is what makes the answer accountable.

## Second pillar: let the small model decline

Confinement answers what the model may use.
The capability bus answers which model should attempt the work.
The recorded implementation asks a model whether it can answer completely and accurately, whether the user would be satisfied, and whether the task should go to a stronger cloud model. Its conservative instruction is explicit: if unsure, lean toward canHandle: false.[^2]
That is a routing mechanism, not proof that the model knows its limits.
The self-assessment proposes a path. The result still needs checking.
A smaller model accepting a task does not establish that its answer is correct. A smaller model declining does not, by itself, establish that the task requires a larger one. The routing becomes useful through the bounded process around it.[^2]
These two pillars must remain separate.
Escalating to a stronger model does not authorize new sources. Receiving confined material does not establish that a smaller model can handle the task.
One boundary concerns evidence. The other concerns capability.
Neither replaces the other.

## Contracts connect the parts

Before a component receives a call, define what it must receive and what it may return.
Then validate the result before anything acts on it.
The contract discipline established earlier is deliberately strict: define the shape before the call, validate before action, reject rather than silently repair an invalid result.[^1]
Otherwise, an invalid response can become an apparently valid instruction through an invisible act of interpretation.
The contract keeps the disagreement visible.
The same discipline carries through the research loop: code fetches, a model ranks, a writer transforms the supplied material, code validates and queues, and a human approves. Those are distinct jobs, not one broad permission to "do the research."[^3]
Rule 6 gives those boundaries somewhere durable to live.
A correction made in conversation is not the same as a rule enforced by the system. Where a requirement can be expressed in code, it can persist beyond the session in which somebody noticed the need for it.
That is the difference between asking for better behavior again and making the acceptance condition explicit.

## Discover what is present

The provider registry addresses another boundary: the difference between a tool being described and a tool being available.
The project's recorded failure was that the provider layer probed for tools that were registered but not present. The remedy was discovery at call time rather than assumption at build time. The decision path does not require an LLM.[^1][^4]
This belongs in the architecture because each user has their own tools.
A remembered configuration cannot establish what is available now. The system needs to inspect the environment in which it is about to act.
Discovery supplies that observation. The model does not need to invent an explanation of what ought to be installed.
The principle is modest: check the thing you are about to depend on.

## Measure, record, report; let the human promote

The Alpha challenge supplies the measurement discipline.
Four models faced five fixed, code-scored tests, including grounding. Three scored perfectly. One was caught inventing. Ties went to the incumbent. No model voted.[^5]
The system did not need a persuasive account of which candidate deserved promotion. It needed the recorded results under the agreed rules.
That is also the boundary around self-improvement.
The system can run checks, preserve baselines, record outcomes, and report differences. The self-education loop is recorded as verified live: ten tools checked, nine baselines.[^6]
Those counts do not establish that every tool improved. They establish the recorded extent of the checks.
The human promotes.
"Without a model deciding anything" must be read at that authority boundary. Models still produce language outputs and routing assessments. They do not acquire authority to promote themselves, approve their own work, or replace the acceptance rules.
The approval queue preserves the distinction between work prepared and work authorized.[^1][^3]

## The implementation record

The chapter's implementation map is DASHBOARD-IMPLEMENTATION.md.
Its stated purpose is to connect the rules to the files implementing them and distinguish completed work from partial work and work not yet written.[^1][^7]
That honesty is part of the architecture.
A partial implementation does not become complete because the surrounding explanation is coherent. An unwritten boundary cannot protect a live action.
⚠️ The map itself was not supplied with this chapter. Its individual entries, file mappings, and current status cannot be reproduced here. The supplied concept identifies it as the implementation record; that is not equivalent to a fresh runtime verification.
The map tells you where to inspect. The checks tell you what happened when the implementation ran.
Neither should impersonate the other.

## The ledger: where this project went wrong

These are not imagined warnings. They are the failures the author supplied as part of the project record. Their value depends on keeping the evidence boundary visible.[^4]

1. **We assumed the tool existed**
   Assumption: registration meant availability.
   What happened: the provider layer encountered tools that were registered but not present.
   Rule: discover at call time. Each user has their own tools.[^4]
   The mistake was in the dependency assumption, not in the model's eloquence. The repair belonged in discovery.

2. **We trusted the fluent answer**
   Assumption: an answer that fitted the question deserved to enter the working account.
   What happened: the book's correction record includes a claim of being first, two tools treated as one company, an effect that did not replicate, and a paper whose numbers changed between versions.[^4]
   Rule: find the source or run the test. Preserve the correction.
   ⚠️ The supplied ledger names these corrections but does not provide the underlying sources, wording, or chronology. No more detailed reconstruction is justified here.
   The author is in this ledger because the book's method was needed while writing the book. It was not merely advice for somebody else.

3. **We let a model judge models**
   Assumption: asking for a ranking would establish which model to use.
   What happened: the project replaced that kind of recommendation with the Alpha challenge's fixed tests and code scoring.[^4][^5]
   Rule: a model's ranking is another claim. Measure the task.
   The recorded result included a tie. The incumbent stayed. The measurement did not need to manufacture a dramatic winner.

4. **We treated more capability as a source**
   Assumption: moving to a bigger model would solve a knowledge problem.
   What happened: the supplied project ledger identifies this as a failure, but does not provide the specific run, models, or outputs.[^4]
   Rule: attach the missing evidence. Escalation is not provenance.
   ⚠️ The skeleton also states that scale improves fluency faster than factuality. No supporting comparative evidence was supplied here, so that general claim is not established in this chapter.
   The architectural conclusion is narrower: a larger model's answer still needs support.

5. **We built around versions**
   Assumption: a named product version could serve as a durable foundation.
   What happened: the supplied ledger identifies version dependence as a project scar, without naming the affected component or change.[^4]
   Rule: preserve the mechanism; discover and test the current implementation.
   ⚠️ A specific breakage or chronology cannot be supplied from this summary. Nor does it establish that every versioned dependency is unsuitable.
   The durable recipe is the contract and the check, not a promise that today's product names will remain current.

## Witness is not a universal citation

The author's cases—Dallas, NCS, FinWise, and MARTA—belong under Rule 15b: testimony is its own source, but only for what was witnessed.[^1]
⚠️ Their underlying accounts were not supplied here. They cannot be expanded into incidents, outcomes, or independent corroboration.
An author can report what they observed. That does not automatically establish another person's motive, an unseen cause, or a general effect.
Rule 15c supplies the necessary corollary: most of what a person says is not a claim.
A preference, a question, a recollection, or a request should not be flattened into the same category as an assertion of fact. The discipline is to identify the factual commitment and support it—not to turn every conversation into an audit.

## The assembled recipe

1. Confine the evidence.
2. Discover the available tools.
3. Define the contracts.
4. Let the capability bus propose the route, including decline.
5. Give the selected model the supplied material and the bounded language task.
6. Validate what can be validated. Measure performance against fixed criteria. Preserve the results.
7. Queue consequential work for approval.
8. Let the human promote changes.

That is one system, not a list of complaints.
The model remains useful inside it. What changes is the source of authority.
Not fluency. Not confidence. Not a claim of completion.
The supplied evidence, the executable boundary, the recorded result, and the human decision.

---

[^1]: **The architectural synthesis and rule set** — `00-BOOK.md` §7 (Chapter 24
  plan) and the supplied assembly concept. The two pillars (confinement of knowledge,
  capability bus), the connecting elements (contracts, measurement, discovery, human
  gates), and the authority boundary ("without a model deciding anything") are the
  book's own design, assembled from its own chapters. Rule 1, Rule 6, Rule 12, and
  Rules 15b/15c are quoted by name — the book's own established rules.
  `DASHBOARD-IMPLEMENTATION.md` exists in the book repo (15,882 bytes) and its stated
  purpose matches the chapter's description; spot-checked this session: Rule 1
  (attach the facts) ✅ `src/lib/config/knowledge-policy.ts`; Rule 6 (rules in code)
  ✅ policy modules; Rule 12 (confinement) ✅ `knowledge-policy.ts` + brand/project
  document scoping. The chapter's ⚠️ — that the map was "not supplied with this
  chapter" — is the honest register about the chapter's own supplied material; the
  map is real and in the repo, and its key rows verified.

[^2]: **The capability bus** — confirmed in `src/lib/services/model-bus.ts` (699
  lines): the self-assessment prompt ("Can you answer this COMPLETELY and ACCURATELY
  right now? Would the user be SATISFIED with your answer? Should this go to a smarter
  cloud model?") and the fail-safe ("If you're UNSURE, lean toward canHandle: false")
  at line 361. ⚠️ Spelling note: the paste said "lean towards"; the source says "lean
  toward" — corrected to match the source (and U.S. spelling).

[^3]: **The research loop** — the Chapter 22 plan's recorded verified run: code
  fetches, a cheap model ranks, the best model writes, code validates and queues, a
  human approves. Confirmed in `docs/SELF-EDUCATION.md` (six-stage loop; the
  five-stage summary compresses report+queue). Detailed run artifacts were not
  supplied.

[^4]: **The failure ledger** — the five scars, folded from the retired Chapter 26
  skeleton (`chapters/_folded/Chapter-26-The-ways-this-goes-wrong.md`), which lists
  all five: assuming a tool exists, trusting a fluent answer, letting a model judge
  a model, treating more capability as a source (bigger model), building on anything
  with a version number. The skeleton is the author's own project record; the
  supporting incident records (sources, wording, chronology) were not included —
  the chapter's ⚠️ to that effect is kept verbatim. Scar 1 (provider layer probed
  for tools registered but not present) is consistent with `model-router.ts`'s
  `AVAILABLE_MODELS` registry with `available: boolean` flags.

[^5]: **The Alpha challenge** — confirmed in `src/lib/models/alpha.ts` (BENCHMARK =
  five `BenchCase` entries including grounding) and `docs/SELF-EDUCATION.md`
  ("Verified behaviour (live)": four models benchmarked; the grounding test caught
  one model fabricating; the incumbent defended at 100%). The chapter's account —
  three perfect, one caught inventing, ties to the incumbent, no model voted —
  matches.

[^6]: **The self-education loop** — confirmed in `docs/SELF-EDUCATION.md`,
  "Verified behaviour (live)": `POST {action:'run'}` → `checked: 10`,
  `baselines: 9`. The chapter reports only the recorded extent of the checks, with
  the honest framing that the counts do not establish every tool improved.

[^7]: **DASHBOARD-IMPLEMENTATION.md** — the rule-to-implementation map. Exists in
  the book repo (15,882 bytes); its header states its purpose ("every one of the 21
  rules, mapped to the code that implements it — or honestly marked as not yet
  implemented"). Spot-checked this session: the rows for Rules 1, 6, and 12 verified
  against the named source files. The chapter's ⚠️ — that the map's "individual
  entries, file mappings, and current status cannot be reproduced here" — is the
  honest register about the chapter's own supplied material; the map is real.

## The rules this chapter carries

**Rule 12 — *Confinement is the design, not a limitation.* (primary).** The whole
chapter is Rule 12 made architectural: the scaffold places boundaries around the
same problem — a model can produce a plausible response without establishing that
the response deserves to be used.

**Rule 1 — *It doesn't know things.* (carried).** "First Pillar": Rule 1 made
architectural — attach the facts rather than request that the model possess them.

**Rule 6 — *You cannot teach it anything.* (carried).** "Contracts Connect the Parts":
a correction made in conversation is not the same as a rule enforced by the system.

**Rule 15b — *Testimony is its own source — but only for what you witnessed.*
(carried).** "Witness Is Not a Universal Citation."

**Rule 15c — *Most of what a person says is not a claim.* (carried).** The
corollary: identify the factual commitment and support it; do not turn every
conversation into an audit.

---

*Verification: the author's prose is adopted verbatim (2,479 words). The paste's
"Sources and evidence boundaries" block ([1]-[7]) is converted into footnotes; all
seven verified this session:

- **DASHBOARD-IMPLEMENTATION.md** (cited as [1]/[7]) — EXISTS in the book repo
  (15,882 bytes). Its header matches the chapter's description of its purpose.
  Spot-checked rows: Rule 1 ✅ `knowledge-policy.ts`; Rule 6 ✅ policy modules;
  Rule 12 ✅ `knowledge-policy.ts` + scoping. The chapter's ⚠️ ("the map itself was
  not supplied with this chapter") is the honest register about the chapter's own
  supplied material — the map is real and in the repo.
- **[2] Capability bus** — confirmed in `model-bus.ts` (699 lines; fail-safe at
  line 361). One disclosed spelling fix: the paste said "lean towards"; the source
  says "lean toward" — corrected to match the source.
- **[3] Research loop** — confirmed in `docs/SELF-EDUCATION.md` (six-stage loop;
  the chapter's five-stage summary compresses report+queue).
- **[4] Failure ledger** — the five scars are in the retired Ch. 26 skeleton
  (`chapters/_folded/Chapter-26-The-ways-this-goes-wrong.md`), the source the
  outline says was folded in. All five confirmed present. The ⚠️ that the
  underlying incident records were not included is kept verbatim.
- **[5] Alpha challenge** — confirmed in `alpha.ts` (five BenchCase entries) and
  `docs/SELF-EDUCATION.md` ("the grounding test caught one model fabricating;
  the incumbent defended at 100%").
- **[6] Self-education loop** — confirmed (`checked: 10`, `baselines: 9`).

The chapter's four ⚠️ flags (the implementation map's entries not reproduced
here; the ledger names corrections but provides no underlying sources/chronology;
the "scale improves fluency faster than factuality" general claim not established;
no specific breakage chronology for the version-dependence scar) are the author's
own, kept verbatim. The chapter quotes Rule 1, Rule 6, Rule 12, and Rules 15b/15c
by name — the book's own established rules.

The assembled recipe (8 steps) is the chapter's own synthesis of the book's
architecture — argument, not external fact. The "Witness Is Not a Universal
Citation" section applies the book's own Rules 15b/15c to the author's own cases
(Dallas, NCS, FinWise, MARTA) — the register's evidence-base cases, referenced
with the author's own ⚠️ that their underlying accounts were not supplied.

Placement: Chapter 24, Part III — between Ch. 23 (Let it build code, because
code is checkable) and Ch. 25 (Pushing is not cooperation). This is the LAST SPECCED
SKELETON — after this chapter, every chapter in the book is drafted. Carries
Rule 12 (primary), Rules 1, 6, 15b, 15c.*
