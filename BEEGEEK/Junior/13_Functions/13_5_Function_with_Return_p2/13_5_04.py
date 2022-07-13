"""
Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента
натуральное число num и возвращает первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

 Примечание 2. Следующий программный код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:

7
11
17
"""


# объявление функции
def get_next_prime(num):
    flag = True

    for i in range(num + 1, 1000):
        count = 0
        for j in range(1, 1000):
            if i % j == 0:
                count += 1
        if count == 2:
            flag = False
            break
    return i


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
