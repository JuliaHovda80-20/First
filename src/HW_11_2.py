class Divider:
    def __enter__(self):
        print("==========")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Error occurred: {exc_type.__name__}: {exc_value}")
        print("==========")
        return True


with Divider():
    with Divider():
        x = 0
        y = 0
        z = x / y
        print(z)
