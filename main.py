import random as ran

def user_input():
    lang_pwd = int(input("Введите желаемый язык пароля. Русский - 1, English - 2: "))
    len_pwd = int(input("Введите желаемое количество слов в парольной фразе: "))
    sep_pwd = input("Введите желаемый разделитель слов: ")
    return lang_pwd, len_pwd, sep_pwd
    
