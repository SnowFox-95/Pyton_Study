"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса
средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются. Номер
класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста
используется натуральное число, но при подсчёте среднего требуется вычислить значение
в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для
классов с первого по одиннадцатый). Если про какой-то класс нет информации,
необходимо вывести напротив него прочерк.

В качестве ответа прикрепите файл с полученными данными о среднем росте.
"""

avg = dict()
for i in range(1, 12):
    avg[i] = 0

with open('datasets/dataset_3_07_5.txt', 'r') as f:
    l = list()
    for line in f:
        l.append(line.strip().split('\t'))

for key in avg.keys():
    cnt = 0
    for pup in l:
        if int(pup[0]) == key:
            cnt += 1
            avg[key] += int(pup[2])

    if cnt == 0:
        avg[key] = '-'
    else:
        avg[key] /= cnt

with open('outputs/outputs_3_07_5.txt', 'w') as f:
    for i in range(1, 12):
        f.write(str(i) + ' ' + str(avg[i]) + '\n')
