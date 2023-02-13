print("Exercise 1")
for element in range(1, 6):
    for count in range(1, element + 1):
        print(count, end=" ")
    print("\n")

print("Exercise 2")
num = 2
for item in range(1, 11):
    print(item * num, "\n")

print("Exercise 3")
for element in range(5, 0, -1):
    for count in range(element, 0, -1):
        print(count, end=" ")
    print("\n")

print("Exercise 4")
list1 = [10, 20, 30, 40, 50]
index = 0
for elements in list1:
    index += -1
    print(list1[index], "\n")

print("Exercise 5")
for i in range(-10, 0):
    print(i, "\n")

print("Exercise 5")
for i in range(1, 6):
    print(i * "* ", "\n")
for i in range(4, 0, -1):
    print(i * "* ", "\n")
