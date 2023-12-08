import pytest
from day07.part2 import part2
import os

def test_given_input():
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/test-input.txt"
    actual_result = part2.main(infile)
    assert actual_result == 71503
