import pytest
from day09.part1 import part1
import os


@pytest.mark.parametrize(
        "inpufilename, expected",
        [
            ("test-input.txt", 2),
            ("test-input-2.txt", 6),
        ]
)
def test_given_input(inpufilename, expected):
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/{inpufilename}"
    actual_result = part1.main(infile)
    assert actual_result == expected

