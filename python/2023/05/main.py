import os
import math

# region part1
part = "part1"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"
summary = 0
with open(infile) as file:
    for line in file:
        winning_numbers, my_numbers = line.split(":")[1].strip().split("|")
        winning_numberstring = winning_numbers.strip().split(" ")
        my_numberstring = my_numbers.strip().split(" ")
        winning_numbers = set()
        my_numbers = set()
        for number in winning_numberstring:
            if number.strip() != "":
                winning_numbers.add(int(number.strip()))
        for number in my_numberstring:
            if number.strip() != "":
                my_numbers.add(int(number.strip()))
        power = len(my_numbers.intersection(winning_numbers)) - 1
        if power >= 0:
            summary += int(math.pow(2, power))


print(f"Part1 answer: {summary}")

# endregion part1

# region part2
part = "part2"
infile = f"{os.path.dirname(os.path.realpath(__file__))}/{part}/input.txt"
summary = 0

cards = {}
with open(infile) as file:
    for line in file:
        card, numbers = line.strip().split(":")
        card_number = int(card.strip().split(" ")[-1])
        winning_numbers, my_numbers = numbers.strip().split("|")
        winning_numberstring = winning_numbers.strip().split(" ")
        my_numberstring = my_numbers.strip().split(" ")
        winning_numbers = set()
        my_numbers = set()
        for number in winning_numberstring:
            if number.strip() != "":
                winning_numbers.add(int(number.strip()))
        for number in my_numberstring:
            if number.strip() != "":
                my_numbers.add(int(number.strip()))
        matches = len(my_numbers.intersection(winning_numbers))
        # print(f"{card_number, matches}")
        if card_number not in cards.keys():
            cards[card_number] = 1
        else:
            cards[card_number] += 1
        for i in range(1, matches+1):
            if card_number+i not in cards.keys():
                cards[card_number+i] = cards[card_number]
            else:
                cards[card_number+i] += cards[card_number]
summary = sum(cards.values())
print(f"Part2 answer: {summary}")
# endregion part2
