"""
Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" –
соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите
программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 00.
"""

str = input()
count_R = 0
max_R = 0
for i in range(len(str)):
    if str[i] == 'Р':
        count_R += 1
        if count_R > max_R:
            max_R = count_R
    else:
        if count_R > max_R:
            max_R = count_R
            count_R = 0
        else:
            count_R = 0
print(max_R)
