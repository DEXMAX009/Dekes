class Animal:
    def __init__(self, nickname):
        self.nickname = nickname

    def __str__(self):
        return f"Животное: {self.nickname}"


class Cat(Animal):
    def voice(self):
        print("Мяу!")

    def run(self):
        print("Побежали!")


class Parrot(Animal):
    def voice(self):
        print("Чирик!")

    def fly(self):
        print("Полетели!")
c = Cat("Барсик")
p = Parrot("Кеша")

print(c)
c.voice()
c.run()

print(p)
p.voice()
p.fly()




class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def showHeader(self):
        print(f"От: {self.sender} | Кому: {self.recipient}")


class TextMessage(Message):
    def __init__(self, sender, recipient, text):
        super().__init__(sender, recipient)
        self.text = text

    def send(self):
        self.showHeader()
        print(self.text)


class StickerMessage(Message):
    def __init__(self, sender, recipient, sticker):
        super().__init__(sender, recipient)
        self.sticker = sticker
        self.count = 1

    def send(self):
        self.showHeader()
        print(f"{self.sticker} (отправлено {self.count} раз)")
        self.count += 1
t = TextMessage("Аня", "Олег", "Привет! Как дела?")
t.send()

s = StickerMessage("Макс", "Дима", "(͡• ͜ʖ ͡•)")
s.send()
s.send()  # счётчик растёт





import random

class MSDice:
    def __init__(self, sides):
        self.sides = sides
        self.value = None

    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value


class D4(MSDice):
    def __init__(self):
        super().__init__(4)


class D6(MSDice):
    def __init__(self):
        super().__init__(6)


class D10(MSDice):
    def __init__(self):
        super().__init__(10)


class D20(MSDice):
    def __init__(self):
        super().__init__(20)
d = D20()
print("Результат броска:", d.roll())

d6 = D6()
print("D6:", d6.roll())



class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.exp_points = 0
        self.inventory = []

    def __str__(self):
        return f"Игрок: {self.nickname}\nОпыт: {self.exp_points}\nИнвентарь: {self.inventory}"

    def addExp(self, exp):
        self.exp_points += exp

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
p = Player("Рыцарь77")

p.addExp(50)
p.addItem("Меч")
p.addItem("Щит")
p.removeItem("Меч")

print(p)





class resistors:

    @staticmethod
    def parallel(r1, r2):
        return (r1 * r2) / (r1 + r2)

    @staticmethod
    def consec(r_list):
        return sum(r_list)
print("Параллельно:", resistors.parallel(10, 20))
print("Последовательно:", resistors.consec([5, 10, 15]))
