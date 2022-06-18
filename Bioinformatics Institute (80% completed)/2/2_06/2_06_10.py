'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде
последовательности строк. После последней строки матрицы идёт строка, содержащая
только строку "end".

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j
равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему
направлению.
'''
a = [list(map(int, s.split())) for s in iter(input, 'end')]
for row in [
    [a[i - 1][j] + a[(i + 1) % len(a)][j] + a[i][j - 1] + a[i][(j + 1) % len(a[i])] for j
     in range(len(a[i]))] for i in range(len(a))]:
    print(*row)
