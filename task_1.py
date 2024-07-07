import datetime


def get_days_from_today(input_date: str) -> int:
    """Calculate diff in days between today and input_date"""

    input_format = "%Y-%m-%d"
    try:
        input_datetime = datetime.datetime.strptime(input_date, input_format)
    except ValueError:
        print(f"invalid input {input_date}, supported format {input_format}")

        return 0

    today = datetime.datetime.today()
    diff = today - input_datetime

    return diff.days
