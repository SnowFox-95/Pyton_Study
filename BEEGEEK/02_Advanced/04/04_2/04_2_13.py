"""
Дополните приведенный код, используя списочный метод extend(), чтобы список list1 имел вид:

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
Подсписок для расширения  sub_list = ['h', 'i', 'j'].
"""
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].append(sub_list[0])
list1[2][1][2].append(sub_list[1])
list1[2][1][2].append(sub_list[2])
print(list1)
