def dub_element(my_set_1, my_set_2):
    new = set(my_set_1 & my_set_2)
    return new


def unic_element(my_set_1, my_set_2):
    new = set(my_set_1 | my_set_2)
    return new

"""
Введення елементів першої множини
"""

my_set_a_str = input("Введіть елементи першої множини через кому: ")
my_set_a = set(map(int, my_set_a_str.split(',')))
"""
Введення елементів другої множини
"""
my_set_b_str = input("Введіть елементи другої множини через кому: ")
my_set_b = set(map(int, my_set_b_str.split(',')))

common = dub_element(my_set_a, my_set_b)
print("Спільні елементи: ", common)

unic = unic_element(my_set_a, my_set_b)
print("Унікальні елементи: ", unic)

