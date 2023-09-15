import random
import multiprocessing
import time



def calculate_sum(arr, result):
    total_sum = 0
    for num in arr:
        total_sum += num
    result.put(total_sum)


MIN = 1
MAX = 100
COUNT_NUM = 1000000
COUNT_CHUNK = 10


def main():

    arr = [random.randint(MIN, MAX) for _ in range(COUNT_NUM)]


    chunk_size = len(arr) // COUNT_CHUNK
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]


    result_queue = multiprocessing.Queue()

    # Создаем и запускаем процессы для выполнения
    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=calculate_sum, args=(chunk, result_queue))
        process.start()
        processes.append(process)

    # Ожидаем завершения всех процессов
    for process in processes:
        process.join()

    # Извлекаем результаты из очереди и считаем общую сумму
    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    # Выводим результат
    print(f"Сумма элементов массива: {total_sum}")


if __name__ == '__main__':
    start_time = time.time()

    main()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.2f} секунд")
