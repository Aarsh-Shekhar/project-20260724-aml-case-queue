import unittest

from aml_case_queue.models import Record
from aml_case_queue.scoring import score_record


class DepthCheck5(unittest.TestCase):
    def test_005_backlog_triage(self):
        record = Record(id="case-005", exposure=90024, signal=0.736, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
