"""
На вход подаётся строка из 3 целых чисел. Найдите сумму чисел.
"""


def summ(l):
    s = 0
    for i in range(0, 3):
        s += int(l[i])
    return s


if __name__ == "__main__":
    listing = input().split(' ')

    print(summ(listing))
