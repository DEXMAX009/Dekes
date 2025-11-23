# def linear_search(arr, target):
#     """Линейный поиск"""
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
#
#
# def main_task1():
#     # Инициализация четырех списков
#     list1 = [5, 2, 8, 1]
#     list2 = [9, 3, 7, 4]
#     list3 = [6, 12, 10, 11]
#     list4 = [15, 13, 14, 16]
#
#     # Объединение списков
#     combined_list = list1 + list2 + list3 + list4
#
#     print("Исходные списки:")
#     print(f"Список 1: {list1}")
#     print(f"Список 2: {list2}")
#     print(f"Список 3: {list3}")
#     print(f"Список 4: {list4}")
#     print(f"Объединенный список: {combined_list}")
#
#     while True:
#         print("\nМеню:")
#         print("1. Отсортировать по возрастанию")
#         print("2. Отсортировать по убыванию")
#         print("3. Найти значение (линейный поиск)")
#         print("4. Выход")
#
#         choice = input("Выберите пункт: ")
#
#         if choice == '1':
#             combined_list.sort()
#             print(f"Отсортировано по возрастанию: {combined_list}")
#
#         elif choice == '2':
#             combined_list.sort(reverse=True)
#             print(f"Отсортировано по убыванию: {combined_list}")
#
#         elif choice == '3':
#             try:
#                 target = int(input("Введите значение для поиска: "))
#                 index = linear_search(combined_list, target)
#                 if index != -1:
#                     print(f"Значение {target} найдено на позиции {index}")
#                 else:
#                     print(f"Значение {target} не найдено")
#             except ValueError:
#                 print("Ошибка: введите целое число")
#
#         elif choice == '4':
#             break
#
#         else:
#             print("Неверный ввод. Попробуйте снова.")
#
#
# # Запуск первой программы
# if __name__ == "__main__":
#     main_task1()

def binary_search(arr, target):
    """Бинарный поиск (требует отсортированного массива)"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def get_unique_elements(*lists):
    """Получить элементы, которые уникальны для каждого списка"""
    all_elements = []
    for lst in lists:
        all_elements.extend(lst)

    # Считаем вхождения каждого элемента
    from collections import Counter
    element_count = Counter(all_elements)

    # Оставляем только элементы, которые встречаются ровно один раз во всех списках
    unique_elements = [elem for elem, count in element_count.items() if count == 1]

    return unique_elements


def main_task2():
    # Инициализация четырех списков
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    list4 = [7, 8, 9, 10, 11]

    # Получение уникальных элементов
    unique_list = get_unique_elements(list1, list2, list3, list4)

    print("Исходные списки:")
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print(f"Список 3: {list3}")
    print(f"Список 4: {list4}")
    print(f"Уникальные элементы: {unique_list}")

    is_sorted = False

    while True:
        print("\nМеню:")
        print("1. Отсортировать по возрастанию")
        print("2. Отсортировать по убыванию")
        print("3. Найти значение (бинарный поиск)")
        print("4. Выход")

        choice = input("Выберите пункт: ")

        if choice == '1':
            unique_list.sort()
            is_sorted = True
            print(f"Отсортировано по возрастанию: {unique_list}")

        elif choice == '2':
            unique_list.sort(reverse=True)
            is_sorted = True
            print(f"Отсортировано по убыванию: {unique_list}")

        elif choice == '3':
            if not is_sorted:
                print("Ошибка: список должен быть отсортирован для бинарного поиска")
                continue

            try:
                target = int(input("Введите значение для поиска: "))
                index = binary_search(unique_list, target)
                if index != -1:
                    print(f"Значение {target} найдено на позиции {index}")
                else:
                    print(f"Значение {target} не найдено")
            except ValueError:
                print("Ошибка: введите целое число")

        elif choice == '4':
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


# Запуск второй программы
if __name__ == "__main__":
    main_task2()