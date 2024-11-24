search_string = input("Введите строку для поиска: ")  # запрос на ввод строки для поиска

with open("text.txt", "r") as file:  # открываем файл в режиме чтения
    lines = file.readlines()  # считываем все строки файла в список

count_found = 0  # переменная для количества строк
found_lines = []  # пустой список для хранения найденных строк

for line in lines:  # перебираем строки из файла
    if search_string in line:  # проверка, есть ли введенная строка в файле
        found_lines.append(line.strip())  # добавляем найденную строку в список, убирая лишние пробелы
        count_found += 1  # увеличиваем счетчик найденных строк

print("Найденные строки:")  # выводим
for found_line in found_lines:  # перебираем строки списка найденных строк
    print(found_line)  # выводим

found_lines.sort(key=len)  # сортируем найденные строки по длине

print(f"Количество найденных строк: {count_found}")  # выводим
