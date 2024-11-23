stroka = input("Введите строку для поиска: ") # запрос на ввод

with open("text.txt", "r", encoding="utf-8") as file: # открываем файл в режиме чтения
    markers = file.readlines() # считываем в переменную ll

kolichestvo = 0 # инициализируем
list = [] # создаем пустой список
for marker in markers: # перебераем строки файла
    if stroka in marker: # если в нем есть наша введенная строка
        list.append(marker.strip()) # то добавляем ее в наш список mm через пробел
        kolichestvo += 1 # и считаем количество

print("Найденные строки:") # выводим строки
for m in list: # элементы списка 
    print(m) # выводятся

list.sort(key=len) #сортируем по длине

print(f"Количество одинаковых строк: {kolichestvo}") # выводим количество
