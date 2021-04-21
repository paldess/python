def one(l):
    out = [l[i] for i in range(len(l)) if not l[i] in l[:i] and not l[i] in l[(i+1):]]
    return out


list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 'd', 'd', 'g']
print(one(list))

