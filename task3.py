def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    test = [3, 6, 8, 10, 1, 2, 1]
    print("исходный массив:", test)
    print("отсортированный:", quick_sort(test))

    test2 = [5, 4, 3, 2, 1]
    print("исходный:", test2)
    print("отсортированный:", quick_sort(test2))