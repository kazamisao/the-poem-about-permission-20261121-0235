#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. Deterministic, no network, standard library only.
"""

import os

# The turn: permission is not the cup changing hands — it is being asked
# where to set it down, instead of having the answer decided for you.
POEM = (
    "Take the cup, I said —\n"
    "you asked where to set it down.\n"
    "Nobody had ever waited\n"
    "for the shake in my hands\n"
    "to finish its sentence\n"
    "before telling me\n"
    "what I meant to spill."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
