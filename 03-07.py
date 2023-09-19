low = 1
high = 1000
middle = (low + high) // 2
tries = 0

while True:
    print("Попытка:", middle)
    response = input("Введите >, < или =: ")

    if response == ">":
        low = middle + 1
    elif response == "<":
        high = middle - 1
    elif response == "=":
        print("Ура! Я угадал число!")
        break

    tries += 1
    if tries >= 10:
        print("Я исчерпал все попытки. Загаданное число:", middle)
        break

    middle = (low + high) // 2