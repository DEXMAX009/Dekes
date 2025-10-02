# print("Hello")
# #Функция которая выводит текст в консоль
# Name = input("Введите ваше имя:")
# Age = int(input("Введите ваш возраст:"))
# water = 4.5
# print(type(Age), type(Name), type(water))
# print("Привет,", Name, "тебе" , Age , "лет")
# print('Я пью', water , 'литра воды')
# #format - Форматирования строки и # вставка переменных напрямую
# Age = int(input('Возраст:'))
# Name = input('Имя:')
# s_name =input('Фамилия:')
# date = input('Дата рождения:')
# print(f'Ваши переданные данные:')
#     f"1.Возраст:{Age} n\"
#     f"2.Имя:{Name} n\"
#     f"3.Фамилия:{s_name} n\"
#     f"4.Дата рождения:{date} n\"
#
#
#
# print("Я сегодня встал рано на пары.", "Мне очень хочется спать."
#        "Но я пересилил себя и пошёл получать знания.",
#       sep="^^^", end= '@'
#       )
# print('Успешного дня')
# ```
# Ариф. Операция
# + - * /
# ** - операция возведения в степень
# print(2**2) #4
# // - деление целочисленное
# print(2//4)# DIV 0
# % - деление по остатку
# print(5%2) # 1
# sum() - сумма переданных элементов
# min() - минимальный элемент
# max() - максимальный элемент

# Как не делить
# 1. Деление на ноль
# 2. Деление целого числа на ноль
# 3. Нахождения остатка от деления на ноль
#
# РЕР-8 Руководство по коду на Python
# 1) Имена функций, переменных, классов, должны состоять из маленьких букв, а слово разделяется
# символами подчёркивания - это необходимо, чтобы их было легче прочитать(fun, my_fun)
# 2)Нельзя давать имена, которые зарегистрированы в самом Python: int, False, True, None, if, in, from. return, list, float,...

# my_var = 100
# my_var = my_var + 200 + 300
# my_var += 200 + 300
# print(my_var)



#Практика 2
# Задание 1
# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
# sum_number = a + b + c
# pro_number = a * b * c
# print(sum_number)
# print(pro_number)

#Задание 2
# Month = int(input('Введите зп за месяц'))
# credit = int(input('Введите сумму кредита в банке за месяц'))
# Communal_services = int(input('Введите задолженность за коммунальные услуги'))
# raz_number = Month - credit - Communal_services
# print(raz_number)

#Задание 3
# d1 = int(input("Введите длину диагонали: "))
# d2 = int(input("Введите длину диагонали: "))
# S_Romb = (d1 * d2) / 2
# print(S_Romb)

#Задание 4
#print("To be\nor not\nto be")

#Задание 5
#print("Life is what happens\n                      when\n                            you're busy making other plans\"\n                                                             Jonh Lennon")

#Практика 1
#Задание 1
# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
# sum_number = a + b + c
# pro_number = a * b * c
# Change = int(input('Выберете действие'))
# if Change == 1:
#     print(sum_number)
# if Change == 2:
#     print(pro_number)

#Задание 2
# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
# Arifm = (a + b + c) / 3
# Change = int(input('Выберете действие'))
# if Change == 1:
#     print(max)
# if Change == 2:
#     print(min)
# if Change == 3:
#     print(Arifm)

#Практика 2

# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))

# Week_day = int('Введите число')
# if Week_day == 1:
#     print('Понедельник')
# elif Week_day == 2:
#     print('Вторник')
# elif Week_day == 3:
#     print('Среда')
# elif Week_day == 4:
#     print('Четверг')
# elif Week_day == 5:
#     print('Пятница')
# elif Week_day == 6:
#     print('Суббота')
# elif Week_day == 7:
#     print('Воскресенье')


# Mouth = int(input('Введите номер месяца'))
# if Mouth == 1:
#     print('Январь')
# elif Mouth == 2:
#     print('Февраль')
# elif Mouth == 3:
#     print('Март')
# elif Mouth == 4:
#     print('Апрель')
# elif Mouth == 5:
#     print('Май')
# elif Mouth == 6:
#     print('Июнь')
# elif Mouth == 7:
#     print('Июль')
# elif Mouth == 8:
#     print('Август')
# elif Mouth == 9:
#     print('Сентябрь')
# elif Mouth == 10:
#     print('Октябрь')
# elif Mouth == 11:
#     print('Ноябрь')
# elif Mouth == 12:
#     print('Декабрь')

# a = int(input('Введите число'))
# if a > 0:
#     print('Number is positive')
# if a < 0:
#     print('Number is negative')
# if a == 0:
#     print('Number is equal to zero')

# a = int(input('Введите число'))
# b = int(input('Введите число'))
#
# if a == b:
#     print('А всё')
# elif a < b:
#     print(a,b)
# elif a > b:
#     print(b,a)

# a = int(input('Введите число'))
# if 1 <= a <= 100:
#     if a % 3 == 0:
#         print('Fizz')
#     elif a % 5 == 0:
#         print('Buzz')
#     elif a % 5 == 0 and a % == 0:
#         print('Fizz Buzz')
#     else:
#         print(a)
#
# else:
#     print('Неверно')

#Практика 2 Задание 1

# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
#
# sum_numbers = a + b + c
# pro_result = a * b * c
# print(sum_numbers, pro_result)
#Задание 2
# a = int(input('Введите зарплату'))
# b = int(input('Введите кредит в банке'))
# c = int(input('Введите задолженность'))
#
# razn_number = a-b-c
# print(razn_number)

#Задание 3
# d1 = float(input('Введите длину диагонали'))
# d2 = float(input('Введите длину диагонали'))
#
# area = (d1 * d2) / 2
#
# print('Площадь ромба:', area)


#Задание 4
#print('To be', 'or not', 'to be', sep = '\n')

#  for i in range(0, 10): #условие цикла
#   выполнение внутреннего кода
# for i in range(10, 0, -1):
#     print('Hello', i)
#while(условие)
#while True:
#    print('*')
# value_user = 1
# sum_user = 0
# while value_user != 0: #Пока выполняется условие
#     value_user = int(input('Введите число суммирования'))
#     sum_user = sum_user + value_user
# print('Сумма числа пользователя:', sum_user)
# for i in range(0, 6):
#     print('*' * i)
#Пользователь вводит строку
#необходимо её проверить на палиндроме
#кок, а буду я у дуба.
# user_string = input('Введите строку для проверки на Палиндром: ')

# counter_letter = len(user_string)#фунция подсчёта кол-во элементов

# counter_letter = len(user_string)#функция подсчёта кол-во элементов

# value_user = True #Переменнная для проверки палиндромов
# for letter_begin in range(0, counter_letter):
#     for letter_end in range(counter_letter, 0, -1):
#         print('Проверяется буква:',user_string[letter_begin])
#         print('Проверяется буква:',user_string[letter_end])
#         if letter_end != letter_end:
#             break
#     if value_user == False:
#         print('Слово не является палиндромом')
#         break


x = 5
y = 0
if x > 1 or x / y == 2:
    print(1)
else:
    print(2)

#Практика 2
#задание 1
# week = int(input("Ввести номер дня недели: "))
# if week == 1:
#     print("Понедельник")
# if week == 2:
#     print("Вторник")
# if week == 3:
#     print("Среда")
# if week == 4:
#     print("Четверг")
# if week == 5:
#     print("Пятница")
# if week == 6:
#     print("Суббота")
# if week == 7:
#     print("Воскресенье")
#задание 2
# month = int(input("Введите месяц: "))
# if month == 1:
#     print("Январь")
# if month == 2:
#     print("Февраль")
# if month == 3:
#     print("Март")
# if month == 4:
#     print("Апрель")
# if month == 5:
#     print("Май")
# if month == 6:
#     print("Июнь")
# if month == 7:
#     print("Июль")
# if month == 8:
#     print("Август")
# if month == 9:
#     print("Сентябрь")
# if month == 10:
#     print("Октябрь")
# if month == 11:
#     print("Ноябрь")
# if month == 12:
#     print("Декабрь")
#задание 3
# a = int(input("Введите число: "))
# if a > 0:
#     print("Number is positive")
# if a < 0:
#     print("Number is negative")
# if a == 0:
#     print("Number is zero")
# срез - подстрока или подмассив извлечённый из основного можно состоять из 1-n символов или элементов
# 1. взятие одного символа
# 2. Срез в двумя параметрами
# print(string[0:6])
# #[a:b] - интервал символов
# #find and rfind
# #нужны для поиска подстроки в строке
# print(string.find('l')) #Вернёт индекс элемента
# #Если элемента не, то -1
# print(string.rfind('l'))
# #find - ищет с лева направо
# #rfind - щет справа на лево
# #METHOD REPLACE - замена одной стр на другую
# print(string.replace('l'))
# #METHOD COUNT - считает кол-во вхождений символа в строку
# print(string.count('l'))
# # Список (массив) - послед элементов
# #пронумер от 0, как символы в строке
# Primes = [2, 3, 5, 7, 11, 13]
# print(Primes)
# print(Primes.count(3))
# print(type(Primes))
# Rainbow = ['red' , 'orange' , 'yellow' , 'green' , 'blue' , 'purple']
# print(f'кол-во цветов радуги: {len(Rainbow)} ')
# for i in Rainbow:
#     print(i, end=' ')
# print()
# # добавление и удаление элементов списка
# my_list = []
# count_list = int(input('Введите кол-во элементов: '))
# for i in range(count_list):
#     print(f"Введите элемент {i}")
#     new_element = int(input("->:"))
#     my_list.append(new_element)#Добавление нового
# print(my_list)
# print(my_list.pop())# удаление посл элемента
# #Методы join и split
# # 1 2 3
# user_str = input()
# user_list = user_str.split()
# print(string.split('l'))
# for i in range (len(user_list)):
#     user_list[i] = int(user_list[i])#Преобр типа
#
# print(''.join(Rainbow))# объединение строк
# #генератор списков
#
# n = 5
# #способ 1
# list_gen1 = []
# for i in range(n):
#     list_gen1.append(i*n)
# print(f"Первый способ {list_gen1}")
# #способ 2
# list_gen2 = [i*n for i in range(0, n)]
# print(f"Второй способ {list_gen2}")
#
# #Практика
# #Задание 1
# from random import randint
# list1 = []
# for i in range(len(list1)):
#     list1[i] = randint(0, 10)
# print(f"Вывод списка {list1}")
# from time import time
# x = [5] * 1_000_000_000
# start = time()
# x.append(0, 999)
# stop = time()
# print(stop - start)
# x = [100, 222, 5454, 7777]
# print(x[3])
# x.append(5)
# x.append(999)
# print(x)
# x.insert(2, 999)
# print(x)
# x.pop(2)

#print(123)

# from time import time
#
# x = [5] * 1_000_000
# start = time()
# for i in range(5):
#     x.pop(0)
#
# stop = time()
# print(stop - start)
#
# start = time()
# for i in range(5):
#     x.pop()
# stop = time()
# print(stop - start)
#
# start = time()
# for i in range(5):
#     x.append(999)
# #x.insert(0, 999)
# stop = time()
# print(stop - start)
#
# start = time()
# for i in range(5):
#     x.insert(0, 999)
# stop = time()
# print(stop - start)

# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# for num in range(start, end + 1):
#     if num % 7 == 0:
#         print(num)

# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# # 1. Все числа диапазона
# print("\n1. Все числа диапазона:")
# for num in range(start, end + 1):
#     print(num, end=" ")
#
# # 2. Все числа диапазона в убывающем порядке
# print("\n\n2. Все числа диапазона в убывающем порядке:")
# for num in range(end, start - 1, -1):
#     print(num, end=" ")
#
# # 3. Все числа, кратные 7
# print("\n\n3. Все числа, кратные 7:")
# for num in range(start, end + 1):
#     if num % 7 == 0:
#         print(num, end=" ")
#
# # 4. Количество чисел, кратных 5
# print("\n\n4. Количество чисел, кратных 5:")
# count = 0
# for num in range(start, end + 1):
#     if num % 5 == 0:
#         count += 1
# print(count)




#append(5)
#insert(0, 5)
#pop()
#pop(0)





