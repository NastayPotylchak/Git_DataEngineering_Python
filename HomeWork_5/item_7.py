import json

file_firms = open('file_item7.txt', 'r', encoding='utf-8')

dict_profit  = {}
dict_deficit = {}
dict_avg     = {}
list_profit_avg = []
list_deficit = []

sum_income = 0

with file_firms:
    data_firms = file_firms.readlines()

    for line in data_firms:
        list_firm_info = line.split()
        firm_name = list_firm_info[0]
        inc = float(list_firm_info[2])
        dec = float(list_firm_info[3])

        income = inc - dec # прибыль

        if income > 0:
            dict_profit[firm_name] = income
            sum_income+=income
        elif income < 0:
            dict_deficit[firm_name] = income

    dict_avg['average_profit'] = round(sum_income / len(dict_profit), 2)

    list_profit_avg.append(dict_profit)
    list_profit_avg.append(dict_avg)
    list_deficit.append(dict_deficit)

file_list_profit  = open('file_list_profit.json', 'w', encoding='utf-8')
file_list_deficit = open('file_list_deficit.json', 'w', encoding='utf-8')

with file_list_profit:
    json.dump(list_profit_avg, file_list_profit)

with file_list_deficit:
    json.dump(list_deficit, file_list_deficit)


