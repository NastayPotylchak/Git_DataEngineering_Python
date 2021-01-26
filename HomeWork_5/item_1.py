# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
txt_file = open('file_item1.txt', 'w')

input_data = None

with txt_file:
    while input_data != '':
        input_data = input('Введите данные: ')
        txt_file.write(input_data + '\n')