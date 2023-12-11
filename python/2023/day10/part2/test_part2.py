import pytest
from day10.part2 import part2 as part
import os

# @pytest.mark.skip
@pytest.mark.day10
@pytest.mark.parametrize(
    "inpufilename, expected",
    [
        # ("test-input.txt", 4),
        ("test-input-3.txt", 4), # this fails
        ("test-input-4.txt", 4), # this passes
    ],
)
def test_main_answer(inpufilename, expected):
    actual_result = part.main(inpufilename)
    assert actual_result == expected

test_map_1 = ['-L|F7', '7S-7|', 'L|7||', '-L-J|', 'L|-JF']
test_map_2 = ['7-F7-', '.FJ|7', 'SJLL7', '|F--J', 'LJ.LJ']
test_loop_1 = [(2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (2, 3), (2, 2)]
test_loop_2 = [(3, 1), (4, 1), (5, 1), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (3, 5), (3, 4), (2, 4), (1, 4), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1)]

@pytest.mark.day10
@pytest.mark.parametrize(
        "map, expected",
        [
            (test_map_2, (2, 0)),
            (test_map_1, (1, 1))
        ]
)
def test_start_coord(map, expected):
    actual = part.get_starting_position(map=map)
    assert actual == expected

@pytest.mark.day10
@pytest.mark.parametrize(
        "map, node, expected",
        [
            (test_map_2, (1, 0), True),
            (test_map_1, (1, 1), False),
            (test_map_2, (2, 0), False),
            (test_map_1, (1, 1), False)

        ]
)
def test_north(map, node, expected):
    actual = part.check_north(map=map, node=node)
    assert actual == expected

@pytest.mark.day10
@pytest.mark.parametrize(
        "map, node, expected",
        [
            (test_map_1, (1, 1), True),
            (test_map_2, (2, 0), True),

        ]
)
def test_south(map, node, expected):
    actual = part.check_south(map=map, node=node)
    assert actual == expected

@pytest.mark.day10
@pytest.mark.parametrize(
        "map, node, expected",
        [
            (test_map_1, (1, 1), True),
            (test_map_2, (2, 0), True),

        ]
)
def test_east(map, node, expected):
    actual = part.check_east(map=map, node=node)
    assert actual == expected

@pytest.mark.day10
@pytest.mark.parametrize(
        "map, node, expected",
        [
            (test_map_2, (2, 0), False),
            (test_map_1, (1, 1), False)

        ]
)
def test_west(map, node, expected):
    actual = part.check_west(map=map, node=node)
    assert actual == expected

@pytest.mark.day10
@pytest.mark.parametrize(
        "current_symbol, prev_node, current_node, expected",
        [
            # balrol
            ("-", (2, 2), (2, 3), (2, 4)),
            ("7", (2, 2), (2, 3), (3, 3)),
            ("J", (2, 2), (2, 3), (1, 3)),
            # jobbrol
            ("-", (2, 3), (2, 2), (2, 1)),
            ("L", (2, 3), (2, 2), (1, 2)),
            ("F", (2, 3), (2, 2), (3, 2)),
            # fentrol
            ("|", (1, 3), (2, 3), (3, 3)),
            ("J", (1, 3), (2, 3), (2, 2)),
            ("L", (1, 3), (2, 3), (2, 4)),
            # lentrol
            ("|", (3, 3), (2, 3), (1, 3)),
            ("7", (3, 3), (2, 3), (2, 2)),
            ("F", (3, 3), (2, 3), (2, 4)),
        ]
)
def test_get_next_node(current_symbol, current_node, prev_node, expected):
    actual = part.get_next_node(current_symbol=current_symbol, current_node=current_node, prev_node=prev_node)
    assert actual == expected

@pytest.mark.day10
@pytest.mark.parametrize(
    "map, loop, line, expected",
    [
        (part.parse_input("test-input.txt"), part.get_loop(part.parse_input("test-input.txt")), 3, 1),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 1, 0),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 2, 0),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 3, 0),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 4, 0),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 5, 0),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 6, 0),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 7, 4),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 8, 0),
        (part.parse_input("test-input-3.txt"), part.get_loop(part.parse_input("test-input-3.txt")), 9, 0),
        
    ]
)
def test_inside_count(map, loop, line, expected):
    actual = part.line_get_inside_count(map=map, loop=loop, line=line)
    assert actual == expected