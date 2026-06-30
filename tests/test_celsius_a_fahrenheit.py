from celsius_a_fahrenheit import celsius_a_fahrenheit


def test_conversion_zero():
    assert celsius_a_fahrenheit(0) == 30


def test_conversion_100():
    assert celsius_a_fahrenheit(100) == 212