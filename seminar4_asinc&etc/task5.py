# Задание №5.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории
# и выводить результаты в консоль.
# Используйте процессы.

import os
import multiprocessing

PATH = '.'
counter = multiprocessing.Value('i', 0)


def count_words(file_name: str, count) -> None:
    with open(file_name, 'r', encoding='utf-8') as f:
        words_count = len(f.read().split())
        print(f'{file_name}: Количиство слов: {words_count}')
        with count.get_lock():
            count.value += words_count


if __name__ == '__main__':
    processes = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            process = multiprocessing.Process(target=count_words, args=(file_path, counter))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

    print(f'Всего слов: {counter.value}')