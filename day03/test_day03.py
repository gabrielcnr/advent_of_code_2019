from day03 import closest_intersecting_point, calculate_distance

def __test_simple():
    wire_1 = ['R8', 'U5', 'L5', 'D3']
    wire_2 = ['U7', 'R6', 'D4', 'L4']
    p = closest_intersecting_point(wire_1, wire_2)
    assert 6 == calculate_distance(p)

def test_2():
    wire_1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire_2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    p = closest_intersecting_point(wire_1, wire_2)
    assert 159 == calculate_distance(p)


def test_3():
    wire_1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire_2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    p = closest_intersecting_point(wire_1, wire_2)
    assert 135 == calculate_distance(p)
