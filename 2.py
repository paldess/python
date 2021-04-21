import random as r
def list_(list):
    try:
        out = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
        return out
    except TypeError:
        print('введите числовой список!')
        exit(0)


list = []
for i in range(1, 20):
    list.append(r.randint(-100, 100))
print(list)
print(list_(list))