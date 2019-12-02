from day01 import calculate_required_fuel, calculate_required_fuel_until_zero


def test_calculate_required_fuel():
    assert 2 == calculate_required_fuel(12)
    assert 2 == calculate_required_fuel(14)
    assert 654 == calculate_required_fuel(1969)


def test_calculate_required_fuel_until_zero():
    assert 966 == calculate_required_fuel_until_zero(1969)
