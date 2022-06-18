'''
Напишите программу, которая считывает список чисел lst из первой строки и число x из
второй строки, которая выводит все позиции, на которых встречается число x в
переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку
"Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''

list = [int(i) for i in input().split()]
x = int(input())
count = 0
for i in range(0, len(list)):
    if list[i] == x:
        print(i, end=" ")
        count += 1
if count == 0:
    print('Отсутствует')