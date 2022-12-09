"""
Advent of Code 2022
Day 8: Treetop Tree House (Part Two)
"""

def first_occurrence_ge(value, considered_list):
    for pos, element in enumerate(considered_list, start=1):
        if element >= value:
            return pos 
    return len(considered_list)

grid = []
with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        grid_row = [int(c) for c in line.strip()]
        grid.append(grid_row)

scenic_scores = []
for i, row in enumerate(grid):
    scenic_scores_row = []
    for j, tree in enumerate(row):
        score_right = first_occurrence_ge(tree, row[j+1:])
        score_left = first_occurrence_ge(tree, list(reversed(row[:j])))
        score_up = first_occurrence_ge(tree, list(reversed([grid[r][j] for r in range(i)])))
        score_down = first_occurrence_ge(tree, [grid[r][j] for r in range(i+1, len(grid))])
        scenic_scores_row.append(score_right * score_left * score_up * score_down)
    scenic_scores.append(scenic_scores_row)

highest_scenic_score = 0
for i, row in enumerate(grid):
    for j, _ in enumerate(row):
        if scenic_scores[i][j] > highest_scenic_score:
            highest_scenic_score = scenic_scores[i][j]

print(f"Highest scenic score: {highest_scenic_score}")
