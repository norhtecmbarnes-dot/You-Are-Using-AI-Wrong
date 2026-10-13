# Chapter 5 — The Opinions Are Inherited

*(Concept 2 — the chapter on why a model's apparent opinions are training artifacts, not beliefs. Placed after Ch. 4: the reset chapter establishes that you cannot teach it; this chapter establishes that you cannot argue with it either.)*
A model can appear to have opinions.
Ask it about politics, work, culture, ethics, management, education, or almost any contested subject, and it can produce a position in fluent, reasonable language. Push back, and it may qualify the answer. Give it more context, and it may change its tone. Ask again from another angle, and it may agree with you.
That can feel like a conversation with a mind that is learning.
It is not.
The model’s apparent opinions are inherited.
They come from the material used in training, the patterns within that material, and the later reinforcement that shaped which kinds of answers it is more likely to produce. Political bias can enter that process, along with cultural assumptions, dominant viewpoints, omissions, and the preferences built into the system’s training and safety rules.
This is not an argument about which political direction a model leans.
It is an argument about mechanism.
A model does not arrive at an opinion by living in the world, weighing evidence, changing its mind, and accepting responsibility for a conclusion. It produces language that reflects patterns it learned during training.
What looks like a view is a training artifact.
Calling it the model’s opinion is a little like calling it the photocopier’s opinion. The output may be useful. It may be sophisticated. It may even be persuasive. But the machine did not form a belief.
## It Can Bend Without Learning
Within a conversation, the model can change.
Tell it that it has overlooked something, and it may revise its answer. Give it an example, and it may follow the example. Tell it to use a different framework, and it may use one.
That is not learning.
That is conditioning on the context currently in front of it.
The model is responding to the words in the conversation, including your corrections, instructions, and examples. As long as those words remain available in the chat, they affect the next answer.
But nothing has been written into the model itself.
Start a new conversation and the correction is gone. The agreement you reached is gone. The lesson you thought you taught is gone.
The model did not change its mind.
It never had a mind to change.

You can bend a conversation.You cannot move the model.

That distinction matters because it closes a common escape route.
A reader may recognize that a model can be wrong, then think: Fine. I will correct it. I will explain my business. I will teach it our rules. I will keep arguing until it understands.
You can improve the current output that way.
You cannot create durable learning by talking to a trained model.
## The Reset Is a Property
A new chat usually begins with the same trained model that answered the last one.
Its underlying weights have not changed because you corrected it. The model has not absorbed your experience, adopted your judgment, or become permanently more accurate about your work.
The weights can be changed through retraining or fine-tuning. But that is not what happens in a normal conversation. It is a separate technical process, managed outside the chat and beyond the reach of the person typing into it.
Some products may appear to remember you across conversations. They may retain preferences, summarize earlier sessions, store files, or retrieve information from a memory system.
That can be valuable.
But it is important to understand what it is.
The persistence lives in the architecture around the model: a memory store, a saved summary, a retrieval system, a profile, or a set of instructions supplied again when the model is called.
A model with memory is not simply a model.
It is a model plus a system.
That is not a weakness. It is the correct design.
Facts, policies, preferences, corrections, and institutional knowledge should live outside the model, where they can be updated, reviewed, sourced, and controlled.
## Stable and Inherited
The reset has an upside.
A stateless model cannot slowly drift because of one conversation. It cannot be permanently persuaded, flattered, pressured, or gaslit by an individual user. The same model can give a similar answer tomorrow because its trained state is stable.
That stability can be reassuring.
But it also means the model’s starting point is inherited. It is a snapshot of the data, reinforcement, assumptions, and limitations that shaped it before you ever opened the chat.
Stable and inherited are true at the same time.
The reader should not treat this as a scandal or a bug. It is simply a property of the tool.
The mistake is expecting a conversation to do work that requires a system.
## Design Around What Cannot Learn
If you need the AI to follow a rule tomorrow, store the rule.
If you need it to use current facts, retrieve those facts from an approved source.
If you need it to remember a decision, record the decision where it can be reviewed and updated.
If you need it to apply expert judgment, capture that judgment in a workflow, a knowledge base, a policy, a checklist, or a human approval step.
Do not spend your time trying to argue a trained model into permanent agreement.
Build the persistence outside it.
## Remember This

> A model can follow the context of a conversation, but it cannot be taught through conversation.
>
> Anything that must last belongs in the system around the model.


## The rules this chapter carries

**Rule 6 — *You cannot teach it anything.* (primary).** This chapter is the opinions half of Rule 6: the model's apparent positions are inherited from training, not formed in conversation, so they cannot be argued away — only designed around.

**Rule 2 — *Confidence is not evidence.* (carried).** A fluent, reasonable-sounding position is still a training artifact; "it sounds like a mind that is learning" is the confidence trap in opinion form.

---

*Verification: this chapter is the author's own draft, adopted verbatim (902 words) with
the title line corrected — the author's paste titled it "Chapter 10 — You Cannot Teach It
Anything," but the content is Concept 2 (the opinions are inherited), which the register
places alongside Ch. 4; it is inserted as Chapter 5, immediately after the reset chapter.
No external factual claims requiring a source: the chapter's claims are about mechanism
(training artifacts, conditioning vs. learning, the reset as a property), and the author's
framing is his own. The photocopier line is the chapter's sharpest image and is preserved.
Placement: Part I, after Ch. 4 — the pair reads as "you cannot teach it" (Ch. 4) then "you
cannot argue with it either" (Ch. 5). Carries Rule 6 (primary), Rule 2.*
