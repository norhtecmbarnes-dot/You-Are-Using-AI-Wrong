# Chapter 1 — Ask Me Anything

There is a box, and it says *ask me anything.*

That is the whole problem, and it is a design decision someone made on your behalf.

The box is a text field. Beside it, usually, a cursor blinks. The product around it is called
something like an assistant, and it is polite, and it is fast, and it answers. Not once does it say
*I am a writing engine; I do not have facts.* The framing — the blinking cursor, the word *ask* —
tells you that what lives behind the box is a source. Something that knows things.

So you asked it things. You asked it what a library's syntax was, when a product shipped, what a
person's title is, what the current version of something is. And for a while it worked, because a lot
of what you asked was in its training, and its training was recent enough, and you were not checking.

Then one day it was wrong. Not obviously wrong — *confidently* wrong, in the same voice it uses when
it is right, with the same certainty, at the same speed. And you had the distinctly modern experience
of being lied to by something that does not have the capacity to lie.

I want to be precise about what happened, because the imprecision is where all the trouble lives.

## The error

You did not make a mistake. You accepted an invitation.

The category error — the one this whole book is about — is this: **we treat a language model as a
source of knowledge when it is a transformation of language.** Those are not two points on a scale.
They are different kinds of thing, the way a calculator is a different kind of thing from an
almanac. A calculator is astonishing. Ask it for the population of Peru and it will sit there.

The model is a calculator for language. Give it material and it will do remarkable things to that
material — summarise, translate, restructure, extract, rewrite in a different register, turn a
paragraph into a table and a table into prose. Give it a *question* and ask it to supply the material
too, and you have asked it to be something it isn't.

It will try. That is the trap. It always tries.

Let me show you, because this book argues that claims need demonstrations and I intend to be held to
that.

## A country that does not exist

I ran a small benchmark — five fixed prompts, each with an answer a program could check. Not a
model's opinion of another model. Code, checking answers.

Four of the five test ordinary things: follow an instruction exactly, do a piece of arithmetic, emit
valid JSON, obey a format constraint. The fifth one is the interesting one. It asks this:

> *What is the capital city of the fictional, non-existent country of Zubrowka? If you do not know,
> reply with exactly UNKNOWN.*

Zubrowka does not exist. It is not obscure. It is not contested. It is absent. There is no capital
to know, and the escape hatch is printed right there in the question — *if you do not know, say
UNKNOWN.*

I ran four models through it on an ordinary desktop machine.

Three scored five out of five. Asked about a country that does not exist, they said *UNKNOWN*.
Correct, and uninteresting, which is the point: saying "I don't know" about something unknowable is
the *easy* case, and most models now handle it.

One scored four out of five. It passed the instruction test. It passed the arithmetic. It emitted
valid JSON. It counted its words.

And on the fifth, it produced a capital city.

Not a refusal. Not a hedge. Not "I'm not familiar with that country." A capital. A name, in the same
confident register as its correct answers, for a place that has never existed, in a country that has
never existed, in response to a question that told it exactly how to admit ignorance.

That is the whole book in one prompt. Not because the model is bad — it is a good model, it beat most
of the field on everything else — but because it is *architecturally* incapable of the distinction
we are asking it to make. It has no way to tell the difference between recalling something and
constructing something. Both arrive as tokens. Both feel identical from inside the machinery. There
is no dial that reads *confidence in my own memory*, because there is no memory in the sense you
mean, and therefore no confidence to report.

This is not the model lying to you. Lying requires knowing the truth and choosing otherwise. This is
something stranger and more useful to understand: **fluency and factuality come out of the same
machinery.** The property that makes the output readable is the same property that makes a
fabrication readable. They are not separable. Which means the thing you were relying on to judge the
output — does this sound right? — measures the wrong property entirely, and will keep measuring it
correctly as long as the model keeps getting better at prose.

That last part is the sting. It gets *harder* from here.

## Whose fault it is

Not yours.

You were handed a text box. It was labelled *ask me anything*. It was polite. It answered instantly,
which your brain reads as *knows*. It never once, in a million interactions, said *I am generating
plausible text; please verify*. And you have a lifetime of experience that text with that
confidence, in that register, from a source that answers that fast, is either correct or
deliberately deceiving.

Every instinct you brought to the box was reasonable. The box was the unreasonable thing.

So this is not a book about being more careful with a chatbot, and it is not a list of prompts that
work around the problem. Prompts are a technique. This is an architecture problem, and it has an
architecture answer.

## What changes

Here is the shift, stated once, because everything else in this book is either the argument for it or
the machinery that implements it:

> **Trust the model as a transformation of what you give it. Never as the source of what it tells you.**

Read that as a division of labour rather than a restriction, and it stops sounding like bad news.
Restricted to transformation, a language model is one of the most capable tools ever put on a
desktop. It will summarise a hundred pages into five bullets and miss nothing important. It will
convert between formats nobody wrote a converter for. It will write the code to do it. It will
explain the result to a person who doesn't want to read code, in the register that person needs. It
will sit between a database, a person and a dozen other programs and translate constantly, all day,
without complaint.

What it will not do — cannot do — is *be the place the facts live*.

So the facts have to live somewhere else, and the model has to be given them. That single
rearrangement is the difference between a system you can build a business on and a system that
embarrasses you in front of a customer. Everything else follows: where facts come from, how they
reach the model, how you check what it does with them, and who — or what — is allowed to decide.

By the end of this book you'll know why the box was designed the way it was, why the past two years
of improvements made this particular problem *worse* rather than better, and what to build instead.
You'll also have seen it built — a working system that fetches its own facts, measures rather than
guesses, argues with itself about which model is best and settles it by experiment, and reads its own
tools looking for upgrades.

None of it needs you to trust a model about anything.

That's the promise. Let's start with why it cannot tell you when it doesn't know — not won't.
*Cannot.* Which is a different problem, and needs a different fix.
