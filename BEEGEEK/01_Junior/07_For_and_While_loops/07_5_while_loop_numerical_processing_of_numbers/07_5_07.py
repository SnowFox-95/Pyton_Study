'''
Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.
'''

n = int(input())
summa_n = 0
count_n=0
proizved_n=1
avr_n=0
first_n = int(str(n)[0])
last_n_of_n = int(str(n)[-1])
while n!=0:
    last_n = n%10
    summa_n+=last_n
    count_n+=1
    proizved_n*=last_n
    avr_n = summa_n/count_n
    n=n//10
print(summa_n)
print(count_n)
print(proizved_n)
print(avr_n)
print(first_n)
print(first_n+last_n_of_n)