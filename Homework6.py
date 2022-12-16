def zadacha_1():
    # Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

    n_str, find_str = ["123", "234", "123", "567"], "123"
    pos = -1 if (n_str.count(find_str) < 2) else list(filter(lambda x: x[1] == find_str, enumerate(n_str)))[1][0]
    print(f'Позиция второго вхождения "{find_str}" -> {pos}')
   

#zadacha_1()

import math, random

def zadacha_2():
# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    def enter_list_size ():
        n_list = [(random.randint(1,21)) for i in range(int(input('Размер списка: ')))]
        return n_list

    n_list = enter_list_size()
    print(n_list)

    normal_list = [(n_list[i]*n_list[(-1-i)]) for i in range(math.ceil(len(n_list)/2))]
    print(normal_list)
    lambda_map_list = list(map(lambda i: n_list[i]*n_list[(-1-i)], [i for i in range(math.ceil(len(n_list)/2))]))
    print(lambda_map_list)

#zadacha_2()


def zadacha_3():
    # 3-Сформировать список из N членов последовательности.

    print(list((-3)**i for i in range(int(input('N: ')))))
    print(list(map(lambda i: (-3)**i, [i for i in range(int(input('N: ')))])))

#zadacha_3()



def zadacha_5():

    # Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
    # Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, 
    # при условии, что они не совпадают.


    n_list = [random.randint(0,100) for i in range(200)]
    print(list(filter((lambda i: i[0]!=i[1]), enumerate(n_list))))

zadacha_5()

