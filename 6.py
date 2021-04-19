def in_func(text):
    return text.title()


input_text = input('Введите текст    ')
input_list = input_text.split()
for i in input_list:

    print(in_func(i), end=' ')