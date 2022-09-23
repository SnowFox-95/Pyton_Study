"""
Считайте 2 строки. Каждая строка содержит по 3 натуральных числа.
Найдите сумму чисел в каждой строке и выведите на печать одной строкой.
В качестве разделителя между двумя получившимися числами используйте символ "#"
"""


def summ(l1, l2):
    s = 0
    for i in range(0, 3):
        s += int(l1[i])
    rez = str(s)
    s = 0
    for i in range(0, 3):
        s += int(l2[i])
    rez = rez + '#' + str(s)
    return rez


if __name__ == "__main__":
    list1 = input().split(' ')
    list2 = input().split(' ')
    print(summ(list1, list2))
