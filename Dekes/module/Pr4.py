def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
lst = [5, 3, 1, 4, 2]
print(bubble_sort(lst))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
lst = [9, 4, 6, 2, 8]
print(insertion_sort(lst))




def half_sort(arr):
    n = len(arr)
    mid = n // 2

    first = sorted(arr[:mid], reverse=True)
    second = sorted(arr[mid:])

    return first + second
lst = [7, 3, 5, 1, 9, 2]
print(half_sort(lst))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
lst = [10, 1, 8, 3, 7, 2]
print(merge_sort(lst))




