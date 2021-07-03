import random
i = 0
x = 0
y = 0
a = 0
while i < 100:
    i += 1
    a = random.randint(1,2)
    if a == 1:
        x += 1
    elif a == 2:
        y += 1
    else:
        print("Something went wrong")
print("Решко выпало ",x, " раз")
print("Орел выпал ",y," раз")