def find_max(arr):
    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    max_left = find_max(left)
    max_right = find_max(right)

    return max_left if max_left > max_right else max_right

if __name__ == "__main__":
    test1 = [3, 7, 2, 9, 1, 5]
    test2 = [1, 2, 3, 4, 5]
    test3 = [10]
    test4 = [5, 1]

    print("максимум в [3,7,2,9,1,5]:", find_max(test1))
    print("максимум в [1,2,3,4,5]:", find_max(test2))
    print("максимум в [10]:", find_max(test3))
    print("максимум в [5,1]:", find_max(test4))