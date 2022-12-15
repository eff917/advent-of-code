from dataclasses import dataclass
import os
from copy import deepcopy
infile_example = f"{os.path.dirname(os.path.realpath(__file__))}/input-example.txt"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"

@dataclass(unsafe_hash=True)
class Coordinate:
    x: int
    y: int

@dataclass
class Sensor:
    coordinate: Coordinate
    scan_distance: int

def solution(infile):
    beacons = []
    sensors = []
    xmax, xmin, ymax, ymin = None, None, None, None
    for line in infile:
        line = line.strip().split(' ')
        sx = int(line[2].replace('x=', '').replace(',',''))
        sy = int(line[3].replace('y=', '').replace(':',''))
        bx = int(line[8].replace('x=', '').replace(',',''))
        by = int(line[9].replace('y=', '').replace(':',''))
        if xmax is None:
            xmax = max(sx, bx)
            xmin = min(sx, bx)
            ymax = max (sy, by)
            ymin = min(sy, by)

        scanned_distance = abs(bx - sx) + abs(by - sy)
        xmax = max(xmax, sx+scanned_distance, bx)
        ymax = max(ymax, sy+scanned_distance, by)
        xmin = min(xmin, sx-scanned_distance, bx)
        ymin = min(ymin, sy-scanned_distance, by)
        # print(xmax, ymax, xmin, ymin)
        # print(line, scanned_distance)
        sensors.append(Sensor(Coordinate(sx, sy), scanned_distance))
        beacons.append(Coordinate(bx, by))
    # print(sensors)
    # print(beacons)
    y = 2000000
    # y = 10
    cannot_sustain = set()
    for x in range(xmin-100, xmax+100):
        if Coordinate(x, y) in beacons:
            # cannot_sustain -= 1
            continue
        for sensor in sensors:
            # print(sensor, x, y)
            md = manhattan_distance(sensor, Coordinate(x, y))
            if md <= sensor.scan_distance:
                # print(f"Cannot sustain. [{x},{y}] {md}, {sensor.scan_distance}")
                cannot_sustain.add(Coordinate(x, y))
                break
    print(len(cannot_sustain))

    # for coord in beacons:
    #     if coord in cannot_sustain:
    #         cannot_sustain.remove(coord)    
    # print(len(cannot_sustain))

def manhattan_distance(sensor: Sensor, coord: Coordinate) -> int:
    return abs(sensor.coordinate.x - coord.x) + abs(sensor.coordinate.y - coord.y)



print("\nExample")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("\nReal")
with open(infile, 'r') as infile:
    solution(infile)

# 4062363 wrong
# 5073496 right
