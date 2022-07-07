"""
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех
пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму
квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
после этого считывание продолжать не нужно.

В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма
этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то,
что остались ещё не прочитанные значения.
"""

sqr = sum_sqr = 0
sum = 1
count_sum = 1
while sum != 0:
    a = int(input())
    if count_sum != 0:
        count_sum -= 1
        sum -= 1
        sqr = a ** 2
        sum_sqr += sqr
        sum += a
    else:
        sqr = a ** 2
        sum_sqr += sqr
        sum += a
        if sum == 0:
            break

print(sum_sqr)