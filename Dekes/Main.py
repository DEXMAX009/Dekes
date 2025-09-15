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

#
# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
#
# result = a - b - c
# print(result)

<<<<<<< HEAD
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
=======
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

a = int(input('Введите число'))
if 1 <= a <= 100:
    if a % 3 == 0:
        print('Fizz')
    elif a % 5 == 0:
        print('Buzz')
    elif a % 5 == 0 and a % == 0:
        print('Fizz Buzz')
    else:
        print(a)

else:
    print('Неверно')



>>>>>>> c72e1007333ed2f60dde80e208dbd0ced626ff8d
