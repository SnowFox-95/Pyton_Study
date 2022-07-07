"""
Алфавит
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка состоит из 26 символов z.
"""
list_of_alphabet = []
n = 1
for i in range(97, 97 + 26):
    str = chr(i) * n
    list_of_alphabet.append(str)
    n += 1
print(list_of_alphabet)
