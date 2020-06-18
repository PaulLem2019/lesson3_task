"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""

def max_two_from_three (var_1, var_2, var_3):
    if var_1 < var_2 and var_1 < var_3:
        return var_2 + var_3
    if var_2 < var_1 and var_2 < var_3:
        return var_1 + var_3
    if var_3 < var_1 and var_3 < var_2:
        return var_1 + var_2

var_1 = 5
var_2 = 10
var_3 = 15

print (f'Сумма наибольших двух аргументов из {var_1}, {var_2}, {var_3} равна {max_two_from_three(var_1, var_2, var_3)}')

var_1 = 25
var_2 = 10
var_3 = 15

print (f'Сумма наибольших двух аргументов из {var_1}, {var_2}, {var_3} равна {max_two_from_three(var_1, var_2, var_3)}')

var_1 = 25
var_2 = 30
var_3 = 15

print (f'Сумма наибольших двух аргументов из {var_1}, {var_2}, {var_3} равна {max_two_from_three(var_1, var_2, var_3)}')
