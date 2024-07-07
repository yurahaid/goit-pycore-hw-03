import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Generate sorted uniq list of random numbers between min and max"""

    # Validation the input data according to the requirements in the task and avoid a infinity loop
    if min < 1 or max > 1000 or (min > max) or (max - min < quantity - 1):
        return []

    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))

    return sorted(result)
