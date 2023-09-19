count = int(input("Количество изначальных монет: "))
while count >= 8:
    count //= 8
print(count)