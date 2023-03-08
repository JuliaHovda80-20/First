a = " I love Python"
b = a*42
print(b)
print(" I love Python"*42)
age_in_month = 27 * 12
print(age_in_month)

age_in_years = 27
print(age_in_years)
age_in_years = age_in_month / 12
print(age_in_years)

age_in_years_str = str(int(age_in_years))    # двічі змінили тип даних щоб позбутись формату цілого числа і перетворили в текст


my_age = "Му name is Julia I’m " + age_in_years_str + " years old"

print(my_age)


k = 1
v = k == 6
print(v)

v = k != 1
print(v)

k = 1
v = k < 1
print(v)

k = 1
v = k <= 10
print(v)

k = 1
v = k >= 1
print(v)

a = "2"
b = "5"
c = "6"
d = (a + b + c)
print(d)

a = 2
b = 5
c = 6
d = str(a) + str(b) + str(c)
print(d)








