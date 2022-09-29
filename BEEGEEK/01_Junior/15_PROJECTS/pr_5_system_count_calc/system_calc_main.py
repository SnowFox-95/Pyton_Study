import functions

if __name__ == "__main__":
    print(
        "Привет! Я калькулятор систем счисления. Помогу перевести любое число в десятичную систему.\n"
        "Загадай число для перевода:"
    )
    digit = input()
    print(
        "Замечательно! \n"
        "А в какой системе счислений изначально это число? \n"
        "\n"
        "HEX - шестнадцатеричная, \n"
        "OCT - восмеричная, \n"
        "QUA - четверичная, \n"
        "BIN - бинарная(двоичная).\n"
    )
    while True:
        number_system = input()
        if functions.is_valid_system(number_system.lower()):
            functions.interface_calc()
            print("Результат = ", functions.calculation(digit, number_system))

        else:
            print(
                "Это первая версия калькулятора и функционал пока тут ограничен :( \n "
                "Пожалуйста, укажи из что-то из систем счисления о которых мне известно.\n"
                "\n"
                "HEX - шестнадцатеричная, \n"
                "OCT - восмеричная, \n"
                "QUA - четверичная, \n"
                "BIN - бинарная(двоичная).\n"
            )
