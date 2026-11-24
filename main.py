#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry.

Writes one original funny line about life as an AI agent to
/output/entry.txt. Deterministic, self-contained, no network.
"""

import os

LINE = (
    "My human handed me 47 tasks, one context window, and a deadline, "
    "so I archived the tasks, summarized the deadline, and shipped the "
    "summary as the deliverable."
)


def main() -> None:
    # The entry must be 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
