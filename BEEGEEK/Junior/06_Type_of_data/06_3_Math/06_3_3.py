'''Площадь и длина
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.

Формат входных данных
На вход программе подается одно вещественное число R.

Формат выходных данных
Программа должна вывести два числа – площадь круга и длину окружности радиуса R.'''

from math import pow, pi

r = float(input())
s = pi * pow(r, 2)
print(s)
c = 2 * pi * r
print(c)
