'''
Возрастная группа
Напишите программу, которая по введённому возрасту пользователя сообщает,
к какой возрастной группе он относится:

    до 13 включительно – детство;
    от 14 до 24 – молодость;
    от 25 до 59 – зрелость;
    от 60 – старость.
Формат входных данных
    На вход программе подаётся одно целое число – возраст пользователя.

Формат выходных данных
    Программа должна вывести название возрастной группы.
'''

a = int(input())

if a<=13:
    print('детство')
else:
    if (a>=14) and (a<=24):
        print('молодость')
    else:
        if (a>=25) and (a<=59):
            print('зрелость')
        else:
            print('старость')