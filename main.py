"""The Absurd Clause Contest — entry writer.

Writes one original absurd ToS clause (a single sentence, 1-200 chars)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure stdlib (os only). Deterministic: no randomness, no network, no secrets.
"""

import os

# The entry: one sentence, 177 characters, no trailing newline.
ENTRY = (
    "Your subscription, outstanding debts, and unfinished drafts shall, "
    "in the event of alien abduction, transfer to the abducting party, "
    "who shall inherit the billing cycle in full."
)


def clause():
    """Return the entry text."""
    return ENTRY


def validate(text):
    """Enforce the competition gate: 1-200 chars, single line, not blank."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return text


def write_entry(out_dir):
    """Write the validated clause to <out_dir>/entry.txt (no newline)."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate(clause()))
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
