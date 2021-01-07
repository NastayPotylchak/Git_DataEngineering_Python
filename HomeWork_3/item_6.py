# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(word):
    return word.capitalize()

list_words = list(input('Введите строку, разделяя слова пробелами: ').split())
list_capitalize = []

for word in list_words:
    list_capitalize.append(int_func(word))

str_capitalize = " ".join(list_capitalize)

print(str_capitalize)

