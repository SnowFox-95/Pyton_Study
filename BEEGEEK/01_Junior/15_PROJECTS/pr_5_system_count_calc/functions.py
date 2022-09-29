import time

list_system = ['hex', 'oct', 'qua', 'bin']


def is_valid_system(n_sys):
    global list_system
    if n_sys in list_system:
        return True


def interface_calc():
    print("Сейчас посчитаю", end='')
    print('\r', end='')
    time.sleep(1)
    print("Сейчас посчитаю.", end='')
    print('\r', end='')
    time.sleep(1)
    print("Сейчас посчитаю..", end='')
    print('\r', end='')
    time.sleep(1)
    print("Сейчас посчитаю...", end='')
    print('\r', end='')
    time.sleep(1)
    print("Готово!")


def calculation(dig, n_sys):
    global list_system
    if n_sys == list_system[0]:
        rez = calc_hex(dig)
        return int(rez)
    elif n_sys == list_system[1]:
        rez = calc_oct(dig)
        return int(rez)
    elif n_sys == list_system[2]:
        rez = calc_qua(dig)
        return int(rez)
    else:
        rez = calc_bin(dig)
        return int(rez)


def calc_bin(dig):
    len_dig = len(dig)
    summ = 0
    for i in range(1, len_dig + 1):
        digit = int(dig[-i])
        summ += int(digit * (2 ** (i - 1)))
    return summ


def calc_qua(dig):
    len_dig = len(dig)
    summ = 0
    # TODO transfer qua -> dec
    return summ


def calc_oct(dig):
    len_dig = len(dig)
    summ = 0
    # TODO transfer oct -> dec
    return summ


def calc_hex(dig):
    len_dig = len(dig)
    summ = 0
    # TODO transfer hex -> dec
    return summ
