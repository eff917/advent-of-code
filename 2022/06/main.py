import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    for line in infile:
        marker_found = False
        markers = []
        start = []
        line = line.strip()
        message_markers = []
        for char in line:
            start.append(char)
            if not marker_found:
                if len(markers) == 4:
                    markers.pop(0)
                if len(markers) < 4 :
                    markers.append(char)
                markers_set = set(markers)
                if len(markers_set) == 4 and not marker_found:
                    print(f"Part1: {len(start)}")
                    marker_found = True
            if len(message_markers) == 14:
                message_markers.pop(0)
            if len(message_markers) < 14 :
                message_markers.append(char)
            message_markers_set = set(message_markers)
            if len(message_markers_set) == 14:
                print(f"Part2: {len(start)}")
                break
            

    pass


print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("Real")
with open(infile, 'r') as infile:
    solution(infile)
