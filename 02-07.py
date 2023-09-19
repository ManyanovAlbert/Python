number = float(input("Введите дробное число: "))
if abs(number) < 0.000001:
    print("Миллион")
else:
    inverse_number = 1 / number
    print("Обратное число:", inverse_number)