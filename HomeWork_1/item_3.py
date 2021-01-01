#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_n = int(input("Введите число n: "))
i = number_n
summ = 0

for n in range(number_n):
    summ = summ + number_n
    number_n = number_n*10 + i

print('Сумма: ', summ)
