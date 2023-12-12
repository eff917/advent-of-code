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
    actual_result = part.main(infile, expansion)
    assert actual_result == expected


@pytest.mark.day11
@pytest.mark.parametrize(
    "inputfilename, expected",
    [
        (
            "test-input.txt",
            (
                {
                    1: (0, 3),
                    2: (1, 7),
                    3: (2, 0),
                    4: (4, 6),
                    5: (5, 1),
                    6: (6, 9),
                    7: (8, 7),
                    8: (9, 0),
                    9: (9, 4),
                },  # galaxy list
                [3, 7],  # empty_rows
                [2, 5, 8],  # empty_columns
            ),
        )
    ],
)
def test_convert_map(inputfilename, expected):
    map = part.parse_input(inputfilename)
    actual_list, actual_rows, actual_columns = part.convert_map(map)
    expected_list, expected_rows, expected_columns = expected
    assert actual_list == expected_list
    assert actual_rows == expected_rows
    assert actual_columns == expected_columns


# expand needs a multiplier
@pytest.mark.day11
@pytest.mark.parametrize(
    "inputfilename, inputs, expected",
    [
        (
            "test-input.txt",
            (
                2,  # expansion value
                [3, 7],  # empty_rows
                [2, 5, 8],  # empty_columns
            ),
            {
                1: (0, 4),
                2: (1, 9),
                3: (2, 0),
                4: (5, 8),
                5: (6, 1),
                6: (7, 12),
                7: (10, 9),
                8: (11, 0),
                9: (11, 5),
            },
        )
    ],
)
def test_expand_galaxy_list(inputfilename, inputs, expected):
    map = part.parse_input(inputfilename)
    expansion_value, expected_rows, expected_columns = inputs
    galaxy_list, rows_list, columns_list = part.convert_map(map)
    actual_galaxy_list = part.expand_galaxy(
        galaxy_list, expansion_value, columns_list, rows_list
    )
    assert actual_galaxy_list == expected
