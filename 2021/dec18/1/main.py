from copy import deepcopy
from collections import Counter
from typing import Tuple
import ast
url = '2021/dec18/input.txt'
url = '2021/dec18/input-example.txt' # without reduction, works
url = '2021/dec18/input-example-2.txt' # 

# url = '2021/dec18/input-example-large-1.txt'

numbers = []
with open(url, 'r') as infile:
    for line in infile:
        numbers.append(ast.literal_eval(line.strip()))


def add_numbers(left_number, right_number):
    return [left_number, right_number]

def split_regular(regular_number: int):
    return [regular_number // 2, regular_number - regular_number // 2]
# print(split_regular(10))
# print(split_regular(11))
# print(split_regular(12))

def explode(sn_number):
    # TODO how to find nearest left and right element?
    # TODO modify other list menbers shomehow
    # add sn_number[0] to left if exists
    # add sn_number[1] to right if exists
    print(f"Exploding {sn_number}")
    return 0

def reduce(sn_number, nest_level):
    print(f"Nest level: {nest_level}, {sn_number}")
    # splitting works
    if type(sn_number) is int and sn_number > 9:
            sn_number = split_regular(sn_number)
    elif type(sn_number) is list:
        if type(sn_number[0]) is int and type(sn_number[1]) is int and nest_level > 4:
            sn_number = explode(sn_number)
        else:
            sn_number[0] = reduce(sn_number[0], nest_level+1)
            sn_number[1] = reduce(sn_number[1], nest_level+1)

    return sn_number

# This is correct
def count_magnitude(sn_number):
    magnitude = 0
    if type(sn_number) is list:
        magnitude += 3*count_magnitude(sn_number[0])
        magnitude += 2*count_magnitude(sn_number[1])
    else:
        magnitude = sn_number
    return magnitude

sum = numbers[0]
for number in numbers[1:]:
    sum = add_numbers(sum, number)

# print(sum)

test_number = ast.literal_eval('[[[[0,7],4],[15,[0,13]]],[1,1]]')
prev_number = None
while test_number != prev_number:
    prev_number = deepcopy(test_number)
    test_number = reduce(test_number, 1)
print(test_number)

