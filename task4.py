import random
import time
from task3 import quick_sort


def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def measure_time(sort_func, size, repeats=5):
    total = 0
    for _ in range(repeats):
        arr = [random.randint(0, 10000) for _ in range(size)]
        start = time.perf_counter()
        sort_func(arr)
        end = time.perf_counter()
        total += (end - start)
    return total / repeats


if __name__ == "__main__":
    sizes = [10, 100, 1000]

    print("сравнение времени выполнения быстрой сортировки и сортировки вставками\n")
    print(f"{'размер':<10} {'быстрая (сек)':<15} {'вставки (сек)':<15}")
    print("-" * 40)

    for size in sizes:
        qt = measure_time(quick_sort, size)
        it = measure_time(insertion_sort, size)
        print(f"{size:<10} {qt:<15.6f} {it:<15.6f}")
