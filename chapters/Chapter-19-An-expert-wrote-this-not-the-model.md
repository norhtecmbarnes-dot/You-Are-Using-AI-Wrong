# Chapter 19 — An expert wrote this, not the model

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

**Claim.** the model is not a source of facts — **and it is not a source of method either.** When you ask an LLM to write the agent's instructions, you get *a generic model's guess at how the work is done*, executed faithfully by an agent that has never done it. **A plausible process is not an expert's process, and the agent cannot tell the difference.**

**Demonstration.** two agents, same model, same task. One is briefed with a model-generated prompt; one with an expert's actual method — the checks, the order, the things to refuse. **The difference in the output is not the model. It is the brief.** And the Dashboard's own evidence is that its system prompt is *hand-written*: a senior capture manager's voice, rules and refusals, authored by a human who knows the work — never generated.

**Fix.** **the prompt is a knowledge artifact.** Write it by hand, extract it from an expert, or capture it from someone who has done the work a thousand times — then let the model run it.

---

## Concept 10 — The prompt is a knowledge artifact, not a model output

> This is the captured material this chapter expands. It is in `CONCEPTS.md`.

*The rule that completes the book's first rule. Stated by the author as a theory; it is a rule.*

**As stated by the author:** (verbatim — preserve the words; they carry intent)

> this is a theory but it is a rule. Agentic AI has great potential but the fault with agentic ai is that
> most people rely on the LLM to prompt the agent itself. A truely great agent should replect the
> knowledge of a true expert with experience, not a gneric self-generated prompt.

### Why it is a rule and not a theory

**It is Rule 1, applied one level up.** The book opens by insisting that a model must never be asked for
*knowledge* — facts are injected, never remembered. This says the same thing about **method**: the plan the
agent follows must come from outside too.

Ask a model to write the agent's instructions and you get **a generic model's guess at how the work is
done**, executed faithfully by an agent that has never done it. The agent cannot tell a plausible process
from an expert's process — that is the whole problem, and it is the book's original sin one layer deeper.
**A confident procedure is exactly as trustworthy as a confident fact.**

### The distinction that makes it sharp

There is a real difference between two things that look alike:

| | What it is | Who authors it |
|---|---|---|
| **The plan** | the method, the order, the checks, **the refusals** | **a human who has done the work** |
| **The execution** | understanding the request, drafting, summarizing, formatting, talking to tools | the model, freely |

**Models may summarize, reformat and draft all day. What they must never author is the plan they will
then be judged against.** That is the line, and it is checkable.

### Verified in the Dashboard — and it is the clearest instance in the project

Every **governing instruction** in the system is hand-written by a human:

- `soul.md` — a senior capture manager's voice, rules, and refusals. Not a generated persona: *"You ASK
  WHEN YOU DON'T KNOW… Guessing when you could ask is a failure."* Somebody who knows the work wrote that.
- `knowledge-policy.ts` — 79 lines of hand-written policy, injected at every call site.
- `strengths-policy.ts` — the strengths-only soul rule, authored.
- `local-first.ts` — the gate, authored.

**None of them is a model output, and none of them would work as well if it were.** The comparison to make
is a system whose system prompt was asked for: it reads fluently and tells the agent nothing an expert
knows.

### The corollary: this is why skills matter

**A skill file is how an expert's method reaches an agent.** It is a hand-authored artifact — a procedure,
a checklist, a set of pitfalls — that the model *executes* rather than *invents*. That is the mechanism by
which **experience, not eloquence, gets into the agent.**

The industry has noticed without naming the principle: Claude Code skills, Vois's `SKILL.MD`, MiniMax's
official caption-rewriter skill. All of them are the same move — **write down what a person who has done
this a thousand times knows, and hand it to the model to follow.**

### The handling rule

- **Lead with the completion, not the complaint.** This is not "prompting is hard." It is *the first rule of
  the book, closing its own loop* — and the chapter should read as a payoff.
- **State the distinction, don't blur it.** Plan versus execution. The rule is about the brief and the
  governing instructions, **not every string the system sends.**
- **Ask the reader a testable question at the end:** *who wrote your agent's instructions — and have they
  ever done the job?* If the answer is "the model," the chapter has done its work.
- **Do not sneer at prompt engineering.** Its practitioners discovered this the hard way and many of them
  already know it. **Credit them; the rule simply says why it works.**

**Where it lands.** **Part III, as Ch. 19** — immediately after the agent evidence (Ch. 18). The sequence is
deliberate and it is the part's spine: *let the small model decline* (18) → *don't scale by multiplying
agents* (19) → **brief it like an expert** (20) → then measure, fetch, and build. Ch. 18 shows why the swarm
fails; Ch. 19 shows what to do instead with the one agent you keep.

**Guard rails:**

- **Do not let it become a chapter about prompts.** It is a chapter about **authorship** — who is allowed
  to decide the method. Prompt tricks are not the subject; expertise is.
- **Do not claim the expert's method must be perfect.** It must be *real*. A rough plan from someone who
  has done the work beats a polished plan from something that hasn't.
- **Do not contradict Ch. 11 ("A function, not a source").** The model is still doing the hard part —
  understanding, drafting, adapting. It is being *briefed*, not deskilled.
- **Remember the book's own rule.** The chapter must not cite a product as the answer. Skills are named as
  the *mechanism*; the claim is the principle.

---

## The rules this chapter carries

**Rule 20 — *The prompt is a knowledge artifact.* (primary).** The prompt is a knowledge artifact: a model-written brief is a generic model's guess at how the work is done, executed faithfully. The chapter is Rule 20, generalising Rule 1 from facts to method — never let it write the plan it will follow.

**Rule 1 — *It doesn't know things.* (carried).**

## DRAFT

*(write it here. Target roughly 1,600 words. Same rule as the rest of the book: every*
*load-bearing claim to a source, citations kept, nothing invented, anything unverifiable*
*marked ⚠️ rather than smoothed over.)*
