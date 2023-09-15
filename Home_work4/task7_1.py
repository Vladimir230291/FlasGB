# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import random
import concurrent.futures
import time

MIN = 1
MAX = 100
COUNT_NUM = 1000000
COUNT_CHUNK = 10


# Функция, которая будет считать сумму элементов массива в потоке
def calculate_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum


def main():
    # Создаем и заполняем массив случайными числами от 1 до 100
    arr = [random.randint(MIN, MAX) for _ in range(COUNT_NUM)]

    # Разделяем массив на части для обработки многопоточностью
    chunk_size = len(arr) // 10
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    # Создаем пул потоков
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Запускаем потоки и получаем объекты Future
        futures = [executor.submit(calculate_sum, chunk) for chunk in chunks]
        # Считаем общую сумму
        total_sum = 0
        for future in concurrent.futures.as_completed(futures):
            total_sum += future.result()
    # Выводим результат
    print(f"Сумма элементов массива: {total_sum}")


if __name__ == '__main__':
    start_time = time.time()

    main()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.2f} секунд")
