"""
    Пересчет временного интервала
Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину,
 выраженную в часах и минутах.

Формат входных данных
    На вход программе подаётся целое число – количество минут.

Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.
"""

# put your python code here
a = int(input())
hour = a // 60
minute = a % 60
print(a, 'мин - это', hour, 'час', minute, 'минут.', sep=' ')
