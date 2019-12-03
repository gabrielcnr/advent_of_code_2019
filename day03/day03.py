import itertools


def closest_intersecting_point(wire_1, wire_2):
    points_1 = set(iter_wire_points(wire_1))
    points_2 = set(iter_wire_points(wire_2))
    intersection = points_1 & points_2
    intersection.remove((0, 0))
    sorted_intersection = sorted(intersection, key=calculate_distance)
    return sorted_intersection[0]


def calculate_distance(p):
    x, y = p
    return abs(x) + abs(y)


def iter_wire_points(wire):
    x, y = (0, 0)
    for ins in wire:
        direction = ins[0]
        offset = int(ins[1:])
        if direction == 'R':
            xvalues = range(x, x + offset + 1)
            yvalues = [y]
        elif direction == 'L':
            xvalues = range(x, x - offset - 1, -1)
            yvalues = [y]
        elif direction == 'U':
            xvalues = [x]
            yvalues = range(y, y + offset + 1)
        elif direction == 'D':
            xvalues = [x]
            yvalues = range(y, y - offset - 1, -1)
        for _x, _y in itertools.product(xvalues, yvalues):
            yield _x, _y
        x, y = _x, _y


def read_input():
    with open('input.txt') as fp:
        line_1, line_2 = fp.readlines()
    wire_1 = line_1.split(',')
    wire_2 = line_2.split(',')
    return wire_1, wire_2


def part1():
    wire_1, wire_2 = read_input()
    p = closest_intersecting_point(wire_1, wire_2)
    distance = calculate_distance(p)
    return distance


if __name__ == '__main__':
    print(part1())
