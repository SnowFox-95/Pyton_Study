"""
Цифра 2
На вход программе подается одна строка. Напишите программу, которая выводит сообщение
«Цифра» (без кавычек), если строка содержит цифру. В противном случае вывести
сообщение «Цифр нет» (без кавычек).

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

"""

str = input()
count = 0
for i in range(len(str)):
    if str[i] == '0' or str[i] == '1' or str[i] == '2' or str[i] == '3' or str[i] == \
            '4' or str[i] == '5' or str[i] == '6' or str[i] == '7' or str[i] == '8' or \
            str[i] == '9':
        count += 1
if count == 0:
    print('Цифр нет')
else:
    print('Цифра')
