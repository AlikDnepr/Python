example = set()  # Только такая форма записи
print(example)
example = set([1, 2, 3])
print(example)
example = {1}  # Или фигурные скобки с элементами
print(example)

example = {1, 2, 5, 8, "a", None}
print(example)
example = {1, 2, 1, 5, 5, 8, "a", None}
print(example)  # {1, 2, 5, 8, "a", None}


# print(example[0])  # rice TypeError exception

# len()
print(len(example))

# in
val = "a"
example = {1, 2, 5, 8, "a", None}
print(val in example)

# ==
example = {1, 2, 5, 8, "a", None}
example_2 = {1, 2, 5, 8, "a", None}
print(example == example_2)  # True
print(example is example_2)  # False
example_2 = example
print(example is example_2)  # True

# .add
example = {1, 2, 5, 8, "a", None}
example.add(1)
print(example)
example.add(3)
print(example)

# .pop()
example = {1, 2, 5, 8, "a", None}
example.pop()
print(example)
# example.pop(1)  # rice TypeError exception

# .remove()
example = {1, 2, 5, 8, "a", None}
print(example)
example.remove(5)
print(example)
# example.remove(10)  # rice KeyError

# .discard()
example = {1, 2, 5, 8, "a", None}
print(example)
example.discard(5)
print(example)
example.discard(10)
print(example)

# .union()
example = {1, 2, 5, 8, "a", None}
example_2 = {1, 2, "5", 8, "b", "10"}
example_3 =  example.union(example_2)
print(example)
print(example_2)
print(example_3)

# .intersection()
example = {1, 2, 5, 8, "a", None}
example_2 = {1, 2, "5", 8, "b", "10"}
example_3 = example.intersection(example_2)
print(example_3)
# .intersection_update()
example = {1, 2, 5, 8, "a", None}
example_2 = {1, 2, "5", 8, "b", "10"}
print(example)
example.intersection_update(example_2)
print(example)

# .difference()
example = {1, 2, 5, 8, "a", None}
example_2 = {1, 2, "5", 8, "b", "10"}
example_3 = example.difference(example_2)
print(example_3)
# .difference_update()
example = {1, 2, 5, 8, "a", None}
example_2 = {1, 2, "5", 8, "b", "10"}
print(example)
example.difference_update(example_2)
print(example)

# .issubset()
example = {1, 2, 5}
example_2 = {1, 2, "5", 8, 5, "b", "10"}
example_3 = example.issubset(example_2)
print(example_3)


# .clear()
example = {1, 2, 5, 8, "a", None}
print(example)
example.clear()
print(example)


# .copy()
example = {1, 2, 5, 8, "a", None}
example_2 = example.copy()
print(example)
print(example_2)
example.pop()
print(example)
print(example_2)

# min() max()

a = {8, -11, 4, 2, -5}
print(max(a))
print(max(a, key=abs))


example = [1, 2, 1, "long string", 8, 5, 9, "a", "b", "long string"]
print(example)
example = set(example)
print(example)