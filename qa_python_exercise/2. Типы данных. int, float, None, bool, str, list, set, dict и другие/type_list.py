lst = list()
print(lst)
lst = []
print(lst)

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(len(lst))

print(lst[0])
print(lst[-1])
print(lst[5])
print(lst[9])
# print(lst[10])  # rice IndexError exception
print(lst[:5])
print(lst[5:])
print(lst[:-1])
print(lst[:-11])  # ""
print(lst[-3:])
print(lst[::2])
print(lst[::100])

var = "5"

print(var in lst)
print(5 in lst)

# .append()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lst)
lst.append("10")
print(lst)


# .insert()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lst)
lst.insert(2, "1.5")
print(lst)


# .extend()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lst)
lst.extend([10, 11, 12])
print(lst)


# .pop()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(3))
print(lst)

# .remove()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lst)
lst.remove("5")
print(lst)


# .count()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '5', '4']
print(lst.count('-1'))
print(lst.count('1'))
print(lst.count('5'))


# .clear()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lst)
lst.clear()
print(lst)


# .copy()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lst_2 = lst.copy()
print(lst)
print(lst_2)
lst.pop()
print(lst)
print(lst_2)


# .reverse()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lst)
lst.reverse()
print(lst)


# .sort()
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lst.reverse()
print(lst)
lst.sort()
print(lst)



# min() max()

a = [8, -11, 4, 2, -5]
print(max(a))
print(max(a, key=abs))
