'''
Сортировка трёх 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
'''

a = int(input())
b = int(input())
c = int(input())

min_a_c = min(a,b,c)
max_a_c = max(a,b,c)

if min_a_c == a: # если а минимум
    if max_a_c == b: # если b максимум
        print(max_a_c,'\n',c,'\n',min_a_c,sep="") # b c a
    else:
        print(max_a_c, '\n', b, '\n', min_a_c, sep="") # c b a
elif min_a_c ==b: # если b минимум
    if max_a_c == a: # если a максимум
        print(max_a_c,'\n',c,'\n',min_a_c,sep="") # a c b
    else:
        print(max_a_c, '\n', a, '\n', min_a_c, sep="") # c a b
elif min_a_c ==c : # если c минимум
    if max_a_c == b: # если b максимум
        print(max_a_c,'\n',a,'\n',min_a_c,sep="") # b a c
    else:
        print(max_a_c, '\n', b, '\n', min_a_c, sep="") # a b c