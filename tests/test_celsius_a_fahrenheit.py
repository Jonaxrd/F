import pytest
from celsius_a_fahrenheit import celsius_a_fahrenheit


def test_conversion_correcta():
    assert celsius_a_fahrenheit(25) == 77


def test_caso_limite_cero_celsius():
    assert celsius_a_fahrenheit(0) == 32


def test_error_con_texto():
    with pytest.raises(TypeError):
        celsius_a_fahrenheit("veinte")