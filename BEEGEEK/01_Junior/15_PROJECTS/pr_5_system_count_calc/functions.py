import time


def is_valid_system(n_sys):
    list_system = ['hex', 'oct', 'qua', 'bin']
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
