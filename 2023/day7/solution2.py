from collections import Counter
from functools import cmp_to_key
import pdb

five_of_a_kind = lambda hand: len(hand) == 1
four_of_a_kind = lambda hand: len(hand) == 2 and 4 in hand.values()
full_house = lambda hand: len(hand) == 2 and 2 in hand.values() and 3 in hand.values()
three_of_a_kind = lambda hand: len(hand) == 3 and 3 in hand.values()
two_pairs = lambda hand: len(hand) == 3 and 2 in hand.values()
one_pair = lambda hand: len(hand) == 4 and 2 in hand.values()
high_card = lambda hand: len(hand) == 5

hash = [
    five_of_a_kind,
    four_of_a_kind,
    full_house,
    three_of_a_kind,
    two_pairs,
    one_pair,
    high_card,
]

strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def compare(hand1, hand2):
    for i, j in zip(hand1, hand2):
        if strength[i] > strength[j]:
            return True
        elif strength[i] < strength[j]:
            return False


def preprocess(hand):
    count = Counter(hand)
    max_val_letter = max(count.keys(), key=lambda x: 0 if x == "J" else count[x])
    return hand.replace("J", max_val_letter)


def comparator(hand_1, hand_2):
    h1 = hand_1.split(" ")[0]
    h2 = hand_2.split(" ")[0]

    hand1 = Counter(preprocess(h1))
    hand2 = Counter(preprocess(h2))

    for function in hash:
        if function(hand1) and function(hand2):
            return 1 if compare(h1, h2) else -1
        if function(hand1):
            return 1
        if function(hand2):
            return -1


input_file = open("input.txt", "r")
data = input_file.read().split("\n")[:-1]

sorted_data = sorted(data, key=cmp_to_key(comparator))
result = 0

for index, value in enumerate(sorted_data):
    result += (index + 1) * int(value.split(" ")[1])

print(result)
