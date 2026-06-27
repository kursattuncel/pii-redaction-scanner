import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pii_redaction_scanner.cli import redact_text, scan_text


class PiiRedactionTests(unittest.TestCase):
    def test_counts_email_and_phone(self):
        counts = scan_text("Contact jane@example.com at 212-555-0188")
        self.assertEqual(counts["email"], 1)
        self.assertEqual(counts["phone"], 1)

    def test_redacts_secret(self):
        output = redact_text("api_key=abcDEF1234567890")
        self.assertNotIn("abcDEF", output)


if __name__ == "__main__":
    unittest.main()
