"""
Advent of Code 2022
Day 7: No Space Left On Device (Part Two)
"""

def set_directory(path, dir_name):
    current_file_tree = file_tree
    for p in path:
        current_file_tree = current_file_tree[p]
    current_file_tree[dir_name] = {}

def set_file(path, file_name, file_size):
    current_file_tree = file_tree
    for p in path:
        current_file_tree = current_file_tree[p]
    current_file_tree[file_name] = file_size

def sum_sizes(tree):
    tree_size = 0
    tree_sums = []
    for subtree in tree:
        if not type(tree[subtree]) == dict:
            tree_size += int(tree[subtree])
        else:
            subtrees_sum, subtree_size = sum_sizes(tree[subtree])
            tree_size += subtree_size
            tree_sums += subtrees_sum
    tree_sums.append(tree_size)
    return tree_sums, tree_size

filesystem_space = 70000000
space_requirement = 30000000
max_size = 100000
current_path = []
file_tree = {'/': {}}

with open("input.txt", encoding='UTF-8') as input_file:
    for line in input_file:
        splitted_line = line.strip().split()
        if splitted_line[0] == '$':
            if splitted_line[1] == 'cd':
                if splitted_line[2] == '/':
                    current_path = ['/']
                elif splitted_line[2] == '..':
                    current_path.pop()
                else:
                    current_path.append(splitted_line[2])
        else:
            if splitted_line[0] == 'dir':
                set_directory(current_path, splitted_line[1])
            else:
                set_file(current_path, splitted_line[1], splitted_line[0])

all_tree_sums, total_size = sum_sizes(file_tree)

size_deleted = 0
for tree_sum in sorted(all_tree_sums):
    if filesystem_space - (total_size - tree_sum) >= space_requirement:
        size_deleted = tree_sum
        break    

print(f"Size deleted: {size_deleted}")
