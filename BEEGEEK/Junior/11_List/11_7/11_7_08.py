"""
Списочное выражение 2
На вход программе подается строка текста, содержащая целые числа. Напишите программу,
использующую списочное выражение, которая выведет кубы указанных чисел также на одной
строке.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенные символом
пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Для вывода элементов списка используйте цикл for.

Примечание 2. Используйте метод split().
"""
print(*[int(i) ** 3 for i in input().split()])
