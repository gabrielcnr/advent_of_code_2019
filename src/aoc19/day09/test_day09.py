from day09 import IntCode


def test_1():
    program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    L = []
    machine = IntCode(program, output=L.append)
    machine.run()
    import pdb; pdb.set_trace()


def test_3():
    program = [104, 1125899906842624, 99]
    L = []
    machine = IntCode(program, output=L.append)
    machine.run()
    assert L[0] == 1125899906842624
