"""
Advent of Code 2022
Day 3: Rucksack Reorganization (Part One)
"""

def get_shared_item(compartment_1, compartment_2):
    for item in compartment_1:
        if item in compartment_2:
            return item

def item_priority(item):
    if item.islower():
        return (ord(item) - ord('a')) + 1
    return (ord(item) - ord('A')) + 27

priorities_sum = 0
with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        rucksack = line.strip()
        half_rucksack = int(len(rucksack)/2)
        compartment_1 = rucksack[:half_rucksack]
        compartment_2 = rucksack[half_rucksack:]
        shared_item = get_shared_item(compartment_1, compartment_2)
        priorities_sum += item_priority(shared_item)
print(f"Sum of the priorities: {priorities_sum}")
