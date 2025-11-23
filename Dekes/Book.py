#Задание 1
def main():
    # Инициализация списков
    codes = [101, 102, 103, 104]
    phones = [1234567, 7654321, 5555555, 8888888]

    while True:
        print("\nМеню справочника:")
        print("1. Отсортировать по идентификационным кодам")
        print("2. Отсортировать по номерам телефона")
        print("3. Вывести список пользователей")
        print("4. Выход")

        choice = input("Выберите пункт: ")

        if choice == '1':
            # Сортировка по кодам (с сохранением соответствия с телефонами)
            combined = list(zip(codes, phones))
            combined.sort(key=lambda x: x[0])
            codes, phones = zip(*combined)
            codes = list(codes)
            phones = list(phones)
            print("Отсортировано по кодам.")

        elif choice == '2':
            # Сортировка по телефонам (с сохранением соответствия с кодами)
            combined = list(zip(phones, codes))
            combined.sort(key=lambda x: x[0])
            phones, codes = zip(*combined)
            phones = list(phones)
            codes = list(codes)
            print("Отсортировано по телефонам.")

        elif choice == '3':
            print("\nСписок пользователей:")
            for i in range(len(codes)):
                print(f"Код: {codes[i]}, Телефон: {phones[i]}")

        elif choice == '4':
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()

# Задание 2
def main():
    # Инициализация списков
    titles = ["Война и мир", "Преступление и наказание", "Мастер и Маргарита"]
    years = [1869, 1866, 1967]

    while True:
        print("\nМеню книг:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг")
        print("4. Выход")

        choice = input("Выберите пункт: ")

        if choice == '1':
            # Сортировка по названиям (с сохранением соответствия с годами)
            combined = list(zip(titles, years))
            combined.sort(key=lambda x: x[0])
            titles, years = zip(*combined)
            titles = list(titles)
            years = list(years)
            print("Отсортировано по названиям.")

        elif choice == '2':
            # Сортировка по годам (с сохранением соответствия с названиями)
            combined = list(zip(years, titles))
            combined.sort(key=lambda x: x[0])
            years, titles = zip(*combined)
            years = list(years)
            titles = list(titles)
            print("Отсортировано по годам.")

        elif choice == '3':
            print("\nСписок книг:")
            for i in range(len(titles)):
                print(f"Название: {titles[i]}, Год выпуска: {years[i]}")

        elif choice == '4':
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()