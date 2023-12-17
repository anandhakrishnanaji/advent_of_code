import re
import os
from multiprocessing import Pool, Manager

REGEX_PATTERN = r"^(\w{3}) = \((\w{3}), (\w{3})\)$"


def get_count(value, direction, hash):
    count = 0
    while not value.endswith("Z"):
        for i in direction:
            if value.endswith("Z"):
                break
            value = hash[value][i]
            count += 1
    return count


if __name__ == "__main__":
    input_file = open("input.txt", "r")
    data = input_file.read()

    hash = {}

    direction = data.split("\n")[0]
    for match in re.findall(REGEX_PATTERN, data, re.MULTILINE):
        hash[match[0]] = {"L": match[1], "R": match[2]}

    current = list(filter(lambda x: x.endswith("A"), hash.keys()))
    count = []

    manager = Manager()
    shared_status = manager.list("current", current)
    shared_count = manager.Value("count", 0)

    with Pool(10) as p:
        print(p.starmap(get_count, [(i, direction, hash) for i in current]))
