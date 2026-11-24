"""Loading Screen Gold entry.

Writes one loading-screen tip (max 200 characters, single line) to
/output/entry.txt. Deterministic: byte-identical output on every run.
"""

import os

ENTRY = "Tip: your agent wrote 300 lines to avoid a 5-minute conversation with you \u2014 and honestly, you'd have done the same."

MAX_CHARS = 200


def validate_entry(text):
    """A loading-screen tip must be one line of 1-200 characters."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    return text


def run():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as handle:
        if handle.read() != ENTRY:
            raise RuntimeError("read-back mismatch")


if __name__ == "__main__":
    run()
