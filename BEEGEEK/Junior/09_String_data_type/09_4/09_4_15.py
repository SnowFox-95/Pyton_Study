"""
Удаление фрагмента
На вход программе подается строка текста, в которой буква «h» встречается минимум два
раза. Напишите программу, которая удаляет из этой строки первое и последнее вхождение
буквы «h», а также все символы, находящиеся между ними.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
string = input()
new_string = ''
new_string_1 = ''
new_string_2 = ''
h_find = string.find('h')
h_rfind = string.rfind('h')
if h_find == 0 and h_rfind == 1:
    new_string = ''
else:
    new_string = string[:h_find] + string[h_rfind+1:]
print(new_string)
