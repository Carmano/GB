# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# ●	Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ●	Избегайте магических чисел
# ●	Добавьте аннотацию типов где это возможно

BIN = 2
OCT = 8


def our_bin_oct(number: int, mode: int) -> str:
    result = ''
    while number:
        result = str(number % mode) + result
        number //= mode
    return result


def our_bin(number: int) -> str:
    result = ''
    while number:
        result = str(number % 2) + result
        number //= 2
    return '0b' + result


def our_oct(number: int) -> str:
    result = ''
    while number:
        result = str(number % 8) + result
        number //= 8
    return '0o' + result


number = int(input('Введите число: '))


if bin(number) == '0b' + our_bin_oct(number, BIN):
    print(True)

if oct(number) == '0o' + our_bin_oct(number, OCT):
    print(True)


print(our_bin_oct(number, BIN))
print(our_bin_oct(number, OCT))

