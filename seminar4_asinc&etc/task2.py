# Задание №2
#  Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
#  После загрузки данных нужно записать их в отдельные
# файлы.
#  Используйте процессы.
from multiprocessing import Process

import requests

urls = ['https://vk.com/',
        'https://youtube.com/',
        'https://wireframe.cc/WJ4Lb1',
        'https://letsencrypt.org/ru/',
        'https://getbootstrap.com/docs/5.3/components/button-group/',
        'https://edit.org/edit/all/14sxb7zt9',
        'https://pythontutor.com/render.html#mode=edit',
        'https://timeweb.cloud/',
        'https://linkmeup.ru/blog/',
        'https://ya.ru']


def download(url: str):
    response = requests.get(url)
    filename = "task2_" + url.replace("https://", "").replace("/", "").replace('.', '') + ".html"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)
        print(f"фаил {filename} успешно загружен")

if __name__ == '__main__':

    processes = []

    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
