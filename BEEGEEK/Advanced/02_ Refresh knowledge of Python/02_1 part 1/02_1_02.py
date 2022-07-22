"""
На easy
На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:

    - сумму чисел a и b;
    - разность чисел a и b;
    - произведение чисел a и b;
    - частное чисел a и b;
    - целую часть от деления числа a на b;
    - остаток от деления числа a на b;
    - корень квадратный из суммы их 10-х степеней: sqrt(a^10 + b^10).
Формат входных данных
На вход программе подаются два целых числа a и b , (b!=0), каждое на отдельной строке.

Формат выходных данных
Программа должна вывести результаты математических операций в соответствии с условием
задачи.
"""
from math import pow, sqrt

a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(sqrt(pow(a, 10) + pow(b, 10)))