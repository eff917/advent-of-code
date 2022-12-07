import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

def solution(infile):
    for line in infile:
        pass


print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("Real")
with open(infile, 'r') as infile:
    solution(infile)
