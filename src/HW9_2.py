
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        next_element = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
        return next_element


# Запит до користувача ввести число, яке потрібно перевірити
number = int(input("Введіть число: "))

# Перевіряємо, чи є введене число невід'ємним цілим числом
if number < 0:
    print("Введіть додатнє число")
else:
    print("Послідовність Фібоначчі:")

print(fibonacci_recursive(number))
