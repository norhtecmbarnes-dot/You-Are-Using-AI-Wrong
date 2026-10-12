# Chapter 6 — The clock is always running

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: knowledge decays, and not at one rate. Versioned, priced, dated and social facts rot in weeks;
  methods last years.
- Demo: a hardcoded leaderboard, months old, presented as current truth — and the same list fetched live.
- Fix: the decay rate tells you what must be fetched and what a model may hold structurally.

---

## Evidence

**This chapter's material is now Concept 13 in `CONCEPTS.md`** — *The clock is always running*. Read that
before drafting; it carries the claim, the rate taxonomy and the demonstration.

⚠️ **The plan's demonstration — "a hardcoded leaderboard, months old, presented as current truth, and the
same list fetched live" — has not been built yet.** Either build it (it is small, and it is the kind of
demonstration this book insists on), or replace it with the examples below, which are already verified.

**The demonstration is available from this book's own working material.** Every one of these happened while
the book was being written, which makes the chapter self-evidencing:

- **NotebookLM Plus was cut from $7.99 to $4.99 on 8 June 2026** — a *priced* fact that moved mid-project.
- **The product was renamed "Gemini Notebook" in July 2026** — a *versioned* fact; the register already carries
  both names.
- **OpenClaw's disclosed CVEs: 138+ by April 2026, ~45 more on 30 June 2026** — a *live* fact that grew while
  the notes sat on disk.
- **And the register warned about itself:** *"Re-check the CVE and cost figures before print — they date
  fastest of anything in this book."*

⚠️ **Two of these need re-verification before print, per Rule 1b and the chapter's own argument.** A chapter
about facts expiring cannot be the one place that treats its own facts as permanent.

---

## The rules this chapter carries

**Rule 2 — *Confidence is not evidence.*** The chapter is Rule 2 with a clock attached: the register is as
confident about a dead fact as a live one.

**Rule 5 — *It cannot tell you it's unsure.*** The chapter's hinge. *"A memory and an invention arrive through the
same door, in the same voice"* — and the SAP case is the same sentence with the nouns swapped.

**Rule 12b — *Put an expiry date on knowledge.*** The chapter's remedy, and the reason the milk analogy is exact.

**Rule 14b — *Spend the verification where it matters.*** Costing data is where the meter belongs.

## DRAFT

Ask who the president is and the answer is good for four years, or eight. Ask who is leading the World Series and
the answer is good until tomorrow night. Both are facts. Both are the kind of thing you would reasonably put to a
system. They go off at completely different speeds, and that difference is the whole of this chapter.

**A language model is frozen at a moment it cannot see.** Everything it knows was learned before a date that is not
in its output, is not available to it, and does not announce itself. This is not a flaw a larger model corrects. It
is what the thing is — a function fitted to a corpus that stopped growing on a particular day. Ask it about the day
after, and it will answer anyway, in exactly the same register it uses for everything else.

**And retrieval does not fix this. It relocates it.**

This is the part that gets missed, and it is the part worth the chapter. A system that answers from documents you
supply is more trustworthy about *where the answer came from*. It is exactly as exposed to the answer having gone
off. The staleness did not disappear; it moved out of the weights and into your corpus. **Your corpus ages too.**
Retrieval cures provenance. It does not cure time, and those were never the same problem.

**So "is the model current?" is not one question.** It is six, and they have different answers:

    structural    years            a mechanism, a method, a concept         safe to hold
    dated         2-8 years        who holds an office, then it moves       stamp it
    versioned     weeks to months  an API, a screen, a product name         never hold it
    priced        months           a subscription tier, a rate              never hold it
    live          minutes to days  a score, a price, a position             fetch at use
    social        weeks            who is leading, what people think        fetch, expect movement

The rate is a property of the claim, not of the pipeline. **That is the useful part: the class of the fact tells you
whether the model may hold it or whether your system has to go and get it.**

**And the failure is silent.** A stale fact is not a different shape from a fresh one. Same fluent register. Same
confident construction. There is no field on it that says *this died in March*. **Nothing announces that it has gone
off.** That is Rule 2 with the clock attached — confidence is what it was trained to produce, and it is identical
whether the answer is current or two years dead.

**Which is why the expiry date has to be written down.**

Milk carries a date on the carton, and you throw it out on that date. **The model's knowledge is the one container
with no date printed on it** — so the date has to be added by whoever fills the container. That is you.

**And where the change date is known, you already have it.** An insurance policy renews on a given date; the premium
cannot change before that date and is dead after it. Writing *"premiums last about six months"* would be strictly
worse than writing down the renewal date already sitting in your files. **Estimating an expiry you could have known
is not caution. It is the error this book is about, wearing a new hat.**

**This book is not exempt from this, and its own working notes prove it.**

While this manuscript was being written, facts it depends on moved:

- **NotebookLM Plus was cut from $7.99 to $4.99 on 8 June 2026.** A *priced* fact, in a book that discusses the tool.
- **The product was renamed "Gemini Notebook" in July 2026.** A *versioned* fact. The notes carried both names for
  weeks, because nobody had gone back and retired the old one.
- **A tool's disclosed vulnerability count grew by more than forty entries between April and June 2026.** A *live*
  fact, changing while the file sat on disk.

**And the register holding those facts warned about itself, in writing:** *re-check the cost and vulnerability
figures before print — they date fastest of anything in this book.*

**That is the argument demonstrating itself.** A chapter about facts expiring, written in a file whose own facts
expired mid-draft. Three of them. And notice what makes that recoverable rather than fatal: **each one carries the
date it was true, and each one is written down where the next person will see it.** One line per fact. That is the
whole remedy, and it is not expensive — which is the point.

⚠️ **And a caution that belongs here rather than in a footnote:** the three figures above will be wrong by the time
you read them. **That is not a defect in the chapter. That is the chapter.** If they were still correct, the
argument would have nothing to stand on.

**⚑ I watched this happen from inside, and it cost me money.**

For several years I managed U.S. sales for a large company. **My bonus was based on my profit margin** — so the cost
of the goods I sold was not an abstraction to me. It was my pay.

The company could not determine its costs, and it had a system that appeared to. The same product carried more than
one price. A cost depended on when it had been purchased, from whom, and on other factors — so a cost was not one
number but a history, and the history had been loaded into a system that displayed it as a figure. **Margins were
computed from it. Quotes were computed from it. My bonus was computed from it.** All of it against costing data that
nobody had verified.

When I went and looked at the actual costs myself — not the report, the underlying numbers — I found out where some
of them came from. **One of the program managers had guessed.** He could not determine the cost, the field required
a value, and so he supplied a value.

**He was not lazy and he was not lying.** He was in a workflow with one box for a number and no box for *I don't
know*. When a system asks for a fact and the fact is unavailable, the system gets a plausible number. **The
alternative to a wrong number was an empty field, and empty was not an option the process offered.**

**And here is the part this book is about.** A guessed cost and a measured cost look identical. Both are a figure in
a field. Both are formatted to two decimals. Neither carries where it came from, and neither carries an error bar.
**A memory and an invention arrive through the same door, in the same voice — and a measurement and a guess arrive
through the same field, in the same format.** There is no dial for doubt to read.

The system was not lying to the company. **It was reporting what it had, and what it had was partly invented, and
nothing in it could tell the difference.** That is the same sentence this book has been using about language
models, and nobody had to install one for it to collect a large company's money.

**So what this chapter asks for is not "get better data." It is: spend the tokens.**

A costing figure is critical. Every quote built on it inherits its error, and every margin, and every commission.
**That is exactly the kind of fact worth the tokens to check** — not because checking is free, but because the
alternative is a number nobody can stand behind, used to price work and pay people.

    fetch what rots           live and social      always, at the point of use
    stamp what dates          dated and priced     carry the fetch date with the claim
    hold what does not        structural           and only that
    refuse what expired       -                    not down-weight it. Refuse it.
    verify what is critical   -                    and let the cheap ones ride

**A number without a date is not a weaker fact. It is an unknown one wearing the costume of a known one.** And a
system that cannot tell a known from an unknown will price work, quote customers and pay people on the difference.

**The clock is always running.** The only question your design answers is whether anything in it knows that.
