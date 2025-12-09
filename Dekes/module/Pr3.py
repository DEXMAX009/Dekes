def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
a = [1, 5, 3]
b = [7, 2]
c = [9]
d = [4, 6]

merged = merge_lists(a, b, c, d)
print("Объединённый список:", merged)

# сортировка по выбору пользователя
sort_type = "asc"   # "desc"

if sort_type == "asc":
    merged.sort()
else:
    merged.sort(reverse=True)

print("Отсортированный:", merged)

# поиск значения
target = 7
pos = linear_search(merged, target)
print(f"Поиск {target}: позиция =", pos)



def unique_merge(*lists):
    result = []
    for lst in lists:
        for x in lst:
            if sum(x in other for other in lists) == 1:
                result.append(x)
    return result

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
a = [1, 2, 3]
b = [3, 4]
c = [4, 5, 6]
d = [7, 1]

unique = unique_merge(a, b, c, d)
print("Уникальные элементы:", unique)

# сортировка
sort_type = "asc"
unique.sort(reverse=(sort_type == "desc"))
print("Отсортировано:", unique)

# бинарный поиск
target = 5
idx = binary_search(unique, target)
print(f"Поиск {target}: позиция =", idx)



