"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(in_word):
    return in_word.capitalize()

def int_func_str (in_str):
    ret_str = ""
    for item in in_str.split(" "):
        ret_str += int_func(item) + " "

    return ret_str


str = "sd fsdgsdfgf str f thzew wer aewtrh ytdhrty"

print (int_func(str))

print (int_func_str(str))