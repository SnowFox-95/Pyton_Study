'''
Сумма чисел
На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.

Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.

Формат выходных данных
Программа должна вывести сумму членов данной последовательности.
'''
summa = 1
n = int(input())
while n>=0:
    summa +=n
    n = int(input())
print(summa-1)