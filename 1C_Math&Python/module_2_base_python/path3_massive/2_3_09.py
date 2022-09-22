"""
На вход подаётся строка, слова в которой разделены между собой пробелами.
Напечатайте 2, 3 и предпоследнее слова из строки (через пробел)
"""


def main(lst):
    new_str = str(lst[1]) + ' ' + str(lst[2]) + ' ' + str(lst[-2])
    print(new_str)


if __name__ == "__main__":
    string = input().split(' ')
    main(string)
