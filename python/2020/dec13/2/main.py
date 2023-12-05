bus_list = []
minutes_to_departure = {}
remainings = {}
with open('2020/dec13/input.txt', 'r') as infile:
    infile.readline()
    bus_list = infile.readline().strip().split(',')
    
    for i in range(len(bus_list)):
        if bus_list[i] != 'x':
            minutes_to_departure[int(bus_list[i])] = i
            remainings[int(bus_list[i])] = (int(bus_list[i]) - i)%int(bus_list[i])


print(minutes_to_departure)
print(remainings)


# T   : bus 23   T%23  == 0
# T+13: bus 41   T%41  == 28
# T+17: bus 37   T%37  == 20
# T+23: bus 479  T%479 == 456
# T+36: bus 13   T%13  == 3
# T+40: bus 17   T%17  == 11
# T+52: bus 29   T%29  == 6
# T+54: bus 373  T%373 == 319
# T+73: bus 19   T%19  == 3


# T+4: bus 59 T%59 == 55
# T+6: bus 31 T%31 == 25
# T+7: bus 19 T%19 == 12
# T+1: bus 13 T%13 == 12
# T+0: bus 7  T%7 == 0


found = False
bus_list = sorted(minutes_to_departure.keys(), reverse=True)
# get the biggest bus id, to reduce the amount of checking
max_id = bus_list.pop(0)
step = max_id
# TODO find a quicker alg
# bus_list = [bus_list.pop(0)]
# set time based on the delay of the biggest ID bus
current_time = 0 - minutes_to_departure[max_id]
print(current_time)
print(bus_list)
matched_buses = set()
while not found:
# for i in range(1000):
    current_time += step
    found = True
    print(f"checking time {current_time}")
    for bus_id in bus_list:
        if current_time % bus_id == remainings[bus_id]:
            print(f"matches bus {bus_id}")
            if bus_id not in matched_buses:
                step = step*bus_id
                matched_buses.add(bus_id)
            # print(f"{(current_time - remainings[bus_id])//bus_id}")
            pass
        else:
            found = False
            break
        pass
    pass

print(current_time)