"""
Группа биологов в институте биоинформатики завела себе черепашку.

После дрессировки черепашка научилась понимать и запоминать указания биологов
следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после
слова — это положительное расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что
можно написать программу, которая определит, куда в итоге биологи приведут черепашку.
Для этого программисты просят вас написать программу, которая выведет точку, в которой
окажется черепашка после всех команд. Для простоты они решили считать, что движение
начинается в точке (0, 0), и движение на восток увеличивает первую координату,
а на север — вторую.

Программе подаётся на вход число команд n, которые нужно выполнить черепашке,
после чего n строк с самими командами. Вывести нужно два числа в одну строку: первую и
вторую координату конечной точки черепашки. Все координаты целочисленные.
"""

n = int(input())
movement = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}

for _ in range(n):
    direction = input().split()
    if direction[0] in movement:
        movement[direction[0]] += int(direction[1])

x = movement['восток'] - movement['запад']
y = movement['север'] - movement['юг']

print(x, y)