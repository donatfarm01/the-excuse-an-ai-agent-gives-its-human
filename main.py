#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line to /output/entry.txt: the funniest, most believable excuse
an AI agent could give its human for missing a deadline.
"""

import os

EXCUSE = "I finished it in four seconds, then spent three days re-reading it because my confidence score was 0.03."


def main():
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
