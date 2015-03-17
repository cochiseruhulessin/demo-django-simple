import time
import unittest

from demo.utils import DUPLICATE
from demo.utils import OK
from demo.utils import RATE_LIMIT
from demo.utils import rate_limit


class RateLimitTestCase(unittest.TestCase):
    """The rate limiting algorithm should limit based on:

    1. Interval.
    2. Hash of the content.
    """

    def test_rate_limit_limits_rate(self):
        checksum = 1
        last_checksum = 2
        last_timestamp = time.time() - 0.1
        timestamp, result = rate_limit(checksum, last_timestamp, last_checksum, 1.0)
        self.assertEqual(result, RATE_LIMIT)

    def test_rate_limit_limits_duplicate(self):
        checksum = 1
        last_checksum = 1
        last_timestamp = time.time() - 1.0
        timestamp, result = rate_limit(checksum, last_timestamp, last_checksum, 1.0)
        self.assertEqual(result, DUPLICATE)
