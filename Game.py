number = int(input("Число человека: "))
low = 1
high = 1000
computer_answer = 50
if number > 0 and number < 1000:
    while number != computer_answer:
        if number > computer_answer:
            print("Меньше...")
            low = computer_answer
            computer_answer = (low + high) // 2
        elif number < computer_answer:
            print("Больше...")
            high = computer_answer
            computer_answer = (low + high) // 2
        else:
            print("Error")
    print("Загаданное число:", computer_answer)
else:
    print("Некорректное число")


