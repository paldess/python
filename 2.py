def param(city, name, age, thername, uear):
    return f'{thername} {name}, из города {city}, {uear}-го года рождения. Возраст {age} лет. '


print(param(name=input("Ваше имя: "), thername=input('Ваша фамилия: '), age=input('Ваш возраст:'),
            city=input('Ваш город: '), uear=input('Ваш год рождения: ')))
