from string import punctuation
user_input = input('Введіть будь ласка текст: ')
for element in user_input:
    print(element)
    if element.isdigit():
        print("Це число")
        element = int(element)
        if element % 2 == 0:
            print("Число парне")
        else:
            print("Число не парне")
    elif element.isalpha():
        print("Це буква")
        if element.isupper():
            print("Буква велика")
        else:
            print("Буква маленька")
    elif element in punctuation:
        print("Це спеціальний символ")
    else:
        print("ТИ ХТО?")