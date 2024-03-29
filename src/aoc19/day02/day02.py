import itertools

ADD = 1
MUL = 2
HALT = 99


def run_intcode(intcode):
    pos = 0
    while (opcode := intcode[pos]) != HALT:
        idx_1, idx_2, idx_3 = intcode[pos + 1:pos + 4]
        value_1 = intcode[idx_1]
        value_2 = intcode[idx_2]
        if opcode == ADD:
            intcode[idx_3] = value_1 + value_2
        elif opcode == MUL:
            intcode[idx_3] = value_1 * value_2
        else:
            raise RuntimeError(f'invalid opcode: {opcode}')
        pos += 4
    return intcode[0]


def read_input():
    with open('input.txt') as fp:
        contents = fp.read()
    return [int(n) for n in contents.strip().split(',')]


def part1():
    intcode = read_input()
    intcode[1] = 12
    intcode[2] = 2
    return run_intcode(intcode)


def part2():
    _intcode = read_input()
    for noun, verb in itertools.product(range(100), range(100)):
        intcode = _intcode[:]
        intcode[1] = noun
        intcode[2] = verb
        output = run_intcode(intcode)
        if output == 19690720:
            return noun, verb
    return None, None

if __name__ == '__main__':
    print(part1())
    noun, verb = part2()
    if noun is not None:
        print(f'part2: {100 * noun + verb}')
