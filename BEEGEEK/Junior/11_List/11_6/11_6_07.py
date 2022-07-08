"""
Количество артиклей
На вход программе подается строка, содержащая английский текст. Напишите программу,
которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

Формат входных данных
На вход программе подается строка, содержащая английский текст. Слова текста разделены
символом пробела.

Формат выходных данных
Программа должна вывести общее количество артиклей 'a', 'an', 'the' вместе с
поясняющим текстом.

Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.
"""
str = input()
count = 0
list_str = str.lower().split(' ')
for i in range(len(list_str)):
    if list_str[i] == 'a' or list_str[i] == 'an' or list_str[i] == 'the':
        count += 1
print('Общее количество артиклей:', count)
