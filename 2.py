my_list = list()
while True:
    in_list = input('Введите добавляемый элемент списка либо "end" для завершения ввода: \n')
    if in_list == 'end':
        break
    else:
        my_list.append(in_list)
print(my_list)
for i in range(len(my_list)):
    if i%2 != 0:
        my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
print(my_list)