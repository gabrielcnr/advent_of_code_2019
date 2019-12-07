import itertools

from aoc19.day05.day05 import run_intcode, read_input

class Amplifier:
    def __init__(self, amp_num, phase_setting, input_signal, intcode):
        self.amp_num = amp_num
        self._inputs = (i for i in (phase_setting, input_signal))
        self.intcode = intcode[:]

    def get_input(self):
        return next(self._inputs)

    def run(self):
        outputs = []
        run_intcode(self.intcode, self.get_input, outputs.append)
        return outputs[0]


def get_thruster_signal(phase_setting_sequence, intcode):
    # create the amplifiers
    input_signal = 0
    for amp_num in range(5):
        phase_setting = int(phase_setting_sequence[amp_num])
        amp = Amplifier(amp_num, phase_setting, input_signal, intcode)
        output = amp.run()
        input_signal = output
    return output


def part1():
    intcode = read_input()
    return max(
        get_thruster_signal(phase_setting_sequence, intcode)
        for phase_setting_sequence in itertools.permutations(range(5), 5)
    )


if __name__ == '__main__':
    print(part1())
