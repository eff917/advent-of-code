import pytest
from day11.part2 import part2 as part
import os


# @pytest.mark.skip
@pytest.mark.day11
@pytest.mark.parametrize(
    "inpufilename, expansion, expected",
    [
        ("test-input.txt", 2, 374),
        ("test-input.txt", 10, 1030),
        ("test-input.txt", 100, 8410),
    ],
)
def test_main_answer(inpufilename, expansion, expected):
    infile = inpufilename
    actual_result = part.main(infile)
    assert actual_result == expected

def get_empty_rows():
    pass

def get_empty_columns():
    pass

def test_get_galaxy_list():
    pass

# expand needs a multiplier
def test_expand_galaxy_list():
    pass

