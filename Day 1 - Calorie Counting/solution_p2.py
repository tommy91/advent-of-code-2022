"""
Advent of Code 2022
Day 1: Calorie Counting (Part Two)
"""

def update_top_3(top_3, current):
    if current > top_3[2]:
        if current > top_3[1]:
            if current > top_3[0]:
                top_3 = [current] + top_3[:2]
            else:
                top_3 = [top_3[0], current, top_3[1]]
        else:
            top_3[2] = current
    return top_3

top_3_elves = [0, 0, 0]
with open("input.txt", encoding='UTF-8') as input_file:
    current_elf_calories = 0
    for line in input_file:
        entry = line.strip()
        if entry == "":
            top_3_elves = update_top_3(top_3_elves, current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(entry)
    top_3_elves = update_top_3(top_3_elves, current_elf_calories)
print(f"Top 3 elves calories: {sum(top_3_elves)}")
