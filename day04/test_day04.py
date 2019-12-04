from day04 import check, check_2


def test_check():
    assert check(111111)
    assert not check(223450)
    assert not check(123789)


def test_check_2():
    assert check_2(112233)
    assert not check_2(123444)
    assert check_2(111122)
    assert not check_2(124444)
    assert check_2(113444)
