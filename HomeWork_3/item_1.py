# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func_div_numeric(numeric1, numeric2):
    try:
        return numeric1 / numeric2
    except ZeroDivisionError:
        print('На ноль делить нельзя')

numeric1 = int(input('Введите делимое: '))
numeric2 = int(input('Введите делитель: '))

result_div = func_div_numeric(numeric1, numeric2)

if (not result_div is None):
    print('Частное = ', result_div)