'''
Средние значения
В математике выделяют следующие средние значения:

среднее арифметическое чисел a и b: (a+b)/2;

среднее геометрическое чисел a и b: sqrt(a*b);

среднее гармоническое чисел a и b: 2a*b/a+b;

среднее квадратичное чисел aa и bb: sqrt((a^2+b^2)/2).
'''

'''
Формат входных данных
На вход программе подается два вещественных числа aa и bb​, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
'''

from math import sqrt, pow

a = float(input())
b = float(input())

arithmetic_mean = (a + b) / 2
geometric_mean = sqrt(a * b)
harmonic_mean = (2 * a * b) / (a + b)
root_mean_square = sqrt((pow(a, 2) + pow(b, 2)) / 2)

print(arithmetic_mean, geometric_mean, harmonic_mean, root_mean_square, sep='\n')
