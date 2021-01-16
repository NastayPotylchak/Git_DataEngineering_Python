# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
def get_words(str_words):
    str_words = str_words.replace("\n", " ")
    str_words = str_words.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    return str_words.split()

file_item2 = open('file_item2.txt', 'r', encoding = 'utf-8')

with file_item2:
    my_list = [line for line in file_item2]

print(f"Количество строк в файле =  {len(my_list)}")

print('^' * 50)

for i, el_str in enumerate(my_list):
    print(f"В  {i+1}-ой строке {len(get_words(el_str))} слов(а)")
