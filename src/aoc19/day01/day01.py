def calculate_required_fuel(mass):
    return (mass // 3) - 2


def calculate_required_fuel_until_zero(mass):
    total_fuel = 0
    fuel = mass
    while (fuel := calculate_required_fuel(fuel)) > 0:
        total_fuel += fuel
    return total_fuel


def sum_fuel_requirements(modules, strategy):
    return sum(strategy(mass) for mass in modules)


def read_input():
    with open('input.txt') as fp:
        return (int(v.strip()) for v in fp.readlines())


def solve(strategy):
    masses = read_input()
    return sum_fuel_requirements(masses, strategy)


def part1():
    return solve(calculate_required_fuel)


def part2():
    return solve(calculate_required_fuel_until_zero)


if __name__ == '__main__':
    print(part1())
    print(part2())
