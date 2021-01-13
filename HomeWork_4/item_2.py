# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# input_list = [1, 0, 3]
#input_list = [0, 2, 12, 7, 1, 6, 4, 10, 7, 1, 78, 123, 55]

result = [input_list[i+1] for i in range(len(input_list) - 1) if input_list[i+1] > input_list[i]]

print(result)