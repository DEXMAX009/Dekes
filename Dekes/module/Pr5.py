def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2
    return arr
lst = [9, 1, 7, 4, 3, 8]
print(shell_sort(lst))





def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
lst = [12, 3, 5, 7, 19, 1]
print(heap_sort(lst))



def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)
lst = [8, 2, 5, 1, 9, 3]
print(quick_sort(lst))




def flip(arr, k):
    return arr[:k+1][::-1] + arr[k+1:]

def pancake_sort(arr):
    n = len(arr)
    for size in range(n, 1, -1):
        max_index = arr.index(max(arr[:size]))
        if max_index != size - 1:
            # переворот до максимума
            arr = flip(arr, max_index)
            # переворот до нужной позиции
            arr = flip(arr, size - 1)
    return arr
pancakes = [6, 1, 5, 3, 4, 2]
print(pancake_sort(pancakes))



