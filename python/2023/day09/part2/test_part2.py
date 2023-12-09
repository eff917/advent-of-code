import pytest
from day09.part2 import part2
import os


@pytest.mark.parametrize(
    "inpufilename, expected",
    [
        ("test-input-3.txt", 6),
    ],
)
def test_given_input(inpufilename, expected):
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/{inpufilename}"
    actual_result = part2.main(infile)
    assert actual_result == expected
