import os
import shutil
import json
import csv

# Путь к папке с файлами
FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

# Функция для чтения CSV-файла
def read_csv(filename):
    filepath = os.path.join(FOLDER_PATH, filename)
    if not os.path.exists(filepath):
        print(f'Файл {filename} не найден!')
        return
    
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Функция для чтения JSON-файла
def read_json(filename):
    filepath = os.path.join(FOLDER_PATH, filename)
    if not os.path.exists(filepath):
        print(f'Файл {filename} не найден!')
        return
    
    with open(filepath, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        print(json.dumps(data, indent=4, ensure_ascii=False))

# Функция сортировки файлов по расширению
def sort_files():
    extensions = ['txt', 'csv', 'jpg', 'png', 'json']
    
    for ext in extensions:
        folder = os.path.join(FOLDER_PATH, ext)
        os.makedirs(folder, exist_ok=True)  # Создаем папку, если ее нет
        
        for file in os.listdir(FOLDER_PATH):
            if file.endswith(f".{ext}"):
                src = os.path.join(FOLDER_PATH, file)
                dest = os.path.join(folder, file)
                shutil.move(src, dest)  # Перемещаем файл
                print(f'Перемещен: {file} → {folder}/')

# Функция переименования файлов
def rename_files():
    for folder in os.listdir(FOLDER_PATH):
        folder_path = os.path.join(FOLDER_PATH, folder)
        if os.path.isdir(folder_path):  # Проверяем, что это папка
            for index, file in enumerate(os.listdir(folder_path), start=1):
                ext = file.split('.')[-1]
                new_name = f'{folder}_{index}.{ext}'
                src = os.path.join(folder_path, file)
                dest = os.path.join(folder_path, new_name)
                os.rename(src, dest)
                print(f'Переименован: {file} → {new_name}')

# Запуск программы
if __name__ == '__main__':
    print('\n Сортируем файлы...\n')
    sort_files()

    print('\n Переименовываем файлы...\n')
    rename_files()

    print('\n Читаем JSON и CSV (если есть)...\n')
    read_csv('csv/test3.csv')
    read_json('json/data.json')
    
    print('\n Готово!')