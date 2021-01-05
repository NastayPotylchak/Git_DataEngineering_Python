# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_change = list(input('Введите элементы списка через пробел: ').split())

list_count = len(list_change)
list_count = list_count if list_count % 2 == 0 else list_count // 2

for i in range(0, list_count, 2):
    list_change[i], list_change[i+1] = list_change[i+1], list_change[i]

print('Преобразованный список: ', list_change)