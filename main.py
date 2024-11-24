search_string = input("Введите строку для поиска: ") # запрашиваем строку для поиска

with open("text.txt", "r", encoding="utf-8") as file: # открываем файл в режиме чтения с кодировкой
    lines = file.readlines() # считываем все строки файла в список

found_lines = [line.strip() for line in lines if search_string in line] # находим строки с помощью генератора списков

print(f"Количество найденных строк: {len(found_lines)}") # выводим количество найденных строк
print("Найденные строки: ") # выводим
for found_line in found_lines: # перебираем строки списка найденных строк
    print(found_line) # выводим

found_lines.sort(key=len) # сортируем найденные строки по длине
print("Строки, отсортированные по длине: ") # выводим заголовок
for found_line in found_lines: # выводим отсортированные строки
    print(found_line)
