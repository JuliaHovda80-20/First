my_set_1 = {1, 3.3, 'hello', 20, 30, 'python'}
result = list(filter(lambda x: isinstance(x, int), my_set_1))
print(result)


my_set_2 = {"hello", "Vitaliy", "python"}
result = list(map(str.upper, my_set_2))
print(result)