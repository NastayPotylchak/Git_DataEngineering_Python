# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число '))
max_digit = 1

if number > 0:
    number_copy = number

    while (number):

            number_mod = number % 10

            if number_mod > max_digit:
                max_digit = number_mod

            number = number // 10
    else:
        str_result = f'Максимальная цифра в числе {number_copy} это {max_digit}'
        print(str_result)
else:
    print('Значение должно быть больше 0.')