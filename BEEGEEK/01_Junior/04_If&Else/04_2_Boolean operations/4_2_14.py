"""
Ход ладьи
Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья
попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа
должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном
случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматная ладья ходит по горизонтали или вертикали.
"""

fcol = int(input())
fstr = int(input())
lcol = int(input())
lstr = int(input())

if (fcol > lcol and lstr == fstr) or (fcol < lcol and lstr == fstr) or (
        fcol == lcol and lstr < fstr) or (
        fcol == lcol and lstr > fstr):
    print('YES')
else:
    print('NO')
