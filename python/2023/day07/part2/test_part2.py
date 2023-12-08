import pytest
from day07.part1 import part1
import os

@pytest.mark.parametrize(
        "hand, expected",
        [
            ("12345", 0),
            ("11234", 1),
            ("11223", 2),
            ("11122", 3),
            ("11112", 4),
            ("11111", 5)
        ]
)
def test_hand_type(hand: str, expected: int):
    actual = part1.get_type(hand=hand)
    assert actual == expected

@pytest.mark.parametrize(
        "card1, card2, expected",
        [
            ("1", "1", 0),
            ("1", "2", 2),
            ("2", "1", 1),
            ("1", "T", 2),
            ("A", "T", 1)
        ]
)
def test_card_strength(card1: str, card2: str, expected: int):
    actual = part1.compare_cards(card1, card2)
    assert actual == expected

def test_given_input():
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/test-input.txt"
    actual_result = part1.main(infile)
    assert actual_result == 6440

