"""
        sum()
Функция sum() принимает на вход массив(любого типа) чисел и находит их сумму:
[Image: https://ucarecdn.com/53e9cdd2-ea5f-455d-9966-cf3a03b0ce22/]
Считайте строку, содержащую произвольное количество целых чисел и найдите их сумму.
"""


def main(L):
    summ = 0
    p = list(map(int, L))
    for i in range(0, len(p)):
        summ += p[i]
    print(summ)


if __name__ == "__main__":
    List = input().split(' ')
    main(List)
