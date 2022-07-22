"""
Зодиак
Китайский гороскоп назначает животным годы в 12-летнем цикле. Один 12-летний цикл
показан в таблице ниже. Таким образом, 2012 год будет очередным годом дракона.

Год	    Животное
2000	Дракон
2001	Змея
2002	Лошадь
2003	Овца
2004	Обезьяна
2005	Петух
2006	Собака
2007	Свинья
2008	Крыса
2009	Бык
2010	Тигр
2011	Заяц
Напишите программу, которая считывает год и отображает название связанного с ним
животного. Ваша программа должна корректно работать с любым годом, не только теми,
что перечислены в таблице.

Формат входных данных
На вход программе подается одно целое число – год.

Формат выходных данных
Программа должна вывести текст – название животного.
"""
year = int(input())
anim = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык",
        "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
x = year % 12
print(anim[x])
