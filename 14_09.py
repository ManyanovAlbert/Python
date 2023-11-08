def ask_password():
    password = "password"
    attempts = 3

    while attempts > 0:
        user_input = input("Введите свой пароль: ")
        if user_input == password:
            print("Пароль принят")
            return
        attempts -= 1

    print("Пароль не принят")
ask_password()