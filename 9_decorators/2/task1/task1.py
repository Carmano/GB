from typing import Callable


def main(number: int, popitka: int) -> Callable[[], None]:
    def game():
        for i in range(popitka):
            num = int(input('Введите число: '))
            if num == number:
                print('Число угаданно')
                break
            elif num > number:
                print("Число больше угаданного")
            else:
                print("Число меньше угаданного")
        else:
            print('Попитки закончились')
    return game


if __name__ == '__main__':
    result = main(47, 10)
    result()
