# Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.
def recursion(n: int) -> None:
    print({n})
    if n == 0:
        return None
    recursion(n - 1)


user_input = input("Введіть ціле число:")
recursion(int(user_input))

