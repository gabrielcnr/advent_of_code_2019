from aoc19.day12.day12 import Moon, MoonSystem, apply_gravity


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
