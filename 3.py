def my_func(x, y, z):
    list = [int(x), int(y), int(z)]
    list.sort()
    print(list)
    return (int(list[1]) + int(list[2]))

input_number = input('Введите 3 числа через пробел: ')
input_number = input_number.split()
print(my_func(input_number[0], input_number[1], input_number[2]))