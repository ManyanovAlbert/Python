while True:
    password1 = input("Введите пароль: ")
    password2 = input("Подтвердите пароль: ")

    if len(password1) < 8:
        print("Короткий!")
    elif "123" in password1:
        print("Простой!")
    elif password1 != password2:
        print("Различаются.")
    else:
        print("OK")
        break