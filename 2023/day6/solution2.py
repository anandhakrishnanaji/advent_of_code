import re
from math import sqrt, pow, ceil, floor

TIME_REGEX_PATTERN = r"^Time:((\s+(\d+))+)$"
DISTANCE_REGEX_PATTERN = r"^Distance:(\s+(\d+))+$"


def get_number(pattern, string):
    return int(
        "".join(
            list(
                filter(
                    lambda x: x.isdigit(),
                    re.search(pattern, string).group(0).split(" "),
                )
            )
        )
    )


input_file = open("input.txt", "r")
data = input_file.read().split("\n")

time = get_number(TIME_REGEX_PATTERN, data[0])
distance = get_number(DISTANCE_REGEX_PATTERN, data[1])

discriminator = pow(time, 2) - (4 * distance)
num1 = ceil((time + sqrt(discriminator)) / 2 - 1)
num2 = floor((time - sqrt(discriminator)) / 2 + 1)
product = num1 - num2 + 1

print(product)
