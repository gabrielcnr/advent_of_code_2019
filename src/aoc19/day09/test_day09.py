import pytest

from day09 import IntCode


def test_1():
    program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    L = []
    machine = IntCode(program, output=L.append)
    machine.run()
    assert L == program


def test_2():
    program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    L = []
    machine = IntCode(program, output=L.append)
    machine.run()
    assert len(str(L[0])) == 16


def test_3():
    program = [104, 1125899906842624, 99]
    L = []
    machine = IntCode(program, output=L.append)
    machine.run()
    assert L[0] == 1125899906842624


def test_day5():
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    L = []
    machine = IntCode(program, output=L.append, get_input=lambda: 8)
    machine.run()
    assert L[0] == 1


@pytest.mark.parametrize(
    ['in_', 'out'],
    [
        (8, 1000),
        (10, 1001),
        (5, 999),
    ]

)
def test_day5_2(in_, out):
    program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
               1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
               999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]


    L = []
    machine = IntCode(program, output=L.append, get_input=lambda: in_)
    machine.run()
    output, = L
    assert output == out

