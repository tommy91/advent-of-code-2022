"""
Advent of Code 2022
Day 6: Tuning Trouble (Part Two)
"""

def read_datastream():
    with open("input.txt", encoding='UTF-8') as input_file:
        return input_file.readline()

datastream = read_datastream()
i = 0
marker_len = 14
current_marker_start = 0
while (i < len(datastream)) and (i - current_marker_start < marker_len):
    for j in range(1, (i - current_marker_start) + 1):
        if i - j < 0:
            break
        if datastream[i] == datastream[i-j]:
            current_marker_start = (i - j) + 1
            break
    if (i - current_marker_start) + 1 == marker_len:
        break
    i += 1

print(f"Last marker character position: {i + 1}")
