'''
На вход программе подается число n > 1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.

Формат входных данных
На вход программе подается одно натуральное число n.

Формат выходных данных
Программа должна вывести наименьший делитель отличный от 11.

Примечание. Используйте оператор break при обнаружении делителя.
'''

n = int(input())
private = 0
for i in range(1,n+1):
    if n%i==0 and i!=1:
       private = i
       break

print(private)