string = input('Введите строку: \n')
#print(list(enumerate(string.split(' '))))

string = string.split()
for i, el in enumerate(string):
    print(f'{i} - {el[:10]}')

