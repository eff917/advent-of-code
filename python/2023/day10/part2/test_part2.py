import pytest
from day09.part2 import part2
import os


@pytest.mark.parametrize(
    "inpufilename, expected",
    [
        ("test-input.txt", 2),
    ],
)
def test_given_input(inpufilename, expected):
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/{inpufilename}"
    actual_result = part2.main(infile)
    assert actual_result == expected


@pytest.mark.parametrize(
    "bottom_line, top_line, expected",
    [([0, 0, 0, 0, 0], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3])],
)
def test_extend_top_line(bottom_line, top_line, expected):
    actual = part2.extend_top_line(bottom_line, top_line)
    assert actual == expected


@pytest.mark.parametrize(
    "submap, expected",
    [
        ([[15, 12, 9, 6, 3, 0], [-3, -3, -3, -3, -3], [0, 0, 0, 0]], -3),
        ([[21, 15, 10, 6, 3, 1], [-6, -5, -4, -3, -2], [1, 1, 1, 1], [0, 0, 0]], 0),
        (
            [
                [45, 30, 21, 16, 13, 10],
                [-15, -9, -5, -3, -3],
                [6, 4, 2, 0],
                [-2, -2, -2],
                [0, 0]
            ],
            5,
        ),
    ],
)
def test_get_submap_extension_value(submap, expected):
    actual = part2.get_submap_extension_value(submap)
    assert actual == expected
