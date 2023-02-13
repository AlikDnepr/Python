print("Exercise 1")
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
toList = list(sampleSet)
answer = set(toList + sampleList)
print(answer)

print("Exercise 2")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)

print("Exercise 3")
set31 = {10, 20, 30, 40, 50}
set32 = {30, 40, 50, 60, 70}
set33 = set31.union(set32)
print(set33)

print("Exercise 4")
set41 = {10, 20, 30}
set42 = {20, 40, 50}
set43 = set41.difference(set42)
print(set43)

print("Exercise 5")
set51 = {10, 20, 30, 40, 50}
set52 = {10, 20, 30}
set51.difference_update(set52)
print(set51)

print("Exercise 5")
set61 = {10, 20, 30, 40, 50}
set62 = {30, 40, 50, 60, 70}
set63 = set61.symmetric_difference(set62)
print(set63)
