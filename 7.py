def fact(i):
    for r in range(1, (i + 1)):
        yield r


try:
    n = int(input("Введите число для вычисления факториала:  "))
except ValueError:
    print('некорректные данные!')
    exit()
if n < 0:
    print('факториал высчитывается для положительных чисел!')
    exit()
out = 1
for i in fact(n):
    out *= i

print(out)