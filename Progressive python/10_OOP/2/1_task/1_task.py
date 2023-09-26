from fractions import Fraction
from decimal import Decimal


class OurFraction:
    def __init__(self, fraction):
        try:
            if '/' in fraction:
                self.numerator, self.denominator = map(int, fraction.split('/'))
            else:
                raise ValueError
        except ValueError:
            print('Не корректный формат, перезапустите программу и введите в правильном формате')

    def __add__(self, other):
        result = Decimal(str(
            (self.numerator / self.denominator) + (other.numerator / other.denominator))
        ).as_integer_ratio()
        return OurFraction(f'{result[0]}/{result[1]}')

    def __mul__(self, other):
        result = Decimal(str(
            (self.numerator / self.denominator) * (other.numerator / other.denominator))
        ).as_integer_ratio()
        return OurFraction(f'{result[0]}/{result[1]}')

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == self.denominator:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


def main():
    print('Дробь а, b')
    a = OurFraction(input('Введите первую дробь: '))
    b = OurFraction(input('Введите вторую дробь: '))
    print(a + b)
    print(a * b)

    print('Дробь c, d')
    c = Fraction(input('Введите первую дробь: '))
    d = Fraction(input('Введите вторую дробь: '))
    print(c + d)
    print(c * d)
    print('\nСравнение суммы и произведения')
    if c + d == a + b:
        print('Суммы равны')
    else:
        print("Суммы не равны")

    if c * d == a * b:
        print('Произведения равны')
    else:
        print("Произведения не равны")


if __name__ == '__main__':
    main()
