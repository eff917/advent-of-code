import pytest
from day11.part1 import part1 as part
import os


# @pytest.mark.skip
@pytest.mark.day11
@pytest.mark.parametrize(
    "inpufilename, expected",
    [
        ("test-input.txt", 374),
    ],
)
def test_main_answer(inpufilename, expected):
    infile = inpufilename
    actual_result = part.main(infile)
    assert actual_result == expected


@pytest.mark.day11
@pytest.mark.parametrize(
    "infile, expected_file", [("test-input.txt", "test-input-expanded.txt")]
)
def test_expand(infile, expected_file):
    map = part.parse_input(infile)
    actual_map = part.expand_map(map=map)
    expected_map = part.parse_input(expected_file)

    assert actual_map == expected_map


@pytest.mark.day11
@pytest.mark.parametrize(
    "infile, expected_list",
    [
        ("test-input-expanded.txt", {
        1: (0, 4),
        2: (1, 9),
        3: (2, 0),
        4: (5, 8),
        5: (6, 1),
        6: (7, 12),
        7: (10, 9),
        8: (11, 0),
        9: (11, 5),
    }),
    ],
)
def test_galaxy_list(infile, expected_list):
    in_map = part.parse_input(infile)
    actual_list = part.replace_galaxies(in_map)
    assert actual_list == expected_list


@pytest.mark.day11
@pytest.mark.parametrize(
    "infile, galaxy_1, galaxy_2, expected",
    [
        ("test-input-expanded.txt", 5, 9, 9),
        ("test-input-expanded.txt", 1, 7, 15),
        ("test-input-expanded.txt", 3, 6, 17),
        ("test-input-expanded.txt", 8, 9, 5),
    ],
)
def test_distance(infile, galaxy_1, galaxy_2, expected):
    map = part.parse_input(infile)
    list = part.replace_galaxies(map)
    actual = part.get_distance(list, galaxy_1, galaxy_2)
    assert actual == expected
