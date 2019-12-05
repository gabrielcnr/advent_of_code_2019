from day02 import run_intcode


def test_run_intcode():
    intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    assert 3500 == run_intcode(intcode)
