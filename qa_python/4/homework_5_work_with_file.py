try:

    with open("../../../../Desktop/example.txt") as file:
        text = file.read().replace(".", "").replace("!", "").replace("?", "").replace(",", "").lower()
        list_of_all_words = text.split()
        uniques = {}
        for word in list_of_all_words:
            if word not in uniques:
                uniques.update({word: 0})

        while len(list_of_all_words) != 0:
            for word in uniques:
                if word in list_of_all_words:
                    counter = uniques[word]
                    uniques[word] = counter+1
                    list_of_all_words.remove(word)

        most_frequent_word = "word"
        counter = 0
        for each in uniques:
            if counter <= uniques[each]:
                most_frequent_word = each
                counter = uniques[each]
        print("Cамое часто встречаемое слово в файле:", most_frequent_word, "\n Слово встретилось:", counter)

        # находим в дикшенари самое маленькое значение
        less_frequent_word = "word"
        counter_less = counter
        for each in uniques:
            if counter_less >= uniques[each]:
                less_frequent_word = each
                counter_less = uniques[each]
        print("Cамое редко встречаемое слово в файле:", less_frequent_word, "\n Слово встретилось:", counter_less)

except FileNotFoundError as i:
    print("File not found, program stopped")
    raise i

try:
    with open("example.txt", "r") as example:
        with open("spam.txt", "w") as spam:
            for line in example:
                spam.write(line.replace(".", "").replace("!", "").replace("?", "").replace(",", "").lower().replace(most_frequent_word, less_frequent_word))
            print(text)
            example.close()
            spam.close()
except FileNotFoundError as i:
    print("File not found, program stopped")
    raise i
