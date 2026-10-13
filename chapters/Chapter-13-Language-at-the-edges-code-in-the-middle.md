# Chapter 13 — Language at the Edges, Code in the Middle

*(Part II — The Model That Works. The division-of-labor chapter: the model
handles language at the edges; deterministic code handles the middle where the
organization's rules must hold. The provider-router demo (a fixed order, no model
involved) is the chapter's spine. Pairs with Ch. 14 (the contract that guards the
handover) and Ch. 15 (the plumbing that feeds the middle).)*

---

Language at the Edges, Code in the Middle
A customer writes:
"I think you charged me twice. Can you sort it out?"
That is a language problem.
The customer has not supplied a neat form. They have described a concern in their own words. A model can help interpret the request and prepare a clear response.
But deciding whether two charges occurred is not a language problem.
Neither is checking whether a refund is permitted, calculating its amount, or recording the transaction.
Those jobs need rules that produce consistent results.
The distinction is simple:
Use the model to understand and explain. Use ordinary software to check, decide, and carry out the agreed procedure.
Language at the edges. Code in the middle.
This is not an argument against capable models. It is an argument for giving them the work that benefits from their capabilities—and keeping them out of decisions that do not need them.
## A Conversation Is Not the Whole Process
AI demonstrations often make the entire workflow look like a conversation.
A person asks for something. The model considers it, chooses a tool, performs the task, and reports success.
From the outside, that can look wonderfully simple.
Inside the organization, however, several different jobs have been bundled together.
Understanding a request is one job.
Checking permission is another.
Finding the current record is another.
Applying a policy is another.
Explaining the result is another.
They do not all need the same kind of intelligence.
Consider an illustrative expense query:
"Can I claim the hotel from last week's client visit?"
A model can help identify what the employee is asking. It can also explain the eventual answer in plain language.
Between those two moments, the system may need to establish which policy applies, whether the required receipt exists, whether the claim is within the permitted amount, and who must approve it.
Where those conditions are already defined, they should be checked directly.
The model should not improvise a company policy because it can describe one convincingly.
Nor should it decide that a missing receipt probably does not matter.
The middle of the process is where the organization's rules must hold.
## What “Deterministic” Means
Builders use the word deterministic for a process that produces the same result from the same inputs and rules.
A manager can think of it as a dependable procedure.
If the amount exceeds the approval limit, the claim goes for approval.
If the user lacks permission, access is denied.
If the required record is missing, the process stops.
The result does not depend on whether a model finds an exception persuasive or chooses a different phrasing today.
This does not mean ordinary software is automatically correct. A mistaken rule can be applied consistently. A stale record can produce a consistently wrong result.
The rules and records still need care.
But once you have agreed on the rule, you should not ask a model to reinvent its application each time.
Consistency makes the procedure inspectable. You can explain why a decision occurred, test it, and change the governing rule deliberately.
That is different from asking a model to reason its way through the same settled decision over and over.
## Do Not Ask a Model to Follow a List You Already Have
Suppose your organization can use three providers for a particular task.
You have already decided their order:
Use the preferred provider if it is available and permitted. Otherwise, try the second. Then the third. If none qualifies, stop.
There is no language problem here.
The procedure is straightforward:
Check which providers are available. Remove those that do not meet the requirements. Follow the agreed order. Select the first remaining option.
A model does not need to participate.
Given the same availability information, restrictions, and preference order, the system should make the same choice.
If availability changes, the choice may change. That is not inconsistency. It is the procedure responding to a changed input.
This example illustrates the chapter's central division of labor. The selection policy belongs to the organization. Ordinary software applies it.
Adding a model would introduce another interpretation where no interpretation is needed.
It would also make a simple question harder to answer:
"Why did the system choose that provider?"
The dependable answer is:
"Because it was the first available provider that met our requirements."
Not:
"Because the model thought it was best."
## Right-Sizing Starts Before Model Selection
Rule 13 says:
Right-size the model to the task.
It is tempting to read that as a shopping instruction: compare models and choose the least expensive one that performs adequately.
That is part of it.
But there is an earlier question:
Does this step need a model at all?
If the work is checking a permission, comparing an amount with a limit, or following a fixed provider order, ordinary software may be the appropriate tool.
No model is smaller or cheaper than a model you do not need to call.
That does not mean eliminating models from difficult work. It means separating difficult language work from routine procedural work.
Then, for the parts that genuinely need a model, choose the smallest one that meets the requirements reliably.
A task may need a capable model to interpret a complicated request. The same task may need no model to check an account identifier or enforce an approval threshold.
Right-sizing applies to the parts of the workflow, not just the workflow as a whole.
## The Source and the Model Are Separate Choices
There is another distinction worth preserving.
What information may the tool use?
And which model should process that information?
These are separate questions.
A confined tool answers from the material you provide. That boundary should not depend on choosing one particular model.
The supplied evidence for Poppy illustrates this separation. Its documented interface allows a request to be directed at a particular knowledge board while also allowing a model to be selected for that request[^1].
The useful point is not that one product wins.
It is that confinement and model choice can be independent.
Your approved material can remain the approved material when the model changes. A larger model does not need broader permission. A smaller model does not need weaker source requirements.
For a manager, this matters at purchase time.
Ask separately:
"Can we control the information the tool uses?"
And:
"Can we choose the model appropriate to the task?"
A product may meet one requirement better than the other. That is a fit question, not a vendor ranking.
The organization should know which freedom it is buying and which restriction it is accepting.
## A Smaller Model Can Try Without Being Trusted
The author's capability service explores a different kind of routing.
It asks a model whether it can complete a task or whether the work should go to a more capable model. The instructions encourage it to decline when unsure.
That is not the same as the fixed provider selection described earlier.
The provider selection follows an agreed order without asking a model to judge it.
The capability service asks for a model's assessment because the difficulty of language work may not be obvious from a simple list of conditions.
The distinction must remain visible.
The model's assessment is useful as a proposal. It is not proof that the model knows its limits.
"I can handle this" means the model may attempt the task. It does not mean the result has passed inspection.
The system still needs to check the output and respond appropriately when the attempt fails.
This arrangement can support an economical workflow: try a smaller model where appropriate, retain the required checks, and move the task elsewhere when necessary.
The author reports successful research work using models as small as 1.5 billion parameters[^2]. That is first-hand experience, not a promise that every research task can run on a small model.
The lesson is not a particular hardware specification.
It is that greater spending should follow demonstrated need rather than become the starting assumption.
## Keep Confidence Out of the Permission Path
There is an important difference between allowing a model to suggest where work should go and allowing it to decide what it may do.
A routing suggestion can be bounded.
Permission must be enforced.
A model may suggest that a task needs a more capable model. It must not grant itself access to additional records to complete it.
It may identify a possible refund request. It must not decide that refund authority follows from having understood the request.
It may explain why an exception seems reasonable. It must not create the exception.
Confidence is not evidence, and it is not permission.
The middle of the workflow should preserve that distinction regardless of how persuasive the language becomes.
## What the Manager Should Ask
Before approving an AI feature, ask the builder to walk through it without using the phrase "the AI handles it."
Where does language enter?
Which steps require interpretation?
Which decisions are already governed by rules?
Where does language leave?
This is not a request for a technical diagram. It is a request for a clear account of responsibility.
For every step, the team should be able to explain why a model is needed—or why it is not.
If the answer is "because we already have a model in the workflow," that is convenience, not justification.
If the answer is "because the input varies and requires interpretation," there may be a genuine language task.
If the answer is "because we must compare this value with that limit," the organization probably already knows the procedure.
The goal is not to minimize the model's role for its own sake.
The goal is to place discretion only where it is useful and keep settled rules dependable.
## Where the Two Kinds of Work Meet
Language at the edges and code in the middle creates a useful division.
The model helps turn a person's request into something the system can work with.
The system applies permissions, checks records, follows procedures, and controls actions.
The model then helps explain the outcome to the person.
But the handover between those stages needs care.
What happens if the model adds an instruction that nobody requested?
What happens if it omits something the procedure requires?
What happens if a proposed answer looks sensible but does not meet the assignment?
The division of labor alone cannot answer those questions. The boundary needs an agreement about what may cross it.
That agreement is a contract.
The model's output must meet the contract before the system acts. The system's result must remain intact when the model explains it. Neither handover should become an opportunity to invent permission or alter the decision.
That is the next chapter's subject.
For now, remember the placement:
Language at the edges. Code in the middle.
Use the model where words need interpretation or explanation.
Use dependable procedures where the organization has already decided what must happen.
And never confuse a tool's ability to describe a decision with authority to make it.

## Remember This

> Language at the edges. Code in the middle.
>
> Use the model where words need interpretation or explanation.
>
> Use dependable procedures where the organization has already decided what must happen.
>
> And never confuse a tool's ability to describe a decision with authority to make it.

---

[^1]: **Poppy AI** (getpoppy.ai) — its documented API takes a per-request `model`
  field (allowed values include `claude-sonnet-4-6` (default), `claude-sonnet-4-5`,
  `o3-mini`, `gpt-4o`, `grok-2-1212`, `gpt-4o-mini`) and scopes the chat to a
  `board_id` ("Chat with knowledge base") — i.e., confinement (the board) and model
  choice (the per-call field) are two independent parameters. Verified against
  Poppy's own API documentation, 12 October 2026. ⚠️ Product documentation;
  capabilities change.

[^2]: The author's first-hand experience — testimony, presented as such; no external
  source required. The author has since pointed to a newer demonstration of the same
  point (a sub-1.5b-parameter model following instructions, shown at
  https://www.youtube.com/watch?v=40FXBcRz4_k). ⚠️ The register's existing note stands: re-verify the 1.5b
  CPU-only figure on the author's hardware before print. No 1.5b-class model is
  installed on this machine (`qwen3.5:9b` at 6.6 GB is the smallest local model
  here), so the figure could not be re-measured in this session.

## The rules this chapter carries

**Rule 13 — *Right-size the model to the task.* (primary).** "Right-Sizing Starts
Before Model Selection" is Rule 13 extended past shopping: *does this step need a
model at all?* No model is smaller or cheaper than a model you do not need to call.

**Rule 14 — *Match the effort to the question.* (carried).** The whole division of
labor: place discretion only where it is useful, keep settled rules dependable.
Observation, not assertion — the model interprets language; code checks, decides,
and carries out.

**Rule 2 — *Confidence is not evidence.* (carried).** "Keep Confidence Out of the
Permission Path": confidence is not evidence, and it is not permission.

---

*Verification: the author's prose is adopted verbatim (1,831 words), with two
disclosed edits: (1) "labour" -> "labor" twice (U.S. English is the book standard;
the author's own paste used the British spelling); (2) the section headings converted
from plain Title Case lines to `## ` markdown headings. The author flagged the
closing placement paragraph as "out of order" in the paste — the thesis line
("Language at the edges. Code in the middle.") already appears in the opening, and
the author wrote the closer as a closer ("For now, remember the placement"), so it
is kept where written; the flag is noted here, and moving the block earlier is a
one-line edit if the author wants it.

Claims checked:
- **The provider-router demo** (three providers, fixed order, no model involved) is
  the outline's specified demonstration, framed as a procedure ("probe, filter,
  walk the order, take the first available") — this is the designed behavior of the
  author's own routing code, confirmed in `model-router.ts` and
  `sdk.server.ts:getBestLightweightModel` (priority list walked in order, fallback to
  first available). ⚠️ The chapter presents it as an illustrative procedure, not a
  recorded run — consistent with the book's ⚠️ flag for specified procedures.
- **Poppy's API** (confinement + per-call model choice as independent parameters) —
  verified against Poppy's documented interface, 12 October 2026. Footnoted.
- **The capability service** ("A Smaller Model Can Try Without Being Trusted") —
  the author's model-routing service, verified in `model-bus.ts` (699 lines; the
  fail-safe "If you're unsure, lean toward canHandle: false" at line 361; the
  routing-proposal-not-guarantee framing matches the code's design).
- **The 1.5-billion-parameter figure** — the author's first-hand testimony about his
  own laptop; footnoted as such, flagged for re-verification before print (the
  register's existing ⚠️ note). Not re-measurable in this session.
- The chapter quotes Rule 13 and Rule 2 by name — the book's own established rules.

The chapter's argument (the division of labor, what "deterministic" means, the
manager's four questions, the handover that needs a contract) is argument about
system design, not external fact. Placement: Chapter 13, Part II — between
Ch. 12 (The world of tokens) and Ch. 14 (Everything is a contract). Carries
Rule 13 (primary), Rules 14, 2.*
