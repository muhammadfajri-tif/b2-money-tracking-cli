import unittest
import sys

sys.path.append("src/")
from datetime import datetime, timedelta
from utils.date_utils import parse_date, calculate_date_range


class TestDateFunctions(unittest.TestCase):

    def test_parse_date(self):
        # Test parsing a date string
        date_string = "2022-03-01"
        expected_date = datetime(2022, 3, 1)
        self.assertEqual(parse_date(date_string), expected_date)

    def test_calculate_date_range_day(self):
        # Test calculating date range for 'day' period
        today = datetime.today()
        start_date, end_date = calculate_date_range("day")

        expected_start_date = today.replace(hour=0, minute=0, second=0, microsecond=0)
        expected_end_date = today.replace(hour=23, minute=59, second=59, microsecond=0)

        self.assertEqual(start_date, expected_start_date)
        self.assertEqual(end_date, expected_end_date)

    def test_calculate_date_range_week(self):
        # Test calculating date range for 'week' period
        today = datetime.today()
        start_date, end_date = calculate_date_range("week")

        expected_start_date = today - timedelta(days=today.weekday())
        expected_end_date = (
            expected_start_date
            + timedelta(days=6)
            + timedelta(days=1)
            - timedelta(seconds=1)
        )

        self.assertEqual(start_date, expected_start_date)
        self.assertEqual(end_date, expected_end_date)

    def test_calculate_date_range_month(self):
        # Test calculating date range for 'month' period
        today = datetime.today()
        start_date, end_date = calculate_date_range("month")

        expected_start_date = datetime(today.year, today.month, 1)
        next_month = expected_start_date.replace(day=28) + timedelta(days=4)
        expected_end_date = next_month - timedelta(days=next_month.day)

        self.assertEqual(start_date, expected_start_date)
        self.assertEqual(end_date, expected_end_date)

    def test_calculate_date_range_year(self):
        # Test calculating date range for 'year' period
        today = datetime.today()
        start_date, end_date = calculate_date_range("year")

        expected_start_date = datetime(today.year, 1, 1)
        expected_end_date = expected_start_date.replace(month=12, day=31)

        self.assertEqual(start_date, expected_start_date)
        self.assertEqual(end_date, expected_end_date)


if __name__ == "__main__":
    unittest.main()
