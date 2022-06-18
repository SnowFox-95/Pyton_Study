'''
Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.
'''

city1 = input()
city2 = input()
city3 = input()

len_city1 = len(city1)
len_city2 = len(city2)
len_city3 = len(city3)
min_city = min(len_city1, len_city2, len_city3)
max_city = max(len_city1, len_city2, len_city3)

if min_city == len_city1:
    print(city1)
    if max_city == len_city2:
        print(city2)
    else:
        print(city3)
elif min_city == len_city2:
    print(city2)
    if max_city == len_city1:
        print(city1)
    else:
        print(city3)
else:
    print(city3)
    if max_city == len_city1:
        print(city1)
    else:
        print(city2)
