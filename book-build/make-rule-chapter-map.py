#!/usr/bin/env python3
"""Generate book-build/rule-chapter-map.csv from the chapter skeletons.

WHY THIS EXISTS. On 12 October 2026 the rule-to-chapter mapping lived only in the
"rules this chapter carries" section of each skeleton in chapters/. 21 of 25 held
the placeholder, and nothing reported the state of the map - the same defect as
the rules reference: one fact, several copies, nothing to compare them.

The book's own discipline (WORKFLOW.md, gate 1) requires every chapter to name
the rule it carries before it can be drafted. This script makes that map a
derived artifact, generated from the skeletons, so the state of the mapping is
one command away and cannot silently drift.

    python3 book-build/make-rule-chapter-map.py

It writes only the CSV below. It refuses to write if a skeleton's mapping
section is missing or still holds the placeholder - a broken source cannot
silently produce a clean-looking map.

The CSV is the working index. The skeletons remain the source of truth; this
is the derived view. If they disagree, trust the skeletons and re-run.

NOTE: the CSV covers chapters 2-27 (the skeletons). The drafted root chapters
(1, 8) and front matter carry their rules inline and are not in this file.
"""

import csv
import os
import re
import sys

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(B, "chapters")
DST = os.path.join(B, "book-build", "rule-chapter-map.csv")

PLACEHOLDER = "map the chapter to its rule numbers"


def main():
    rows = []
    broken = []
    for fname in sorted(os.listdir(CH)):
        m = re.match(r"Chapter-(\d+)-(.+)\.md$", fname)
        if not m:
            continue
        ch = int(m.group(1))
        title = m.group(2).replace("-", " ")
        with open(os.path.join(CH, fname), encoding="utf-8") as f:
            s = f.read()
        mm = re.search(r"(?s)## The rules this chapter carries(.*?)(?=\n## )", s)
        body = (mm.group(1).strip() if mm else "")
        if not body or PLACEHOLDER in body:
            broken.append((ch, fname))
            continue
        rules = list(dict.fromkeys(re.findall(r"Rule (\d+[a-z]?)", body)))
        rows.append((ch, title, rules, fname))

    if broken:
        for ch, fname in broken:
            sys.stderr.write("placeholder still in: ch %02d  %s\n" % (ch, fname))
        sys.exit("refusing to write: %d skeleton(s) still hold the placeholder - "
                 "fill the mapping first, then re-run" % len(broken))

    rows.sort()
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["chapter", "title", "status", "primary_rule",
                    "rules_carried", "source_file"])
        for ch, title, rules, fname in rows:
            w.writerow([ch, title, "MAPPED", rules[0] if rules else "",
                        ";".join(rules), "chapters/" + fname])

    # coverage check against RULES.md
    with open(os.path.join(B, "RULES.md"), encoding="utf-8") as f:
        defined = re.findall(r"^\*\*(\d+[a-z]?)\.", f.read(), re.M)
    carried = set()
    for r in rows:
        carried.update(r[2])
    missing = [r for r in defined if r not in carried]

    print("wrote %s" % DST)
    print("   chapters mapped: %d" % len(rows))
    print("   rules defined:   %d" % len(defined))
    print("   rules carried:   %d" % len(carried))
    if missing:
        print("   NOT carried:     %s" % ", ".join(missing))
        sys.exit(1)
    print("   coverage:        every rule has a chapter")


if __name__ == "__main__":
    main()
