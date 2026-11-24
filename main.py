"""One-Line AI Excuse for Breaking Production.

Reads the excuse from entry.txt and prints it.
"""

from pathlib import Path

MAX_CHARS = 280


def load_excuse() -> str:
    path = Path(__file__).with_name("entry.txt")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty")
    if "\n" in text:
        raise ValueError("the excuse must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"the excuse is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    print(load_excuse())


if __name__ == "__main__":
    main()
