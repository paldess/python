my_list = [7, 5, 3, 3, 2]
while True:
    number = input('Введите число или exit для выхода: \n')
    if number.replace('-', '').isdigit():
        if my_list[-1] > int(number):
            my_list.append(int(number))
            print(my_list)
            continue
        for i in range(len(my_list)):
            if my_list[i] < int(number):
                my_list.insert(i, int(number))
                print(my_list)
                break

    elif number == 'exit':
        break
    else:
        print('Введите число!')
