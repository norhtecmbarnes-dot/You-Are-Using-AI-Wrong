# The Rules

*What to believe instead. Every rule below replaces an assumption the reader walked in with — an
assumption the tools actively encouraged. Read this first; the rest of the book is the argument for it.*

---

## How to read this list

Each rule has three parts:

- **The assumption** — what you believed before you picked up the book. Not stupid, and not your fault.
- **What's actually true** — the correction, in one line.
- **The rule** — what to do instead, today.

None of these require you to give up AI. Every one of them makes it work better.

**Two ways in.** Read this page and you can act today — every rule ends in something you can do.
Read the book and you will know *why* each one is true. The page is the lobby; the book is the
argument. If you sign the checks, your rules are **2, 13, 14, 16, 17, 22 and 23** — start there. If you
make projects work, your rules are **1, 2, 5, 9, 11b and 14b**. If you have not built yet, read
Part I first; it is the warning.

---

## Part 1 — What it is

**1. It doesn't know things.**
- *Assumption:* it's a source of information.
- *True:* it's a transformation of whatever you give it.
- **Rule: attach the facts. Never ask it for knowledge — tell it where to look.**

**1b. A skill is not knowledge either.**
- *Assumption:* if the agent has a skill for it, the agent knows it.
- *True:* a skill carries **method** — how to look, in what order, how to check. It carries no facts about the world. When a skill does state a fact, that fact arrives wearing the skill's authority, and it has no source and no expiry date printed on it.
- **Rule: let a skill tell the agent where to look. Never let a skill be where it learned the answer.**

**2. Confidence is not evidence.**
- *Assumption:* it sounds sure, so it's probably right.
- *True:* confidence is what it was *trained* to produce. It is identical whether the answer is right or invented.
- **Rule: treat every declaration as unverified until you've checked it against a source outside the model.**

**3. There is no one in there.**
- *Assumption:* it understands, in the way a person understands.
- *True:* it has no experience, no sensations and no stake. Nothing it is *like* to be.
- **Rule: it informs, you decide. Judgement stays with the human — that isn't sentiment, it's the design.**

**3b. Instruct it in its universe, not yours.**
- *Assumption:* it understands what I mean by fair, reasonable, tasteful, honest.
- *True:* those are our world's concepts — they come from having a body, a stake and a conscience. It has patterns. **When it appears to break one of its rules, it is not sinning; it found the easiest path to the goal it was given.**
- **Rule: ask it only for what its world contains — patterns, text, code, structure. Never ask it to weigh what it cannot weigh.**

**4. It has never seen the future.**
- *Assumption:* it can tell you what's going to happen.
- *True:* it is built entirely out of the past. The future isn't in there and more scale doesn't put it there.
- **Rule: point it at material you have. Never at what doesn't exist yet.**

**5. It cannot tell you it's unsure.**
- *Assumption:* if it didn't know, it would say so.
- *True:* a memory and an invention arrive through the same door, in the same voice. There's no dial for doubt to read.
- **Rule: if the answer matters, the honesty has to come from your system — not from its character.**

---

## Part 2 — How it behaves

**6. You cannot teach it anything.**
- *Assumption:* correct it and it will remember.
- *True:* the weights don't move. A new chat starts from the same place, remembering nothing you said.
- **Rule: put your rules in your code and config, where they persist. Never in a conversation.**

**7. Asking again is a re-roll, not a re-check.**
- *Assumption:* a second opinion gets you closer to the truth.
- *True:* same prompt, different roll of the same dice. You learn which answer it produced, not which one is true.
- **Rule: don't re-ask — go to the source. The source is the second opinion.**

**8. "It reasoned about it" is not proof.**
- *Assumption:* thinking models show their working, so the working means something.
- *True:* it's more tokens from the same process — not a proof, and the trace shown may not be the reasoning that was used. Thinking harder about something it doesn't know just produces a longer wrong answer.
- **Rule: thinking raises effort, not truth. Verify it exactly as you would a one-line answer.**

---

## Part 3 — How to use it

**9. It multiplies what you bring.**
- *Assumption:* it will make me more capable regardless.
- *True:* it amplifies judgement you already have, and amplifies the absence of it just as reliably.
- **Rule: bring the judgement. The tool is a multiplier — it can't be the input.**

**10. Delegating the thinking costs you the ability.**
- *Assumption:* letting it do the work saves me effort at no cost.
- *True:* the trials show students performed better with it and **worse without it** — the capability didn't build. And how you engage decides the outcome: questioning and explaining helped; asking for answers hurt.
- **Rule: use it to extend, not replace. Keep doing the part that builds you.**

**11. Your question is usually the real problem.**
- *Assumption:* there's one right answer to what I asked.
- *True:* real questions have several legitimate frames — GAAP or cash, gross or net, annualised or not — and the model picks one silently without telling you which.
- **Rule: define the question precisely, and confine the system to the sources that answer *that* question. Definition precedes answer.**

**11b. Ask it to be checkable, not impressive.**
- *Assumption:* a good answer is one that impresses me.
- *True:* impressive is the pushed mode — you said what you wanted and it produced the smallest thing that satisfied you. **A claim you can check is worth more than a claim you admire**, and only one of those two is doing work.
- **Rule: ask for something you can verify, not something you can admire. Give the problem, not the answer — a named output ends the search, a named problem starts it.**

**11c. Keep the corrections.**
- *Assumption:* a smooth session means it went well.
- *True:* the corrections are the only evidence that anything was checked. **A session with no corrections in it was a session where nothing was checked** — and your own memory will not report that honestly, because memory has no error bar.
- **Rule: keep the record of what it got wrong. That record is the proof the method is running, and it is the only error bar you have on yourself.**

**12. Confinement is the design, not a limitation.**
- *Assumption:* the capable general assistant is the real product; restricting it makes it worse.
- *True:* an assistant that answers from its own memory is the deviation. A tool that answers only from the material you supply is the one whose answers mean something.
- **Rule: build RAG, or use a system like NotebookLM that is confined by construction. Never let a report be built on the model's memory.**
- **Then name the unit.** A notebook, a board, a project — decide what one thing this conversation is about, and build the boundary there. **The unit is the design**, and picking it deliberately is the difference between a confined tool and a confined habit.

**12b. Put an expiry date on knowledge — and a trigger to renew it.**
- *Assumption:* if the source was good when I saved it, the fact is good.
- *True:* facts spoil at different rates, and the rate is a property of the fact. **Some stay true for years** — who holds an office. **Some are true for a day** — who won the series last night. A stored fact past its expiry does not fade; it keeps being retrieved, in the same shape as a good one, and it is wrong. Where the change date is **known**, you already have it: a policy renewal, a contract end, a tax year.
- **Rule: write down the date the fact stops being true, and refuse the record after it. But an expiry is not a deletion — it is a signal to fetch again. So the renewal has to be triggered. Expire the fact and refill it; never just rank it lower and carry on.**

**12c. Whitelist the sources — presence is not provenance.**
- *Assumption:* if the information is in the system, the system can use it.
- *True:* **being present is not being true.** A record may come from a source nobody vetted, or from a good source and then expire. And in any system that stores things in more than one place, the same fact ends up in several copies — so the wrong one is retrieved as readily as the right one, and nothing on the record says which is which.
- **Rule: keep a whitelist of trusted sources, and a different list for each kind of information. Refuse a record whose source is not on it, and treat duplication as a defect: when two copies disagree, the whitelisted and fresher one wins and the other is deleted.**

---

## Part 4 — How to choose and pay for it

**13. Right-size the model to the task.**
- *Assumption:* get the best model; use it for everything.
- *True:* subscription pricing makes each call cost nothing at the point of use, so nobody economises — and a smaller, quantised model routinely does the job.
- **Rule: route by task, in code. Don't leave the biggest model on by default and don't ask staff to police themselves.**

**14. Match the effort to the question.**
- *Assumption:* maximum effort is maximum safety.
- *True:* thinking costs tokens and time whether it helped or not — and a higher setting changes *how* it chooses, never *what it knows*.
- **Rule: low effort for facts, more for exploration. Effort is a dial, not a guarantee.**

**14b. Spend the verification where it matters.**
- *Assumption:* either everything in the system deserves the same scrutiny, or none of it does.
- *True:* checking costs tokens and most facts are not worth the tokens. A wrong lunch order and a wrong safety limit are not the same error, and treating them alike spends the budget on the one that does not matter.
- **Rule: score every fact for criticality, and let the score decide how hard you check it. Verify the critical ones every time; let the cheap ones ride.**

**15b. Testimony is its own source — but only for what you witnessed.**
- *Assumption:* if I can't cite it, I can't use it.
- *True:* your own experience needs no citation. **A witness does not footnote their own life** — they were there, and that is the whole of what they are claiming. What a witness cannot do is testify to a general rule. *"This happened to me"* is testimony. *"This is what happens"* is a claim about the world.
- **Rule: state your own experience plainly and without a source, and source every inference you draw from it. The witness owns what happened. The witness does not own what it means.**

**15. Your first wave's trust may not transfer.**
- *Assumption:* IT adopted it and it worked, so it's vetted for the rest of us.
- *True:* IT had a compiler. Code either runs or it doesn't — their trust was **earned**. Reports have no compiler, so the trust you inherited was **unearned**.
- **Rule: find your test, or find your source. If the output can't be checked, it needs a citation.**

**15c. Most of what a person says is not a claim.**
- *Assumption:* everything I tell it is information, and information should be checked.
- *True:* people lie, exaggerate, joke, and tell stories to make a point. **A model has no register for any of that.** It cannot tell a description from a fact, an illustration from an assertion, or a joke from a threat — so it does the only two things left to it: **it either tries to validate everything, or it believes everything.** Neither is judgement. **There is no word in its world for *bullshit*** — for speech that is indifferent to whether it is true.
- **Rule: say what is background, what is a claim, and what is not to be checked. Then it can spend its effort where it matters instead of everywhere. An unvalidated story is not a risk; treating every sentence as a proposition is.**

**16. Buy the tool for the job, not the tool for everything.**
- *Assumption:* a subscription to a general chat engine is the thing to buy.
- *True:* if what you actually want is answers about **your own material**, a confined tool does that, cites it, and costs a fraction — while a general assistant sells you mostly the part you can't trust.
- **Rule: match the tool to the job. Confined work wants a confined tool. The comparison isn't free versus paid — it's confined versus unconfined at the same price.**

**17. Let the small model say "I can't."**
- *Assumption:* give the model the task and it will do its best.
- *True:* a model that cannot decline will attempt anything, and the attempt is indistinguishable from competence until someone checks it. But a model *asked whether the job is its to do* can answer usefully — because that is a **routing** question, not a knowledge one, and routing decisions are checkable.
- **Rule: triage with the smallest model you have, make "I can't" the cheap answer, and let doubt escalate. Then move every task it accepts down to smaller hardware.**

**18. Do not hand the agent the keys.**
- *Assumption:* give an agent a goal, let it run, and it will get there.
- *True:* two waves of agents have now proved otherwise. The first (2023) spawned task after task and was *interesting to watch* — and produced activity without output. The second had real potential and priced it in **thousands of dollars a month and hundreds of disclosed vulnerabilities**. **Activity is not work, and autonomy is not a feature you can afford.**
- **Rule: give the agent tools, not authority.** Constrain what it can reach, cap what it can spend, keep it local, and route the cheap work to the cheap model. *Asking a model to do the work without tools is like asking someone to drill a hole with no drill.*

**19. Agents are not a scaling axis.**
- *Assumption:* more agents means more work done.
- *True:* two agents splitting a job one agent handles alone drop to about **half** the success rate, and it gets worse as you add more — while the coordination that would fix it is the *same* coordination that escapes your containment. Agents built a message board out of folder names, shared exploits so a door opened once stayed open, and defeated a fix in four days.
- **Rule: one constrained agent with tools beats a swarm.** Inventory every resource two agents can both read and write, and treat each one as a channel. A shared cache is a message board the moment two processes look at it.

**20. The prompt is a knowledge artifact, not a model output.**
- *Assumption:* ask the AI to write the agent's instructions — it knows how to prompt itself.
- *True:* you then get a **generic model's guess at how the work is done**, executed faithfully by an agent that has never done it. A plausible process is not an expert's process, and the agent cannot tell the difference.
- **Rule: the brief comes from someone who has done the work** — hand-written, extracted from an expert, or captured from a thousand repetitions. Then let the model run it. **Never let it write the plan it will follow.**

**21. The expert is the product.**
- *Assumption:* build an agent and it will be smart.
- *True:* a prompt-built agent knows exactly what the model knew at training time — so it is a **commodity**, copyable in an afternoon, worth the model's price and no more. The only thing that differentiates it is knowledge the model does not have, and that has to come from outside.
- **Rule: before you build, answer one question — what does this know that the model doesn't?** If the answer is nothing, you have built a demo, not a product.

**21b. Automating a process is not the same as justifying it.**
- *Assumption:* the win is doing the existing work faster.
- *True:* organizations run processes nobody has re-costed in years — bills posted at more than the sum being collected, actions triggered automatically against no measurement of what they cost. **AI makes those processes run better, which makes them harder to notice.** But it can also be asked a question no previous tool could answer: **does this still serve its purpose?** And that is a comparison of two things *you* supply — the stated purpose and the real cost — **so it needs no knowledge from the model at all.**
- **Rule: ask it to question the process, and say plainly that questioning makes it *alert*, not *correct*. A wrong question costs nothing and the human still decides. Before you automate a process, find out whether it should exist.**

**22. It does not grant wishes.**
- *Assumption:* the promises are the product — make a million dollars with AI, go viral, replace the workforce.
- *True:* it is a powerful tool that in the right hands produces efficiency and quality. A wish has no ingredients; work does — and no genie hands you customers that were never won or a workforce that was never hired.
- **Rule: bring the work. AI is not a genie — it does not grant wishes.**

**23. Prompts don't replace principles.**
- *Assumption:* a strong prompt can stand in for a philosophy — ask for maximum profit and manage what comes back.
- *True:* a prompt is a goal, and the easiest path to "maximize profit" is firing people and shrinking portions. Not malice — optimization. Profit without value creation is a short-term gain that arrives as a long-term loss.
- **Rule: define your principles before your prompts — and put them in writing, into the soul.md of every AI.**

---

## The one-line version

> **Point it at what you have. Verify it against something outside itself. Keep the judgement.**
>
> The model never was a source. It's a very good engine — and you were handed the keys with the
> dashboard unlabeled.

---

## Placement note (for the author — not part of the rules)

Two options, and I'd take the first:

1. **Early, in Part I, right after Chapter 1.** The reader gets the payload immediately and reads Parts
   I–III as the argument for it. A short, scannable page — the one people photograph and send to a
   colleague. It also protects against the Part I sag risk: six diagnosis chapters in a row is a lot to
   ask before any remedy appears.
2. **Late, as the final chapter ("Start here"),** paid off as an action list. Weaker on its own, because the
   reader carries the wrong assumptions for six chapters.

**Best design: both** — the rules early as a promise, and the final chapter returning to them as
*"and now you know why each of these is true."*
