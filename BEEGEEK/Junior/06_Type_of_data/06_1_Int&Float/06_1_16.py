"""
Манхэттенское расстояние
Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его
параллельно-перпендикулярных улиц.
На плоскости манхэттенское расстояние между двумя точками (p_1; p_2) и (q_1; q_2)
определяется так |p_1-q_1|+|p_2-q_2|.
Напишите программу определяющую манхэттенское расстояние между двумя точками,
координаты которых заданы.

Формат входных данных
На вход программе подается четыре целых числа, каждое на отдельной строке – p_1, p_2,
q_1, q_2
.

Формат выходных данных
Программа должна вывести одно число – манхэттенское расстояние.
"""

p_1, p_2, q_1, q_2 = int(input()), int(input()), int(input()), int(input())

print(abs(p_1 - q_1) + abs(p_2 - q_2))
