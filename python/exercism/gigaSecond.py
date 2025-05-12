from datetime import datetime
import unittest

def add(moment):
    # 1sec = 1000msec
    # 1 giga-sec = 1_000_000_000 msec
    giga_second = 1_000
    return datetime.fromtimestamp((moment.timestamp() + 1_000_000_000))
















class GigasecondTest(unittest.TestCase):
    def test_date_only_specification_of_time(self):
        self.assertEqual(
            add(datetime(2011, 4, 25, 0, 0)), datetime(2043, 1, 1, 1, 46, 40)
        )
    def test_second_test_for_date_only_specification_of_time(self):
        self.assertEqual(
            add(datetime(1977, 6, 13, 0, 0)), datetime(2009, 2, 19, 1, 46, 40)
        )
    def test_third_test_for_date_only_specification_of_time(self):
        self.assertEqual(
            add(datetime(1959, 7, 19, 0, 0)), datetime(1991, 3, 27, 1, 46, 40)
        )
    def test_full_time_specified(self):
        self.assertEqual(
            add(datetime(2015, 1, 24, 22, 0)), datetime(2046, 10, 2, 23, 46, 40)
        )
    def test_full_time_with_day_roll_over(self):
        self.assertEqual(
            add(datetime(2015, 1, 24, 23, 59, 59)), datetime(2046, 10, 3, 1, 46, 39)
        )

uniTest = GigasecondTest()

uniTest.test_full_time_specified()