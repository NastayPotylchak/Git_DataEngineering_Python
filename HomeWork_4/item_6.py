# итератор, генерирующий целые числа, начиная с указанного,
from itertools import count, cycle

number_start = int(input('Введите число-начало последовательности: '))
number_end = int(input('Введите число-конец последовательности: '))

for number in count(number_start):
    if number >= number_end:
        break
    else:
        print(number)

print('*' * 100)

# итератор, повторяющий элементы некоторого списка, определенного заранее.
list_example = [4, 5, 8, 9, 77, 2, 45]

print('Исходный список:', list_example)
point_break = int(input('Сколько раз желаете повторить? '))
x = 1

for l_example in cycle(list_example):
    if x > len(list_example) * point_break:
        break
    print(l_example)
    x+=1
