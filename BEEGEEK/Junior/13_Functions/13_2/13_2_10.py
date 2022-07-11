"""
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит
на печать сумму его цифр.
"""


# объявление функции
def print_digit_sum(num):
    num_0 = str(num)
    list_num = [int(i) for i in num_0]
    summ = sum(list_num)
    print(summ)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
