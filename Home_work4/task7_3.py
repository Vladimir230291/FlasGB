import random
import asyncio
import time

MIN = 1
MAX = 100
COUNT_NUM = 1000000
COUNT_CHUNK = 10


def calculate_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum


async def main():
    arr = [random.randint(MIN, MAX) for _ in range(COUNT_NUM)]

    chunk_size = len(arr) // COUNT_CHUNK
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    # Запускаем асинхронные задачи
    futures = []
    for chunk in chunks:
        future = loop.run_in_executor(None, calculate_sum, chunk)
        futures.append(future)

    # Получаем результаты выполнения задач
    results = await asyncio.gather(*futures)

    # Считаем общую сумму
    total_sum = sum(results)

    # Выводим результат
    print("Сумма элементов массива:", total_sum)


if __name__ == '__main__':
    start_time = time.time()

    # Создаем цикл событий asyncio и запускаем функцию
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.2f}")
