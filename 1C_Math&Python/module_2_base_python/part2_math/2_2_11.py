"""
Додекаэдр





На вход программа получает 1 строку - длину ребра додекаэдра.

Используя формулы из Wiki найдите площадь поверхности и объём фигуры.

Ответ округлите до 2 знака после запятой.
"""
from math import sqrt, pow


def square(el_a):
    s = (3 * (pow(el_a, 2))) * sqrt(5 * (5 + 2 * sqrt(5)))
    return round(s, 2)


def volume(el_a):
    v = ((a ** 3) / 4) * (15 + 7 * sqrt(5))
    return round(v, 2)


if __name__ == "__main__":
    a = int(input())
    print(square(a))
    print(volume(a))
