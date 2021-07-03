import random

a = random.randint(-1,6)

print(a)


if 1 == 1:
    print("true")


print('Дoбpo пожаловать к нам в ООО "Системы безопасности ". ')
print( ' - - Безопасность - наше второе имя\n')
password = input("Введите пароль : ")
if password == "secret":
    print( "Дocтyп открыт")
    input(" \n\nHaжмитe Enter . чтобы выйти . ")
else:
    print("next step")

