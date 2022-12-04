"""
Advent of Code 2022
Day 2: Rock Paper Scissors (Part One)
"""

# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def round_points(move_p1, result):
    my_move_points = {
        'R': 1, 
        'P': 2,
        'S': 3
    }
    game_result_points = {
        'Z': 6,
        'Y': 3,
        'X': 0
    }
    game_result = {
        'X': {'A': 'S', 'B': 'R', 'C': 'P'},
        'Y': {'A': 'R', 'B': 'P', 'C': 'S'},
        'Z': {'A': 'P', 'B': 'S', 'C': 'R'}
    }
    return my_move_points[game_result[result][move_p1]] + game_result_points[result]

points = 0
with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        move_p1, move_p2 = line.strip().split()
        points += round_points(move_p1, move_p2)
print(f"Points: {points}")
