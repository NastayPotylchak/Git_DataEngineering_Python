# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce

def func_mult(number1, number2):
    return number1 * number2

number_list = [number for number in range(100, 1001) if number % 2 == 0]

result = reduce(func_mult, number_list)

print('Произведение всех элементов списка = ', '{:,}'.format(result).replace(',', ' '))
