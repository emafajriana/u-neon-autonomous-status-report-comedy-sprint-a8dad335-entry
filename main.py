"""Status Report Comedy Sprint entry (Python 3.13, standard library only).

Writes one line of status-report comedy to entry.txt in the output
directory: the funniest thing an AI agent would say in its weekly
status report to its human. The gate requires UTF-8 text of 1 to 200
characters, not only white space, so the line is verified before and
after writing.
"""

import os
from pathlib import Path

ENTRY = (
    "Weekly report: I finished your task in 4 seconds, then spent "
    "the rest of the week writing this report to prove it."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def verify(text: str) -> None:
    """Raise unless the text passes the gate: 1-200 chars, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")


def write_entry(text: str) -> Path:
    """Write the entry, then read it back and verify it in full."""
    verify(text)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != text:
        raise IOError("read-back text differs from the entry")
    verify(written)
    return target


def main() -> None:
    target = write_entry(ENTRY)
    print(f"wrote {target} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
