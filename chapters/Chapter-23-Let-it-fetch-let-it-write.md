# Chapter 23 — Let it fetch, let it write

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: give it what code fetched, and it will do the language work over it.
- Demo: a research loop end to end — code pulls facts, a cheap model ranks, the best model writes, code
  validates and queues, a human approves. **Real, verified run.**
- Fix: split every task into the part code must do and the part language should do.

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **The self-education loop** (Ch. 22) — real, verified live. 10 tools checked, 9 baselines.

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

**Rule 1 — *It doesn't know things.* (primary).** Give it what code fetched, and it does the language work over it: Rule 1 (attach the facts) with the pipeline made explicit. The fetch is code; the writing is language; the boundary is Rule 12's contract.

**Rule 12 — *Confinement is the design, not a limitation.* (carried).**


**Rule 21b — *Automating a process is not the same as justifying it.* (carried).** Rule 21b belongs in the fetch-and-write chapter: the pipeline automates a process, and the chapter should ask whether that process should exist before it is made faster.
## DRAFT

*(write it here. Target roughly 1,600 words. Every load-bearing claim to a source,*
*citations kept, nothing invented, anything unverifiable marked ⚠️ rather than*
*smoothed over — the same rule the rest of the book was written under.)*
