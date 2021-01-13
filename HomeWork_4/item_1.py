# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час)
# + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт
# с параметрами.
from sys import argv

def calc_income(total_hours, rate, bonus):
    return round((total_hours * rate) + bonus, 2)

if len(argv) < 3:
    print("Ошибка. Слишком мало параметров.")
    exit(1)

total_hours = float(argv[1])
rate = float(argv[2])
bonus = float(argv[3]) if len(argv) >= 4 else 0

print(calc_income(total_hours, rate, bonus))