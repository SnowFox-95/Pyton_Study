"""
BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с
необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные
  числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента
строковое значение пароля password и возвращает значение True если пароль является
  действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False
"""


# объявление функции
def is_valid_password(password):
    list_pass = password.split(':')
    if len(list_pass) == 3:
        first = int((list_pass[0]))
        second = int((list_pass[1]))
        third = int((list_pass[2]))
        first_check = is_palindrome(str(first))
        second_check = is_prime(second)
        third_check = is_even(third)
        if first_check == True and second_check == True and third_check == True:
            return True
        else:
            return False
    else:
        return False


def is_palindrome(text):
    clean_rev_text = text[::-1].replace(' ', '').replace('.', '').replace(',', ''). \
        replace('!', '').replace('?', '').replace('-', '').lower()
    clean_text = text[:].replace(' ', '').replace('.', '').replace(',', ''). \
        replace('!', '').replace('?', '').replace('-', '').lower()
    if len(clean_text) == len(clean_rev_text):
        count = 0
        for i in range(len(clean_text)):
            if clean_text[i] == clean_rev_text[i]:
                count += 1
        if count == len(clean_text) and count == len(clean_rev_text):
            return True
        else:
            return False
    else:
        return False


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
