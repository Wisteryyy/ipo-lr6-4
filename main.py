with open("text.txt", "r") as file: # открываем файл в формате чтения
    l = file.readlines() #считываем и присваиваем l

a = input("Введите строку для поиска: ") # вводим строку для посика

dver = [] # создаем пустой спислк
for i in l: # перебераем строки в l
    if a in i: #если наша строка есть и в l
        dver.append(i) # то добавляем ее в список
    
dver.sort(key=len) #сортируем по длине

print(f"Найденные строки: {len(dver)}") #выводится количество
for i in dver: # и затем выводится каждая строка из списка
    print(i) #выводится
