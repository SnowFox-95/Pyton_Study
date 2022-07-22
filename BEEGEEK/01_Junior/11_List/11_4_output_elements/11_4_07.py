"""
Google search - 2 🌶️🌶️
На вход программе подается натуральное число n, затем n строк, затем число k —
количество поисковых запросов, затем k строк — поисковые запросы. Напишите программу,
которая выводит все введенные строки, в которых встречаются все поисковые запросы.

Формат входных данных
На вход программе подаются натуральное число n — количество строк, затем сами строки в
указанном количестве, затем число k, затем сами поисковые запросы.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречаются все поисковые
запросы.

Примечание. Поиск не должен быть чувствителен к регистру символов.
"""
n = int(input())
list_of_n = []
search_str = ''
search_rez = []
for i in range(n):
    x = input()
    list_of_n.append(x)

k = int(input())
searching_list = []
for i in range(k):
    search = input()
    searching_list.append(search)

for i in range(len(list_of_n)):
    count = 0
    search_str = list_of_n[i]
    for j in range(len(searching_list)):
        control_str = searching_list[j]
        if control_str.lower() in search_str.lower():
            count += 1

    if count == k:
        search_rez.append(search_str)
print(*search_rez, sep='\n')
