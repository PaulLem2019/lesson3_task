"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def divisor (div1, div2):
    if div2 == 0:
        # print("Знаменатель не должен быть равен нулю")
        return "Знаменатель не должен быть равен нулю"

    return div1/div2

def divisor_v2 (div1, div2):
    try:
        rezult = div1/div2
    except ZeroDivisionError:
        return 'Деление на ноль не допустимо'

    return rezult


numerator = float (input ("Введите значение числителя "))
denominator = float (input ("Введите значение знаменателя "))

print (f'Деление числитела {numerator} на знаменатель {denominator} равно {divisor(numerator, denominator)}')

print (f'Ver2_Деление числитела {numerator} на знаменатель {denominator} равно {divisor_v2(numerator, denominator)}')
