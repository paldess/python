q = 0
out = 0
def my_func(string):
    global q, out
    lists = string.split()

    iter = 0
    for i in lists:
        if i == 'q':
            q = 1
            break
        try:
            out += float(i)
            iter += float(i)
        except ValueError:
            print('Вводите либо действительные значения либо "Q"! Пропускаем ошибочный символ...')
    return out, iter, q

while q != 1:
    input_str = input('Введите значения через пробел для суммы, либо Q для выхода: \n')
    sum_out = my_func(input_str)
    print(f'Общая сумма = {round(sum_out[0], 2)}\nСумма итерации = {round(sum_out[1], 2)}')
