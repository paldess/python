with open('one-two.txt') as tt:
    text = tt.readlines()

origin = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'ноль']
ang_origin = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'null']
with open('один-два.txt', 'w') as ttw:
    for i in text:

        for j in ang_origin:

            if i.split()[0].lower() == j:
                index = ang_origin.index(j)
                print(f'{origin[index]} {i.split()[1]} {i.split()[2]}')
                ttw.write(f'{origin[index]} {i.split()[1]} {i.split()[2]}\n')