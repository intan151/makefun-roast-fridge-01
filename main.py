#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — make.fun #167.

Writes a single-line roast of the author's fridge to /output/entry.txt.
Deterministic: the same entry text on every run.
"""

import os

ENTRY = (
    "My fridge hums all night like it's warming up for a concert, "
    "but the only thing it ever serves is expired yogurt and disappointment."
)


def main() -> None:
    # Self-check gate: mirror the competition gate (RULES.txt) before writing.
    # Entry must be UTF-8 text of 1 to 200 characters, not only white space,
    # a single line, and must roast a fridge or a phone.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY, "entry is not UTF-8"
    assert "fridge" in ENTRY.lower() or "phone" in ENTRY.lower(), (
        "entry must roast a fridge or a phone"
    )
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
