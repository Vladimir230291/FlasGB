# Задание №9
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует
# названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# Программа должна выводить в консоль информацию о времени скачивания каждого изображения
# и общем времени выполнения программы.


import argparse
import os
import time
import aiohttp
import asyncio


# Функция для скачивания изображения с помощью aiohttp и сохранения на диск
async def async_download_image(session, url):
    image_name = url.split("/")[-1]
    async with session.get(url) as response:
        with open(image_name, "wb") as f:
            f.write(await response.read())
    return image_name


async def async_download(urls):
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [async_download_image(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    return results, total_time


# Код для запуска программы из командной строки
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скачивание изображение с заданных URL-адресов")
    parser.add_argument("urls", nargs="+", help="Список URL-адресов, с которых можно загрузить изображения")
    args = parser.parse_args()

    # Проверка существования директории "images" для сохранения файлов
    if not os.path.exists("images"):
        os.makedirs("images")
    os.chdir("images")

    # Асинхронный подход
    loop = asyncio.get_event_loop()
    results, total_time = loop.run_until_complete(async_download(args.urls))
    print("Async download results:", results)
    print("Total time (async):", total_time, "seconds")
