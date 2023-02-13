tpl = tuple()
print(tpl)
tpl = ()
print(tpl)

tpl = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

print(len(tpl))

print(tpl[0])
print(tpl[-1])
print(tpl[5])
print(tpl[9])
# print(tpl[10])  # rice IndexError exception
print(tpl[:5])
print(tpl[5:])
print(tpl[:-1])
print(tpl[:-11])  # []
print(tpl[-3:])
print(tpl[::2])
print(tpl[::100])

var = "5"

print(var in tpl)
print(5 in tpl)


# .count()
tpl = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '5', '4')
print(tpl.count('-1'))
print(tpl.count('1'))
print(tpl.count('5'))


# .index()
tpl = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '5', '4')
# print(tpl.index('-1'))  # rice Value exception
print(tpl.index('1'))
print(tpl.index('5'))



# min() max()

a = (8, -11, 4, 2, -5)
print(max(a))
print(max(a, key=abs))
