example = frozenset()  # Только такая форма записи
print(example)
example = frozenset([1, 2])
print(example)

example = frozenset({1, 2, 5, 8, "a", None})
print(example)
example = frozenset({1, 2, 1, 5, 5, 8, "a", None})
print(example)  # frozenset({1, 2, 5, 8, "a", None})


# print(example[0])  # rice TypeError exception

# len()
print(len(example))

# in
val = "a"
example = frozenset({1, 2, 5, 8, "a", None})
print(val in example)

# ==
example = frozenset({1, 2, 5, 8, "a", None})
example_2 = frozenset({1, 2, 5, 8, "a", None})
print(example == example_2)  # True
print(example is example_2)  # False
example_2 = example
print(example is example_2)  # True

# .union()
example = frozenset({1, 2, 5, 8, "a", None})
example_2 = frozenset({1, 2, "5", 8, "b", "10"})
example_3 =  example.union(example_2)
print(example)
print(example_2)
print(example_3)

# .intersection()
example = frozenset({1, 2, 5, 8, "a", None})
example_2 = frozenset({1, 2, "5", 8, "b", "10"})
example_3 = example.intersection(example_2)
print(example_3)

# .difference()
example = frozenset({1, 2, 5, 8, "a", None})
example_2 = frozenset({1, 2, "5", 8, "b", "10"})
example_3 = example.difference(example_2)
print(example_3)

# .issubset()
example = frozenset({1, 2, 5})
example_2 = frozenset({1, 2, "5", 8, 5, "b", "10"})
example_3 = example.issubset(example_2)
print(example_3)

# min() max()

a = frozenset({8, -11, 4, 2, -5})
print(max(a))
print(max(a, key=abs))


example = [1, 2, 1, "long string", 8, 5, 9, "a", "b", "long string"]
print(example)
example = set(example)
print(example)