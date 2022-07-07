"""
Корректный ip-адрес
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
Напишите программу, которая определяет является ли введенная строка текста корректным
ip-адресом.

Формат входных данных
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.

Формат выходных данных
Программа должна вывести «ДА», если введеная строка является корректным ip-адресом,
и «НЕТ» — в противном случае.

Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0
до 255 включительно.
"""
ip_address = input()
list_ip = ip_address.split('.')
count = 0
for i in range(len(list_ip)):
    part_ip = int(list_ip[i])
    if 0 <= part_ip <= 255:
        count += 1
if count == 4:
    print('ДА')
else:
    print("НЕТ")
