"""
Advent of Code 2022
Day 1: Calorie Counting (Part One)
"""

def update_most(most, elf_calories):
    if elf_calories > most:
        most = elf_calories
    return most

most_calories = 0
with open("input.txt", encoding='UTF-8') as input_file:
    current_elf_calories = 0
    for line in input_file:
        entry = line.strip()
        if entry == "":
            most_calories = update_most(most_calories, current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(entry)
    most_calories = update_most(most_calories, current_elf_calories)
print(f"Most calories: {most_calories}")
