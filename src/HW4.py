user_input = input('Введіть будь ласка текст: ')
print(user_input)
if user_input.isnumeric():
    user_input = int(user_input)
    if user_input % 2 == 0:
        print('Число є парним')
    else:
        print('Число є непарним')
elif user_input.isalpha():
    user_input_len = len(user_input)
    print('Кількість букв в тексті становить')
    print(user_input_len)
