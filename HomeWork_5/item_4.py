# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import json

dict_Num_ENG_RU = {"One": "Один",
                   "Two": "Два",
                   "Three": "Три",
                   "Four": "Четыре"
                  }

dict_numeric_ru = {}

file_numeric = open('file_item4.json', 'r')

with file_numeric:
    dict_numeric_eng = json.load(file_numeric)

    for numeric_eng, numeric in dict_numeric_eng.items():
        key_ru = dict_Num_ENG_RU.get(numeric_eng)
        dict_numeric_ru[key_ru] = numeric

file_numeric_ru = open('file_item4_result.json', 'w', encoding='utf-8')

with file_numeric_ru:
    json.dump(dict_numeric_ru, file_numeric_ru, ensure_ascii= False)

