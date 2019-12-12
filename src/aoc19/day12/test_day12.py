# from aoc19.day12.day12 import Moon
import itertools

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Moon:
    position: Tuple
    velocity: Tuple

    @classmethod
    def create(cls, pos):
        return cls(position=pos, velocity=(0, 0, 0))

    def apply_velocity(self):
        new_position = tuple(p + v for p, v in zip(self.position, self.velocity))
        self.position = new_position

    @property
    def potential_energy(self):
        return sum(abs(v) for v in self.position)

    @property
    def kinetic_energy(self):
        return sum(abs(v) for v in self.velocity)

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy


class MoonSystem:
    def __init__(self, moons):
        self.moons = moons

    # def __iter__(self):
    #     while True:
    #         yield

    def next(self):
        for a, b in itertools.combinations(self.moons, 2):
            # if a is self.moons[0] or b is self.moons[0]:
            #     import pdb; pdb.set_trace()
            apply_gravity(a, b)
            # if a is self.moons[0] or b is self.moons[0]:
            #     print(self.moons[0].velocity)
        for moon in self.moons:
            moon.apply_velocity()

    @property
    def total_energy(self):
        return sum(m.total_energy for m in self.moons)


def apply_gravity(a, b):
    a_velocity = list(a.velocity)
    b_velocity = list(b.velocity)
    for i, (a_pos, b_pos) in enumerate(zip(a.position, b.position)):
        if a_pos > b_pos:
            b_incr = 1
            a_incr = -1
        elif a_pos < b_pos:
            b_incr = -1
            a_incr = 1
        else:
            b_incr = 0
            a_incr = 0
        a_velocity[i] += a_incr
        b_velocity[i] += b_incr
    a.velocity = tuple(a_velocity)
    b.velocity = tuple(b_velocity)


def test_apply_gravity():
    callisto = Moon.create((5, 2, 3))
    ganymede = Moon.create((3, 2, 4))

    apply_gravity(callisto, ganymede)

    assert callisto.velocity == (-1, 0, 1)
    assert ganymede.velocity == (1, 0, -1)


def test_apply_velocity():
    europa = Moon(position=(1, 2, 3), velocity=(-2, 0, 3))
    europa.apply_velocity()
    assert (-1, 2, 6) == europa.position


def test_example():
    moon_1 = Moon.create((-1, 0, 2))
    moon_2 = Moon.create((2, -10, -7))
    moon_3 = Moon.create((4, -8, 8))
    moon_4 = Moon.create((3, 5, -1))
    system = MoonSystem([moon_1, moon_2, moon_3, moon_4])

    system.next()

    assert moon_1.velocity == (3, -1, -1)
    assert moon_1.position == (2, -1, 1)

    assert moon_2.velocity == (1, 3, 3)
    assert moon_2.position == (3, -7, -4)

    assert moon_3.velocity == (-3, 1, -3)
    assert moon_3.position == (1, -7, 5)

    assert moon_4.velocity == (-1, -3, 1)
    assert moon_4.position == (2, 2, 0)

    # advance to 10th step
    for _ in range(9):
        system.next()

    assert moon_1.velocity == (-3, -2, 1)
    assert moon_1.position == (2, 1, -3)

    assert moon_2.velocity == (-1, 1, 3)
    assert moon_2.position == (1, -8, 0)

    assert moon_3.velocity == (3, 2, -3)
    assert moon_3.position == (3, -6, 1)

    assert moon_4.velocity == (1, -1, -1)
    assert moon_4.position == (2, 0, 4)
