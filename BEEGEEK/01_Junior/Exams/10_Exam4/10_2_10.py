"""
Второе вхождение
На вход программе подается строка текста. Напишите программу, которая выводит индекс
второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите
число -1, а если не встречается ни разу, выведите число -2.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

str = input()
count = str.count('f')
#print(count)
new_str = str.replace('f','a',1)
#print(new_str)
if count == 1:
    print('-1')
elif count == 0:
    print('-2')
else:
    print(new_str.find('f'))
