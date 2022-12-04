"""
Advent of Code 2022
Day 3: Rucksack Reorganization (Part Two)
"""

from itertools import islice

def get_shared_item(rucksack_1, rucksack_2, rucksack_3):
    for item in rucksack_1:
        if (item in rucksack_2) and (item in rucksack_3):
            return item

def item_priority(item):
    if item.islower():
        return (ord(item) - ord('a')) + 1
    return (ord(item) - ord('A')) + 27

priorities_sum = 0
with open("input.txt", encoding='UTF-8') as input_file:
    while True:
        next_3_lines = list(islice(input_file, 3))
        if not next_3_lines:
            break
        rucksack_1 = next_3_lines[0].strip()
        rucksack_2 = next_3_lines[1].strip()
        rucksack_3 = next_3_lines[2].strip()
        shared_item = get_shared_item(rucksack_1, rucksack_2, rucksack_3)
        priorities_sum += item_priority(shared_item)
print(f"Sum of the priorities: {priorities_sum}")
