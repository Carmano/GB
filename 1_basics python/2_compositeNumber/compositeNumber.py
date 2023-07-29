def composite_number():
    a = int(input('Введите число: '))
    result = ''
    if a == 1:
        return 'Число равно task1. А единица не простое и не составное число'
    if a in [2, 3, 5]:
        result = 'Число простое'
    else:
        if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
            result = 'Число составное'
        else:
            result = 'Число простое'
    return result
# 4, 6, 8, 9, 10, 12, 14, 15, 16

if __name__ == '__main__':
    print(composite_number())
