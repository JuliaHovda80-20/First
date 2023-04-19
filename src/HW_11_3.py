import datetime

def print_func_name_and_time(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Function {func.__name__} was called at {datetime.datetime.now()}.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@print_func_name_and_time(times=10)
def add(x, y):
    return x + y

add(0, 3)
