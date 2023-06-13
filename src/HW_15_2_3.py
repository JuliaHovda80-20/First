# import re
#
# # отримуємо ім'я файлу від користувача
# filename = input("Введіть назву файлу: ")
#
# # зчитуємо текст з файлу
# with open(filename, "r") as f:
#     text = f.read()
#
# # знаходимо всі електронні адреси у тексті та замінюємо їх на "*@*"
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# replaced_text = re.sub(pattern, '*@*', text)
#
# # виводимо замінений текст
# print(replaced_text)
#

# import re
#
# # отримуємо ім'я файлу від користувача
# filename = input("Введіть назву файлу: ")
#
# # зчитуємо текст з файлу
# with open(filename, "r") as f:
#     text = f.read()
#
# # знаходимо всі електронні адреси у тексті та замінюємо їх на "X***@****X"
# pattern = r'\b([A-Za-z])[A-Za-z0-9._%+-]*@([A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\b'
# replaced_text = re.sub(pattern, r'X***@\2X', text)
#
# # виводимо замінений текст
# print(replaced_text)
import re
email = 'example@gmail.com'
first_letter = email[0]
last_letter = email.split('@')[0][-1]
email = email.replace(email.split('@')[0], '*' * len(email.split('@')[0]))


filename = input("Enter file name: ")
with open(filename, 'r') as f:
    text = f.read()

# регулярний вираз для знаходження електронної адреси
pattern = r'[\w\.-]+@[\w\.-]+'

# замінюємо кожну електронну адресу у тексті на <перша літера><зірочки><остання літера>
text = re.sub(pattern, lambda match: f"{match.group(0)[0]}{'*'*(len(match.group(0))-2)}{match.group(0)[-1]}", text)

print(text)
