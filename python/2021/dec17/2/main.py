from copy import deepcopy
from collections import Counter
from typing import Tuple
url = '2021/dec17/input.txt'
# url = '2021/dec17/input-example.txt'

with open(url, 'r') as infile:
    line = infile.readline().strip().split(' ')

txmin, txmax = line[2].split('..')
txmin = int(txmin[2:])
txmax = int(txmax[:-1])

tymin, tymax = line[3].split('..')

tymin = int(tymin[2:])
tymax = int(tymax)

print(txmin, txmax)
print(tymin, tymax)


start_values = set()
# calculate the new position ans speed of the probe
def step(px: int, py: int, psx: int, psy: int) -> Tuple[int, int, int, int]:
    # increase horizontal position
    px += psx
    # calculate new vertical position
    py += psy
    # decrease horizontal speed due to drag
    if psx > 0:
        psx -= 1
    # gravity
    psy -= 1
    return (px, py, psx, psy)

# initial probe values
probe_x = 0
probe_y = 0
probe_max_height = 0
probe_speed_x = 0
probe_speed_y = 0

valid_x_speeds = []
# step one find the feasible horizontal speed ranges
for x in range(txmax+1):
    # set initial horizontal speed
    probe_speed_x = x
    probe_x = 0
    print(f"checking initial x speed: {x}")
    while probe_speed_x > 0 and probe_x <= txmax:
        probe_x, probe_y, probe_speed_x, probe_speed_y = step(probe_x, probe_y, probe_speed_x, probe_speed_y)
        print(probe_x, probe_speed_x)
        if probe_x <= txmax and probe_x >= txmin:
            break
    if probe_x <= txmax and probe_x >= txmin:
        valid_x_speeds.append(x)
    
print(valid_x_speeds)

# step 2: for each valid X speed, try to find the highest y speed which still hits target area

for x in valid_x_speeds:
    for y in range(-1000, 1000):
        max_height = 0
        probe_speed_x = x
        probe_speed_y = y
        probe_y = 0
        probe_x = 0
        # check right and bottom boundaries
        while probe_x <= txmax and probe_y >= tymin:
            probe_x, probe_y, probe_speed_x, probe_speed_y = step(probe_x, probe_y, probe_speed_x, probe_speed_y)
            max_height = max(probe_y, max_height)
            # cheack left and top boundaries
            if probe_x >= txmin and probe_y <= tymax and probe_x <= txmax and probe_y >= tymin:
                # we're in the target area, so current launch is valid
                probe_max_height = max(probe_max_height, max_height)
                print(f"Probe hit the target area at {probe_x} {probe_y}")
                start_values.add((x,y))
                break

print()
print(f"Maximum height (stage 1 answer): {probe_max_height}")
# print(valid_x_speeds)
# print(start_values)
print(f"Number of valid start values (stage 2 answer): {len(start_values)}")