# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

list_numbers = [5, 78, 94, 6, 74, 25, 11, 4, 9,10, 88, 42]

file_numbers = open('file_item5.txt', 'w')

with file_numbers:
    file_numbers.write(' '.join(map(str, list_numbers)))

file_numbers_read = open('file_item5.txt', 'r')

with file_numbers_read:
    list_number = list(map(int, file_numbers_read.read().split(' ')))

print(f"Сумма чисел в файле = {sum(list_number)}")