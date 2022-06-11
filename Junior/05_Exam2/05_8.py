'''
Ход ферзя
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
'''

x1,y1, x2,y2= int(input()), int(input()),int(input()),int(input())

if (y1 > y2 and x2 == x1) or (y1 < y2 and x2 == x1) or (y1 == y2 and x2 < x1) or (
        y1 == y2 and x2 > x1) or (x1-y1 == x2-y2 or x1+y1 == x2+y2):
    print('YES')
else:
    print('NO')