# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

# num_day = int(input('Введите цифру от 1 до 7: '))
# if num_day > 7 or num_day < 1:
#     print('Введи цифру от 1 до 7, дружок!')
# elif 1 <= num_day <= 5:
# elif 1 <= num_day <= 5:
#     print('Нет, еще будний день')
# else:
#     print("Ура, выходной!")

#2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Нужно написать таблицу истинности.

# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             print(f'При x = {x}, y = {y}, z = {z} - {not (x or y or z) == (not x) and (not y) and (not z)}')
#             # При таком выводе в таблице присутствуют и True и False
            
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             print(not (x or y or z) == ((not x) and (not y) and (not z)))
#             print(x, y, z)
            # А при таком выводе все True. Не совсем понимаю, почему так. Мне казалось, что оба варианта записи верные


#3- Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# while True:
#     try:
#         x, y = int(input('Введите значение x: ')), int(input('Введите значение y: '))
#         break
#     except ValueError:
#         print('Введите корректные данные')
        
# if x == 0 or y == 0:
#     print('Координаты лежат на оси')
# elif x > 0 and y > 0:
#      print('Точка находится в первой четверти')
# elif x < 0 and y > 0:
#      print('Точка находится во второй четверти')
# elif x < 0 and y < 0:
#      print('Точка находится в третьей четверти')
# elif x > 0 and y < 0:
#      print('Точка находится в четвертой четверти')
# else:
#      print('Точка вне четверти')

     # Можно сделать так, что если  x > 0, то второе if с условиями для y. И else если x < 0, с if с условиями для y

# 4-Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# num = int(input('Введите номер четверти '))
# if 0 < num < 5:
#     if num == 1:
#         print('x∈(0,∞) u y∈(0,∞)')
#     elif num == 2:
#         print('x∈(-∞,0) u y∈(0,∞)')
#     elif num == 3:
#         print('x∈(-∞,0) u y∈(-∞,0)')
#     elif num == 4:
#         print('x∈(0, ∞) u y∈(-∞,0)')
#     else:                                       # Нужен ли этот else или можно обойтись без него?
#         print('Это невозможно')
# else:
#     print('Введите корректный номер четверти')


# 5- Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними в 2D пространстве.

# xa = float(input('Введите значениe x первой точки'))
# ya = float(input('Введите значениe y первой точки'))
# xb = float(input('Введите значениe x второй точки'))
# yb = float(input('Введите значениe y второй точки'))
# distance = round(((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5, 2)
# print(f'Расстояние между точками равно {distance}')