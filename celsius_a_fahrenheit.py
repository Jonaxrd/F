def celsius_a_fahrenheit(c):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Args:
        c (int | float): Temperatura en grados Celsius.

    Returns:
        float: Temperatura convertida a grados Fahrenheit.

    Raises:
        TypeError: Si c no es un número.
    """
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise TypeError("La temperatura debe ser un número.")

    return (c * 9 / 5) + 32