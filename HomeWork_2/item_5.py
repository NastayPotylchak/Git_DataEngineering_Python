# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

rating_list = [7, 5, 3, 3, 2]

element = int(input('Введите новый элемент рейтинга: '))
is_insert = False

for el in rating_list:
    if element > el:
        rating_list.insert(0, element)
        is_insert = True
        break

    elif element == el:
        count_pos = rating_list.count(el)
        rating_list.insert(rating_list.index(el) + count_pos, element)
        is_insert = True
        break

if not is_insert:
  rating_list.append(element)

print('Рейтинг: ', rating_list)

