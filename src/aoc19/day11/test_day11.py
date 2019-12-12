import pytest
from aoc19.day11.day11 import Robot, Direction, Turn


@pytest.mark.parametrize(
    ['direction', 'expected_pos'],
    [
        (Direction.UP, (0, 1)),
        (Direction.RIGHT, (1, 0)),
        (Direction.DOWN, (0, -1)),
        (Direction.LEFT, (-1, 0)),
    ]
)
def test_move(direction, expected_pos):
    r = Robot(direction=direction)
    r.move()
    assert expected_pos == r.pos


def test_sanity():
    r = Robot()
    for _ in range(4):
        r.turn(Turn.RIGHT)
    assert r.pos == (0, 0)

def test_sanity_2():
    r = Robot()
    for _ in range(4):
        r.turn(Turn.LEFT)
    assert r.pos == (0, 0)


def test_example():
    pass
