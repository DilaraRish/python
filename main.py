# name = "admin"
# print("Hello", name)
# age = 20.2
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
#
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# # print(b, id(b))
# a = b = c = 5
# print(a, b, c)
# a, b, c = 7, "Hello", 9.2
# print(a, b, c)
# PI = 3.14
# print(PI)
# PI = 2  # нарушение соглашения
# print(PI)

# a = 5
# b = "7"
# print(a + int(b))
# print(str(a) + b)

# a = 1
# b = 2
# print("a: ", a)
# print("b: ", b)
# a, b = b, a
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# print("a: ", a)
# print("b: ", b)

# print("строка \n"
#       "символов")
# print("     строка символов   строка символов   строка символов строка символов строка символов строка символов "
#       "строка символов строка символов")
# print("\"program\"C:\r\nfolder\\file.txt")  # \ - экранирует \r - затирает

#
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)
#
# print(4567756545677656656886676)
# print(4.567756545677656656886676)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(5 / 2)
# print(5 // 2)
# print(6 ** 2)
# print(6 % 2)

# a = 5
# b = 7
# c = 3
# sum = a + b + c
# print("Сумма: ", sum)
# print("Произведение: ", a * b * c)
# print("Среднее арифметическое", sum/3)

# numbers = 6 + 4 * 5 ** 2 +7
# print(numbers)
#
# numbers = (6 + 4) * (5 ** 2 +7)
# print(numbers)

# num = 10
# num += 5
# print(num)
# num -= 3
# print(num)
# num *= 4
# print(num)

# a = 10
# b = 2
#
# print("a: ", a)
# print("b: ", b)



#
# num = 4321;
# res = num % 10 * 1000;
# num //= 10;
# res += num % 10 * 100;
# num //= 10;
# res += num % 10 * 10;
# num //= 10;
# res += num % 10;
# print(res);


# a = round(3.765, 2);
# print(round(3.765));
# print(a, type(a));


# a = "5.2"
# b = 10
# c = int(a) + b
# print(c)

# name = "виктор"
# age = 28
# print("меня зовут", name, ".Мне", age, "лет.")
# print("меня зовут", name, ".Мне", str(age), "лет.")
# print("меня зовут", name, ".Мне", age, "лет.", end=" ", sep="---")
# print("Hello")


# name = input("Введите имя: ")
# city = input("Введите город: ")
# print(name, city)


# num = input("Введите число: ")
# power = input("Введите степень: ")
# num = int(num)
# power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)


# print("Введите четыре числа: ")
# one = input("1:")
# two = input("2:")
# three = input("3:")
# four = input("4:")
# one = int(one)
# two = int(two)
# three = int(three)
# four = int(four)
# res1 = one + two
# res2 = three + four
# res3 = round(res1 / res2, 2)
# print("Результат: ", res3)


# False => "", 0, 0.0, False

# print(7 = 7) => =, >, <, >=, <=, !=


# print("привет" > "ПРИВЕТ")   #по первой букве

# print(2 * 5 > 7 >= 4 + 3) #True


# a = 10
# b = 5
# c = a == b
# print(a, b, c) #10, 5, false


# print(5 - 3 == 2 and 1 + 3 == 4)   #True and True => True
# print(5 - 3 == 2 or 1 + 3 < 4)   #true or false => true
# print(not 9 - 5) #False    - переворачив в противополож сторону



# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)
#
#
# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("доступ запрещен")

# a = 25
# b = 35
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a = b")


# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("трегульник разносторонний")
#
# day = int(input("Введите день недели(цифрой): "))
# if (day >= 1) and (day <=5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("субблта")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дгя недели не сущ")



# n = int(input("введите кол-вл ворон: "))
# if 0 <= n <= 9:
#     print("на ветке: ", end= "")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("ошибка ввода данных")
#
# a = 10
# b = 2
# print("a: ", a)
# print("b: ", b)
# a = a + b
# b = a - b
# a = a - b
# print("a: ", a)
# print("b: ", b)


# n = int(input("Введите число от 1 до 99: "))
# if (n % 10 == 1) and n != 11:
#     print(n, "копейка")
# elif (n % 10 == 2) and n != 12 or (n % 10 == 3) and n != 13 or (n % 10 == 4) and n != 14:
#     print(n, "копейки")
# else:
#     print(n, "копеек")



# n = int(input("ввндите номер месяца: "))
# if n == 1 or n == 2 or n == 12:
#     print("Зима")
# elif 3 <= n <= 5:
#     print("Весна")
# elif 6 <= n <= 8:
#     print("Лето")
# elif 9 <= n <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


#
# password = "admin"
#
# match password:
#     case 'admin':
#         print("Administratot")
#     case 'user':
#         print("Polzovatel")
#     case _:
#         print("Parol neveren")
#
# day = "понедельник"
# time = 19
# match day:
#     case 'понедельник' | 'вторник'| 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("такого дня не сущ или нерабочее время")



# true <= if условие else=> false

# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 20, 10
#
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = int(input("введите первое число ")), int(input("введите второе число "))
# print("на ноль делить нельзя" if b == 0 else a / b)

# a = 5
# b = 0
# print(5 / 0)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не таак")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("нельзя вводит строки")
# except ZeroDivisionError:
#     print("нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("нельзя вводить строки и нельзя делить на ноль")
# else:  #отраб когла в блоке try не возникло исключений
#     print("все нормально. Вы ввели числа", n, "и", m)
# finally: #выполняется в люблм случае
#     print("Конец программы")



# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)

#
# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n +m)


# циклы

# i = 0
# while i < 5:
#     print("i= ", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i= ", i)
#     i -= 1

# i = 2
# while i < 21:
#     print("i= ", i)
#     i += 2


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i= ", i)
#     i += 1

# n = int(input("укажите кол-во символов: "))
# print("*" * n)

# n = int(input("укажите кол-во символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#        print("*", end = "")
#     else:
#        print("-", end="")
#     i += 1

# n = int(input("укажите кол-во символов: "))
# while n > 0:
#     print("*", end = "")
#     n -= 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечетных чисел: ", res)


#
# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nцикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

#
# while True:
#     n = int(input("Введите полож число: "))
#     if n < 0:
#         break


# res = 1
# while True:
#      n = int(input("Введите число: "))
#      if n == 0:
#          break
#      res *= n
# print("результат: ", res)


# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\nвнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="\t\t")
#         j += 1
#     print()
#     i += 1

#
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

#
# j = 0
# while j < 5:
#     print(" " * j, "*", sep="")
#     j += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# for i in "hello":  #for element in collection
#     print(i)


# for color in "red", "orange", "green", 20, 1:  #кортеж
#     print(color)


# print(range(9))
#range(start, stop, step)  range(1, 9, 2)


# for i in range(9):
#     print(i, end="")


# for i in range(9, 0, -1):
#     print(i)

# a = int(input("введите целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# else:
#     print("done")


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите длинну прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()


# w = int(input("Введите длинну прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#           print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print([i * 2 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])


#Spiski
# num = [4, 3, 5, 2, 5, "hello"]
# print(num)
# print(type(num))
# print(num[0])
# print(num[-1])
# print(num[8])


# num[1] = 100
# print(num)

# print(len(num))

# nums = list(range(2, 21, 2))
# print(nums)
# print(type(nums))

# nums = list("hello")
# num = nums * 2
# print(num + [1, 2, 3])


# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):
#     print(i)


#generator spiskov

#[viragenie for peremennaya in posledovatelnost]

# a = [0 for i in range(5)]
# print(a)  #[0,0,0,0,0]
# b = [i ** 2 for i in range(1, 6)]
# print(b)
# c = [c * 3 for c in "list"]
# print(c)

# a = [0] * int(input("Vvedite kol-vo elementov spiska: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [input() for i in range(int(input("n = ")))]
# print(a)


# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print(s)

# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):   # 0 1 2 3 4 5 6 7 8
#     print(lst[i], end=" ")
# print()
# for i in lst:      # 10 20 30 40 50 60 70 80 90
#     print(i, end=" ")

# colors = ["red", "blue", "red"]
# for i in range(len(colors)):
#     print(colors[i], end=" ")
# print()
# for i in colors:
#     print(i, end=" ")


# n = list(range(21, 41))
# print(n)
# count = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         s += n[i]

 # for i in n:
 #    if i % 2 == 0:
 #        count += 1
 #    else:
 #        s += i
# print("Kol-vo chetnx rlrmrntov skiska: ", count)
# print("Summa nechet el spiska:", s)



# n = list(range(21, 41))
# print(n)
# i = 2
# print(n[i])
# print(n[i-1])




# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")
#
# for i in a:
#     if i > i - 1:        #так не получится решить задачу
#         print(i,end=" ")


# a = [7, 9, 3, 1, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)



#срезы- список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[0:3])     #5, 9, 3
# b = s[10:20]
# print(b)
# s = [5, 9, 3, 7, 1, 8]
# print(s[5::-1])


# s = "hello"
# print(list("hello"))
# print(s[0])
# f = "hello world"
# print(f[6:11])


# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

#
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2] = 50
# print(s)
# s[2:4]=[]
# print(s)
# del s[2]
# print(s)


# Методы списков
#dir(list)
# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# s[7:] = [12]
# print(s)
# s.append(12)   #добавляет элемент в конец списка
# print(s)
# s.append([1, 2, 3])
# print(s)
# s.extend([1, 2, 3])  #добавл любое кол-вл элементов в конец списка
# s.append("add")
# print(s)
# s.extend("add")  #доьавляет посимвольно
# print(s)
# s.insert(3, "hello") # добавл элемент в список в заданный индекс(первый параметр), значение(второе параметр)
# print(s)
# s.insert(20, 90)
# print(s)


# s = []
# n = int(input("kol-vo el spiska: "))
# for num in range(n):
#     x = int(input("vvedide chislo: "))
#     # s.append((x))
#     s.insert(0, x)
# print(s)


# a = [5, 6, 3, 5, 4, 3]
# b = [4, 2, 8, 3, 5]
# c = []   # [3, 4, 5]
# for i in a:    #5, 6, 3, 5, 4, 3
#     for j in b:  #4, 2, 8, 3, 5
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

#
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
# print(c)



# a = [int(input("Кол-во элементов списка: "))]
# c = []
# for i in range(len(a)):
#     b = int(input("Введите число кратное 3: "))
#     if b % 3 == 0:
#         c.append(b)
#     else:
#         print(b, "не делится на 3 без остатка.")
# print(c)


# i = 0
# a = int(input("кол-во символов: "))
# b = input("Тип символа: ")
# print("0 - горизонтальная")
# print("1 - вертикальная")
# c = int(input("ориентация линии: "))
# while i < a:
#     if c == 0:
#         print(b * a)
#         break
#     else:
#         print(b)
#     i += 1



# a = [int(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
# count = 0
# print()
#
#

# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#    for i in range(len(a)):  # 0-3
#      c.append(a[i])
#      c.append(b[i])
#    for i in range(len(a), len(b)):  # range(3, 5)
#      c.append(b[i])
# else:
#    for i in range(len(b)):  # 0-3
#      c.append(a[i])
#      c.append(b[i])
#    for i in range(len(b), len(a)):  # range(3, 5)
#      c.append(a[i])
# print(c)


# a = [1, 3, 2, 3, 4, 5]
# print(a)
# # n = 2
# # if n in a:
# #     a.remove(3)    #удаление по значению, выбрасывает исключение valueError - ксли элемента не сущ
# last = a.pop()  # удал послед элемент и возращ удаленный элемент
# print(last)
# second = a.pop(1)  # удал элемент по заданному индексу и возращает
# print(second)
# print(a)
# a.clear()
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите элементы: ")))]
# k = int(input("Введите индекс:"))
# print(a.pop(k))
# print(a)



# a = [1, 5, 3, 2, 3, 4, 5]
# print(a)
# num = a.count(5)  #возваращает кол-во значениц в списке
# print(num)
# ind = a.index(3, 3)  #индекс где располагается элемент, (1 - элемент, 2 - какой по счету элемент
# print(ind)
# a.reverse() #перестроил элементы списка в обратном порядке
# print(a)
# a.sort(reverse=True)     #cортировка списка
# print(a)
# s = ["Vitali", "Sergey", "Alex", "Anna"]
# print(s)
# s.sort(key=len)
# print(s)
# print(len("Alex"))

# a = [1, 5, 3, 2, 3, 4, 5]
# print(a)
# a.sort()
# n = sorted(a)
# print("n = ", n)
# print(a)


# a = [1, 2, 3]
# b = a.copy()  #возвар копию списка
# print("a =", a)
# print("b = ", b)
# a.append(20)
# b.append(120)
# print("a =", a)
# print("b = ", b)


#генерация случайныз данных


import random
import time

# print(random.random())   # от 0 до 1(не вкд)
# print(random.randint(0, 9))  #от 0 до 9(вкл)
# print(random.randrange(2, 9, 2)) #(star, stop, step) randrange(0, 9)
# print(round(random.uniform(10.5, 25.5), 2))  #вещественный список
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(s))
# random.shuffle(s)
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# mas = ['a', 'b', 'c']
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))
# print(sum(mas))

# s = 0
# for i in mas:
#     s += i
# print(s)

# a = [random.randint(0, 100) for i in range(10)]
# print(a)
# b = max(a)
# print(b)
# a.remove(b)
# a.insert(0, b)
# print(a)

# a = [random.randint(-20, 20) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)

# a = [random.randint(0, 20) for i in range(10)]
# print(a)
# b = min(a)
# print("Min: ", b)
# ind = a.index(b)
# print(ind)
# # print(a[ind:])
# del a[:ind]
# print(a)


#dz
# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс: "))
# c = int(input("Введите значение: "))
# a.insert(k, c)
# print(a)


#
# lst = []
# # if len(lst) == 0:
#
# if not lst:
#     print("Spisoc pustoy")


# lst = [5, 6, 8, 9, 7]
# print(5 not in lst)

# n1 = int(input("Vvedide razmer 1 cpiska: "))
# n2 = int(input("Vvedide razmer 2 cpiska: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Perviy spisok:", a)
# print("Vtoroy spisok", b)
# c = a + b
# print("Treriy spisok: ", c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Elementy oboix spiskov bez povtor: "c)

# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)


# c = [min(a), min(b), max(a), max(b)]
# print(c)



# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# print()
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end = "\t")
#     print()
# print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()




# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#    # print(row)
# for x in row:
#         print(x, end="\t")
# print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#         print(x, "+",  y, "=", x + y)


# w, h = 5, 3
# matrix = [[random.randint(0, 100) for x in range(w)] for y in range(h)]
# print(matrix)
# print()
# for row in matrix:
#    # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# w, h = 3, 4
# sum = 0
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#    # print(row)
#    for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#                 sum += 1
#
#    print()
# print("Kol-vo otr el: ", sum)



#Modules

# import math
#
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))   #4
# print(math.floor(3.8))   #3

# import math as  m
#
# print(m.ceil(3.2))
# print(m.floor(3.8))


# from math import ceil, floor
#
# print(ceil(3.2))
# print(floor(3.8))


# from math import *
# print(ceil(3.2))
# print(floor(3.8))

# from math import pi
#
# radius = int(input("Vvedite radius okr: "))
# print("Dlina okr: ", round(2 * pi * radius))

# from math import sqrt
# a = int(input("Vvedite katet1: "))
# b = int(input("Vvedite katet2: "))
# print("Gipotenuza: ", sqrt(a**2 + b**2))

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "")

# seconds = time.time()
# print(seconds)
# print(time.ctime())
# res = time.localtime()
# print(res)
# print(res.tm_mday, "." , res.tm_mon , "." , res.tm_year)
#
#
# print(time.strftime("сегодня: %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))


# pause = 5
# print("Programma zapuska")
# time.sleep(pause)
# print(pause, "sec")


# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# print()
#
#
# def hello(name):
#     print("hello", name)
#
#
# hello("irina")
# hello("ivan")



# def get_sum( a, b):
#     print("hello")
#     return a + b
#
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 6
# m = 3

#
# get_sum(n, m)
#
# get_sum('abc', 'def')

# a = [int(input("Кол-во элементов списка: "))]
# c = []
# for i in range(len(a)):
#     b = int(input("Введите число кратное 3: "))
#     if b % 3 == 0:
#         c.append(b)
#     else:
#         print(b, "не делится на 3 без остатка.")
# print(c)


# i = 0
# a = int(input("кол-во символов: "))
# b = input("Тип символа: ")
# print("0 - горизонтальная")
# print("1 - вертикальная")
# c = int(input("ориентация линии: "))
# while i < a:
#     if c == 0:
#         print(b * a)
#         break
#     else:
#         print(b)
#     i += 1



# a = [int(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
# count = 0
# print()
#
#







# #dz
# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс: "))
# c = int(input("Введите значение: "))
# a.insert(k, c)
# print(a)

#
# i = 0
# a = int(input("кол-во символов: "))
# b = input("Тип символа: ")
# print("0 - горизонтальная")
# print("1 - вертикальная")
# c = int(input("ориентация линии: "))
# while i < a:
#     if c == 0:
#         print(b * a)
#         break
#     else:
#         print(b)
#     i += 1

# c = []
# a = int(input("Кол-во элементов списка: "))
# for i in range(a):
#     b = int(input("Введите число кратное 3: "))
#     if b % 3 == 0:
#         c.append(b)
#     else:
#         print(b, "не делится на 3 без остатка.")
# print(c)



# from math import pi
#
# print("Выбор фигуры: ")
# print("1 - треугольник")
# print("2 - прямоугольник")
# print("3 - круг")
# x = int(input(": "))
# for i in range(x):
#     if x == 1:
#         a = int(input("Введите основание а = "))
#         b = int(input("Введите высоту b = "))
#         print(1/2*a*b)
#     elif x == 2:
#          c = int(input("Введите сторону а = "))
#          d = int(input("Введите сторону b = "))
#          print(c*d)
#          break
#     else:
#          a = int(input("Введите радиус: "))
#          print(2*pi*a)
#          break

#
# sum = 0
# a = [float(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности:")))]
# print("Количество чисел: ", len(a))
# for i in range(len(a)):
#     sum += a[i]
# print("Среднее арифметическое: ", sum/len(a))
# print("Минимальное число: ", min(a))
# print("Максимальное число: ", max(a))


#22.01


#
# def get_sum(a, b):
#     print(a + b)
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
#
#
# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
#
#
# m = maximum(9, 6)
# print(m)


# c = 0
# def math(a, b):
#     if a > b:
#         c = a - b
#         return c
#     else:
#         c = a + b
#         return c
#
#
#
# m = math(int(input("a = ")), int(input("b = ")))
# print(m)

#
# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "В кубе равно = ", cube(i))


#
# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop()
#     lst.append(end)
#     lst.insert(0, start)
#     return lst



#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

#
# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(5, 10))
# a = 10
# b = 5
# if func(a, b):
#     print("PErvoe chislo bolshe vtorogo")
# else:
#     print("Vtoroe cjislo bolshe pervogo")


#
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#
#
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
#
# p = input("Vvedite parol: ")
# if check_password(p):
#     print("Eto nadegny parol")
# else:
#     print("Eto nenadeg parol")



#
#
# def get_sum(a, b, c, d=1):
#     return  a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))

#
#
# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# s = "#"
# set_param(s=s)



# def digit_sum(n, even=True):
#     s = 0
#     while n>0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
#
# print("Summa chetnyx cifr")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
#
# print("Summa nechetnyx cifr")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("name:", name, "\nAge:", age)
#
#
# # display_info("Ira", 23, nm)
# # display_info(23, "Ira")
# # display_info(age=23, name="Ira")
# display_info(nm="Igor", age=23, name="Ira")


# a = "Hello"
# b = "Hello"
# b = b + "_new"
# print(a == b)
# print(a is b)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)
# print(lst1 is lst2)


#изменяемые объекты:  list
#неизменяемые объекты  : int, float, bool, str


# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))

#кортежи (tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst. __sizeof__())
# print(tpl. __sizeof__())




# a = "red", "blue", "green"
# print(a)
# print(type(a))


#
# a = (5,)
# print(a)
# print(type(a))


# a = tuple("Hello")
# a = tuple([1, 5, 3, 6])
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])






#
# def prymoug(a, b):
#     return a*b
#
#
# def trio(h, c):
#     return h*c/2
#
#
# def krug(r):
#     return 2*3.14*r
#
#
# x = int(input("1-прямоугольник, 2-треугольник, 3-круг: "))
# if x == 1:
#     one = int(input("Cторона1: "))
#     two = int(input("Cторона2: "))
#     print(prymoug(one, two))
# elif x == 2:
#     one = int(input("Высота: "))
#     two = int(input("Основание: "))
#     print(trio(one, two))
# else:
#     one = int(input("Радиус: "))
#     print(krug(one))




# sum = 0
# a = [float(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности:")))]
# print("Количество чисел: ", len(a))
# for i in range(len(a)):
#     sum += a[i]
# print("Среднее арифметическое: ", sum/len(a))
# print("Минимальное число: ", min(a))
# print("Максимальное число: ", max(a))



# s = tuple(i for i in range(5))
# s = tuple(input("->") for i in range(5))
# s = tuple(randint(20, 40) for i in range(5))
# print(s)


# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4))
# print(t3.index('l1', 4)) #ошибка
# ch = "w"
# try:
#     print(t3.index(ch))
# except ValueError:
#     print("Takogo simvola net")
# for i in t3:
#     print(i, end="")
#


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
# def ran(a, b):
#     return tuple(randint(a,b) for i in range(10))

# def foo(a, b):
#     res = a + b
#     c = res.count(0)
#     return res, c
#
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# print(foo(tpl1, tpl2))



# t = (10, 11, (1, 2, 3), [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t     #распаковка кортежа
# print(x, y, z)


#
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])




# def func(lst):
#     return sum(lst),len(lst)
#
# a, b = func([2, 6, 4, 5, 6, 7, 435, 34, 56, 45])
# print("Сумма: ", a)
# print("Kol-vo: ", b)
#
# for i in 1, 2, 3, 5, 7:
#     print(i)
#
# for i in "red", :
#     print(i)



# lst = [1, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst1 = list(tpl)
# print(lst1)



# countries = (
#     ("Гкрмания", 80.2, (("Belin", 3.326), ("Gamburg", 1.718 ))),
#     ("France", 43.2, (("Paris", 5.765), ("Marsel", 2.718 )))
# )
# print(countries)


# for country in countries:
#     country_name, country_population, cities = country
#     print("\nCtrana: ", country_name,", Naselenie = ",  country_population, sep = "")
#     for city in cities:
#         city_name, city_population = city
#         print("\tGorod: ", city_name,", Naselenie = ", city_population, sep="")

#множество(set) - неупорядлчная коллекция, уоторая содержит только уникальные элементы
# s = {'banana', 'apple', 'orange', 'banana'}
# print(s)
# print(len(s))
# print(type(s))
# for i in s:
#     print(i)


# s = {'banana', 'apple', 'orange', 'banana'}
# print(s)
# st = set(s)
# s1 = list(st)
# print(s1)


# a = set("hello")
# print(type(a))
# print(a)


# s = {input("->") for i in range(5)}
# print(s)

# a = set("hello")
# print(a)
# print('o' in a)
# print('a' in a)
# a.add("a")
# print(a)
# a.remove("e")
# print(a)
# el = "e1"
# if el in a:
#     a.remove(e1)
# print(a)    #KeyError
# a.discard("o")
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)



