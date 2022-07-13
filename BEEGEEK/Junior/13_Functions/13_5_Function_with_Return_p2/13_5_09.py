"""
Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента
непустую строку text, состоящую из символов ( и ) и возвращает значение True если
поступившая на вход строка является правильной скобочной последовательностью и False в
противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая
 только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая
 скобка.

Примечание 2. Следующий программный код:

print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
должен выводить:

True
False
"""


# объявление функции
def is_correct_bracket(text):
    if ')' == text[0] or '(' == text[-1]:
        return False
    else:
        weigth = 0
        for i in range(len(text)):
            if text[i] == '(':
                weigth += 1
            else:
                weigth -= 1
            if weigth == -1:
                break
        if weigth == 0:
            return True
        else:
            return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

# tests DONOTCOPY!!!
print('#1', is_correct_bracket('((()))'))  # 1
print('#2', is_correct_bracket('(()())'))  # 2
print('#3', is_correct_bracket('(())()'))  # 3
print('#4', is_correct_bracket('()(())'))  # 4
print('#5', is_correct_bracket('()()()'))  # 5
print('#6', is_correct_bracket('()(())()()()(())()(()())((()))'))  # 6
print('#7', is_correct_bracket('()(())()(()())((()))()(())'))  # 7
print('#8', is_correct_bracket('())()()()('))  # 8
print('#9', is_correct_bracket(')))((('))  # 9
print('#10', is_correct_bracket('()(())()((())((()))()(())'))  # 10
print('#11', is_correct_bracket('()(())()(()())((()))()(()'))  # 11
print('#12', is_correct_bracket(')(())()(()())((()))()(())'))  # 12
print('#13', is_correct_bracket('())(()'))  # 13
print('#14', is_correct_bracket(')))'))  # 14
print('#15', is_correct_bracket('(((('))  # 15
print('#16', is_correct_bracket('())((((())))'))  # 16
