import pytest
from day03 import (closest_intersecting_point, calculate_distance,
                   calculate_intersection_with_fewest_steps)


@pytest.mark.parametrize(
    ['wire_1', 'wire_2', 'distance'],
    [
        # case 1
        [
            ['R8', 'U5', 'L5', 'D3'],
            ['U7', 'R6', 'D4', 'L4'],
            6,
        ],

        # case 2
        [
            ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
            ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
            159,
        ],

        # case 3
        [
            ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
            ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
            135,
        ],

    ]
)
def test_simple(wire_1, wire_2, distance):
    p = closest_intersecting_point(wire_1, wire_2)
    assert distance == calculate_distance(p)


def test_fewest_intersections_simple():
    wire_1 = ['R8', 'U5', 'L5', 'D3']
    wire_2 = ['U7', 'R6', 'D4', 'L4']
    assert 30 == calculate_intersection_with_fewest_steps(wire_1, wire_2)
