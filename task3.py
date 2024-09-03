import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    norm_phone = re.sub(r"[^0-9+]", "", phone_number)
    if not norm_phone.startswith("+"):
        if norm_phone.startswith("380"):
            norm_phone = "+" + norm_phone
        else: 
            norm_phone = "+38" + norm_phone
    return norm_phone

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)