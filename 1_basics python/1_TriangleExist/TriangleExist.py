
def main():
    a, b, c = map(int, input().split())

    if a + b > c and a + c > b and b + c > a:
        print('Треугольник существует')
        if a == b and a == c and b == c:
            print('Треугольник равносторонний')
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разностороний')
    else:
        print('Треугольник не существует')


if __name__ == '__main__':
    main()
