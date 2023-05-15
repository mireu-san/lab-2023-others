import re

phone_regex = re.compile(r"0\d{1,2}[-,. ]?\d{3,4}[-,. ]?\d{4}.?")

for phone_number in phone_regex.findall(
    "010-9091-5491, 010-5043-2901, 010-5050-40409, 010 2913 3132, 01019133829, 064-721-3213, 010.1913.3829"
):
    print(phone_number)
