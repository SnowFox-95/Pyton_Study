"""
Магические даты
Магическая дата – это дата, когда день, умноженный на месяц, равен числу
образованному последними двумя цифрами года.

Напишите функцию, is_magic(date) которая принимает в качестве аргумента строковое
представление корректой даты и возвращает значение True если дата является магической
и False в противном случае.

Примечание. Следующий программный код:

print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))
должен выводить:

True
False
"""


# объявление функции
def is_magic(date):
    list_date = date.split('.')
    day_date = int(list_date[0])
    month_date = int(list_date[1])
    year_date = int(str(list_date[2])[-2:])
    if day_date * month_date == year_date:
        return True
    else:
        return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
