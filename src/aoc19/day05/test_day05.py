from unittest import mock
from aoc19.day05.day05 import (opcode_3,
                               opcode_4,
                               parse_instruction,
                               Mode,
                               execute,
                               get_input, output,
                               read_value)


@mock.patch('aoc19.day05.day05.get_input')
def test_opcode_3(mock_get_input):
    mock_get_input.return_value = 777
    ins_pointer = 2
    state = [1, 0, 3, 6, 8, 8, 8, 8]

    new_pos = opcode_3(state, ins_pointer, None, mock_get_input, output)

    assert 4 == new_pos
    assert [1, 0, 3, 6, 8, 8, 777, 8] == state


@mock.patch('aoc19.day05.day05.output')
@mock.patch('aoc19.day05.day05.get_input')
def test_opcode_4(mock_get_input, mock_output):
    mock_get_input.return_value = 7676

    ins_pointer = 3
    state = [9, 312, 5, 4, 1, 99]

    new_pos = opcode_4(state, ins_pointer, None, get_input, mock_output)

    assert 5 == new_pos
    assert [9, 312, 5, 4, 1, 99] == state
    [(args, kwargs)] = mock_output.call_args_list
    assert (312,) == args


def test_parse_instruction():
    assert (2, 0, 1, 0) == parse_instruction(1002)


def test_read_value():
    state = [1, 2, 3, 4, 5, 6]
    assert 3 == read_value(state, 3, Mode.IMMEDIATE)
    assert 4 == read_value(state, 3, Mode.POSITION)


def test_opcode_1():
    state = [1001, 4, 5, 6, 11, 22, -1, 99]

    execute(state, 0, get_input, output)

    assert [1001, 4, 5, 6, 11, 22, 16, 99] == state
