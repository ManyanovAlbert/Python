temperature = float(input("Введите температуру в градусах Цельсия: "))

if temperature < 15.5:
    print("ХОЛОДНО")
elif temperature > 28:
    print("ЖАРКО")
else:
    print("НОРМАЛЬНО")