days = 0
while True:
    temperature = float(input("Напишите нынешнее значение температуры: "))
    days += 1
    if temperature >= 22.0:
        break
weeks = days // 7
print(weeks,' полных недель')