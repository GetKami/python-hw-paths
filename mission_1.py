import os


def get_files_list():
    migrations = "Migrations"
    file_expansion = ".sql"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    list_file = []
    for random_file in os.listdir(path=os.path.join(current_dir, "Migrations")):
        if file_expansion in random_file:
            list_file.append(random_file)
    return list_file


def find_files():
    list_file = get_files_list()
    while True:
        user_input = input("Введите строку:")
        file_list_search = []
        i = 0
        for files in list_file:
            with open(os.path.join("Migrations", files)) as file:
                if user_input in file.read():
                    print(files)
                    i += 1
                    file_list_search.append(files)
        print("Всего найдено файлов: {}".format(i))
        list_file = file_list_search


if __name__ == "__main__":
    find_files()