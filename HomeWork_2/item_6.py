import ast

NAME = 'название'
PRICE = 'цена'
TOTAL = 'количество'
MEASURE = 'ед'

list_products = []
list_name = []
list_price = []
list_total = []
list_measure = []

dict_analytics = {NAME: list_name,
                  PRICE: list_price,
                  TOTAL: list_total,
                  MEASURE: list_measure
}

count_elements = int(input('Введите кол-во товаров: '))

for i in range(count_elements):
    input_list = []
    input_str = input('Введите характеристики товара через пробел (название, цена, кол-во и ед.измерения соответсвенно): ')
    input_list = list(input_str.split())
    dict_str = '"{}": "{}", "{}": {}, "{}": {}, "{}": "{}"'.format(NAME, input_list[0], PRICE, input_list[1], TOTAL, input_list[2], MEASURE, input_list[3])
    dict_str = ast.literal_eval('{' + dict_str + '}')
    list_products.append(i+1)
    list_products.append(dict_str)

list_itog = [tuple(list_products[i:i + 2]) for i in range(0, len(list_products), 2)]

print('Полученный список: ')
print(list_itog)

for l in list_itog:
    if not (l[1].get(NAME) in list_name):
        list_name.append(l[1].get(NAME))

    if not (l[1].get(PRICE) in list_price):
        list_price.append(l[1].get(PRICE))

    if not (l[1].get(TOTAL) in list_total):
        list_total.append(l[1].get(TOTAL))

    if not (l[1].get(MEASURE) in list_measure):
        list_measure.append(l[1].get(MEASURE))

dict_analytics.update({NAME: list_name, PRICE: list_price, TOTAL: list_total, MEASURE: list_measure})

print('Аналитика по товарам: ')
print(dict_analytics)
