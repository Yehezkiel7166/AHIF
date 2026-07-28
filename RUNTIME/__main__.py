"""Command-line delegate to the canonical AHIF execution interface."""
import json
import sys
from pathlib import Path

from . import Framework


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 -m RUNTIME REQUEST.json", file=sys.stderr)
        return 2
    request = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(Framework.execute(request), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
