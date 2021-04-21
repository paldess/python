from itertools import cycle, count

def first(ot, do):
    out = []
    for close, i in enumerate(count(ot), ot):
        if close > do:
            return out
        out.append(i)

while True:
    deistv = input('Выберите номер подзадания задачи 6 \n'
                   'а) итератор, генерирующий целые числа, начиная с указанного \n'
                   'b) итератор, повторяющий элементы некоторого списка, определенного заранее \n'
                   'q) для завершения программы\n')

    if deistv == 'q':
        exit(0)
    elif deistv == 'a':
        try:
            y = int(input('Введите от какого значения: '))
        except TypeError:
            print('некоректные значения')
            break
        x = input('Введите до какого значения(по умолчанию до 15): ')
        if not x.isdigit():
            x = 15
        print(first(y, int(x)))
        print('-' * 30)
    elif deistv == 'b':
        inp = input('Что будем повторять?(через пробел): ')
        inp = inp.split()
        kolvo = int(input('Сколько раз повторить?: '))
        povtor_list = input('Повторить весь список или элементы списка?(1-весь список, 2-элементы списка): ')
        if povtor_list == '2':
            for i, j in enumerate(cycle(inp), 1):
                print(j)
                if i == kolvo:
                    break
        elif povtor_list == '1':
            chet = 0
            for i, j in enumerate(cycle(inp), 1):
                if i % len(inp) == 0:
                    print(j)
                    chet += 1
                else:
                    print(j, end=' ')
                if chet == kolvo:
                    break
        print('-' * 30)
    else:
        print('не понимаю.')