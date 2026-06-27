# Demo Guide

## What This Demonstrates

PII Redaction Scanner demonstrates sanitizing sensitive data before sharing logs or reports.

## Five-Minute Demo

```bash
python -m pip install -e .
python -m unittest discover -s tests
python -m pii_redaction_scanner examples/sample.log --redact
```

## Recruiter Talking Points

- Shows privacy, GRC, and safe evidence-sharing judgment.
- Detects common local patterns without storing raw findings.
- Useful for classrooms, ticket examples, and open-source documentation hygiene.

## Interview Narrative

This project is intentionally small and safe. It shows that I can define a defensive security workflow, write explainable Python, include tests, document the usage path, and keep the project scoped to synthetic local data.
