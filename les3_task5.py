"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""

def sum_string():
    bQuit = 1
    sum = 0
    while bQuit:
        numb_str = input("->")
        for item in numb_str.split(" "):
            if item == '.':
                bQuit = 0
                break
            if item.isalnum():
                sum += int(item)
    return sum


print ("Вводите целые числа через пробел, после приглашения '->'")
print ("для завершения ввода ввести: . (точка)")

print ("Сумма введенных чисел: ", sum_string())