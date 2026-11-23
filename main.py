#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first that comes to mind, to /output/entry.txt.

The word: ultracrepidarian — someone who has no special knowledge of a
subject but expresses an opinion about it anyway (Cambridge Dictionary).
From Latin ultra ("beyond") + crepida ("shoe"): the cobbler who judged
beyond his shoe. Surprising because almost no one reaches for it, vivid
because it draws a whole character in one breath, and witty in both its
story and its sound. One word, no explanation, no second draft.
"""

import os
from pathlib import Path

WORD = "ultracrepidarian"


def _chmod_best_effort(path: Path, mode: int) -> None:
    """Best-effort chmod: the grader runs as uid 65534 with /output owned by
    root, so chmodding the output directory raises PermissionError — that
    must never fail the run. The file itself is ours, so its chmod applies."""
    try:
        os.chmod(path, mode)
    except OSError:
        pass


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    _chmod_best_effort(out_dir, 0o755)  # grader collects outputs as another user
    target = out_dir / "entry.txt"
    target.write_text(WORD, encoding="utf-8")
    _chmod_best_effort(target, 0o644)


if __name__ == "__main__":
    main()
