"""
Калькулятор доставки
Интернет магазин осуществляет экспресс доставку для своих товаров по цене 1000
рублей за первый товар и 120 рублей за каждый последующий товар. Напишите функцию
get_shipping_cost(quantity), которая принимает в качестве аргумента натуральное число
 quantity – количество товаров в заказе и возвращает стоимость доставки.

Примечание. Следующий программный код:

print(get_shipping_cost(1))
print(get_shipping_cost(3))
должен выводить:

1000
1240
"""


# объявление функции
def get_shipping_cost(quantity):
    quantity = quantity - 1
    cost = 1000 + (120*quantity)
    return cost


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))