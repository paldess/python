from functools import reduce

def func(el_1, el_2):
    return el_1 * el_2
summ = 0
print(reduce(func, [i for i in range(100, 1001) if i % 2 == 0]))

