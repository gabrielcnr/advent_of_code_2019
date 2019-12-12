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


def create_moon_system():
    """
    <x=4, y=1, z=1>
    <x=11, y=-18, z=-1>
    <x=-2, y=-10, z=-4>
    <x=-7, y=-2, z=14>
    """
    m1 = Moon.create((4, 1, 1))
    m2 = Moon.create((11, -18, -1))
    m3 = Moon.create((-2, -10, -4))
    m4 = Moon.create((-7, -2, 14))
    system = MoonSystem([m1, m2, m3, m4])
    return system


def part1():
    system = create_moon_system()
    for _ in range(1000):
        system.next()
    return system.total_energy


if __name__ == '__main__':
    print(part1())
