'''
Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:

«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

Формат входных данных
На вход программе подаётся строка – название футбольной команды.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

club = input()

print ('Футбольная команда '+club+' имеет длину '+str(len(club))+' символов')