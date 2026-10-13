# Reader's Guide — Who This Book Is For

*(Front matter, between the Introduction and the Rules. The author's own text,
adopted verbatim. It consolidates 00-BOOK.md §4 ("Who it's for") and the
RULES.md "Two ways in" block into one reader-facing page: three readers, three
paths, three first moves. The Rules page itself stays as the rules page — this
guide is the front door to it, not a replacement.)*

---

This book is for the person who signs the checks, the person responsible for making the project work, and the person preparing to build an AI project for the first time.

You do not need to understand how a model is trained to make sound decisions about using one.

You do need to know what to trust, what to check, and when to stop.

The goal is practical: better results, securely, spending less money.

## If you sign the checks

This book helps you ask what the project actually delivers, how its answers are verified, and what mistakes will cost.

The subscription price is visible. The cost of trusting an unchecked answer often is not.

Start with the rules page. Then read the discussions of cost, verification, and accountability.

## If you are responsible for making it work

This book helps you turn an impressive demonstration into a dependable system.

A confined tool answers only from the material you supply. A contract defines what an acceptable answer must contain and checks it before anything acts on it. Routing sends each job to the smallest model capable of doing it reliably.

Start with the rules page. Then read the discussions of confinement, contracts, source quality, and freshness.

## If you have not built the project yet

This book gives you the warning before the mistake.

Start with the rules page, then the opening discussion of what models can and cannot be trusted to do. Learn the failure modes before committing money, data, or authority.

You do not need to begin with the most ambitious project.

Begin with one whose errors you can detect.

## How to Read the Rules

Read this page and you can act today. Read the book and you will understand why.

Each rule has three parts:

- **The assumption:** what we are tempted to believe.
- **The correction:** what is actually true.
- **The action:** what to do instead.

The rules are written to be repeated to a colleague without the book open. The explanations show the failure, explain its cause, and give you a practical response.

The language is plain. The argument is not simplified away.

You can read the book from beginning to end, or follow the path that matches your responsibility. All three paths begin with the same instruction:

> Point it at what you have, verify it against something outside itself, keep the judgment.

And keep Rule 2 in view:

> Confidence is not evidence.

That applies whether you are approving a budget, building a workflow, or reading the first answer from a new tool.

## Your First Move

### The signer: ask how success will be checked

Before approving the next stage, ask for a one-page description of the result the project must deliver, how that result will be verified, and who owns the consequences of an error.

Start with: the rules page, followed by the cost discussion.

Say this aloud:

> "Show me how we will know it worked—not just what the demonstration can do."

### The builder: make one task verifiable

Choose one bounded task. Identify its approved sources, define an acceptable output, and establish what happens when the system cannot meet those conditions.

Do this before expanding the workflow.

Start with: the rules page, followed by the discussions of confinement and contracts.

Say this aloud:

> "Before we act on the answer, we need a check outside the model."

### The first-time project owner: test the mistake, not just the success

Choose a low-consequence task whose answer you can independently check. Test missing information, stale information, and a wrong premise—not only the easy example.

Start with: the rules page, followed by the opening warnings.

Say this aloud:

> "What happens when it does not know?"

---

These are three routes through the same book, not three different sets of rules.

The signer needs to understand what deserves funding. The builder needs to understand what deserves deployment. The first-time project owner needs to understand what deserves trust.

None of them should have to take the model's word for it.

---

*Verification: the author's prose is adopted verbatim (1,089 words). No external
factual claims requiring a source — this is front matter (audience routing and
first moves), and its content is the routing already established in 00-BOOK.md
§4 and the RULES.md "Two ways in" block, here consolidated into one reader-facing
page. It references the rules page (RULES.md / control/references/the-rules.md),
which is published out of band and is not in the interior build (RULES.md is in
the build's SKIP list by design — the rules travel as their own document). The
guide tells the reader to "start with the rules page," which is the correct
instruction for that document. Placement: front matter, between the Introduction
and the first chapter; the Rules reference document sits alongside the book, not
inside it.*
