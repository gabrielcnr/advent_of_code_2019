def closest_distance(wire_1, wire_2):
    points_1 = set(iter_wire_points(wire_1))
    points_2 = set(iter_wire_points(wire_2))
    intersection = points_1 & points_2
    import pdb; pdb.set_trace()
    sorted_intersection = sorted(intersection, key=lambda p: sum(p))
    return sorted_intersection[0]


def iter_wire_points(wire):
    x, y = (0, 0)
    for ins in wire:
        direction = ins[0]
        offset = int(ins[1])
        if direction == 'R':
            x += offset
        elif direction == 'L':
            x -= offset
        elif direction == 'U':
            y += offset
        elif direction == 'D':
            y -= offset
        yield (x, y)


def test_simple():
    wire_1 = ['R8', 'U5', 'L5', 'D3']
    wire_2 = ['U7', 'R6', 'D4', 'L4']
    assert 6 == closest_distance(wire_1, wire_2)
