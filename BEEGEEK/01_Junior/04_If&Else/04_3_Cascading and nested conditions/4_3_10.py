"""
Цвета колеса рулетки 🌶️
На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:

карман 0 зеленый;
для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

Формат входных данных
На вход программе подаётся одно целое число.

Формат выходных данных
Программа должна вывести цвет кармана либо сообщение «ошибка ввода», если введённое число лежит вне диапазона от 0 до 36.
"""

a = int(input())

if (1 <= a <= 10) and a % 2 == 0:  # чет 1-10
    print('черный')
elif (1 <= a <= 10) and not (a % 2 == 0):  # нечет 1-10
    print('красный')
elif (11 <= a <= 18) and a % 2 == 0:  # чет 11-18
    print('красный')
elif (11 <= a <= 18) and not (a % 2 == 0):  # нечет 11-18
    print('черный')
elif (19 <= a <= 28) and (a % 2 == 0):  # чет 19-28
    print('черный')
elif (19 <= a <= 28) and not (a % 2 == 0):  # нечет 19-28
    print('красный')
elif (29 <= a <= 36) and (a % 2 == 0):  # чет 29-36
    print('красный')
elif (29 <= a <= 36) and not (a % 2 == 0):  # нечет 29-36
    print('черный')
elif a == 0:
    print('зеленый')
else:
    print('ошибка ввода')