
""" normalize phone numbers according to standardt"""


import re


def normalize_phone(phone_number: str) -> str:
    pattern = r"\+|\d+"
    matches = re.findall(pattern, phone_number)
    norm_phone_number = "".join(matches)

    if not norm_phone_number.startswith("+38"):
        if norm_phone_number.startswith("38"):
            norm_phone_number = "+" + norm_phone_number
        elif norm_phone_number.startswith("8"):
            norm_phone_number = "+3" + norm_phone_number
        elif norm_phone_number.startswith("0"):
            norm_phone_number = "+38" + norm_phone_number
        else: 
            norm_phone_number = "+380" + norm_phone_number[-9:]

    return norm_phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)