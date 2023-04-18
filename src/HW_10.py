my_dictionary = {}

def stats(my_dict):
    """
    Дана функція рахує кількість записів
    """
    print(len(my_dict))



def add_func(my_dict, key_word, phone_number):
    """
       Ця функція додає записи
    """
    import re
    # phone_number = int(phone_number)
    key_word = str(key_word)
    try:
        pattern = r'^\+380\d{9}$'  # Регулярний вираз для перевірки формату
        if re.match(pattern, phone_number):
            print("Номер телефону введено коректно!")
        else:
            raise ValueError("Номер телефону введено некоректно. Будь ласка, введіть номер у форматі +380xxxxxxxxx.")

    except ValueError as e:
        print("Помилка введення:", e)

    my_dict[key_word] = phone_number
    return my_dict


def delete_name(my_dict, key_word):
    """
    Ця функція видаляє записи за ключовими словами
    """

    try:
        del my_dict[key_word]

    except KeyError:
        print(key_word, "Такого імені у словнику немає")

    return my_dict


def name(my_dict):
    """
    Ця функція друкує записи
    """
    print(my_dict.keys())


def show_name(my_dict, phone_number):
    """
    Ця функція показує інфомрацію по імені
    """
    print(my_dict.get(phone_number))


while True:
    user_command = input("Що може робити дана телефонна книга:"
                         "\nstats - загальна кількість записів у телефонній книжці"
                         "\nadd - додати запис  !!Формат: команда ім'я номер!!"
                         "\ndelete - видалити запис  !!Формат: команда ім'я контакту!!"
                         "\nname - вивести в список всі імена контактів "
                         "\nshow - показати інформацію по імені !!Формат: команда номер телефону!!"
                         "\nВведіть команду:")

    user_command = user_command.split()
    if user_command[0] == 'stats':
        stats(my_dictionary)
    elif user_command[0] == 'add':
        x = add_func(my_dictionary, user_command[1], user_command[2])
        print(x)
    elif user_command[0] == 'delete':
        y = delete_name(my_dictionary, user_command[1])
        print(y)
    elif user_command[0] == 'name':
        name(my_dictionary)
    elif user_command[0] == 'show':     # такого імені (ключогового слова) не існує kye terror
        show_name(my_dictionary, user_command[1])
