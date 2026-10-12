# The Rules, and where the Dashboard implements them

**The book points back at the system.** This file is the evidence: every one of the 21 rules, mapped to
the code that implements it — or honestly marked as not yet implemented.

**This file exists because the book claims the Dashboard is its worked example.** That claim is only
worth making if it is true, so each row is verified against the source, with the file named, and anything
not found is recorded as a gap rather than quietly rounded up. A book about not trusting confident claims
cannot afford a flattering one of its own.

**Status key:** ✅ implemented · ◐ partly — something is there, but not the whole rule · ○ not yet — a
target, not a claim.

| # | Rule | Status | Where it lives |
|---|---|---|---|
| 1 | Attach the facts; never ask it for knowledge | ✅ | `src/lib/config/knowledge-policy.ts` |
| 2 | Treat every declaration as unverified | ✅ | `knowledge-policy.ts` §§4–5 |
| 3 | It informs, you decide | ◐ | `soul.md` — *"ASK WHEN YOU DON'T KNOW"* |
| 4 | It has never seen the future | ◐ | `src/lib/models/alpha.ts` grounding test |
| 5 | It cannot tell you it's unsure | ✅ | `knowledge-policy.ts` §4 |
| 6 | You cannot teach it — put rules in code | ✅ | All four policy modules; see §6 below |
| 7 | Asking again is a re-roll, not a re-check | ◐ | `alpha.ts` — fixed seeds, ties to incumbent |
| 8 | "It reasoned about it" is not proof | ○ | — |
| 9 | It multiplies what you bring | ✅ | `src/lib/config/strengths-policy.ts` |
| 10 | Delegating the thinking costs you the ability | ○ | — |
| 11 | Your question is usually the real problem | ◐ | `knowledge-policy.ts` §3 — ask, don't guess |
| 12 | Confinement is the design | ✅ | `knowledge-policy.ts` + brand/project document scoping |
| 13 | Right-size the model to the task | ✅ | `src/lib/models/model-router.ts` |
| 14 | Match the effort to the question | ✅ | `model-router.ts` tiers + `model-bus.ts` self-assessment, fail-safe by design |
| 15 | Find your test, or find your source | ✅ | `alpha.ts` benchmark; `agent/self-education.ts` |
| 16 | Buy the tool for the job | ✅ | `src/lib/config/local-first.ts`; the render provider registry |
| 17 | Let the small model say "I can't" | ✅ | `src/lib/services/model-bus.ts` — self-assessment + fail-safe escalation |
| 18 | Do not hand the agent the keys | ✅ | the project itself: `local-first.ts` gate, router budget, provider registry, agent-as-operator with a restricted toolset |
| 19 | Agents are not a scaling axis | ◐ | architecture is one agent with tools (the correct answer) — but nothing yet forbids adding concurrent agents |
| 20 | The prompt is a knowledge artifact | ✅ | `soul.md`, `knowledge-policy.ts`, `strengths-policy.ts`, `local-first.ts` — every governing instruction is hand-written, none is a model output |
| 21 | The expert is the product | ✅ | the Dashboard's differentiator *is* its domain knowledge: government-contracting docs, compliance, brand vault, bid workflow — none of it in the model |

**Score: 14 fully implemented, 5 partial, 2 not started.** That is a fair picture and the book should say
so — a half-built method is still a method, and claiming more would be the exact failure the book
prosecutes.

---

## The two the author named

### "Focusing on using lowest cost models where possible" — ✅ implemented, with one important caveat

**Verified in `src/lib/models/model-router.ts` — 953 lines.** It is a genuine three-tier escalation
system, not a stub:

- **Tier 1 — housekeeping:** *"Always use smallest fastest model."* A `TASK_MODEL_MAP` routes around forty
  task types by name. `heartbeat`, `scheduled`, `health_check`, `memory_search`, `token_optimization`,
  `cleanup`, `maintenance`, `monitoring` all resolve to `local-fast`.
- **Tier 3 — complex reasoning:** `complex_analysis`, `strategic_planning`, `architecture_design`,
  `decision_making`, `planning`, `system_design`, `troubleshooting`, `debugging`, `optimization` resolve
  to `cloud-thinking`. The expensive tier is reserved for the tasks that need it — which is the rule.
- **A token budget:** `dailyTokenLimit: 100000`, tracked daily.
- **Budget-critical fallback:** when `remaining < dailyLimit * 0.1`, the router **forces local** and logs
  *"Budget critical, using local models."* That is cost-aware behavior in code, not sentiment.
- **Local models are declared free** — `costPerToken: 0` — and `preferLocal` defaults to `true`.

**⚑ The caveat, and it must go in the book honestly:** the router is **local-first and budget-aware, but
it does not rank by cost.** Two specifics:

1. `costPerToken` is **`0` for almost every model**, including the large cloud ones — `glm-5`,
   `kimi-k2.5`, `deepseek-v3.2`, `qwen3.5:397b` are all `0`. Only three entries carry a nonzero price.
   Cost is *declared* in the type but is **not** used as a ranking signal.
2. In Tier 2 the candidates are sorted by **model size, largest first** (`sizeB - sizeA`) — the comment
   says *"Prefer larger models for complex tasks."* That is capability-first, not cost-first.

**So the accurate claim is:** *the Dashboard avoids cost rather than minimising it* — it does the
expensive work locally where it is free, uses the smallest model for grunt work, and abandons cloud
entirely when the budget runs low. **That is the substance of Rule 13, and it is real.** But a reader who
opens the file will see that `costPerToken` is inert, so the book must not describe a cost-optimising
router.

**If you want the stronger claim to be true**, the change is small and worth doing: populate real
`costPerToken` values for the cloud entries and make the Tier 2 sort cost-aware when a budget is
configured. Then "lowest cost where possible" is literally what the code does.

### "Can I answer this question to my human's expectation, and will he be happy with my response?" — ✅ FOUND, and already built

**This entry corrects an earlier one. I first reported this as not found. I was wrong, and the mistake
was mine** — I searched for the author's *paraphrase* and the code uses different words. The mechanism is
there: `src/lib/services/model-bus.ts`, the **model escalation message service**, 699 lines, in both
repos. See *The capability bus* below.

**The question, verbatim in the prompt** — `getSelfAssessmentPrompt()`:

> 1. Can you answer this COMPLETELY and ACCURATELY right now?
> 2. **Would the user be SATISFIED with your answer?**
> 3. Should this go to a smarter cloud model?

**And the line that makes it safe to run unattended:**

> **"If you're UNSURE, lean toward canHandle: false."**

**The lesson is worth keeping, because the book will make the same mistake if it is careless: a search
for your own words is not a search for the thing.** Absence of a phrase is not absence of a mechanism —
and the honest report is *"I could not find it"*, never *"it is not there."*

---

## Where the strong rules already live (detail)

**Rule 6 — put policy in code, not in the model's character.** The Dashboard does not *ask* the model to
behave; it injects policy at every call site. Four modules, all authored, all committed:

```
src/lib/config/knowledge-policy.ts   KNOWLEDGE_POLICY + withKnowledgePolicy()  (79 lines)
src/lib/config/local-first.ts        LOCAL_ONLY / PREFER_LOCAL / gateModel()  (113 lines)
src/lib/config/strengths-policy.ts   the strengths-only soul rule             (51 lines)
src/lib/models/alpha.ts              the contestable Alpha + benchmark       (234 lines)
```

This is the single clearest instance of the book's own thesis inside the system: **a rule written into
the prompt is a design; a rule hoped for in the model's character is a wish.**

**Rule 12 — confinement, and the unit of focus.** Not one mechanism but **four** layers, all verified.
The fourth is the one the author named, and it is the sharpest.

1. **Policy** — `knowledge-policy.ts`: *"Never answer a factual question from your own memory or
   training… Your internal knowledge is untrusted by design."*
2. **Scoping** — documents carry `source: 'brand' | 'project'` with `brandId` / `projectId`
   (`src/types/brand-workspace.ts`). The bid workflow loads *"the project's own documents (the RFP
   uploads), **not the whole brand vault**."*
3. **Voice** — `Brand.voiceProfile` (`tone`, `style`, `keyMessages`, `avoidPhrases`, `customInstructions`)
   gives the system a defined perspective rather than an anonymous one. **The same idea as Poppy's brand
   voice, arrived at independently.**
4. **⚑ The unit of focus — one project at a time.** This is the design decision that makes the other
   three hold, and it is the direct answer to *how* NotebookLM and Poppy confine.

### The unit of confinement — the axis that makes the trio comparable

All three tools confine, but each picks a **different unit**, and naming the unit is what turns the
comparison into an argument:

| Tool | The unit of confinement | The voice layer |
|---|---|---|
| **NotebookLM** | a **notebook** | — none |
| **Poppy AI** | a **board** (`board_id` in its API) | brand voice profile |
| **Proposal Genie** | a **project** (`projectId`) — **one proposal at a time** | `Brand.voiceProfile` |

**In Proposal Genie the two levels do different jobs, and that is the insight:**

- **The brand is what stays.** The voice, the key messages, the phrases to avoid — the company's
  identity persists across everything. It is the *continuity* layer.
- **The project is what changes.** One solicitation, one set of RFP documents, one deadline, one bid.
  It is the *focus* layer.

So the reader is never inside a general assistant with the whole company in the context window. They are
inside **one proposal**, written **in one voice**. Verified in the types: `ChatRequest` requires **both
`brandId` and `projectId`** — you cannot open a chat without naming the project it belongs to. A
`Project` carries its `solicitationType` (SBIR, STTR, BAA, OTA, CSO, RFI, RFP), status, requirements,
deliverables and deadline; the bid workflow tracks it through
`capture → compliance → outline → writing → review → submitted → archived`.

### And it goes further than either commercial tool: the confinement is *auditable*

NotebookLM shows citation chips — which is good, and better than most. Proposal Genie **records the
provenance**: every `ChatSession` carries

```
context: {
  brandDocumentsUsed: string[]      ← exactly which brand documents fed this conversation
  projectDocumentsUsed: string[]    ← exactly which project documents fed it
  totalTokensUsed: number           ← what it cost
}
```

and every `ChatMessage` carries `metadata: { model, tokens, documentsReferenced }`.

**So it can answer, after the fact, three questions neither NotebookLM nor Poppy can:** *which documents
were in play, which model answered, and what it cost.* That is the routing (Rule 13) and the confinement
(Rule 12) sharing one record — and it is the reason the token budget in the router is meaningful rather
than decorative.

**This is the strongest thing in the system, and the book should treat it as such.** Rule 12 is not
"partly implemented" — it is implemented in a way that is *evidence-producing*.

**Rule 16 — buy the tool for the job.** The render provider registry contains **no LLM at all**: probe →
filter by capability → walk the configured order → take the first available. It fell through from Vois
(unavailable, app not running) to VocalLab (available) with no model consulted. That is the user's own
principle — *code is predictable, LLMs are not* — implemented rather than stated.

### The capability bus — Rules 13 and 14, and the book's second pillar

**`src/lib/services/model-bus.ts`, 699 lines, in both repos.** This is Concept 7, and it is the only place
in the system where a model is asked a question it can actually answer.

Its own header states the architecture:

```
Uses self-assessment: local model decides if it can handle a task or needs to escalate to a smarter
cloud model.
1. Small local model receives query with self-assessment prompt
2. Model honestly evaluates: can I answer this well?
3. If yes, process locally (cheap, fast)
4. If no, escalate to user's preferred cloud model
```

**The prompt, verbatim** (`getSelfAssessmentPrompt()`):

```
You are a tiny local AI model with limited capabilities. Your job is to be HONEST about what you can handle.
Analyze the user's query and decide:
1. Can you answer this COMPLETELY and ACCURATELY right now?
2. Would the user be SATISFIED with your answer?
3. Should this go to a smarter cloud model?
Rules:
- simple fact / definition / calculation / format / routine  → canHandle: true
- deep reasoning, up-to-date knowledge, creative writing, complex analysis → canHandle: false
- If you're UNSURE, lean toward canHandle: false
- If the query is in a language you weren't trained on, lean toward canHandle: false
{"canHandle": true/false, "reason": "...", "suggestedTier": 2}
```

**⚑ The fail-safe is the design.** *"If you're UNSURE, lean toward canHandle: false."* Doubt escalates.
The cheap mistake ("I'll pass, send it up") is the default; the expensive mistake ("I've got this")
requires confidence. And if the assessment call itself errors, the fallback is
`canHandle: context.length < 500` — short task handled, long task escalated. **Even the failure path leans
the right way.**

The assessment runs on the **smallest available model** at `temperature: 0.3`, `maxTokens: 200`, and the
response carries `costSavings` and a `delegationPath`, so the routing is visible after the fact.

**Why this is legitimate when the book spends nine chapters saying a model's confidence is worthless:**
the question is not *"is this true?"* — a fact the model cannot see — but **"is this job mine to do?"**
That is a routing decision, and routing decisions are **checkable**, because you learn immediately
whether the cheap path held. **The design does not trust the self-assessment; it bounds it.**

**And the hardware consequence, which is the real prize.** `ModelTier` carries an explicit
**`isCPUFriendly`** flag on `local-small`. BitNet is integrated (`src/lib/services/bitnet.ts`,
`/api/bitnet`) for Microsoft's 1.58-bit models — *"AI inference on machines WITHOUT a GPU."* And
`docs/CPU-ONLY-SETUP.md` documents CPU-only operation, recommending **`qwen2.5:1.5b`** (1.5 GB, ~2.5 GB
RAM, *"Very Fast"*, **"Recommended"**).

> **The smallest model that correctly declines is the model you need.** Every task the small model
> *accepts* is a task that can move down — off the cloud, off the GPU, off the big machine. **The
> capability bus is a hardware-migration engine disguised as a router.**

The author reports first-hand research on models as small as **1.5B parameters on CPU-only laptops.**
Present that as experience, which is what it is — and verify the `qwen2.5:1.5b` figure before printing it.

---

## How to use this file

1. **Chapter 27 ("Start here") should close on it.** The rules are paid off by a system, not by a
   summary — and the ◐ and ○ rows are where the next round of work goes.
2. **Keep it honest.** If a rule moves from ○ to ✅, change the row *and* the code. If the code changes
   in a way that breaks a claim, fix the row in the same commit.
3. **Do not print the SHAs or file paths in the manuscript.** Chapter text says *"the model router"*;
   this file says which file and line. The book needs the claim, the reader needs the pointer, and
   neither needs a commit hash.
