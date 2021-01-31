# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ErrorDivZerro(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

x = float(input('Введите делимое: '))
y = float(input('Введите делитель: '))

try:
    if y == 0:
        raise ErrorDivZerro('На ноль делить нельзя.')
    else:
        result_div = x / y
        print(f"Результат деления: {result_div}")
except ErrorDivZerro as error:
    print(error)
