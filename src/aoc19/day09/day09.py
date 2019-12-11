import operator

END = object()

class Mode:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class IntCode:
    def __init__(self, program, output=None, get_input=None):
        self.pos = 0
        self.program = program
        self._output = output
        self._input = get_input
        self._relative_base = 0
        self.running = False

    @classmethod
    def from_input(cls, **kwargs):
        with open('input.txt') as fp:
            contents = fp.read()
        program = [int(n) for n in contents.strip().split(',')]
        return cls(program, **kwargs)

    def run(self):
        self.running = True
        while self.running:
            instruction = self.program[self.pos]
            opcode, *modes = self._parse_instruction(instruction)
            func = getattr(self, f'opcode_{opcode}')
            func(modes)

    def _parse_instruction(self, n):
        p3_mode, n = divmod(n, 10_000)
        p2_mode, n = divmod(n, 1_000)
        p1_mode, opcode = divmod(n, 100)
        return (opcode, p1_mode, p2_mode, p3_mode)

    def get_input(self):
        if self._input is None:
            raise RuntimeError('cannot read input')
        return self._input()

    def output(self, value):
        if self._output is not None:
            self._output(value)

    def opcode_1(self, modes):
        return self._opcode_add_mul(modes, operator.add)

    def opcode_2(self, modes):
        return self._opcode_add_mul(modes, operator.mul)

    def opcode_3(self, modes):
        """read input"""
        p1 = self.read_value(self.pos + 1)
        self.program[p1] = self.get_input()
        self.pos += 2

    def opcode_4(self, modes):
        """send to output"""
        p1 = self.read_value(self.pos + 1)
        value = self.program[p1]
        self.output(value)
        self.pos += 2

    # TODO: refactor opcode_5 and opcode_6
    def opcode_5(self, modes):
        """jump equal"""
        p1_mode, p2_mode, _ = modes
        p1 = self.read_value(self.pos + 1, p1_mode)
        p2 = self.read_value(self.pos + 2, p2_mode)
        if p1:
            self.pos = p2
        else:
            self.pos += 3

    def opcode_6(self, modes):
        """jump not equal"""
        p1_mode, p2_mode, _ = modes
        p1 = self.read_value(self.pos + 1, p1_mode)
        p2 = self.read_value(self.pos + 2, p2_mode)
        if not p1:
            self.pos = p2
        else:
            self.pos += 3

    # TODO: refactor opcodes 7 and 8
    def opcode_7(self, modes):
        p1_mode, p2_mode, _ = modes
        p1 = self.read_value(self.pos + 1, p1_mode)
        p2 = self.read_value(self.pos + 2, p2_mode)
        idx = self.program[self.pos + 3]
        self.program[idx] = int(p1 < p2)
        self.pos += 4

    def opcode_8(self, modes):
        p1_mode, p2_mode, _ = modes
        p1 = self.read_value(self.pos + 1, p1_mode)
        p2 = self.read_value(self.pos + 2, p2_mode)
        idx = self.program[self.pos + 3]
        self.program[idx] = int(p1 == p2)
        self.pos += 4

    def opcode_9(self, modes):
        p1_mode, _, _ = modes
        p1 = self.read_value(self.pos + 1, p1_mode)
        self._relative_base = p1
        self.pos += 2

    def opcode_99(self, modes):
        self.running = False

    def _opcode_add_mul(self, modes, op):
        p1_mode, p2_mode, p3_mode = modes
        p1 = self.read_value(self.pos + 1, p1_mode)
        p2 = self.read_value(self.pos + 2, p2_mode)
        p3 = self.read_value(self.pos + 3)
        self.program[p3] = op(p1, p2)
        self.pos += 4

    def read_value(self, value_or_addr, mode=Mode.IMMEDIATE):
        if mode == Mode.IMMEDIATE:
            return value_or_addr
        elif mode == Mode.POSITION:
            return self.program[value_or_addr]
        elif mode == Mode.RELATIVE:
            return self.program[value_or_addr + self._relative_base]
        else:
            raise RuntimeError(f'unexpected parameter mode: {mode}')


# def part1():
#     intcode = read_input()
#     return run_intcode(intcode)




if __name__ == '__main__':
    part1()
    # part2()
