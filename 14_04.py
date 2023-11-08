def who_are_you_and_hello():
    while True:
        name = input()
        if name.isalpha() and name.istitle():
            print(f"Привет, {name}!")
            break
        else:
            name = input()

who_are_you_and_hello()