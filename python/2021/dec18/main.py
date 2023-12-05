import os
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

import ast

# magnitude works
def magnitude(snailnumber):
    result = 0
    if type(snailnumber) is int:
        result = snailnumber
    else:
        result = 3 * magnitude(snailnumber[0]) + 2 * magnitude(snailnumber[1])
    return result

def add_numbers(left_number, right_number):
    return [left_number, right_number]

def split_regular(regular_number: int):
    return [regular_number // 2, regular_number - regular_number // 2]

def explode(snailnumber):

    result = 0
    
    return result

def solution(infile):
    pass

print("Example")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)
print("Normal")
with open(infile, 'r') as infile:
    solution(infile)

sn1 = ast.literal_eval('[[[[4,3],4],4],[7,[[8,4],9]]]')
sn2 = ast.literal_eval('[1,1]')

print(f"{sn1} + {sn2}")
result = add_numbers(sn1, sn2)