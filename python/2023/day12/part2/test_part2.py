import pytest
from day12.part2 import part2 as part
import os


# @pytest.mark.skip
@pytest.mark.day12
@pytest.mark.parametrize(
    "inpufilename, expected",
    [
        ("test-input.txt", 525152),
    ],
)
def test_main_answer(inpufilename, expected):
    infile = inpufilename
    actual_result = part.main(infile)
    assert actual_result == expected


@pytest.mark.day12
@pytest.mark.parametrize(
    "input, expected",
    [
        ("#.#.###", [1, 1, 3]),
        (".#...#....###.", [1, 1, 3]),
        (".#.###.#.######", [1, 3, 1, 6]),
        ("####.#...#...", [4, 1, 1]),
        ("#....######..#####.", [1, 6, 5]),
        (".###.##....#", [3, 2, 1]),
    ],
)
def test_get_damages(input, expected):
    actual = part.get_damages(input)
    assert actual == expected


@pytest.mark.day12
@pytest.mark.parametrize(
    "line, damages, expected",
    [
        ("???.###", [1, 1, 3], 1),
        (".??..??...?##.", [1, 1, 3], 4),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        ("????.#...#...", [4, 1, 1], 1),
        ("????.######..#####.", [1, 6, 5], 4),
        ("?###????????", [3, 2, 1], 10),
    ],
)
def test_line_permutations(line, damages, expected):
    actual = part.get_line_permutations(line, damages)
    assert actual == expected


@pytest.mark.day12
@pytest.mark.parametrize(
    "map, damage_groups, expected",
    [
        (
            [
                ".#",
            ],
            [[1]],
            ([".#?.#?.#?.#?.#"], [[1, 1, 1, 1, 1]]),
        ),
        (
            ["???.###"],
            [[1, 1, 3]],
            (
                ["???.###????.###????.###????.###????.###"],
                [[1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3]],
            ),
        ),
    ],
)
def test_unfold(map, damage_groups, expected):
    actual_map, actual_damage_groups = part.unfold(map, damage_groups)
    assert actual_map == expected[0]
    assert actual_damage_groups == expected[1]

@pytest.mark.day12
@pytest.mark.parametrize(
    "line, damages, expected",
    [
        ("???.###", [1, 1, 3], 1),
        ("????.#...#...", [4, 1, 1], 16),
        ("????.######..#####.", [1, 6, 5], 2500),
        (".??..??...?##.", [1, 1, 3], 16384),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        ("?###????????", [3, 2, 1], 506250),
    ],
)
def test_unfolded_line_permutations(line, damages, expected):
    new_line = line
    for _ in range(4):
        new_line += f"?{line}"
    actual = part.get_line_permutations(new_line, damages*5)
    assert actual == expected
