# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(argument1, argument2, argument3):
    list_sum = [argument1, argument2, argument3]
    max_0 = max(list_sum)
    list_sum.remove(max_0)
    max_1 = max(list_sum)
    return max_0 + max_1

print('Сумма двух наибольших чисел = ', my_func(9,4,9))