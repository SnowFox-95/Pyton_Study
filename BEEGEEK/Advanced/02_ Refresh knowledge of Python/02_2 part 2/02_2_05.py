"""
Различные элементы
На вход программе подается строка текста, содержащая натуральные числа, расположенные
по неубыванию. Из строки формируется список чисел. Напишите программу для подсчета
количества разных элементов в списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные
символом пробела, расположенные по неубыванию.

Формат выходных данных
Программа должна вывести одно число – количество различных элементов списка.

Примечание. Задачу можно решить без множеств.
"""
str = input().split()

count = 1
for i in range(0, len(str)-1):
    if int(str[i]) < int(str[i + 1]):
        count += 1
print(count)
