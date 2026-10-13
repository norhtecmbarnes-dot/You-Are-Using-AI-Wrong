# Chapter 7 — Activity is not work

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

**Claim.** agents have been sold twice now as **autonomy**, and autonomy is the expensive, insecure way to get work done. A system that fires off tasks looks busy; a system that can reach anything costs more than the work is worth. **Neither wave failed for lack of intelligence. Both failed for lack of constraints.**

**Demonstration.** **wave one, 2023** — **AgentGPT and AutoGPT**, agents that spawned tasks from tasks, which the author watched because they were *interesting to watch*, and which died because *there was a lot of activity and very little achieved in terms of output*. **The community's own verdict agrees, almost in his words:** *"like doing stuff for you (tho it barely worked, if at all)"* — and what survived was not the autonomous agent but the *frameworks* (CrewAI, AutoGen, OpenDevin, Devika, MetaGPT). **The ambition was replaced by scaffolding.** **Wave two** — a real framework with real potential, priced in numbers that end the argument: a heavy user at **$3,600/month**, a magazine's day-long test at **$100+ in a single day**, and an overnight heartbeat costing **$18.75** to repeatedly ask whether it was daytime — alongside **138+ disclosed CVEs**, a critical RCE, and **341 malicious marketplace skills**. *No organization can accept that* — and thirty years in the industry is why the author didn't.

**Fix.** **give the agent tools, not authority.** Constrain what it can reach, cap what it can spend, keep it local, route the cheap work to the cheap model. The productivity was never in the autonomy — *"like asking someone to drill a hole with no drill."*

---

## Concept 8 — Do not hand the agent the keys

> This is the captured material this chapter expands. It is in `CONCEPTS.md`.

*The two waves of agents. This is the origin story of the whole project, and the rule is the plainest in
the book: activity is not work.*

**As stated by the author:** (verbatim — preserve the words; they carry intent)

> I want to ad another rule. that rule is over trusting and relying on agents. I want to start out by my
> firs t experience with agents were the first one that came out shortly afte rthe introduction of Chat
> GPT. I thinkn one was called AgentGPT another GODGPT or somethign like that. They wer einteresting to
> watch because the sytem would fire off multiple tasks. however, these systems didn't survive because
> whlie there was a lot of activity, there was very little achieved in terms of output. the next wave of
> agents was the release of Open Claw. It was the release of Open Claw that motivated me to create the
> Personal AI Dashboard project. I saw how Open Claw had potential but at too high a cost in tokens and
> too big a risk for security. AS someone who has worke din the computer industry for over 30 years, I
> realized that no organization could risk the unlimited potneal tokens costs or security costs generated
> by Open Claw. I developed the Peersonal AI Dashboard to show how a constrained enviornment with local
> models could accomplish actual work without high cost and securely. I demonstrated that giving AI tools
> to work with made them far more productive than expecting them to do the work without tools. It would be
> like asking someonw to drill an hole with no drill.

### Wave one, 2023 — activity without output, and it is documented

The author recalls **AgentGPT** and a second he remembers as *"GODGPT."* **Both are real, and the name flag
is now resolved:** the second is **AutoGPT** — the flagship 2023 autonomous agent — whose *"continuous"*
mode was widely called **god mode**, which is almost certainly what the memory is holding.

**And the community's own verdict matches the author's recollection almost word for word.** From
`r/AutoGPT`, thread *"Is AutoGPT dead?"*:

> *"AutoGPT became more of a framework for creating agents than what it used to be, like **doing stuff for
> you (tho it barely worked, if at all)**."*

> *"I was crazy active a year ago but after forge came out it's like everything related to applying thought
> and automations just died. So many promising threads for features and fixes for local LLM and multi agent
> frameworks but now it seems sidelined."*

> *"Came back to this sub after a long absence… It appears that the repository on GitHub hasn't been
> updated in a while."* — a 14K+ member subreddit, gone quiet.

**So the wave-one story is not "the agents were never built."** It is that **the autonomous-agent product
did not survive** — and it did not survive because it produced **activity instead of output**. What
survived instead were the *frameworks*: CrewAI, AutoGen, OpenDevin, Devika, MetaGPT. **The ambition was
replaced by scaffolding.** The industry's own correction was to stop selling autonomy and start selling
structure — which is this book's argument, arrived at the hard way.

**And note the shape, because it repeats in wave two:** an ambitious autonomous system, real activity, no
delivered output, a pivot, and a community that drifts away. Wave two delivers the output and pays for it
in cost and exposure instead. **Same cause, different bill.**

### Wave two — OpenClaw. Verified, and the numbers are severe

An MIT-licensed, self-hosted agent framework (Electron + Next.js, SQLite, memory-bank files) that the
author compared against the Dashboard in `docs/OPENCLAW-COMPARISON.md` — *which, note, is a feature
comparison and captures none of this.* The cost and security record is the part that matters:

- **Cost:** users report **$5/day to $3,600/month**. A documented heavy user at **1.8M tokens =
  $3,600/month**. A German magazine's (*c't*) day-long test: **$100+ in one day**. An overnight heartbeat
  repeatedly asking *"Is it daytime yet?"*: **$18.75**. Light users $30–150/mo; moderate $150–450/mo.
- **The cost drivers, as its own docs name them:** *context accumulation* (session history grows
  indefinitely), *heartbeat* (runs even when idle), and **autonomous multi-step tool use**.
- **Security:** **138+ CVEs as of April 2026**; ~45 advisories batch-published 30 June 2026; a critical
  RCE (**CVE-2026-25253**); **4 chainable TOCTOU vulnerabilities** (CVSS up to 9.6); and **341 malicious
  marketplace skills**.
- **And the direct evidence of user pain**, from the OpenClaw users group, verbatim:
  > *"Why openclaw is too expensive? I know that we are using a api key sending a lot of information to
  > openai and anthropic but wtf... at this moment I spent like 200 dollars in openai... what do you guys
  > use to mitigate?"*

**⚑ The clinching detail: OpenClaw's own documentation prescribes this book's design.** Its listed cost
mitigations are *use a local model for the heartbeat, increase the interval, set quiet hours, enable
isolated sessions, use local models for $0, route sub-agents to cheaper models.* One documented case:
**$1,200/month → $36/month using model routing.** **The cure is the architecture the Dashboard was built
on** — arrived at independently, by a different community, from a different direction.

### Why it works (the sharp part)

1. **The diagnosis is precise, and it is not "agents can't work."** It is that **autonomy is what costs.**
   Every named cost driver — context accumulation, an idle heartbeat, autonomous multi-step tool use — is
   a measure of the agent's *freedom*, not its capability. Constrain the freedom and the cost collapses:
   **97%** in the documented case.
2. **The security problem is the same problem.** 341 malicious marketplace skills is what happens when
   the thing being distributed is *executable authority*. Constrain what the agent can reach and the blast
   radius shrinks with it.
3. **The productivity came from tools, not autonomy** — the author's own demonstration. Which reframes the
   whole agent question: **it was never "can it plan?" but "can it act?"** A model with tools does work; a
   model with a loop produces activity.

**The drill line is the chapter's epigraph** and must be preserved exactly: *"It would be like asking
someone to drill a hole with no drill."*

### The handling rule

- **Never sneer at the first wave.** They were *interesting to watch* — and the honest note is that the
  author watched them too. That candour is what makes the critique land.
- **Never attack OpenClaw as a product.** It is a real framework with real capability, and its community
  arrived at the right answers unaided. The claim is about **autonomy as a design default**, not about a
  vendor. **Cite its own documentation as the corroboration** — that is stronger than any criticism.
- **Keep the personal thread.** This is the origin of the whole project: *"it was the release of Open Claw
  that motivated me to create the Personal AI Dashboard project."* It lands better as experience than as
  analysis, and it answers the question every reader will have by Part I's end — *why did you build this?*
- **Do not print the CVE and cost figures without a re-check.** They are exactly the kind of number that
  dates. Sources and dates are logged in `00-BOOK.md` §9.

**Where it lands.** **Part I, as Ch. 7** — immediately *before* the 8-Ball, which closes the part. Part I
diagnoses the error; this is that error at institutional scale, with receipts. Order matters: the
organizational misuse of an unconstrained system (Ch. 7) is followed by the personal misuse of a confident
answer (Ch. 8), and then Part II explains what to build instead.

**Guard rails:**

- **Do not let it become a takedown.** Same vendor rule as everywhere: name the pattern, never a culprit.
- **Do not overclaim the counter-demonstration.** The claim is *actual work, low cost, secure* —
  demonstrated on the author's own tasks. Not "solved for everyone."
- **Do not confuse the two waves.** Wave one failed at **output**; wave two has real output and fails at
  **cost and containment**. Different failure modes, one cause: unconstrained autonomy.
- **The wave-one names are now verified** — AgentGPT and AutoGPT (via its *god mode*). Cite `r/AutoGPT`
  for the verdict, not memory.

---

## The rules this chapter carries

**Rule 18 — *Do not hand the agent the keys.* (primary).** Two waves of agents: the first produced activity without output, the second priced autonomy in thousands a month and hundreds of CVEs. The chapter is Rule 18 — give the agent tools, not authority — with Rule 7 as the corollary: asking again is a re-roll, and so is spawning another agent for the same job.

**Rule 7 — *Asking again is a re-roll, not a re-check.* (carried).**

## DRAFT

> *"It would be like asking someone to drill a hole with no drill."*

Agents have been sold twice now as autonomy.

The promise is appealing: give a system a goal, let it plan, let it break that goal into tasks, let it create more tasks, and let it continue until the work is done.

Watch it operate and the promise becomes even more persuasive. The screen fills with plans, sub-tasks, tool calls, status updates, retries, and new branches of reasoning. It looks busy. It looks independent. It looks like work.

But activity is not work.

A system can generate a long list of actions without delivering an outcome. It can search, plan, reflect, delegate, retry, and narrate its progress while failing to produce anything useful. And if it has broad access to tools, systems, credentials, money, or executable code, it can create a second problem alongside the first:

It can become expensive and unsafe while accomplishing very little.

That is not an argument against agents.

It is an argument against confusing autonomy with productivity.

## The First Wave: Interesting to Watch

My first experience with agents came shortly after the introduction of ChatGPT.

I remember AgentGPT and another system I called "GODGPT," or something like it. The name was imprecise, but the memory was real: AutoGPT, the prominent autonomous-agent project of 2023, was widely associated with a "god mode" or continuous mode.

These systems were interesting to watch.

They would take a goal, create tasks, create more tasks from those tasks, and appear to work through a plan without constant human direction. The activity was visible. It was one of the first times many people had seen a language model apparently managing a sequence of actions on its own.

That was compelling.

It was also the problem.

There was often a great deal of activity and very little achieved in terms of output.

The agents could look industrious while struggling with the ordinary requirements of useful work: identifying the right objective, holding onto relevant context, using reliable information, making decisions at the appropriate level of confidence, and finishing the task rather than expanding it.

The community's own retrospective describes the result almost exactly. In a discussion titled "Is AutoGPT dead?", one user wrote:

> "AutoGPT became more of a framework for creating agents than what it used to be, like doing stuff for you (tho it barely worked, if at all)."

Another described a once-active community losing momentum after its framework changes:

> "I was crazy active a year ago but after forge came out it's like everything related to applying thought and automations just died."

And another returning user noted that the repository had not been updated in some time.

The point is not that nothing was built. It was.

The point is that the first wave did not establish the autonomous agent as a dependable product for getting work done. What survived was not the original promise of an independent system that would simply do the work for you.

What survived was scaffolding.

CrewAI. AutoGen. OpenDevin. Devika. MetaGPT.

Frameworks for defining roles, controlling workflows, assigning tools, structuring tasks, and building systems around models.

The ambition was replaced by structure.

That was not a retreat from progress. It was the industry learning the right lesson.

The useful question was never:

> Can a model keep generating the next task?

It was:

> Can the system deliver a bounded, verifiable result?

Those are not the same thing.

## A Loop Is Not a Workforce

An autonomous loop can create the appearance of work because it produces a visible sequence of steps.

It plans.

It searches.

It reflects.

It asks itself what to do next.

It creates sub-agents.

Those sub-agents create reports for the original agent.

The original agent reviews the reports, revises the plan, and starts again.

At every stage, the system has something to show.

But visible motion is not proof of useful progress.

A meeting can be busy without producing a decision. A dashboard can be full without showing the right metric. A project can have hundreds of tasks without delivering a product.

An agent is no different.

A good system should be judged by the output it produces under defined constraints:

- Did it complete the requested task?
- Was the result correct enough for its intended use?
- Did it use authorized data and tools?
- Can a person inspect what it did?
- Did it stay within a known cost?
- Could it have caused harm while trying?

If the answer is no, the fact that it generated twenty pages of plans is not a consolation.

It is evidence of activity.

Not work.

## The Second Wave: Output With a Bill Attached

The second wave of agents is more serious.

The systems are more capable. The tool use is more real. The integrations are broader. The frameworks can operate over files, browsers, code, databases, messaging systems, APIs, and other parts of an organization's environment.

That creates real potential.

It also creates real cost and real exposure.

OpenClaw was the release that motivated me to create the Personal AI Dashboard project. It was an MIT-licensed, self-hosted agent framework, built with Electron, Next.js, SQLite, and memory-bank files. It had features and possibilities that were worth paying attention to.

But I saw the same underlying problem in a more expensive form.

The system had potential, but at too high a token cost and too great a security risk.

As someone who has worked in the computer industry for more than thirty years, I did not believe an organization could accept unlimited potential token costs or the security exposure created by broadly empowered autonomous agents.

The reported figures make the concern concrete.

OpenClaw users reported costs ranging from roughly $5 per day to $3,600 per month. A documented heavy user reportedly consumed 1.8 million tokens at a cost of $3,600 per month. A day-long test by the German magazine *c't* reportedly exceeded $100 in a single day. One overnight heartbeat—repeatedly asking whether it was daytime—cost $18.75.

The pattern is visible even in the user complaints. One OpenClaw user wrote:

> "Why openclaw is too expensive? I know that we are using a api key sending a lot of information to openai and anthropic but wtf... at this moment I spent like 200 dollars in openai... what do you guys use to mitigate?"

This is not a complaint about intelligence.

It is a complaint about unconstrained activity.

The documented cost drivers were context accumulation, heartbeats that run while the system is idle, and autonomous multi-step tool use.

Each is a measure of freedom.

A context that grows indefinitely gives the agent more history to process, at increasing cost. A heartbeat that runs without a user request gives the agent more opportunities to spend. Autonomous multi-step tool use permits the agent to make more calls, take more actions, and create more work for itself.

The more freedom the system has, the more it can do.

It can also spend more while doing it.

## Autonomy Is What Costs

This is the sharp part.

The cost of an agent is not simply the cost of intelligence.

It is often the cost of autonomy.

Every extra loop, heartbeat, context refresh, sub-agent, retry, browser action, and tool call is a decision to let the system continue acting without a person first deciding that the next action is worth its cost.

That is sometimes useful. It is never free.

The same OpenClaw material describes the remedies:

- use a local model for the heartbeat;
- increase the heartbeat interval;
- set quiet hours;
- enable isolated sessions;
- use local models where appropriate;
- route sub-agents to cheaper models.

In one documented case, model routing reduced costs from $1,200 per month to $36 per month.

That is a 97 percent reduction.

The important lesson is not that every agent should use one particular framework or model. It is that the cure was architectural.

Constrain the activity.

Route inexpensive work to inexpensive systems.

Do not run when there is no work to do.

Do not carry unnecessary context.

Do not let the agent choose an unbounded number of expensive next steps.

The productivity was never in giving the system unlimited autonomy. The productivity came from giving it the right tools, within a controlled environment.

## Security Is the Same Problem in Another Form

The security problem has the same shape as the cost problem.

A system that can reach everything can damage everything.

OpenClaw's reported security record included 138+ disclosed CVEs by April 2026, approximately 45 further advisories published in a batch on June 30, 2026, a critical remote-code-execution vulnerability identified as CVE-2026-25253, four chainable time-of-check/time-of-use vulnerabilities with CVSS scores up to 9.6, and 341 malicious marketplace skills.

⚠️ These figures are live security facts and must be re-verified before publication. They are included here as dated evidence, not as permanent counts. The exact number will change. The design lesson will not.

A marketplace skill is not just text. It can be executable authority. It can access files, tools, accounts, services, and workflows depending on what permissions the system grants it.

Three hundred and forty-one malicious skills are not merely a marketplace moderation problem. They demonstrate what happens when an ecosystem distributes executable capability at scale.

The security question is not:

> Is the agent intelligent enough to make good decisions?

It is:

> What can the agent reach if it makes a bad one?

That is the blast radius.

If the agent can access a customer database, send email, execute code, move money, alter infrastructure, or install software, then a mistake, prompt injection, compromised skill, malicious input, or flawed workflow can turn generated language into a real-world action.

The answer is not to ask the agent to be more careful.

The answer is to limit authority.

Give it access only to the tools required for the job. Give each tool only the permissions required for the action. Require approval for high-consequence steps. Keep sensitive systems separate. Log every consequential action. Use local tools and local models where that reduces exposure. Make sure a failure is contained.

Constrain what it can reach, and the blast radius shrinks with it.

## Give the Agent Tools, Not Authority

This is the rule:

> **Do not hand the agent the keys.**

An agent should have tools.

It should not have unlimited authority.

That distinction matters.

A useful tool might allow an agent to search an approved document repository, calculate a value, read a customer record within the current user's permissions, draft an email without sending it, or create a support ticket for human review.

Those are bounded capabilities.

Unlimited authority is different. It means the agent can decide what to access, what to spend, who to contact, what software to run, what code to deploy, or what records to alter—often across multiple steps and without a defined stopping point.

That is not productivity.

That is delegation without governance.

The Personal AI Dashboard was built to demonstrate the alternative: a constrained environment, using local models where appropriate, that could accomplish actual work without high cost and without handing an autonomous system broad access to everything it could find.

The result was not less capable because it had limits.

It was more useful because it had a job.

## The Drill Is the Point

The productivity came from tools, not autonomy.

A model asked to perform a task with no access to the information, software, or systems needed to complete it is being asked to improvise.

It may produce a plan. It may produce instructions. It may produce plausible language around the task.

But it cannot do the work that requires a tool it does not have.

> "It would be like asking someone to drill a hole with no drill."

Giving the model a drill changes what it can accomplish.

Giving it the keys to the whole building does not make it better at drilling holes.

It only gives it more places to go wrong.

A constrained agent can retrieve the right document, use the approved calculator, call the relevant API, update a permitted record, or create an output for review. It can complete a defined unit of work.

A loosely governed autonomous loop can generate plans about all of those things indefinitely.

The difference is not intelligence.

It is design.

## Build for Outcomes

The right goal is not an agent that appears independent.

It is a system that reliably completes useful work at an acceptable cost and risk.

That means defining:

- the specific task;
- the tools needed to complete it;
- the data the agent may access;
- the actions it may take;
- the maximum cost it may incur;
- the point at which it must stop;
- the conditions that require human approval;
- the logs and evidence needed to review its work.

An agent should know when it has completed the job.

It should also know when it is not allowed to continue.

That is not a limitation of the system. It is what turns activity into work.

The first wave showed that autonomous motion is not enough.

The second wave showed that autonomy can produce output—but that broad freedom carries a bill in tokens, security exposure, and operational risk.

The better path is neither to abandon agents nor to worship them.

Give them real tools.

Give them bounded authority.

Use local and cheaper models for cheap work.

Cap spending.

Keep sensitive capabilities isolated.

Require evidence for consequential actions.

And judge the system by what it delivers, not by how busy it looks.

---

*Verification: this chapter is the author's own draft, adopted with one correction — "drill an
hole" is "drill a hole," the canonical form used everywhere else in the book (RULES.md,
00-BOOK.md, and the concept's own handling note, which says the drill line is the chapter's
epigraph and must be preserved exactly). Carries Rule 18 (primary) — *do not hand the agent the
keys* — with Rule 7 (*asking again is a re-roll, not a re-check*). Every load-bearing figure
traces to the §9 register, verified 12 October 2026: the wave-one names (AgentGPT, AutoGPT,
"GODGPT" = AutoGPT's continuous/god mode) and the r/AutoGPT community quotes; the wave-two cost
figures ($5/day–$3,600/month, 1.8M tokens, the c't day-long test at $100+, the $18.75 overnight
heartbeat, the $1,200→$36 routing case = 97%); and the security record (138+ CVEs by April 2026,
~45 advisories batch-published 30 June 2026, CVE-2026-25253, four chainable TOCTOU flaws at CVSS
≤9.6, 341 malicious marketplace skills). ⚠️ Per the register's own standing caution — re-check
the cost and CVE figures before print; they date fastest of anything in the book. The author's
first-hand experience (his first agents, OpenClaw motivating the Personal AI Dashboard) is
testimony, not a citation, and is presented as such. OpenClaw appears as an example of a pattern
(autonomy as a design default), not as a culprit — per the book's standing rule.*
