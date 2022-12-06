"""
Advent of Code 2022
Day 5: Supply Stacks (Part Two)
"""

stacks = {}
with open("stacks.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        stack_index, crates = line.strip().split()
        stacks[stack_index] = list(crates)

with open("moves.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        splitted_line = line.strip().split()
        crates = int(splitted_line[1])
        from_stack = splitted_line[3]
        to_stack = splitted_line[5]
        temp_stack = []
        for _ in range(crates):
            temp_stack.append(stacks[from_stack].pop())
        for _ in range(crates):
            stacks[to_stack].append(temp_stack.pop())

top_crates = [stacks[str(i+1)][-1] for i in range(len(stacks.keys()))]
print(f"Top crates: {''.join(top_crates)}")
