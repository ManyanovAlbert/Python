n = int(input("Введите количество строк с данными: "))
lines = []
for i in range(n):
    line = input("Введите строку данных {}: ".format(i + 1))
    lines.append(line)
poisk_line = input("Введите поисковую строку: ")
print("Результат поиска:")
for line in lines:
    if poisk_line in line:
        print(line)
