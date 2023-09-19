def calculate_cost(message):
    cost_per_symbol = 0.40
    total_cost = len(message) * cost_per_symbol
    return total_cost

message = input("Введите ваше сообщение: ")
cost = calculate_cost(message)
print(cost, " руб.")
print(int(cost * 100 % 100), " коп.")