print("Exercise 1")

text_input = input("Пользовательский ввод: ")
rep_count = text_input.count("bad")  # пришлось делать так, так как если ввести 'good bad', то он посчитает это как 2
text_input = text_input.replace("bad", "good")
print(text_input)
print("Было произведено:", rep_count, "замен(ы)")

"""Не очень понятно, что такое 'в не измененном пользовательском вводе', 
очень странная формулировка как по мне. Заменить что-то в не измененном  """

print("Exercise 2")

variable = False and True or True and not False or not True and True or not False and False
variable2 = (((False and True) or (True and not False)) or ((not True and True) or (not False and False)))
print(variable)
print(variable2)


print("Exercise 3")

roster = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15, 0, "last variable"]
print(roster[-1])
print(roster[len(roster) - 1])

print("Exercise 4")

example = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15, 0, "last variable"]
slice_start = int(input("Enter slicing start: "))
slice_end = int(input("Enter slicing end: "))
slice_step = int(input("Enter slicing step: "))
print(example[slice_start:slice_end:slice_step])

print("Exercise 5")

example_list = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, "last variable", "last variable", "last variable", 0, 3, 3, 3]
example_list = list(set(example_list))
print(example_list)

print("Exercise 5")

user_input1 = input("Первый пользовательский вводи: ")
user_input2 = input("Второй пользовательский ввод: ")
variable1 = set(user_input1.split())
variable2 = set(user_input2.split())
common_values = list(variable1.intersection(variable2))
print("Одинаковые значения в двух вводах: ")
for i in common_values:
    print(i, end=" ")

print("Exercise 7")

input_sequence = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 12, -11, -12, -13, -14, -15, 24, 0]  # можно менять
complete_sequence = range(min(input_sequence), max(input_sequence) + 1)
print(list(set(complete_sequence) - set(input_sequence)))

print("Exercise 8")

dictionary = {}
dictionary.update({"name": input("Enter your name: "), "age": input("Enter your age: ")})
dictionary.update({"films": input("Enter your favorite films: ").split(",")})
print(dictionary)
print(dictionary.keys())
dictionary.update({input("What element do you want to change?Enter Key: "): input("What value do you want to assign:")})
print(dictionary)
key = input("Enter a key that may be in the dictionary: ")
error = input("What to display if there is no value in the dictionary?: ")
print(dictionary.get(key, error))
