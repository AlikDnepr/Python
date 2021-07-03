import random

i = 0
while i < 10:
    i = i + 1
    mood = random.randint(1,3)
    if mood == 1:
        print("равно 1")
    elif mood == 2:
        print("равно 2")
    elif mood == 3:
        print("равно 3")
    else:
        print("Рендом не верный")


response = ""
while response !="Потому что.":
    response = input("Пoчeмy?\n")
    print( " A . ладно.")