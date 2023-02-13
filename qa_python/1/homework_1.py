print("Task 1163")
watermelons = 600
print("""Инициализировали переменную watermelons со значением 600 (арбузов).
    watermelons = 600""")
first_day = watermelons / 6
print("""Инициализировали переменную first_day в которой определили количесво оставшихся арбузов,
 после продажи в первый день. 
    first_day = watermelons / 6 """)
second_day = watermelons - first_day * 2 - 27
print("""Инициализировали переменную second_day в которой расчитываем количество арбузов проданных за 2 дня:
    second_day = watermelons - first_day * 2 - 27, в нашем случае в этой переменной будет находитсья ответ, 
на поставленную задачу.""")
print("После коночания продаж осталось", int(second_day), "арбуза.\n")


print("Task 1166")
linen = 244
print("""Инициализировали переменную linen со значением 244.
    linen = 244""")
seeds = linen / 2
print("""Инициализировали переменную seeds в которой расчитаем количесво кг семян получившихся из 244 кг льна
    seeds = linen / 2, соответственно это и будет ответом.""")
print("Получили", int(seeds), "кг семян льна.\n")

print("Task 1168")
coal = 9
print("""Инициализировали переменную coal со значением 9.
    coal = 9 """)
day = 72  # days
print("""Инициализировали переменную day со значением 72.
    day = 72 """)
coal_amount = day * coal
print("""Инициализировали переменную coal_amount в которой расчитываем изначальное количество угля.
    coal_amount = day * coal """)
days_amount = coal_amount / 8
print("""Инициализировали переменную days_amount в которой расчитываем количество дней, в случае затрат 8 кг в день
    days_amount = coal_amount / 8 """)
print("Если тратить по 8 кг угля в день, то угля хватит на", int(days_amount), "день\n")

print("Task 1169")
acorns_count = 300
print("""Инициализировали переменную acorns_count со значением 300.
    acorns_count = 300 """)
two_kg = acorns_count * 2
print("""Инициализировали переменную two_kg в вычисляем количесвто желудей в 2 кг.
    two_kg = acorns_count * 2 """)
seedling_count = two_kg - (two_kg / 10)
print("""Инициализировали переменную seedling_count в которой вычисляем количесвто взошедших желудей.
    seedling_count = two_kg - (two_kg / 10), соответственно это и будет ответом. """)
print("Взошло", int(seedling_count), "саженца дуба\n")

print("Task 1172")
briar = 322  # kg
print("""Инициализировали переменную briar со значением 322.
    briar = 322 """)
dry_fruits = briar / 2
print("""Инициализировали переменную dry_fruits в которой вычисляем вес сухих фруктов.
    dry_fruits = briar / 2 , соответственно это и будет ответом. """)
print("После сушки вышло",int(dry_fruits), "кг сухого шиповника.")