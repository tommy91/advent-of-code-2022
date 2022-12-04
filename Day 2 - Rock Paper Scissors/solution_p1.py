"""
Advent of Code 2022
Day 2: Rock Paper Scissors (Part One)
"""

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def round_points(move_p1, move_p2):
    my_move_points = {
        'X': 1, 
        'Y': 2,
        'Z': 3
    }
    game_result_points = {
        'w': 6,
        'd': 3,
        'l': 0
    }
    game_result = {
        'AX': 'd',
        'AY': 'w',
        'AZ': 'l',

        'BX': 'l',
        'BY': 'd',
        'BZ': 'w',

        'CX': 'w',
        'CY': 'l',
        'CZ': 'd',
    }
    return my_move_points[move_p2] + game_result_points[game_result[f"{move_p1}{move_p2}"]]

points = 0
with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        move_p1, move_p2 = line.strip().split()
        points += round_points(move_p1, move_p2)
print(f"Points: {points}")
