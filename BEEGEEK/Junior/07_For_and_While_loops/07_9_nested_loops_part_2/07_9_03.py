"""
Делители-1 🌶️
На вход программе подается два натуральных числа a и b (a < b). Напишите программу,
которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два числа на одной строке, разделенных пробелом: число с
максимальной суммой делителей и сумму его делителей.

Примечание. Если таких чисел несколько, то выведите наибольшее из них.
"""


'''summ_count = 0
max_x = 0

for x in range(a,b+1):
    count = 0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
        if count>=summ_count:
            summ_count=count
            max_x=x
print (max_x, summ_count)'''
a, b = int(input()), int(input())
counter = 0
largest = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
        if total >= counter and i >= largest:
            counter = total
            largest = i
print(largest, counter)
