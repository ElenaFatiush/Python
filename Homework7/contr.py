import view
import import_data
import export

def main():
    request = view.choise()
    test_list = list(request[0].split())
    if 1 == request[1]:

        if (len(test_list) == 4):
            import_data.write_data(test_list)
        else:
            print('Введены некорректные данные')

    else:
        view.out_put(export.exp(test_list)) 

main()