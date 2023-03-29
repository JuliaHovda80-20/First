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
    my_dict[key_word] = phone_number
    return my_dict


def delete_name(my_dict, key_word):
    """
    Ця функція видаляє записи за ключовими словами
    """
    del my_dict[key_word]
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
    user_command = input("Оберіть дію:")
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
    elif user_command[0] == 'show':
        show_name(my_dictionary, user_command[1])
