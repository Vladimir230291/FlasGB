# Многопроцессорный подход

import argparse
import multiprocessing
import os
import time

import requests

IMG_DIR = 'images'


def download_image(url: str, target_dir: str) -> None:
    start_process_time = time.time()
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(os.path.join(target_dir, filename), 'wb') as img:
        for data in response.iter_content(1024):
            img.write(data)
    print(f"Downloaded image {url} in {time.time() - start_process_time:.2f} sec")


def parse():
    parser = argparse.ArgumentParser(description="Скачивание изображение с заданных URL-адресов")
    parser.add_argument("urls", nargs="+", help="Список URL-адресов, с которых можно загрузить изображения")
    return parser.parse_args()


if __name__ == '__main__':
    urls = parse().urls

    if not os.path.exists(IMG_DIR):
        os.mkdir(IMG_DIR)

    start_time = time.time()

    processes = []
    for img_url in urls:
        process = multiprocessing.Process(target=download_image, args=(img_url, IMG_DIR))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Total download time (multiprocessing): {time.time() - start_time:.2f} sec')