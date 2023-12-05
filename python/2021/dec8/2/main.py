url = '2021/dec8/input.txt'
# url = '2021/dec8/input-example.txt'

data = []
with open(url, 'r') as infile:
    for line in infile:
        head, tail = line.strip().split(' | ')
        datadict = {}
        datadict['input'] = head.split(' ')
        for itemid, item in enumerate(datadict['input']):
            datadict['input'][itemid] = ''.join(sorted(list(item)))
        datadict['output'] = tail.split(' ')
        for itemid, item in enumerate(datadict['output']):
            datadict['output'][itemid] = ''.join(sorted(list(item)))
        data.append(datadict)

print(data)
# segments:
# initial:
# 1: 2 (TR BR)
# 7: 3 (TH TR BR)
# 4: 4 (TL MH TR BR)
# 8: 7 (TL BL TH MH BH TR BR)

# second round:
# 4 - 1 = TL MH

# 7 - 1 = TH

# 8 - 1 = e (TH MH BH TL BL)
# 8 - 4 = BL TH BH
# 8 - 7 = TL BL MH BH

# 6: 6 (TL BL TH MH BH BR)
# 6-1 -> length = 5 all others are 4
# if len(x) == 6 and len(x - 1) == 5 -> 6
# 3-7 -> 2 segments: if len(x) == 5 and len(x-7) == 2


# TO find:
# 2: 5 (BL TH MH BH TR)
# 3: 5 (TH MB BH TR BR)
# 5: 5 (TL TH MH BH BR)
# solved 6: 5

# 0: 6 (TL BL TH BH TR BR)
# 9: 6 (TL TH MH BH TR BR) 


#### counts
# 0-7 -> 3 segments
# 2-7 -> 3 segments
# 3-7 -> 2 segments: if len(x) == 5 and len(x-7) == 2
# 5-7 -> 3 segments
# 9-7 -> 3 segments


# 8 - 0 = middle horizontal segment
# 3 - 7 - middle horizontal = bottom horizontal

# 8 - 6 = upper right vertical segment

# 8 - 9 = lower left vertical segment
# 6 - 5 = lower left vertical segment

# 1 - upper right vertical = lower right vertical

def calculate_segments(segmentlist: list):
    segments = {}
    # insert known number segments into dict
    for segment in segmentlist:
        if len(segment) == 2:
            segments['1'] = segment
        elif len(segment) == 3:
            segments['7'] = segment
        elif len(segment) == 4:
            segments['4'] = segment
        elif len(segment) == 7:
            segments['8'] = segment

    segmentlist.remove(segments['1'])
    segmentlist.remove(segments['7'])
    segmentlist.remove(segments['4'])
    segmentlist.remove(segments['8'])

    for segment in segmentlist:
        # find 6
        if len(segment) == 6:
            subs = [item for item in segment if item not in segments['1']]
            if len(subs) == 5:
                segments['6'] = segment
        # find 3
        if len(segment) == 5:
            subs = [item for item in segment if item not in segments['7']]
            if len(subs) == 2:
                segments['3'] = segment
            pass
    segmentlist.remove(segments['6'])
    segmentlist.remove(segments['3'])
    # remaining numbers: 6long: 0,9 5long: 2,5
    for segment in segmentlist:
        # find 0
        if len(segment) == 6:
            subs = [item for item in segment if item not in segments['3']]
            if len(subs) == 2:
                segments['0'] = segment
            # the only other 6long is 9
            elif len(subs) == 1:
                segments['9'] = segment
        # find 2 and 5
        elif len(segment) == 5:
            subs = [item for item in segment if item not in segments['6']]
            #5-6 == 0
            if len(subs) == 0:
                segments['5'] = segment
            # 2-6 == 1
            elif len(subs) == 1:
                segments['2'] = segment
    segmentlist.remove(segments['0'])
    segmentlist.remove(segments['9'])
    segmentlist.remove(segments['5'])
    segmentlist.remove(segments['2'])
    return segments

sum = 0
for line in data:
    line['segments'] = calculate_segments(line['input'])
    print(line['input'])
    print(line['output'])
    for segment in sorted(line['segments'].items()):
        print(segment)

    # decode outputs
    outputvalue = ''
    for number in line['output']:
        for key, value in line['segments'].items():
            if value == number:
                outputvalue += key
    print(int(outputvalue))
    sum += int(outputvalue)
print(sum)

