"""
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и
возвращающую количество делителей данного числа.

Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

Примечание 2. Следующий программный код:

print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))
"""


# объявление функции
def number_of_factors(num):
    counter = 0
    list_factors = [i for i in range(1, num + 1) if num % i == 0]
    for i in range(len(list_factors)):
        counter += 1
    return counter


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
