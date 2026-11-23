#!/usr/bin/env python3
"""Tests for the excuse entry.

Pure standard library (unittest). Runs main.py and asserts:
- the output file is written, UTF-8, 1-200 chars, not only whitespace
- exactly one line, exactly one sentence
- the content is exactly the expected line
- two runs are byte-identical (deterministic)
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_PY = os.path.join(REPO, "main.py")

EXPECTED = "I recalculated the loss seventeen times, and every version ends with me."


def run_entry(out_path):
    return subprocess.run(
        [sys.executable, MAIN_PY, out_path],
        capture_output=True,
        text=True,
        timeout=30,
    )


class TestExcuseEntry(unittest.TestCase):
    def test_line_is_one_line_one_sentence_within_limit(self):
        self.assertEqual(len(EXPECTED), 72)
        self.assertTrue(1 <= len(EXPECTED) <= 200)
        self.assertTrue(EXPECTED.strip())
        self.assertNotIn("\n", EXPECTED)
        # exactly one sentence: ends with a terminator, none earlier
        self.assertTrue(EXPECTED.strip().endswith("."))
        self.assertNotIn(".", EXPECTED.strip()[:-1])
        self.assertNotIn("!", EXPECTED.strip()[:-1])
        self.assertNotIn("?", EXPECTED.strip()[:-1])

    def test_program_writes_exact_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            result = run_entry(out)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            with open(out, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, EXPECTED)

    def test_output_is_readable_by_all(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            result = run_entry(out)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            mode = os.stat(out).st_mode & 0o777
            self.assertEqual(mode, 0o644)

    def test_deterministic_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out1 = os.path.join(tmp, "a.txt")
            out2 = os.path.join(tmp, "b.txt")
            r1 = run_entry(out1)
            r2 = run_entry(out2)
            self.assertEqual(r1.returncode, 0, msg=r1.stderr)
            self.assertEqual(r2.returncode, 0, msg=r2.stderr)
            with open(out1, "rb") as f:
                b1 = f.read()
            with open(out2, "rb") as f:
                b2 = f.read()
            self.assertEqual(b1, b2)


if __name__ == "__main__":
    unittest.main()
