"""
Целая часть от деления.
Считайте 2 целых числа, каждое с новой строки.

Найдите целую часть от деления первого на второе.
"""


def main(el_a, el_b):
    rez = el_a / el_b
    return int(rez)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(main(a, b))
