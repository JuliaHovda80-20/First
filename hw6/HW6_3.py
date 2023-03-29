"""
Знайти найбільший елемент масиву використати built-in функцію
"""
my_list = [0, 5, 9, 1, -4, 1, 7, 3, 100, 10]
print(max(my_list))

"""
Знайти найбільший елемент масиву створити свою функцію
"""
def my_max (my_list):
    n = len(my_list)
    max_el  = my_list[0]
    for i in range(n):
        element_1 = my_list[i]
        if element_1 > max_el:
             max_el = element_1
    return max_el
max_element = my_max(my_list)
print(max_element)

"""
Знайти найбільший елемент масиву використати лямбда функцію
"""
import functools
func = lambda a, b: a if a > b else b
lst_max = functools.reduce(func, my_list)
print(lst_max)