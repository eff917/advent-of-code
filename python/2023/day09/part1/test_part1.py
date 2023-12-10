import pytest
from day09.part1 import part1
import os


@pytest.mark.day09
@pytest.mark.parametrize(
    "inpufilename, expected",
    [
        ("test-input.txt", 114),
    ],
)
def test_given_input(inpufilename, expected):
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/{inpufilename}"
    actual_result = part1.main(infile)
    assert actual_result == expected


@pytest.mark.day09
@pytest.mark.parametrize(
    "bottom_line, top_line, expected",
    [([0, 0, 0, 0, 0], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3])],
)
def test_extend_top_line(bottom_line, top_line, expected):
    actual = part1.extend_top_line(bottom_line, top_line)
    assert actual == expected

@pytest.mark.day09
@pytest.mark.parametrize(
    "submap, expected",
    [
        ([[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]], 18),
        ([[1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]], 28),
        (
            [
                [10, 13, 16, 21, 30, 45],
                [3, 3, 5, 9, 15],
                [0, 2, 4, 6],
                [2, 2, 2],
                [0, 0],
            ],
            68,
        ),
    ],
)
def test_get_submap_extension_value(submap, expected):
    actual = part1.get_submap_extension_value(submap)
    assert actual == expected
