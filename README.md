# PII Redaction Scanner

Find and redact common sensitive data patterns in local text files before sharing logs or reports.

## Job Signal

This repository is designed to demonstrate readiness for: **GRC analyst, security analyst, privacy/security engineer**.

## Problem

Analysts and instructors need a safe way to sanitize sample logs before sharing them.

## What It Shows

- Detect emails, US phone numbers, SSN-like values, and token-like secrets.
- Generate a count-by-type report without storing raw findings.
- Produce redacted text for classroom, ticket, or open-source examples.

## Quickstart

```bash
python -m pip install -e .
python -m unittest discover -s tests
python -m pii_redaction_scanner examples/sample.log --redact
```

## Portfolio Talking Points

- I can turn ambiguous security work into repeatable workflows.
- I can write clear documentation for analysts, engineers, and learners.
- I can build safe, local-first examples that avoid real secrets and third-party targets.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## Safety

This project is for defensive security, education, and local synthetic data only.
