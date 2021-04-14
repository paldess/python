string = input('Введите строку: \n')

string = string.split()
for i, el in enumerate(string, 1):
    print(f'{i} - {el[:10]}')

