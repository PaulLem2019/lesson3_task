"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

def personal_data (first_name, last_name, birthday, residence_place, email, tel_number):
    return first_name+ " " + last_name + " " + birthday + " " + residence_place + " " + email + " " + tel_number

def personal_data_v2 (**kwargs):
    return kwargs



dp = personal_data(first_name = "Ivanov", last_name= "Petr", birthday="1985", residence_place="Moscow",
              email="email@mail.ru", tel_number="(495)365-29-45")

dp_v2 = personal_data_v2(first_name = "Ivanov", last_name= "Petr", birthday="1985", residence_place="Moscow",
              email="email@mail.ru", tel_number="(495)365-29-45")


print (dp)
print (dp_v2)

