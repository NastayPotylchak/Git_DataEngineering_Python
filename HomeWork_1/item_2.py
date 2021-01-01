#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

is_try = True

while is_try:
    time_seconds = int(input('Введите время в секундах '))

    if time_seconds > 0:
        hours = time_seconds // 3600
        minutes = (time_seconds // 60) % 60
        seconds = time_seconds % 60

        time = f"Time: {hours:02}:{minutes:02}:{seconds:02}"

        print(time)
    else:
        print('Значение должно быть больше 0.')
    is_try = input('Попробовать еще раз? ')
    if is_try != 'Да':
        is_try = False