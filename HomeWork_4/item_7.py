def fact_n(n):
    f = 1
    for i in range(1, n+1):
        f*=i
        yield f

n= int(input('Вычислить факториал числа: '))
for el in fact_n(n):
    print(el)