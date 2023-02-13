print("Exercise 1")
aTuple = (10, 20, 30, 40, 50)
aTuple = tuple(reversed(aTuple))
print(aTuple)

print("Exercise 2")
aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple
print(a)  # should print 10
print(b)  # should print 20
print(c)  # should print 30
print(d)  # should print 40

print("Exercise 3")
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

print("Exercise 4")
e = (50,)
print(e)

print("Exercise 5")
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

print("Exercise 6")
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = (tuple1[3], tuple1[4])
print("tuple2: ", tuple2)

print("Exercise 7")
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print("tuple1: ", tuple1)

print("Exercise 8")
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
