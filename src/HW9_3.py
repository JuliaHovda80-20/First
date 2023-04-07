def factor_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factor_recursive(n - 1)


# Запит до користувача ввести число, яке потрібно перевірити
number = int(input("Введіть число: "))

# Перевіряємо, чи є введене число невід'ємним цілим числом
if number < 0:
    print("Введіть додатнє число")
else:
    print("Факторіал числа", number, "дорівнює", factor_recursive(number))