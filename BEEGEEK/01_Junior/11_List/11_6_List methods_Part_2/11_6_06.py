"""
Переставить min и max
На вход программе подается строка текста, содержащая различные натуральные числа. Из
данной строки формируется список чисел. Напишите программу, которая меняет местами
минимальный и максимальный элемент этого списка.

Формат входных данных
На вход программе подается строка текста, содержащая различные натуральные числа,
разделенные символом пробела.

Формат выходных данных
Программа должна вывести строку текста в соответствии с условием задачи.

Примечание. Используйте подходящие встроенные функции и списочные методы.
"""
str = input()
list_str = str.split(' ')
for i in range(len(list_str)):
    list_str[i] = int(list_str[i])
min_list_str = min(list_str)
max_list_str = max(list_str)
max_index = list_str.index(max_list_str)
min_index = list_str.index(min_list_str)
list_str[min_index], list_str[max_index] = list_str[max_index], list_str[min_index]
print(*list_str)
