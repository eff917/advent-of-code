from copy import deepcopy
from os import readlink
from collections import Counter
url = '2021/dec14/input.txt'
# url = '2021/dec14/input-example.txt'


polimers = {}
polimers = {}
with open(url, 'r') as infile:
    template = infile.readline().strip()
    infile.readline()
    rule = infile.readline().strip().split(' -> ')
    while len(rule) > 1:
        # add the first char of the source to the target
        polimers[rule[0]]= rule[0][0] + rule[1] + rule[0][1]
        rule = infile.readline().strip().split(' -> ')


# example runtime with list:
# 10 loops: 0.5s
# 20 loops: 4.6s
# 21 loops: 9.3s
# 22 loops: 16.446s
# 23 loops: 34.163s

# example runtimes with string:
# 20 loops:  1.981s
# 21 loops:  4.930s
# 22 loops:  7.395s
# 23 loops: 15.583s
# 24 loops: 31.695s
# 25 loops: ~1minute
# only halved the runtime, it would take ~ 2^15 minutes to run 40 loops ~546hours

# runtimes with less operations (added char to rule result, instead of adding chars separately)
# 20 loops: example  1.335s full  6.411s
# 21 loops: example   1.895s full 12.223s
# 22 loops: example   3.903s full 22.628s
# 23 loops: example   7.547s full 44.531s
# 24 loops: example  14.155s full - 
# 25 loops: example  27.538s full -
# 26 loops: example  54.910s full -
# 27 loops: exmaple 118.695s full -

# time to start memoization, and recursively gettint containing letters, memory usage is too high, and code is too slow

print(polimers)
results = {}
def get_containing_letters(letter_pair, rounds):
    if rounds == 1:
        return Counter(polimers[letter_pair])
    else:
        if (letter_pair, rounds) in results:
            return results[(letter_pair, rounds)]
        else:
            next_round = polimers[letter_pair]
            results[(letter_pair, rounds)] = get_containing_letters(next_round[:2], rounds-1) + get_containing_letters(next_round[1:], rounds-1) - Counter(next_round[1])
            return results[(letter_pair, rounds)]

            

first_char = template[0]
sum = Counter()
for char in template[1:]:
    # print(first_char + char)
    subresult = get_containing_letters(first_char+char, 40)
    # print(subresult)
    sum += subresult 
    first_char = char

sum -= Counter(template[1:-1])
print()
print(sum)

print(f"{max(sum.values()) - min(sum.values())}")
# Counter({'N': 2, 'C': 1})
# Counter({'N': 1, 'B': 1, 'C': 1})
# Counter({'B': 2, 'N': 1})
# print(Counter("NBBBCNCCNBBNBNBBCHBHHBCHB"))