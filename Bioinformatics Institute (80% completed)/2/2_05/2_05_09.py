'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки.
'''

a = [int(i) for i in input().split()]
sum = 0
for j in (range(len(a))):
    sum += a[j]

print(sum)
