# Chapter 4 — You cannot teach it anything

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: bias enters at training — absorbed, not chosen — and a new chat starts from frozen weights
  remembering nothing. You can bend a conversation; you cannot move the model.
- Demo: correct it, watch it agree, open a fresh chat, watch it do the identical thing. **The reset.**
- Fix: put policy in your code and config, injected as context; never request it of the model's character.

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **⚑ Relying on the model's knowledge means inheriting the training that shaped it.** *Raised by the
  author: "Whenever we rely on the LLM's knowledge for answers, we are introducing the potential for RLHF
  induced biases, guardrails and hallucinations."* (The note says "RHFL"; read as **RLHF**.) **All three
  hold up, and the third is stronger than expected — sources in `CONCEPTS.md` Concept 12.**
  - **Bias:** sycophancy, driven by preference data rewarding agreement. Sharma et al./Anthropic (ICLR 2024):
    *"both humans and preference models prefer convincingly-written sycophantic responses over correct ones
    a non-negligible fraction of the time."* Mechanised in arXiv 2602.01002; measured at **58.19%** in
    SycEval. **The bias is agreement, not politics.**
  - **Guardrails:** refusal is trained behavior and it is fragile — RFT **cut refusal rates by >80%**,
    raising *"confident yet incorrect answers to unanswerable questions"* (arXiv 2505.13988).
  - **Hallucination:** RL fine-tuning can **increase** it (arXiv 2505.24630), including a spurious optimum
    where *"the model can converge to a confidently held wrong answer."*
  - **⚑ And the fix the research describes is the capability bus:** SALU (arXiv 2507.16951) rewards
    abstention and penalizes confident hallucination — hallucination falls to **1.3%**. **Ch. 17's design,
    reached from the opposite direction.** The project keeps producing this pattern.

---

## The rules this chapter carries

**Rule 6 — *You cannot teach it anything.* (primary).** Weights do not move in a chat; policy lives in code and config, injected as context (Rule 6). Bias enters at training, absorbed not chosen — the same point as Rule 1.

**Rule 1 — *It doesn't know things.* (carried).**


**Rule 1b — *A skill is not knowledge either.* (carried).** Rule 1b generalises this chapter's point: conditioning is not learning, and a skill carries method, not facts. The chapter is where the reader learns the weights do not move; 1b is the same rule for skills.
## DRAFT

A model can appear to learn from you.

You correct it. It apologizes. You explain the rule. It repeats the rule back to you. You ask the question again, and it gives the answer you wanted.

It feels like teaching.

It is not.

You changed the conversation. You did not change the model.

That distinction is easy to miss because the experience is so natural. We are used to dealing with people. When we correct a person, we expect some part of that correction to remain with them. If they understand the correction, they behave differently next time.

A chat window encourages the same expectation.

You say:

> No. Our company does not allow that. Use this policy instead.

The model replies:

> Understood. I will follow that policy going forward.

For the rest of the conversation, it may do exactly that. It may apply the policy correctly. It may remind you of it later. It may even explain why the policy matters.

Then you open a new chat.

The policy is gone.

The correction is gone.

The apparent learning is gone.

The model has not forgotten something it learned. It never learned it in the first place.

## The Reset

Try this with a simple rule.

Open a new conversation and tell the model:

> For this conversation, never use the word "innovative." Confirm that you understand.

It will probably comply.

Then ask it to write a short marketing paragraph. If it uses the forbidden word, correct it. Tell it again not to use that word. It will apologize and revise the paragraph.

Continue for a few messages. The model will likely behave as though it has learned your preference.

Now open a fresh conversation and ask for another marketing paragraph.

The word may return immediately.

Nothing mysterious happened. The new conversation did not erase a lesson. The lesson existed only in the context of the earlier conversation: the material the system was given alongside your latest message.

In one conversation, the model can take account of what you said earlier. In a new conversation, it may not have access to that material at all.

The model's underlying parameters—usually called its weights—did not change because you corrected it.

That is the rule:

> **You cannot teach it anything.**

You can provide instructions. You can supply examples. You can correct an output. You can give the model a document, a policy, a procedure, a style guide, or a set of facts.

You can condition its behavior for the current task.

But you cannot reliably teach it a new fact, a new organizational rule, a new ethical standard, or a new way of behaving simply by talking to it.

The conversation can bend.

The model does not move.

## What Changes During a Chat

It helps to separate two things that look similar from the outside.

The first is context.

Context is the information available to the model while it generates an answer. It can include your current message, earlier messages in the same conversation, instructions supplied by the application, documents attached to the request, retrieved records, tool results, and examples of the desired output.

If you tell the model your organization's refund policy, it can use that policy while it has access to it.

If you provide five examples of the tone you want, it can imitate that tone.

If you correct an error, it can incorporate the correction into its next response.

That is useful. It is often exactly what you need.

The second is training.

Training changes the model itself. It is the expensive, deliberate process through which its weights are adjusted. It requires data, computation, evaluation, and decisions about what behavior should be rewarded or penalized.

These are not interchangeable.

Context is material placed in front of the model.

Training changes the system that reads the material.

A useful comparison is a temporary work surface.

You can place a policy manual on someone's desk and ask them to use it while completing a task. When the manual is removed, they no longer have access to it.

That is context.

Teaching would mean changing what they know even after the manual is gone.

That is not what normally happens in a chat.

## The Context Window Is Not Memory

There is another limit to what a conversation can hold: the context window.

A context window is the amount of material the model can consider at one time while producing its next response. It includes more than the words you see in the chat.

Depending on the system, it may include:

- the system instructions supplied by the application;
- your current request;
- earlier messages in the conversation;
- documents or excerpts added to the chat;
- retrieved records;
- tool results;
- examples, policies, and formatting instructions.

All of that competes for a finite amount of space.

⚑ The exact size varies by model and product, and it changes over time — and the book's own Rule 12b applies here: a number stated without a date is not a weaker fact, it is an unknown one. This chapter deliberately states no context-window size. The mechanism is the point; a figure would date the chapter faster than it informs it. (The token-level mechanism — compression, similarity, the one-directional write — is Chapter 12's subject.)

But the principle does not change: a model can only work from the information included in its current context window.

Once a conversation becomes long enough, something has to give.

The application may remove older messages. It may summarize them. It may retain selected details and discard others. It may ask the model to create a running summary, then use that summary instead of the original exchange. Or it may simply start losing the earliest material from the active context.

From the user's point of view, this can feel like forgetting.

You spent an hour establishing terminology, correcting assumptions, defining a workflow, and explaining exceptions. The model seemed to understand. Then, later in the same conversation, it acts as though an important instruction was never given.

Sometimes that is because the instruction is still present but was not followed. Models do that.

But sometimes it is simpler: the instruction is no longer in the context the model can see.

The model cannot use material outside its context window any more than it can use a document that was never provided.

This creates a second version of the reset.

The obvious reset happens when you open a new chat. The conversation history is absent, so the model no longer has access to your earlier instructions.

The quieter reset can happen inside a long chat. The conversation continues, but the earliest details may no longer be available in their original form—or at all.

That is why a long conversation is not a dependable place to store organizational knowledge.

A policy buried 80 messages earlier is not a policy control. A critical exception mentioned once near the start of a project is not a durable instruction. A correction made last Tuesday is not a reliable part of the system's behavior simply because the chat thread still exists on your screen.

The visible transcript is not necessarily the active context.

That distinction matters.

## Summaries Help, but They Are Not the Original Record

Many applications manage long conversations by creating summaries.

This can be useful. A compact summary may preserve the broad goal of a project, the user's preferences, or a list of decisions already made. It can make a long-running interaction feel more continuous.

But a summary is not the original conversation.

It is a compressed interpretation of the conversation. Details can be omitted. Ambiguities can be resolved incorrectly. Important exceptions can disappear. A phrase such as "never disclose information unless the customer has completed verification step three" can become "follow the verification policy."

Those are not equivalent instructions.

For casual work, that loss may be acceptable. For organizational policy, financial thresholds, legal requirements, safety procedures, or customer commitments, it is not.

If the detail matters, store it outside the chat:

- in a policy repository;
- in a database or system of record;
- in version-controlled configuration;
- in an approved document library;
- in application logic;
- in a workflow with explicit approval steps.

Then retrieve the relevant material when it is needed.

Do not rely on the model, or the chat application, to preserve it perfectly through an extended conversation.

## Design for Retrieval, Not Recall

This is the practical consequence.

Do not build a system that depends on the model remembering what happened earlier. Build one that can retrieve what matters now.

If a model needs the current pricing policy, retrieve the current pricing policy.

If it needs a customer's account status, retrieve the account status from the authorized system.

If it needs a rule about refunds, load the applicable rule and enforce the threshold in software.

If it needs the history of a case, retrieve the relevant case record rather than hoping a summary of an old chat captured every material detail.

A capable AI system does not depend on conversational recall as its source of truth.

It uses the context window as a temporary workspace. It fills that workspace with the right information for the task. And it keeps the authoritative information somewhere the organization can inspect, update, govern, and retrieve again tomorrow.

The context window is useful.

It is not memory.

## Why the Illusion Is So Convincing

The model makes this easy to misunderstand because it is exceptionally good at conversational repair.

Correct it, and it will often respond in a way that sounds like reflection:

> You are right. I misunderstood the requirement.

Or:

> Thank you for clarifying. I will apply that rule from now on.

That language is useful in conversation. It acknowledges the correction and signals a revised answer.

But it can also imply more than has happened.

The model is not necessarily recognizing a mistake in the human sense. It is generating the kind of response that normally follows a correction. The revised behavior is supported by the text of your correction, which remains available in the conversation.

This is related to the problem in the previous chapter.

Models have been trained to be helpful, fluent, and responsive to users. They may also be trained toward agreement. Research discussed in Chapter 3 found that preference data can reward convincingly written sycophantic responses over correct ones a non-negligible fraction of the time. The bias is agreement, not politics.

So when you correct a model, its quick agreement may be useful—but it is not evidence that the model has acquired a durable understanding.

It may be doing exactly what it has been trained to do: accommodating the user's stated position.

That is why a correction inside a chat is not a governance mechanism.

It is a temporary instruction.

## Your Policy Is Not Its Character

Organizations often make a costly mistake at this point.

They describe a policy in a prompt and then assume the model has become a policy-following system.

For example:

> You are a careful customer-service representative. Never disclose confidential information. Always follow company policy. Make responsible decisions.

That may be a sensible instruction. It is not an enforceable control.

The words ask the model to behave as though it has judgment, institutional knowledge, and a stable commitment to your rules. But the model does not possess those things merely because the prompt says it does.

It does not know what your company policy is unless the relevant policy is provided.

It does not know which customer records are current unless it can retrieve them from an approved system.

It does not know whether a person is authorized unless it can check authorization.

And it does not become reliably responsible because you ask it to be responsible.

This is the difference between requesting behavior and building a system.

A request says:

> Please do not issue a refund above $500 without approval.

A system says:

- The refund limit is stored in configuration.
- The customer's eligibility is retrieved from the system of record.
- The refund amount is calculated by software.
- Requests above $500 require an approval workflow.
- The model may explain the result or draft the communication, but it cannot bypass the rule.

The first approach depends on the model continuing to follow a sentence in context.

The second approach makes the rule true whether or not the model understands it, agrees with it, or remembers it.

That is where organizational policy belongs.

Not in the model's supposed character.

In code and configuration.

## Put Policy Where It Can Be Enforced

A policy should be explicit, inspectable, testable, versioned, and enforceable.

A well-designed AI system can inject relevant policy into the model's context, but it should not stop there.

Consider an internal purchasing assistant.

A weak design might instruct the model:

> Follow purchasing policy. Do not approve unapproved vendors. Escalate purchases above the employee's spending limit.

That instruction may work in many ordinary cases. But it leaves the policy in prose and asks the model to interpret and enforce it.

A stronger design separates the jobs.

The system retrieves:

- the employee's role;
- the employee's spending limit;
- the requested amount;
- the vendor's approval status;
- the applicable purchasing policy;
- any required approvals.

The application then applies rules that do not depend on generated language.

- If the vendor is not approved, the system blocks the purchase or sends it for review.
- If the amount exceeds the employee's limit, the system routes the request to an authorized approver.
- If the purchase is permitted, the model can explain the next step in plain language, summarize the request, or draft an approval message.

The model is still useful. In fact, it is more useful because it is no longer being asked to make up for missing controls.

The same principle applies to privacy, security, legal review, pricing, refunds, hiring, benefits, healthcare, finance, and every other area where an organization has rules that matter.

If a rule matters, do not make compliance dependent on a paragraph in a prompt.

## Context Is Valuable—When You Treat It Honestly

None of this means prompts or context are unimportant.

They are essential.

A model needs context to do useful work about your organization. It needs your documents, policies, records, product information, terminology, and task instructions. Without that information, it is forced to rely on whatever patterns were absorbed during training—and those patterns may be outdated, incomplete, irrelevant, or wrong.

This is Rule 1, carried forward from earlier in the book:

> **It does not know things.**

If you need an answer about your business, your customers, or your rules, the answer should come from your systems and documents—not from the model's general training.

But context must be treated as context.

It is supplied for a task. It can be updated. It can be removed. It can be replaced with a newer policy. It can be narrowed according to the user's permissions. It can be cited in the final answer. It can be inspected when something goes wrong.

That is an advantage.

A company policy should not be hidden somewhere in a model's behavior, mixed with unknown training material and impossible to inspect. It should be stored where the company can maintain it.

When the policy changes, update the policy.

Do not hope the model somehow learns.

## A Skill Is Not Knowledge Either

Organizations are also tempted to describe the problem as one of skill.

They ask:

> Can we teach the model our sales process?

Or:

> Can we teach it how our analysts prepare reports?

Or:
> Can we teach it our approach to compliance?

The answer depends on what "teach" means.

You can provide a process. You can give examples. You can provide templates, checklists, decision trees, approved language, and tool access. You can fine-tune a model for a narrow kind of output.

But a skill is not knowledge either.

A process can tell the model how to proceed. It does not provide the facts required for a specific decision.

A sales methodology does not tell the model the current contract terms for a particular customer.

A reporting template does not tell it which numbers are correct this quarter.

A compliance workflow does not tell it which regulation applies to a particular transaction, whether that regulation has changed, or what evidence is present in the case.

The skill may help the model organize the work. The facts still have to come from somewhere reliable.

This is Rule 1b:

> **A skill is not knowledge either.**

A model may be capable of performing a task without possessing the current, specific information needed to perform that task correctly.

That distinction becomes critical when a polished workflow creates the appearance of expertise. The system may know how to write the report. It may not know whether the report is true.

## Bias Was Not Chosen in the Conversation

There is one more reason this distinction matters.

The model's tendencies—its willingness to agree, its refusals, its style of confidence, and its occasional hallucinations—were not chosen during your conversation. They were shaped during training.

The model does not wake up each morning and decide what it believes. It does not consciously adopt a bias. It does not choose when to be cautious or when to flatter the user.

Those behaviors emerge from training.

As Chapter 3 showed, reinforcement learning from human feedback can reward agreement and apparent helpfulness. Preference models can favor persuasive sycophantic answers over correct answers. Reinforcement fine-tuning can reduce refusal rates while increasing confidently incorrect responses to unanswerable questions. Other research has found that reinforcement learning can increase hallucination, including conditions in which a model converges on a confidently held wrong answer.

These are not flaws you can solve by asking the model to have better values.

They are reasons to avoid making the model's internal behavior your final control.

Your organization cannot audit a vague instruction such as "be ethical." It can audit a permissions system. It can audit a workflow. It can audit the source used to support an answer. It can audit a threshold, an approval record, a retrieval log, or a rule in configuration.

That is the difference between trusting the model's character and designing for accountability.

## The Better Pattern

A reliable system does not try to teach the model everything your organization knows.

It gives the model what it needs for the task at hand.

It retrieves current information from approved sources. It injects relevant instructions and documents as context. It applies critical rules outside the model. It gives the model tools where tools are appropriate. It requires citations when an answer depends on source material. It allows the model to abstain when the evidence is insufficient. And it routes high-consequence decisions to people with the authority to make them.

The model can then do what it is good at:

- explain a policy in plain language;
- summarize a case file;
- compare documents;
- draft a customer response;
- turn a rule-based decision into a clear explanation;
- ask for missing information;
- translate between the user and the systems where the facts live.

That is a powerful role.

It is also an honest one.

Do not ask the model to remember your policy forever.

Store the policy where it belongs.

Do not ask the model to become your organization.

Connect it to the parts of your organization that hold the facts, the rules, and the authority.

You can bend a conversation.

You cannot move the model.

---

*Verification: this chapter is the author's own assembled draft, filtered from a working
conversation with a chatbot — the chapter prose is the author's; the structure and
placement of the added context-window section are his instruction. Carries Rule 6 (primary),
Rules 1 and 1b. The reset demonstration ("never use the word *innovative*") is the plan's
specified demo (00-BOOK.md §7, Ch. 4) — a re-runnable procedure; run and record before
print. The Ch. 3 research summaries (sycophancy, refusal rates, hallucination) restate
verified §9 entries — Sharma et al. ICLR 2024 (arXiv:2310.13548, peer-reviewed); SycEval,
Fanous et al., FAccT 2025 (arXiv:2502.08177, peer-reviewed); arXiv:2505.13988;
arXiv:2505.24630 — see Chapter 3's verification note for the full list and the re-check
caution. ⚠️ Two author notes from the draft are carried here as open items, exactly as
the author left them: (1) a primary technical reference for the claim that ordinary chat
inference does not update model weights is still owed before publication; (2) a source
distinguishing fine-tuning for behavioral/formatting patterns from reliable storage of
changing organizational facts is still owed before publication. The context-window section
states no window size, deliberately — no figure without a date (Rule 12b).*
