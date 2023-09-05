import logging
import argparse


FORMAT = '{levelname: <8} - {asctime}. В модуле "{name}" '\
         'в строке {lineno:03d} функция "{funcName}()" '\
         'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(level=logging.NOTSET, filename='2_triangle_exist.log', filemode='w', encoding='utf-8', format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-a', metavar='a', type=int)
    parse.add_argument('-b', metavar='b', type=int)
    parse.add_argument('-c', metavar='c', type=int)
    # parse.add_argument('param', metavar='a b c', nargs=3, type=int, help='separated a b c by a space')
    args = parse.parse_args()
    logger.info(f'Треугольник с параметрами {args}')
    a, b, c = args.a, args.b, args.c

    if a + b > c and a + c > b and b + c > a:
        logger.info('Треугольник существует')
        if a == b and a == c and b == c:
            logger.debug('Треугольник равносторонний')
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            logger.debug('Треугольник равнобедренный')
        else:
            logger.debug('Треугольник разностороний')
    else:
        logger.error('Треугольник не существует')


if __name__ == '__main__':
    main()
