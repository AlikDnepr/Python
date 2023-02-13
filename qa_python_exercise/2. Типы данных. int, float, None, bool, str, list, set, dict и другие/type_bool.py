# False
bool()
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# True
bool(True)
bool(1)

# operators
print(5 > 6)
print(5 != "5")
print([1] == [1])
print("a" in "string with char")

print(not True)
print(True and False)
print(True or False)

print(not True and True)  # True
print(not (True and True))  # False

print(True and False or True)  # True
print(True and True or False)  # True
print(True and not False or False)  # True
