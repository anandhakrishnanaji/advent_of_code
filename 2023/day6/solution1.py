import re
from math import sqrt, pow, ceil, floor

TIME_REGEX_PATTERN = r"^Time:((\s+(\d+))+)$"
DISTANCE_REGEX_PATTERN = r"^Distance:(\s+(\d+))+$"


def get_number_list(pattern, string):
    return list(
        map(
            int,
            filter(
                lambda x: x.isdigit(),
                re.search(pattern, string).group(0).split(" "),
            ),
        )
    )


input_file = open("input.txt", "r")
data = input_file.read().split("\n")

time_list = get_number_list(TIME_REGEX_PATTERN, data[0])
distance_list = get_number_list(DISTANCE_REGEX_PATTERN, data[1])

product = 1

for time, distance in zip(time_list, distance_list):
    discriminator = pow(time, 2) - (4 * distance)
    num1 = ceil((time + sqrt(discriminator)) / 2 - 1)
    num2 = floor((time - sqrt(discriminator)) / 2 + 1)
    product *= num1 - num2 + 1

print(product)
