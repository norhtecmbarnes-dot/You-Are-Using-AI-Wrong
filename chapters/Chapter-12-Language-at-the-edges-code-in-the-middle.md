# Chapter 12 — Language at the edges, code in the middle

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: the LLM belongs where language enters and leaves. Determinism belongs everywhere the work has
  to be right.
- Demo: a provider router choosing between tools with no model involved — probe, filter, walk the order,
  take the first available. Same input, same decision.
- Fix: the division of labour as a rule for any feature you're about to build.

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **⚑ Poppy's real advantage — model freedom and configurability. Verified in Poppy's own API docs.**
  *Raised by the author: "Poppy AI has the advantage that it is not limited to Google models. It also
  provides a more configurable input/output model."* **Both confirmed:**
  - `POST https://api.getpoppy.ai/api/conversation?board_id=…&api_key=…` takes a **`model` field set per
    request**. Documented allowed values: **`claude-sonnet-4-6`** (default), `claude-sonnet-4-5`,
    `o3-mini`, `gpt-4o`, `grok-2-1212`, `gpt-4o-mini`. *"Leave it off and Poppy uses its current
    default."*
  - The chat endpoint is literally documented as **"Chat with knowledge base"** / **"Ask knowledge
    base"**, scoped by `board_id` — **the knowledge is confined to a board, and the model is chosen per
    call.** That is the synthesis in one API signature.

  **So the two tools fail in opposite directions, which is the chapter's whole shape:**
  **NotebookLM** is confined *and* cheap, but welded to Gemini. **Poppy** frees the model but is a paid
  content tool. **Neither is the answer on its own** — and the fix is to stop treating confinement and
  model choice as a trade-off. *The API above proves they are two independent parameters.*

- **⚑ The capability bus — the second axis, and it sits outside the notebook frame entirely.**
  *Raised by the author: "a model escalation message service that provided a mechanism for models to test
  their limits and only do tasks they were confident that they could complete… I have had good luck doing
  research using models as small as 1.5b parameters — even running these tasks on laptops without CPUs.
  Giving a model the ability to test its limits opens up the possibility of migrating tasks to smaller
  and smaller hardware."*

  **Verified in `src/lib/services/model-bus.ts` — 699 lines, in both repos.** The self-assessment prompt
  asks the question the author remembered, in substance if not in wording:
  *"Can you answer this COMPLETELY and ACCURATELY right now? **Would the user be SATISFIED with your
  answer?** Should this go to a smarter cloud model?"* — and the fail-safe that makes it safe:
  **"If you're UNSURE, lean toward canHandle: false."**

  **Why it earns a chapter (Ch. 18).** It is the one place in the book where a model's self-report is
  worth something, and the reason is exact: it is asked a **routing** question — *"is this job mine to
  do?"* — not a **knowledge** question. Routing is checkable, because you find out immediately whether the
  cheap path held. **The design does not trust the self-assessment; it bounds it.**

  **And it inverts the hardware story.** `local-small` is flagged `isCPUFriendly`; BitNet is integrated
  for GPU-free inference; `docs/CPU-ONLY-SETUP.md` recommends `qwen2.5:1.5b` on CPU alone. So: **the
  smallest model that correctly declines is the model you need** — and every task it *accepts* is a task
  that can migrate down. *The usual expectation is that AI demands more compute. This design makes the
  requirement fall over time.*

  ⚠️ **Two things to carry honestly:** do not claim the model *knows* its limits (it is asked to make a
  routing call, under a prompt biased toward declining), and verify `qwen2.5:1.5b` still runs CPU-only
  before printing the figure. The 1.5B research claim is the author's first-hand experience — **present it
  as such, which is stronger than any statistic.**

---

## The rules this chapter carries

**Rule 13 — *Right-size the model to the task.* (primary).** The division of labour: language at the edges, determinism in the middle. The architecture that makes Rule 13 (route in code) and Rule 14 (match effort) enforceable — no model in the decision path.

## DRAFT

*(write it here. Target roughly 1,600 words. Every load-bearing claim to a source,*
*citations kept, nothing invented, anything unverifiable marked ⚠️ rather than*
*smoothed over — the same rule the rest of the book was written under.)*
