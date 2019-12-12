import itertools
from aoc19.day09.day09 import IntCode


class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Turn:
    LEFT = 0
    RIGHT = 1


class Action:
    PAINT = 'PAINT'
    TURN = 'TURN'


class Color:
    BLACK = 0
    WHITE = 1


class Robot:
    def __init__(self, pos=(0, 0), direction=Direction.UP):
        self.pos = pos
        self.direction = direction
        self.panels = {}
        self.mode = itertools.cycle([Action.PAINT, Action.TURN])

    def run(self, program):
        program = IntCode(program,
                          get_input=self.get_input,
                          output=self.output)
        program.run()

    def run_from_input(self):
        program = IntCode.from_input(get_input=self.get_input,
                                     output=self.output)
        program.run()

    def get_input(self):
        color = self.panels.get(self.pos, Color.BLACK)
        return int(color == Color.WHITE)

    def output(self, value):
        mode = next(self.mode)
        func = getattr(self, mode.lower())
        func(value)

    def paint(self, color):
        self.panels[self.pos] = color

    def move(self):
        d = self.direction
        x, y = self.pos
        if d == Direction.UP:
            self.pos = (x, y + 1)
        elif d == Direction.RIGHT:
            self.pos = (x + 1, y)
        elif d == Direction.DOWN:
            self.pos = (x, y - 1)
        elif d == Direction.LEFT:
            self.pos = (x - 1, y)

    def turn(self, side):
        if side == Turn.LEFT:
            incr = -1
        elif side == Turn.RIGHT:
            incr = 1
        else:
            raise ValueError
        direction = (self.direction + incr + 4) % 4
        self.direction = direction
        self.move()


def part1():
    r = Robot()
    r.run_from_input()
    return len(r.panels)


if __name__ == '__main__':
    print(part1())
