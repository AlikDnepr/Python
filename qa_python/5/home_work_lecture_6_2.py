"""спрашивать у пользователя путь к читаемому файлу
открыть файл по этому пути
если файл не существует - предотвратить ошибку и напечатать пользователю что ошибка была предотвращена,
 файл не существует и остановить работу скрипта"""


def read_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError as i:
        print("File not found, program stopped")
        raise i


def clean_text(text):
    return sorted(text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").split())


def max_word(cleaned_text):
    c = sorted(cleaned_text, key=cleaned_text.count)
    return c[-1]


def min_word(cleaned_text):
    c = sorted(cleaned_text, key=cleaned_text.count)
    return c[0]


def replace(text_list, max_word, min_word):
    return [word if word != max_word else min_word for word in text_list]


def replace_spaces_with_paragraphs(text):
    words = text.replace("\n", "").split(" ")
    result = ""
    for i, word in enumerate(words):
        if (i + 1) % 10 == 0:
            result += f"{word}\n"
        else:
            result += word
        if i != len(words) - 1:
            result += " "
    result = result.replace(" \n", "\n").replace("\n ", "\n")  # Удаление пробела перед второй и последующими строками
    return result.strip()


def write_to_file(join_by_ten):
    try:
        with open("new file.txt", "x") as file:
            return file.writelines(join_by_ten)
    except FileExistsError:
        user_input = input("Файл уже существует перезаписать? Возможные ответы Y/N: ")
        if user_input.lower() == "y":
            with open("new file.txt", "w") as file:
                return file.writelines(join_by_ten)
        else:
            print("Файл не перезаписан")
    except FileNotFoundError:
        with open("new file.txt", "w") as file:
            return file.writelines(join_by_ten)


def main():
    """
    Это ваша главная функция, определите в ней всю лолгику скрипта и используйте другие функции которые определите ВЫШЕ
    """
    file_path = input("filename:")
    text = read_from_file(file_path)
    if not text:
        print('File not found')
        return

    cleaned_text = clean_text(text)
    word_min = min_word(cleaned_text)
    word_max = max_word(cleaned_text)
    replaced_text = text.replace(word_max, word_min, 14)
    new_text = replace_spaces_with_paragraphs(replaced_text)
    write_to_file(new_text)
    print(new_text)


"""/Users/oshlymeta.ua_1/PycharmProjects/PythonTesting/qa_python/5/example1.txt"""
if __name__ == "__main__":
    """
    Эта конструкция гарантирует что файл будет исполнен только когда запущен на прямую
    """
    main()
