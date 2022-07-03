'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].

Числа a, b, c и d являются натуральными и не превосходят 10,  a≤b, c≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.
'''

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print('', end = '\t')
for g in range(c, d + 1):
    print(g, end='\t')
for i in range(a, b + 1):
    print()
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
print()
