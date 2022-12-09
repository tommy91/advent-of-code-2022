"""
Advent of Code 2022
Day 8: Treetop Tree House (Part One)
"""

grid = []
with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        grid_row = [int(c) for c in line.strip()]
        grid.append(grid_row)

visible_trees = []
rows = len(grid)
columns = len(grid[0])

for i in range(rows):
    visible_trees.append([0] * columns)

# Left to right
for i, row in enumerate(grid):
    biggest_tree = -1
    for j, tree in enumerate(row):
        if tree > biggest_tree:
            visible_trees[i][j] = 1
            biggest_tree = tree

# Right to left
for i, row in enumerate(grid):
    biggest_tree = -1
    for j, tree in enumerate(reversed(row)):
        if tree > biggest_tree:
            visible_trees[i][columns - j - 1] = 1
            biggest_tree = tree

# Top to down
for j in range(columns):
    biggest_tree = -1
    for i in range(rows):
        if grid[i][j] > biggest_tree:
            visible_trees[i][j] = 1
            biggest_tree = grid[i][j]

# Down to top
for j in range(columns):
    biggest_tree = -1
    for i in range(rows):
        if grid[rows - i - 1][j] > biggest_tree:
            visible_trees[rows - i - 1][j] = 1
            biggest_tree = grid[rows - i - 1][j]

visible = 0
for row in visible_trees:
    for tree in row:
        visible += tree

print(f"Visible trees: {visible}")
