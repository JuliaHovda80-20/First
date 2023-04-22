import datetime

def print_func_name_and_time(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called at {datetime.datetime.now()}.")
        return func(*args, **kwargs)
    return wrapper

@print_func_name_and_time
def my_func(x, y):
    print("У мене вийшло)")

my_func(3, 5)