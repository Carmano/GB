# Своя реализация функции hex
def our_hex(num: int) -> str:
    result = ''
    chars_hex = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    while num:
        remainder = num % 16
        result = (str(chars_hex[remainder]) if remainder in chars_hex else str(remainder)) + result
        num //= 16
    if result == '':
        result = '0'
    return "0x" + result


def main():
    num = int(input("Введите число: "))
    print(hex(num))
    print(our_hex(num))
    if hex(num) == our_hex(num):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
