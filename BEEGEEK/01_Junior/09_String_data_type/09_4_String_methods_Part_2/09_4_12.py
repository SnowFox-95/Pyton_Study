"""
.com or .ru
На вход программе подается строка текста. Напишите программу, которая проверяет,
что строка заканчивается подстрокой .com или .ru.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com
или .ru и «NO» в противном случае.
"""
str = input()
if str.endswith('.com') is True or str.endswith('.ru') is True:
    print('YES')
else:
    print('NO')
