
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         next_element = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#         return next_element
#
#
# # Запит до користувача ввести число, яке потрібно перевірити
# number = int(input("Введіть число: "))
#
# # Перевіряємо, чи є введене число невід'ємним цілим числом
# if number < 0:
#     print("Введіть додатнє число")
# else:
#     print("Послідовність Фібоначчі:")
#
# print(fibonacci_recursive(number))

def GetFibonacciList(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = GetFibonacciList(n-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# Отримуємо введення від користувача
num = int(input("Введіть число: "))

# Отримуємо список чисел Фібоначчі
fib_list = GetFibonacciList(num+1)

# Виводимо наступний елемент послідовності Фібоначчі
print("Наступний елемент послідовності Фібоначчі після числа", fib_list[-2], "є", fib_list[-1])
