import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    # filesystem representation: dictionary
    # key: directory/file name
    # value: [size, parent_dir, [contained dirs], [contained files]]
    filesystem = {}
    parent_dir = ''
    current_dir = ''
    for line in infile:
        line = line.strip()
        line = line.split(' ')
        if line[0] == '$':
            command = line[1]
            if command == 'ls':
                continue
            if command == 'cd':
                if line[2] != '..':
                    parent_dir = current_dir
                    current_dir = parent_dir + '/' + line[2]
                    filesystem[current_dir] = [0, parent_dir, [], []]
                else:
                    current_dir = filesystem[current_dir][1]
                    parent_dir = filesystem[current_dir][1]
        elif line[0] == 'dir':
            filesystem[current_dir][2].append(current_dir + '/' + line[1])
        else:
            filesize = int(line[0])
            filename = current_dir + '/' + line[1]
            filesystem[filename] = [filesize, current_dir, [], []]
            filesystem[current_dir][3].append(filename)
    # print(filesystem)
    part1_sum = 0

    directory_minimum = dirsize('//', filesystem) - 40000000
    target_directory_name = ''
    target_directory_size = dirsize('//', filesystem)

    for name in filesystem.keys():
        size = dirsize(name, filesystem)
        # print(name, size)
        if size <= 100000:
            part1_sum += size
        if size > directory_minimum and size < target_directory_size:
            target_directory_name = name
            target_directory_size = size
    print(f"\nPart1: {part1_sum}")

    
    print(f"Part2: {target_directory_size}")

def dirsize(directory, filesystem):
    dir_size = 0
    for filename in filesystem[directory][3]:
        dir_size += filesystem[filename][0]
    for directory_name in filesystem[directory][2]:
        dir_size += dirsize(directory_name, filesystem)
    return dir_size

print("\nExample\n")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("\nReal\n")
with open(infile, 'r') as infile:
    solution(infile)
