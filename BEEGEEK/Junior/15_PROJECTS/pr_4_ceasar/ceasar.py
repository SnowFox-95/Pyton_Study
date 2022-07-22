EN_LANG_UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
EN_LANG_LO = 'abcdefghijklmnopqrstuvwxyz'
RU_LANG_UP = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
RU_LANG_LO = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def dest_valid():
    while True:
        n = int(input('Необходимо зашифровать или дешифровать? 1 - дешифровка, '
                      '0- шифрование -> '))
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            print('Кажется нажата не та клавиша. Попробуй еще раз')
            continue


def lang_valid():
    while True:
        lang_v = input('Какой язык использовать? еn - английский, ru - русский -> ')
        if lang_v in ['en', 'англ', 'английский', 'e', 'а']:
            return True
        elif lang_v in ['ru', 'рус', 'русский', 'r', 'р']:
            return False
        else:
            print('Кажется выбрана неверная команда. Попробуй еще раз')
            continue


def ceasar_rot(destin, language, string, rotate):
    global EN_LANG_UP, EN_LANG_LO, RU_LANG_UP, RU_LANG_LO
    old_str = string
    rez_str = ''

    if destin:  # дешифровка
        if language:  # дешифр на английск
            for i in range(len(old_str)):
                if string[i] in EN_LANG_UP:
                    order = string[i].ord()
                    new_order = order - rotate % len(EN_LANG_UP)

                elif string[i] in EN_LANG_LO:
                    pass
                else:
                    continue
        else:  # дешифр на русск
            pass
    else:  # расшифровка
        if language:  # шифр на английск
            pass
        else:  # шифр на русск
            pass

    return rez_str


dest = dest_valid()  # по флагу True - дешифровка, по False - расшифровка
lang = lang_valid()  # по флагу True - английский, по False - русский

print('Какую фразу нужно зашифровать?')
str = input()

print('На сколько символов сдвигаем?')
rot = int(input())

print('Готовая строка: ')
print(ceasar_rot(dest, lang, str, rot))
