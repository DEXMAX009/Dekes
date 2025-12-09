class Directory:
    def __init__(self, ids, phones):
        self.ids = ids
        self.phones = phones

    def sort_by_id(self):
        combined = list(zip(self.ids, self.phones))
        combined.sort(key=lambda x: x[0])
        self.ids, self.phones = zip(*combined)
        self.ids, self.phones = list(self.ids), list(self.phones)

    def sort_by_phone(self):
        combined = list(zip(self.ids, self.phones))
        combined.sort(key=lambda x: x[1])
        self.ids, self.phones = zip(*combined)
        self.ids, self.phones = list(self.ids), list(self.phones)

    def show(self):
        for i, p in zip(self.ids, self.phones):
            print(f"ID: {i}, Телефон: {p}")
ids = [3, 1, 2]
phones = ["555-12-34", "777-88-99", "111-22-33"]

d = Directory(ids, phones)

print("Исходный список:")
d.show()

print("\nСортировка по ID:")
d.sort_by_id()
d.show()

print("\nСортировка по телефонам:")
d.sort_by_phone()
d.show()



class Books:
    def __init__(self, titles, years):
        self.titles = titles
        self.years = years

    def sort_by_title(self):
        combined = list(zip(self.titles, self.years))
        combined.sort(key=lambda x: x[0])
        self.titles, self.years = zip(*combined)
        self.titles, self.years = list(self.titles), list(self.years)

    def sort_by_year(self):
        combined = list(zip(self.titles, self.years))
        combined.sort(key=lambda x: x[1])
        self.titles, self.years = zip(*combined)
        self.titles, self.years = list(self.titles), list(self.years)

    def show(self):
        for t, y in zip(self.titles, self.years):
            print(f"{t} — {y}")
titles = ["Мастер и Маргарита", "Том Сойер", "Гарри Поттер"]
years = [1967, 1876, 1997]

b = Books(titles, years)

print("Исходный список книг:")
b.show()

print("\nСортировка по названию:")
b.sort_by_title()
b.show()

print("\nСортировка по году выпуска:")
b.sort_by_year()
b.show()



