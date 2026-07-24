import unittest

from aml_case_queue.models import Record
from aml_case_queue.scoring import score_record


class DepthCheck20(unittest.TestCase):
    def test_020_threshold_calibration(self):
        record = Record(id="case-020", exposure=24140, signal=0.856, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
