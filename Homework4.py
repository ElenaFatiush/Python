def zadacha_1():

    # Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

    n_list = []
    n_num = int(input("N: "))
    simple = 2
    n_list.append(simple) 
    while simple <= n_num:
        if n_num % simple == 0:
            if simple != 2:
                n_list.append(simple)
            n_num //= simple
            simple = 2
        else: simple += 1
    print(n_list)

# zadacha_1()

def zadacha_2():
    # Задайте последовательность чисел. Напишите программу, 
    # которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.

    init_list = [1, 2, 3, 2, 4, 4]
    print('исходный список => ', init_list)
    result_list = []
    for i in init_list:
        if i not in result_list:
            result_list.append(i)
    print('неповторяющиеся элементы:', result_list)

#zadacha_2()

def zadacha_3():
    #В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
    # которые имеют средний балл более «4». Нужно перезаписать файл.

   n_list = ['\nAngela 5', '\nOlga 4','\nAlexander 5','\nVictor 3','\nPetr 4','\nEva 5','\nKristina 4','\nArina 5']
   data = open('file.txt', 'w')
   data.writelines(n_list)
   data.close()

   for i in range(0,len(n_list)):    
        if ('4' in n_list[i]) or ('5' in n_list[i]):
            n_list[i] = n_list[i].upper()

   path = 'file.txt'
   data = open(path, 'w+')
   for i in n_list:    
        data.write(f'{i}\n')
   data.close()




    

zadacha_3()