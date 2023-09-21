import threading
import requests
import argparse


urls = [
    "https://habr.com/ru/companies/simbirsoft/articles/701020/",
    "https://habr.com/ru/companies/wunderfund/articles/700474/",
    "https://gb.ru/lessons/353429",
]


def download_to_urls(url):
    response = requests.get(url)
    filename = url.replace('https://', '').replace('/', '-')
    with open(f'download/{filename}', 'wb') as file:
        file.write(response.content)


def image_nothing():
    pass

def image_process():
    pass

def image_thread():
    pass


def image_async():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+", help="Список URL-адресов для скачивания изображений")
    args = parser.parse_args()
    urls = args.urls

