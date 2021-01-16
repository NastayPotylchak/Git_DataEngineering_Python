# каждая строка описывает учебный предмет и наличие лекционных, пр-х и лаб. занятий и их количество
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
file_subjects = open('file_item6.txt', 'r', encoding='utf-8')
list_digit = []
is_find_digit = False
s_digit = ''
dict_subjects = {}

with file_subjects:
    data_subjects = file_subjects.readlines()

    for line in data_subjects:
        list_digit = []

        for i, symb in enumerate(line):
            if symb == ':':
                index_ = i

            if symb.isdigit():
                is_find_digit = True
                s_digit += symb
            elif is_find_digit:
                list_digit.append(int(s_digit))
                s_digit = ''
                is_find_digit = False

        key = line[:index_]
        value = sum(list_digit)
        dict_subjects[key] = value

print(dict_subjects)
