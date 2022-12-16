def zadacha_1():
    # Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

    input_text = input('Введите текст:\n').split()
    input_word = input('Введите слово, которое нужно удалить:\n')

    def delete_word(input_text: list, input_word: str) -> str:
        output_str=''
        for j in range(0, len(input_text)):
            if str(input_text[j]).find(input_word) == -1:
                output_str += input_text[j] + ''
        return output_str

    print(delete_word(input_text, input_word))

#zadacha_1()

from random import randint

def zadacha_2():
    # На столе лежит ___ конфета. Играют два игрока делая ход друг после друга. 
    # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем ___ конфет. 
    # Все конфеты оппонента достаются сделавшему последний ход. 
   
    print('          ============xxx============')
    print('Игра с конфетами, человек против человека.')
    print('          ============xxx============')
    candy = 350             # количество конфет
    max_candy_round = 28    # за один ход можно забрать не более чем 28 конфет
    count = randint(1, 2)   # для рандомного определения того кто ходит первым
    print(f'Колво конфет:{candy}, за один ход можно забрать не более чем {max_candy_round} конфет')
    print('          ============xxx============')
    print(f'Итак!  монета брошена первым ходит {count} игрок!')
    print('          ============xxx============')
    while candy >= 0:
        if count == 1:
            print(f'       оставшееся количество конфет =', candy)
            a = int(input('1 Игрок введите кол-во конфет которое хотите забрать =>'))
            if a > max_candy_round:
                print('ИГРОК 1 играет не по правилам!!!')
            else:
                candy -= a
                count = 2
            if candy <= 0:
                break
        else:
            print(f'       оставшееся количество конфет =', candy)
            b = int(input('2 Игрок введите кол-во конфет которое хотите забрать =>'))
            if b > max_candy_round:
                print('ИГРОК 2 играет не по правилам!!!') 
            else:
                candy -= b
                count = 1
            if candy <= 0:
                break

    if count == 2:
        print('1 ИГРОК WIIIN !!!')
    else:
        print('2 ИГРОК WIIIN !!!')

#zadacha_2()

def zadacha_3():
    # Создайте программу для игры в ""Крестики-нолики""

    field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def show_field(field):
        for i in range(3):
            print ("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")


    def input_data(player_mot):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_mot+"? ")
            try:
                player_answer = int(player_answer)
            except:
                print('Некорректный ввод. Вы уверены, что ввели число?')
                continue
            if player_answer >= 1 and player_answer <= 9:
                if (str(field[player_answer-1]) not in "XO"):
                    field[player_answer-1] = player_mot
                    valid = True
                else:
                    print('Эта клеточка уже занята')
            else:
                print('Некорректный ввод. Введите число от 1 до 9 чтобы походить.')
                

    def check_win(field):
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for each in win_coord:
            if field[each[0]] == field[each[1]] == field[each[2]]:
                return field[each[0]]
        return False    


    def main(field):
        counter = 0
        win = False
        while not win:
            show_field(field)
            if counter % 2 == 0:
                input_data("X")
            else:
                input_data("O")
            counter += 1
            if counter > 4:
                tmp = check_win(field)
                if tmp:
                    print(tmp, 'выиграл!')
                    win = True
                    break
            if counter == 9:
                print('Ничья!')
                break
        show_field(field)  

    main(field)      

zadacha_3()



    