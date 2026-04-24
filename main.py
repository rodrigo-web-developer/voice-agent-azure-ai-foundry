from __future__ import annotations

import runpy
from pathlib import Path


def run() -> None:
    script_path = Path(__file__).with_name("english_friend.py")
    runpy.run_path(str(script_path), run_name="__main__")


if __name__ == "__main__":
    run()
