example = dict()
print(example)
example = {}
print(example)

example = {
    "name": "Bob",
    "age": 30,
    "is_married": True,
    "pets_names": ["Rex", "Popo"],
}
print(example)
print(example["name"])
print(example["pets_names"][1])

example["age"] = 31
print(example)

example["is_new"] = False
print(example)
# .pop()
print(example.pop("is_new"))
print(example)

# .get()
# example["NOT EXISTS"]  # rice KeyError exception
print(example.get("NOT EXISTS"))  # None
print(example.get("NOT EXISTS", "nothing"))  # "nothing"

print("name" in example)  # True
print("Bob" in example)  # False

# .items() .values() .keys()
print(example.items())  # tuples of key, value -> (key, value), (key, value)...
print(example.values())  # value, value, value...
print(example.keys())  # key, key, key...

print(len(example))


# .clear()
example_2 = {
    "a": 1,
    "b": 2,
}
print(example_2)
example_2.clear()
print(example_2)

# .copy()
example_2 = example
print(example == example_2)
print(example is example_2)
example_2 = example.copy()
print(example == example_2)
print(example is example_2)
example_2 = dict(example)
print(example == example_2)
print(example is example_2)

# .fromkeys()
# print(example.fromkeys(["name", "is_married"]))

# .update()
example.update({"new_key": "new_value", "example__": 123123})
print(example)