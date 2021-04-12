vir_ka = int(input('Выручка =  '))
izd = int(input('Издержки = '))
if vir_ka > izd:
    rent = (vir_ka-izd)/vir_ka*100
    print(f'Прибыль в этом месяце составила {vir_ka - izd}, рентабельность  {rent:.2f}%')
    sotrudniki = int(input('Введите кол-во сотрудников: '))
    print(f'В расчете на каждого сотрудника - {(vir_ka-izd)/sotrudniki}')
else:
    ubitok = izd-vir_ka
    print(f'К сожалению фирма понесла убытки в размере {ubitok} ')