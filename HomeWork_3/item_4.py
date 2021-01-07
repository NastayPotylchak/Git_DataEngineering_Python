# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
VAR_X = 4
VAR_Y = -3

def my_func(x, y):
    return (1 / x**abs(y))

print ('Результат с помощью **: ', my_func(VAR_X, VAR_Y),)

def my_func_cycle(x, y):
    divisor = x
    for i in range(1, abs(y)):
        divisor*= x
    return (1 / divisor)

print ('Результат с помощью цикла: ', my_func_cycle(VAR_X, VAR_Y))
