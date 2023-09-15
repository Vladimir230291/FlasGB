# Задание №4
# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте потоки.

import threading
import os

PATH = '.'
count = 0


def count_words(file_name: str) -> None:
    global count
    with open(file_name, 'r', encoding='utf-8') as f:
        words_count = len(f.read().split())
        print(f'{file_name}: Количиство слов:{words_count}')
        count += words_count


if __name__ == '__main__':
    threads = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            thread = threading.Thread(target=count_words, args=[file_path, ])
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print(f'Всего слов: {count}')
