# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(first_name, last_name, bd_year, home_town, email, phone):
    result = f"Пользователь {first_name} {last_name}. {bd_year} г.р.. Проживающий в городе {home_town}. " \
             f"Контакты: email = {email}; телефон = +{phone}"
    return result

print(user_info(first_name='Максим',last_name='Иванов',bd_year=1987,home_town='Белгород',
                email='max@mail.ru',phone='79884557788'))