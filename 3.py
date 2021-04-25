print('Работа над файлом oklad.txt\n', '*'*30)

with open('oklad.txt') as txt:
    text = txt.readlines()
    text_2 = (text[i].split() for i in range(len(text)))
okl20k = []
sr = []
print('Оклад больше 20 тыс:\n','*'*30)
for i in text_2:
    if float(i[1]) >= 20000:
        print(f'{i[0]} ')
    sr.append(float(i[1]))
print('*' * 30)
print(f'Средний оклад: {round(sum(sr)/len(sr), 2)}')