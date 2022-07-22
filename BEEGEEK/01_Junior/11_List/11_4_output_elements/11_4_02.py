"""
Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
"""
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
summ_cube = 0
for num in numbers:
    summ_cube += num**2
print(summ_cube)
