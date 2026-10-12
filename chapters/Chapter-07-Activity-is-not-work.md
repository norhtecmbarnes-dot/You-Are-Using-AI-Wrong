# Chapter 7 — Activity is not work

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

**Claim.** agents have been sold twice now as **autonomy**, and autonomy is the expensive, insecure way to get work done. A system that fires off tasks looks busy; a system that can reach anything costs more than the work is worth. **Neither wave failed for lack of intelligence. Both failed for lack of constraints.**

**Demonstration.** **wave one, 2023** — **AgentGPT and AutoGPT**, agents that spawned tasks from tasks, which the author watched because they were *interesting to watch*, and which died because *there was a lot of activity and very little achieved in terms of output*. **The community's own verdict agrees, almost in his words:** *"like doing stuff for you (tho it barely worked, if at all)"* — and what survived was not the autonomous agent but the *frameworks* (CrewAI, AutoGen, OpenDevin, Devika, MetaGPT). **The ambition was replaced by scaffolding.** **Wave two** — a real framework with real potential, priced in numbers that end the argument: a heavy user at **$3,600/month**, a magazine's day-long test at **$100+ in a single day**, and an overnight heartbeat costing **$18.75** to repeatedly ask whether it was daytime — alongside **138+ disclosed CVEs**, a critical RCE, and **341 malicious marketplace skills**. *No organisation can accept that* — and thirty years in the industry is why the author didn't.

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
organisational misuse of an unconstrained system (Ch. 7) is followed by the personal misuse of a confident
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

*(map the chapter to its rule numbers here before drafting — every chapter carries at least one)*

## DRAFT

*(write it here. Target roughly 1,300 words. Same rule as the rest of the book: every*
*load-bearing claim to a source, citations kept, nothing invented, anything unverifiable*
*marked ⚠️ rather than smoothed over.)*
