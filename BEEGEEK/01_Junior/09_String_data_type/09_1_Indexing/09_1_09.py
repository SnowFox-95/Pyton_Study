"""
ФИО
На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу,
которая выводит инициалы человека.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести ФИО человека.

Примечание. Гарантируется, что имя, фамилия и отчество начинаются с заглавной буквы.
"""
N_string = input()
F_string = input()
O_string = input()

print(F_string[0] + N_string[0] + O_string[0])
