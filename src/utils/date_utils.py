from datetime import datetime, timedelta
from typing import Tuple


def parse_date(date_string: str, format_str: str = "%Y-%m-%d") -> datetime:
    """Parse a date string into a datetime object."""
    return datetime.strptime(date_string, format_str)


def calculate_date_range(period: str) -> Tuple[datetime, datetime]:
    """Calculate the date range (start and end dates) based on the specified period."""
    today = datetime.today()
    if period == "day":
        # start date will be the beginning of the before of current day (00:00:00), and end date will be the end of the current day (23:59:59)
        start_date = today.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = today.replace(hour=23, minute=59, second=59, microsecond=0)

    elif period == "week":
        # For week period, start date is the beginning of the current week (Monday 00:00:00),
        # and end date is the end of the current week (Sunday 23:59:59)
        start_date = today - timedelta(days=today.weekday())
        end_date = (
            start_date + timedelta(days=6) + timedelta(days=1) - timedelta(seconds=1)
        )
    elif period == "month":
        # For month period, start date is the beginning of the current month (1st day 00:00:00),
        # and end date is the end of the current month (last day 23:59:59)
        start_date = datetime(today.year, today.month, 1)
        next_month = start_date.replace(day=28) + timedelta(days=4)
        end_date = next_month - timedelta(days=next_month.day)
    elif period == "year":
        # For year period, start date is the beginning of the current year (Jan 1st 00:00:00),
        # and end date is the end of the current year (Dec 31st 23:59:59)
        start_date = datetime(today.year, 1, 1)
        end_date = start_date.replace(month=12, day=31)
    else:
        raise ValueError(
            "Invalid period. Please choose from 'day', 'week', 'month', or 'year'."
        )
    return start_date, end_date
