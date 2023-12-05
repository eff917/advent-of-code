from dataclasses import dataclass
import os
import time
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
    possible_beacons = set()
    for index, line in enumerate(infile):
        line = line.strip().split(' ')
        sx = int(line[2].replace('x=', '').replace(',',''))
        sy = int(line[3].replace('y=', '').replace(':',''))
        bx = int(line[8].replace('x=', '').replace(',',''))
        by = int(line[9].replace('y=', '').replace(':',''))
        scanned_distance = abs(bx - sx) + abs(by - sy)
        # print(f"Points: {scanned_distance * 4}")

        sensors.append(Sensor(Coordinate(sx, sy), scanned_distance))
        beacons.append(Coordinate(bx, by))

    beacon_coord_limit = 20
    beacon_coord_limit = 4000000 
    # print(sensors)
    sensors = sorted(sensors, key=lambda a: a.scan_distance)
    # print(sensors)
    for index, sensor in enumerate(sensors):
        print(f"Checking sensor {index} with range {sensor.scan_distance}")
        for step in range(0, sensor.scan_distance + 2):
            # 0 11
            # 1 10
            # 2 9
            # 3 8
            # 4 7
            # 5 6
            # 6 5
            # 7 4
            # 8 3
            # 9 2
            # 10 1
            
            c1 = Coordinate(sensor.coordinate.x - step, sensor.coordinate.y + (sensor.scan_distance +1 - step))
            c2 = Coordinate(sensor.coordinate.x + step, sensor.coordinate.y + (sensor.scan_distance +1 - step))
            c3 = Coordinate(sensor.coordinate.x - step, sensor.coordinate.y - (sensor.scan_distance +1 - step))
            c4 = Coordinate(sensor.coordinate.x + step, sensor.coordinate.y - (sensor.scan_distance +1 - step))
            if c1.x >= 0 and c1.x <= beacon_coord_limit and c1.y >= 0 and c1.y <= beacon_coord_limit:
                is_c1_beacon = True
            else:
                is_c1_beacon = False
            if c2.x >= 0 and c2.x <= beacon_coord_limit and c2.y >= 0 and c2.y <= beacon_coord_limit:
                is_c2_beacon = True
            else:
                is_c2_beacon = False
            if c3.x >= 0 and c3.x <= beacon_coord_limit and c3.y >= 0 and c3.y <= beacon_coord_limit:
                is_c3_beacon = True
            else:
                is_c3_beacon = False
            if c4.x >= 0 and c4.x <= beacon_coord_limit and c4.y >= 0 and c4.y <= beacon_coord_limit:
                is_c4_beacon = True
            else:
                is_c4_beacon = False
            for sensor in sensors:
                if is_c1_beacon and manhattan_distance(c1.x, c1.y, sensor.coordinate.x, sensor.coordinate.y) <= sensor.scan_distance:
                    is_c1_beacon = False
                if is_c2_beacon and manhattan_distance(c2.x, c2.y, sensor.coordinate.x, sensor.coordinate.y) <= sensor.scan_distance:
                    is_c2_beacon = False
                if is_c3_beacon and manhattan_distance(c3.x, c3.y, sensor.coordinate.x, sensor.coordinate.y) <= sensor.scan_distance:
                    is_c3_beacon = False
                if is_c4_beacon and manhattan_distance(c4.x, c4.y, sensor.coordinate.x, sensor.coordinate.y) <= sensor.scan_distance:
                    is_c4_beacon = False
            if is_c1_beacon:
                print(c1)
            if is_c2_beacon:
                print(c2)
            if is_c3_beacon:
                print(c3)
            if is_c4_beacon:
                print(c4)

    print(len(possible_beacons))    

    # for beacon in possible_beacons:
    #     print(f"Part2: {beacon.x * 4000000 + beacon.y}")

    # for coord in beacons:
    #     if coord in cannot_sustain:
    #         cannot_sustain.remove(coord)    
    # print(len(cannot_sustain))

def manhattan_distance(sx: int, sy: int, bx: int, by: int) -> int:
    return abs(sx - bx) + abs(sy - by)



print("\nExample")
with open(infile_example, 'r') as infile_example:
    solution(infile_example)

print("\nReal")
with open(infile, 'r') as infile:
    solution(infile)

# 4062363 wrong
# 5073496 right
