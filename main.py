"""make.fun entry: The Robot Vacuum's Best Excuse.

Writes the single-line entry to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

Deterministic, no network, no randomness. The file holds exactly the
LINE below: no trailing newline, one line, 1-140 Unicode code points.
"""

import os
from pathlib import Path

LINE = "I skipped the corner because my lidar has declared that sock load-bearing."


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
