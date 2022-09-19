"""
Площадь и периметр треугольника

Даны длины 3 сторон треугольника (каждая с новой строки).

Найдите:

    Периметр треугольника
    Площадь треугольника

на Wiki можно найти обе формулы, если забыли формулу Герона.

Примечание. Извлечение квадратного корня эквивалентно возведению в степень 0.5
"""
from math import sqrt


def perim(el_a, el_b, el_c):
    p = el_a + el_b + el_c
    return p


def square(el_a, el_b, el_c):
    p2 = perim(el_a, el_b, el_c) / 2
    s = sqrt(p2 * (p2 - el_a) * (p2 - el_b) * (p2 - el_c))
    return s


if __name__ == "__main__":
    a, b, c = int(input()), int(input()), int(input())
    print(perim(a, b, c))
    print(square(a, b, c))
