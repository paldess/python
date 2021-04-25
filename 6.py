with open('zadacha-6.txt') as tt:
    text = tt.readlines()
slovar = {}
for i in text:
    number = i.split(':')[1]
    for j in number:
        if not j.isdigit():
            number = number.replace(j, ' ')

    slovar[i.split(':')[0]] = number
for i in slovar:
    slovar[i] = sum(int(i) for i in slovar[i].split())

print(slovar)