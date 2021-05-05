class MyError(Exception):
    def __init__(self):
        self.text = 'это моя ошибка'
    def __str__(self):
        return self.text


class Data():
    date = input('Введите дату формата: день-месяц-год:   \n')

    @classmethod
    def classmetod(cls):
        date = cls.date.split('-')
        try:
            for i in date:
                if not i.isdigit():
                    raise MyError()
            date = map(int, date)
        except MyError:
            print('неверные данные')
            exit()
        return list(date)

    @staticmethod
    def static(a):
        day = a
        if 1 <= day[0] <= 31 and 1<= day[1] <= 12 and 1990 <= day[2] <= 2021:
            return 'данные верны'
        else:
            return 'проверьте данные (Д(1-31)-М(1-12)-Г(1990-2021))'
date = Data()
date1 = date.classmetod()
print(date1)
print(Data.static(date1))