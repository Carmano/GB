import threading

import aiohttp
import requests
import multiprocessing
import asyncio
import argparse
import time

urls_test = [
    "https://img3.fonwall.ru/o/ib/dodge-challenger-red-and-white-muscle-cars-cars.jpeg",
    "https://img3.fonwall.ru/o/jv/sea-coast-water-ocean-rupc.jpeg",
    'https://img3.fonwall.ru/o/fa/portrait-girl-warrior.jpg'
]


def download_to_urls(url, approach, start_time):
    response = requests.get(url)
    filename = approach + "_" + url.split("/")[-1]
    with open(f'download/{filename}', "wb") as file:
        file.write(response.content)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


async def async_download_to_urls(url, approach, start_time):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = approach + "_" + url.split("/")[-1]
            with open(f'download/{filename}', "wb") as file:
                file.write(await response.read())
            print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


def image_nothing(urls):
    start_time = time.time()
    for url in urls:
        download_to_urls(url, 'nothing', start_time)
    return time.time() - start_time


def image_process(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        t = multiprocessing.Process(target=download_to_urls, args=(url, 'thread', start_time), daemon=True)
        processes.append(t)
        t.start()

    for t in processes:
        t.join()

    return time.time() - start_time


def image_thread(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download_to_urls, args=(url, 'process', start_time), daemon=True)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return time.time() - start_time


async def image_async(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(async_download_to_urls(url, 'async', start_time))
        tasks.append(task)
    await asyncio.gather(*tasks)
    return time.time() - start_time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs='*', help="Список URL-адресов для скачивания изображений", default=urls_test)
    args = parser.parse_args()
    urls_list = args.urls

    print('Запуск программы синхронным подходом:')
    print('Общий результат', image_nothing(urls_list), '\n')
    print('Запуск программы используя многопоточности:')
    print('Общий результат', image_thread(urls_list), '\n')
    print('Запуск программы используя многопроцессорности:')
    print('Общий результат', image_process(urls_list), '\n')
    print('Запуск программы используя асинхронность:')
    print('Общий результат', asyncio.get_event_loop().run_until_complete(image_async(urls_list)), '\n')

