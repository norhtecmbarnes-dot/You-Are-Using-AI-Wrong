# Chapter 14 — Your plumbing is your ceiling

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: if facts must be injected, the quality of the system is the quality of its retrieval. A bigger
  model does not fix a stale fact.
- Demo: two systems, same model — one with no injection, one with live sources.
- Fix: spend on sources and plumbing before you spend on brains.

### Part III — What right looks like

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **⚑ The answer to no-provenance — RAG and brand voice.** *Requested by the author: "explain how this
  might work."* Full explanation in `CONCEPTS.md` Concept 6. **The principle, which is bigger than the
  chapter:** *nothing that matters should live only in the weights.* **Facts → RAG. Perspective → brand
  voice. Rules → policy files. Method → a hand-written brief.** Four moves, one idea: convert an inherited,
  uninspectable disposition into a declared, readable artifact. **And RAG's real gain is not accuracy — it
  is that the failure mode moves from invention (unprovable) to misreading (checkable).**

- **⚑ The Personal Dashboard is itself a worked example of the confinement principle — verified in the
  code, not asserted.** This is the strongest evidence in the book, because the author built it, and it
  makes the two books lock together: *Building Your AI Dashboard* becomes the *how* of the *why*.

  Two of the same concepts NotebookLM and Poppy rely on are already implemented, and the code is the
  proof:

  1. **A voice, for perspective.** `Brand.voiceProfile` in `src/types/brand-workspace.ts` carries `tone`,
     `style`, `keyMessages`, `avoidPhrases` and `customInstructions`, with a `BrandVoiceSelector.tsx`
     in the UI. This is Poppy's "Remember your brand" — the system speaks *as* a defined perspective
     rather than as an anonymous assistant.
  2. **Focused attention on specific documents and links.** Documents carry a
     `source: 'brand' | 'project'` and are scoped by `brandId` / `projectId`. The bid workflow loads
     *"the project's own documents (the RFP uploads), **not the whole brand vault**"*
     (`src/app/bid-workflow/page.tsx`) — retrieval narrowed to what is relevant to *this* task.
  3. **⚑ One project at a time — the unit of focus.** *Raised by the author: "we work on projects
     separately… a brand voice, and a project to focus on one proposal at a time."* Verified:
     `ChatRequest` requires **both `brandId` and `projectId`** — a chat cannot be opened without naming
     the project it belongs to. **The brand is what stays; the project is what changes.**

  **Which gives the trio its missing axis — the unit of confinement:**

  | Tool | The unit | The voice layer |
  |---|---|---|
  | **NotebookLM** | a **notebook** | — none |
  | **Poppy AI** | a **board** (`board_id`) | brand voice profile |
  | **Proposal Genie** | a **project** — one proposal at a time | `Brand.voiceProfile` |

  All three confine. Only one of them **names the unit as the design** — and it is the author's.

  **And the Dashboard's confinement is *auditable*, which neither commercial tool's is.** Each
  `ChatSession` records `brandDocumentsUsed`, `projectDocumentsUsed` and `totalTokensUsed`; each
  `ChatMessage` records `{ model, tokens, documentsReferenced }`. So it can answer after the fact:
  **which documents were in play, which model answered, and what it cost.** Confinement that leaves a
  receipt. *That is the strongest single thing in the system.*

  **And it goes one step further than either commercial tool, which is the real point of the chapter.**
  NotebookLM confines by architecture and stops there. Poppy works from your sources and stops there.
  The Dashboard **states the rule as policy and injects it into every call that can state a fact** —
  `src/lib/config/knowledge-policy.ts`, *"the LLM is a communications manager, not a knowledge source"*,
  with the instruction to *"never fill a gap with a guess"* and to *"attribute every specific claim."*
  Confinement as an unstated UI affordance is a feature. Confinement written down, in the prompt and
  enforced in code, is a **design** — which is exactly what §15's thesis claims.

  **Use it as the close of Ch. 16:** three tools, one principle, at three levels of rigour.
  *NotebookLM confines. Poppy scopes. The Dashboard makes it a rule you can read.*

- **NotebookLM is source-grounded by construction.** *"Its defining characteristic is that it is
  source-grounding, meaning it operates only within the boundaries of the sources uploaded by the user.
  It does not generate answers from general training data."* It answers with citation chips that link to
  the specific passage, and *"if the information isn't in your files, the AI will tell you it doesn't
  know, rather than making something up."* — University of Chicago, Academic Technology Solutions,
  *Google NotebookLM: An AI Tool for Research and Studying* (April 2026).
  **Carry the honest caveat with it:** *"This does not eliminate error entirely, but it meaningfully
  reduces the risk of receiving fabricated information."* The book claims confinement **reduces**
  fabrication. It must not claim confinement eliminates it.
  **The gift for Ch. 16:** NotebookLM lets the reader uncheck sources so the AI isn't *"distracted"* by
  irrelevant material. That is the author's *"limit the choices to that information that is relevant"* —
  the same idea arriving as a UI feature. Quote it.

---

## The rules this chapter carries

**Rule 1 — *It doesn't know things.* (primary).** If facts must be injected, the system's quality is its retrieval's quality. Rule 1's plumbing made explicit, with the three storage subrules: date it (12b), whitelist it (12c), meter the check (14b).

**Rule 12b — *Put an expiry date on knowledge.* (carried).**

**Rule 12c — *Whitelist the sources.* (carried).**

**Rule 14b — *Spend the verification where it matters.* (carried).**

## DRAFT

*(write it here. Target roughly 1,600 words. Every load-bearing claim to a source,*
*citations kept, nothing invented, anything unverifiable marked ⚠️ rather than*
*smoothed over — the same rule the rest of the book was written under.)*
