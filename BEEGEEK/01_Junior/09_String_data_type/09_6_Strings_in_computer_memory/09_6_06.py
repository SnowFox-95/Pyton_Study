"""
Шифр Цезаря 🌶️
Легион Цезаря, созданный в 23 веке на основе Римской Империи не
изменяет древним традициям и использует шифр Цезаря. Это их и подвело, ведь данный шифр
очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира,
поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения.
Напишите программу для декодирования этого шифра.

Формат входных данных
В первой строке дается число n (1≤ n≤ 25) – сдвиг, во второй
строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.

Формат выходных данных Программа должна вывести одну строку – декодированное сообщение.
Обратите внимание, что нужно декодировать сообщение, а не закодировать.
"""

n = int(input())
str = input()
new_str = ''
if 1 <= n <= 25:
    for i in range(len(str)):
        old_ch = ord(str[i])
        transp_ch = old_ch - n
        if transp_ch < 97:
            transp_ch += 26
        new_ch = chr(transp_ch)
        new_str = new_str + new_ch
print(new_str)
