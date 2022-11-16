def calc_from_hex(dig):
    dig_list = []
    base = 16
    flag = True
    while flag == True:
        if int(dig / base) > base:
            subrez = int(dig % base)
            if subrez < 9:
                dig_list.append(str(subrez))
                dig = int(dig / base)
            else:
                if subrez == 10:
                    dig_list.append("A")
                elif subrez == 11:
                    dig_list.append("B")
                elif subrez == 12:
                    dig_list.append("C")
                elif subrez == 13:
                    dig_list.append("D")
                elif subrez == 14:
                    dig_list.append("E")
                else:
                    dig_list.append("F")
        else:
            subrez = int(dig % base)
            if subrez < 9:
                dig_list.append(str(subrez))
                dig = int(dig / base)
            else:
                if subrez == 10:
                    dig_list.append("A")
                elif subrez == 11:
                    dig_list.append("B")
                elif subrez == 12:
                    dig_list.append("C")
                elif subrez == 13:
                    dig_list.append("D")
                elif subrez == 14:
                    dig_list.append("E")
                else:
                    dig_list.append("F")
            dig_list.append(str(int(dig / base)))
            flag = False
            break

    rez = int(''.join(dig_list))
    return rez


def calc_from_oct(dig):
    dig_list = []
    base = 8
    flag = True
    while flag == True:
        if int(dig / base) > base:
            subrez = dig % base
            dig_list.append(str(subrez))
            dig = int(dig / base)
        else:
            dig_list.append(str(int(dig % base)))
            dig_list.append(str(int(dig / base)))
            flag = False
            break
    rez = int(''.join(dig_list))
    return rez


def calc_from_qua(dig):
    dig_list = []
    base = 4
    flag = True
    while flag == True:
        if int(dig / base) > base:
            subrez = dig % base
            dig_list.append(str(subrez))
            dig = int(dig / base)
        else:
            dig_list.append(str(int(dig % base)))
            dig_list.append(str(int(dig / base)))
            flag = False
            break
    rez = int(''.join(dig_list))
    return rez


def calc_from_bin(dig):
    digg = int(dig)
    dig_list = []
    base = 2
    flag = True
    while flag == True:
        if int(digg / base) > base:
            subrez = digg % base
            dig_list.append(str(subrez))
            dig = int(digg / base)
        else:
            dig_list.append(str(int(digg % base)))
            dig_list.append(str(int(digg / base)))
            flag = False
            break
    rez = int(''.join(dig_list))
    return rez
