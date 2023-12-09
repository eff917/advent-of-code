import os
import pprint
from enum import IntEnum

pp = pprint.PrettyPrinter(indent=2)


def convert_hand(hand: str) -> str:
    return (
        hand.replace("T", "a")
        .replace("J", "b")
        .replace("Q", "c")
        .replace("K", "d")
        .replace("A", "e")
    )


# hand types: 5, 4, 3+2, 2+2, 2, 1
def get_type(hand: str):
    hand = sorted(hand)
    type = 0
    counts = [
        hand.count(hand[0]),
    ]
    sum = counts[0]

    while sum < 5:
        next = hand.count(hand[sum])
        counts.append(next)
        sum += next

    counts.sort(reverse=True)
    print(counts)
    if counts[0] > 3:
        return counts[0] + 1
    elif counts[0] == 3 and counts[1] == 2:
        return 4
    elif counts[0] == 3:
        return 3
    elif counts[0] == 2 and counts[1] == 2:
        return 2
    elif counts[0] == 1:
        return 0
    else:
        return 1


def compare_cards(card1: str, card2: str):
    if Card_strength[card1] > Card_strength[card2]:
        return 1
    elif Card_strength[card1] < Card_strength[card2]:
        return 2
    else:
        return 0


def parse_input(path: str):
    hands_list = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}
    with open(path) as file:
        for line in file:
            hand, bid = line.split()
            bid = int(bid)
            hands_list[get_type(hand)][convert_hand(hand)] = bid
    pp.pprint(hands_list)
    return hands_list


Card_strength = IntEnum(
    "Card_strength",
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"],
)
# TODO change cards to: 123456789abcde
# this way simple comparison should work to determine the second ordering
# T->a
# J->b
# Q->c
# K->d
# A->e


def main(infile):
    hands_list = parse_input(infile)
    answer = 0
    rank = 1
    for key, value in sorted(hands_list.items()):
        for key2, value2 in sorted(value.items()):
            print(f"Type: {key} Hand: {key2} Bid: {value2} Rank: {rank}")
            answer += rank * value2
            rank += 1

    return answer


if __name__ == "__main__":
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    result = main(infile)
    print(result)
