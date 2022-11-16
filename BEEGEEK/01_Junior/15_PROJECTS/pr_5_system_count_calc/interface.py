import time
from conv_to_dec import *
from conv_from_dec import *


def is_valid_menu(m_sys):
    m_sys_list = ["1", "2"]
    if m_sys in m_sys_list:
        return True
    else:
        return False


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


def calculation_in_dec(dig, n_sys) -> int:
    global list_system
    if n_sys == list_system[0]:
        rez = calc_in_hex(dig)
        return int(rez)
    elif n_sys == list_system[1]:
        rez = calc_in_oct(dig)
        return int(rez)
    elif n_sys == list_system[2]:
        rez = calc_in_qua(dig)
        return int(rez)
    else:
        rez = calc_in_bin(dig)
        return int(rez)


def calculation_from_dec(dig, n_sys) -> int:
    global list_system
    if n_sys == list_system[0]:
        rez = calc_from_hex(dig)
        return int(rez)
    elif n_sys == list_system[1]:
        rez = calc_from_oct(dig)
        return int(rez)
    elif n_sys == list_system[2]:
        rez = calc_from_qua(dig)
        return int(rez)
    else:
        rez = calc_from_bin(dig)
        return int(rez)
