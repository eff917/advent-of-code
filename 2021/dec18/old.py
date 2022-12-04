from copy import deepcopy
from collections import Counter
from typing import Tuple
import ast
url = '2021/dec18/input.txt'
url = '2021/dec18/input-example.txt' # without reduction, works
# url = '2021/dec18/input-example-2.txt' # 

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

def explode(sn_number, original_number: str):
    # TODO how to find nearest left and right element?
    # TODO modify other list members shomehow
    # add sn_number[0] to left if exists
    # add sn_number[1] to right if exists
    splitnumber = original_number.split(sep=str(sn_number))
    print(f"Exploding {sn_number}")
    # print(f"Add {sn_number[0]} to {splitnumber[0]} rightmost regular number")
    # print(f"Add {sn_number[1]} to {splitnumber[1]} leftmost regular number")

    return 0, sn_number[0], sn_number[1]

def reduce(sn_number, nest_level, original_number, reduction_executed, left_carry, right_carry):
    print(f"Nest level: {nest_level}, Number: {sn_number}, Carries: {left_carry}, {right_carry}")
    if type(sn_number) is list:
        if type(sn_number[0]) is int and left_carry > 0:
            sn_number[0] += left_carry
            left_carry = 0
        if type(sn_number[1]) is int and right_carry > 0:
            sn_number[1] += right_carry
            right_carry = 0
        print(f"Nest level: {nest_level}, Number: {sn_number}, Left side: {sn_number[0]}, Right side: {sn_number[1]} Carries: {left_carry}, {right_carry}")
        if type(sn_number[0]) is int and type(sn_number[1]) is int and nest_level > 4 and not reduction_executed:
            sn_number, left_carry, right_carry = explode(sn_number, original_number)
            reduction_executed = True
        else:
            sn_number[0], reduction_executed, left_carry, right_carry = reduce(sn_number[0], nest_level+1, original_number, reduction_executed, left_carry, right_carry)
            sn_number[1], reduction_executed, left_carry, right_carry = reduce(sn_number[1], nest_level+1, original_number, reduction_executed, left_carry, right_carry)
    # splitting works
    elif type(sn_number) is int and sn_number > 9 and not reduction_executed:
            print(f"Splitting {sn_number}")
            sn_number = split_regular(sn_number)
            reduction_executed = True
    return sn_number, reduction_executed, left_carry, right_carry

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

original = ast.literal_eval('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
test_number = ast.literal_eval('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
prev_number = None
reductions = 0
print(f"Reducing: {str(original)}")
while test_number != prev_number:
    prev_number = deepcopy(test_number)
    test_number, reduction_executed, lc, rc = reduce(test_number, 1, str(test_number), False, 0, 0)
    print(lc, rc)
    reductions += 1
    print(f"Reductions: {reductions}, number: {test_number}")
print(original)
print(test_number)
