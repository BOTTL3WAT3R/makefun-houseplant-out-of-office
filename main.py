#!/usr/bin/env python3
"""The Houseplant Out-of-Office — writes one auto-reply line to /output/entry.txt.

The fern has not been watered since March, so it now answers email on
exactly the same schedule it gets watered: never. Anything urgent is
referred to the cactus, which cares even less.
"""
import os

ENTRY = (
    "Out of office. Last watered in March, so I reply on that schedule: "
    "never. Urgent? Ask the cactus. It cares even less."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
