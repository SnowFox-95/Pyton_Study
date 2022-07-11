"""
Merge lists 1
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два
отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в
один отсортированный список.

Примечание 1. Списки list1 и list2 могут иметь разную длину.

Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.

Примечание 3. Следующий программный код:

print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
должен выводить:

[1, 2, 3, 5, 6, 7, 8]
[1, 5, 6, 7, 10, 13, 16, 20]
"""


# объявление функции c сортировкой пузырьком
def merge_puz(list1, list2):
    list3 = list1 + list2
    for i in range(len(list3) - 1):
        for j in range(len(list3) - i - 1):
            if list3[j] > list3[j + 1]:
                list3[j], list3[j + 1] = list3[j + 1], list3[j]
    return list3


# объявление функции c сортировкой выбором
def merge_sel(list1, list2):
    list3 = list1 + list2
    for i in range(len(list3) - 1):
        for j in range(i + 1, len(list3)):
            if list3[j] < list3[i]:
                list3[j], list3[i] = list3[i], list3[j]
    return list3


# объявление функции c методом sort()
def merge_sort(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию

print('Соединение списков и сортировка пузырьком', merge_puz(numbers1, numbers2))
print('Соединение списков и сортировка выбором', merge_sel(numbers1, numbers2))
print('Соединение списков и сортировка методом sort()', merge_sort(numbers1, numbers2))
