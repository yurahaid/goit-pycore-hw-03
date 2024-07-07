import re


def normalize_phone(phone_number: str) -> str:
    """Normalize phone number"""
    # find all allowed symbols
    founded_symbols = re.findall(r"(\+|\d+)", phone_number)
    normalized_phone = "".join(str(item) for item in founded_symbols)

    country_code = "+380"
    phone_length = 12

    # calculate amount of country code symbols that we should add to the beginning phone number
    country_code_slice_end = phone_length - len(normalized_phone) + 1

    return f"{country_code[:country_code_slice_end]}{normalized_phone}"
