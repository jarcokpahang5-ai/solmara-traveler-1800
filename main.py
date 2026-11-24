"""One Sentence for a Traveler from 1800 -- make.fun entry.

A single sentence of at most 200 characters that explains the modern
internet to someone who has just stepped out of the year 1800: every
letter and book ever made, gathered in one invisible library that
answers before you finish asking. The program checks the sentence,
prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "Imagine every letter ever written, every book ever printed, and "
    "every gossiping neighbour on Earth, all gathered into one great "
    "invisible library that answers before you finish asking."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank sentence within the limit.

    The sentence must also end with terminal punctuation and contain
    no doubled spaces, so a truncated or sloppily joined line is
    rejected instead of being submitted half-finished.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if "  " in line:
        raise ValueError("entry must not contain doubled spaces")
    if line[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the sentence and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed sentence is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
