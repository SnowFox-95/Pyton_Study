"""
Считайте число (см таблицу) в арабской записи и выведите на печать, соответствующую ему римскую цифру:
1 - I
5 - V
10 - X
50 - L
100 - C
500 - D
1000 - M
"""
arab = int(input())
if arab == 1:
    print('I')
elif arab == 5:
    print('V')
elif arab == 10:
    print('X')
elif arab == 50:
    print('L')
elif arab == 100:
    print('C')
elif arab == 500:
    print('D')
else:
    print('M')
