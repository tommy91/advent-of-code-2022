"""
Advent of Code 2022
Day 9: Rope Bridge (Part One)
"""

visited_positions = {"0_0": 1}
head_pos = {'x': 0, 'y': 0}
tail_pos = {'x': 0, 'y': 0}

def move(direction):
    if direction == 'R':
        head_pos['x'] += 1
    elif direction == 'L':
        head_pos['x'] -= 1
    elif direction == 'U':
        head_pos['y'] += 1
    else:
        head_pos['y'] -= 1
    
    if (tail_pos['x'] == head_pos['x']):
        if head_pos['y'] - tail_pos['y'] > 1:
            tail_pos['y'] += 1
        elif tail_pos['y'] - head_pos['y'] > 1:
            tail_pos['y'] -= 1
    
    elif (tail_pos['y'] == head_pos['y']):
        if head_pos['x'] - tail_pos['x'] > 1:
            tail_pos['x'] += 1
        elif tail_pos['x'] - head_pos['x'] > 1:
            tail_pos['x'] -= 1
        
    else:
        x_distance = head_pos['x'] - tail_pos['x']
        y_distance = head_pos['y'] - tail_pos['y']
        if abs(x_distance) > 1 or abs(y_distance) > 1:
            if x_distance > 0:
                if y_distance > 0:
                    tail_pos['x'] += 1
                    tail_pos['y'] += 1
                else:
                    tail_pos['x'] += 1
                    tail_pos['y'] -= 1
            else:
                if y_distance > 0:
                    tail_pos['x'] -= 1
                    tail_pos['y'] += 1
                else:
                    tail_pos['x'] -= 1
                    tail_pos['y'] -= 1
    
    add_tail_position()
    

def add_tail_position():
    visited_positions[f"{tail_pos['x']}_{tail_pos['y']}"] = 1

with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            move(direction)

tail_visited_positions = len(visited_positions.keys())
print(f"Visible positions by the tail: {tail_visited_positions}")
