from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PATTERNS = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone": re.compile(r"\b(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "token": re.compile(r"\b(?:api[_-]?key|token|secret)[=:]\s*[A-Za-z0-9_\-]{12,}\b", re.IGNORECASE),
}


def scan_text(text: str) -> dict[str, int]:
    return {name: len(pattern.findall(text)) for name, pattern in PATTERNS.items()}


def redact_text(text: str) -> str:
    redacted = text
    for name, pattern in PATTERNS.items():
        redacted = pattern.sub(f"[REDACTED_{name.upper()}]", redacted)
    return redacted


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scan and redact local text containing common PII patterns.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--redact", action="store_true", help="Print redacted text instead of JSON counts")
    args = parser.parse_args(argv)
    text = args.path.read_text(encoding="utf-8")
    if args.redact:
        print(redact_text(text), end="" if text.endswith("\n") else "\n")
    else:
        print(json.dumps(scan_text(text), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
