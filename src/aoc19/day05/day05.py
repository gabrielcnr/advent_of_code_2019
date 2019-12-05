import operator

END = object()


class Mode:
    POSITION = 0
    IMMEDIATE = 1


def get_input():
    return 5
    # return 1


def opcode_3(state, pos, modes):
    dest_idx = state[pos + 1]
    state[dest_idx] = get_input()
    return pos + 2


def output(value):
    print(value)


def opcode_4(state, pos, modes):
    idx = state[pos + 1]
    value = state[idx]
    output(value)
    return pos + 2


def _opcode_add_mul(state, pos, modes, op):
    p1_mode, p2_mode, p3_mode = modes
    p1 = read_value(state, state[pos + 1], p1_mode)
    p2 = read_value(state, state[pos + 2], p2_mode)
    idx = state[pos + 3]
    state[idx] = op(p1, p2)
    return pos + 4


def opcode_1(state, pos, modes):
    return _opcode_add_mul(state, pos, modes, operator.add)


def opcode_2(state, pos, modes):
    return _opcode_add_mul(state, pos, modes, operator.mul)


def opcode_99(state, pos, modes):
    return END


# TODO: refactor opcode_5 and opcode_6
def opcode_5(state, pos, modes):
    p1_mode, p2_mode, _ = modes
    p1 = read_value(state, state[pos+1], p1_mode)
    p2 = read_value(state, state[pos+2], p2_mode)
    if p1:
        return p2
    else:
        return pos + 3


def opcode_6(state, pos, modes):
    p1_mode, p2_mode, _ = modes
    p1 = read_value(state, state[pos+1], p1_mode)
    p2 = read_value(state, state[pos+2], p2_mode)
    if not p1:
        return p2
    else:
        return pos + 3


def opcode_7(state, pos, modes):
    p1_mode, p2_mode, p3_mode = modes
    p1 = read_value(state, state[pos + 1], p1_mode)
    p2 = read_value(state, state[pos + 2], p2_mode)
    idx = state[pos + 3]
    state[idx] = int(p1 < p2)
    return pos + 4


def opcode_8(state, pos, modes):
    p1_mode, p2_mode, p3_mode = modes
    p1 = read_value(state, state[pos + 1], p1_mode)
    p2 = read_value(state, state[pos + 2], p2_mode)
    idx = state[pos + 3]
    state[idx] = int(p1 == p2)
    return pos + 4


def parse_instruction(n):
    p3_mode, n = divmod(n, 10_000)
    p2_mode, n = divmod(n, 1_000)
    p1_mode, opcode = divmod(n, 100)
    return (opcode, p1_mode, p2_mode, p3_mode)


def read_value(state, parameter, mode):
    if mode == Mode.IMMEDIATE:
        return parameter
    elif mode == Mode.POSITION:
        return state[parameter]
    else:
        raise RuntimeError(f'unexpected parameter mode: {mode}')


def execute(state, pos):
    instruction = state[pos]
    opcode, *modes = parse_instruction(instruction)
    func = globals().get(f'opcode_{opcode}')
    if func is not None:
        return func(state, pos, modes)

    assert False, f"something very bad happened! got opcode {opcode}"


def run_intcode(intcode):
    pos = 0
    while (pos := execute(intcode, pos)) != END:
        pass
    print('End.')


def read_input():
    with open('input.txt') as fp:
        contents = fp.read()
    return [int(n) for n in contents.strip().split(',')]


def part1():
    intcode = read_input()
    return run_intcode(intcode)


def part2():
    intcode = read_input()
    return run_intcode(intcode)


if __name__ == '__main__':
    # part1()
    part2()
