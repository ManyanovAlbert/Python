import time #от себя добавил

n = int(input("Введите количество секунд до запуска: "))
if n < 0:
    print("Пуск")
else:
    for i in range(n, -1, -1):
        time.sleep(1) #от себя добавил
        print(f"Осталось секунд: {i}")
    print("Пуск")