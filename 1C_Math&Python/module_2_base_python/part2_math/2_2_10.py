"""
9 друзей шестиугольника
На плоскости нарисован правильный шестиугольник с длиной стороны a.
У 3 сторон шестиугольника нарисовали по квадрату с длиной стороны, равной стороне шестиугольника.
Оставшиеся 3 стороны разделили пополам, после чего нарисовали по равностороннему треугольнику, касающемуся каждого из получившихся половинных отрезков.
[Image: https://ucarecdn.com/6244aaf8-2910-4445-b8ab-ef734eafdb52/]
Найдите площадь получившейся фигуры.
На вход подаётся 1 строка - длина стороны шестиугольника.
Ответ округлите до целых.
"""
from math import pow, sqrt


def square_triangle(el_a):
    s = (sqrt(3) / 4) * pow(el_a, 2)
    return s


def square_hexagon(el_a):
    s = (3 * sqrt(3) * pow(el_a, 2)) / 2
    return s


def square_quadrilateral(el_a):
    s = el_a ** 2
    return s


def main(el_a):
    a_tri = el_a / 2
    s_tri = square_triangle(a_tri)
    s_qua = square_quadrilateral(el_a)
    s_hex = square_hexagon(el_a)
    rez = (6 * s_tri) + (3 * s_qua) + s_hex
    return round(rez)


if __name__ == "__main__":
    a = int(input())
    print(main(a))
