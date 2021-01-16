# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
import json

list_income_to_20 = []
income_avg = 0

file_income = open('file_item3.json', 'r')

with file_income:
    data_income = json.load(file_income)

    d_list = data_income.get('income_workers')

    for l in d_list:
        for key, value in l.items():
            if value < 20000:
                list_income_to_20.append(key)

            income_avg += value

    income_avg = round(income_avg / len(d_list), 2)

print(f"Оклад < 20000 у сотрудников: {list_income_to_20}")
print(f"Средняя величина дохода сотрудников: {income_avg}")



