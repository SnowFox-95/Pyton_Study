"""
Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку
text и возвращает значение True если указанный текст является палиндромом и False в
противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также
 игнорируйте пробелы, а также символы , . ! ? -.

Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
должен выводить:

True
True
False
"""


# объявление функции
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


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
