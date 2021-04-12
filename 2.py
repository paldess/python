time = int(input('Введите время в секундах: '))
sek = time % 60
min_ = (time // 60) % 60
hour = (time // 60) // 60
print(f'{hour:02}:{min_:02}:{sek:02}')