# Chapter 15 — Your Plumbing Is Your Ceiling

*(Part II — The Model That Works. The input chapter: the contract (Ch. 14) governs
what the system will accept; the plumbing (this chapter) supplies the facts it
needs. Closes the "system around the model" run: where the model sits (Ch. 13),
what guards its output (Ch. 14), what feeds it (this chapter).)*

---

The last chapter established a boundary: an answer is not acted on until it meets the contract.
But an answer can meet the contract and still be based on the wrong information.
It can contain every required detail, follow the approved format, and make no unauthorized additions. If the underlying policy expired last month, the answer is still wrong.
That is the next problem to solve.
A contract governs what the system will accept. It does not, by itself, supply the facts the system needs.
Those facts have to come from somewhere dependable. They have to arrive in time, belong to the task, and remain current enough for the decision.
That work is the plumbing.
And the quality of that plumbing sets a ceiling on what the model can usefully do.
A bigger model does not fix a stale fact.
## Same Model, Different Answer
Imagine two systems answering the same employee question:
"What is the current approval limit for travel expenses?"
Both use the same model.
The first has no connection to the organization's approved policy. It receives the question and produces a plausible answer.
It might describe a common approval arrangement. It might qualify its response. It might ask for the policy.
What it cannot establish from the question alone is your organization's current limit.
The second system retrieves the current, approved travel policy and supplies the relevant section with the question. The model can then explain the limit and identify the passage supporting its answer.
The difference is not a more powerful model.
It is access to the right information.
This is an illustrative comparison, not a reported performance test. Its point is the design: the second system has a basis for answering the organization's question that the first lacks.
It can still make a mistake. It may misread the passage or overlook an exception. But there is now something outside the model against which the answer can be checked.
The question has moved from "Where did that come from?" to "Did it correctly explain this source?"
That is a substantial improvement.
## Retrieval Is How Facts Reach the Work
Builders often call this arrangement retrieval-augmented generation, or RAG.
The name is less important than the procedure.
Before the model answers, the system finds relevant material and supplies it. The model uses that material to produce a response.
For a manager, think of it as giving an assistant the correct file before asking for a summary.
The assistant's ability matters. So does the file.
An excellent assistant working from last year's policy is not a substitute for a current policy. An excellent assistant given the wrong customer record cannot produce the right customer answer.
Retrieval is therefore not a minor technical step behind the impressive part.
It determines what information is available to the model when the work happens.
If facts must be supplied, the system's usefulness depends heavily on how well it finds and supplies them.
That is Rule 1 made operational:
It doesn't know things.
The model's training is not an approved source for your current prices, permissions, project requirements, or commitments.
Those belong in records the organization controls.
## The Gain Is Checkability, Not Infallibility
Source-grounded answers are not automatically correct.
Giving a model an approved document does not guarantee that it will interpret every condition correctly. Supplying several documents does not guarantee that it will resolve a conflict properly.
The important improvement is that the answer can have an inspectable basis.
Without supplied evidence, an unsupported claim may be difficult to trace.
With supplied evidence, you can compare the claim with the material the model received.
Did the source actually say that? Was the exception omitted? Was the cited passage relevant?
Retrieval creates the conditions for those checks. It does not perform all of them merely by existing.
The system must still require supported claims and an honest response when the material does not answer the question.
The author's Dashboard expresses the division plainly:
"The LLM is a communications manager, not a knowledge source."
Its governing instructions include "never fill a gap with a guess" and "attribute every specific claim."
Those are important requirements. Their effectiveness still depends on the sources, the retrieval process, and the checks around the answer.
A written rule is a foundation, not a guarantee.
## More Documents Can Mean More Confusion
When a system gives a poor answer, one tempting response is to add more material.
Upload the whole shared drive. Include every policy. Give it all the old proposals.
Surely more information will help.
Sometimes it will. But more material also creates more opportunities to retrieve something irrelevant, obsolete, or intended for a different situation.
A previous proposal may contain a commitment that does not apply to the current bid. A brand document may describe a general capability without establishing that it meets a particular requirement.
The retrieval task is not "find everything."
It is "find the approved information relevant to this job."
The author's Dashboard uses the project as that unit of focus.
The brand remains the continuing context: its voice, positioning, and approved organizational material.
The project identifies the work being done now.
For proposal work, the system retrieves the current project's documents rather than treating the entire brand collection as equally relevant.
That separation matters to a manager. It reduces the risk of yesterday's assignment quietly becoming evidence for today's.
## Date the Knowledge
Rule 12b says:
Put an expiry date on knowledge.
A document can be genuine, approved, and no longer suitable for use.
Prices change. Policies are superseded. Certificates expire. Project requirements receive amendments.
The system needs to know more than whether a document exists.
It needs to know whether the document is still valid for the question being asked.
Not every source requires the same review interval. A short-lived price schedule and a historical project record serve different purposes.
The practical requirement is to assign ownership and a review rule.
Someone must be responsible for deciding when the information needs checking, replacement, or retirement.
An expiry date does not necessarily mean deleting a record. Old records may be essential for understanding past decisions.
It means preventing an old record from silently presenting itself as current authority.
If the source is no longer current, the system should say so or stop for review.
It should not ask the model to bridge the gap with confidence.
## Whitelist the Sources
Rule 12c says:
Whitelist the sources.
That means deciding which sources the system is permitted to rely on.
A document's availability is not the same as its authority.
A draft, an informal message, and an approved policy may all discuss the same subject. They should not have equal standing merely because the search process can find them.
Whitelisting makes that distinction explicit.
For one workflow, approved sources may be the current policy collection. For another, they may be the customer's issued requirements and formal amendments.
The approved set should match the task.
This does not prohibit research or discovery. It separates material worth investigating from material authorized to support a decision.
The manager's question is:
"Who decides what counts as an approved source?"
If nobody owns that decision, retrieval may be efficient without being dependable.
## Keep a Receipt
A useful answer should leave enough of a record to explain how it was produced.
Which documents were supplied? Which model answered? What resources did the attempt use?
The author's Dashboard records documents used in a session and information about the model and documents associated with messages.
That is confinement with a receipt.
The record does not prove that the answer was correct. A document listed as available is not proof that every claim was properly supported by it.
But it provides a starting point for investigation.
Without a record, a bad answer may leave the team reconstructing events from memory.
With a record, they can examine whether the wrong document was retrieved, the right document was misread, or the instructions failed to govern the response.
That distinction helps determine what to fix.
A model upgrade will not repair a retrieval process that keeps selecting an obsolete policy.
## Keep Facts, Voice, Rules, and Method Separate
Not everything supplied to a model serves the same purpose.
Facts establish what may be claimed.
Voice establishes how the organization communicates.
Rules establish what is permitted.
Method establishes how the work should be performed.
The author's Dashboard reflects this separation. Its brand voice defines characteristics such as tone, key messages, and phrases to avoid. Its project material supplies task-specific information.
These are not interchangeable.
A confident brand voice cannot authorize a confident factual claim.
A preferred message cannot establish that a capability exists.
An expert method cannot supply a missing price.
Keeping these elements explicit makes them reviewable. A manager can change the voice without changing the facts, update a policy without rewriting the method, or replace a source without altering the brief.
The common principle is that nothing important should depend solely on an invisible disposition inherited from the model's training.
Put it somewhere readable, owned, and open to correction.
## Spend the Verification Where It Matters
Rule 14b says:
Spend the verification where it matters.
Not every output deserves the same checking effort.
An internal draft may need ordinary editorial review. A statement of contractual compliance may require direct comparison with the requirement and supporting evidence.
The difference is consequence.
The organization should decide which claims require closer checking before those claims appear in a polished answer.
Otherwise, fluency can conceal the point at which a low-risk drafting task becomes a high-risk commitment.
Retrieval supports proportionate verification by making the evidence available. It does not remove the need to decide how much checking the action warrants.
Include that effort in the project budget.
The cost of the system is not only the model call. It includes maintaining the sources and checking the results.
## Spend on Plumbing Before Brains
When an AI system disappoints, a more capable model is an easy purchase.
Improving sources is less glamorous.
It may require identifying authoritative records, removing duplicates, assigning owners, separating projects, and retiring stale material.
Yet those tasks may address the actual failure.
Before upgrading the model, ask:
Did it receive the correct, current source?
Did the source answer the question?
Could the answer be checked against it?
If the answer to any of those is no, model capability may not be the limiting factor.
Fix the information path first. Then test whether the model still needs upgrading.
That is how the contract from the previous chapter becomes useful in practice. The contract defines acceptable work. The plumbing supplies the evidence needed to meet it.
A dependable system needs both.
Date the knowledge. Approve the sources. Keep the receipt. Check in proportion to the consequence.
Then choose the model.
Spend on sources and plumbing before you spend on brains.

## Remember This

> Date the knowledge. Approve the sources. Keep the receipt. Check in proportion to
> the consequence.
>
> Then choose the model.
>
> Spend on sources and plumbing before you spend on brains.

---

## The rules this chapter carries

**Rule 1 — *It doesn't know things.* (primary).** "Retrieval Is How Facts Reach the
Work" is Rule 1 made operational: the model's training is not an approved source
for your current prices, permissions, project requirements, or commitments.

**Rule 12b — *Put an expiry date on knowledge.* (carried).** "Date the Knowledge":
a document can be genuine, approved, and no longer suitable; the system needs to
know whether it is still valid for the question being asked.

**Rule 12c — *Whitelist the sources.* (carried).** "Whitelist the Sources": a
document's availability is not the same as its authority; whitelisting makes the
distinction explicit.

**Rule 14b — *Spend the verification where it matters.* (carried).** "Spend the
Verification Where It Matters": not every output deserves the same checking effort;
the difference is consequence.

---

*Verification: the author's prose is adopted verbatim (2,011 words), with the
section headings converted from plain Title Case lines to `## ` markdown headings.
No external factual claims requiring a source: the "Same Model, Different Answer"
demo is framed by the author as an illustrative comparison, not a reported
performance test ("This is an illustrative comparison, not a reported performance
test") — the honest register. The Dashboard references ("The LLM is a communications
manager, not a knowledge source"; "never fill a gap with a guess"; "attribute every
specific claim"; brand voice with tone/key messages/phrases to avoid; project-scoped
document retrieval; session records of documents used) are the author's own system,
described from first-hand knowledge — testimony, presented as such. The chapter
quotes Rule 1, Rule 12b, Rule 12c, and Rule 14b by name — the book's own established
rules. The RAG mechanism (retrieval-augmented generation: the system finds relevant
material and supplies it before the model answers) is standard, well-documented
practice, and the chapter describes it accurately without asserting performance
figures. Placement: Chapter 15, Part II — closes the "system around the model" run
after Ch. 13 (where the model sits) and Ch. 14 (what guards its output). Carries
Rule 1 (primary), Rules 12b, 12c, 14b.*
