"""
However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).


Part 2
-------
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
"""
from collections import Counter


def check(n):
    n = str(n)
    has_double = False
    for d1, d2 in zip(n, n[1:]):
        if d1 == d2:
            has_double = True
        if d2 < d1:
            return False
    return has_double


def iter_good_passwords(passwords):
    for password in passwords:
        if check(password):
            yield password


def check_2(password):
    counter = Counter(str(password))
    return 2 in counter.values()


def iter_good_passwords_2(passwords):
    for password in iter_good_passwords(passwords):
        if check_2(password):
            yield password


def get_input():
    return range(372037, 905157 + 1)


def part1():
    numbers = get_input()
    return sum(1 for p in iter_good_passwords(numbers))


def part2():
    numbers = get_input()
    return sum(1 for p in iter_good_passwords_2(numbers))


if __name__ == '__main__':
    print(part1())
    print(part2())
