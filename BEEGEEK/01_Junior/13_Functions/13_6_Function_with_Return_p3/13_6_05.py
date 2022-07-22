"""
Корни уравнения 🌶️🌶️
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых
числа a, b, c – коэффициенты квадратного уравнения ax^2+bx+c = 0ax
2
 +bx+c=0 и возвращает его корни в порядке возрастания.

Примечание 1. С подобной задачей мы уже сталкивались.

Примечание 2. Гарантируется, что квадратное уравнение имеет корни.

Примечание 3. Следующий программный код:

print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
должен выводить:

-1.0 5.0
1.0 2.5
-1.0 -1.0
"""
from math import pow, sqrt


# объявление функции
def solve(a, b, c):
    diskr = pow(b, 2) - 4 * a * c
    if diskr > 0:
        x_1 = (-b + sqrt(diskr)) / (2 * a)
        x_2 = (-b - sqrt(diskr)) / (2 * a)
    else:
        x_1 = -b / (2 * a)
        x_2 = x_1
    return min(x_1, x_2), max(x_1, x_2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

# TESTS DONOTCOPY!
x1, x2 = solve(1, -4, -5)
print(x1, x2)
x1, x2 = solve(-2, 7, -5)
print(x1, x2)
x1, x2 = solve(1, 2, 1)
print(x1, x2)
x1, x2 = solve(22, 34, -8)
print(x1, x2)
x1, x2 = solve(-22, 34, -8)
print(x1, x2)
x1, x2 = solve(5, 20, 20)
print(x1, x2)
