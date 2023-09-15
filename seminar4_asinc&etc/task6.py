# Задание №6.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории
# и выводить результаты в консоль.
# Используйте асинхронный подход.

import os
import asyncio

PATH = '.'
count = 0


async def count_words(file_name: str) -> None:
    global count
    with open(file_name, 'r', encoding='utf-8') as f:
        words_count = len(f.read().split())
        print(f'{file_name}: Количиство слов: {words_count}')
        count += words_count


async def main():
    tasks = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            tasks.append(asyncio.create_task(count_words(file_path)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print(f'Всего слов: {count}')
