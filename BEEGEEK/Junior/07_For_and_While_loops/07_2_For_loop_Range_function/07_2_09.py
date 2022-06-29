"""
Последовательность чисел 3 🌶️
Даны два целых числа m и n (m > n). Напишите программу, которая выводит все нечетные
числа от m до n включительно в порядке убывания.

Формат входных данных
На вход программе подаются два целых числа m и n, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести числа в соответствии с условием задачи.

Примечание. Попробуйте решить задачу двумя способами: с использованием условного
оператора if и без него.
"""

m = int(input())
n = int(input())

# вариант с if
for i in range(m, n - 1, -1):
    if not (i % 2 == 0):
        print(i)
