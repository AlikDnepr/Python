print("Hello world")

a = 3
print(a)

print(type(a))
print("{},{}".format("asd", a))

values = [1, 2, "String", 4, 5]
print(values[1])
print(values[1:3])  # он возьмет второе с начала по индексу и 3 с конца по порядку
values.insert(3, "New item") # инсерт добавляет новое значение в айтем
print(values)
values.append("end") # Добаляет в конец
print(values)

values[2] = "RHUL" # заменяет элемент
print(values)
del values[3] # удаляет значение из списка
print(values)
del values
print(values)



name = input("Привет. Как тебя зовут? ")
a = "ках, первые буквы всех слов прописные, а остальныестрочные. Именно таков формат строк, которые возвращает метод"
print(name.upper())
print(name.lower())
print(name.replace("s","вот это"))
print(a.capitalize())
