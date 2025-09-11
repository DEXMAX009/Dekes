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
# 2. Деление целогоо числа на ноль
# 3. Нахождения остатка от деления на ноль
#
# РЕР-8 Руководсто по коду на Python
# 1) Имена функций, переменнных, классов, должны состоять из маленьких букв, а слово разделяеться
# символами подчёркивания - это необходимо, чтобы их было легче прочитать(fun, my_fun)
# 2)Нельзя давать имена, которые зареганы в самом Python: int, False, True, None, if, in, from. return, list, float,...

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

# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))

<<<<<<< HEAD
# n = int(input())
# if n % != 0:
#     print('Делится на 7')
# n = 957
# print(n % 10)# посл цифра
# print(n // 10)# отсекает последнюю цифру

# n = int(input('Enter number:'))
#
# a = n % 10
# n = n // 10
# b = n % 10
# n = n // 10
# c = n % 10
# print(a + b + c)



#Блок 1 задание 2

# a = int(input('Введите число'))
# b = (a % 10)
# if b < a:
#     print('Первое число меньше')
# else:
#     print('Первое число больше')



#Блок 2 задание 1

# r = int(input('Введите число'))
# S = 3.14 * r ** 2
# C = 2 * 3.14 * r
# print(S)
# print(C)


#блок 2 задание 2
# year = int(input('Введите возраст'))
# if year > 18 or year = 18:
#     print('Пропуск в стрипуху разрешён')
# else:
#     print('Пропуск запрещён! Гуляй малолетка')

#блок 2 задание 3

# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
#
# if a >= b  and a >= c:
#     print(a)
# if b >= a and b >= c:
#     print(b)
# if c >= a and c >= b:
#     print(c)

#блок 2 задание 4

# a = int(input('Введите сторону треугольника'))
# b = int(input('Введите сторону треугольника'))
# c = int(input('Введите сторону треугольника'))
#
# if (b + c > a) and (c + a > b) and (b + a > c):
#     print('Такой треугольник существует')
# else:
#     print('Такого трегольника не существует')

=======
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



