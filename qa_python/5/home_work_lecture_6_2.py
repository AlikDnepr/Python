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
    return text.lower().replace(",", "").split()

"""вывести в консоль самое часто встречаемое слово в файле, и сколько раз оно встречается"""
def max_word(text_lst):

    return
"""вывести в консоль самое редко встречаемое слово в файле, и сколько раз оно встречается"""
def min_word(text_lst):

    return

def replace(text_list, max_word, min_word):
    return [word if word != max_word else min_word for word in text_list]

def join_by_ten(text_list):
    new_text = []
    for i, word in enumerate(text_list):
        new_text.append(word)
        if i % 10 == 0 and i != 0:
            new_text.append("\n")
    return new_text

def write_to_file(file_path, text_list):
    try:
        with open(file_path, "a") as file:
            return file.writelines(text_list)
    except FileNotFoundError:
        with open(file_path, "w") as file:
            return file.writelines(text_list)


def main():
    """
    Это ваша главная функция, определите в ней всю лолгику скрипта и используйте другие функции которые определите ВЫШЕ
    """
    file_path = input("filename")
    text = read_from_file(file_path)
    if not text:
        print('File not found')
        return
    cleaned_text = clean_text(text)
    word_min = min_word(cleaned_text)


if __name__ == "__main__":
    """
    Эта конструкция гарантирует что файл будет исполнен только когда запущен на прямую
    """
    main()
