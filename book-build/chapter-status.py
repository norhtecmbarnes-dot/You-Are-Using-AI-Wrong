#!/usr/bin/env python3
"""Report the state of every chapter, and what is blocking it.

WHY THIS EXISTS. On 12 October 2026 it turned out that 22 of 25 chapter skeletons still held the
placeholder in their "rules this chapter carries" section, that Chapter 15's evidence block had
gone stale without anyone noticing, and that a chapter the author designed had fallen out of the
outline entirely. None of that was visible, because nothing reported the state of a chapter.

So the workflow is a script, not a document. Rule 6 of the book this builds: put your rules in
code and config, where they persist.

    python3 book-build/chapter-status.py            # the table
    python3 book-build/chapter-status.py --blockers # only what is stuck, and why

THE FIVE STATES a chapter moves through, and the gate at each:

    PLANNED    in the outline (00-BOOK.md section 7), nothing else
    SPECCED    skeleton exists, with plan spec + concept + evidence + RULE MAPPING
    DRAFTED    prose exists under '## DRAFT'
    VERIFIED   every load-bearing claim has a dated section-9 entry
    BUILT      it renders into the interior PDF

The gate that matters most is PLANNED -> SPECCED, and it is the rule mapping. A chapter with no
rule mapping is a chapter nobody has asked "which rule does this carry?" - and that question is
what surfaces the staleness and the gaps.
"""

import os
import re
import sys
import glob

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(B, "00-BOOK.md")
CHAPTERS = os.path.join(B, "chapters")
BUILD = os.path.join(B, "book-build", "build-interior.py")

# All chapters live in chapters/ now - drafted chapters and skeletons alike.
# The mode (skeleton vs whole-file) is decided per file by inspect_mode() below.
FRONT_MATTER = ["Preface-Why-This-Book-Exists.md",
                "Introduction-AI-Is-Already-Smart-Enough.md"]


def words(s):
    return len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s))


def plan_chapters():
    """[(n, title)] from 00-BOOK.md SECTION 7 only.

    Restricted to that section on purpose: the register in section 9 also carries bold-numbered
    entries ("1. Dallas Fire-Rescue ..."), and an earlier version of this script read those as
    chapters. Twenty-two phantom chapters, and it looked like a finding.
    """
    try:
        doc = open(PLAN, encoding="utf-8").read()
    except OSError:
        return []
    m = re.search(r"(?s)^##\s*7\.(.*?)(?=^##\s*8\.)", doc, re.M)
    body = m.group(1) if m else ""
    out = []
    for mm in re.finditer(r"(?m)^\*\*(\d+)\.\s+([^*\n]+?)\*\*", body):
        out.append((mm.group(1), mm.group(2).strip()))
    return out


def inspect(path, is_skeleton):
    s = open(path, encoding="utf-8").read()
    d = {}
    if is_skeleton:
        d["concept"] = bool(re.search(r"Concept\s+\d+", s))
        d["evidence"] = "Nothing in the section-9 register bears directly" not in s and \
                        bool(re.search(r"section[- ]9|section 9", s))
        m = re.search(r"(?s)## The rules this chapter carries(.*?)(?=\n## )", s)
        body = (m.group(1).strip() if m else "")
        d["rules"] = bool(body) and "map the chapter to its rule numbers" not in body
        dm = re.search(r"(?s)^##\s+DRAFT\s*$(.*)", s, re.M)
        draft = (dm.group(1).strip() if dm else "")
        draft = re.sub(r"(?s)^\s*\*\(.*?\)\*", "", draft).strip()
        d["draft_words"] = words(draft)
        d["drafted"] = bool(draft) and not re.match(r"^\s*(?:\*\*|\*)?\s*(\u26a0|STATUS|NOTE|\()", draft)
    else:
        d["concept"] = d["evidence"] = d["rules"] = True
        d["draft_words"] = words(s)
        d["drafted"] = True
    return d


def state(d):
    if not d["drafted"]:
        if d.get("rules"):
            return "SPECCED"
        return "PLANNED"
    return "DRAFTED"


def main():
    rows = []

    for f in FRONT_MATTER:
        p = os.path.join(B, f)
        if os.path.exists(p):
            rows.append(("--", f.replace(".md", ""), "DRAFTED", words(open(p, encoding="utf-8").read()), True, True))

    for p in sorted(glob.glob(os.path.join(CHAPTERS, "*.md"))):
        f = os.path.basename(p)
        pm = re.match(r"Part-0*(\d+)-", f)
        if pm:
            # A part divider, not a chapter. Sort it just before the first chapter
            # of its part (key uses the part number as a float offset).
            d = inspect(p, False)
            rows.append((int(pm.group(1)) - 0.5, f.replace(".md", "")[:44], "PART", d["draft_words"], True, True))
            continue
        n = re.search(r"Chapter-(\d+)", f)
        with open(p, encoding="utf-8") as fh:
            head = fh.read()
        # A skeleton carries the working sections (plan / concept / evidence) and
        # writes prose under ## DRAFT. A drafted chapter is prose whole.
        is_skel = ("## From the plan" in head or "## Concept" in head
                   or "## Evidence already verified" in head)
        d = inspect(p, is_skel)
        rows.append((n.group(1) if n else "?", f.replace(".md", "")[:44], state(d), d["draft_words"], d["rules"], d["evidence"]))

    def sortkey(r):
        k = r[0]
        if k == "--":
            return (0, 0)
        if isinstance(k, (int, float)):
            return (1, k)
        return (2, 99)
    rows.sort(key=sortkey)

    total = sum(r[3] for r in rows)
    TARGET = 45000

    print("=" * 78)
    print("CHAPTER STATUS".ljust(50), "%d pieces" % len(rows))
    print("=" * 78)
    print("%-5s %-46s %-9s %6s %-6s %-6s" % ("ch", "file", "state", "words", "rules", "evid"))
    print("-" * 78)
    for n, name, st, w, ru, ev in rows:
        label = ("P%d" % (int(n) + 1)) if isinstance(n, float) else n
        print("%-5s %-46s %-9s %6s %-6s %-6s" % (
            label, name, st, w, "yes" if ru else "-", "yes" if ev else "-"))

    print("-" * 78)
    print("drafted prose: %d words = %.0f%% of %d" % (total, 100.0 * total / TARGET, TARGET))
    print("remaining:     %d words  (~%d chapters at 1,600)" % (TARGET - total, round((TARGET - total) / 1600.0)))
    print()

    plan = plan_chapters()
    have = set()
    for n, name, st, w, ru, ev in rows:
        if str(n).isdigit():
            have.add(int(n))
    missing = [(n, t) for n, t in plan if int(n) not in have]     # 1 vs 01: compare as ints
    print("in the outline with no file of its own: %d of %d" % (len(missing), len(plan)))
    for n, t in missing:
        print("   %-4s %s" % (n, t[:60]))
    print()

    blockers = [(n, name, st, w, ru, ev) for n, name, st, w, ru, ev in rows
                if st not in ("DRAFTED", "PART") or not ru]
    print("================================ BLOCKERS ================================")
    print("%d pieces are not finished. What each one needs:" % len(blockers))
    for n, name, st, w, ru, ev in blockers:
        need = []
        if st == "PLANNED":
            need.append("a skeleton")
        if not ru:
            need.append("RULE MAPPING  <-- the gate that matters")
        if not ev:
            need.append("section-9 evidence (or a note saying it carries none)")
        if st == "SPECCED":
            need.append("prose")
        print("   ch %-4s %-44s %s" % (n, name[:44], "; ".join(need) or "nothing known"))


if __name__ == "__main__":
    if "--blockers" in sys.argv:
        sys.argv = [sys.argv[0]]
    main()
