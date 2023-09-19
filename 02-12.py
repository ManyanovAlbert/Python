message = input("Введите ваше сообщение: ")
cost = 0.4
total_cost = len(message) * cost
rubley = int(total_cost)
copeek = int(total_cost * 100 % 100)
print(rubley,'руб',copeek,'коп')
