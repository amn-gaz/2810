import os

# Ввод пути и расширения
path = input("Введите путь к папке: ")
ext = input("Введите расширение файла (например: .txt, .py, .jpg): ")

# Проверяем существование папки
if not os.path.isdir(path):
    print("Указанная папка не найдена.")
else:
    print(f"Файлы с расширением {ext}:")
    for file in os.listdir(path):
        if file.endswith(ext):
            print(file)