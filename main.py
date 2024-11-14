with open("text.txt", "r") as file:
    l = file.readlines()

a = input("Введите строку для поиска: ")

dver = []
for i in l:
    if a in i:
        dver.append(i.strip())
    
dver.sort(key=len)

print(f"Найденные строки: {len(dver)}")
for i in dver:
    print(i)
