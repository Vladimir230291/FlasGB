# Задание №3
#  Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
#  После загрузки данных нужно записать их в отдельные
# файлы.
#  Используйте асинхронный подход.

import asyncio
import aiohttp

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

async def download(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = "task3_" + url.replace("https://", "").replace("/", "").replace('.', '') + ".html"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(await response.text())
                print(f"фаил {filename} успешно загружен")

async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())