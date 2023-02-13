def read_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError as i:
        print("File not found, program stopped")
        raise i

read_from_file("/Users/oshlymeta.ua_1/Downloads/home_work_lecture_6_21.py")