import os
import pprint

pp = pprint.PrettyPrinter(indent=2)

def parse_input(path: str):
    races = []
    with open(path) as file:
        time = file.readline().strip().split(":")[1].strip().split()
        distance = file.readline().strip().split(":")[1].strip().split()

        time = int(''.join(time))
        distance = int(''.join(distance))

            
    return (time, distance)

def calculate_winning_options(time, distance):
    # we spend i ms to get speed, so we travel (time-i)ms at i mm/ms
    wins = 0
    for i in range(time):
        if (time-i)*i > distance:
            wins += 1
    return wins

def main(infile):
    time, distance = parse_input(infile)
    winning_options = calculate_winning_options(time, distance)

    summary = winning_options
    return summary



if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    result = main(infile)
    print(result)

