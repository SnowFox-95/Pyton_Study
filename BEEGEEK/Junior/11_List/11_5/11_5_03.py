"""
Построчный вывод
На вход программе подается строка текста. Напишите программу, которая выводит слова
введенной строки в столбик.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
str = input()
list_str = str.split()
print(*list_str, sep='\n')
