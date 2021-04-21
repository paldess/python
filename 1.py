from sys import argv


# параметры должны быть введены в порядке: 1.выработка часов, 2.ставка за час,
# 3.проценты премии(не обязательно-приравняется 0)


list_zp = argv
if list_zp == 4 or list_zp == 3:
    for i in range(1, len(list_zp)):
        if not list_zp[i].isdigit():
            print(f'введите лишь числовое значемие вместо {list_zp[i]}')
            exit(0)
if len(list_zp) == 4:
    print(f'Заработная плата сотрудника(премия {list_zp[3]}%):  \
    {int(list_zp[1]) * int(list_zp[2]) + (int(list_zp[1]) * int(list_zp[2]) * int(list_zp[3]))}')
elif len(list_zp) == 3:
    print(f'Заработная плата сотрудника(премия 0%):  \
    {int(list_zp[1]) * int(list_zp[2])}')

else:
    print('Необходимо 2 обязательных параметра: кол-во часов, ставка з/п(в час), и 1 необязательный- премия(в %)')
    print(f'У Вас введено параметров: {len(list_zp)-1}' )