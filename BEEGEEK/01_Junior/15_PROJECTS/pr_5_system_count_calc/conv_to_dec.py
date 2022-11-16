# convert 2 -> 10
def calc_in_bin(dig):
    len_dig = len(dig)
    summ = 0
    for i in range(1, len_dig + 1):
        digit = int(dig[-i])
        summ += int(digit * (2 ** (i - 1)))
    return summ


# convert 4 -> 10
def calc_in_qua(dig):
    len_dig = len(dig)
    summ = 0
    for i in range(1, len_dig + 1):
        digit = int(dig[-i])
        summ += int(digit * (4 ** (i - 1)))
    return summ


# convert 8 -> 10
def calc_in_oct(dig):
    len_dig = len(dig)
    summ = 0
    for i in range(1, len_dig + 1):
        digit = int(dig[-i])
        summ += int(digit * (8 ** (i - 1)))
    return summ


# convert 16 -> 10
def calc_in_hex(dig):
    len_dig = len(dig)
    summ = 0
    for i in range(1, len_dig + 1):
        hex_list = "a b c d e f".split(' ')
        digit = str(dig[-i]).lower()
        if digit in hex_list:
            for j in range(0, len(hex_list)):
                if digit == hex_list[j]:
                    digit = int('1' + str(j))
                    summ += int(digit * (16 ** (i - 1)))
                else:
                    continue
        else:
            digit = int(digit)
            summ += int(digit * (16 ** (i - 1)))
    return summ
