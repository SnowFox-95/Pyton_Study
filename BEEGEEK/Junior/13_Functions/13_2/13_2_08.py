"""
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.
"""


# объявление функции
def draw_triangle(fill, base):
    for i in range(base // 2 + 1):
        for j in range(i + 1):
            print(fill, end='')
        print()
    for i in range(base // 2 - 1, -1, -1):
        for j in range(i + 1):
            print(fill, end='')
        print()


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
