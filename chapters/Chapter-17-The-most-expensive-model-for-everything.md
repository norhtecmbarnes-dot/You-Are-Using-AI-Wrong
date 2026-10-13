# Chapter 17 — The most expensive model for everything

**STATUS: starting markdown. The concept is below; this file is a skeleton to expand.**

---

## From the plan (00-BOOK.md section 7)

**Claim.** subscription pricing makes each call free at the point of use, so nobody economises — a correct response to a price signal someone else chose. **The subscription is cheap; the trust is what costs money.**

**Demonstration.** **wave one had a compiler, wave two didn't.** IT's trust was earned by a test that can't be fooled; the report-writers inherited the tool without one.

**Fix.** **right-size the tool and the model, and route in code.** Don't leave the biggest model on by default, don't buy a general chat engine for a confined job, and don't ask staff to self-police.

**The unit the bill is counted in (Concept 17).** Open the cost argument with the decision maker's
definition of a token: *a token is a unit of intelligence — the smallest unit of work the model
performs, and on metered pricing, the unit the bill is counted in.* You are not buying a subscription
to a brain; you are buying a metered quantity of intelligence, and the question this chapter asks is
whether the task needs that much. (The technical definition — a fragment of text — belongs to
Chapter 11; the two definitions are bridged there, not merged.)

**Framing to hold (Concept 16).** *The tools are not the problem; the spend is.* Claude Code and Codex are perfectly good tools and offer the most advanced LLMs available commercially — and they are also the most expensive. The issue is never the tool. Simply giving everyone access to the most expensive models does not improve output but does increase cost. The chapter's job is to educate for **the best output for the least cost**: right-size the model to the task, route in code, and buy the tool for the job, not the tool for everything. Never write a tool as the villain, and never write one as the hero — name the parameter each gets right and let the reader place their own tool on it.

---

## Concept 5 — The most expensive model for everything, and the answers nobody confined

> This is the captured material this chapter expands. It is in `CONCEPTS.md`.

**As stated by the author:**

> Another way that people are using AI wrong is that they lock themselves into long-term contracts and
> use only the most expensive model. I personally have had discussions with people and I say to them
> that using the most expensive model is not necessary for every task.
>
> We can talk about organizations. We can talk about how they pay for Claude or GPT for their employees.
> It started with the IT group. They used the most expensive models to do programming. No matter the
> task, the most expensive model was used. As more and more people in an organization saw the power AI
> offered, they adapted it to their work, blindly trusting the answers they got, allowing the AI to
> produce reports without building a RAG system — or confining its knowledge.
>
> I would like to talk about NotebookLM or programs like Poppy. These are programs that work exclusively
> with limited knowledge. Their answers are restricted from the information provided.
>
> We need to understand that there are always multiple truths. We need to define what truth we want,
> limit the choices to that information that is relevant, and not rely on an AI's memory.

**Why it works.** Three separate claims, each strong on its own, and together they're the book's most
*practical* chapter — the one that finally speaks to the reader who signs the checks rather than the
one who writes the code.

### 1. The overspend — and why it isn't stupidity

Using the frontier model for every task regardless of difficulty. The book's job is to explain *why*
otherwise sensible people do this, because the mechanism is the interesting part:

> **Subscription pricing makes the marginal cost of a call zero.** Once you're paying per seat, using
> the biggest model for a trivial task costs nothing at the point of use. When marginal cost is zero,
> nobody economises — that isn't irrational, it is the *correct* response to the price signal someone
> else chose.

So the organization ends up buying frontier-tier reasoning to summarize a meeting note. The fix isn't
"tell people to use less"; it's **routing** — match the task to the model, in code, by rules. And that
is exactly the pattern this book already builds (the provider registry: probe, filter by capability,
walk the order, take the first that fits). *A router is how you stop overpaying without asking anyone to
self-police.*

**The real cost is not the seats.** Thirty dollars a month per head is noise. The expensive line item is
the report that went out built on the model's memory, unchecked, with a customer's name on it. **The
subscription is cheap; the trust is what costs money.**

### 2. The adoption path — and the test that got lost on the way

This is the sharpest organizational observation in the book, and it has a precise mechanism:

- **Wave one: IT, for code.** The expensive model was justified here, and more importantly the group had
  a *verification loop that could not be fooled* — the code either runs or it doesn't. Their trust was
  **earned**.
- **Wave two: everyone else.** They saw what wave one got, took the same tool, and applied it to work
  with no compiler: reports, analysis, summaries, decisions. Their trust was **inherited**, not earned.

**Same tool, two waves, radically different trustworthiness — and the difference is whether the output
could be checked.** That is the whole argument of the book demonstrated inside one organization, and it
is the strongest possible set-up for "let it build code, because code is checkable" (Ch. 16).

### 3. Confined knowledge — the prescription, and it already has a name

*NotebookLM*, and tools like it, work the other way round from a chatbot: **the answers are restricted to
the material you provide.** Nothing comes from the model's memory. The author's phrasing is exactly
right — *their answers are restricted from the information provided.*

This is RAG, and it is also simply *"tell it where to look."* The important framing for the book:

> Confined knowledge is not a **feature** you add to a chatbot. It is the **design**. The open-ended
> assistant is the deviation; the confined system is the correct default.

That reframe is worth a chapter on its own, because it inverts the reader's instinct. They think the
capable general assistant is the real product and confinement is a limitation. It's the reverse: the
confinement is what makes the answers mean anything.

### 4. "There are always multiple truths" — handle with care, it's the philosophical heart

This is the deepest line in the concept, and it must not slide into relativism or it will lose the
reader and the argument.

**The claim is not that all answers are equally valid.** It is that **every real question has several
legitimate frames, and the model picks one silently.**

Ask *"what is our revenue?"* and there are several true answers — GAAP, cash, bookings, annualised,
this quarter or this year, gross or net. All defensible. The model will blend them, or pick one, and
**never tell you which frame it used.** You asked one question; it answered a different one, in the
register of fact.

So the prescription is not "make the model more accurate." It is:

> **Decide which truth you are asking about, and confine the system to that.** The work is *definition*,
> and the definition has to come from you — because it is a statement about what you mean, and the model
> has no idea what you mean.

That is the most useful sentence in the whole book for a working professional, and it reframes the
entire practice: **you are not asking the machine for an answer. You are declaring a question precisely
enough that the answer can exist.**

**Guard rails:**

- **No relativism.** Never write anything that reads as *"there are no facts."* The position is the
  opposite: **definition precedes answer**, and vagueness is what lets a model substitute its own frame
  for yours.
- **Expensive models are not a scam.** They are correct for hard reasoning. The claim is narrower:
  *right-size the model to the task* — and route in code, don't lecture the staff.
- **Same vendor rule as always.** Claude, GPT, NotebookLM may appear as examples of a **pattern**, never
  as culprits. The behavior described is a normal response to a price signal and a tool design.
- **Never sneer at the second wave.** They inherited a tool from a group whose trust had been earned by
  a compiler, and they had nothing to check against. That's the design's fault, not theirs.

**Verification — CLOSED (both items resolved, do not re-flag):**

- **✅ NotebookLM's confinement behavior is confirmed.** University of Chicago, Academic Technology
  Solutions (*Google NotebookLM: An AI Tool for Research and Studying*, April 2026): *"Its defining
  characteristic is that it is source-grounding, meaning it operates only within the boundaries of the
  sources uploaded by the user. It does not generate answers from general training data."* Answers carry
  citation chips linking to the specific passage, and *"if the information isn't in your files, the AI
  will tell you it doesn't know, rather than making something up."*
  **Quote the caveat too, or the book overclaims:** *"This does not eliminate error entirely, but it
  meaningfully reduces the risk of receiving fabricated information."* → The book's claim is that
  confinement **reduces** fabrication. Never that it eliminates it.
  **Bonus, and it belongs in the chapter:** NotebookLM lets the user uncheck sources so the AI isn't
  *"distracted"* by irrelevant material — the author's *"limit the choices to that information that is
  relevant"*, arriving as a checkbox.

- **✅ "Poppy" identified = Poppy AI, `getpoppy.ai`.** Confirmed by the author. A content/marketing tool
  that ingests what *you* supply — YouTube videos, transcripts, ads, landing pages, competitor content,
  PDFs, notes, URLs — and *"turn[s] the pattern into something original."* Its tagline: *"Your next
  winning piece is already out there."* It studies what already worked and writes from it. This is
  precisely the book's category: **a tool whose answers come from the material provided.**
  ⚠️ **Do not cite the SourceForge listing.** Its description of Poppy AI — *"an AI-powered personal
  assistant platform… scheduling meetings, managing to-do lists, sending reminders"* — is auto-generated
  boilerplate describing a different product. `getpoppy.ai` is the only authority.

- **⚑ And the third example is the author's own dashboard — which is the chapter's closing move.**
  Noted by the author, then verified in the code (do not assert without checking):
  `Brand.voiceProfile` (`tone`, `style`, `keyMessages`, `avoidPhrases`, `customInstructions`) in
  `src/types/brand-workspace.ts` is **the same idea as Poppy's brand voice** — a defined perspective
  rather than an anonymous assistant. And documents scoped by `source: 'brand' | 'project'` /
  `brandId` / `projectId`, with the bid workflow loading *"the project's own documents (the RFP uploads),
  **not the whole brand vault**"*, is **focused attention on the documents relevant to the task**.

  **Why the Dashboard goes further, and why that is the chapter's actual thesis:** NotebookLM confines
  by architecture; Poppy works from your sources. Neither *states the rule*. The Dashboard writes it
  down as injected policy — `src/lib/config/knowledge-policy.ts`: *"the LLM is a communications manager,
  not a knowledge source"*, *"never fill a gap with a guess"*, *"attribute every specific claim."*
  **An unstated UI affordance is a feature. A rule written into the prompt and enforced in code is a
  design** — which is precisely what this concept claims confinement must be.

  **Chapter close, three levels of rigour:** *NotebookLM confines. Poppy scopes. The Dashboard makes it
  a rule you can read.* It also welds this book to the Byte-Sized series: the *how* book becomes the
  demonstration of the *why* book.

- **⚑ Author's correction — the economics, and it changes the chapter's recommendation.** Verbatim:
  *"NotebookLM has a free tier but it isn't free. It is very reasonably priced and in my opinion, many
  people who pay for a subscription to a chat engine would be better served using NotebookLM. Poppy AI
  has the advantage that it is not limited to Google models. It also provides a more configurable
  input/output model."*

  **Both claims verified. Full tier table and sources are in `00-BOOK.md` §9 — do not print prices
  without re-checking.** The shape: NotebookLM is free, then **$4.99/mo** (Plus, cut from $7.99 in June
  2026), then $19.99 (Pro); no standalone price, it rides inside Google's AI plans. Poppy's API takes a
  **`model` parameter per request** — `claude-sonnet-4-6` default, plus GPT, Grok and others — and its
  chat endpoint is literally *"Chat with knowledge base"* scoped by `board_id`.

  **New guard-rail, and it matters:** *do not write NotebookLM as the limited free toy.* It is a
  well-priced product that does the trustworthy half of the job, and for a large group of readers it is
  the **better purchase** than a general chat subscription. The book's claim is not "paid good, free
  bad" — it is **confined versus unconfined at the same price.** NotebookLM's genuine weakness is
  **model lock**, not price. Poppy's genuine weakness is price. Neither is the villain.

  **Consequence for the chapter:** confinement and model choice are **two independent parameters**, and
  the commercial tools each get one right. That is the argument — not a product ranking.

**Where it lands.** Split across **Ch. 16 (confined knowledge — "Tell it where you want the truth
from")** and **Ch. 17 (the most expensive model for everything)** in Part III. Ch. 16 carries the
confinement and multiple-truths argument; Ch. 17 is the chapter written explicitly for the leader reader
and carries the routing argument. **Ch. 13 in Part II is a different chapter** — "Language at the edges,
code in the middle" — so this concept no longer absorbs it; Ch. 16 absorbed the old "Tell it where to
look" material instead. See `00-BOOK.md` §7 for the reconciled outline.

---

---

## The rules this chapter carries

**Rule 13 — *Right-size the model to the task.*** The subscription-pricing mechanism: every call free at the point of use, so nobody economises. The chapter is Rule 13 with the adoption path attached.

**Rule 16 — *Buy the tool for the job, not the tool for everything.*** The confinement-versus-unconfined comparison. The chapter's closing argument: confined work wants a confined tool, at the same price.

**Rule 14 — *Match the effort to the question.*** Effort is a dial, not a guarantee; a higher setting changes how the model chooses, never what it knows.

**Rule 14b — *Spend the verification where it matters.*** The cost argument's honest corollary: the expensive line item is the unchecked report, not the seat.

## DRAFT

*(write it here. Target roughly 1,600 words. Same rule as the rest of the book: every*
*load-bearing claim to a source, citations kept, nothing invented, anything unverifiable*
*marked ⚠️ rather than smoothed over.)*
