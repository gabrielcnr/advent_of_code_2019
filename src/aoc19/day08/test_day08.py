from aoc19.day08.day08 import iter_layers, calculate_final_pixels

def test_iter():
    expected = [
        [('1', '2', '3'), ('4', '5', '6')],
        [('7', '8', '9'), ('0', '1', '2')],
    ]

    assert expected == list(iter_layers('123456789012', 3, 2))


def test_calculate_final_pixels():
    expected = [
        ('0', '1'),
        ('1', '0'),
    ]

    assert expected == list(calculate_final_pixels('0222112222120000', 2, 2))

