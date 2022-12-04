"""
Advent of Code 2022
Day 4: Camp Cleanup (Part One)
"""

fully_overlaps = 0
with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        assignment_1, assignment_2 = line.strip().split(',')
        assignment_1_start, assignment_1_end = map(int,assignment_1.split('-'))
        assignment_2_start, assignment_2_end = map(int,assignment_2.split('-'))
        if (((assignment_1_start >= assignment_2_start) and (assignment_1_end <= assignment_2_end)) or
            ((assignment_2_start >= assignment_1_start) and (assignment_2_end <= assignment_1_end))):
            fully_overlaps += 1
print(f"Fully overlaps: {fully_overlaps}")
