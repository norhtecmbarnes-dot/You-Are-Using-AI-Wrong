# Chapter 23 — Let it build code, because code is checkable

**STATUS: starting markdown. The plan spec and the verified evidence are below; expand it.**

---

## From the plan (00-BOOK.md section 7)

- Claim: code has a property prose never will — it either runs or it doesn't. Verifiable output is where
  the model's weakness stops mattering. *(Payoff of Ch. 17's two waves.)*
- Demo: a real bug caught by **looking at the bytes** — a payload that was JSON wearing an audio file's
  name — not by asking a model whether it looked right.
- Fix: prefer the model for work whose output can be tested. Trust the test, not the model.

### Part IV — The scaffold

---

## Evidence already verified for this chapter

*(from `00-BOOK.md` section 9 — the book's evidence register. Quoted as it stands,
including its own ⚠️ cautions. Nothing here needs re-verifying; the cautions*)
*are part of the material and must travel with it.*

- **The VocalLab bug** (Ch. 22) — a payload that was JSON wearing an audio file's name, caught by
  inspecting the bytes. Real.

- **The Alpha challenge** (Ch. 17) — five code-scored tests, ties to the incumbent. Real result.

---

## The rules this chapter carries

**Rule 15 — *Your first wave's trust may not transfer.* (primary).** Code is checkable — it runs or it doesn't — so verifiable output is where a model's weakness stops mattering. Rule 15 (find your test) aimed at the model's strongest output, with Rule 11b as the discipline.

**Rule 11b — *Ask it to be checkable, not impressive.* (carried).**

## DRAFT

Working software tells you the truth about itself, which is more than most answers manage.

Everything else a model produces asserts. A fluent paragraph claims a fact; a persuasive summary
claims to have weighed the evidence; an analysis claims a conclusion follows. Nothing in any of it
signals whether any of that holds. A program is different: it either runs or it throws. The deliverable
carries its own test, and the test is cheap. That asymmetry is the whole subject of this chapter, and
it changes where AI belongs in your work.

## The payload that lied about its own shape

The demonstration comes from my own project, and it is a single recorded run — it demonstrates the
mechanism, not a rate.[^1]

The system had asked for an audio file. What came back carried an audio file's name and an audio
file's extension, as far as the filename went. Nothing about the response's wording would have raised
an eyebrow — the model that produced it would have cheerfully explained what it had made. The file
was a lie told in eight characters, and the way it was caught was by **looking at the bytes**: the
first two were `{"`. A JSON document was wearing an audio file's name.

Notice what did not find the failure. Nobody asked the producing model whether it had done the job
right — the producer's opinion is exactly the thing this book teaches you not to buy. Nobody read a
fluent description of the output. The check that worked was the dumbest one available: open the
artifact and look at what is actually there.

That is the discipline the rest of this chapter argues for, and it is worth stating plainly: **the
artifact is the second opinion that cannot flatter you.** A model asked to review its own work will
produce confident agreement (Chapter 2). The bytes, the spreadsheet, the rendered page, the executed
test — these agree with you or they do not, and they have no training incentive to smooth it over.

## Code is the deliverable with a compiler

Chapter 16 told the story of the two waves. The first wave was the IT group, whose trust in AI was
earned: they wrote code, and code has a compiler — the group had a verification loop that could not
be fooled. The second wave inherited the tool for work with no compiler — reports, summaries,
analysis — and inherited the trust without the check. The book's whole cost argument lives in that
gap, and this chapter supplies the honest version of the fix.

The fix is not "stop using AI for prose," and it is not "code is the only safe output." The fix is to
know which kind of work you are handing over. **Where the deliverable can be executed, let the model
build it — and keep the execution in your hands.** Where it cannot be executed, everything this book
says about confinement, sources and judgement applies in full (Parts II and III). The mistake is not
the task; it is sending uncheckable work out with checkable-work confidence.

And the model's part is real. It can write the script, draft the query, generate the transformation,
assemble the report pipeline. The book never said otherwise — Chapter 15 and Chapter 17 are built on
models doing model-sized work. What the model cannot supply is the standard the work must meet, and
code is the one deliverable where the standard can be *run* rather than *described*.

## The Alpha challenge: measurement, not persuasion

The second demonstration is already in this book's record. Chapter 16's provider registry was not
built on trust, and it was not built on a model's ranking of itself — the author ran the Alpha
challenge: five fixed, code-scored tests, including a grounding test, with incumbent candidates
defending their position.[^2]

Three models scored perfectly. One was caught inventing — the grounding test asked for the capital
of a country that does not exist, and the fabrication was visible in the record. The incumbent
defended at one hundred percent. Ties held. Nobody was persuaded of anything; the measurement said
what it said, in code, and the promotion decision followed the scores.

That is the shape of every check worth having: a test written before the answer arrives, scored by
something that is not part of the conversation. A model judging another model's output is the trap
(Chapter 18's agents; Chapter 21's "you cannot ask a model who's best"). The compiler, the test
suite, the byte inspection — these are checkable judges, and the book's whole architecture leans on
them: contracts at the boundary (Chapter 14), measurement before promotion (Chapter 24's first
pillar), the recorded result instead of the explained result.

## What code does not excuse

One honest limit, or the rule overclaims. Code that runs is not code that is *right for the purpose*.
A script can execute cleanly and compute the wrong thing, because the specification was thin — and a
model will happily pass a shallow test. The test you write is the judge, which means the judge is
still yours: the requirements come from you (Chapter 14's contract), the brief from someone who has
done the work (Chapter 19). Code is checkable; *correctness to purpose* still lives with the human.
That is not a caveat against the rule. It is the rule being precise: the compiler settles **does it
run** — you settle **was it the job.**

And a single recorded run stays a single recorded run. The chapter's claim is the asymmetry —
checkable output beats asserted output — which needs no statistics to hold. Where you want a rate,
run the Alpha challenge again on your own tasks; the book's method is designed to be re-run, not
believed.

## What changes

It changes what you ask for. Where a working artefact is possible, ask for one: `write the query`,
not `explain how you would build the query`; `make the failing test pass`, not `tell me why the
test might fail`. Working artefacts can be inspected, run and re-run — and they turn every following
conversation into a check of something that exists.

It changes where you put the checks. Keep the tests where you can read them. Keep the acceptance
criteria in the contract, not in the model's memory (Chapter 6 — the conversation holds none of it).
When a produced artefact fails, the failure is information — Chapter 14's rule: do not quietly fix a
failed answer; record it.

And it changes the default posture toward AI work in your organization: the second wave was not
wrong to adopt the tool, it was wrong to adopt the tool's *confidence* for work with no check. Give
every AI task findable judge — a test, a run, an inspection — before you give it a budget. For
everything a model produces, the cheapest honest question is the same one: **what tells me this
worked?** For code, the answer exists. Ask for the deliverable that comes with it.

## Remember This

- Code either runs or it throws — the only deliverable in this book that grades itself.
- Inspect the artifact, never accept the producer's account of the artifact. The bytes caught what
  the flattery would have approved.
- Write the test before the answer arrives; a model can pass a shallow test, so the specification
  stays yours.
- Uncheckable work is not forbidden — it is governed by the rest of this book. Checkable work is
  governed by running it.

[^1]: The recorded bug: an output named and sized as an audio file whose first bytes were the JSON
    opener `{"` — caught on inspection, not on review. Project record; the run is the author's own
    (witness, per Rule 15b — presented as such, no rate claimed).
[^2]: The Alpha challenge: five code-scored tests with a grounding case — recorded in the project
    (`alpha.ts`, five BenchCase entries; `docs/SELF-EDUCATION.md`: "the grounding test caught one
    model fabricating; the incumbent defended at 100%"). The counts are the project's own record,
    offered as a demonstration of the method, not a benchmark.
