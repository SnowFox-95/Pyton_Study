'''
Количество дней
Дан порядковый номер месяца (1,2,…, 12). Напишите программу, которая выводит на экран количество дней в этом месяце.
Принять, что год является невисокосным.

Примечание. Постарайтесь написать программу, так чтобы в ней было не более трех условий.

Формат входных данных
На вход программе подаётся одно целое число – порядковый номер месяца.

Формат выходных данных
Программа должна вывести количество дней в этом месяце.
'''

m = int(input())

if m == 1 or m == 3 or m == 5 or 7 == m or m == 8 or m == 10 or m == 12:
    print('31')
elif m == 4 or m == 6 or m == 9 or m == 11:
    print('30')
else:
    print('28')
