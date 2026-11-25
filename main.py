#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line (under 200 characters) in which a home Wi-Fi router
excuses itself for dying at the climax of a movie, to /output/entry.txt.
"""

import os

ENTRY = "I peeked at the ending, gasped, and fainted. Even routers die of spoilers."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
