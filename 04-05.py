product = 1
for i in range(6):
    num = int(input("Введите целое число: "))
    if num != 0:
        product *= num
print("Произведение введенных чисел без учета нулей:", product)