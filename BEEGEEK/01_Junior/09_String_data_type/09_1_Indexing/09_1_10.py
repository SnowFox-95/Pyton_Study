"""
Цифра 1
На вход программе подается одна строка состоящая из цифр. Напишите программу, которая
считает сумму цифр данной строки.

Формат входных данных
На вход программе подается одна строка состоящая из цифр.

Формат выходных данных
Программа должна вывести сумму цифр данной строки.
"""

num_str = input()
num = int(num_str)
sum = 0
while num != 0:
    last_digit = num % 10
    sum += last_digit
    num //= 10
print(sum)