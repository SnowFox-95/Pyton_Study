'''
max и min
Дано натуральное число  n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).
'''
n = int(input())
print('Максимальная цифра равна',int(max(str(n))))
print('Минимальная цифра равна',int(min(str(n))))