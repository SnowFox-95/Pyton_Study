'''
Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.
'''
n = int(input())
count_n = 0
len_n = len(str(n))
for i in range(len_n):
    if str(n)[i]!=str(n)[0]:
        count_n+=1
if count_n==0:
    print('YES')
else:
    print('NO')