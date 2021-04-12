number = int(input('Введите число: '))
max_number = 0
while number > 1:
    i = number % 10
    if i > max_number:
        max_number = i
    number //= 10
print(max_number)