import pytest
from day07.part1 import part1
import os

def test_given_input():
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/test-input.txt"
    actual_result = part1.main(infile)
    assert actual_result == 288
