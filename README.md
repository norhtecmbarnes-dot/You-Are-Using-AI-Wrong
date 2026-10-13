# You Are Using AI Wrong — And It Isn't Your Fault

*by Michael C. Barnes*

> **A language model is trustworthy as a transformation of what you give it, and untrustworthy
> about anything it has to supply.**

Everything in this book either proves that sentence or builds from it.

**License:** content is **CC BY-SA 4.0**; the companion repositories are **MIT**. Code and content are
licensed separately and deliberately.

---

## What this repository is

The working repository for the book. It holds the argument, the evidence, the rule register, and the
machinery that builds the manuscript — so the project can be picked up from any machine.

**The manuscript is markdown. Everything else is generated from it.** Edit the markdown; rebuild.

---

## Layout

    You-Are-Using-AI-Wrong/
    ├── README.md                      this file
    ├── STATUS.md                      where the project is right now  <- read this second
    ├── 00-BOOK.md                     master document: thesis, tone rules, 28-chapter outline,
    │                                  and section 9, the evidence register
    ├── RULES.md                       the 21 rules + Rule 1b — the book's spine
    ├── AGENT-CONTRACT.md              the rules as an installable contract: a prompt,
    │                                  and the three parts that actually enforce anything
    ├── control/                       the installable skill
    │   ├── SKILL.md                   load this in an agent to operate under the rules
    │   └── references/the-rules.md    the full rule register, for the skill
    ├── CONCEPTS.md                    the concept register: the captured material
    ├── DASHBOARD-IMPLEMENTATION.md    every rule mapped to the code that implements it
    ├── LICENSE-CONTENT                CC BY-SA 4.0
    │
    ├── Preface-Why-This-Book-Exists.md
    ├── Introduction-AI-Is-Already-Smart-Enough.md
    ├── Chapter-01-Ask-Me-Anything.md
    ├── Chapter-DRAFT-The-8-Ball-Never-Fooled-Anyone.md      (this is Chapter 8)
    │
    ├── chapters/                      starting markdown, one file per chapter still to draft
    │   ├── Chapter-02-…
    │   └── … through Chapter-27
    │
    ├── book-build/                    the build: markdown -> .docx -> PDF. No LLM anywhere in it.
    │   ├── build-interior.py
    │   ├── README.md
    │   └── You-Are-Using-AI-Wrong-INTERIOR.{docx,pdf}
    │
    ├── samples/                       source material: the prior book, transcripts, threads
    └── youbooks-input/                a retired tool evaluation — see STATUS.md

---

## Building the book

Requires `python-docx` and `pypdf`, and LibreOffice for the PDF step.

```bash
cd "$LOCALAPPDATA/Temp"
"ytvenv/Scripts/python.exe" "C:/ai/proposal genie/You-Are-Using-AI-Wrong/book-build/build-interior.py"
```

Two things that will bite you:

- **Use a `C:/` native path.** MSYS paths like `/c/ai/...` are not translated for native Windows
  programs and fail with `can't open file`.
- **Use that interpreter.** `python-docx` and `pypdf` are installed in `$LOCALAPPDATA/Temp/ytvenv` —
  not in the system Python, and not in Hermes' own.

**Chapters are auto-discovered.** Dropping a chapter file into the book folder is the whole procedure.
The build finds it, orders it, and rebuilds in seconds.

---

## The rule the book was written under

**Every load-bearing claim goes to a source before it goes in the book. Nothing is asserted from
memory. Anything that cannot be verified is marked ⚠️ rather than smoothed over.**

That rule is why `00-BOOK.md` §9 exists. It is the evidence register, and it is the reason the
manuscript can be trusted — every claim in it either carries a citation or carries its own warning.

**The same rule applies to this repository's own documents.** If a claim appears here without a
source, that is a defect.

---

## Want to run your own system under these rules?

**The book is not only an argument. The controls are installable.**

    AGENT-CONTRACT.md       the contract in three parts, plus a prompt to paste into a system prompt
    control/SKILL.md        the same rules as a loadable skill, for an agent
    control/references/     the full 22-rule register the skill draws on

**Read `AGENT-CONTRACT.md` first, and read its first section before anything else**, because it says the
thing most people get wrong: **a prompt cannot enforce anything.** It can only ask. The rules that hold are
enforced by the human in the loop or by code, and the prompt exists to stop the model working against both.

**If you implement one thing from this book, implement the contract at the boundary** — parse and validate
before you act on anything a model produced, and reject rather than repair. A repaired payload is a guess
wearing the shape of data.

---

## Companion work

This book is the ***why***. *Building Your AI Dashboard* is the ***how*** — the same argument, built:
code that fetches its own facts, measures instead of guessing, and confines what the model may assert.

    PersonalAI-Dashboard    the system this book argues for
    Director-Dashboard      the sibling: local-first media generation
