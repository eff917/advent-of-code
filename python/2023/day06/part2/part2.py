import os
import pprint

pp = pprint.PrettyPrinter(indent=2)

def parse_input(path: str):
    races = []
    with open(path) as file:
        times = file.readline().strip().split(":")[1].strip().split()
        distances = file.readline().strip().split(":")[1].strip().split()
        # for i in range(len(times)):
        #     times.remove('')
        # for _ in range(distances.count('')):
        #     distances.remove('')
        for i in range(len(times)):
            races.append({"time": int(times[i]), "distance": int(distances[i])})
            
    return races

def calculate_winning_options(time, distance):
    # we spend i ms to get speed, so we travel (time-i)ms at i mm/ms
    wins = 0
    for i in range(time):
        if (time-i)*i > distance:
            wins += 1
    return wins

def main(infile):
    race_list = parse_input(infile)
    winning_options = []
    for race in race_list:
        winning_options.append(calculate_winning_options(race["time"], race["distance"]))

    summary = 1
    for option in winning_options:
        summary *= option

    return summary



if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    result = main(infile)
    print(result)

