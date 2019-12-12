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
