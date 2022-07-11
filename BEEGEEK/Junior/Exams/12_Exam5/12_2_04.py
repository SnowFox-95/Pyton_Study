"""
Валидный номер 🌶️🌶️
На вход программе подается строка текста. Напишите программу, которая определяет
является ли введенная строка корректным телефонным номером. Строка текста является
корректным телефонным номером если она имеет формат:

abc-def-hijk или
7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести «YES» если строка является корректным телефонным номером и
«NO» в противном случае.

Примечание. Телефонный номер должен содержать только цифры и символ -, а количество
цифр в каждой группе должны быть правильным.
"""
number = input()
list_len_n = [len(i) for i in number.split("-")]
control_summ = 0
for c in number:
    new_number = number.replace('-', '')
# print(new_number)
if list_len_n == [3, 3, 4] or list_len_n == [1, 3, 3, 4]:
    if new_number[0] == '7':
        for c in new_number:
            if c.isdigit():
                control_summ += 1
        #print(control_summ)
        if control_summ == 11:
            print('YES')
        else:
            print('NO')
    else:
        for c in new_number:
            if c.isdigit():
                control_summ += 1
        #print(control_summ)
        if control_summ == 10:
            print('YES')
        else:
            print('NO')
else:
    print('NO')
