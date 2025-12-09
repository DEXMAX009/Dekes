import random

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
lst = [random.randint(1, 20) for _ in range(10)]
print("Список:", lst)

target = 7
pos = linear_search(lst, target)

print(f"Ищем {target}. Результат:", pos)



def binary_search(lst, target):
    if not isinstance(target, str):
        return "Ошибка: принимается только строка!"

    try:
        target = int(target)
    except:
        return "Ошибка: строку нельзя преобразовать в число!"

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
lst = sorted([random.randint(1, 20) for _ in range(10)])
print("Список:", lst)

result = binary_search(lst, "7")
print("Результат поиска:", result)



class Soda:
    def __init__(self, addon=None):
        self.addon = addon

    def show_my_drink(self):
        if self.addon:
            print(f"Газировка и {self.addon}")
        else:
            print("Обычная газировка")
s1 = Soda("лимон")
s2 = Soda()

s1.show_my_drink()
s2.show_my_drink()




class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_triangle(self):
        a, b, c = self.sides

        # проверка типа
        if not all(isinstance(x, (int, float)) for x in self.sides):
            return "Нужно вводить только числа!"

        # проверка на положительность
        if a <= 0 or b <= 0 or c <= 0:
            return "С отрицательными числами ничего не выйдет!"

        # условие существования треугольника
        if a + b > c and a + c > b and b + c > a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."
t1 = TriangleChecker(3, 4, 5)
t2 = TriangleChecker(-1, 4, 5)
t3 = TriangleChecker(1, 2, 3)

print(t1.is_triangle())
print(t2.is_triangle())
print(t3.is_triangle())



class Nikola:
    __slots__ = ("name", "age")  # запрещает добавление любых других атрибутов

    def __init__(self, name, age):
        if name != "Николай":
            self.name = f"Я не {name}, а Николай"
        else:
            self.name = name
        self.age = age
n1 = Nikola("Алексей", 30)
n2 = Nikola("Николай", 25)

print(n1.name, n1.age)
print(n2.name, n2.age)





class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hours = 0
        self.salary = 0
        self.senior_bonus = 0

    def work(self, time):
        self.hours += time
        self.salary += time * self.get_rate()

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        else:  # Senior
            self.senior_bonus += 1

    def get_rate(self):
        if self.position == "Junior":
            return 10
        elif self.position == "Middle":
            return 15
        else:
            return 20 + self.senior_bonus

    def info(self):
        return f"{self.name}: {self.hours}ч., {self.salary} тгр."
p = Programmer("Иван", "Junior")

p.work(5)
p.rise()       # теперь Middle
p.work(3)
p.rise()       # теперь Senior
p.work(2)
p.rise()       # Senior +1 к ставке
p.work(2)

print(p.info())






import random

class NPC:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def info(self):
        print(f"Имя: {self.name}, Очки здоровья: {self.hp}")

class Swordsman(NPC):
    def __init__(self, name, hp, min_dmg, max_dmg):
        super().__init__(name, hp)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def attack(self):
        dmg = random.randint(self.min_dmg, self.max_dmg)
        print(f"Мечник {self.name} нанёс {dmg} урона!")

class Mage(NPC):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self):
        if self.mana <= 0:
            print("Не могу атаковать! Мана закончилась.")
        else:
            dmg = self.mana * 2
            print(f"Маг {self.name} нанёс {dmg} урона!")
            self.mana = 0
g = Mage("Гендальф", 100, 5)
a = Swordsman("Арагорн", 50, 5, 10)
b = NPC("Бильбо", 15)

b.info()
print("Попытка атаки Бильбо:")
# нет метода attack

g.info()
g.attack()
g.attack()  # маны нет

a.info()
a.attack()

