"""
Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения
символа a в строке. Проблема заключается в том, что данный метод не находит
местоположение всех символов а.

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента:
строку target и символ symbol и возвращает список, содержащий все местоположения этого
символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой
список.

Примечание 2. Следующий программный код:

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))
"""


# объявление функции
def find_all(target, symbol):
    finded_list = []
    for c in range(len(target)):
        if target[c] == symbol:
            finded_list.append(c)
    return finded_list


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
