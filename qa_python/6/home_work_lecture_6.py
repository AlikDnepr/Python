def is_even(x):
    return x % 2 == 0


assert is_even(1) is False
assert is_even(10) is True


def is_odd(x):
    return not is_even(x)


assert is_odd(2) is False
assert is_odd(11) is True


def custom_max(a, b):
    if a > b:
        return a
    return b


assert custom_max(1, 10) == max(1, 10)
assert custom_max(100, 10) == max(100, 10)


def multiply(*args, base=1):
    for i in args:
        base *= i
    return base


example_list = list(range(1, 10))

assert multiply(*example_list) == 362880
assert multiply(*example_list, base=2) == 725760


def reverse(a):
    return a[::-1]


assert reverse("") == ""
assert reverse("QWERqwer123!@#") == "#@!321rewqREWQ"


def upper_count(a):
    b = 0
    for i in a:
        if i.isupper():
            b += 1
    return b


assert upper_count("") == 0
assert upper_count("QWER qwer 123 !@#") == 4


def unique(a):
    """
    Принмает один аргумент, список
    Возвращает список уникальных элементов этого списка отсортированных от меньшего к большему
    """
    return sorted(list(set(a)))


assert unique([2, 2, 1, 5, 5, 2, 7]) == [1, 2, 5, 7]


def is_pangram(x):
    """
    Функция принимает один аргумент, строку
    Возвращает True если в строке хотя бы раз встречается каждая буква английского алфавита
    иначе возвращает False
    """
    all_letters = set("qwertyuiopasdfghjklzxcvbnm")
    x = set(x.lower().replace(" ", ""))
    return all_letters == x


assert is_pangram("The five boxing wizards jump quickly") is True
