import json

with open('zadacha-7.txt', encoding="utf-8") as tt:
    text = tt.read().split('\n')
slovar_pr = {}
slovar_ub = {}
for i in text:
    if len(i.split(' ')[0]) > 0:
        prib = int(i.split(' ')[2]) - int(i.split(' ')[3])
        if prib > 0:
            slovar_pr[i.split(' ')[0]] = prib
        elif prib < 0:
            slovar_ub[i.split(' ')[0]] = prib
sr_zn = 0
for i in slovar_pr:
    sr_zn += slovar_pr[i]
sr_zn /= len(slovar_pr)



itog_slovar = {'С прибылью': slovar_pr, 'С убытками': slovar_ub, 'Средняя прибыль': sr_zn}
print(itog_slovar)
with open('zadacha-7(dump).txt', 'w', encoding="utf-8") as tt:
    json.dump(itog_slovar, tt, ensure_ascii=False)