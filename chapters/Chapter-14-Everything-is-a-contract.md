# Chapter 14 — Everything Is a Contract

*(Placed in Part II — The Model That Works. The boundary chapter: the model
proposes, the system checks, the organization retains authority. The invoice
demo (the unauthorized "Approved for payment") is the chapter's spine.)*

---

Imagine asking an assistant to read an invoice and tell you two things: the invoice number and the amount owed.

The assistant returns both. Then it adds a third:

> "Approved for payment."

It looks helpful. It may even look efficient. Someone has saved you a step.

But you did not ask the assistant to approve the invoice. You asked it to read one.

That extra sentence changes the nature of the work. What began as information has become permission.

If your organization acts on it, the assistant has crossed a boundary that nobody authorized.

This is the problem a contract prevents.

A contract, in this chapter, is not a legal document. It is a clear agreement about what a tool may do, what it must return, and what must happen before anyone acts on the result.

The model can offer an answer. It cannot decide that the answer deserves to be used.

The boundary is where trust is decided.

## An Answer Is a Proposal

We are accustomed to treating a completed answer as completed work.

Someone asks a question. Someone else answers it. The conversation moves forward.

AI makes that habit risky because an answer can look finished before the work has been checked.

The language is fluent. The details fit together. There may be headings, explanations, and a confident conclusion. Nothing in the presentation tells you whether the model followed the assignment, used the right material, or added something it had no authority to add.

That is why the answer must remain a proposal until it passes the checks appropriate to the job.

For an invoice, the question may be whether the amount matches the original document.

For a policy question, it may be whether the answer comes from the current, approved policy.

For an action, it may be whether the person requesting it has permission.

These are different checks. None can be replaced by asking the model, "Are you sure?"

The model's confidence does not settle the matter. Rule 2 still applies:

> Confidence is not evidence.

## Agree on the Work Before It Begins

A manager does not need to write software to understand this boundary.

You already use it when delegating work.

"Review these applications and recommend three candidates" is not the same assignment as "Hire three people."

"Prepare a purchase recommendation" is not permission to place an order.

"Summarize the customer's complaint" is not permission to promise a refund.

The distinction is familiar. AI does not remove it.

Before using a model, define what the assignment includes and what it excludes.

What information may it use? What must it produce? What is it not allowed to decide? Who or what checks the result? What happens if the required information is missing?

Those questions are the contract.

They should be answered before the model begins, not after an impressive response makes everyone reluctant to slow down.

A useful contract is specific enough that another person can tell whether the job was done.

"Give us a good answer" is not specific.

"Answer from the current policy, identify the supporting passage, and report when the policy does not answer the question" is much clearer.

The second assignment leaves less room for a plausible invention to pass as completed work.

## Helpful Is Not the Same as Authorized

The most dangerous addition may be the one that sounds reasonable.

An invoice can be approved. A customer can receive a refund. An employee can be granted access.

So an extra recommendation or decision may not look strange. It may look like initiative.

But initiative is not authority.

The invoice example matters because the added approval is not obviously absurd. It belongs to the surrounding business process. That makes it easy to overlook.

A dependable system does not ask whether the addition sounds sensible. It asks whether the addition was permitted.

If the task was extraction, approval is outside the task.

If the task was recommendation, execution is outside the task.

If the task was drafting, publication is outside the task.

These boundaries protect the organization from a gradual expansion of responsibility that nobody explicitly agreed to.

The tool can be capable and still be operating outside its assignment.

## A Well-Presented Answer Can Still Be Wrong

There are two questions to keep separate:

Did the model return the kind of answer we requested?

And is the answer supported well enough for us to use it?

An invoice response can contain exactly the requested information and still contain the wrong amount.

A policy answer can follow the requested format and still quote an obsolete policy.

A report can be complete, concise, and beautifully organized while resting on an unsupported claim.

Checking the shape of the answer is necessary, but it is not enough.

The information must also be checked against something outside the model.

For a manager, the important question is not, "Does this look professional?"

It is:

> "What establishes that this result is acceptable for the decision we are about to make?"

The answer should identify a source, a comparison, an authorization, or another appropriate check.

If the only explanation is that the model said so, the boundary has not been established.

## Do Not Quietly Fix a Failed Answer

When an answer almost meets the requirements, it is tempting to tidy it up and move on.

Remove the extra approval. Fill in the missing detail. Interpret the unclear phrase. Treat the omission as harmless.

Sometimes the repair takes only a moment.

But the repair can hide a more important failure.

Why did the model add an approval? Did it misunderstand the task? Why was the amount missing? Was the source incomplete, or did the model fail to find it?

If the organization quietly fixes every answer, the workflow can appear dependable while relying on constant human rescue.

The cost disappears into someone's working day.

Rejecting a response does not mean abandoning the project. It means refusing to treat failed work as accepted work.

The next step may be another attempt, a different model, or human review. Whatever the route, the requirements remain the same.

A failure should not lower the standard.

That is the practical meaning of:

> Reject rather than repair.

Keep the failure visible. Find out what happened. Require a result that meets the contract before proceeding.

## A Reminder Is Not a Control

Suppose the model adds an unauthorized approval and you reply:

> "Never do that again."

That may help with the next response. It does not establish a dependable organizational control.

A reminder in a conversation is not the same as a rule enforced by the system.

This is the practical point of Rule 6:

> You cannot teach it anything.

For this chapter, the issue is not whether a model can follow a correction. It is whether your organization can depend on that correction remaining effective.

A rule that matters must persist outside the conversation.

The system must refuse an unauthorized action even when the model proposes it confidently. It must stop when required information is absent, even when the model offers a plausible substitute.

The manager's responsibility is not to inspect the technical details of every check. It is to require those checks and make sure they have consequences.

Ask the builder:

> "What happens when the tool does not follow the assignment?"

"Someone notices" is not a strong enough answer for an unattended workflow.

## Confinement Gives the Tool a Clear Job

Rule 12 says:

> Confinement is the design, not a limitation.

A confined tool answers only from the material you provide.

But the boundary does not end with the source material. It also includes what the tool may return and what anyone may do with that return.

A tool may read approved invoices without being allowed to approve payments.

It may summarize personnel records without being allowed to grant access.

It may draft a message without being allowed to send it.

These limits do not make the tool less useful. They make its responsibility clearer.

Broad capability is valuable when the work needs it. Narrow authority is valuable when the consequences require it.

The two can exist together.

## "I Can Handle This" Is Also a Proposal

The author's model-routing service asks a smaller model whether it can handle a task or whether the work should go to a more capable model.

It encourages the smaller model to decline when unsure.

That can be useful. It can help direct work toward less expensive resources without asking every user to make the choice manually.

But it does not mean the model knows its limits.

"I can handle this" is a routing proposal, not a guarantee.

The accepted work still has to pass the checks appropriate to the task.

This separates two decisions that are often confused:

Which model should try?

And did the result meet our requirements?

A smaller model may be a sensible first choice. A more capable model may be necessary for difficult work. Neither gets to certify its own answer merely by accepting the assignment.

The contract stays in place whichever model is used.

## Do Not Let the Tool Write Its Own Job Description

There is another boundary managers should protect: the method.

An experienced professional brings more than facts to a task. They bring a way of working.

They know what to examine first, which exceptions matter, when to seek approval, and when to stop.

That experience should guide the agent's instructions.

If you ask the model to invent its own operating method, then follow it, you have allowed the tool to define the job by which it will be judged.

The result may sound expert without reflecting an expert's actual practice.

Models can help draft instructions. They can organize an expert's notes or suggest improvements for review.

But the governing brief must remain under human authority.

The model should execute an approved method, not quietly replace it with a plausible one.

## Completing Something Is Not Completing the Assignment

The author encountered this distinction when purchasing AI book-writing tools.

Some attempted to generate their own plan rather than execute the supplied brief.

They could produce a book-shaped result. That was not necessarily the requested book.

The same failure can happen anywhere.

A detailed report is not necessarily the report you commissioned. A polished recommendation is not necessarily based on the sources you approved. A completed workflow is not necessarily an authorized workflow.

Output is not success merely because something was produced.

Success means the agreed work was completed under the agreed conditions.

That is what the contract preserves.

## The Manager's Boundary

You do not need to become a programmer to insist on a dependable boundary.

You need to make acceptance part of the project, rather than an assumption at the end.

Before approving deployment, ask what the tool is allowed to do, how its result will be checked, and what happens when it fails.

Then ask the team to demonstrate a failure—not just a success.

Show the extra approval. Show the missing source. Show the answer that looks right but cannot be supported.

A working boundary stops those results from becoming actions.

That is the point of the contract.

The model proposes. The system checks. The organization retains authority.

## Remember This

> Define the work before you call.
>
> Check the result before you act.
>
> Reject rather than repair.

The tool does not earn trust by sounding certain.

It earns a place in the workflow by meeting requirements it did not write and cannot waive.

---

## The rules this chapter carries

**Rule 6 — *You cannot teach it anything.* (primary).** "A Reminder Is Not a Control"
is Rule 6 at the organizational level: a correction in conversation does not persist,
so a rule that matters must be enforced by the system, not remembered by the model.

**Rule 12 — *Confinement is the design, not a limitation.* (carried).** "Confinement
Gives the Tool a Clear Job" — the boundary includes not just the source material but
what the tool may return and what anyone may do with that return.

**Rule 2 — *Confidence is not evidence.* (carried).** "An Answer Is a Proposal" —
the model's confidence does not settle whether the answer followed the assignment
or is supported; none of the checks can be replaced by "Are you sure?"

**Rule 11 — *Your question is usually the real problem.* (carried).** "Agree on the
Work Before It Begins" — the contract is the sharpened question: define what the
assignment includes and excludes before the model begins.

---

*Verification: the author's prose is adopted verbatim (1,904 words). No external
factual claims requiring a source: the invoice demo is a constructed illustration
(the unauthorized "Approved for payment" is a hypothetical, not a recorded incident),
the delegation examples ("Review these applications…" vs. "Hire three people") are
common workplace distinctions, and the author's book-writing-tools experience
("Some attempted to generate their own plan rather than execute the supplied brief")
is testimony about his own purchasing, presented as such. The chapter references its
own prior work: the model-routing service ("I Can Handle This" Is Also a Proposal)
is the capability bus verified in `model-bus.ts` (699 lines) — the fail-safe
*"If you're unsure, lean toward canHandle: false"* is confirmed at line 361, and the
routing-proposal-not-guarantee framing matches the code's design (the self-assessment
is bounded, not trusted). The chapter also quotes Rule 2, Rule 6, and Rule 12 by name,
which are the book's own established rules. Placement: Chapter 14, Part II — between
Ch. 13 (Language at the edges, code in the middle) and Ch. 15 (Your plumbing is your
ceiling). The sequence is: where the model sits (13) → what guards its output (14) →
what feeds it (15). Carries Rule 6 (primary), Rules 12, 2, 11.*
