import random
print( "\tДобро пожаловать в игру 'Отгадай число'!")
print("\033[33m {}" .format("\nЯ загадал натуральное число из диапазона от 1 до 100."))
print("\033[33m {}" .format("Постарайтесь отгадать его за 8 попыток."))
print("\033[34m {}" .format("Если проиграешь буду ругаться!!!!!\n"))
# начальные значения
the_number = random.randint(1,100)
guess = int(input("Baшe предположение: "))
tries = 7

# цикл отгадывания
while guess != the_number:
    if guess > the_number and tries > 0:
        print("Меньше...")
        print("Осталось попыток:", tries)
        guess = int(input("Ваше предположение:"))
        tries -= 1
    elif guess < the_number and tries > 0:
        print("Больше...")
        print("Осталось попыток:", tries)
        guess = int(input("Ваше предположение:"))
        tries -= 1
    else:
        break
if tries != 0:
    print("Baм удалось отгадать число! Зто в самом деле", the_number)
    print("Bы затратили на отгадывание всего лишь ", 6 - tries, " попыток!\n")
else:
    print("\033[31m {}".format("Владик Ты Еблан"))