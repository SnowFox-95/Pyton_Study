"""
Середина отрезка
Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве
аргументов координаты концов отрезка (x_1;  y_1)и (x_2; y_2) и возвращает координаты
точки являющейся серединой данного отрезка.

Примечание 1. Координаты середины отрезка вычисляются по формуле:
x_1+x_2/2; y_1+y_2/2

Примечание 2. Следующий программный код:

print(get_middle_point(0, 0, 10, 0))
print(get_middle_point(1, 5, 8, 3))
должен выводить:

5.0 0.0
4.5 4.0
"""


# объявление функции
def get_middle_point(x1, y1, x2, y2):
    x_middle = (x1 + x2) / 2
    y_middle = (y1 + y2) / 2
    return x_middle, y_middle


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# Tests. DONOTCOPY!
x, y = get_middle_point(1, 1, 2, 2)
print(x, y)
x, y = get_middle_point(-10, 10, 0, 100)
print(x, y)
x, y = get_middle_point(10, 10, 10, 20)
print(x, y)
