# Многопоточный подход

import argparse
import os
import threading
import time
import requests


IMG_DIR = 'images'


def download_image(url: str, target_dir: str) -> None:
    start_thread_time = time.time()
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(os.path.join(target_dir, filename), 'wb') as img:
        for data in response.iter_content(1024):
            img.write(data)
    print(f"Downloaded image {url} in {time.time() - start_thread_time:.2f} sec")


def parse():
    parser = argparse.ArgumentParser(description="Скачивание изображение с заданных URL-адресов")
    parser.add_argument("urls", nargs="+", help="Список URL-адресов, с которых можно загрузить изображения")
    return parser.parse_args()


if __name__ == '__main__':
    urls = parse().urls

    if not os.path.exists(IMG_DIR):
        os.mkdir(IMG_DIR)

    start_time = time.time()

    threads = []
    for img_url in urls:
        thread = threading.Thread(target=download_image, args=[img_url, IMG_DIR])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Total download time (threading): {time.time() - start_time:.2f} sec')