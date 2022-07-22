"""
Negatives, Zeros and Positives
На вход программе подается натуральное число n, а затем n целых чисел. Напишите
программу, которая сначала выводит все отрицательные числа, затем нули, а затем все
положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же
порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на
отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
n = int(input())
list_of_n = []
for i in range(n):
    x = int(input())
    list_of_n.append(x)
list_of_neg = []
list_of_zer = []
list_of_poz = []
for i in range(len(list_of_n)):
    if list_of_n[i] < 0:
        list_of_neg.append(list_of_n[i])
    elif list_of_n[i] == 0:
        list_of_zer.append(list_of_n[i])
    else:
        list_of_poz.append(list_of_n[i])
list_of_sort_n = list_of_neg + list_of_zer + list_of_poz
print(*list_of_sort_n,sep='\n')
