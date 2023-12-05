maxid = 0
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        row = 0
        seat = 0
        range = 64
        seatrange = 4
        for char in line:
            if char == 'F':
                pass
            elif char == 'B':
                row += range
                pass
            elif char == 'L':
                pass
            elif char == 'R':
                seat += seatrange
            if char in ['F', 'B']:
                range = range // 2
            if char in ['L', 'R']:
                seatrange = seatrange // 2
        print(8*row+seat)
        if 8*row+seat > maxid:
            maxid = 8*row+seat

print()
print(maxid)