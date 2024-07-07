from datetime import datetime


def get_upcoming_birthdays(users: dict) -> list:
    """Find users who have a birthday in the next 7 days"""

    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        today = datetime.today()

        current_year = today.year
        year_diff = current_year - birthday.year
        # find the nearest next birthday
        next_birthday = birthday.replace(year=birthday.year + year_diff).date()
        if next_birthday < today.date():
            next_birthday = next_birthday.replace(year=next_birthday.year + 1)

        birthday_diff = next_birthday - today.date()
        # skip user if the birthday is more than 7 days away
        if birthday_diff.days > 7:
            continue

        # if the birthday is on a day off, postpone the date to the next Monday
        if next_birthday.weekday() > 4:
            next_birthday = next_birthday.replace(day=next_birthday.day + 7 - next_birthday.weekday())

        result.append({"name": user["name"], "congratulation_date": next_birthday.strftime("%Y.%m.%d")})

    return result
