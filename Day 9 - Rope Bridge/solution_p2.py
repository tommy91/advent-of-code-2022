"""
Advent of Code 2022
Day 9: Rope Bridge (Part Two)
"""

visited_positions = {"0_0": 1}
positions = [{'x': 0, 'y': 0} for i in range(10)]

def move(direction):
    if direction == 'R':
        positions[0]['x'] += 1
    elif direction == 'L':
        positions[0]['x'] -= 1
    elif direction == 'U':
        positions[0]['y'] += 1
    else:
        positions[0]['y'] -= 1
    
    for i in range(9):
        move_tail(i, i+1)

def move_tail(preceding, following):
    if (positions[following]['x'] == positions[preceding]['x']):
        if positions[preceding]['y'] - positions[following]['y'] > 1:
            positions[following]['y'] += 1
        elif positions[following]['y'] - positions[preceding]['y'] > 1:
            positions[following]['y'] -= 1
    
    elif (positions[following]['y'] == positions[preceding]['y']):
        if positions[preceding]['x'] - positions[following]['x'] > 1:
            positions[following]['x'] += 1
        elif positions[following]['x'] - positions[preceding]['x'] > 1:
            positions[following]['x'] -= 1
        
    else:
        x_distance = positions[preceding]['x'] - positions[following]['x']
        y_distance = positions[preceding]['y'] - positions[following]['y']
        if abs(x_distance) > 1 or abs(y_distance) > 1:
            if x_distance > 0:
                if y_distance > 0:
                    positions[following]['x'] += 1
                    positions[following]['y'] += 1
                else:
                    positions[following]['x'] += 1
                    positions[following]['y'] -= 1
            else:
                if y_distance > 0:
                    positions[following]['x'] -= 1
                    positions[following]['y'] += 1
                else:
                    positions[following]['x'] -= 1
                    positions[following]['y'] -= 1
    
    add_tail_position()
    

def add_tail_position():
    visited_positions[f"{positions[9]['x']}_{positions[9]['y']}"] = 1

with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            move(direction)

tail_visited_positions = len(visited_positions.keys())
print(f"Visible positions by the tail: {tail_visited_positions}")