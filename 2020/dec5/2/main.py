maxid = 0
seatids = []
with open('../input.txt', 'r') as inputfile:
    for line in inputfile:
        row = 0
        seat = 0
        rowrange = 64
        seatrange = 4
        for char in line:
            if char == 'F':
                pass
            elif char == 'B':
                row += rowrange
                pass
            elif char == 'L':
                pass
            elif char == 'R':
                seat += seatrange
            if char in ['F', 'B']:
                rowrange = rowrange // 2
            if char in ['L', 'R']:
                seatrange = seatrange // 2
        seatids.append(8*row+seat)
        if 8*row+seat > maxid:
            maxid = 8*row+seat
 
for i in range(977):
    if (i-1 in seatids) and (i+1 in seatids) and (i not in seatids):
        print(i)

