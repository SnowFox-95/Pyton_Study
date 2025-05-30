"""
Кремниевая долина 🌶️🌶️

Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в
качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и
нужно вывести номер холодильника, нумерация начинается с единицы.

Формат входных данных.
 В первой строке подаётся число n – количество холодильников. В последующих n строках
вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

Формат выходных данных.
 Программа должна вывести номера зараженных холодильников через пробел. Если таких
холодильников нет, ничего выводить не нужно.
"""

def find_anton(str):
    tik = 0  # переменная флаг успешного поиска = 0

    a = str.find('a')  # ищем а
    if a == -1:  # если а не найдена
        return 0
    else:
        tik += 1
        str2 = str[a:]  # срез от найденной а до конца
        n = str2.find('n')
        if n == -1:
            return 0
        else:
            tik += 1
            str3 = str2[n:]

            t = str3.find('t')
            if t == -1:
                return 0
            else:
                tik += 1
                str4 = str3[t:]

                o = str4.find('o')
                if o == -1:
                    return 0
                else:
                    tik += 1
                    str5 = str4[o:]

                    n2 = str5.find('n')
                    if n2 == -1:
                        return 0
                    else:
                        tik += 1
                        return tik


n = int(input())
listing = []
antons_list = []
for i in range(1, n + 1):
    str = input()
    listing.append(str)

for j in range(len(listing)):
    new_str = listing[j]
    chk = (find_anton(new_str))
    if chk == 0:
        continue
    else:
        antons_list.append(int(j + 1))

print(*antons_list)
