import random

class Number:
    def __init__(self, size=12, min_v=-10, max_v=10):
        self.nums = [random.randint(min_v, max_v) for _ in range(size)]

    def process(self):
        avg = sum(self.nums) / len(self.nums)

        n = len(self.nums)
        one_third = n // 3
        two_thirds = 2 * n // 3

        if avg > 0:
            # сортируем первые 2/3
            sorted_part = sorted(self.nums[:two_thirds])
            rest = list(reversed(self.nums[two_thirds:]))
            self.nums = sorted_part + rest
        else:
            # сортируем только первую треть
            sorted_part = sorted(self.nums[:one_third])
            middle = self.nums[one_third:two_thirds]
            rest = list(reversed(self.nums[two_thirds:]))
            self.nums = sorted_part + middle + rest

obj = Number(size=9)
print("Исходный список:", obj.nums)

obj.process()
print("Обработанный список:", obj.nums)




class Grades:
    def __init__(self):
        self.grades = [int(input(f"Введите оценку {i+1}: ")) for i in range(10)]

    def show(self):
        print("Оценки:", self.grades)

    def retake(self, index, new_grade):
        self.grades[index] = new_grade

    def scholarship(self):
        avg = sum(self.grades) / len(self.grades)
        return avg >= 10.7

    def sort_grades(self, reverse=False):
        self.grades.sort(reverse=reverse)
g = Grades()

g.show()
g.retake(2, 12)
print("После пересдачи:")
g.show()

print("Стипендия:", "Да" if g.scholarship() else "Нет")

print("Сортировка по убыванию:")
g.sort_grades(reverse=True)
g.show()



def improved_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
lst = [5, 1, 3, 8, 2]
print("До:", lst)
print("После:", improved_bubble_sort(lst))
