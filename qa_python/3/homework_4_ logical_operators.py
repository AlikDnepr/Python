"""Задача 1"""

a = int(input("Пользовательский ввод: "))
if a % 2 == 0:
    val = 2
    print(f"multiple of {val}")
elif a % 3 == 0:
    val = 3
    print(f"multiple of {val}")
elif a % 5 == 0:
    val = 5
    print(f"multiple of {val}")
elif a % 7 == 0:
    val = 7
    print(f"multiple of {val}")
else:
    val = a
    print(f"multiple of {val}")

"""Задача 2"""

input_lists = []
stop = input("Введите стоп слово: ")
e = 0
c = 0
while True:
    if e < 30:
        inlet = input("Пользовательский ввод: ")
        if inlet.find(stop) != -1 and inlet != stop:
            b = inlet.replace(stop, "")
            input_lists.append(b)
            e += 1
        elif inlet != stop:
            input_lists.append(inlet)
            e += 1
        elif inlet == stop:
            if c < 5:
                e += 1  # Предполагаю, что ввод "стоп слова" это тоже итерация, одна из 30
                c += 1
                continue
            else:
                for i in input_lists:
                    print(i)
                break
    else:
        for i in input_lists:
            print(i)
        break

"""Задача 3"""


keys = list((input("Пользовательский ввоод: ")).split(" "))
values = list((input("Пользовательский ввоод: ")).split(" "))

#1 2 3 4 5 6 7
#Значени1 Значени2 Значени3 Значени4 Значени5 Значени6 Значени7

dic = {}
for i, j in enumerate(keys):
    dic[keys[i]] = values[i]
print(dic)

a = dict(zip(keys, values))
print(a)

"""Задача 4"""

print([(i - 1) ** 3 for i in list(range(int(input("Введите число: ")))) if (i - 1) % 3 == 0])

"""Задача 5"""

value_str = input("Пользовательский ввоод: ")
value_list = value_str.split()
if len(value_list) == 0:
    print("Empty")
elif value_list.count("5") >= 1:
    print("5" * value_str.count("5"))
elif len(value_list) == 1:
    print(int(value_list[0]) ** 2)
elif len(value_list) % 2 == 0:
    print(int(min(value_list)) * int(max(value_list)))
else:
    print(', '.join(map(str, set(value_list))))
    #  print(set(value_list)) #но тогда выведутся еще и скобки

"""Важно, есть 1 кейс, если мы вводим "5" и один элемент в списке, я предполагаю, что нужно выполнять 2 вывода """
"""я говорю про пункты: 
Если же в списке встречается хотя бы одна строка "5" - посчитайте количество символов "5" 
в пользовательском вводе (не в списке) и умножьте str("5") на это значение. Выведете получившуюся строку.
Если же в списке только одно значение - возведите его в квадрат предварительно переведя в int"""

"""Прмимер моего подхода к решению, но я не могу все доделать из-за Элса и множества условий"""

"""
value_str = input("Пользовательский ввоод: ")
value_list = value_str.split()
if len(value_list) == 0:
    print("Empty")
elif len(value_list) % 2 == 0:
    print(int(min(value_list)) * int(max(value_list)))
if len(value_list) == 1:    # интересный кейс с 1 значением "5" в списке,тогда нужно выводить 2 значения по условию
    print(int(value_list[0]) ** 2)  # из-за это пришлось писать через if 3 отдельных операции
if value_list.count("5") >= 1:
    print("5" * value_str.count("5"))
#else:
    print(str(set(value_list)))
"""
