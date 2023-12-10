import pytest
from day10.part1 import part1
import os

@pytest.mark.day10
@pytest.mark.parametrize(
    "inpufilename, expected",
    [
        ("test-input.txt", 4),
        ("test-input-2.txt", 8),
    ],
)
def test_main_answer(inpufilename, expected):
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/{inpufilename}"
    actual_result = part1.main(infile)
    assert actual_result == expected

@pytest.mark.day10
@pytest.mark.parametrize(
        "map, expected",
        [
            (['7-F7-', '.FJ|7', 'SJLL7', '|F--J', 'LJ.LJ'], (2, 0)),
            (['-L|F7', '7S-7|', 'L|7||', '-L-J|', 'L|-JF'], (1, 1))
        ]
)
def test_start_coord(map, expected):
    actual = part1.get_starting_position(map=map)
    assert actual == expected