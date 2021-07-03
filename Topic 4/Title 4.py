Oleg = ("asd","asd",3,21,4,1)
print(Oleg)
for item in Oleg:
    print(item)
print(len(Oleg))

print(len("asdasfasd"))

Oleh = ("asdasfasd")



print(Oleg[1:])
inventory= ("меч",
"кольчуга",
"щит",
"целебное снадобье")
chest = ("золото",1)
inventory += chest
print(inventory)
a = inventory[1:2] + chest[:2]
print(a)
