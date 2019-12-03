ADD = 1
MUL = 2
HALT = 99

def run_intcode(intcode):
    pos = 0
    while True:
        opcode = intcode[pos]
        if opcode in {ADD, MUL}:
            idx_1, idx_2, idx_3 = intcode[pos+1:pos+4]
            value_1 = intcode[idx_1]
            value_2 = intcode[idx_2]
            if opcode == ADD:
                intcode[idx_3] = value_1 + value_2
            else:
                intcode[idx_3] = value_1 * value_2
            pos += 4
        elif opcode == HALT:
            return intcode[0]
        else:
            raise RuntimeError(f'invalid opcode: {opcode}')
