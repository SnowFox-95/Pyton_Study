"""
В институте биоинформатики по офису передвигается робот. Недавно студенты из группы
программистов написали для него программу, по которой робот, когда заходит в комнату,
считает количество программистов в ней и произносит его вслух: "n программистов".
Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное
окончание слова.
Напишите программу, считывающую с пользовательского ввода целое число n (
неотрицательное), выводящее это число в консоль вместе с правильным образом
изменённым словом "программист", для того, чтобы робот мог нормально общаться с
людьми, например: 1 программист, 2 программиста, 5 программистов.
В комнате может быть очень много программистов. Проверьте, что ваша программа
правильно обработает все случаи, как минимум до 1000 человек.
Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше
решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из
случаев входных данных (число программистов 0≤n≤1000). Обязательно проверяйте свои
решения на дополнительных значениях, а не только на тех, что приведены в условии
задания. Так как задание повышенной сложности, вручную код решений проверяться не
будет. Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте,
что вы используете только русские символы для ответа. В остальных случаях ищите
ошибку в логике работы программы.
"""

prog_int = int(input())
lng_prog = len(str(prog_int))
prog2 = (prog_int % 100) // 10  # вторая с конца цифра
prog_last = prog_int % 10  # последняя цифра
if lng_prog == 1:
    # для 1 символа
    if (prog_int == 0) or (5 <= prog_int <= 9):  # если 0 или от 5 до 9
        print(str(prog_int) + ' программистов')
    elif 2 <= prog_int <= 4:
        print(str(prog_int) + ' программиста')
    elif prog_int == 1:
        print(str(prog_int) + ' программист')
elif 2 <= lng_prog <= 3:
    if prog2 == 1:
        print(str(prog_int) + ' программистов')
    else:
        if prog_last == 0:
            print(str(prog_int) + ' программистов')
        elif 5 <= prog_last <= 9:
            print(str(prog_int) + ' программистов')
        elif prog_last == 1:
            print(str(prog_int) + ' программист')
        elif 2 <= prog_last <= 4:
            print(str(prog_int) + ' программиста')
else:
    print(str(prog_int) + ' программистов')
