print("Exercise 1")
aLsit = [100, 200, 300, 400, 500]
aLsit.reverse()
print(aLsit)

print("Exercise 2")
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]]
print(list3)

print("decision 2")
concat = [
    l1 + l2
    for l1, l2 in zip(list1, list2)
]
print(concat)

print("Exercise 3")
aList = [1, 2, 3, 4, 5, 6, 7]
bList = []
for index in aList:
    bList.append(index ** 2)
print(bList)

print("Exercise 4")
list41 = ["Hello ", "take "]
list42 = ["Dear", "Sir"]
res = [x + y for x in list41 for y in list42]
print(res)

print("Exercise 5")
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y, "\n")

print("Exercise 6")
list11 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list11[2][2].append(7000)
print(list11)
