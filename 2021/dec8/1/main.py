url = '2021/dec8/input.txt'
# url = '2021/dec8/input-example.txt'

unique_count = 0
with open(url, 'r') as infile:
    for line in infile:
        head, tail = line.strip().split(' | ')
        head = head.split(' ')
        tail = tail.split(' ')
        print(head, tail)
        for output in tail:
            if len(output) in [2, 3, 4, 7]:
                unique_count += 1

# segment count:
# 1: 2

# 7: 3

# 4: 4

# 2: 5
# 3: 5
# 5: 5

# 0: 6
# 6: 6
# 9: 6

# 8: 7
print(unique_count)