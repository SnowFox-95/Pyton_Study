"""
    Арифметическая прогрессия
Арифметической прогрессией называется последовательность чисел a_1, a_2, ..., a_n,
каждое из которых, начиная с a_2, получается из предыдущего прибавлением к нему одного
и того же постоянного числа dd (разность прогрессии), то есть:

    a_n=a_{n−1}+d

Если известен первый член прогрессии и её разность, то n-ый член арифметической прогрессии
находится по формуле:

    a_n=a_1+d(n-1)

Входные данные
На вход программе подаётся три целых числа: a_1  , d и n, каждое на отдельной строке.

Выходные данные
Программа должна вывести n-ый член арифметической прогрессии.
"""

# put your python code here
a_1 = int(input())
d = int(input())
n = int(input())

print(a_1 + (d * (n - 1)))
