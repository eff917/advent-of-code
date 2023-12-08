import pytest
import part2
import os

@pytest.mark.parametrize(
    "ranges, id_range, expected_result",
    [
        # id_range fully inside
        (
            [
                {"range_start": 98, "range_end": 99, "offset": -48},
                {"range_start": 50, "range_end": 97, "offset": 2},
            ],
            {"id_start": 79, "id_end": 92},
            [{"id_start": 81, "id_end": 94}],
        ),
        # id_range fully outside
        (
            [
                {"range_start": 98, "range_end": 99, "offset": -48},
                {"range_start": 50, "range_end": 97, "offset": 2},
            ],
            {"id_start": 10, "id_end": 30},
            [{"id_start": 10, "id_end": 30}],
        ),
        # id_range partially before
        (
            [
                {"range_start": 98, "range_end": 99, "offset": -48},
                {"range_start": 50, "range_end": 97, "offset": 2},
            ],
            {"id_start": 10, "id_end": 60},
            [{"id_start": 52, "id_end": 62}, {"id_start": 10, "id_end": 49}],
        ),
        # id_range partially after
        (
            [
                {"range_start": 98, "range_end": 99, "offset": -48},
                {"range_start": 50, "range_end": 97, "offset": 2},
            ],
            {"id_start": 98, "id_end": 110},
            [{"id_start": 50, "id_end": 51}, {"id_start": 100, "id_end": 110}],
        ),
        # id_range bigger than rule range
        (
            [
                {"range_start": 98, "range_end": 99, "offset": -48},
                {"range_start": 50, "range_end": 97, "offset": 2},
            ],
            {"id_start": 96, "id_end": 110},
            [
                {"id_start": 50, "id_end": 51},
                {"id_start": 100, "id_end": 110},
                {"id_start": 98, "id_end": 99},
            ],
        ),
    ],
)
def test_convert_range_to_next(ranges, id_range, expected_result):
    actual_result = part2.convert_range_to_next(ranges=ranges, id_range=id_range)

    assert actual_result == expected_result

def test_given_input():
    infile = f"{os.path.dirname(os.path.realpath(__file__))}/part2/test-input.txt"
    actual_result = part2.main(infile)
    assert actual_result == 46
