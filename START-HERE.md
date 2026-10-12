# Start here

**For the next session — human or assistant.** This file assumes you know nothing about this project. If
you are an assistant reading this cold: **everything you need is in this folder or one link away, and none of
it is in your training data.**

---

## What this is, in four lines

A book: ***You Are Using AI Wrong — And It Isn't Your Fault***, by Michael C. Barnes.
**Written *with* AI, not by it** — an open-source model on the author's own machine.
The method *is* the subject: the rules in this book are the rules the book was written under.
Licence: **code MIT, content CC BY-SA 4.0.**

## Where it is

    local      C:\ai\proposal genie\You-Are-Using-AI-Wrong\
    public     https://github.com/norhtecmbarnes-dot/You-Are-Using-AI-Wrong   (branch: master)

**Read these three, in this order. Then stop reading and run something.**

| file | what it gives you |
|---|---|
| `STATUS.md` | where the project actually stands, with counts |
| `WORKFLOW.md` | the seven states a chapter moves through, and the gate at each |
| `OPEN-ITEMS.md` | everything outstanding, written as questions the author can answer |

**Do not read `00-BOOK.md` first.** It is 100KB of master document. Read the three above, then use it as a
reference.

---

## Run these two commands

    python3 book-build/chapter-status.py          # what state is every chapter in, and what blocks it
    python3 book-build/build-interior.py         # render the book to DOCX + PDF

The first one is the answer to *"where are we?"* — trust it over any summary, including this file.
The second one rebuilds the reading copy and prints the real page numbers.

*(On the author's Windows machine the interpreter is
`%LOCALAPPDATA%\Temp\ytvenv\Scripts\python.exe`, and native tools need `C:/...` paths, not `/c/...` —
passing an MSYS path to native Python fails silently and prints the previous build's numbers.)*

---

## The rules of engagement

**The full contract is `AGENT-CONTRACT.md`. Read it. Do not let this file paraphrase it — a restatement drifts
from the thing it restates, which is the lesson this project keeps re-learning.**

Three things it will tell you, and they are the ones that matter from the first minute:

1. **Never supply a fact from your own knowledge.** Every load-bearing claim in this book traces to a source
   in `00-BOOK.md` §9. If you cannot find the source, say the claim is unsupported — **do not fix it quietly.**
2. **The author's own experience needs no source.** He was there. **What he cannot do is testify to a general
   rule** — *"this happened to me"* is testimony, *"this is what happens"* is a claim about the world, and it
   needs one. **He already draws this line correctly; follow his lead.**
3. **Leave the ⚠️ marks in place.** An unclosed warning is information. A smoothed-over one is a lie.

**And one working habit, learned the hard way: verify before you report.** Four defects were found in this
book's own files in a single session, and twice the *check* was wrong while the file was fine. If a number
looks convenient, re-derive it.

---

## ⚑ What to do first

**Gate 1, in one batch.** Twelve chapters already have a full spec and verified §9 evidence — **they are not
blocked on writing. They are blocked on one unanswered question each: *which rule does this chapter carry?***

    chapters 2, 3, 4, 5, 10, 12, 13, 14, 16, 22, 23, 24

**Ask the author the question for each one. One sentence each. Then those twelve are ready to draft.**

After that, the order is in `WORKFLOW.md`: draft those twelve, then the nine that have neither spec nor
evidence, then `Start here` last.

**And the fastest way to begin a session is one line:** *"read START-HERE.md and do what it says."*

---

## Mechanics that will otherwise cost you an hour

- **`gh` is not authenticated** and refuses to log in. Pushing works via the Windows Credential Manager
  entry for github.com. **The token is in the credential store — read it with `git credential fill`,
  never print it.**
- **Use the system git**, `C:\Program Files\Git\mingw64\bin\git.exe`. Hermes's bundled git credential
  helper hangs.
- **Commit with `--no-verify`** — the husky pre-commit hook is broken.
- **Always confirm with `git log --oneline -1` and `ls-remote`** that the push landed. `git push` has
  timed out mid-flight and still completed.
- **The build skips `RULES.md`, `CONCEPTS.md`, `00-BOOK.md`** and every file whose name marks it as
  scaffolding. Anything under `## DRAFT` in a skeleton **is prose** — author notes go *above* that line,
  never below it. A note placed below it once printed in the manuscript as though it were the chapter.
- **The shipped rule list is generated, not maintained:** run `book-build/make-rules-reference.py` after any
  edit to `RULES.md`, and copy the result to the installed skill. It exists in three places and they have
  already drifted to three different counts once.

---

## What not to do

- **Do not summarise the book back to him.** He wrote it.
- **Do not add a rule, chapter, or file without asking.** He has accepted several, and rejected none — but
  every one was his idea first. **The ten subrules added in one session were all his.**
- **Do not "improve" the prose.** The measured `de-ai-ify` score is 9.36/10 with **zero** AI patterns; the only
  thing its edits would change is adding contractions, which alters his voice.
- **Do not let a chapter ship with author notes in it.** The build now refuses to, and the refusal is the
  point.
