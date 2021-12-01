#!/usr/bin/env python3

with open('../input.txt', 'r') as infile:
    count = 0
    value = None
    prev_value = None
    for line in infile:
        if prev_value is None:
            prev_value = int(line)
            continue
        else:
            value = int(line)
            if value > prev_value:
                count += 1
            prev_value = value
print(count)
