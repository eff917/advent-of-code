departure_time = 0
bus_list = []
with open('2020/dec13/input.txt', 'r') as infile:
    departure_time = int(infile.readline())
    bus_list = infile.readline().strip().split(',')
    
    bus_list = [int(x) for x in bus_list if x != 'x']


minutes_to_departure = {}

for bus in bus_list:
    minutes_to_departure[bus] = bus - (departure_time % bus)
print(departure_time)
print(bus_list)
print(minutes_to_departure)
minwait = min(minutes_to_departure.values())
for bus, wait_time in minutes_to_departure.items():
    if wait_time == minwait:
        print(bus*wait_time)