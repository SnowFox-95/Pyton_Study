"""
            Арифметические операции
Напишите программу, в которой вычисляется сумма, разность и произведение двух целых
чисел, введенных с клавиатуры.

Формат входных данных
    На вход программе подаётся два целых числа, каждое на отдельной строке.

Формат выходных данных
    Программа должна вывести сумму, разность и произведение введённых чисел, каждое на
    отдельной строке.

"""
# put your python code here
a = int(input())
b = int(input())

print(a, '+', b, '=', a + b, sep=' ')
print(a, '-', b, '=', a - b, sep=' ')
print(a, '*', b, '=', a * b, sep=' ')
