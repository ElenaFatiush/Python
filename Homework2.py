#Напишите программу, которая принимает на вход вещественное число 
#и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

#num = float(input('Вещественное число: '))
#sum = 0
#if(num<0):
#    num= -num    
#while(num!=int(num)):
#    num = round(num*10, len(str(num))-1)
#else: num=int(num)
#while num!=0:
#    sum += num%10
#    num = num//10
#print(sum)


# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список)
#  чисел от 1 до N.
# Не используйте функцию math.factorial.

#n_list = []
#factorial = 1
#for i in range(1, (int(input('N: ')))+1):
#    n_list.append(factorial)
#    factorial+=factorial*i
#print(n_list)




# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

import random

n_list = []
for i in range(1, (int(input('N: ')))+1):
    n_list.append(random.randint(-99, 100))
print(n_list,end=' => ')
for i in range(0, len(n_list)+1):
    if(n_list[i]<0):
        n_list.insert(i+1,0)
        i+=1
print(n_list)



