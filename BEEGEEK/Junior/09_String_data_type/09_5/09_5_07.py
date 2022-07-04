"""
Дополните приведенный код, используя форматирование строк с помощью метода format,
 так чтобы он вывел текст:

«In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).
"""
#Исходный код
"""
s = 'In {0}, someone paid {1} {2} for two pizzas.'
print()
"""
year = 2010
count ='10k'
valute = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year,count,valute)
print(s)